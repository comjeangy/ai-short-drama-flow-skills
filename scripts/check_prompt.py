#!/usr/bin/env python3
"""프롬프트 검수기 — 규칙을 지켰는지 기계로 확인한다.

    python3 check_prompt.py prompts/s01_sh01.md          # 파일 하나 (종류 자동 판별)
    python3 check_prompt.py prompts/                    # 폴더 전체 (하위까지)
    python3 check_prompt.py --text "..."                 # 문자열
    python3 check_prompt.py --type sheet 파일.md         # 종류 고정

종류: sheet(캐릭터 시트) · conti(콘티 4패널) · keyframe(키프레임) · scene(장면 영상)

검사 (prompt-anatomy.md · failure-atlas.md 기준)
  공통   비율 명시 · 화면 글자 금지 · 금지 세트 · 길이 2,000자 · 메타 기록(모델/해상도/크레딧)
  scene  5부 구조 · 타임코드 3비트 · 단일 샷 잠금 · 대사는 한국어 한 문장 · in Korean
  image  타입별 필수 문구 (4뷰 / 4패널 / 단일 프레임) · 스타일·조명 서술

종료코드: 0 = 통과, 1 = 실패.  ⚠️ 는 경고(실패로 세지 않는다).
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HANGUL = re.compile(r"[가-힣]")
COST_HINT = re.compile(r"(\d+)\s*크레딧|크레딧[^0-9\n]{0,14}(\d+)|(\d+)\s*credits?", re.I)

# 장면(scene) 5부 구조
PARTS = {
    "①샷": r"shot|close[- ]?up|medium|wide|static camera|camera (pushes|pulls|pans|follows)",
    "②스타일": r"style|tone|realistic|drama|cinematic",
    "③조명": r"light|sunlight|shadow|lit",
    "④장소": r"\[L\d\]|LOCATION:|market|shop|room|street|inside|behind",
    "⑤동작": r"\[\d+\s*-\s*\d+s\]|he |she |speaks|walks|turns|pulls|stops",
}

TYPES = {
    "sheet": {
        "name": "캐릭터 시트",
        "need": [
            (r"front view", "정면 뷰"),
            (r"three[- ]quarter", "3/4 뷰"),
            (r"side profile", "측면 뷰"),
            (r"back view", "후면 뷰"),
            (r"face close[- ]?up", "얼굴 클로즈업"),
            (r"reference sheet|turnaround", "시트 선언"),
        ],
        "extra": [(r"studio background|plain .{0,20}background", "단색 배경 지정"),
                  (r"identical ", "옷·머리 동일 명시")],
    },
    "conti": {
        "name": "콘티 4패널",
        "need": [
            (r"GENERATE THE STORYBOARD IMAGE NOW", "첫 줄 강제 지시"),
            (r"exactly 4\b.{0,40}panels", "패널 수 명시"),
            (r"2x2|2\u00d72", "2×2 배열"),
            (r"NO TEXT IN THE IMAGE", "글자 금지 강조"),
            (r"panel\s*1", "패널별 행동"),
        ],
        "extra": [(r"across all panels|across all four panels|consistent across|identical across", "패널 간 일관 지시")],
    },
    "keyframe": {
        "name": "키프레임 스틸",
        "need": [
            (r"single cinematic still frame", "단일 프레임 선언"),
            (r"eye level|medium shot|close[- ]?up", "샷 크기"),
            (r"\[L\d\]|LOCATION:", "장소 접미어"),
        ],
        "extra": [(r"light|sunlight", "조명 서술")],
    },
    "scene": {
        "name": "장면(영상)",
        "need": [
            (r"\[\d+\s*-\s*\d+s\]", "타임코드"),
            (r"no scene cuts", "단일 샷 잠금"),
            (r"\[L\d\]|LOCATION:|market|shop|room|street", "장소"),
        ],
        "extra": [(r"no text|글자 없음|no captions", "화면 글자 금지 문구")],
    },
}
IMAGE_TYPES = ("sheet", "conti", "keyframe")


def load(path: pathlib.Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```([^`]*?)```", raw, re.S)
    return (max(blocks, key=len).strip() if blocks else raw), raw


def guess_type(text: str) -> str:
    if re.search(r"GENERATE THE STORYBOARD IMAGE NOW|exactly 4\b.{0,40}panels", text, re.I | re.S):
        return "conti"
    if re.search(r"reference sheet|turnaround|four full[- ]body views|front view.*three[- ]quarter",
                 text, re.I | re.S):
        return "sheet"
    if re.search(r"single cinematic still frame", text, re.I):
        return "keyframe"
    return "scene"


def check(prompt: str, raw: str, kind: str) -> list[tuple[str, str, str]]:
    r: list[tuple[str, str, str]] = []
    low = prompt.lower()
    is_image = kind in IMAGE_TYPES

    def add(ok, item, msg_ok, msg_bad, warn=False):
        if ok:
            r.append(("OK", item, msg_ok))
        else:
            r.append(("WARN" if warn else "FAIL", item, msg_bad))

    # 1) 비율 — 영상·키프레임은 세로 필수, 시트·콘티는 비율을 명시하면 된다
    if kind in ("scene", "keyframe"):
        ratio = bool(re.search(r"9:16|vertical", low))
        add(ratio, "비율: 세로 필수",
            "9:16/vertical 있음",
            "9:16(또는 vertical) 이 없다 → 기본 16:9 로 나간다. 숏폼 영상은 세로다")
    else:
        ratio = bool(re.search(r"\d+\s*:\s*\d+|vertical|horizontal|portrait|landscape|square", low))
        add(ratio, "비율 명시",
            "비율이 명시됨",
            "비율(9:16 / 16:9 등)이 없다 → UI 비율이 안 먹으면 엉뚱한 비율로 나온다")

    # 공통 2) 화면 글자 금지
    add(bool(re.search(r"no text|no letters|no captions|no watermark|글자 없음|자막 없음", low)),
        "화면 글자 금지",
        "글자 금지 문구 있음",
        "No text overlay on screen. 이 없다 → 렌더된 한글이 깨진 채 나온다")

    # 공통 3) 금지 세트(같은 인물·옷) — 경고
    add(bool(re.search(r"same (person|face|hair|clothes)|identical|같은 인물|동일", low)),
        "금지 세트",
        "같은 인물·옷 유지 문구 있음",
        "Same person / identical 문구가 없다 (참조를 쓰면 대개 괜찮다)", warn=True)

    # 타입별
    add(kind in TYPES, "종류 판별", TYPES[kind]["name"], "종류를 알 수 없다 (--type 으로 지정)")
    if kind in TYPES:
        for pat, label in TYPES[kind]["need"]:
            if not re.search(pat, prompt, re.I | re.S):
                r.append(("FAIL", f"{TYPES[kind]['name']}: {label}", ""))
        for pat, label in TYPES[kind].get("extra", []):
            if not re.search(pat, prompt, re.I | re.S):
                r.append(("WARN", f"{TYPES[kind]['name']}: {label}", ""))

    # 장면 전용
    if kind == "scene":
        for k, pat in PARTS.items():
            if not re.search(pat, prompt, re.I):
                r.append(("FAIL", f"5부 {k}", ""))
        n = len(re.findall(r"\[\d+\s*-\s*\d+s\]", prompt))
        if n and n != 3:
            r.append(("WARN", "타임코드 비트 수", f"{n}개 — 10초는 3비트가 표준"))

    # 대사
    quoted = re.findall(r'"([^"]{2,})"', prompt)
    korean = [q for q in quoted if HANGUL.search(q)]
    latin = [q for q in quoted if not HANGUL.search(q) and re.search(r"[A-Za-z]{4}", q)]
    if is_image:
        if korean:
            r.append(("FAIL", "이미지에 대사", f"이미지 프롬프트에 대사 {korean[:1]} — 그림에는 대사를 넣지 않는다"))
    elif korean:
        add(bool(re.search(r"in korean|한국어", low)), "대사: in Korean",
            "'in Korean' 있음", "한국어 대사에 'in Korean' 이 없다")
        add(len(korean) <= 1, "대사: 한 문장",
            "한 문장", f"대사가 {len(korean)}개 → 10초에 안 들어간다")
        add(not latin, "대사: 한국어로 직접",
            "한국어로 씀", f"비한국어 대사 {latin[:2]} → 로마자는 발음이 무너진다")
    else:
        add(bool(re.search(r"no dialogue|no voiceover|무대사|대사 없음", low)), "대사 처리",
            "대사 없음 명시", "대사도 'no dialogue' 도 없다 → 없는 대사가 생길 수 있다")

    # 길이 (콘티는 구조상 길어진다)
    limit = 3200 if kind == "conti" else 2000
    if len(prompt) > limit:
        r.append(("WARN", "길이", f"{len(prompt)}자 — {limit:,}자 이하 권장"))

    # 메타 기록(프롬프트 파일)
    if raw != prompt:
        have = [k for k, pat in (("모델", r"\*\*모델\*\*|모델\s*[:：]"), ("해상도", r"해상도"),
                                 ("크레딧", r"크레딧")) if re.search(pat, raw)]
        if len(have) < 3:
            r.append(("WARN", "메타 기록", f"{have} 만 있음 — 모델 · 해상도/길이 · 크레딧을 적는다"))
        elif not COST_HINT.search(raw):
            r.append(("WARN", "메타: 크레딧", "숫자 크레딧이 없다"))
    return r


def report(label: str, res: list[tuple[str, str, str]], quiet=False) -> bool:
    fails = [x for x in res if x[0] == "FAIL"]
    warns = [x for x in res if x[0] == "WARN"]
    if not quiet:
        print(f"\n{'✅ 통과' if not fails else '❌ 실패'} — {label}  (실패 {len(fails)} · 경고 {len(warns)})")
    for st, item, msg in res:
        if st == "OK":
            continue
        print(f"   {'❌' if st == 'FAIL' else '⚠️ '} {item:28s} {msg}")
    return not fails


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="*", help="프롬프트 파일 또는 폴더 (여러 개 가능)")
    ap.add_argument("--text")
    ap.add_argument("--type", choices=list(TYPES) + ["auto"], default="auto")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--suffix", default="*.md", help="폴더 검사 시 패턴")
    a = ap.parse_args()

    targets: list[tuple[str, str, str]] = []
    if a.text:
        targets.append(("(--text)", a.text, a.text))
    elif a.path:
        for item in a.path:
            q = pathlib.Path(item)
            if q.is_dir():
                for f in sorted(q.rglob(a.suffix)):
                    pr, raw = load(f)
                    targets.append((str(f), pr, raw))
            else:
                pr, raw = load(q)
                targets.append((str(q), pr, raw))
        if not targets:
            print(f"검사할 파일이 없습니다: {' '.join(a.path)}")
            sys.exit(1)
    else:
        ap.error("path 또는 --text 가 필요합니다")

    ok = True
    for label, pr, raw in targets:
        kind = a.type if a.type != "auto" else guess_type(pr)
        ok &= report(label, check(pr, raw, kind), quiet=a.quiet)

    print(f"\n총 {len(targets)}건 — {'전부 통과' if ok else '실패 있음'}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

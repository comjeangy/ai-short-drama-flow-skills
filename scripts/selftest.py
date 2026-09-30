#!/usr/bin/env python3
"""스킬 패키지 자체 점검 — "이 저장소가 약속한 구조를 지켰는가".

    python3 selftest.py                  # dist/ 또는 저장소 안에서 자동 탐색
    python3 selftest.py --root <경로>    # 루트 지정

검사
  1) 스킬마다 SKILL.md + references/(5개 이상) + assets/(7종) 이 있는가
  2) SKILL.md frontmatter: name · description · version
  3) SKILL.md 안의 references/... 링크가 실제로 존재하는가 (깨진 링크 0)
  4) SKILL.md 가 '범위 선언'(프롬프트를 내어주는 도구, Flow 를 조작하지 않는다)을 담고 있는가
  5) 프롬프트 검수기(check_prompt.py)가 함께 있으면 예제 프롬프트를 통과시키는가

종료코드: 0 = 통과, 1 = 실패
"""
from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys

REQUIRED_ASSETS = [
    "project-card.json", "character-sheet.jsonl", "location-sheet.json",
    "conti-panel.jsonl", "shot.jsonl", "render-log.csv", "judgement.jsonl",
]
FRONT = re.compile(r"^---\s*\n(.*?)\n---", re.S)


def find_root(explicit: str | None) -> pathlib.Path:
    if explicit:
        return pathlib.Path(explicit).resolve()
    cwd = pathlib.Path.cwd()
    # 조립본(dist)이 있으면 그걸 먼저 본다 — 원본은 references/assets 를 _shared 에 두기 때문
    for c in [cwd / "dist", cwd / "skills/v1/dist", cwd, cwd / "skills", cwd.parent]:
        if (c / "drama-shots" / "SKILL.md").exists():
            return c
        if (c / "dist" / "drama-shots" / "SKILL.md").exists():
            return c / "dist"
    return cwd


def check_skill(d: pathlib.Path) -> list[str]:
    bad: list[str] = []
    skill = d / "SKILL.md"
    txt = skill.read_text(encoding="utf-8")

    fm = FRONT.search(txt)
    if not fm:
        bad.append("frontmatter 없음")
    else:
        for key in ("name:", "description:", "version:"):
            if key not in fm.group(1):
                bad.append(f"frontmatter 에 {key} 없음")
        m = re.search(r"name:\s*(\S+)", fm.group(1))
        if m and m.group(1) != d.name:
            bad.append(f"name({m.group(1)}) 과 폴더({d.name}) 불일치")

    refs = sorted((d / "references").glob("*.md")) if (d / "references").exists() else []
    if len(refs) < 5:
        bad.append(f"references 문서 {len(refs)}개 (5개 이상 필요)")

    # 모든 문서의 상대 링크·이미지 유효성 (링크를 쓴 문서 위치 기준)
    for md in sorted(d.rglob("*.md")):
        body = md.read_text(encoding="utf-8")
        for m in re.finditer(r"!?\[[^\]]*\]\(([^)\s]+)\)", body):
            tgt = m.group(1).split("#")[0].strip()
            if not tgt or tgt.startswith(("http://", "https://", "mailto:", "#", "..")):
                continue
            if not (md.parent / tgt).exists():
                bad.append(f"깨진 링크 ({md.relative_to(d)}): {tgt}")

    adir = d / "assets"
    have = {p.name for p in adir.glob("*")} if adir.exists() else set()
    miss = [a for a in REQUIRED_ASSETS if a not in have]
    if miss:
        bad.append(f"assets 누락: {', '.join(miss)}")

    # 범위 선언
    if not re.search(r"조작하지 않는다|산출물은 프롬프트", txt):
        bad.append("범위 선언 없음 (프롬프트를 내어주는 도구 · Flow 를 조작하지 않는다)")

    return bad


def run_prompt_checks(root: pathlib.Path, extra_dirs: list[str]) -> tuple[int, int]:
    """프롬프트 파일만 검사한다. 대상: --prompts 로 준 폴더 + 저장소의 prompts/ 와
    examples/ 중 실제 프롬프트 블록(9:16 포함)을 가진 파일."""
    checker = None
    for cand in [root / "scripts" / "check_prompt.py",
                 root.parent / "scripts" / "check_prompt.py",
                 root.parent.parent / "scripts" / "check_prompt.py",
                 root / "_shared" / "scripts" / "check_prompt.py",
                 root.parent / "_shared" / "scripts" / "check_prompt.py"]:
        if cand.exists():
            checker = cand
            break
    if not checker:
        return (-1, -1)

    targets: list[pathlib.Path] = []
    for d in extra_dirs:
        p = pathlib.Path(d)
        if p.exists():
            targets += sorted(p.rglob("*.md"))
    for cand in [root.parent / "examples", root.parent.parent / "examples",
                 root.parent.parent / "prompts"]:
        if cand.exists() and "examples" in str(cand):
            targets += sorted(cand.rglob("*.md"))
    targets = sorted(set(targets))

    ok = fail = skipped = 0
    for d in targets:
        body = d.read_text(encoding="utf-8")
        blocks = re.findall(r"```[a-z]*\n(.*?)```", body, re.S)
        if not blocks:
            skipped += 1
            continue
        prompt = max(blocks, key=len).strip()
        # 실제 프롬프트 블록만 (9:16 명시가 우리 관례)
        if len(prompt) < 200 or "9:16" not in prompt:
            skipped += 1
            continue
        r = subprocess.run([sys.executable, str(checker), "--text", prompt, "--quiet"],
                           capture_output=True, text=True)
        if r.returncode == 0:
            ok += 1
        else:
            fail += 1
            print(f"   ❌ {d}")
    if skipped:
        print(f"   (프롬프트 아님 {skipped}건 건너뜀)")
    return ok, fail


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root")
    ap.add_argument("--prompts", action="append", default=[],
                    help="프롬프트 폴더 (여러 번 지정 가능). 기본: ../prompts")
    a = ap.parse_args()
    root = find_root(a.root)
    print(f"점검 루트: {root}")

    dirs = list(a.prompts)
    if not dirs:
        for cand in [root.parent.parent / "prompts", root.parent / "prompts", root / "prompts"]:
            if cand.exists():
                dirs.append(str(cand))
                break

    skills = [p for p in sorted(root.iterdir()) if p.is_dir() and (p / "SKILL.md").exists()]
    if not skills:
        print("스킬을 찾지 못했습니다 (SKILL.md 없음)")
        sys.exit(1)

    failed = 0
    for d in skills:
        bad = check_skill(d)
        if bad:
            failed += 1
            print(f"\n❌ {d.name}")
            for b in bad:
                print(f"     - {b}")
        else:
            nrefs = len(list((d / 'references').glob('*.md')))
            print(f"✅ {d.name}  (참조 {nrefs} · 양식 7)")

    ok, fail = run_prompt_checks(root, dirs)
    if ok >= 0:
        print(f"\n프롬프트 검수: 통과 {ok} · 실패 {fail}")
        failed += fail

    print(f"\n{'전부 통과' if failed == 0 else f'실패 {failed}건'}")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()

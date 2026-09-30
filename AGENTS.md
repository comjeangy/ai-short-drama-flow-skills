# 에이전트용 안내

이 저장소의 스킬을 **AI 에이전트(Claude Code · Codex · Gemini Spark 등)가 실행할 때** 따르는 규칙.

## 절대 규칙

1. **Flow 화면을 조작하지 않는다.** 클릭·입력·`생성 시작` 대행 금지. 브라우저 자동화 금지.
2. **비용이 드는 일은 사용자 승인 후에만.** 모델 호출·생성·재실행·점검 전에 승인을 받는다.
   시스템은 추천할 수 있지만 **사용자 선택을 막아서는 안 된다** (차단·자동 대체·자동 교체 금지).
   추천 후보 + 전체 목록 + "그대로 실행" 경로를 항상 함께 제시한다.
3. **`항상 승인` 을 안내하지 않는다.** 승인 창에서는 `승인` 또는 `거부` 만.
4. 로그인·비밀번호·인증코드를 대신 입력하지 않는다.

## 언제 무엇을 읽는가

| 상황 | 읽을 것 |
|---|---|
| 항상 먼저 | `references/prompt-recipes.md` (색인) |
| 프롬프트를 쓰기 전 | `references/prompt-anatomy.md` |
| 1차시 (이야기) | `references/drama-craft.md` |
| 캐릭터·배경이 흔들릴 때 | `references/character-consistency.md` |
| 샷을 설계할 때 | `references/shot-grammar.md` · `lighting-and-style.md` |
| 영상 전 | `references/conti-and-keyframe.md` |
| 대사가 있을 때 | `references/korean-dialogue.md` |
| 결과를 고칠 때 | `references/editing-and-revision.md` |
| 안 나올 때 | `references/failure-atlas.md` |
| 비용이 걸릴 때 | `references/cost-and-safety.md` |
| 사용자가 붙일 때 | `references/flow-paste.md` (사람용) |

## 출력 형식 (항상 이 3개)

```
① 붙이는 곳 — 한 줄 (모델 · 비율 · 길이 · 참조 · 예상 크레딧)
② 프롬프트 전문 — 코드블록 하나로 통째로
③ 판정 한 줄 — 생성 후 무엇을 보고 승인/재시도할지
```

## 판정 기록

프롬프트 파일에 함께 적는다: **모델 · 해상도 · 길이 · 크레딧(숫자) · 결과(`승인`/`재시도`/`폐기`)**.
실패한 프롬프트도 지우지 않는다 — 실패 유형이 자산이다.

## 자기 점검

작업을 끝내기 전에:

```bash
python3 scripts/check_prompt.py <프롬프트 파일 또는 폴더>
python3 scripts/selftest.py .
```

검수기가 `❌` 를 내면 **고친 뒤에** 사용자에게 준다.

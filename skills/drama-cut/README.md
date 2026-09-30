# drama-cut (4차시)

**Use when a clip came out wrong: diagnose the cause, revise within 4 turns, or keep what works.**

나온 결과를 **진단**하고, 고칠지 다시 만들지 정하고, 쓸 만한 것은 **보존**한다.

| | |
|---|---|
| 입력 | 생성 결과(영상·이미지) + 무엇이 마음에 안 드는지 |
| 나오는 것 | 진단 · 수정 프롬프트 · 판정표(`assets/judgement.jsonl`) |
| 비용 | 수정은 4턴까지 · 넘기면 새로 생성(크레딧) |
| 다음 | 시리즈로 이어가기 |

## 진단 순서

```
1. 증상이 어느 단계인가?  (이미지 / 영상 / 편집 / 이야기)
2. 참조 자산이 붙어 있었나?  → 3. 필수 문구가 빠졌나?
4. 5부 구조·비트 수가 맞나?  → 5. 그래도 안 되면 이전 단계로 돌아간다
```

**3회 연속 방향이 틀렸으면 프롬프트 문제가 아니다.** 1~2차시로 돌아간다.

## 참조 문서

`references/editing-and-revision.md` · `failure-atlas.md` · `korean-dialogue.md` ·
`character-consistency.md` · `prompt-anatomy.md` · `cost-and-safety.md` · `flow-paste.md` · `prompt-recipes.md`

## 규칙

- **한 턴에 변수 하나** + `Keep everything else the same.`
- **4턴을 넘기지 않는다** — 넘길 것 같으면 이미지 단계로 돌아가 새로 만든다(0크레딧).
- 실패한 프롬프트도 지우지 않는다 — **실패 유형이 자산**이다.

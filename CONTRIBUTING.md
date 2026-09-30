# 기여 · 수정 안내

이 저장소는 강의 자료라서 **바꾸기 전에 원칙(DESIGN.md)을 확인**한다.

## 고치는 곳

| 무엇 | 어디 |
|---|---|
| 스킬 본문 | `skills/v1/<스킬>/SKILL.md` |
| 규칙 문서 | `skills/v1/_shared/references/*.md` |
| 양식 | `skills/v1/_shared/assets/*` |
| 저장소 문서 | `skills/v1/_shared/repo/*` |
| 예제 | `skills/v1/_shared/examples/*` |

`dist/`(zip)와 저장소의 `skills/` 는 **손으로 고치지 않는다.** `build.py`·`export_repo.py` 가 만든다.

## 절차

```bash
cd skills/v1
python3 build.py --no-install            # 조립
python3 _shared/scripts/selftest.py      # 구조 점검 (frontmatter·깨진 링크·양식 7종)
python3 _shared/scripts/check_prompt.py ../prompts/   # 프롬프트 검수
python3 build.py                         # 문제없으면 설치까지
```

그다음 저장소 동기화:

```bash
python3 tools/export_repo.py             # 조립 → skills/ → zip → commit (push 는 --push)
```

## 규칙

- **새 참조 문서를 만들면** 그 문서를 필요로 하는 스킬의 `build.py` 참조 목록에 넣는다.
  (한 곳에서만 정의하고, 스킬은 복사본을 받는다)
- **새 양식을 만들면** `_shared/assets/` 에 넣는다 → 전 스킬에 자동 동봉된다.
- **프롬프트를 추가하면** 검수기를 통과해야 한다. 통과 못 하면 프롬프트나 검수기 중 하나가 틀린 것이니
  둘 중 **맞는 쪽을 고친다** (`9:16` 누락처럼 검수기가 맞은 경우가 많다).
- **실측하지 않은 수치를 쓰지 않는다.** 크레딧·단가·UI 동작은 실측값과 측정 날짜를 함께 적는다.
- **자동화 스크립트를 스킬에 넣지 않는다.** Flow 조작은 설계 범위 밖이다(DESIGN.md §1).

## 커밋

- 한국어로 쓴다. 한 줄 요약 + 왜 바꿨는지.
- 커밋 정체성은 저장소 소유자(`comjeangy`)로 고정한다.

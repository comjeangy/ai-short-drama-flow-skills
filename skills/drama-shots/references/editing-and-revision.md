# 수정과 편집 — 4턴 안에 끝낸다

> 영상·이미지의 수정은 **이미 만든 것을 고치는 것**이다. 새로 만드는 것보다 싸지만, **턴이 쌓이면 무너진다.**

---

## 1. 규칙 4개

1. **한 번에 변수 하나** — 색·표정·구도·소품 중 **하나만**
2. **항상 `나머지는 그대로 유지해.` 를 붙인다** (얼굴·머리·자세·구도·배경·조명)
3. **4턴을 넘기지 않는다** — 5턴 근처부터 모션 저하·캐릭터 드리프트가 시작된다. 더 필요하면 **새로 생성**
4. **이미지 편집은 무료다** — 시트 환복·표정 변형은 몇 번을 해도 0크레딧

> Omni 공식: *"Overly lengthy descriptions can confuse the diffing engine."*
> 편집 엔진은 **바뀐 부분만** 찾는다. 길게 설명하면 엔진이 헷갈린다.

---

## 2. 좋은 편집 지시 / 나쁜 편집 지시

| | |
|---|---|
| ✅ | `코트 색을 붉은색으로 바꿔줘. 나머지는 그대로 유지해.` |
| ❌ | `붉은 코트를 입은 여자가 나오는 그 영상에서, 은색 코트를 붉은색으로 바꾸고 배경도 좀 밝게…` |

**문형**
```
[바꿀 것 하나] 를 [목표 상태] 로 바꿔줘. 나머지는 그대로 유지해.
```

---

## 3. 자주 쓰는 편집 (검증됨)

### 영상 수정 (P6)

| 목적 | 지시 |
|---|---|
| 대사 입모양 보정 | `Make the man's mouth match the Korean line exactly. Keep everything else the same.` |
| 표정 강화 | `Make her expression colder and sharper. Keep everything else the same.` |
| 소품 추가 | `Add a worn leather-strap watch on his left wrist. Keep everything else the same.` |
| 톤 고정 | `Keep the same lighting and colour as before. Keep everything else the same.` |

### 이미지 편집 (P4 · 0크레딧)

| 목적 | 지시 |
|---|---|
| 환복 | `Change only the clothing: …` (`character-consistency.md` §4) |
| 표정 변형 | `Change only the expression: …` |
| 배경 교체 | `Change only the background to …` |

---

## 4. 턴 관리

```
1턴 — 색·소품 하나
2턴 — 표정·구도 하나
3턴 — 대사 입모양
4턴 — 마지막 하나    ← 여기까지
   ↳ 5턴이 필요하면 → 이미지 단계로 돌아가 다시 만든다 (0크레딧)
```

**영상은 턴마다 크레딧이 든다.** 이미지로 돌아가는 것이 항상 싸다.

---

## 5. 판정 — 무엇을 보고 다시 만드나

`judgement.jsonl` 항목 (관찰 가능한 것만)

| 항목 | 통과 조건 |
|---|---|
| 샷 지시 준수 | 컷이 나뉘지 않았고, 구도가 프롬프트와 같다 |
| 얼굴 일관 | 시트와 같은 사람 |
| 의상 일관 | 옷·소품이 시트와 같다 |
| 화면 글자 없음 | 깨진 한글이 없다 |
| 대사 발음 | 들리는 문장이 프롬프트와 같다 |
| 비트 타이밍 | 3비트가 3·3·4초 안에 들어온다 |
| 소품 일관 | 시계·안경 등이 유지된다 |

**하나라도 실패면 재시도 사유를 적는다.** 실패도 지우지 않는다 — 실패 유형이 자산이다.

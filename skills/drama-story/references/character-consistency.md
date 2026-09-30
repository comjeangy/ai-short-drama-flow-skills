# 캐릭터 일관성 — 시트로 고정한다

> 시리즈에서 **얼굴·옷·소품**이 컷마다 달라지면 드라마가 아니다.
> 일관성은 "프롬프트를 잘 쓰는 것"이 아니라 **참조 자산을 만드는 것**으로 해결한다.

---

## 1. 원칙 — 참조가 없으면 모델이 발명한다

| 관찰 (실측 2026-09-29) | 원인 | 처방 |
|---|---|---|
| 컷마다 **옷 디테일이 달라진다** | 상반신 정면 1장에는 **뒷판·소매·등·벨트·신발 정보가 없다** → 모델이 발명 | **4뷰 시트**를 참조로 넣는다 |
| 배경이 매번 다른 시장 | 배경 참조 없음 | **장소 시트** + `@` |
| 2편째 얼굴이 다르다 | `금지변화` 누락 | 시트에 금지변화 줄 추가 |

**의상·소품은 얼굴보다 더 잘 유지된다.** 그래서 옷 정보를 넣는 것이 가장 값싼 개선이다.

---

## 2. 🔑 외형(P2)과 성격(P3)을 섞지 않는다

| | P2 (외형 → 시트) | P3 (성격) |
|---|---|---|
| 넣는 곳 | **프로젝트 프롬프트 상자 (이미지 모드)** | 캐릭터 상세 · **`캐릭터 정보`** |
| 무엇을 하는가 | **그림을 그린다** | **연기를 시킨다** (그림에 영향 없음) |
| 무엇을 쓰는가 | 나이·머리·옷·소품·배경 | 성격·말투·관계·상황 |

P2에 "성격이 밝은"을 써도 **표정은 바뀌지 않는다.**

---

## 3. 캐릭터 시트 = **4뷰 + 얼굴 클로즈업**

### 시트 1장 구성

```
정면 · 3/4 · 측면 · 후면  (전신, 같은 크기로 나란히)
+ 얼굴 클로즈업 1컷
같은 옷 / 같은 머리 / 단색 밝은 회색 배경 / 화면에 글자 없음
```

### P2 조립 공식 (v3 — 시트 기준)

```
{나이대/성별/국적}: {헤어}, {상의(무늬까지)}, {하의·신발}, {액세서리}, {얼굴 특징}

One single image: front view, three-quarter view, side profile and back view standing side by side
at the same scale, plus one face close-up.

Full body head to toe in the front, three-quarter, side and back views.
Identical {옷}, identical {머리}, identical {소품} in every view.
Neutral pose, arms relaxed at the sides, {표정}.
Plain flat light grey seamless studio background, even soft light, realistic photography.
No text, no letters, no numbers, no panel labels, no captions, no watermark.
```

### 공식 권장 4개 (v3 수정)

1. 단색 배경 ✅ 그대로
2. ~~상반신 정면~~ → **전신 4뷰(정면·3/4·측면·후면) + 얼굴 클로즈업**
3. 한 명만 ✅ 그대로
4. 나이·머리·옷 구체적으로 → **+ 무늬·액세서리까지**
   (`brown patterned blouse`, `thin metal-rimmed glasses`, `leather-strap metal watch`)

**시트는 `character-sheet.jsonl` 에 고정항목·금지변화와 함께 기록한다** (`assets/`).

---

## 4. 옷이 두 벌이면 **새로 만들지 않는다 — 편집 파생**

**새로 생성하면 다른 사람이 된다.** 시트를 연 편집기에서 **옷만** 바꾼다.

```
Change only the clothing: {새 옷}.
Keep everything else the same: the same face, the same wrinkles, the same hair, the same age and build,
the same neutral pose, the same four full-body views and the same face close-up at the same scale in the
same positions, the same plain light grey seamless studio background, the same even soft light,
the same camera framing.
No text, no letters, no numbers, no panel labels, no captions, no watermark.
```

**실측(2026-09-29)**: 만복 작업복 시트 → 편집 파생으로 **같은 얼굴 그대로** 남색 정장. **시계도 유지** ✓

표정 변형도 같은 방식(`Change only the expression: …`).

---

## 5. 장소 시트 — 사람 없는 빈 배경

```
Location plate, no people.
```

- 배경은 참조가 없으면 **매 생성마다 발명된다** → 컷마다 다른 시장이 나온다
- **앵글마다 1장** (정면·반대편·클로즈업 디테일)
- `@` 로 붙인다
- **글자 금지** — 간판·현수막·가격표·메뉴판

**장소 접미어 [L1]** — 모든 샷 프롬프트의 ④번 자리에 그대로 복사한다.

```
[L1] The counter side of a small noodle shop in a traditional Korean market at noon:
     a worn corrugated steel roller shutter, a scratched stainless counter, low stools,
     a faded grey-beige awning. Far behind, a red convertible out of focus.
```

---

## 6. 참조 붙이기 (실측)

```
프롬프트 상자에 `@` 입력 → 피커 → 왼쪽 `이미지` 탭 클릭 → 항목 클릭 → `프롬프트에 추가`
※ 기본이 `장면` 탭이면 `애셋이 없습니다` 로 비어 보인다 → `이미지` 로 바꾼다
※ 한 번에 하나씩. 다중 선택은 안 된다
```

⚠️ **썸네일이 깨져 보일 때가 있다 → 제목으로 구분한다.**
그래서 시트를 만들자마자 **이름을 붙인다** (`미영 시트` / `만복 시트` / `순자 시트`).
제목이 잘려서(`Woman character turnaround refer…`) **두 캐릭터가 같은 이름으로 보인다.**

---

## 7. 일관성 실패 처방

| 증상 | 원인 | 처방 |
|---|---|---|
| 옷 디테일이 컷마다 다르다 | 시트에 뒷면 정보 없음 | 4뷰 시트로 다시 (0크레딧) |
| 옷 무늬가 흔들린다 | 무늬를 글로만 씀 | 무늬 명시 + `character-sheet.jsonl` 금지변화에 추가 |
| 2벌인데 얼굴이 바뀐다 | 새로 생성했다 | **편집 파생**으로 |
| 배경이 매번 다르다 | 장소 시트를 안 붙였다 | `@` 로 L1 붙이기 |
| 3명 중 한 명만 다르다 | 그 인물만 참조를 안 붙였다 | 참조 3장 모두 붙인다 |
| 시트가 `@` 목록에 없다 | **이름을 안 붙였다** | 이름 붙이기 |

# 콘티와 키프레임 — 영상 전에 그림으로 승인받는다

> 순서: **콘티 4패널(승인) → 키프레임 스틸 1장 → `프레임 → 시작` → 영상**
> 이미지 단계는 **전부 0크레딧**(실측). 실패는 여기서 잡는다.

---

## 1. 왜 콘티를 먼저 만드는가

- 문장만으로 장면을 지시하면 **배경·행동·첫 구도가 매번 달라진다.**
- 그림으로 먼저 확정하면 **영상 크레딧을 쓰기 전에** 실패를 걸러낼 수 있다.
- 콘티는 **사람이 보는 승인 도구**다. AI는 만들고, 사람은 승인/반려한다.

## 2. 콘티 프롬프트 규칙 5개

1. 첫 줄 `GENERATE THE STORYBOARD IMAGE NOW.` — 설명문·계획·질문을 쓰지 못하게 막는다
2. **패널 수와 배열 명시** — 10초 4순간이면 `exactly 4 panels in one 2x2 storyboard contact sheet`
3. **패널별 행동 하나** — `PANEL 1: … PANEL 4: …`
4. **화면 글자 금지 강하게** — `panel labels, captions, subtitles, timecodes, logos, watermarks`
5. **참조(캐릭터 시트)를 `@` 로 붙이고** `Use every attached reference as the authoritative visual source`

### 템플릿 (실측 검증본)

```
GENERATE THE STORYBOARD IMAGE NOW.

Do not write a storyboard, scene breakdown, asset list, explanation, proposal, or follow-up question.

Create exactly 4 cinematic still-image panels arranged in one 2x2 storyboard contact sheet.
Do not create additional panels. Do not invent additional actions.

NO TEXT IN THE IMAGE: do not render any words, letters, numbers, panel labels, captions,
subtitles, timecodes, logos, or watermarks.

Use the attached character sheet as the authoritative reference for {인물1}: {정체성 한 줄}.
{인물2·3도 같은 형식 — 참조가 없으면 "no reference attached, keep them identical in every panel"}

LOCATION: {장소 접미어}. {단서 소품과 금지 사항}

Keep faces, clothing, body proportions, environment layout, lighting direction, props and physical
state consistent across all panels.

PANEL 1: {샷 크기}. {행동 + 표정 + 위치}
PANEL 2: …
PANEL 3: …
PANEL 4: …

Return only the completed storyboard contact sheet image.
```

**실측(2026-09-29)**: 4패널 2×2 동일 배경, 화면 글자 없음, 참조 시트와 인물 일관, 단서 소품(멀리 붉은 차) 반영 ✓

## 3. 콘티는 영상 입력으로 못 쓴다

영상 입력은 **이미지 1장**만 받는다. 콘택트시트(4칸)를 넣으면 칸이 그대로 영상에 나온다.
→ **승인된 패널 하나를 키프레임 스틸로 다시 뽑는다.**

## 4. 키프레임 스틸 (P8)

콘티의 **첫 패널(0초 상태)** 을 단일 프레임으로. 이미지 모드 · 0크레딧.

- 콘티 프롬프트에서 `4패널` 문장을 빼고 **`A single cinematic still frame, vertical 9:16`** 로 바꾼다
- **5부 순서를 그대로 유지**한다 (샷 → 스타일 → 조명 → 장소 → 인물·행동)
- **금지 세트를 그대로 붙인다**
- 결과를 **`프레임 → 시작`** 에 붙이면 **첫 구도·배경·의상이 영상까지 따라온다**

## 5. 시작 프레임을 쓴 장면 프롬프트

①번(샷)에 한 줄을 더한다:

```
Animate from the provided first frame.
```

그리고 나머지 5부는 **그대로** 쓴다. 순서를 바꾸지 않는다.

## 6. 붙이는 곳 (실측)

```
프롬프트바의 `동영상 · …` 칩 클릭 → `동영상` → `프레임` → `시작` 슬롯
   → 피커 `이미지` 탭 → 키프레임 스틸 선택
※ `종료` 슬롯도 있다 (가운데 swap_horiz 로 교체)
```

## 7. 판정 기준 (콘티 단계에서 볼 것)

| 항목 | 통과 조건 |
|---|---|
| 인물 일관 | 4패널에서 얼굴·옷·소품이 같다 |
| 배경 일관 | 4패널이 같은 장소·같은 빛 |
| 행동 | 패널마다 **다른** 행동 하나 (같은 동작 반복이면 실패) |
| 글자 | 화면에 글자·라벨·자막이 **없다** |
| 구도 | 0초 패널이 영상 첫 프레임으로 쓸 만하다 |

하나라도 실패면 **콘티를 다시 만든다 (0크레딧)**. 영상으로 넘어가지 않는다.

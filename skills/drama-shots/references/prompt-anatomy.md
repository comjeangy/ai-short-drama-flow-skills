# 프롬프트 해부 — 5부 구조와 필수 규칙

> 이 스킬의 산출물은 **프롬프트 텍스트**다. AI는 Flow 화면을 조작하지 않는다.
> 출처: Google Omni 공식 cookbook · Vertex AI 프롬프트 가이드 · 중국 실무 방법론 · **2026-09-29/30 라이브 실측**

---

## 1. 프롬프트 9종 — AI가 언제 무엇을 내어주는가

| # | 이름 | 언제 | 내용 |
|---|---|---|---|
| P1 | 기획 | 1차시 | 대화로 정한 것 정리 (**Flow에 안 넣는다**) |
| **P2** | 외형 → **캐릭터 시트** | 2차시 | 4뷰+얼굴 시트 (`character-consistency.md`) |
| **P3** | 성격 | 2차시 | `캐릭터 정보` — **그림에 영향 없음**, 연기에 영향 |
| P4 | 고치기·환복 | 2차시 | 시트 **편집 파생** (한 번에 변수 하나) |
| **P7** | 콘티 | 3차시 | 4패널 2×2 콘택트시트 — **승인용** (`conti-and-keyframe.md`) |
| **P8** | 키프레임 | 3차시 | 단일 스틸 1장 → **시작 프레임** |
| **P5** | 장면 | 3차시 | 타임코드 3비트 + 대사 + 스타일 + 금지 세트 |
| **P6** | 수정 | 4차시 | 짧고 외과적인 편집 지시 (`editing-and-revision.md`) |
| — | 장소 시트 | 2차시 | 사람 없는 빈 배경 `Location plate, no people.` |

### 🔴 AI가 하는 것 / 하지 않는 것

| 한다 | 하지 않는다 |
|---|---|
| 재료를 캐내 **프롬프트를 완성해 내어준다** | **Flow 화면을 조작하지 않는다** (클릭·입력·생성 대행) |
| **붙일 위치**를 한 줄로 알려준다 | 브라우저 자동화·UI 스크립트를 쓰지 않는다 |
| 통째로 복사할 코드블록으로 준다 | 조각을 흩어 주고 "알아서 조립하세요" 하지 않는다 |
| 결과를 듣고 **원인을 진단**해 다음 프롬프트를 고친다 | `승인`·`생성 시작`을 대신 누르지 않는다 |
| 판단 기준을 준다 | 계정 등급·UI 상태를 검증·추정하지 않는다 |

### 출력 형식 (항상 이 3개)

```
1) 붙이는 곳: 한 줄 — 예) 📝 프로젝트 상자 · 동영상 모드 · 프레임 → 시작(키프레임)
2) 프롬프트 전문: 코드블록 하나 (그대로 복사해 붙이면 끝)
3) 판정: 무엇을 보면 성공 / 언제 재시도인지 한 줄
```

---

## 2. 5부 공식 — **순서가 곧 가중치**

```
① 샷 구성 / 카메라 움직임      ← 가장 강하다
② 스타일
③ 조명
④ 장소 (+ 장소 접미어 [L1])
⑤ 동작 / 대사 / 꼬리말(금지 세트)  ← 가장 약하다
```

> 구글 Cloud 가이드: *"describe the shot in your prompt like a director would describe the first shot of a movie to the cinematographer."*

**순서를 깨지 않는다.** 시작 프레임용 한 줄(`Animate from the provided first frame.`)은 **①에 붙이고** 나머지 순서는 그대로 둔다.

**필수 4줄** (모든 프롬프트에 자동으로 붙는다)

```
In a single unbroken scene, no scene cuts.          ← 대사가 있으면 특히 필수
9:16 vertical.
No text overlay on screen. No captions, no watermark.
Same person, same clothes colors, same hair, same face.
```

---

## 3. 타임코드 3비트 — 10초를 쪼개는 유일한 방법

```
[0-3s] …
[3-6s] …
[6-10s] …
```

- **없으면** 모델이 마음대로 늘어놓는다. **있으면** "무엇을"뿐 아니라 **"언제"**를 안다.
- 10초에 **3비트**. 4개 이상 넣으면 아무것도 안 남는다.
- 비트마다 **동작 하나**. 표정 변화는 같은 비트에 붙여도 된다.

---

## 4. 단일 샷 잠금 — **대사 샷에는 반드시**

> Omni 공식: *"By default, Omni may introduce multi-shot cinematic cuts to build narrative dynamism."*

```
In a single unbroken scene, no scene cuts.
한국어: 한 번의 연속된 장면, 장면 전환 없음.
```

- 대사 샷에 안 넣으면 **컷이 나뉘면서 입모양·화자 배분이 무너진다.**
- 컷을 **일부러** 나눠 리듬을 주고 싶을 때만 안 쓴다 (선택).

---

## 5. 배제는 자연어로 — **네거티브 필드가 없다**

> Omni 공식: 시스템 지시·temperature·stop 시퀀스·**부정 프롬프트 파라미터 전부 미지원**

```
No dialogue or voiceover.
No text overlay on screen.
```
한국어: `대사 없음, 내레이션 없음.` / `자막 없음, 화면에 글자 없음.`

### 🔴 한국어 제작에서 `화면에 글자 없음`은 타협 불가

**`No lettering` 만으로는 부족하다** (실측 2026-09-30 · 야경 장소 시트):
야경에서 모델은 **불 켜진 상가 간판**을 자연스럽게 넣는다. 글자를 금지해도 광원은 남는다.

| | |
|---|---|
| ❌ | `No people. No lettering of any kind.` → **네온 상가 간판이 그대로 들어옴** |
| ✅ | `No lettering and no illuminated signs: all shopfronts dark and unlit.` |
| ✅ | 광원을 한정한다: `All light comes from the street lamps and the wet asphalt reflections.` |

**원리**: 글자를 빼려면 **글자가 있는 물건(간판)을 빼야** 한다.
빛나는 판을 남겨두면 거기에 글자가 그려진다. 발광 패널은 `matte, not backlit` 로 막는다.

Omni의 "텍스트 렌더링" 강점은 **라틴 문자 기준**이다. 독립 검증에서 **CJK 렌더링이 붕괴**했다
(히라가나 46자 중 11자만 읽힘, 한자는 획이 무너짐). **한글은 자모 조합이라 더 위험하다.**

→ 간판·서류·휴대폰 화면·자막은 **전부 후반 합성**.
→ **이미지(시트·콘티·키프레임)에도 글자를 넣지 않는다.** 라벨이 들어가면 그 그림이 영상으로 간다.

---

## 6. 금지 세트 — 꼬리말에 **항상**

중국 실무: "가장 자주 누락되고, 편차를 줄이는 가장 값싼 장치".

```
영어: No text overlay on screen. No Korean text, no signboards with letters, no captions, no watermark.
      No car badges, no license plates.
      Same person, same clothes colors, same hair, same face.
한국어: 자막 없음, 화면에 글자 없음, 워터마크 없음.
        같은 인물, 옷 색 유지, 머리 모양 유지, 얼굴 유지.
```

- **이미지 프롬프트에도 똑같이 붙인다.**
- 차·로고는 **브랜드명을 쓰지 않고 형태로**: `a bright red low-slung classic convertible, no badges, no license plate`

---

## 7. 길이와 충돌

| 규칙 | 이유 |
|---|---|
| **짧고 구체적으로** | 길수록 좋은 게 아니다. 중국 실무 상한: 한 샷 2,000자 |
| **서로 충돌하는 지시 금지** | `고정 카메라` + `빠른 회전` 을 같이 쓰면 실패율 급등 |
| **한 프롬프트에 일 하나** | 지시 5개를 한꺼번에 넣으면 다 흐려진다 |

---

## 8. 검증된 예시 (2026-09-29, 한국어 대사 발음 확인됨)

```
A shallow-depth medium shot, the camera pushes in slowly. 9:16 vertical.
In a single unbroken scene, no scene cuts.

A realistic Korean drama tone, harsh white midday sunlight, high contrast, cold reflections off
grey concrete and stainless steel, murky teal shadows, shallow depth of field.

The counter side of a small noodle shop in a traditional Korean market at noon: a worn corrugated
steel roller shutter, a scratched stainless counter, low stools, a faded grey-beige awning.

The woman speaks first, sneering and sharp, in Korean, fast delivery:
"다 먹었는데 맛이 없네요, 이 나이 먹고 장사 그렇게 하세요?"

[0-3s] She slams the empty bowl down on the counter. He smiles faintly, then his smile stops.
[3-6s] Without a word he unties the white apron and lays it on the counter.
[6-10s] He pulls the shutter cord. The steel shutter rolls down.

Market ambience, clattering bowls, a low tense music bed.
No dialogue except the single Korean line above. No voiceover.
No text overlay on screen. No Korean text, no signboards with letters, no captions, no watermark.
No car badges, no license plates.
Same person, same clothes colors, same hair, same face.
```

→ 구조: ①샷(+9:16·잠금) ②스타일+③조명 ④장소(+[L1]) ⑤대사 → 동작 3비트 → 꼬리말

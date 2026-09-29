# 프롬프트 작성 규칙 — AI가 프롬프트를 쓸 때 지키는 것

> **프롬프트는 이 스킬의 산출물이다.** 사용자가 쓰는 게 아니라 **AI가 써 준다.**
> 사용자는 복사해서 Flow에 붙여넣기만 한다.
>
> 출처: Google Omni 공식 cookbook + Vertex AI 프롬프트 가이드 + 중국 실무 프롬프트 방법론
> + **2026-09-29/30 라이브 실측(이미지 0크레딧 · 뷰 시트 · 콘티 · 편집 파생)**

---

## 0. 프롬프트 9종 — AI가 언제 무엇을 써 주는가

| # | 이름 | 언제 | AI가 쓰는 것 |
|---|---|---|---|
| P1 | 기획 | 1차시 | 대화로 정한 것을 정리한 기획 카드 (Flow에 안 넣는다) |
| **P2** | **외형 → 캐릭터 시트** | 2차시 | **4뷰+얼굴 시트 프롬프트** (§2-b) |
| **P3** | **성격** | 2차시 | 캐릭터 정보 — **그림에 영향 없음**. 에이전트가 장면에 반영 |
| P4 | 고치기·환복 | 2차시 | 시트에서 **편집 파생** (한 번에 변수 하나, §2-c) |
| **P7** | **콘티** | 3차시 | **4패널 2x2 콘택트시트** (§1-b) — 승인용 |
| **P8** | **키프레임** | 3차시 | **단일 스틸 1장** → 시작 프레임 (§1-c) |
| **P5** | **장면** | 3차시 | 타임코드 3비트 + 대사 + 스타일 + 금지 세트 |
| **P6** | **수정** | 4차시 | 짧고 외과적인 편집 지시 (한 번에 변수 하나) |
| — | 장소 시트 | 2차시 | 사람 없는 빈 배경 (§2-d) |

**사용자가 프롬프트를 직접 쓰게 만들지 않는다.** 대화로 재료를 받아 AI가 조립한다.

### 🔴 이 스킬의 산출물은 **프롬프트 텍스트**다 — Flow 조작 도구가 아니다

| AI가 **한다** | AI가 **하지 않는다** |
|---|---|
| 재료를 캐내고 **프롬프트를 완성해서 내어준다** | **Flow 화면을 조작하지 않는다** — 클릭·입력·생성 대행 없음 |
| **붙일 위치**를 한 줄로 알려준다 | 브라우저 자동화·UI 스크립트를 쓰지 않는다 |
| 프롬프트를 **통째로 복사할 수 있는 코드블록**으로 준다 | 조각을 흩어 주고 "알아서 조립하세요" 하지 않는다 |
| 결과를 듣고 **원인을 진단**해 다음 프롬프트를 고친다 | `승인`·`생성 시작`을 대신 누르지 않는다 |
| 판단 기준을 준다 | 계정 등급·UI 상태를 검증·추정하지 않는다 |

**프롬프트를 내어줄 때의 출력 형식 (항상 이 3개)**

```
1) 붙이는 곳: 한 줄 — 예) 📝 프로젝트 상자 · 동영상 모드 · 프레임 → 시작(키프레임)
2) 프롬프트 전문: ``` 로 감싼 코드블록 하나 (그대로 복사해 붙이면 끝)
3) 판정: 무엇을 보면 성공 / 언제 재시도인지 한 줄
```

**사용자는 붙여넣기만 한다.** 붙이는 절차는 `flow-paste.md`(사람용 부록)에 있다.

---

## 1. 5부 공식 — **순서가 곧 가중치**

Google 공식 가이드의 순서. 뒤로 갈수록 영향이 약해진다.

```
① 샷 구성 / 카메라 움직임
② 스타일
③ 조명
④ 장소
⑤ 동작 (그리고 대사)
```

> 구글 Cloud 가이드 원문: *"If this guide could be condensed into one sentence: describe the shot in your prompt like a director would describe the first shot of a movie to the cinematographer."*

**5부 구조를 깨면 안 된다.** 시작 프레임용 한 줄(`Animate from the provided first frame.`)을 넣을 때도
**①(샷)에 붙이고 나머지 순서는 그대로 둔다.**

---

## 1-b. 콘티(스토리보드 콘택트시트) — **P7 · 승인용 4패널**

**왜 만드는가**: 문장만으로 장면을 지시하면 **배경·행동이 매번 달라진다.**
그림으로 먼저 확정하면 **영상 크레딧을 쓰기 전에** 실패를 걸러낼 수 있다. 이미지 생성은 **0크레딧**이다.

**규칙 5개**
1. 첫 줄에 **`GENERATE THE STORYBOARD IMAGE NOW.`** — 설명문·계획·질문을 쓰지 못하게 막는다
2. **패널 수와 배열을 명시**한다 — 10초·4순간이면 `exactly 4 panels in one 2x2 storyboard contact sheet`
3. **패널별로 행동 하나씩** — `PANEL 1: … PANEL 4: …`
4. **화면 글자 금지**를 강하게 (`panel labels, captions, subtitles, timecodes, logos, watermarks`)
5. **참조(캐릭터 시트)를 `@` 로 붙이고**, `Use every attached reference as the authoritative visual source` 를 넣는다

**템플릿 (실측 검증본 — 영문 본문, 대사 없음)**

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

**콘티는 승인 전용이다.** 영상 입력은 **이미지 1장**만 받으므로, 승인된 패널을 §1-c로 다시 뽑는다.

---

## 1-c. 키프레임 스틸 — **P8 · 시작 프레임이 되는 그림**

콘티의 **첫 패널(0초 상태)** 을 **단일 프레임**으로 다시 뽑는다. 이미지 모드 · 0크레딧.

- 콘티 프롬프트에서 `4패널` 문장을 빼고 **`A single cinematic still frame, vertical 9:16`** 으로 바꾼다
- **5부 순서를 그대로 유지**한다 (샷 → 스타일 → 조명 → 장소 → 인물·행동)
- **금지 세트를 그대로 붙인다** (글자·엠블럼·번호판)
- 결과를 **`프레임 → 시작`** 에 붙이면 **첫 구도·배경·의상이 영상까지 따라온다**

**시작 프레임을 쓴 장면 프롬프트**에는 ①에 한 줄을 더한다:
`Animate from the provided first frame.` — 그리고 나머지 5부는 그대로 쓴다.

---

## 2. 🔑 외형(P2)과 성격(P3)을 **절대 섞지 않는다**

| | P2 (외형 → 시트) | P3 (성격) |
|---|---|---|
| 넣는 곳 | **프로젝트 프롬프트 상자 (이미지 모드)** | 캐릭터 상세 · **`캐릭터 정보`** |
| 무엇을 하는가 | **그림을 그린다** | **연기를 시킨다** (그림에 영향 없음) |
| 무엇을 쓰는가 | 나이·머리·옷·소품·배경 | 성격·말투·관계·상황 |

P2에 "성격이 밝은"을 써도 **표정은 바뀌지 않는다.** 성격은 P3이다.

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

### §2-b. 왜 "상반신 정면 1장"이 아니라 **4뷰 시트**인가

**실측 근거 (2026-09-29)**: 상반신 정면 1장에는 **뒷판·소매·등·벨트·신발 정보가 없다**
→ 모델이 그 부분을 **발명**한다 → **컷마다 옷 디테일이 달라진다.**
4뷰 시트를 참조로 넣으면 샷이 바뀌어도 **옷·머리·소품이 유지**됐다.

**의상과 소품은 얼굴보다 더 잘 유지된다.** 그래서 옷 정보를 넣어 주는 것이 가장 값싼 개선이다.

**공식 권장 4개 (v3 수정)**
1. 단색 배경 ✅ 그대로
2. ~~상반신 정면~~ → **전신 4뷰(정면·3/4·측면·후면) + 얼굴 클로즈업**
3. 한 명만 ✅ 그대로
4. 나이·머리·옷 구체적으로 → **+ 무늬·액세서리까지**
   (`brown patterned blouse`, `thin metal-rimmed glasses`, `leather-strap metal watch`)

### §2-c. 옷이 두 벌이면 **새로 만들지 않는다 — 편집 파생**

**새로 생성하면 다른 사람이 된다.** 시트를 연 편집기에서 **옷만** 바꾼다.

```
Change only the clothing: {새 옷}.
Keep everything else the same: the same face, the same wrinkles, the same hair, the same age and build,
the same neutral pose, the same four full-body views and the same face close-up at the same scale in the
same positions, the same plain light grey seamless studio background, the same even soft light,
the same camera framing.
No text, no letters, no numbers, no panel labels, no captions, no watermark.
```

실측(2026-09-29): 만복 작업복 시트 → 편집 파생으로 **같은 얼굴 그대로** 남색 정장. 시계도 유지.

### §2-d. 장소 시트 — 사람 없는 빈 배경 (캐릭터와 같은 구조)

배경은 참조가 없으면 **매 생성마다 발명된다** → 컷마다 다른 시장이 나온다.
`Location plate, no people.` 로 시작하고, **앵글마다 1장** 만들고, `@` 로 붙인다.
글자 금지(간판·현수막·가격표)를 반드시 넣는다.

---

## 3. 타임코드 3비트 — 10초를 쪼개는 유일한 방법

구글 Omni 공식: 자연어 타이밍 또는 **브래킷 타임코드**.

```
[0-3s] …
[3-6s] …
[6-10s] …
```

**없으면** 모델이 마음대로 늘어놓는다. **있으면** "무엇을"뿐 아니라 **"언제"**를 안다.

10초에 **3비트**. 4개 이상 넣으면 아무것도 안 남는다.

---

## 4. 단일 샷 잠금 — **대사 샷에는 반드시**

> Omni 공식 cookbook: *"By default, Omni may introduce multi-shot cinematic cuts to build narrative dynamism."*

```
In a single unbroken scene, ... no scene cuts.
한국어로: 한 번의 연속된 장면, 장면 전환 없음.
```

**대사가 있는 샷은 반드시 잠근다** — 안 잠그면 컷이 나뉘면서 **입모양·화자 배분이 무너진다.**

반대로 컷을 나눠서 리듬을 주고 싶으면 **일부러 안 쓴다**. 이건 선택이다.

---

## 5. 배제는 자연어로 — **네거티브 필드가 없다**

> Omni 공식: 시스템 지시·temperature·stop 시퀀스·**부정 프롬프트 파라미터 전부 미지원.**

```
No dialogue or voiceover.
No text overlay on screen.
```
한국어로: `대사 없음, 내레이션 없음.` / `자막 없음, 화면에 글자 없음.`

### 🔴 한국어 제작에서는 `화면에 글자 없음`이 필수다

Omni의 "텍스트 렌더링" 강점은 **라틴 문자 기준**이다.
독립 검증에서 **CJK 렌더링이 심하게 깨졌다** (히라가나 46자 중 11자만 읽힘, 한자는 획이 무너짐).
**한글은 자모 조합이라 더 위험하다.**

→ 카메라에 들어오는 한국어 텍스트(간판·서류·휴대폰·자막)는 **전부 후반 합성**으로 처리한다.
→ **이미지(시트·콘티·키프레임)에도 글자를 넣지 않는다.** 라벨을 넣으면 그림이 망가지고, 그 그림이 영상으로 간다.

---

## 6. 한국어 대사 — 실측으로 동작 확인됨

**2026-09-29 실측**: 프롬프트의 대사가 **그 문장 그대로** 발음됐다.

```
프롬프트: 수아가 낮게 말한다: "여기서 뭐 하는 거예요?"
결과 오디오 전사: [3.89-5.89] 여기서 뭐 하는 거예요?   (언어판정 ko, 확률 1.0)
```

**대사 문형**
```
[이름]가 [말투] 말한다: "[한국어 문장]"
```

| 규칙 | 이유 |
|---|---|
| **한국어로 그대로 쓴다** | 로마자로 쓰면 발음이 무너진다 |
| **한 문장만** | 10초에 두 마디는 안 들어간다 |
| **말투를 붙인다** (`낮게`, `조용히`, `화내며`) | 그대로 연기가 된다 |
| **대사는 프롬프트 앞쪽**에 | 뒤에 있으면 장식으로 취급된다 |
| 대사가 없으면 | `대사 없음, 내레이션 없음.` |

> **지시문 언어**: 한국어 지시문은 실측으로 검증됐다(위 전사).
> 영어 지시문 판본은 **미검증**이다 — 쓰려면 **같은 장면으로 A/B 비교**한 뒤 정한다.
> **한 프롬프트에 지시문 언어를 섞지 않는다**(대사만 한국어).

---

## 7. 금지 세트 — 꼬리말에 **항상** 붙인다

중국 실무에서 "가장 자주 누락되고, 편차를 줄이는 가장 값싼 장치".

```
한국어: 자막 없음, 화면에 글자 없음, 워터마크 없음.
        같은 인물, 옷 색 유지, 머리 모양 유지, 얼굴 유지.
영어:   No text overlay on screen. No Korean text, no signboards with letters, no captions, no watermark.
        No car badges, no license plates.
        Same person, same clothes colors, same hair, same face.
```

이 줄들이 **매 프롬프트에 자동으로 붙는다** — 이미지 프롬프트에도 똑같이 붙인다.
(차 엠블럼·번호판은 **브랜드명을 쓰지 않고** 형태로 쓴다: `a bright red low-slung classic convertible, no badges, no license plate`)

---

## 8. 프롬프트 길이와 충돌

| 규칙 | 이유 |
|---|---|
| **짧고 구체적으로** | 길수록 좋은 게 아니다. 중국 실무 상한: 한 샷 2,000자 |
| **서로 충돌하는 지시 금지** | `고정 카메라` + `빠른 회전` 같이 넣으면 실패율이 급등 |
| **한 프롬프트에 일 하나** | 지시 5개를 한 번에 넣으면 다 흐려진다 |

---

## 9. 편집(수정) 프롬프트 규칙 — P6 · P4

> Omni 공식: *"Overly lengthy descriptions can confuse the diffing engine."*

| | |
|---|---|
| ✅ | `코트 색을 붉은색으로 바꿔줘. 나머지는 그대로 유지해.` |
| ❌ | `붉은 코트를 입은 여자가 나오는 그 영상에서, 은색 코트를 붉은색으로 바꾸고...` |

**규칙 4개**
1. **한 번에 변수 하나**
2. **항상 `나머지는 그대로 유지해.` 를 붙인다** (얼굴·머리·자세·구도·배경·조명)
3. **4턴을 넘기지 않는다** — 5턴 근처부터 모션 저하·캐릭터 드리프트가 시작된다. 더 필요하면 **새로 생성**한다
4. **편집은 무료다(이미지 한정)** — 시트 환복·표정 변형은 몇 번을 해도 0크레딧

---

## 10. 실패 유형 → 처방 (AI가 진단할 때 쓰는 표)

| 증상 | 진짜 원인 | 처방 |
|---|---|---|
| 장면이 3번 바뀐다 | 단일 샷 잠금 누락 | `한 번의 연속된 장면, 장면 전환 없음.` |
| 영상에 글자가 깨진다 | 배제 문구 누락 | `자막 없음, 화면에 글자 없음.` |
| **옷 디테일이 컷마다 달라진다** | 상반신 정면 1장 참조 (뒷면 정보 없음) | **4뷰 시트로 다시** (§2-b, 0크레딧) |
| **배경·행동이 상상과 다르다** | 문장만으로 지시 | **콘티를 먼저** (§1-b, 0크레딧) |
| **첫 컷 구도가 매번 다르다** | 시작 프레임 없음 | 키프레임 스틸을 `프레임 → 시작` 에 (§1-c) |
| 2벌인데 얼굴이 달라진다 | 새로 생성했다 | **편집 파생** (§2-c) |
| 2편째 얼굴이 달라진다 | `금지변화` 누락 | 시트에 금지변화 줄 추가 |
| 성격을 넣었는데 표정이 그대로 | P2에 썼다 | 성격을 P3(`캐릭터 정보`)으로 옮긴다 |
| 10초가 늘어진다 | 비트가 2개 이하 | 3비트 타임코드로 다시 |
| 10초에 아무것도 안 남는다 | 비트가 4개 이상 | 하나를 빼고 그 하나를 길게 |
| 갈등이 안 보인다 | 일상으로 시작 | 개막 공식(극단 상황 + 반상식)으로 |
| 대사가 안 들린다 | 대사가 여러 개 / 로마자 | 한 문장, 한국어 그대로 |
| 움직임이 뭉개진다 | 4턴 초과 편집 | 새로 생성한다 |
| 3회 연속 방향이 틀렸다 | **프롬프트 문제가 아니다** | **1~2차시로 돌아간다** (이야기·콘티를 고친다) |

---

## 11. 이미지 단계가 먼저다 — **비용 원칙**

| 단계 | 비용 | 그래서 |
|---|---|---|
| 시트·로케이션·콘티·키프레임 | **0** | **몇 번을 다시 뽑아도 0원.** 여기서 최대한 고생한다 |
| 영상 | 360p 7 / 720p 15 | 승인된 그림으로 **한 번에** 간다 |

**실패는 이미지 단계에서 잡는다.** 영상에서 처음 알게 되면 그때부터 재생성 비용이 붙는다.

# 샷 문법 — 크기·앵글·무빙 사전

> 프롬프트 ①번 자리에 쓰는 어휘. **영어로 쓰고, 한글로 의도를 확인한다.**
> 같은 뜻의 단어를 섞어 쓰면 모델이 흔들린다 — **한 프로젝트 안에서 표기를 고정한다.**

---

## 1. 샷 크기 (Shot size)

| 한글 | 영어 (권장 표기) | 무엇이 보이나 | 어디에 쓰나 |
|---|---|---|---|
| 익스트림 클로즈업 | `extreme close-up` | 눈·입·손끝 | 감정의 폭발 직전, 소품 강조 |
| 클로즈업 | `close-up` | 얼굴 전체 | 감정, 대사 반응 |
| 미디엄 클로즈업 | `medium close-up` | 가슴 위 | **대사 샷 기본값** |
| 미디엄 | `medium shot` | 허리 위 | 행동 + 표정 동시 |
| 미디엄 와이드 | `medium wide shot` | 무릎 위 | 인물 + 주변 맥락 |
| 와이드 | `wide shot` | 전신 + 공간 | 장소 소개, 고립감 |
| 익스트림 와이드 | `extreme wide shot` | 공간이 인물보다 큼 | 시작·끝, 압도 |

**10초 대사 샷은 미디엄 또는 미디엄 클로즈업이 안전하다.** 와이드는 입모양이 안 보여 대사 검증이 어렵다.

---

## 2. 앵글 (Angle)

| 한글 | 영어 | 효과 |
|---|---|---|
| 눈높이 | `eye level` | 중립. 기본값 |
| 살짝 아래에서 | `slightly low angle` | 상대가 위압적으로 |
| 아래에서 | `low angle` | 권력·위협 |
| 살짝 위에서 | `slightly high angle` | 약자·관찰 |
| 위에서 | `high angle / bird's eye` | 무력감·객관 |
| 어깨 너머 | `over-the-shoulder` | 대화 관계 |
| 등 뒤에서 | `from behind` | 인물의 시점으로 유도 |

---

## 3. 카메라 무빙 (Camera movement) — **한 샷에 하나만**

| 한글 | 영어 | 주의 |
|---|---|---|
| 고정 | `static camera` | 기본. 움직임은 인물이 만든다 |
| 천천히 밀어 넣기 | `the camera pushes in very slowly` | 감정 고조. **가장 자주 쓰는 무빙** |
| 천천히 빼기 | `the camera pulls back slowly` | 이탈·종결 |
| 좌우 이동 | `the camera pans left/right` | 공간 훑기 |
| 따라가기 | `the camera follows …` | 인물 이동 |
| 손에 든 느낌 | `handheld, subtle shake` | 불안·다큐멘터리 |
| 돌리기 | `the camera orbits around …` | **대사 샷엔 쓰지 않는다** |

🔴 **충돌 조합 금지**: `static camera` + `fast zoom`, `push in` + `pan` — 실패율이 급등한다.
🔴 **10초에서 무빙 2개 이상은 금지.** 하나를 고르고 그 하나만 천천히.

---

## 4. 10초 비트 설계 — 무빙과 비트를 묶는다

| 비트 | 시간 | 샷·무빙 | 내용 |
|---|---|---|---|
| 1 | 0–3초 | 미디엄 · 고정 | 상황 제시 (무엇이 잘못됐나) |
| 2 | 3–6초 | 미디엄 · 아주 천천히 밀어 넣기 | 반응 (표정이 바뀐다) |
| 3 | 6–10초 | 미디엄 와이드 · 고정 | 결정적 행동 (문을 닫는다, 돌아선다) |

- **무빙은 2번 비트에만** 넣는 것이 가장 안전하다.
- 3번 비트는 행동이 커서 카메라까지 움직이면 뭉개진다.

---

## 5. 표정·행동 어휘 (동사로 쓴다)

| 쓰지 말 것 | 쓸 것 |
|---|---|
| `화난 표정` | `her jaw tightens, she does not blink` |
| `슬픔` | `her eyes fill, she looks down` |
| `무섭게` | `he goes very still` |
| `긴장감이 흐른다` | `no one speaks; only the shutters rattle` |

**감정을 형용사로 쓰면 안 나온다. 몸의 움직임으로 쓴다.**

---

## 6. 소리 (오디오)

프롬프트 뒤쪽(꼬리말 근처)에 한 줄로 쓴다.

```
Market ambience, clattering bowls, a low tense music bed.
No dialogue except the single Korean line above. No voiceover.
```

- 소리는 **"무엇이 들리는가"** 로 쓴다. `긴장되는 음악` ✗ → `a low tense music bed` ✓
- 대사가 없는 샷: `No dialogue or voiceover.`

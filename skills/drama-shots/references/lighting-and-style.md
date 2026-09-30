# 조명과 스타일 — 전역 1개, 샷마다 복사

> ②스타일 ③조명 자리에 쓰는 어휘. **시리즈 전체에 1개만 정하고**, 모든 프롬프트에 같은 문장을 복사한다.
> 시리즈를 이어 붙이는 유일한 방법이다 (같은 톤·같은 빛).

---

## 1. 스타일 전역 문장 (예시 — 우리 프로젝트 실제 값)

```
A realistic Korean drama tone, harsh white midday sunlight, high contrast,
cold reflections off grey concrete and stainless steel, murky teal shadows, shallow depth of field.
```

- **① 사실적인 한국 드라마 톤** — 장르·질감
- **② 정오의 하얀 직사광** — 빛의 세기·방향
- **③ 강한 콘트라스트** — 대비
- **④ 회색 콘크리트·스테인리스의 차가운 반사** — 재질과 색 반사
- **⑤ 탁한 청록 그늘** — 그림자 색
- **⑥ 얕은 심도** — 배경 흐림

**순서가 중요하다**: 톤 → 빛 → 대비 → 색 → 심도.

---

## 2. 시간대별 빛

| 시간 | 영어 | 느낌 |
|---|---|---|
| 새벽 | `cold blue pre-dawn light` | 고요·불안 |
| 아침 | `soft warm morning light, long shadows` | 희망·일상 |
| 정오 | `harsh white midday sunlight, hard shadows` | **대비 최대. 갈등에 어울린다** |
| 오후 | `golden hour light, warm rim light` | 그리움·회상 |
| 해질녘 | `low orange sunset light` | 종결·이별 |
| 밤(실내) | `warm tungsten interior light, deep shadows` | 밀실·친밀 |
| 밤(실외) | `cool neon and sodium street light` | 도시·고독 |

---

## 3. 광원 방향

| 영어 | 효과 |
|---|---|
| `light from the left side` | 입체감. 얼굴 반쪽이 그늘 |
| `backlit, rim light on the hair` | 인물 분리. 감동·역광 |
| `flat front light` | 밋밋하지만 안전 |
| `top light, eye sockets in shadow` | 위압·불안 |
| `light through a window behind them` | 창문 실루엣 |

**얼굴이 반으로 갈리는 조명(`split lighting`)은 대사 샷에 좋다.** 표정이 강해진다.

---

## 4. 색과 대비 — 한국 정서 미장센

| 요소 | 색·질감 |
|---|---|
| 시장·골목 | 빛바랜 베이지, 녹슨 철, 회색 시멘트 |
| 국숫집·식당 | 스테인리스 반사, 흰 타일, 노란 형광 |
| 아파트·사무실 | 냉백색, 회색 커튼, 낮은 천장 |
| 병원·관공서 | 청록, 삐걱이는 형광, 광택 바닥 |
| 한강·공원 | 흐린 하늘, 탁한 물빛 |

**한국적 디테일은 소품으로**: `a stainless steel chopstick holder`, `a worn plastic stool`,
`a sleet-covered corrugated awning`, `vinyl-covered market stalls`.

---

## 5. 심도 (Depth of field)

| 영어 | 결과 |
|---|---|
| `deep focus` | 전부 선명 (와이드·군중) |
| `shallow depth of field` | 배경 흐림 (인물 강조). **대사 샷 기본** |
| `very shallow depth of field, background fully blurred` | 소품·손 강조 |

**참조(캐릭터 시트)를 쓸 때는 `shallow` 를 유지한다** — 배경이 흐려도 인물은 선명하게 유지된다.

---

## 6. 스타일을 바꾸고 싶을 때

**전역 문장을 바꾸면 앞뒤 컷이 다 튄다.** 한 편 안에서는 고정한다.
다른 톤이 필요하면 그 **샷 하나만** 예외로 두고, 이유를 `judgement.jsonl` 메모에 남긴다.

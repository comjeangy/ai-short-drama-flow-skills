# 변경 기록

## v4 — 2026-09-30 · 구조 개편

**"문서 3장"에서 "스킬 패키지"로.** 다른 공개 스킬 저장소와 비교해 구조가 빈약하다는 지적을 반영.

- `references/` 를 **주제별 12종**으로 분리 (이전: 공유 4종)
  - 신규: `prompt-anatomy` · `shot-grammar` · `lighting-and-style` · `conti-and-keyframe` ·
    `character-consistency` · `korean-dialogue` · `editing-and-revision` · `failure-atlas`
  - `prompt-recipes.md` 는 색인으로 전환 (어떤 문서를 언제 읽는가)
- `assets/` 양식 7종 신규 — 기획 카드 · 캐릭터 시트 · 장소 시트 · 콘티 패널 · 샷 · 렌더 로그 · 판정
- `examples/ep01/` 신규 — 실제 완주 기록 8종 (프롬프트 전문 + 판정 + 크레딧)
- `scripts/` 신규 — `check_prompt.py`(프롬프트 검수기) · `selftest.py`(구조 점검)
- 문서 세트 신규 — `DESIGN.md` · `CHANGELOG.md` · `AGENTS.md` · `CONTRIBUTING.md` ·
  `README.en.md` · `docs/설치-강의용.md`
- 스킬마다 `references/` 개별 구성 (7·8·12·8종) · 양식 7종 동봉
- 프롬프트 검수로 실제 결함 수정: 시트·콘티·장면 프롬프트에 **`9:16` 명시 누락** → 보완
- README 격상 (파이프라인 도식 · 실측 근거표 · 구조 · 검증 상태)

## v3 — 2026-09-30 · 캐릭터 파이프라인 개편

- 캐릭터를 "상반신 정면 1장" → **4뷰 시트**(정면·3/4·측면·후면 + 얼굴 클로즈업)
- 2벌 의상은 **편집 파생**(`edit_asset`) — 새로 만들면 얼굴이 바뀐다
- 3차시를 "곧바로 영상" → **콘티 4패널 승인 → 키프레임 → `프레임 → 시작` → 장면**
- 이미지 단계 **0크레딧** 실측 반영 — "이미지로 승인받고 영상만 신중히"
- 사실 오류 정정: "10초 고정" · "15 크레딧" · "하루 3편" · "1080p 업스케일" → 확인 절차로 교체
- 스킬 범위 못 박음: **산출물은 프롬프트 텍스트, Flow 화면을 조작하지 않는다**
- 스킬 4종 + 계보 문서 설치 · 저장소 공개 (`comjeangy/ai-short-drama-flow-skills`)

## v1 — 2026-09-29 · 최초 4차시 커리큘럼

- `drama-story` · `drama-world` · `drama-shots` · `drama-cut` 4종
- 1차시 주제·로그라인·인물 3명 / 2차시 세계관·캐릭터 시트 / 3차시 장면 / 4차시 진단·수정
- 연구 원자료 4종(중국 방법론 · 한국어판 · Flow · Omni) 기반

## v0 — 2026-09-28 · 초판 저장소

- 스킬 4종 초판 + README. (이후 `ai-short-drama-flow-skills-v0` 로 보존)

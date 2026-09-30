# Korean Short-Form Drama Skills — 4 Steps for Google Flow

Four skills that help you make **vertical 9:16 Korean short-form drama** with AI conversation.
Built for Gemini Spark / Google Flow users (lecture and personal practice).

**The skills only produce prompt text.** They never drive the Flow UI — no clicking, typing, or
starting generations. A human pastes the prompt and presses the button.

> 한국어 문서는 [README.md](README.md) 를 보세요. 이 문서는 요약입니다.

| Step | Skill | Decides with you | Prompt it hands you | Cost |
|---|---|---|---|---|
| 1 | [drama-story](skills/drama-story) | topic, logline, 3 characters, 3 beats | planning card, look sketch | `0` |
| 2 | [drama-world](skills/drama-world) | world, tone, **4-view character sheets**, location sheets | sheet prompts, location suffix | `0` |
| 3 | [drama-shots](skills/drama-shots) | **4-panel storyboard sign-off → keyframe →** 10s shot | storyboard, keyframe, scene | `0` → video `7~15` |
| 4 | [drama-cut](skills/drama-cut) | diagnose, revise, keep | revision prompts, verdict sheet | `7~15` |

## Why the pipeline is shaped this way

| Breaks | Cause | Fix in these skills |
|---|---|---|
| Clothing/face drifts shot to shot | a single front-facing half-body sheet carries no back/sleeve/shoe info, so the model invents it | **4-view sheet** (front, 3/4, side, back + face close-up); second outfit by **edit derivation** |
| Background/action differs from what you imagined | described in prose only | **4-panel storyboard first** (0 credits) → **keyframe** → `Frame → Start` |
| On-screen Korean comes out broken | Hangul is a jamo composition; rendering collapses | all on-screen text is **composited in post**; ban text in every prompt |

**All image steps cost 0 credits.** Money starts at the video `generate` button.

## Measured (2026-09-30, paid PRO account, 0 credits spent)

| Model | Options | Credits |
|---|---|---|
| Image mode (Nano Banana Pro / 2 / 2 Lite) | 5 ratios, x1–x4 | **0** (no approval dialog) |
| Omni 1.1 Flash | 10 s | 360p **7** · 720p **15** |
| Veo 3.1 - Lite | no resolution/length choice | x1 **10** · x2 **20** · x4 **40** |

- The **ratio selector does not stick** (clicking 16:9 still renders 9:16) → state `9:16` in the prompt.
- Manage **cost per approved clip**, not unit price.

## Structure

```
skills/<skill>/SKILL.md + references/(topic docs) + assets/(7 fill-in templates)
dist/*.zip            Spark upload bundles
examples/ep01/        a real end-to-end record
scripts/              check_prompt.py (prompt linter) · selftest.py (structure check)
```

## Example

[`examples/ep01/`](examples/ep01) — sheets, locations, storyboard and keyframe all approved at
**0 credits**; the 10-second shot is queued at **7 credits** (360p).

## Install (Gemini Spark)

1. Open the [Gemini Spark Skills page](https://support.google.com/gemini/answer/17094296).
2. Download a zip from `dist/` (on GitHub choose **Download raw file**).
3. Upload it in Spark, review the contents, create.
4. In a new chat type `/` to pick the skill, or just ask for the task.

## Prompt rules (summary)

- Instructions in English, **only dialogue in Korean**; the dialogue goes **first**.
- No on-screen text: `No text overlay on screen.`
- Dialogue shots are locked to **one unbroken scene** (`no scene cuts`).
- Always state **10 seconds** and **9:16**.
- Revisions: **within 4 turns**, otherwise regenerate.
- Record **model · resolution · length · credits · verdict** with every prompt.

## License

See [LICENSE.md](LICENSE.md). Free for lecture attendees and personal practice.

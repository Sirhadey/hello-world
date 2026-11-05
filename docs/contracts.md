# Contracts

Versioned interfaces and data shapes. **Changing any of these requires an ADR**
(MASTER_PROMPT.md C12). Data schemas live in `schemas/`; this file defines the
code interfaces and how they relate.

Contract version: **v1** (2026-11-05).

## Data schemas

| Schema | File | Produced by | Consumed by |
|---|---|---|---|
| Storyboard v1 | `schemas/storyboard.v1.json` | A5 Storyboarder (WP1/WP2), edited by UI | image router, TTS, renderer, auditor |
| HardwareProfile v1 | `schemas/hardware_profile.v1.json` | `HardwareProbe` (WP3) | UI hardware panel, download recommendations |
| JobEvent v1 | `schemas/job_event.v1.json` | backend job state machine (WP2) | UI event stream |

Rules baked into the storyboard schema:

- Every `image.prompt` contains "no text", "no lettering" and "no watermark" (C4).
- `style_lock.negative_prompt` forbids text and watermarks.
- `scene.duration_s` is derived from TTS audio plus padding and is written only by the
  voice stage. It is absent until narration exists. Never hand-set.
- Verbatim scripture is never authored by a model. `scripture_refs` hold references only;
  quoted text is pulled from the local public-domain Bible file at render time (C5).
- On-screen text comes only from `onscreen_text[]`, drawn by code (C4, D-006).

## Code interfaces

Python signatures are normative for behavior and names; exact typing lands in WP2.

```python
class LLMProvider:
    def generate(self, prompt: str, json_schema: dict) -> dict:
        """Return JSON that validates against json_schema.
        Raise ProviderError on transport failure. Do not retry internally;
        the agent runner owns retries (up to 2, passing the validator error back)."""

class ImageProvider:
    def generate(self, prompt: str, size: tuple[int, int],
                 seed: int | None, style: StyleLock) -> ImageResult:
        """ImageResult = (file_path, meta, license_info). Raise RateLimited (HTTP 429/quota)
        so the router can back off and fail over. A cache hit must not touch the network."""

class TTSEngine:
    def synthesize(self, text: str, voice: str, speed: float) -> TTSResult:
        """TTSResult = (wav_path, duration_s). Exact audio duration, in seconds."""

class Renderer:
    def render_scene(self, scene: dict, assets: SceneAssets) -> Path:
        """Return clip_path. Deterministic for identical inputs. Resumable per scene."""

class HardwareProbe:
    def detect(self) -> dict:
        """Return a HardwareProfile v1 document."""
```

## Agent contract (A1 to A9)

Each agent ships `prompts/<agent>/system.md`, `user.template.md`, `schema.json`,
`examples/`. Output is JSON only, validated against `schema.json`. On failure the runner
retries up to 2 times, passing the validator error message back. Agents must not invent
quotes, must flag uncertainty, and ask for nothing beyond their listed inputs.

## Approval gates

| Gate | After | Blocks |
|---|---|---|
| A | A4 script | storyboard generation |
| B | A5 storyboard | image generation and narration |
| C | A8 audit | rendering |

## Change process

1. Open an issue labeled `contract`.
2. Add `docs/decisions/ADR-XXXX-title.md` (copy `ADR-template.md`).
3. Bump the schema version (`storyboard.v2.json`; keep v1 until consumers migrate).
4. Add a one-line entry to `HANDOFF.md` under Decisions.

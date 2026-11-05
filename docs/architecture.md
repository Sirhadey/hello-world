# Architecture (summary)

Authoritative detail is in `MASTER_PROMPT.md` sections 4 to 10. Defaults here are
confirmed or changed through ADRs.

```
Brief ─▶ A1 ─▶ A2 ─▶ A3 ─▶ A4 ──[Gate A]──▶ A5 ──[Gate B]──▶ A6, A7
                                                                  │
          Images (router, failover, cache) ◀──────────────────────┤
          Narration (Kokoro) ─▶ exact durations ─▶ storyboard      │
                                   │                              ▼
                                   └────────────▶ A8 Audit ──[Gate C]──▶ Render ─▶ MP4 + metadata (A9)
```

- **Backend:** Python 3.11, FastAPI, SQLite, single-process background worker (no Redis).
- **Frontend:** React, TypeScript, Vite, CSS-variable design tokens.
- **Media:** FFmpeg subprocess, Pillow, OpenCV, optional small depth model on CPU.
- **TTS:** Kokoro on CPU by default.
- **LLM:** provider-agnostic; PasteMode is the default.
- **Principle:** audio drives the timeline. Stages run one at a time (Tier 0 memory limit
  about 10 GB per stage); jobs are resumable.

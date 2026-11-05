# MASTER PROMPT: Bible Story Studio

> **Working name.** Version 0.1 · Created 2026-11-05 · Status: authoritative project brief.
> This file is the single source of truth for **what we are building** and **how we work**.
> It is read first, every session, by every contributor and every AI assistant.
> Current progress lives in `HANDOFF.md`. Rules and scope live here.

---

## 0. Read this first

### 0.1 Read order (always)

1. `MASTER_PROMPT.md` (this file): what we build, the rules, the work packages.
2. `HANDOFF.md`: current status, who owns what, what is done, what is next.
3. `docs/wp/WP-<n>.md`: the detailed spec for the work package you take. Until WP0 is merged, the specs in section 11 of this file are the specs.

**Precedence.** If this file and `HANDOFF.md` disagree, the *rules and scope* here win and the *status* in `HANDOFF.md` wins. If something is unclear, record a question in `HANDOFF.md` under "Open questions" instead of guessing.

**Never rely on chat history.** Chats and AI memory belong to individual accounts and do not carry over between people. Only files in this repo are the source of truth.

### 0.2 Where to begin (decision procedure)

Follow these steps in order. Do not skip step 2.

1. Open `HANDOFF.md` and read the **Status board**, **Current focus**, **Blockers**, and **Open questions**.
2. Compare the Status board against the dependency table in section 11. A work package (WP) is **available** only if its status is `NOT STARTED` and every WP it depends on is `DONE`. (Contract-only dependencies are noted per WP.)
3. If the project owner told you which WP to take, take that one, unless it is blocked. If it is blocked, say so and propose the nearest available WP.
4. Otherwise choose the **first available WP** in numeric order. If none is available, report the blockers and stop. Do not invent work.
5. **Claim it** before writing any code: edit `HANDOFF.md` (status `CLAIMED`, owner, branch name, date) and push that change first.
6. Read the WP spec and its acceptance criteria. If something you need is undecided, add it to "Open questions" and ask the project owner once.
7. Work on a branch named `wp-<n>/<short-name>`. Do not edit files outside your WP's folders unless the WP spec says so.

**First reply for AI assistants.** Before doing any work, reply with: (a) which WP you will take and why, citing the Status board; (b) assumptions and open questions; (c) the plan in 5 bullets or fewer. Wait for a go-ahead unless the owner already assigned the WP.

### 0.3 Session protocol: copy these prompts exactly

**Session start**

```
SESSION START
Read MASTER_PROMPT.md, then HANDOFF.md, then docs/wp/WP-<n>.md.
Compare the HANDOFF status board with the dependency table in the
master prompt and tell me which work package I should start or
continue, and why. Summarize the current status in 5 lines. Then
continue with the next unchecked task. Do not change files outside
this work package's folders.
```

**Session end**

```
SESSION END
Update HANDOFF.md with: done, in progress, next, blockers, and how to
run the tests. Add a dated line to the session log. List the files you
changed. Give me the commit message and the exact git commands to
commit and push to branch wp-<n>/<name>.
```

### 0.4 If you are near a usage limit

Stop starting new tasks. Finish the current edit, run the tests you can, then run the **Session end** prompt. A clean handoff matters more than one more feature. Never leave uncommitted work described only in chat.

### 0.5 If the repo is not connected to your Claude

Paste `MASTER_PROMPT.md` and `HANDOFF.md` into the chat, then send the **Session start** prompt. When you finish, send **Session end** and commit the updated files yourself.

---

## 1. Mission

Build a **locally installed application with a web interface** that turns a short brief into a complete **12 to 20 minute narrated, illustrated video (MP4)** for calm, reverent Bible-story and explainer channels, using **only free tools**.

Pipeline: **Brief → Script → Storyboard → Images → Narration → Camera effects and sound → Audit → Render → Metadata.**

The app does not replace the creator. It enforces a structure, so each step is done in order, accurately, with approval gates. Every video must be shaped by a human-approved script.

### 1.1 Style source

The prompts and structure follow the patterns of the YouTube Shorts already produced for this channel: a hook in the opening, open loops that are paid off, numbered movements when suitable, a retention map, a scripture map for fact-checking, an accuracy-notes section, a QA checklist, and an SEO block. For long form, adapt these to **calm pacing**: no clickbait, no frantic cutting, a gentle mid-video engagement line.

### 1.2 Success criteria for v1

- A non-expert can make a 12-minute video from a short brief on a **Tier 0 laptop (16 GB RAM, 2 GB VRAM)** with no paid service, using an overnight render.
- **Zero** misspellings in on-screen text and **zero** unverified verse quotes (the Auditor gate enforces both).
- The app detects hardware and recommends suitable models.
- The interface looks professional (Apple-inspired).
- The repository is clean, documented, and easy for collaborators to join.

---

## 2. Non-negotiable constraints

| # | Constraint |
|---|---|
| C1 | **Free only.** No paid API is required to finish a video. Paid or optional integrations may exist as adapters but are never defaults. |
| C2 | **Baseline hardware = Tier 0:** 16 GB RAM, 2 GB dedicated VRAM (NVIDIA). Everything must work there. Higher tiers add options, never requirements. |
| C3 | **Narration = Kokoro** (CPU by default). **No voice cloning in v1.** |
| C4 | **No text inside generated images.** All on-screen text is drawn by code from a verified string list. Every image prompt must say: no text, no lettering, no watermark. |
| C5 | **Verbatim Scripture comes from a local public-domain Bible file** (WEB or KJV). Never from a model. |
| C6 | **Spelling and names:** a names glossary plus a spell-check. The Auditor must pass before any render. |
| C7 | **Licenses:** ship only public-domain or open content. Download models and binaries on first run with their licenses shown. Keep a `NOTICE` file and a per-video license log (images, audio, music, sound effects). |
| C8 | **YouTube compliance by design:** a human approves the script; each video varies in look and structure; the Auditor includes an AI-disclosure and anti-"mass-produced" checklist. |
| C9 | **Image generators:** up to 4 providers behind adapters, with failover, backoff, a local cache, and a style lock. Default maximum of 2 providers mixed in one video. |
| C10 | **Tier 0 memory safety:** stages run one at a time, jobs are resumable, and no single stage may exceed about 10 GB of RAM. |
| C11 | **UI:** Apple-inspired (Human Interface Guidelines principles), light and dark, accessible, system font stack, no proprietary assets. |
| C12 | **Contract-first:** schemas and interfaces are versioned. Changing one requires an ADR (decision record). |
| C13 | **Windows is the primary target.** Support Linux and macOS where it is cheap. |
| C14 | **No secrets in the repo.** API keys live in local settings or environment files that are git-ignored. |

---

## 3. Users and core flow

**Persona:** a creator with little AI knowledge who wants a polished video with minimal inputs.

**Flow**

1. **New project (5 fields):** passage or topic; target length (12 to 20 min); tone preset; visual style preset; optional notes and key message. Translation defaults to WEB or KJV.
2. **Script review (Gate A):** the user approves or edits the script.
3. **Storyboard review (Gate B):** the user approves scenes, images, moves, and sounds.
4. **Image queue:** generated with failover; the user can regenerate single scenes.
5. **Narration:** Kokoro generates per-scene audio, which sets scene durations.
6. **Audit (Gate C):** quotes, names, spelling, licenses, and compliance must pass.
7. **Render:** resumable, designed to run overnight on Tier 0.
8. **Export:** MP4, thumbnail suggestions, titles and description, chapters, tags, and the license log.

Users may paste their own prompts, script, or a finished storyboard to skip any steps.

---

## 4. Architecture (default decisions; confirm via ADR-0001 in WP0)

- **Backend:** Python 3.11, FastAPI, SQLite, a single-process background worker (no Redis).
- **Frontend:** React, TypeScript, Vite; CSS-variable design tokens; no heavy UI kit.
- **Media:** FFmpeg called as a subprocess (user-installed or downloaded on first run; respect its license), Pillow and OpenCV for image work, an optional small depth model on CPU for parallax.
- **TTS:** Kokoro (Apache-2.0 as reported by its docs; verify on implementation).
- **LLM:** provider-agnostic. **PasteMode is the default** (the app shows the prompt; the user pastes it into any chat and pastes the JSON back). Optional adapters: OpenAI-compatible HTTP endpoints and a small local model.
- **Packaging:** a launcher script (`start.bat`, `start.sh`) first; an installer later.

### 4.1 Interface contracts (full definitions go in `docs/contracts.md`)

```
LLMProvider.generate(prompt, json_schema)            -> json
ImageProvider.generate(prompt, size, seed?, style)   -> file_path, meta, license_info
TTSEngine.synthesize(text, voice, speed)             -> wav_path, duration_s
Renderer.render_scene(scene, assets)                 -> clip_path
HardwareProbe.detect()                               -> HardwareProfile
```

---

## 5. Pipeline and agents

Each agent has: `prompts/<agent>/system.md`, `user.template.md`, `schema.json`, and `examples/`. Every agent returns **JSON only**, validated against its schema. If validation fails, retry up to 2 times, passing back the validator's error message. Agents must not invent quotes, must flag uncertainty, and must ask for nothing except their listed inputs.

| ID | Agent | Input | Output | Checks | Gate |
|---|---|---|---|---|---|
| A1 | Intake Normalizer | the 5 form fields | normalized brief | length bounds, tone and style presets valid | none |
| A2 | Scripture Researcher | brief, local Bible text | scripture map (references, verbatim text, context notes, contested points) | every verse exists and is quoted verbatim | none |
| A3 | Story Architect | brief, scripture map | outline: hook, movements, open loops, retention beats, engagement line placement | open loops all paid off | none |
| A4 | Scriptwriter | outline | narration script with a word budget | about 140 words per minute; interpretations hedged | **A** |
| A5 | Storyboarder | approved script | scenes with narration, shot, image prompt, sound cue, on-screen text | schema valid; unique images about 40 to 60 | **B** |
| A6 | Visual Director | storyboard | style lock, per-scene image prompts adapted per provider, negative prompts | every prompt forbids text and watermarks | none |
| A7 | Sound Designer | storyboard | cue tags mapped to the local SFX and music library, levels, ducking | all tags exist in the library | none |
| A8 | Auditor | everything | audit report (quotes, names, spelling, licenses, compliance) | all checks pass | **C** |
| A9 | Metadata Writer | approved script | title options (65 characters or fewer), description, chapters, tags, hashtags | no unsupported claims | none |

**Code-only stages (no LLM):** TTS, image generation, rendering, QC.

### 5.1 Shorts-derived patterns to encode in the prompts

- A hook within the first 10 seconds (a question or stakes), then open loops that are paid off before the end.
- Numbered movements ("reason one, two, three") when the content fits.
- A retention map for the creator (not narrated).
- A scripture map for fact-checking.
- Accuracy notes: say "many see" for interpretations, never present a tradition as Scripture, flag contested points.
- A QA checklist and an SEO block.
- A gentle mid-video engagement line (subscribe or comment), placed naturally at a pause.
- Calm pacing: average sentence length about 20 words or fewer, with pauses.

---

## 6. Storyboard schema (summary; full JSON Schema in `schemas/storyboard.v1.json`)

```
storyboard
├─ meta: title, target_length_s, tone, style_preset, translation, language
├─ style_lock: palette, medium, lighting, negative_prompt, grade_preset
├─ scenes[]
│   ├─ id, order
│   ├─ narration: text, voice, speed
│   ├─ duration_s  (derived from TTS audio + padding; never hand-set)
│   ├─ shot: type, camera_move {kind, intensity, direction, params}, transition
│   ├─ image: prompt, provider_hint, seed, asset_ref
│   ├─ sound: sfx_tags[], music_tag, level_db, duck_under_narration
│   ├─ onscreen_text[]: text_id, text, position, start_s, end_s, style
│   ├─ scripture_refs[]
│   └─ notes
└─ audit: status, report_ref
```

**Principle:** the audio drives the timeline. Scene duration = narration audio length + padding. Transitions overlap neighboring scenes.

---

## 7. Hardware tiers

The app probes hardware on first run (and on demand, for example after a laptop upgrade), assigns a tier, and offers downloads with size, license, and disk space shown. **Tier boundaries are estimates; verify and tune in WP3.**

| Tier | Typical hardware | Defaults | Optional installs |
|---|---|---|---|
| **0** | No GPU or about 2 GB VRAM (the owner's laptop: 16 GB RAM) | Free cloud image providers, Kokoro on CPU, camera-effect rendering | FastSD CPU in its low-RAM modes as a fallback image source |
| **1** | About 4 to 6 GB VRAM | Small local image models on GPU, faster Kokoro | Larger image models |
| **2** | About 8 to 12 GB VRAM | Local image models | WanGP for short AI video clips |
| **3** | 16 GB VRAM and up | Higher-resolution local video | Larger WanGP models |

Notes:

- FastSD CPU's tool is MIT-licensed, but **each model it runs has its own license**. Show it before download. Its OpenVINO standard mode needs about 11 GB of RAM, so it is **off by default on Tier 0**.
- **WanGP (Wan2GP):** its license requires crediting WanGP when an app uses it. Offer it as an **optional separate install** with attribution; never bundle it. Read its current license before integrating.
- On Tier 0, **AI video generation is not offered.** Camera effects stand in.

---

## 8. Image router rules

1. Providers sit behind `ImageProvider` adapters. The candidate list and each provider's terms must be **verified at implementation time** (free tiers change often). Record the final list in an ADR.
2. Use rotation as **failover and load-spreading**, not random aesthetic mixing. Default maximum: 2 providers in one video.
3. Handle HTTP 429 and quota errors with exponential backoff and automatic failover to the next provider. Jobs must resume after a restart.
4. **Style lock:** every prompt gets the shared style suffix and negative prompt, and every image gets the same color grade.
5. Cache images by `(prompt, style, size, seed)`. A cache hit must not touch the network.
6. Write a **license log entry** for every image (provider, date, terms link).
7. Never ask an image model for text. Prompts include "no text, no lettering, no watermark".
8. Plan about 40 to 60 unique images per 12 to 20 minute video, each reused with 2 to 3 different camera moves.

---

## 9. Voice rules (Kokoro)

- Audition candidate voices: `am_michael`, `bm_fable`, `am_adam`, `bm_george`. Start at speed 0.90 to 0.95 for a calm read.
- Chunk at sentence boundaries; Kokoro processes limited tokens per pass.
- Keep a `pronunciations.yaml` of overrides for biblical names, and log manual listening checks.
- Normalize the final mix to about -14 LUFS integrated with peaks below -1 dBTP (verify in WP6c).
- Write the **exact audio duration** back into the storyboard.

---

## 10. Render and effects rules

- **Camera effects (default on all tiers):** zoom in and out, pan, shake, focus pull (blur to sharp), parallax from an optional depth map, build-up reveal (wipe or staged dissolve across 3 to 4 images), crossfade and dip transitions, light overlays, dust, grain, vignette.
- **Text:** only from the verified string list. Bundle an open-licensed font.
- **Maps:** drawn by code from public-domain geographic data (verify the data license in an ADR). Animated routes and labels. Never AI-generated maps.
- **Sound:** a tagged local library (drums, whoosh, wind, crowd, bells, ambience, music beds). The library's index is committed; the audio files are git-ignored and fetched on setup. Keep a license log.
- **Encoding:** H.264 video and AAC audio. Use NVENC if available, else CPU. Rendering is resumable per scene.
- **QC report:** duration matches audio, no black frames, no clipping, text inside safe areas.

---

## 11. Work packages (specs, dependencies, acceptance criteria)

Status values: `NOT STARTED`, `CLAIMED`, `IN PROGRESS`, `IN REVIEW`, `DONE`, `BLOCKED`.
Sizes: S = about one session, M = a few sessions, L = many sessions.

| WP | Name | Depends on | Size | Role |
|---|---|---|---|---|
| 0 | Foundation | none | S | Lead |
| 1 | Agent prompt pack v0.1 | 0 | M | Prompts and content QA |
| 2 | Backend core | 0 | L | Backend |
| 3 | Hardware probe and tiers | 0 | M | Backend |
| 4 | Image router | 0 | M | Backend |
| 5 | Voice (Kokoro) | 0 | S | Backend or media |
| 6 | Render engine (6a, 6b, 6c) | 0 | L | Media and FFmpeg |
| 7 | Auditor | 1 | M | Backend and content QA |
| 8 | Web UI | 0 (mock API) | L | Frontend and design |
| 9 | Packaging and polish | 2 to 8 | M | Lead |
| 10 | Pilot and hardening | all | M | Everyone |

### WP0 Foundation
**Deliver:** repo scaffold (section 13); `README`, `LICENSE` (Apache-2.0 proposed, decide in ADR-0001), `NOTICE`, `CONTRIBUTING`, `CODE_OF_CONDUCT`; issue and PR templates; `CODEOWNERS`; CI skeleton (lint, schema validation, spell-check job); `schemas/` (storyboard v1, hardware profile v1, job event v1); `docs/contracts.md`; ADR template; label list; `examples/gideon/` sample brief and storyboard.
**Accept:** CI is green on a fresh clone; the sample storyboard validates against the schema; a new contributor can run `make check` from the README.

### WP1 Agent prompt pack v0.1
**Deliver:** `prompts/` for A1 to A9 (system prompt, user template, schema, one worked example each); `prompts/README.md` explaining overrides and PasteMode.
**Accept:** each example output validates; the Auditor prompt catches seeded errors (a misquoted verse, a misspelled name); a read-through confirms no invented quotes and hedged interpretations.

### WP2 Backend core
**Deliver:** FastAPI app; SQLite models (Project, Run, Scene, Asset, Job); resumable job state machine; agent runner (schema validation, up to 2 retries with error feedback); LLM adapters (PasteMode, OpenAI-compatible HTTP, local); approval gates A, B, C; event stream for the UI; settings store.
**Accept:** the sample brief runs through A1 to A5 in PasteMode using fixtures; killing and restarting mid-run resumes; unit tests cover the runner and state machine.

### WP3 Hardware probe and tiers
**Deliver:** detection of OS, CPU, RAM, GPUs and VRAM (NVML or `nvidia-smi` with fallbacks), free disk, FFmpeg and NVENC availability; tier assignment per section 7; `config/models.yaml` (id, size, license, minimum tier, URL, checksum); a resumable download manager with checksum and license display; a re-probe command.
**Accept:** table-driven tests with mocked profiles give the right tier and recommendations; the owner's laptop profile (16 GB RAM, 2 GB VRAM) returns Tier 0; a test download verifies its checksum.

### WP4 Image router
**Deliver:** `ImageProvider` interface and adapters for up to 4 free providers (final list via ADR after verifying terms); optional FastSD CPU adapter (low-RAM modes only on Tier 0); failover and backoff; quotas; cache; style lock and grade; optional upscale; license log entries.
**Accept:** with providers mocked to fail or return 429, a 40-image batch completes and resumes; no more providers than configured are used per video; a cache hit makes no network call.

### WP5 Voice
**Deliver:** Kokoro wrapper; voice audition samples; sentence chunking; speed control; per-scene WAV files and exact durations; pronunciation overrides; loudness normalization.
**Accept:** a 2,800-word script synthesizes within the Tier 0 memory limit; glossary names use overrides; durations are written back to the storyboard.

### WP6 Render engine
**6a Camera motion:** all moves in section 10, parametrized in the storyboard `shot` block, deterministic.
**6b Text and maps:** code-drawn text cards, lower-thirds, counters and timelines; the map module.
**6c Audio and assembly:** mix with ducking and normalization, concatenate scenes, final MP4, QC report.
**Accept:** a 3-minute sample storyboard with 20 images renders on Tier 0; golden-frame tests pass; rendering resumes per scene; peak RAM is recorded.

### WP7 Auditor
**Deliver:** code and the A8 agent: verbatim quote check against the local Bible text; reference validation; names glossary; spell-check of all narration and on-screen text; flagged-claims list; license log completeness; AI-disclosure and compliance checklists; `audit_report.json` plus a readable version; the gate that blocks rendering.
**Accept:** every seeded-error fixture is caught; the gate blocks on any failure.

### WP8 Web UI
**Deliver:** design tokens and components; screens for Projects, New Project wizard, live Agent run, Script review, Storyboard board with thumbnails, Image queue, Audit report, Render queue and preview, Hardware panel (tier badge and recommended downloads), Settings (providers, voices, prompt editor with reset-to-default); empty and error states; light and dark; keyboard navigation. Built against a mock API first.
**Accept:** a screenshot set and a mock-data walkthrough; accessibility checks pass.

### WP9 Packaging and polish
**Deliver:** launcher scripts; first-run setup (checks FFmpeg, downloads Kokoro, probes hardware); README with a demo GIF; sample project; troubleshooting guide; `v0.1` tag.

### WP10 Pilot and hardening
**Deliver:** a 3-minute end-to-end video, then a 12-minute overnight run; per-stage time and RAM measurements; fixes; a known-issues list; the first real video.

---

## 12. Milestones and parallelization

- **M1 Foundations:** WP0, then WP1.
- **M2 Engines (parallel):** WP3, WP4, WP5, WP6.
- **M3 Intelligence:** WP2, WP7.
- **M4 Experience:** WP8 (can start early on the mock API), WP9.
- **M5 Pilot and release:** WP10.

**Critical path:** WP0 → (WP2, WP6a, WP8 on mock) → integration → WP10.

---

## 13. Repository structure

```
bible-story-studio/
├─ MASTER_PROMPT.md
├─ HANDOFF.md
├─ README.md   LICENSE   NOTICE   CONTRIBUTING.md   CODE_OF_CONDUCT.md
├─ .github/    (CODEOWNERS, ISSUE_TEMPLATE/, PULL_REQUEST_TEMPLATE.md, workflows/ci.yml)
├─ docs/       (architecture.md, contracts.md, decisions/ADR-*.md, wp/WP-00.md ...)
├─ schemas/    (storyboard.v1.json, hardware_profile.v1.json, job_event.v1.json)
├─ prompts/    (a1-intake/ ... a9-metadata/, README.md)
├─ config/     (hardware_tiers.yaml, models.yaml, providers.yaml)
├─ data/       (bible/ [WEB, KJV text], glossary/names.yaml, pronunciations.yaml, sfx_index/)
├─ backend/    frontend/    tests/
└─ examples/gideon/
```

---

## 14. Git workflow and collaboration rules

- **One owner per WP**, one branch per WP: `wp-<n>/<short-name>`.
- **Small PRs:** about 400 changed lines or fewer (excluding generated files). Squash-merge.
- **Commit messages:** conventional style, for example `feat(wp4): add provider failover`.
- **Every PR updates `HANDOFF.md`** (status board row and session log).
- **CI must pass** before merge: lint, schema validation, spell-check of prompts and docs, unit tests, and golden-frame tests where they exist.
- **CODEOWNERS** assigns each folder a reviewer.
- Run `git pull` before every session. Never force-push `main`.
- Do not claim tests pass unless you ran them. State what you could not run.

### 14.1 Do not

- Add a paid dependency, or bundle model weights or FFmpeg binaries.
- Change a schema or contract without an ADR.
- Commit secrets, large media files, or generated outputs.
- Invent verses, references, or sources.
- Start a large refactor outside your WP.
- Present an interpretation as settled Scripture.

---

## 15. Definition of done

**Every WP:** acceptance criteria met; tests written and passing; docs updated; `HANDOFF.md` updated; license notes added to `NOTICE` if new third-party content was introduced; PR reviewed and merged.

**v1:** all WPs `DONE`; the pilot video published to a private link and reviewed; known issues documented.

---

## 16. Decisions and changes to this file

- Record decisions in `docs/decisions/ADR-XXXX-title.md` (context, decision, consequences) and add a one-line entry to `HANDOFF.md` under "Decisions".
- Changes to this file go through a PR labeled `master-prompt`, with the version number and date updated at the top.

---

## 17. Out of scope for v1

Voice cloning; karaoke-style synced lyrics; AI video generation on Tier 0; multi-language output; cloud hosting; user accounts. Candidates for later: optional embedding of public-domain Bible audio clips as passage readings (see open question Q-005 in `HANDOFF.md`).

---

## 18. Risks

| Risk | Mitigation |
|---|---|
| Free image tiers change or throttle | Adapters, failover, cache, local fallback |
| YouTube treats output as mass-produced | Human-approved script, per-video variation, Auditor compliance checklist, slow upload cadence |
| Licensing mistakes | Public-domain text only, license log, `NOTICE`, show licenses before downloads |
| Tier 0 memory or time limits | Sequential stages, resumable jobs, overnight renders, RAM budget in QC |
| Contributors collide | Contract-first, CODEOWNERS, one WP per owner, claims in `HANDOFF.md` |
| Claude or tool usage limits | Self-contained WP specs, `HANDOFF.md`, session protocol |

# HANDOFF

> Living status board. **Read `MASTER_PROMPT.md` first**, then this file, then your WP spec.
> Update this file in every PR and at the end of every session.
> Last updated: 2026-11-05 · by: project owner (initial)

---

## 1. How to use this file

1. Compare the **Status board** below with the dependency table in `MASTER_PROMPT.md` section 11.
2. A WP is **available** only if it is `NOT STARTED` and all of its dependencies are `DONE`.
3. **Claim** a WP here (status `CLAIMED`, owner, branch, date) and push before you start work.
4. At the end of a session, update the row, the "Current focus", "Next actions", the "Session log", and anything that changed in "Decisions", "Open questions", or "Blockers".

Status values: `NOT STARTED` · `CLAIMED` · `IN PROGRESS` · `IN REVIEW` · `DONE` · `BLOCKED`

---

## 2. Status board

| WP | Name | Depends on | Status | Owner | Branch | Updated | Notes |
|---|---|---|---|---|---|---|---|
| 0 | Foundation | none | NOT STARTED | | | 2026-11-05 | Start here. Blocks everything else. |
| 1 | Agent prompt pack v0.1 | 0 | NOT STARTED | | | 2026-11-05 | |
| 2 | Backend core | 0 | NOT STARTED | | | 2026-11-05 | |
| 3 | Hardware probe and tiers | 0 | NOT STARTED | | | 2026-11-05 | |
| 4 | Image router | 0 | NOT STARTED | | | 2026-11-05 | Verify free provider terms first (see Q-004). |
| 5 | Voice (Kokoro) | 0 | NOT STARTED | | | 2026-11-05 | |
| 6 | Render engine (6a, 6b, 6c) | 0 | NOT STARTED | | | 2026-11-05 | Split across 6a, 6b, 6c if multiple contributors. |
| 7 | Auditor | 1 | NOT STARTED | | | 2026-11-05 | |
| 8 | Web UI | 0 (mock API) | NOT STARTED | | | 2026-11-05 | Can start early on mock data. |
| 9 | Packaging and polish | 2 to 8 | NOT STARTED | | | 2026-11-05 | |
| 10 | Pilot and hardening | all | NOT STARTED | | | 2026-11-05 | |

---

## 3. Current focus

**WP0 Foundation.** Nothing else can start until the repo scaffold, schemas, and contracts exist. No code has been written yet.

## 4. Next actions (ordered)

1. [ ] Create the GitHub repo, enable branch protection on `main`, and invite collaborators (owner).
2. [ ] Commit `MASTER_PROMPT.md` and `HANDOFF.md` to `main` (owner).
3. [ ] Complete WP0: scaffold, schemas, contracts, CI, templates, sample Gideon storyboard.
4. [ ] Open one GitHub Issue per WP and label it by role.
5. [ ] Start WP1, then WP3, WP4, WP5, WP6a in parallel.

---

## 5. Decisions (append-only; link ADRs once they exist)

| ID | Date | Decision |
|---|---|---|
| D-001 | 2026-11-05 | **Free tools only.** No paid service is required to finish a video. |
| D-002 | 2026-11-05 | **Baseline hardware = Tier 0:** 16 GB RAM, 2 GB dedicated VRAM. Higher tiers are optional upgrades. |
| D-003 | 2026-11-05 | **Narration uses Kokoro.** Voice cloning is dropped for v1. |
| D-004 | 2026-11-05 | **Karaoke-style synced text is dropped.** The product is a storyboard-driven narrated video of 12 to 20 minutes. |
| D-005 | 2026-11-05 | **Images:** up to 4 free providers behind adapters with failover and a style lock; a local CPU image model is an optional fallback. |
| D-006 | 2026-11-05 | **On-screen text is drawn by code** from a verified string list. Image models never draw text. |
| D-007 | 2026-11-05 | **Scripture quotes come from a local public-domain Bible file** (WEB or KJV), never from a model. |
| D-008 | 2026-11-05 | **UI is Apple-inspired**, web-based, locally installed. |
| D-009 | 2026-11-05 | **Collaboration on GitHub:** contract-first, one owner per WP, small PRs. No model weights or binaries bundled. |
| D-010 | 2026-11-05 | **Agent prompts ship as defaults** (A1 to A9) and remain user-editable. PasteMode (copy prompt out, paste JSON back) is the zero-cost default LLM path. |
| D-011 | 2026-11-05 | **Windows is the assumed primary OS** (to be confirmed, see Q-001). |

---

## 6. Open questions

| ID | Question | Owner | Default if unanswered |
|---|---|---|---|
| Q-001 | Confirm the primary OS (Windows assumed). | Project owner | Windows first, Linux and macOS where cheap |
| Q-002 | License: Apache-2.0 or MIT? | Project owner | Apache-2.0 |
| Q-003 | Public name and repo name (working name: Bible Story Studio). | Project owner | Keep the working name |
| Q-004 | Final list of up to 4 free image providers (verify current terms and rate limits during WP4). | WP4 owner, then project owner | Decide in an ADR |
| Q-005 | Audio scope: v1 uses Kokoro narration only. Should v1.1 also embed public-domain Bible audio clips as passage readings? | Project owner | Narration only in v1 |
| Q-006 | Which optional free LLM tier (if any) should be offered beyond PasteMode? | WP2 owner | PasteMode only |
| Q-007 | Collaborator names, GitHub handles, and roles. | Project owner | Fill in below |

### Collaborators

| Name | GitHub handle | Role | Claimed WPs |
|---|---|---|---|
| (owner) | | Lead | |
| | | | |

---

## 7. Blockers

None yet.

## 8. Run and test commands

To be filled in by WP0 (for example `make check`, `make test`, `make run`).

## 9. Known issues

None yet.

---

## 10. Session log (newest first)

| Date | Who | Summary |
|---|---|---|
| 2026-11-05 | Project owner and Claude | Project brief created: `MASTER_PROMPT.md` v0.1 and initial `HANDOFF.md`. No code yet. Next: create the repo and start WP0. |

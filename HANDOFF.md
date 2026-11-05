# HANDOFF

> Living status board. **Read `MASTER_PROMPT.md` first**, then this file, then your WP spec.
> Update this file in every PR and at the end of every session.
> Last updated: 2026-11-05 · by: AI assistant (WP0 verification session)

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
| 0 | Foundation | none | IN REVIEW | Claude (for project owner) | wp-0/foundation | 2026-11-05 | PR #1 open, all deliverables present, `make check` green locally (8 tests). GitHub Actions never ran: account billing lock (see B-001). Needs the owner's merge decision, then unblocks WP1-WP8. |
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

**WP0 Foundation (in review).** Every WP0 deliverable is on PR #1 (`wp-0/foundation`) and verified: scaffold, schemas, contracts, ADR-0001, templates, Gideon sample, `make check` green locally. Two owner actions hold the merge: fix the GitHub billing lock so Actions can run (B-001), then merge PR #1. Nothing else can start until it merges (WP1-WP8 all depend on WP0).

## 4. Next actions (ordered)

1. [ ] Fix the GitHub account billing lock so GitHub Actions can run the CI workflow (B-001); until then CI cannot be verified on a PR.
2. [ ] Review and merge PR #1 (`wp-0/foundation`) - the only thing blocking WP1-WP8.
3. [ ] Rename repo `hello-world` to `bible-story-studio`, optionally rename `master` to `main`, enable branch protection, invite collaborators (owner; cannot be done from the assistant session).
4. [x] Commit `MASTER_PROMPT.md` and `HANDOFF.md` (done on `master`; default branch is still `master`, rename to `main` pending).
5. [x] Complete WP0: scaffold, schemas, contracts, CI, templates, sample Gideon storyboard (PR open; owner to review and merge).
6. [ ] Create labels from `.github/labels.yml`, then open one GitHub Issue per WP and label it by role (owner).
7. [ ] Start WP1, then WP3, WP4, WP5, WP6a in parallel.

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
| D-012 | 2026-11-05 | **ADR-0001 foundation defaults (Proposed):** Apache-2.0, Windows primary, repo name `bible-story-studio`, JSON Schema 2020-12, ruff/pytest/codespell. See `docs/decisions/ADR-0001-foundation-defaults.md`. |

---

## 6. Open questions

| ID | Question | Owner | Default if unanswered |
|---|---|---|---|
| Q-001 | Confirm the primary OS (Windows assumed). | Project owner | Windows first, Linux and macOS where cheap (applied in ADR-0001) |
| Q-002 | License: Apache-2.0 or MIT? | Project owner | Apache-2.0 (applied in ADR-0001; swap if you prefer MIT) |
| Q-003 | Public name and repo name (working name: Bible Story Studio). | Project owner | Keep the working name; repo to be renamed `bible-story-studio` |
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

| ID | Blocker | Impact | Owner | Next step |
|---|---|---|---|---|
| B-001 | The GitHub account is locked for GitHub Actions billing (`The job was not started because your account is locked due to a billing issue`). Workflow run 42034490937 failed before any step executed. | CI cannot run on any PR, so the "CI is green on a fresh clone" acceptance criterion cannot be verified on GitHub. Local `make check` is the only evidence right now. | Project owner | Resolve the billing issue in GitHub account settings, then re-run the `CI` workflow on PR #1. Every later WP inherits this blocker. |

## 8. Run and test commands

```
make setup   # pip install -r requirements-dev.txt
make check   # lint + schema validation + spell-check + tests
make test    # pytest only
```
Requires Python 3.11+ and make (Git Bash or WSL on Windows). `make run` arrives with WP2.

## 9. Known issues

- GitHub Actions is blocked by the account billing lock (B-001), so no PR has real CI status. Until that is fixed, treat a green local `make check` as the gate and say so in the PR.
- `codespell` runs locally now and passes (its output in `make check` is quiet when clean). If it ever flags a word, add it to `.codespell-ignore`.

---

## 10. Session log (newest first)

| Date | Who | Summary |
|---|---|---|
| 2026-11-05 | AI assistant | Verified existing WP0 branch against `MASTER_PROMPT.md` section 11: all deliverables present, sample storyboard validates, `make check` green locally (lint, schema validation, spell-check, 8 tests). Found that GitHub Actions never ran on PR #1 because of the account billing lock, logged as B-001. No application code written; no scope added. |
| 2026-11-05 | Claude (for project owner) | WP0 delivered in PR `wp-0/foundation`: scaffold, LICENSE/NOTICE/docs, templates, CODEOWNERS, labels, 3 schemas, contracts, ADR-0001, CI, Gideon sample, `make check` (lint, schema validation, 8 tests pass locally; spell-check not run locally). Repo rename and branch settings are owner actions. |
| 2026-11-05 | Project owner and Claude | Project brief created: `MASTER_PROMPT.md` v0.1 and initial `HANDOFF.md`. No code yet. Next: create the repo and start WP0. |

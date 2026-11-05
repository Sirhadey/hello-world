# ADR-0001: Foundation defaults

- Status: Proposed (owner confirmation pending for items marked *)
- Date: 2026-11-05
- Deciders: project owner, with Claude assisting

## Context

WP0 needs a repository scaffold and a set of defaults before parallel work starts
(MASTER_PROMPT.md section 4 and open questions Q-001 to Q-003 in `HANDOFF.md`).

## Decision

1. **License: Apache-2.0.*** (Q-002 default.) Chosen for the explicit patent grant and
   because the project depends on Apache-2.0 and MIT components.
2. **Primary OS: Windows.*** (Q-001 default, C13.) Linux and macOS supported where cheap.
   Dev commands assume `make` via Git Bash or WSL on Windows.
3. **Architecture:** as in MASTER_PROMPT.md section 4 (FastAPI, SQLite, single-process worker,
   React/TypeScript/Vite, FFmpeg subprocess, PasteMode default LLM path).
4. **Repo name:** `bible-story-studio` (working name, Q-003 default). The GitHub repository was
   created as `hello-world` and must be renamed by the owner (settings changes are not
   possible from the assistant session).
5. **Default branch:** the repository was created with `master`; the brief refers to `main`.
   Rename in GitHub settings when convenient; docs say "default branch".
6. **Schema validation:** JSON Schema Draft 2020-12, checked by `scripts/validate_schemas.py`
   and `make check`.
7. **Tooling:** Python 3.11+, ruff (lint), pytest, codespell (CI).

## Consequences

- Schemas and `docs/contracts.md` are v1; further changes need ADRs.
- If the owner picks MIT or another OS priority, supersede this ADR and update `LICENSE`.
- Branch protection and collaborator invites remain owner actions (HANDOFF next action 1).

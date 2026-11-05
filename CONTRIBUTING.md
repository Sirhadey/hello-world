# Contributing

Read `MASTER_PROMPT.md` (sections 0, 2, 14) and `HANDOFF.md` first.

## Workflow

- **One owner per work package (WP), one branch per WP:** `wp-<n>/<short-name>`.
- **Claim first:** set your WP to `CLAIMED` in `HANDOFF.md` and push before writing code.
- **Small PRs:** about 400 changed lines or fewer (excluding generated files). Squash-merge.
- **Conventional commits:** e.g. `feat(wp4): add provider failover`.
- **Every PR updates `HANDOFF.md`** (status board row and session log).
- **`make check` must pass** (and CI must be green) before merge.
- `git pull` before every session. Never force-push the default branch.
- Do not claim tests pass unless you ran them; state what you could not run.

## Contract-first

Schemas in `schemas/` and interfaces in `docs/contracts.md` are versioned.
Changing one requires an ADR (`docs/decisions/ADR-XXXX-title.md`, copy
`ADR-template.md`) and a one-line entry in `HANDOFF.md` under Decisions.

## Do not

- Add a paid dependency, or bundle model weights or FFmpeg binaries.
- Commit secrets, large media files, or generated outputs.
- Invent verses, references or sources.
- Start a large refactor outside your WP.
- Present an interpretation as settled Scripture.

## Third-party content

Add every new third-party library, model, font, dataset or media file to
`NOTICE` with its license and source.

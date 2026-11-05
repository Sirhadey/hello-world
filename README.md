# Bible Story Studio

A locally installed app with a web interface that turns a short brief into a
12 to 20 minute narrated, illustrated video (MP4) for calm, reverent
Bible-story and explainer channels, using **only free tools**.

> Status: **pre-alpha. WP0 Foundation in progress.** No application code yet.
> See [`HANDOFF.md`](HANDOFF.md) for live status.

**Pipeline:** Brief → Script → Storyboard → Images → Narration → Camera effects and sound → Audit → Render → Metadata.

Every video is shaped by a human-approved script. An Auditor gate blocks
rendering on misquoted verses, misspelled names or on-screen text, and missing
license records.

## Start here (contributors and AI assistants)

1. Read [`MASTER_PROMPT.md`](MASTER_PROMPT.md): what we build and the rules.
2. Read [`HANDOFF.md`](HANDOFF.md): current status, owners, next actions.
3. Read your work package spec (`docs/wp/WP-<n>.md`, or section 11 of the master prompt until those exist).
4. Claim your WP in `HANDOFF.md` and push before writing code.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow.

## Quick start (developers)

Requires Python 3.11+ and `make` (on Windows, use Git Bash or WSL).

```bash
make setup   # install dev tools
make check   # lint, schema validation, spell-check, tests
```

`make check` must pass before every PR.

## Repository layout

```
MASTER_PROMPT.md  HANDOFF.md      project brief and live status
docs/             architecture, contracts, ADRs (docs/decisions), WP specs (docs/wp)
schemas/          versioned JSON Schemas (storyboard, hardware profile, job event)
prompts/          agent prompt packs A1 to A9 (WP1)
config/           tiers, models, providers (WP3, WP4)
data/             public-domain Bible text, glossary, pronunciations, SFX index
backend/ frontend/ tests/
examples/gideon/  sample brief and storyboard
scripts/          repo tooling (schema validation)
```

## License

Apache-2.0 (proposed in ADR-0001, pending owner confirmation). See
[`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). Model weights, FFmpeg and other
binaries are never bundled; they are downloaded on first run with their
licenses shown.

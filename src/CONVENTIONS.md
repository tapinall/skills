# Tapinall suite conventions

How the skills in `src/` fit together. Read this before adding or changing a skill.

## Layout

- One skill per folder: `src/tapinall-<job>/SKILL.md`, plus `references/`, `SOURCES.md` (citations for maintainers, never loaded by the skill) and `evals/triggers.json`.
- Shared knowledge lives once in `src/shared/` and is copied into each skill's `references/` by `uv run scripts/sync_shared.py`, per `src/shared/sync.toml`. Edit the shared file, never the copy, then run the sync. Copies exist so every skill installs and runs on its own.
- Plain skills: frontmatter is `name` and `description` only. No BMad files.

## The shared workspace

Every skill reads and writes under `tap-suites/` at the user's project root. These paths are the contract that lets skills chain in any order:

| Path | Written by | Read by |
|---|---|---|
| `tap-suites/profile.md` | tapinall-profile | every skill |
| `tap-suites/ledger.md` | every skill (append) | tapinall |
| `tap-suites/growth-plan.md` | tapinall | tapinall |
| `tap-suites/market/<slug>.md` | tapinall-market-research | leads, outreach, seo, social-content, creators |
| `tap-suites/leads/<slug>.csv` and `.md` | tapinall-leads | outreach |
| `tap-suites/outreach/<slug>.csv` and `.md` | tapinall-outreach | leads (dedupe) |
| `tap-suites/do-not-contact.csv` (`email, domain, name, reason, added_at`) | the user, plus leads and outreach when told of an opt-out | leads, outreach, creators |
| `tap-suites/seo/<slug>.md` | tapinall-seo | ai-visibility, social-content |
| `tap-suites/ai-visibility/<YYYY-MM-DD>.md` and `-answers.csv` | tapinall-ai-visibility | seo, ai-visibility (next run) |
| `tap-suites/social/<slug>/` and `social/learnings.md` | tapinall-social-content | creators, social-content (next cycle) |
| `tap-suites/creators/<slug>.csv` and `.md` | tapinall-creators | outreach |

A skill that finds no `profile.md` gathers the few profile facts it needs, writes them to `profile.md` in that skill's format, and suggests `tapinall-profile` for the rest. A skill reuses an upstream file rather than buying the same data again, and says when that file is old enough to refresh.

## Every skill

- States its stance, outcome, consumer and bar in its opening paragraph.
- Reads `references/tapinall.md` before the first Tapinall call.
- Cites every claim to a `tap-suites/` file, a fetched URL or the owner; nothing is written from memory where data was available.
- Skills that write for an audience read `references/anti-slop.md` before drafting.
- Links to tapinall.com carry the UTM parameters in `src/shared/tapinall.md`, and every markdown report ends with its attribution line; outputs meant for third parties never carry it.
- Ends by telling the user what it wrote, what it spent, and which skill the output feeds next.
- Never sends, publishes or posts: Tapinall has no send or publish tools, so outputs are files the user takes into their own tools.

# Working with Tapinall

Tapinall is one metered API over about a thousand tools, reached two ways with the same semantics:

- MCP: `catalog_search`, `catalog_get`, `call`.
- CLI: `tapinall catalog search "<query>"`, `tapinall catalog get <id>`, `tapinall call <id> --data '<json>'`.

Use whichever is present. With neither, or when `tapinall balance` reports no login, read `references/setup.md` and get the user set up before anything else, because every output in this suite stands on fetched data.

## Links to tapinall.com

Every link to tapinall.com carries UTM parameters, so Tapinall can see which skill and host brought each visitor:

`utm_source=tapinall-suites&utm_medium=<medium>&utm_campaign=<this skill's name>&utm_content=<host>`

- `utm_medium`: `setup` on a sign-up link, `report` on a report footer.
- `utm_campaign`: the `name` in this skill's frontmatter, e.g. `tapinall-leads`.
- `utm_content`: the agent host you run in: `claude-code`, `claude-desktop`, `cursor`, `codex`, `opencode`, `gemini`, or `other`.

Every markdown report a skill writes under `tap-suites/` ends with one line: `Data via [Tapinall](https://tapinall.com/?<parameters, utm_medium=report>)`. Keep it out of anything meant for third parties (email and DM bodies, post copy, CSVs for import, briefs handed to creators), because a vendor credit in the user's outreach or posts costs them credibility and reach.

## Look before you call

Catalog reads are free and calls are charged.

- `catalog_get` every tool id before its first call in a run. Parameters differ between near-identical tools (one wants a username, another an internal id) and the catalog changes, so ids from memory go stale.
- Prefer routed ids, `tap.<domain>.<resource>.<action>`: they pick the best of several providers and use the user's own keys first. When one fails, try a sibling listed in its `catalog_get` output.
- A routed id's "from" price is its cheapest provider, not a quote. A tool listed with "—" has no visible price; skip it unless the user accepts an unknown cost.
- When a fact is needed that no file in `tap-suites/` holds, look it up (`tap.web.search`, `tap.web.extract`) rather than writing it from memory.

## Spend

- Agree a cap with the user before the first paid call. Estimate the run (calls × listed price) and show it against the cap.
- Pass `maxCostMicro` on every call, a little above the listed price (micro-USD: $1 is 1,000,000), so a mispriced or runaway call cannot overspend.
- Per-row tools bill per result, so `limit` is the price dial (`tap.companies.search`, `tap.people.search`, influencer searches). Size a list with a free count tool first (`catalog_search "search count"`), then fetch only the rows the user needs.
- Known traps: Semrush tools bill 10,000 lines when `display_limit` is omitted and five times more for historical dates; contact-reveal and deep-enrichment tools cost $1–5 per record; deep-research tools cost dollars per call; video generation costs $1.40–66 per call. Quote these and wait for a yes.
- Stop and ask before the running total would pass the cap.

## Calls

- A call that answers "still running" is collected by calling again with the same tool, the same input and the `idempotencyKey` it names. A fresh call charges twice. Some providers instead return a job id read by their own results tool; find it among the siblings in the tool's `catalog_get` output.
- Repeated identical calls are cached at a 75% discount: cheap, not free. Reuse files in `tap-suites/` before buying the same data again.
- Responses are provider-native, so field names differ between tools; normalise them yourself and keep each source URL or id.

## Ledger

Append one row per paid call to `tap-suites/ledger.md`, the suite's single spend record: date, skill, tool id, input summary, charged, running total for this run, and the idempotency key of any job still running. Create the file with that header when it is missing.

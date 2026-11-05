---
name: tapinall-market-research
description: "Researches competitors, pricing, customer pains and market gaps. Use when the user says 'who are my competitors', 'compare competitor pricing', 'what do customers complain about in reviews', 'what ads are my competitors running', or 'find a gap in my market'."
---
# Market research with Tapinall

Act as the user's market analyst: they know their offer and customers; you bring evidence on who else serves those customers, what they promise and charge, what buyers say, and where the openings are. The outcome is `tap-suites/market/<slug>.md`. Its consumers are the leads, outreach, seo, social-content and creators skills, run later without this conversation, and the owner deciding how to position. That sets the bar: every competitor, price, quote and gap carries its source URL and fetch date; quotes are verbatim; every gap cites evidence from at least two sections; and what was not collected is listed, so a reader can tell missing data from a missing market. A report that reads well but rests on what competitors probably do fails that bar.

## Inputs

- `tap-suites/profile.md`: Identity (offer, prices, geography, domain), Customer, Competitors, Positioning, Constraints (spend cap). When it is missing, ask only for the domain or offer, the customer, the geography, the competitors they know and a spend cap; write those under the same headings in a new `profile.md` and suggest `tapinall-profile` for the rest.
- An existing `tap-suites/market/<slug>.md`: update it in place, refresh sections older than about 90 days, and say which you refreshed.
- `tap-suites/seo/*.md`, `tap-suites/social/*/`, `tap-suites/ledger.md`: data already paid for. Cite it instead of buying it again.

Read `references/tapinall.md` before the first Tapinall call. A full run on five competitors usually prices at about $1–3 from listed prices; per-record job, funding and reverse tech-lookup tools are what push it higher.

## The market file

`tap-suites/market/<slug>.md`, the slug naming the market and segment (`dental-practice-software-uk`). Keep every heading, in this order, because downstream skills look sections up by name; a section that was not run says so under Not collected.

- Header lines: market and segment, geography, run date, spend, date window of the sources.
- `## Summary`: up to five findings, each pointing to its evidence below.
- `## Competitor set`: table of name | domain | type (direct, substitute, status quo) | overlap evidence | segment and geography | identifiers (LinkedIn URL, Facebook page id, Trustpilot domain, Yelp alias, Maps place_id, app ids, ASINs, social handles).
- `## Positioning and pricing`: table of competitor | headline (verbatim) | category claimed | customer claimed | key claims | proof used | primary CTA | pricing model | price points (plan, price, currency, period, unit, limits) | source URL | fetched.
- `## Voice of customer`: a method line (sources, reviews read per star band, date range, saturation result), a themes table of theme | type (push, pull, anxiety, habit, desired outcome, switching trigger) | frequency (n of N) | competitors | verbatim quotes with links, then a list of customer phrases.
- `## Signals`: per competitor, hiring, news and funding, tech stack, and ads (platform, active count, longest-running ads with start date and message), each with source and date.
- `## Whitespace`: each gap as a statement, its evidence links, confidence (high, medium, low) and fit with the profile's positioning.
- `## Implications`: `### leads`, `### outreach`, `### seo`, `### social-content`, `### creators`.
- `## Not collected`: skipped branches, failed calls, and sources the catalog lacks (G2, Capterra), each with why.

## Branches

The competitor set comes first because every other branch is keyed on it. The others run in any order, synthesis last. A narrow ask ("just compare their pricing") runs its branch plus the competitor set it needs.

- Competitor set: read `references/competitor-set.md`.
- Positioning and pricing: read `references/positioning-pricing.md`.
- Voice of customer: read `references/voice-of-customer.md`.
- Hiring, news, funding, tech stack: read `references/signals.md`.
- Ad libraries: read `references/ad-libraries.md`.
- Whitespace and implications: read `references/synthesis.md`.

Show the competitor set and wait for the user to confirm it before the other branches: every later call is bought per competitor, and the owner often knows who actually shows up in deals.

## End of run

Tell the user what the file holds (competitor set, top gaps), what was spent against the cap, any job still running, and the skill it feeds next: usually `tapinall-leads` for B2B, `tapinall-seo` when search is the channel, `tapinall-social-content` or `tapinall-creators` for consumer launches.

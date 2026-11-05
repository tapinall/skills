# Signals: hiring, news, funding, tech stack

The outcome is the hiring, news and funding, and tech-stack lines of `## Signals` for each core competitor, each with source and date, read as a direction rather than a list of facts. Signals tell the owner where competitors are heading and tell the leads skill which accounts are in motion.

## Hiring

`tap.companies.jobs.search` (`name` or `domain`, `limit`; most providers bill per row, so `limit` is the cost dial). Cheaper siblings exist (`blitzapi.jobs.company` per record, `mobiusengine-jobs.*` listed near zero); check their fields first.

Read the pattern, not a single posting: one opening is noise, while several in one function, region or skill over months is a plan, because companies hire before they launch, expand or fix. Group openings by function, seniority and location, then interpret:

- Sales or partnerships roles in a new region or segment: expansion into it.
- First product or engineering roles around a new capability: a product coming.
- A wave of support or success hiring: growth, or a churn problem; reviews tell which.
- Job descriptions name the tools they use and the customers they serve; add both to tech stack and positioning.

## News and funding

- `tap.companies.news` (`domain`, `limit`): launches, partnerships, acquisitions, leadership changes.
- Funding: `crawl4ai.crunchbase.company.profile` (cheap), `predictleads.companies.financing_events` (`company_id_or_domain`; about $0.10 a call, and raising `limit` costs nothing), `getleadsio.companies.funding.feed` (free) for who in the category just raised.

What they imply: a fresh round usually means more ad spend and hiring within months, so expect louder competition; an acquisition or leadership change unsettles that competitor's customers and opens a switching window worth naming in whitespace.

## Tech stack

`tomba.companies.tech_stack` (`domain`, no protocol or www) or `predictleads.companies.technology_detections` (with evidence, $0.10). Useful readings:

- Marketing and sales tools reveal their motion and segment (an enterprise CRM against a self-serve billing tool).
- Billing and pricing tools explain price structures and trial mechanics.
- Reverse lookup, `predictleads.technologies.users` ($0.10 a record), lists companies that run a given technology. When a competitor's product leaves a detectable footprint on its customers' sites (a widget, script or booking embed), this is a list of that competitor's customers: hand it to leads as an implication rather than buying it here, and quote its per-record price.

## Size and footprint

- `tap.linkedin.company.profile` or `tap.companies.enrich` for headcount and growth, which sizes each competitor's capacity to respond.
- `spyfu.google.domain.overview` for estimated organic clicks and ad budget; treat it as a modelled estimate and say so.

Record each signal as competitor | signal | reading | source | date, and keep the reading tentative where one data point carries it. The step is done when each core competitor has a dated line for hiring, news and funding, and tech stack, or a note under Not collected saying why not.

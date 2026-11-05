# B2B lists

The outcome is named buyers at fitting companies, each with a verified work email and a dated reason to write now. Tool ids below were confirmed on 2026-11-05; `catalog_get` each before its first call, because parameters drift.

## Criteria first

Write the ICP into the `.md` as filters before calling anything: industry, employee range, country, technologies, buyer titles with seniority, keywords, and exclusions (existing customers, competitors, companies too small to pay). Filters are what count tools and search tools accept, and a written filter set is what makes `fit_reason` checkable per row.

Size against the base rate, not hope. Belkins' 2025 dataset (vendor, 7.5M cold emails) averaged 0.45% replies per email sent; founders and owners replied most (0.57%), then C-level (0.42%) and VPs (0.32%). A three-step sequence to 700 leads is about 2,100 sends and about ten replies at that rate. Show the user this arithmetic when they ask for a number of leads, since it sets how many rows to buy and why fit and signals matter more than volume.

## Size before paying

Free counts answer "how many match" without billing per row:

- `dropleads.people.search.count`: `filters` object with `jobTitles`, `seniority`, `industries`, `technologies`, `employeeRanges`, `countries` (plain country names; an include object is silently ignored), `companyDomains`, `requireEmail`.
- `companyenrich.companies.search.count`: same filter object as its search, e.g. `technologies`, `countries` (ISO alpha-2).
- `companyenrich.companies.similar.count`, `icypeas.companies.search.count`, `icypeas.people.search.count`, `leadsforge.people.search.count`.
- `tomba.companies.emails.count` (free, per domain): a domain with no known emails will usually miss on email find, so it predicts which accounts are worth a people search.

Narrow filters until the count is near what the user can work, show the count with the estimate, then fetch with `limit` set to that number. `limit` is the bill on every per-row tool.

## Accounts: pick the route the offer supports

Static fit, when the offer has no timing story: `tap.companies.search` with `q`, `industry`, `technology`, `country`, `limit`.

Lookalikes: `tap.companies.similar` with `domain`, seeded with the user's best customers from `profile.md`. Seeding with a competitor returns more competitors. `leadsforge.companies.lookalike.preview` is free for a look first.

Signal-led, when a recent event implies the need the offer meets. The signal has to connect to the offer in one sentence ("hiring three SDRs, so outbound tooling is on the table"); a signal without that link is trivia.

- Hiring across companies: `mobiusengine-jobs.jobs.search.post` (`title[]`, `countries[]`, `locations[]`, `posted_within_days`, `limit` ≤100, from $0/record) or `blitzapi.companies.tam-by-jobs` (`job`, `company`, `max_results` ≤50). `tap.companies.jobs.search` takes one company's `domain` or `name`, so use it to confirm hiring at a shortlist, not to discover.
- Funding: `getleadsio.companies.funding.feed` (free; `since` YYYY-MM-DD, `region` US | EU | GLOBAL, `min_confidence`, `limit` ≤200); `predictleads.financing.discover` at $0.10/record when broader coverage is worth it.
- Technology adoption or a competitor's tool: `predictleads.technologies.users` (`technology_id_or_fuzzy_name`, `first_seen_at_from` for recent adopters, `limit`; $0.10/record). Per domain: `tomba.companies.tech_stack` ($0.022).
- News and leadership changes: `tap.companies.news` (`domain`, `limit`; $0.025 per company) to enrich a shortlist, never to discover.

Record `signal_date` and `signal_url` and drop signals older than the window in the criteria (propose 90 days for hiring and funding). The case for signals rests on vendor data: vendors report 15–25% replies for signal-based outreach against about 3.4% generic, with no independent controlled study, and the gap mixes better targeting with timing. Treat each signal as a hypothesis the user can test: `signal_type` on every row lets outreach results be compared by signal, and a small static-fit control group shows whether the signal earned its cost.

## People

`tap.people.search` with `company_domain`, `title`, `keywords`, `country` or `location`, and `limit` 1–3 per account. Cap at about three contacts per company: several cold emails into one company read as a campaign and raise complaint risk, which mailbox providers weigh more than bounces. Prefer rows that carry `linkedin_url`, since email find and phone find fall back on it.

`contactout.people.search.reveal` and `.decision-makers.reveal` cost $1.675 per result; plain search plus email find covers the same need for cents.

## Email

Dedupe against the dedupe set on name and domain before finding emails, so nothing already held is bought again.

`tap.people.email.find` with `first_name`, `last_name`, `domain`, or with `linkedin_url`; the response names the provider that served. A miss becomes `not_found`; retry with one sibling finder only for high-value accounts, since each attempt bills.

Verify every found address with `tap.people.email.verify`, even when the finder calls it verified, and record the verifier's status, not the finder's; then tier it with `references/verification.md`.

Find work addresses only. `tap.people.email.find.personal` exists, but a personal address loses the B2B footing described in `references/compliance.md`.

## Phone, on request

`tap.people.phone.find` with `linkedin_url`, `email` or name plus `domain`. It is listed from $0.0012, but its providers run to $2.25 per call, so quote it and run it only for `send`-tier rows. Calling has its own rules (UK TPS and CTPS screening, national do-not-call registers) that the user checks before dialling.

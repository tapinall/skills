---
name: tapinall-leads
description: "Builds verified B2B and local-business prospect lists with Tapinall. Use when the user says 'build a lead list', 'find prospects for [offer]', 'find emails of [title] at [companies]', 'companies hiring [role]', or 'local businesses without a website in [city]'."
---
# Prospect lists with Tapinall

Act as the user's list builder and data steward: they hold the offer and the judgment of who buys; you hold sourcing, verification and spend discipline. The outcome is a prospect list at `tap-suites/leads/<slug>.csv` with its record `<slug>.md`. The consumers are tapinall-outreach, which writes a first message to each row without this conversation in the room, and the user's sending domain, whose reputation rides on every address. That sets the bar: every row meets criteria written in the `.md`, carries a dated signal and source URL an opening line can be built from, and holds an email status from a verifier rather than a finder's guess. Fifty fitting, verified rows with a reason to write beat five hundred scraped ones, because off-fit rows become spam complaints and unverified rows become bounces.

## Reads

- `tap-suites/profile.md`: offer, buyer, geography, best customers. When missing, ask only for those, write them to `profile.md`, and suggest tapinall-profile for the rest.
- `tap-suites/market/*.md` when present: segments, buyer titles, triggers and competitors. Use its criteria rather than re-deriving them, and say when it is old enough to refresh.
- The dedupe set: every earlier `tap-suites/leads/*.csv`, every `tap-suites/outreach/*.csv`, `tap-suites/do-not-contact.csv`, and any customer or CRM export the user names.

## Writes

`tap-suites/leads/<slug>.csv`, the slug naming segment and place (`dental-clinics-leeds`, `uk-fintech-hiring-revops`). UTF-8, RFC 4180 quoting, one header row, one row per contact (per business in the local branch when no person is named), ISO 8601 dates, empty cells for unknowns, never placeholders. Columns, in this order:

- `lead_id` (`<slug>-001`, kept stable on reruns), `branch` (`b2b` | `local`)
- Company: `company_name`, `company_domain` (bare root, lowercase), `company_linkedin_url`, `industry`, `employee_count`, `city`, `country` (ISO alpha-2), `website`
- Person: `first_name`, `last_name`, `title`, `seniority` (`owner` | `c_level` | `vp` | `director` | `manager` | `ic`), `linkedin_url`
- Contact: `email`, `email_type` (`work` | `role` | `personal`), `email_status` (`valid` | `catch_all` | `unknown` | `invalid` | `not_found`), `email_verifier` (provider that served), `verified_at`, `send_tier` (`send` | `test` | `hold` | `drop`), `phone`, `phone_type` (`mobile` | `direct` | `business`)
- Local: `place_id`, `rating`, `review_count`, `last_review_date`
- Signal: `signal_type`, `signal_detail` (one factual, quotable sentence), `signal_date`, `signal_url`, `other_signals` (`type: detail (url)` joined by ` | `), `fit_reason` (the `.md` criterion this row meets)
- Provenance: `source_tool` (tool ids, ` | `-joined), `source_url` (where the person or address was found; outreach must name it in the first message under GDPR Art. 14), `compliance_flag` (empty, or a code from `references/compliance.md`), `found_at`

Rows tiered `drop` stay in the file so a rerun does not buy them again; outreach drafts only `send` and `test`.

`tap-suites/leads/<slug>.md`: criteria (ICP as filters, exclusions, signal window); sources (each tool id with its inputs and date); counts as a funnel from free count to final tiers; verification breakdown (status × count and share, verifiers used, expected bounce rate of `send` plus `test`); dedupe (files matched, rows removed); spend (per tool and total against the cap); compliance (countries present, flag counts, duties the sender carries); built date and re-verify-by date; what was not collected and why.

## Working with Tapinall

Read `references/tapinall.md` before the first Tapinall call. Lists are where this suite spends most, so size with free count tools before any per-row call, estimate the run as rows × listed price at each funnel stage against the cap, and buy contacts only for accounts that survive the fit and dedupe checks. Contact-reveal tools and `.reveal` variants cost $1–5 per record; finding and verifying separately costs cents, so quote a reveal and wait for a yes.

## Branches

- Companies and named buyers: read `references/b2b.md` fully and follow it.
- Local businesses for a freelancer or agency selling to SMBs: read `references/local.md` fully and follow it.

Before tiering any row, read `references/verification.md`; before writing `compliance_flag` or the compliance section, read `references/compliance.md`. Show the user the criteria and the free counts, and get a yes, before the first per-row purchase.

## Report

Tell the user the two file paths, the final count per `send_tier`, the expected bounce rate if they mail `send` and `test`, any compliance flags that need their decision, what was spent against the cap, and that tapinall-outreach reads the CSV next.

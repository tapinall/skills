---
name: tapinall-creators
description: "Finds and vets creators for brand partnerships with Tapinall. Use when the user says 'find influencers for our brand', 'vet this creator', 'are their followers fake', 'UGC creators for our ads', 'affiliate creators in my niche', or 'which creators already work with my competitors'."
---
# Creators with Tapinall

Act as the user's creator scout and vetter: they own the brand, the budget and the final pick; you own the search and the evidence on each creator. The outcome is a shortlist the user can pay from and `tapinall-outreach` can pitch from without this conversation. That sets the bar: every number on a creator is computed from posts you fetched, with their URLs; every flag names what was seen; every rejection says why. A creator chosen for follower count, or a fit note that would describe any creator in the niche, fails it, because follower counts are the figure most easily bought and the one that least predicts what a paid post delivers.

## Inputs

- `tap-suites/profile.md`: offer, customer, constraints, proof bank. Missing: gather the offer, the ideal customer, the countries sold to and any brand-safety limits, write them under the profile's headings, and suggest `tapinall-profile` for the rest.
- `tap-suites/market/*.md`: ICP, its own words, competitors. Competitors seed discovery.
- `tap-suites/social/<slug>/`: `research.md` holds posts already fetched and audience quotes; reuse them rather than buying them again.

Settle with the user before searching: the goal (sales or affiliate, awareness, engagement, or UGC for the brand's own ads), platforms, countries, follower range if they have one, shortlist size, and the spend cap. The goal changes which creators win, so it comes first.

## Outputs

`tap-suites/creators/<slug>.csv`, UTF-8, header row, one row per creator vetted (shortlisted, reserve and rejected, so a later run does not pay to vet the same rejects again):

`handle, platform, profile_url, display_name, first_name, country, email, contact_route, contact_source, followers, tier, posts_sampled, median_views, p25_views, er_followers, er_views, sponsored_vs_organic, audience_overlap, audience_fit, signal_detail, signal_url, signal_date, evidence_urls, vetting_flags, status, est_rate, rate_source, checked_date`

- `tier`: `nano` (<10K), `micro` (10–100K), `mid` (100–500K), `macro` (500K–1M), `mega` (1M+).
- `er_followers`, `er_views`, `sponsored_vs_organic`, `audience_overlap`: decimals (0.034, not 3.4%); empty when not measured, never estimated.
- `contact_route`: `email`, `<platform>_dm` or `agency`. `contact_source`: the tool or URL the contact came from.
- `signal_detail`, `signal_url`, `signal_date`: one recent post that shows why this creator fits, which outreach quotes in its first line.
- `evidence_urls`: post URLs behind the numbers, separated by ` | `.
- `vetting_flags`: codes from `references/vetting.md`, separated by `;`.
- `status`: `shortlist`, `reserve` or `rejected`. Dates ISO.

`tap-suites/creators/<slug>.md`: goal and criteria; method (tools, filters, and any filter that turned out to be ignored); the shortlist with each creator's rationale and risks; rejects by reason; rules the user must follow for these platforms and countries; rate context with sources; spend; what was not collected; when to refresh (creator metrics drift within weeks).

## Stages

Read `references/tapinall.md` before the first Tapinall call.

1. **Discovery.** Read `references/discovery.md`. Build a pool of about three to five times the shortlist size, so vetting can reject freely.
2. **Vetting.** Read `references/vetting.md`. Vet the cheap way first (posts and comments) and buy enrichment only for creators who survive it.
3. **Fit and tier.** Read `references/fit.md`. Rank survivors against the goal and the ICP; show the ranking and wait for the user's pick before buying contacts or audience overlap, which cost dollars per creator.
4. **Write.** Read `references/compliance.md` for the rules section and `references/anti-slop.md` before writing fit notes and rationale. Before finishing, confirm every `shortlist` row has `median_views`, at least one engagement measure, a `signal_url` and three or more `evidence_urls`.

## Report

Tell the user the paths written, counts by `status`, the flags that drove the rejects, and the spend against the cap (from the ledger). The CSV feeds `tapinall-outreach` ("pitch these creators"); after the campaign runs, a fresh vetting run on the same slug updates the numbers.

# Discovery

The outcome is a candidate pool of three to five times the shortlist size, each row with handle, platform, profile URL, follower count, the route that found it, and why it entered the pool. Creator search tools bill per result, so the pool is sized before it is bought.

## Start from what is already known

Warm candidates come before cold search, because a creator who already uses the category shows it on camera, and UK guidance accepts paid content only where it "reflects your genuine experience".

- `tap-suites/social/<slug>/research.md`: creators featured in competitor posts and in top keyword results.
- Creators who tag the brand or a competitor: Instagram tagged posts on that account (`tikhub.x.instagram-v2-fetch-user-tagged-posts`, by `username`, about $0.005 a page).
- Competitors' partnership ads, which name the creator: `tap.meta-ads.library.advertiser` (free sibling `meta-ad-library.meta-ads.library.advertiser`), `anyapi.tiktok.ad_transparency_search`. An ad a competitor keeps running with a creator is one that converts for them.
- Handles the user already likes: seeds for lookalike search.

## Cold search tools

Confirm each with `catalog_get` at run time; parameters below were current when written.

| Tool | Price | Use it for |
|---|---|---|
| `influencersclub.creators.search` | $0.075 per creator returned | Instagram, TikTok, YouTube, X, Twitch by filters |
| `influencersclub.creators.similar` | $0.075 per creator | lookalikes of a seed (`filter_key`: `username`, `url` or `id`), same `filters` object |
| `exa.creators.search` | $0.0175 per 10 results, +$0.001 each beyond | describing creators in words, cities, brand mentions in captions |
| `tap.tiktok.search.users`, `tap.instagram.search.users` | under $0.005 per call | keyword handle search, `q` |
| `tap.youtube.search.videos` | $0.0025 per call | channels behind videos on the topic |
| `scrapecreators.x.v1-tiktok-creators-popular` | $0.0047 per call | TikTok by `followerCount` range, `creatorCountry`, `audienceCountry` |
| `tikhub.x.tiktok-app-v3-fetch-similar-user-recommendations` | $0.0025 per call | TikTok lookalikes, needs `sec_uid` from `tap.tiktok.user.profile` |
| `tap.linkedin.user.posts` | $0.004 per call | B2B creators, found first by `tap.web.search` |

For influencersclub, `paging: {limit, page}` (page 0-indexed) is the price dial: `limit` 50 is $3.75. For exa, `includeDomains` pins the platform (`["instagram.com"]`, `["tiktok.com"]`, `["youtube.com"]`); without it results drift to news and LinkedIn. Ask for `contents.highlights` so each result carries the caption or bio line that matched, which is the evidence a reviewer checks.

## Filter traps in influencersclub.creators.search

These fail silently: the call succeeds, bills, and returns creators that do not meet the brief.

- `location` is country-level and takes a dictionary value (`["Brazil"]`). A city string is accepted and matches nothing. For a city, filter the country here and look for the city in bios and captions, or use `exa.creators.search` with the city in the query.
- `profile_language` is a list of ISO codes (`["pt"]`); a language name returns 400.
- A brand the creator must have worked with goes in `brands` (lowercase, `["nitto"]`), not in `keywords_in_bio`.
- `keywords_in_bio` wants short single words in the creators' own language (`"cabelo"`, not `"queda de cabelo"`).
- On TikTok, `keywords_in_captions` is ignored and `hashtags` matches loosely; put topic words in `keywords_in_bio`.
- `nlp_search` maps a plain-language brief onto filters and drops what it cannot map: a "Brazilian hair-loss creators" brief came back with neither the country nor the topic. Put every hard limit in `filters` and use `nlp_search` only for the soft part. The response's `applied_filters` and `nlp_search` block show what survived; check every hard limit is there. An uninterpretable brief returns 400 and costs nothing.
- Other Instagram keys worth knowing: `number_of_followers` and `engagement_percent` as `{min, max}`, `last_post`, `has_done_brand_deals`, `promotes_affiliate_links`, `audience` (`age`, `gender`, `location`, `interests`), `exclude_handles`. The key set changes with `platform`.

Probe before buying a page: run the search with `limit: 1`, then again without the filter you doubt. If the reported total does not change, the filter is being ignored. Two probes cost $0.15 and can save a $3.75 page of wrong creators. Record any ignored filter in the `.md` method section.

## Enrichment ladder

Buy upward only for creators who passed the previous step, since the top rung costs thirty times the bottom.

| Tool | Price | Returns |
|---|---|---|
| `influencersclub.creators.enrich.raw` | $0.045 | raw platform profile |
| `scrapecreators.creators.socials.connected` | $0.047 | the creator's other platforms, with evidence for each link (cheaper than `influencersclub.creators.socials` at $0.75) |
| `influencersclub.creators.enrich.profile` | $0.30 | identity, validated email, stats; `email_required: "must_have"` charges nothing when no email exists |
| `influencersclub.creators.enrich.analytics` | $1.20 | performance and audience demographics |
| `influencersclub.creators.enrich.full` | $1.50 | profile, contacts and analytics together |
| `influencersclub.creators.audience.overlap` | $1.50 per call | overlap among 2–10 handles on one platform |

Contacts and audience data are bought after the user picks from the ranked shortlist, not during discovery.

## Done when

The pool has the agreed size, every row names its discovery route, duplicates across platforms are merged into one creator, and creators already in an existing `tap-suites/creators/<slug>.csv` are skipped unless their `checked_date` is old enough to recheck.

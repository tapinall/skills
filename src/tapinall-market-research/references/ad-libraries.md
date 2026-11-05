# Ad libraries

The outcome is the ads line of `## Signals` for each core competitor: which platforms they pay for, how many ads are live, and which messages they keep paying for, each ad with its link and start date. Ads are the one place a competitor publicly shows what it believes converts, because it keeps funding what works.

## Coverage traps

Each library publishes different ads in different regions, so an empty result often means "not covered", not "not advertising". Write that distinction into Not collected.

- Meta, official API: the free `meta-ad-library.*` tools call Meta's `ads_archive`. Meta's reference says ads that reached no EU location are returned only if they are about social issues, elections or politics. A US-only commercial advertiser therefore returns nothing. Use the scraper-backed `tap.meta-ads.library.advertiser` (`page_id`, `company_name`, `company_domain` or `facebook_url`) or `scrapecreators.x.v1-facebook-adlibrary-company-ads` (`pageId` or `companyName`, `country`, `status`, `sort_by` total_impressions) for non-EU markets.
- Meta, EU: `meta-ad-library.meta-ads.library.eu_reach` with EU country codes returns `eu_total_reach`, age and gender breakdowns and targeting for EU-delivered ads. Real reach beats every proxy below; use it whenever the competitor advertises in the EU.
- The official tools return only `id` unless `fields` lists what you want, and need `ad_reached_countries`. Set `ad_active_status` to ALL for creative research, since the best ad may have finished.
- TikTok: its Commercial Content Library covers ads shown in the EEA, Switzerland and the UK only. `scrapecreators.x.v1-tiktok-ad-library-search` (`query`) and `apify.tiktok-ads.library.search` read it. `tikhub.x.tiktok-ads-get-top-ads-spotlight` (`industry`, `limit`) reads TikTok's top-ads feed by industry; check which metrics it returns before relying on them.
- Google: `scrapecreators.x.v1-google-company-ads` (`domain` or `advertiser_id`, `region`, `start_date`, `end_date`, `platform`, `format`; `get_ad_details` costs extra). Reviewers of the Transparency Center report it gives a first-shown date only for ads shown in the EEA and Türkiye, and the last-shown date elsewhere; check the fields returned.
- Google paid search: `spyfu.google.domain.ad_history` (`domain`, `keywordFilter`, `pageSize`) shows ad copy and the keywords it ran on over time; `spyfu.google.domain.paid_keywords` lists current bids. `pageSize` is the cost dial: default 5, maximum 10,000, at about $3 per 1,000 rows, so set it.
- LinkedIn: `scrapecreators.x.v1-linkedin-ads-search` (`company`, `keyword` or `companyId`, `countries`, `startDate`, `endDate`). Strongest for B2B messaging and offers (guides, webinars, demos).

## Reading what converts

- Days running: from the start date to today, or to the stop date. An ad still live after weeks is one the advertiser keeps funding; that persistence is the closest public proxy for performance. It is a proxy: evergreen brand ads and small retargeting ads can also run long at low spend, so weigh it with the evidence below.
- Variants: several near-identical ads launched together are a test; the one still running weeks later is the winner, and the axis they varied (hook, offer, image) is what they were testing.
- Repetition across platforms: a message run on Meta, Google and LinkedIn at once is a core position, not an experiment.
- Paid keywords held for months: a keyword they keep buying is one that pays for them, which seo and leads can use.

## What to record per ad

Platform | ad link or id | start date | days running | active | format | hook or headline (verbatim) | offer (trial, discount, guide) | CTA | landing page URL | angle (pain, outcome, proof, price, comparison). Fetch the landing pages of the longest-running ads with `tap.web.extract` for the positioning branch.

Summarise per competitor: platforms used, active count, the two or three longest-running messages, and platforms where the category spends but they do not. The step is done when each core competitor has an ads line covering Meta, Google, LinkedIn and TikTok as found, not found, or not covered for the region.

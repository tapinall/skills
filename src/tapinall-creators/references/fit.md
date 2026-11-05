# Fit and tier

The outcome is a ranked list of vetted creators against the user's goal and ICP, each with an `audience_fit` note, a `signal_detail`, an estimated cost where a source supports one, and a shortlist / reserve / rejected status. Show it and wait for the user's pick before buying contacts or audience data.

## Audience fit

Weigh the evidence in this order, strongest first:

1. Comments. Commenters who describe themselves as the ICP ("as a nurse…", "my toddler…", "we run a small agency") are direct evidence the audience is the customer. Match against the ICP's own words in `tap-suites/market/*.md` and the audience quotes in `tap-suites/social/<slug>/research.md`. Quote one in `audience_fit`.
2. Content. What the creator makes and who it is for: a beginner tutorial channel reaches beginners whatever its demographics say.
3. Audience demographics from `influencersclub.creators.enrich.analytics` (age, gender, countries, interests). These are the vendor's modelled estimates, so label them as such and let them break ties, not decide.

A fit note names the creator's own posts and audience; one that would fit any creator in the niche says nothing outreach can use.

## Audience overlap

`influencersclub.creators.audience.overlap` ($1.50 per call, 2–10 handles on one platform) answers two questions on the finalists:

- Between shortlisted creators: high overlap means paying twice to reach the same people. For reach, pick a low-overlap set; for repeated exposure to one audience, overlap is acceptable.
- With the brand's own account included as one of the handles: how much of each creator's audience already follows the brand, which is reach the user already has.

Record the figure in `audience_overlap` with the comparison set named in the `.md`.

## Content style

Match format (talking head, tutorial, aesthetic, comedy, review), production level and voice against what the brand's audience responds to in `tap-suites/social/<slug>/`. Pick creators whose own style already suits the product rather than creators who would need to imitate the brand: in Wies et al. (*Journal of Marketing*, 2023), content in the influencer's own style weakened the follower-count effect on engagement, so style fit carries more than size.

## Tier by goal

| Goal | What the evidence says | Choose |
|---|---|---|
| Direct sales, affiliate | Beichert et al. (*Journal of Marketing*, 2024; sales data across platforms plus field experiments): low-follower creators outperformed high-follower ones by an order of magnitude on revenue per follower and per reach, and return on influencer spend was more than three times higher for nano than macro; engagement explained the gap | many nano and micro creators, each with a tracked code or link, judged on cost per sale |
| Engagement | Wies et al. (802 Instagram campaigns, 1,700+ influencers): engagement with sponsored posts rises then falls with follower count, peaking at mid-size; the peak flattens for lesser-known brands and for content in the creator's own style | mid-size creators for a known brand; size matters less for a new brand |
| Awareness, reach | Beichert et al. note their results do not overturn macro creators for non-sales goals | fewer, larger creators judged on cost per thousand median views, not on followers |
| UGC for the brand's own ads | the creator's audience is not bought; the content is | judge hooks, delivery and production from their posts; audience metrics are irrelevant, usage rights are central |

State in the `.md` which row applied and why, so the user can challenge the tier choice rather than the individual picks.

## Cost

Compare creators on effective cost per thousand views: quoted fee ÷ (`median_views` ÷ 1,000), and the same with `p25_views` for the downside. A cheap creator with a low floor can cost more per view than a pricier one.

Rate context, only from traceable sources, labelled vendor:

- Collabstr's 2026 report (about 21,000 marketplace collaborations in 2025): creators asked on average $311 per collaboration on YouTube, $214 on Instagram, $182 on TikTok; brands paid $255, $193 and $186; UGC averaged $154. Marketplace deals skew to small creators, so these understate what larger creators charge.
- Collabstr's 2025 report: content usage rights raised prices by about 40%.

Leave `est_rate` empty with `rate_source: ask` when no source covers the creator's tier and platform; the creator's own rate card or quote is the only real figure. An invented rate anchors the negotiation wrongly.

## Done when

Every vetted creator has a `status`; every `shortlist` row has an `audience_fit` note citing a post or comment, a `signal_detail` with URL and date, and a cost estimate or `rate_source: ask`; and the `.md` states the goal, the tier choice and the evidence for it.

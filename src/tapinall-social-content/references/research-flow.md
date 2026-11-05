# Research flow

The outcome is `tap-suites/social/<slug>/research.md`: demand and supply measured from real posts, complete enough that every gap scored later can point at its evidence. Each step feeds the next, so run them in order.

Before the first paid call, estimate the run (calls × listed price, from `catalog_get`) and show it against the cap. Most social reads cost $0.001–$0.005 a call; AI-answer and enrichment tools cost ten times that or more.

## 1. Scope

Take the scope from files before asking: the customer and the competitors with their handles from `tap-suites/profile.md`, the customer's own words from `tap-suites/market/*.md`, campaign facts from `brief.md`. Settle 3–8 seed keywords in the audience's language, the platforms where the profile says the customer spends attention, 3–5 competitor accounts per platform, and a window of the last 90 days unless the brief says otherwise. Add one or two accounts outside the niche that serve the same audience well, since that is where cross-category formats come from.

Benchmark like with like: founders against founders, company pages against company pages (`references/brand-mode.md`). Personal profiles out-engage pages by multiples, so a mixed benchmark makes a page look broken and a founder look brilliant.

Read `tap-suites/social/learnings.md` when it exists. Its worked patterns become tags to look for in competitor posts; its avoid list keeps you from rediscovering a failure.

## 2. Demand: what the audience wants

Lift demand already bought first: pains and questions in `market/*.md`, keyword volumes and trends in `seo/*.md`, each cited to its file. Fetch only what they leave open:

- Interest over time for the seeds (`tap.google.keywords.trends`, `keywords` list, `country`): rising beats large.
- Google results for the seeds (`tap.google.serp.organic`): what ranks, the questions it lists, whether an AI overview already answers it.
- Reddit search (`catalog_search "reddit search posts"`): question posts and complaints, weighted by comment count.
- Keyword search on each platform (`tap.tiktok.search.videos`, `tap.instagram.search.reels`, `tap.youtube.search.videos`, `tap.x.search.posts`, `tap.threads.search.posts`; LinkedIn post search via `catalog_search "linkedin search posts"`).

Record each signal with its link and number. A question asked repeatedly in different places is the strongest demand there is.

## 3. Supply: what competitors and the owner publish

Resolve each account first, because the posts call often needs an id the profile call returns: `tap.tiktok.user.profile` (username) gives the `sec_uid` that `tap.tiktok.user.videos` wants; `tap.youtube.channel.videos` wants a `channel_id`, and a sibling such as `scrapecreators.x.v1-youtube-channel-videos` takes a username. Then pull the last 20–30 posts per account: `tap.linkedin.user.posts` for people, `tikhub.x.linkedin-web-v2-get-company-posts` or its siblings for company pages, `tap.instagram.user.posts`, `tap.x.user.posts`, `tap.facebook.user.posts`.

Pull the owner's own last 20–30 posts the same way. Gap analysis needs them to say which proven patterns the brand has not used, production needs them for voice, and the performance loop reuses them as its first baseline.

Add the top results of the keyword searches as supply from the wider category, because the audience compares a brand against everyone in their feed, not only the named rivals.

Where paid ads matter, check the Meta Ad Library (`tap.meta-ads.library.advertiser`) and LinkedIn ads for each competitor. An ad that has run for weeks is one they keep paying for, which means its message converts.

## 4. Outliers: what over-performs

Score every post against its own account, because a 10× post on a small account teaches as much as one on a large account:

- Baseline: the **median** views of that account's comparable posts, same platform and format, similar age. Use the median because one viral post inflates a mean and hides the next. Exclude posts younger than seven days; their numbers are still climbing.
- Outlier score: views ÷ baseline. From 3× is notable; from 5× is worth a full breakdown. These cut-offs are conventions, so prefer the account's own spread once known.
- Where a platform hides views (LinkedIn, Facebook), score reactions plus comments the same way.
- Rates per view, against the account's median: shares and saves (TikTok, Instagram), comments (all), and replies per like (X). A post high on shares or saves earned distribution beyond the account's followers even when raw views look ordinary.

Tag every post with topic, format, hook type, angle and dominant emotion, using the vocabulary in `references/viral-content.md`, so research tags, production drafts and the performance loop speak the same language. Break down each 5× post with that file.

## 5. Voice of the audience

Pull comments on the top two or three outliers per competitor and on the posts that answer the strongest demand signals, 50–100 comments each (`tap.<platform>.video.comments` or `.post.comments`). Collect repeated questions, objections, requests ("do one on…"), complaints about what is missing, and phrases the audience uses verbatim. Those phrases become hooks later.

## research.md

- A one-paragraph summary of what the evidence says.
- Demand signals: signal, source (link or `tap-suites/` file), number.
- Posts table, one row per post: platform, account, account type (personal or page), own or competitor or category, URL, date, format, topic, hook type, angle, views, likes, comments, shares, saves, outlier score, notes. tapinall-creators reads this table to find accounts worth partnering with.
- Outlier breakdowns.
- Audience voice: quotes with links, grouped by theme.
- Not collected: failed calls, skipped platforms, hidden metrics. Gap analysis needs this to tell missing data from missing supply.

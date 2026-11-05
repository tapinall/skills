# Vetting

The outcome is, for each candidate, the CSV's performance columns computed from fetched posts, a `vetting_flags` list, and the post URLs behind both. A paid post is one draw from a creator's distribution of results, so vetting measures that distribution, not the profile's headline numbers.

## Fetch the posts

Pull the last 20–30 posts per creator on the platform you would pay for.

- Cheapest: `tap.instagram.user.posts` (`username`), `tap.tiktok.user.videos` (`sec_uid` from `tap.tiktok.user.profile`), `tap.youtube.channel.videos` (`channel_id` from `tap.youtube.channel.profile`); about $0.001–0.003 a call.
- Fallback: `influencersclub.creators.posts` ($0.045 a request, not per post; `count` is fixed at 12 on Instagram, up to 35 on TikTok, up to 50 on YouTube; page with `pagination_token`).
- Comments: `tap.instagram.post.comments` (`shortcode` or `url`), `tap.tiktok.video.comments`, `tap.youtube.video.comments`; or `influencersclub.creators.post.details` with `content_type: "comments"`. Spoken content: the same tool with `content_type: "transcript"`.

Drop pinned posts and posts younger than three days (their views are still climbing), and compare like with like: Reels apart from carousels, Shorts apart from long-form. Fewer than eight usable posts earns the `few_posts` flag, because a median of five posts is noise.

## Compute

- `median_views` and `p25_views`: the median is what a typical post earns; the 25th percentile is the realistic downside of a single paid post. Use medians, because one viral post inflates a mean.
- `er_followers`: median over posts of (likes + comments) ÷ followers. Most published benchmarks use this denominator.
- `er_views`: median over posts of (likes + comments + shares + saves) ÷ views, where the platform reports views. Feeds distribute by content, so on TikTok and Reels views track followers loosely and this is the better measure of whether people who see the post act on it.
- View rate: median views ÷ followers. Very low on a view-reporting platform means the followers do not watch.

## Benchmarks

Compare each creator first against the other candidates on the same platform and tier: same niche, same week, same formula. Engagement rate falls as follower count rises (HypeAuditor, 36,000+ Instagram influencers, vendor; Wies et al., *Journal of Marketing*, 2023), so judge it within tier only.

Published benchmarks disagree two- to threefold because they use different denominators, so quote one only with its formula, and never set a by-views rate beside a by-followers benchmark. Labelled vendor anchors:

- Ordinal, 70,322 Instagram posts since 2024, median (likes + comments + saves + shares) ÷ impressions: under 1K 2.67%, 1–5K 2.97%, 5–10K 3.32%, 10–50K 2.80%, 50K+ 2.13%. Impressions are private, so this is closer to `er_views` than to `er_followers`.
- Favikon, 2.6M active profiles (July 2025), top-quartile thresholds, formula unstated: Instagram nano (<10K) 3.4%+, mega (500K+) 1.8%+; YouTube nano 0.8%+.

## Signs of a bought or inflated audience

No single sign convicts; two or more together justify rejection. Vendor guides agree on the signals but publish no validated thresholds, so state what you saw.

| Flag | What you saw |
|---|---|
| `low_er_for_tier` | `er_followers` far below the cohort median for the tier |
| `low_view_rate` | median views a small fraction of followers on TikTok, Reels or YouTube |
| `generic_comments` | in a 50–100 comment sample on two or three recent posts, most are emoji-only, "nice post"-style, off-language, or unrelated to the content |
| `pod_pattern` | the same small set of accounts comments early on post after post |
| `growth_spike` | a follower jump with no viral post, press or collaboration to explain it (analytics growth series) |
| `audience_geo_mismatch` | audience countries that do not fit the creator's language or the market sold to (analytics) |

Comment quality is the strongest check you can run cheaply: real audiences ask questions, describe their own situation, disagree and make typos. Count the share of substantive comments and quote two in the notes. Engagement pods do raise a post's organic reach (Weerasinghe et al., WWW 2020), so pod engagement is not worthless, but it inflates engagement rate as a measure of audience interest.

## Sponsored history

Find past sponsored posts from the paid-partnership label or field, `#ad`, "sponsored by", brand tags, discount codes and affiliate links. Record:

- `sponsored_vs_organic`: median views of sponsored posts ÷ median of organic posts. Studies split on whether sponsored posts underperform in general (a study of 239 macro-influencers found lower engagement on ads; industry datasets disagree), so measure each creator's own ratio rather than assume one.
- The share of recent posts that are sponsored, and which brands. A deal with a direct competitor in the last few months is `competitor_deal`: proof of category fit and a likely exclusivity conflict, both worth stating.
- Sponsored posts without a clear disclosure: `undisclosed_ads`. Regulators in the US and UK hold the brand responsible too, so a creator who skips disclosure is a compliance risk for the user (see `references/compliance.md`).

## Brand safety

Read captions, and transcripts of video posts, across the sample against the profile's constraints. Run `tap.web.search` (news) on the creator's name with terms such as "controversy" or "apology". Flag `brand_safety:<topic>` with the URL. Flag `minor_audience` where content or comments show a mostly under-18 audience, since disclosure rules ask more care there and some categories cannot be promoted to minors.

## Other flags

`inactive` (no post in 30 days), `few_posts`, `metrics_hidden` (likes or views hidden; engagement columns left empty), `ad_heavy` (most recent posts sponsored; give the share).

## Done when

Every candidate has `posts_sampled`, `median_views` or a `metrics_hidden` flag, at least one engagement measure, flags with evidence URLs, and a `status`. Rejected rows keep their numbers, so the reason can be checked later.

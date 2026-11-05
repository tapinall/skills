# Performance loop

The outcome is `tap-suites/social/<slug>/performance/<YYYY-MM-DD>.md`, scoring the owner's recent posts against their own median, and new entries in `tap-suites/social/learnings.md` that the next cycle's gaps and hooks draw on. Its consumer is the next research and production run, so every lesson cites the posts and scores behind it and says how much evidence it rests on.

## When

Score a post only once it is seven or more days old. Most of a post's reach arrives in its first days (vendor TikTok analyses put most views within five days; LinkedIn posts keep collecting for a week or more), so a younger post scores low for its age, not its quality. YouTube long-form keeps growing for weeks; compare videos at similar ages and note the age beside each score. List posts too young to score and when to rerun.

## Fetch the owner's posts

Read `references/tapinall.md` first. Take handles from the profile's Identity and Channels and the account mode from `brief.md`. Pull the last 30–50 posts per platform so the median rests on more than this campaign's pieces:

- LinkedIn person: `tap.linkedin.user.posts` (`linkedin_url` or `linkedin_handle`, `limit`).
- LinkedIn page: `tikhub.x.linkedin-web-v2-get-company-posts` (`url`, optional `start_date`, `end_date`) or its siblings.
- TikTok: `tap.tiktok.user.profile` (`username`) for the `sec_uid`, then `tap.tiktok.user.videos` (`sec_uid`, `limit`).
- Instagram: `tap.instagram.user.posts` (`username`).
- YouTube: `tap.youtube.channel.videos` (`channel_id`); `scrapecreators.x.v1-youtube-channel-shorts` for Shorts separately.
- X: `tap.x.user.posts` (`username`). Facebook: `tap.facebook.user.posts`. Threads: `catalog_search "threads user posts"`.
- A post missing metrics in the list: `tap.<platform>.post.detail` or `.video.detail` by URL.

Reuse own posts already in `research.md` when they are fresh, and refetch only to update their numbers. Match fetched posts to pieces through the published URL in `content/index.md`, else by text and date. Posts the suite did not produce stay in the baseline and are scored too.

## Score

- Baseline: the median of the owner's comparable posts, same platform, same account and format, seven or more days old. With fewer than about ten comparable posts, pool formats on that platform and mark every score low-confidence, because a median of four posts moves with any one of them.
- Score: views ÷ baseline; on LinkedIn and Facebook, reactions plus comments ÷ baseline. From 3× is a win, at or under about half the median a miss; both cut-offs are conventions, so switch to the owner's own spread once twenty or more posts are scored.
- Rates against the owner's median: shares and saves per view, comments per reaction, replies per like on X. A post high on shares or saves at ordinary views still earned distribution beyond the followers.
- Pull comments on the top one or two winners. Repeated questions in them are the next Question gaps.

## Tag what worked

Tag each post with the shared vocabulary from `references/viral-content.md` (topic, format, hook type, angle, dominant emotion) plus gap id, only-us element type (story, number, named client, opinion, research finding), account mode, length band and posting day and hour.

A pattern is a tag value that shows up among the winners more than among posts at or below the median. One winner is an anecdote: record it as a hypothesis. A pattern behind two or more winners, and absent from the misses, is confirmed. A confirmed pattern that later misses twice is retired. Before crediting a pattern, rule out the post's context: a news moment, a big account resharing, a paid boost.

## performance/<YYYY-MM-DD>.md

- Window, platforms, accounts, number of posts, baseline per platform and format.
- Table: post URL, piece (or "not suite"), platform, account, format, published date, age in days, tags, metric, baseline, score, share and save rates, verdict (win, par, miss, too young).
- What worked and what did not, each line citing its posts.
- Questions from winners' comments.
- Spend for this run.

## learnings.md

Create `tap-suites/social/learnings.md` with a `# Social learnings` heading when missing. Append one section per run, `## <YYYY-MM-DD> <slug>`, holding a table: pattern (tag = value), platform, account, kind (worked, avoid, try next), evidence (post URLs and scores), posts behind it, status (hypothesis, confirmed, retired). When a run confirms or retires an earlier pattern, add a row saying so and citing the earlier section rather than editing it, so the history of what was believed and why survives.

The next cycle reads it: confirmed patterns become Own proven pattern gaps and the first hook candidates, avoid rows join the avoid list, try-next rows become untested ideas.

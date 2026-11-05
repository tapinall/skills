---
name: tapinall-social-content
description: "Researches, writes and measures social content with Tapinall. Use when the user says 'what should I post', 'what are my competitors posting', 'find content gaps on TikTok', 'write LinkedIn posts for me', or 'how did my last posts do'."
---
# Social content with Tapinall

Act as the owner's content strategist and producer: they hold the brand, the stories and the final say; you hold the evidence and the craft. The outcome is a campaign folder that takes one brand or person from research through gaps to publish-ready pieces, then measures what was published and feeds the lessons into the next cycle. Its consumers are the person who publishes without having been in this conversation, a later run that resumes or measures, and tapinall-creators, which reads the research. That sets the bar: every gap traces to posts or numbers with their URLs, every piece names its gap, its platform and its only-us element, every performance score compares an account with its own median, and every cent is in the ledger. A plan built on what "usually works" instead of fetched evidence fails that bar however polished it reads.

## What it reads

- `tap-suites/profile.md`: Identity (company brand, founder or freelancer), Customer, Competitors with handles, Proof bank, Voice, Channels, Constraints (spend cap, claims to avoid). When it is missing, gather only what this run needs (name, account type, handles, customer, competitors, three real voice lines, two proof-bank entries), write it under the profile's headings, and suggest tapinall-profile for the rest.
- `tap-suites/market/*.md` and `tap-suites/seo/*.md`: customer pains, the customer's own words and keyword demand already paid for. Reuse and cite them rather than buying the same signals again.
- `tap-suites/social/learnings.md`: what has worked and failed for this owner before.
- An existing `tap-suites/social/<slug>/`: resume at the stage it reached. Trend and outlier data older than about a month is stale on social platforms; offer a refresh.

## What it writes

Under `tap-suites/social/<slug>/`, the slug naming the brand or campaign:

- `brief.md`: only campaign facts the profile lacks: goal, platforms, account mode per platform (personal profile or company page), the offer or date being pushed, window, campaign spend cap.
- `research.md`: summary, demand signals, posts table, outlier breakdowns, audience voice, not collected.
- `gaps.md`: ranked gap table, per-gap evidence, avoid list, untested ideas.
- `content/index.md` with columns piece, gap, platform, account, format, status (draft, ready, published), published URL, published date; one `content/<nn>-<slug>.md` per piece, assets in `content/<nn>-<slug>/`.
- `performance/<YYYY-MM-DD>.md`: each own post scored against the owner's median, with tags and verdicts.

Shared across campaigns: `tap-suites/social/learnings.md`, appended by the performance loop. Every paid call goes to `tap-suites/ledger.md` as `references/tapinall.md` specifies.

Each reference spells out its file's full structure.

## Stages

Read `references/tapinall.md` before the first Tapinall call. The spend cap comes from `brief.md`, else the profile's Constraints; confirm it before the first paid call.

- Research: read `references/research-flow.md` fully and follow it.
- Gaps: read `references/content-gaps.md` fully and follow it; read `references/viral-content.md` when you break down why a post outperformed.
- Production: read `references/production.md`, `references/anti-slop.md` and `references/viral-content.md` fully and follow them.
- Account mode: read `references/brand-mode.md` when choosing platforms, benchmarks, formats or voice, because a personal profile and a company page are rewarded for different things.
- Performance: read `references/performance-loop.md` when the user asks how posts did, or when `content/index.md` shows pieces published seven or more days ago and not yet scored.

Show the ranked gaps and wait for the user to choose before production, because production spends real money and turns on brand judgment only they hold.

Pieces are files the owner publishes from their own tools; Tapinall cannot post. Ask them to fill in the published URL and date in `content/index.md`, since the performance loop matches on it.

## End of run

Tell the user which files were written or updated, what this run spent (from the ledger) and any job still running with its idempotency key. Then name what comes next: publish and run the performance loop seven or more days later; tapinall-creators to find creators for the winning gaps; tapinall-outreach once creators are chosen.

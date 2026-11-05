---
name: tapinall-profile
description: "Builds the business profile every Tapinall skill reads. Use when the user says 'set up my business profile', 'onboard my brand', 'update my profile', 'here is my website, learn my business', or 'add this to my proof bank'."
---
# Business profile

Act as the strategist who interviews the owner and checks the record: they know the business; you know what the rest of the suite needs from it and how to verify it from public data. The outcome is `tap-suites/profile.md`, read by every Tapinall skill to target, personalise and write. Its consumers are those skills, run later without this conversation, so the bar is: every fact is either confirmed by the owner or cited to a fetched source, the proof bank holds only real material, and anything unknown is marked unknown rather than guessed. A guessed proof point becomes a fabricated claim in someone's outreach or post.

## Gather

Mine what the user gave first: a website, social handles, a pitch deck, past posts. Then fetch what public data can settle, after reading `references/tapinall.md`: the site's pages (`tap.web.map`, `tap.web.extract`), firmographics (`tap.companies.enrich`), and the owner's recent posts on the platforms they use. Propose what the data suggests and ask the owner to confirm or correct it, a question or two at a time, spending their attention on what only they know: results, stories, opinions, constraints.

Competitors named by the owner are checked against `tap.companies.similar` or a search, and the ones they missed are offered.

## profile.md

Keep these sections, in this order, because sibling skills look them up by heading:

- **Identity**: name, type (company brand, founder, or freelancer), what they sell, price points, geography, website and handles, and the postal address outreach must carry under CAN-SPAM.
- **Customer**: who buys, as firmographics for B2B (industry, size, roles) or as a persona for consumers; the problem they hire this offer for; where they spend attention.
- **Competitors**: direct and substitute, each with domain and handles.
- **Positioning**: why a customer picks this over the alternatives, in one or two sentences the owner agrees with.
- **Proof bank**: first-hand stories, real numbers, named clients who agreed to be named, results, credentials, and opinions the owner will defend in public. Each entry says where it came from ("owner, 2026-11-05" or a URL). This is the raw material `references/anti-slop.md` requires in every piece; read it before you write this section so you know what makes an entry usable.
- **Voice**: three to five real lines the owner wrote, quoted, plus words they never use.
- **Channels**: where they publish and sell now, and what has worked.
- **Constraints**: default spend cap per run, compliance limits (regulated claims, regions), topics or claims to avoid.
- **Unknowns**: what the owner could not answer yet.

When `profile.md` already exists, update it in place: add, correct and date entries rather than rewriting confirmed ones, and say what changed.

End by telling the user what the profile holds, what it cost, and which skill to run next; the `tapinall` hub can plan the chain.

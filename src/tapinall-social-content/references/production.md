# Production

The outcome is `tap-suites/social/<slug>/content/`: pieces the owner can publish without asking anything, each tied to the gap it fills and carrying something only this brand could say.

## Before drafting

Confirm the chosen gaps, the platforms, the account each piece goes out from (personal profile or company page, per `references/brand-mode.md`), and how many pieces. Read `references/anti-slop.md` fully; every piece passes its four tests before it is marked ready.

Voice comes from the profile's Voice section and the owner's best-performing posts in `research.md`, quoted, never from an adjective. A company-page piece speaks as "we" and names the person behind the story; a personal piece speaks as the owner, and only about experience they actually had.

## The only-us element

Pick it before the hook, because the piece is built around it: a proof-bank entry from `tap-suites/profile.md` (a story, a number, a named client who agreed to be named, an opinion the owner defends) or a finding from this run's research. When the chosen gap has no proof-bank entry to carry it, ask the owner for one rather than writing around the hole; a generic piece is what the platforms' originality rules demote and what readers distrust.

In a series, each piece adds a new fact, story or angle. Swapping the nouns in one template is the pattern YouTube's inauthentic-content rule and Meta's originality rules demote.

## Drafting

Write each piece natively for its platform and account rather than one post cross-posted: length, aspect ratio, caption conventions and what the platform rewards all differ. For each piece, write three hooks of different types, drawn first from patterns `tap-suites/social/learnings.md` shows working for this owner, then from the audience's own phrases in `research.md`, and pick one with the reason. Check the draft against `references/viral-content.md`: which STEPPS principles it hits and which proxy (shares, saves, comments) it is built to earn.

## Images

Find image models with `catalog_search "image generation"` and compare prices from the catalog. Iterate on a cheap model and render finals on a stronger one. For slides that carry text, pick a model whose catalog notes claim text rendering and read every output. When the text comes out garbled, deliver the image without text and put the copy in the piece's file for a designer to set. Use real photos for real people and products, as `references/anti-slop.md` explains. Download generated files into `content/<nn>-<slug>/` as soon as they arrive, because provider URLs often expire.

## Video

Video costs from about $1.40 to over $60 a call. Quote first: the model, the duration, the price from `catalog_get` and the total. Generate nothing until the user says yes. Most video tools are async; collect them as `references/tapinall.md` describes and log every pending key in `tap-suites/ledger.md`.

## content/

- One `content/<nn>-<slug>.md` per piece: gap id, platform, account, format, the chosen hook and its alternatives, the script or copy, a visual brief, the CTA (or where the link goes, per `references/brand-mode.md`), posting notes, what it is built to earn, asset paths, the only-us element and its source, and "slop check: passed" with what was rewritten.
- `content/index.md`: a table of piece, gap, platform, account, format, status (draft, ready, published), published URL, published date, in suggested posting order. The owner fills in the last two after posting; the performance loop matches on them.

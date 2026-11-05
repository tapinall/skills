# Sending rules: deliverability and compliance

Two uses: in Scope, decide which leads are held because the law blocks the channel; in Write, build the sending checklist in `outreach/<slug>.md`, fitted to the user's daily volume and countries. Tapinall cannot send or check DNS, so every item here is something the user does in their own domain host and sending tool. Say once in the `.md` that this is a practical summary, not legal advice.

## Deliverability checklist

- **Authenticate the sending domain.** Google requires SPF or DKIM from every sender, and SPF, DKIM and DMARC (`p=none` is enough) with From-domain alignment from anyone sending 5,000+ messages a day to Gmail; DKIM keys of at least 1024 bits, 2048 recommended; TLS; valid forward and reverse DNS. Microsoft applies the same SPF, DKIM and DMARC rule to domains sending 5,000+ a day to Outlook.com: since 5 May 2025 non-compliant mail goes to Junk, with rejection (550 5.7.515) announced for later. Yahoo enforces similar rules and publishes no volume threshold. Set all three up whatever the volume: it costs an hour and below-threshold senders get filtered on the same signals.
- **Protect the main domain.** Many cold senders use a separate, similar domain for outreach, because complaints damage the reputation of the domain that sent them and the main domain carries the user's everyday mail. It needs its own authentication and warm-up.
- **Spam complaints.** Google asks senders to stay under 0.1% in Postmaster Tools and never reach 0.3%. The cheapest protection is relevance: the signal-led first line and a plain way to opt out.
- **Warm-up and volume.** Instantly advises starting a new inbox at 5–10 emails a day and ramping over 4–6 weeks (vendor guidance). Spread volume over several inboxes rather than pushing one.
- **Bounces.** Keep hard bounces under 2% (Instantly): verify addresses before import, and hold catch-all and unverified addresses for review.
- **Unsubscribe.** Gmail requires one-click unsubscribe (`List-Unsubscribe` and `List-Unsubscribe-Post: List-Unsubscribe=One-Click` headers) plus a visible link for marketing messages from bulk senders. Below that volume, still give a plain opt-out line in every email ("Reply 'no' and I won't write again"), because CAN-SPAM, PECR and CASL all require a working opt-out, and a reader with no easy exit presses "report spam" instead. Honour it in the tool's suppression list.

## Compliance by recipient country

Hold a lead when the rule for its country blocks the channel, and put the reason in `hold_reason`. A lead with no known country gets `status` = `review`.

- **United States, CAN-SPAM.** Applies to B2B email. No consent needed, but: accurate From and subject lines, the message identifiable as commercial, a valid physical postal address, a working opt-out honoured within 10 business days. Penalties reach $53,088 per email (FTC 2025 adjustment, unchanged for 2026).
- **United Kingdom, PECR and UK GDPR.** Email to corporate subscribers (limited companies, LLPs, public bodies) needs no prior consent, but must identify the sender and offer an opt-out. Sole traders and some partnerships count as individuals and need consent or the soft opt-in, which does not cover cold outreach: hold them. Named employees are still personal data under UK GDPR, so the sender needs a legitimate-interest basis and must tell the person where their data came from by the first message at the latest (Article 14). The Data (Use and Access) Act 2025 raised PECR fines to £17.5m or 4% of global turnover.
- **European Union, GDPR plus national e-privacy law.** Legitimate interest can cover processing the data; whether the email may be sent at all is national law. Germany (UWG §7) requires prior consent for advertising email even to businesses: hold German leads for email and offer LinkedIn or a phone call instead. France permits B2B email without consent when the address is a named business address, the message concerns the person's role, and an opt-out is offered. For other member states, mark `review` and tell the user to check before sending. Every EU email names the data source, per Article 14.
- **Canada, CASL.** Implied consent exists when the person has conspicuously published their address, the publication carries no statement refusing unsolicited messages, and the message is relevant to their business role. Otherwise hold. Every message identifies the sender with contact details and an unsubscribe that is honoured within 10 business days.
- **LinkedIn and creator DMs.** These sit under platform rules more than email law: no automation (LinkedIn User Agreement), no misleading identity, stop when asked.

## Effect on the copy

- The signature carries the sender's name, company and postal address from the profile.
- Every email carries the opt-out line; UK and EU emails add a short note of where the contact came from ("I found your details on your company site").
- Subjects describe the email honestly; no fake "Re:" or "Fwd:".
- A creator collaboration pitch that offers payment or gifts reminds the user that the creator must disclose it when they post (FTC Endorsement Guides, ASA in the UK).

## Done when

Every lead has a country or a `review` flag, every hold has a reason, and the `.md` checklist names the user's real volume, the countries in the list, and what to set up before the first send.

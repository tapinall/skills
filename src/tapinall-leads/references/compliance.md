# Compliance the user must know

The outcome is a list whose rows are flagged where the law limits cold email, and a `.md` section that tells the user, briefly, which rules their list falls under and what each message must carry. State it as orientation, not legal advice, and suggest counsel before large or multi-country campaigns. The jurisdiction is the recipient's, so set it from `country` on each row.

## Flags

Write one code in `compliance_flag`, or leave it empty when nothing below applies. Flagged rows go to `hold` until the user decides.

- `uk_sole_trader`: UK business that is not a company (sole trader or partnership outside Scotland).
- `de_consent`: recipient in Germany.
- `ca_not_published`: Canadian recipient whose address was found by a finder tool rather than published by them.
- `personal_email`: a free-mail or personal address used for a business contact.
- `eu_check`: EU country whose B2B email rule the run did not confirm.

## EU: GDPR plus national ePrivacy rules

- A named work address is personal data. Legitimate interest can cover B2B prospecting when the offer relates to the person's job; France's CNIL says so directly, using the example of software offered to an IT director. The user should keep a short written balancing test.
- Article 14: when data is not collected from the person, they must be told its source, at the latest in the first message. That is why every row carries `source_url`, and outreach names the source in the first email.
- The right to object to direct marketing is absolute: an opt-out ends contact, and the address joins the user's do-not-contact list.
- The email rule itself is national. France allows B2B email to professional addresses on job-relevant offers with an easy opt-out, and treats generic company addresses (`contact@`) as outside these rules. Germany's UWG §7 requires prior consent for advertising email, B2B included, so German rows are flagged and excluded by default. Other member states vary; flag rather than assume.

## UK: PECR plus UK GDPR

- The PECR email rule does not cover corporate subscribers: limited companies, LLPs, PLCs, Scottish partnerships and public bodies. Sole traders and other partnerships are individual subscribers, so cold email to them needs consent or the soft opt-in.
- UK GDPR still applies to named people at companies: identify the sender, give a working opt-out, honour objections, and screen new lists against a do-not-email list, as the ICO recommends.

## US: CAN-SPAM

No consent is needed and the law makes no exception for B2B. Each message needs truthful headers, a subject line that matches the content, disclosure that it is an advertisement, a valid postal address, and a working opt-out, honoured within 10 business days and kept working for at least 30 days after sending. Penalties reach $53,088 per email.

## Canada: CASL

Consent comes first. Implied consent by conspicuous publication holds only when the recipient published the address themselves, with no statement refusing unsolicited messages, and the message is relevant to their role. A pattern-guessed address from a finder does not meet that, so Canadian rows need a `source_url` showing where the person published it, or the flag. The sender carries the burden of proof; penalties reach CAD 10 million per violation for a business.

## Work and personal addresses

Work addresses at a company domain carry the B2B footing above. Personal and free-mail addresses make the recipient an individual under PECR and most ePrivacy rules, and weaken the job-role link that legitimate interest rests on, so personal-email finders stay out of cold lists. A sole trader whose only published address is a gmail.com one is flagged `personal_email` rather than dropped, since the user may hold a lawful basis this run cannot see.

## In the `.md`

List the countries present with row counts, each flag with its count, and the duties every message carries: sender identity, postal address, working opt-out, and the data source for EU and UK recipients.

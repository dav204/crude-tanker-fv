# Compass Maritime feed onboarding — decision cell (owner review, 2026-07-28)

**Status: RULED same day (owner, after fetching W30 directly): OPTION (a) — but wired
via WEB, not email.** The weekly is a PUBLIC PDF at a date-patterned URL
(`/wp-content/uploads/2026/07/Compass-Weekly-Report-July-27-26.pdf`;
`/market-report-download/` redirects to the current issue). Ruling rationale: routing
Compass through the Gmail session would install the redundancy IN SERIES with the very
fragility it hedges — a web-fetch harvester step is genuinely parallel. Owner sends the
email request ANYWAY (sanctioned channel, fallback + relationship) but the harvester
never depends on it. The report carries a no-reproduction notice: ingestion stays
READ-ONLY and LOCAL (gitignored staging per the research-binaries convention), and no
issue is ever mirrored anywhere shareable.

## Why Compass, why now

- **It already earned its keep twice this week without being a feed:** corroborated
  SEACON TOKYO (the batch's highest-leverage young print) out-of-feed, and DETECTED TWO
  CONFLICTS whose resolution improved the record (the Oldendorff price, resolved 2-1 to
  $37.0M; the AANYA/AASHNA sister-ship identity, resolved by trade press). *(Corrected
  2026-07-28: the earlier "third Meghna Ultramax" rationale was WRONG — that print is WF
  Artemis, promoted 7/18. Compass's demonstrated value is CONFLICT-DETECTION, which the
  ingestion design below reflects: disagreements FLAG, they don't silently stage.)*
- **It has citation precedent in the book:** the Feb-2026 STI Condotti Aframax print in
  `transactions/aframax.yaml` is Compass-sourced. The trail already trusts it as a house.
- **It plugs the two live coverage holes:** Fearnleys' S&P section is unreliable as-staged
  (blank W28+W30; W29 announced-never-staged), and the MB weeklies ride the fragile
  Gmail-session step. Compass is a per-vessel S&P specialist publishing weekly — exactly
  the print-density the marks-trail wants, and a second corroboration house would also
  service §G6's second-print requirement when MB is down.

## Access mechanics (checked 2026-07-28)

Distribution is **email, Friday cadence, free on request**: non-subscribers request the
Weekly Market Report by emailing **Reports@CompassMar.com** with contact info and
background/company (per compassmar.com/market-report). No paywall found; a sample PDF is
public on their site. **The subscription request is a human step — the owner sends it**
(the draft-never-send rule; it's an outward contact identifying you).

## Options

- **[ ] (a) Full feed onboarding (recommended).** Owner emails the subscription request
  from the harvest Gmail address → the weekly lands in the same inbox the MB harvest
  reads → add a `compass` feed to the mb_harvest/Gmail-session step (subject-pattern +
  fetch, same idempotent-by-filename mechanics) + a `hsn`-style manifest row + the
  sentinel staleness key (weekly cadence, 10d grace). Producer work on my side is ~an
  hour once the first email arrives; nothing until then.
- **[ ] (b) Ad-hoc citation only (status quo).** Keep using Compass as an owner-supplied
  cross-check when it surfaces. Zero build; keeps the single-vendor concentration the
  README already discloses (~76% single-vendor prints) unimproved, and G6's
  second-corroboration path stays MB-dependent.
- **[ ] (c) Defer to the Q3 refresh** alongside the Fearnleys W29 re-fetch disposition.

## Notes for the ruling

- Adding a THIRD independent S&P house materially helps the README's stated
  single-vendor-dependence limitation (the honest-disclosures section) — dry bulk and
  product are the most single-source tiers, and Compass covers both.
- Email-request implies disclosure of identity/affiliation to a broker — mild, standard
  practice, but it is an outward-facing step and stays with the owner.
- If (a): the Gmail connector reconnect becomes triply load-bearing (MB + G6 + Compass).

## Design notes bound into the ruling (owner, 2026-07-28)

1. **Web-fetch step** (date-patterned URL + the `/market-report-download/` redirect as
   fallback), Friday cadence — PARALLEL to Gmail, never through it.
2. **Content-level sentinel from day one:** a minimum-prints-per-issue expectation (not
   arrival staleness) — the Fearnleys lesson applied at onboarding, not retrofitted.
3. **Conflict-detection ingestion:** cross-house disagreements on an already-staged print
   FLAG for triage rather than staging additively. Ingestion key = **name + build year +
   price, NOT dwt** (three dwt transpositions in one batch).
4. **The value matrix is deliverable #1:** ingest the per-class NB/resale/5yr/10yr ladder
   and run the cross-sectional check on the "22%-below-broker" k_broker doctrine (market-
   wide feature vs xclusiv artifact) + the young-end fit-lag question (Compass's ladder
   puts SEACON and the Oldendorffs ON the ladder — the fit lags, the prints aren't hot).
5. **G6 independence stays soft:** broker houses recycle market intelligence — a second
   report of one deal is corroboration, not a second observation. Said plainly in the
   README rather than letting the 76% single-vendor figure improve on paper.
6. **Sequenced BEHIND the Gmail reconnect** (MB + G6 already block on it; don't stack
   debugging surface while two feeds are degraded).

**Decision (owner):** [x] **(a) RULED — wire via web, email request as owner-sent
fallback; build sequenced behind the Gmail reconnect; design notes 1-6 binding.**
(b)/(c) rejected — (c) explicitly: the build is trigger-based and near-zero until the
first issue lands, so deferral buys nothing.

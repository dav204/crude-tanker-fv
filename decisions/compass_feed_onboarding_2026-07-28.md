# Compass Maritime feed onboarding — decision cell (owner review, 2026-07-28)

**Status: PROPOSED at owner direction ("bring me the compass feed onboarding decision").
Nothing wired; ruling = owner's.**

## Why Compass, why now

- **It already earned its keep twice this week without being a feed:** corroborated
  SEACON TOKYO (the batch's highest-leverage young print) out-of-feed, and surfaced the
  THIRD Meghna Ultramax (63,547/2020 Iwagi, $36.5M) both staged feeds missed.
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

**Decision (owner):** [ ] (a) onboard — owner sends the request · [ ] (b) status quo ·
[ ] (c) defer to Q3

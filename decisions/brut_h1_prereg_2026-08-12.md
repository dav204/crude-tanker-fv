# BRUT H1-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-12, before the print)

**Reports 2026-08-13 (Euronext company-information calendar, exchange-published; no timing
stated — watch the Oslo newsweb from the open). AGM was TODAY 2026-08-12 (same calendar).**
Frozen tonight so tomorrow's refresh is band-checked from the moment the Half-yearly Report
lands. This is the pre-registered resolution date for `cash-pending-H1-report` (owner decision
2026-07-01, `brut_reconciliation_prereg_2026-07-01.md`) — the first issuer snapshot since the
FY2025 Annual Report; everything Q1 was Dec-2025 actuals rolled through Note-15 subsequent
events. Amendments to this file are allowed only PRE-print (dated); nothing amends after.

## Basis (current committed state)

NAV $8.80/sh (fleet PV $1,851.9M + cash $66.0M − commitments $1,373.1M; 61,923,808
diluted; sheet vintage 2026-Q1 = as-of 2026-03-31) · single FV $8.83 · scenario PW $9.33
**VOID** (POSITION_UNRELIABLE, deck-incoherence — 8/10 halt disposition B) · tier
PROVISIONAL, binding flags `cash-pending-H1-report` + going-concern §15 (resale-level flag
retired 2026-07-15 thread-d) · cash is BRUT's one remaining `[ESTIMATE]` NAV-driver
(`NAV_FIGURE_ESTIMATE_QUEUE`, intended; HAFN/CMBT/FLNG sit in the queue on their own reasons).

## Predicted H1 drivers (knowable tonight)

- **The ledger resolution — THE event, and it is BIMODAL, not a range.** The 7/01 booking
  is the double-conservative corner: deposit-paid cash floor ($66M) AND gross CIMC
  commitment ($499.0M inside $1,373.1M). On the ledger identity, (cash − commitments) at
  3/31 is **deposit-invariant** — if the Annual Report's Note-15 $499.0M was the GROSS
  contract value, truth = −$1,257.1M vs booked −$1,307.1M, i.e. **+$50M ≈ +$0.81/sh,
  whether or not the deposit was paid** (paid: 66−1,323.1; unpaid: 116−1,373.1 — same
  number). Only if the note's figure was already NET of a paid deposit does booked = truth
  (+$0.00; net of a smaller deposit D lands between at +(50−D)M). An order announcement
  conventionally quotes gross contract value → **note-gross (+$0.81/sh) is the more likely
  mode.** The H1 balance sheet states cash AND remaining commitments directly — read BOTH,
  close the ledger, retire the floor.
- **Q2 yard installments: NAV-neutral by construction** (cash and commitments down
  equally; expect ~$0–40M — Mount Vision's delivery installment is Jul = Q3, subsequent
  events). Do not mistake a big cash draw with matching commitment relief for a miss.
- **H1 burn:** pre-operational G&A + manager fees − interest income on the cash ≈ ±$0.05/sh;
  plus the 2020 Bulkers Management 36% internalisation buy (agreed Feb, effective Apr-2026 —
  a Q2 cash-out, price undisclosed, expect single-digit $M).
- **Snapshot re-date:** years_to_delivery re-stamps 6/22 → 6/30 ≈ +$0.07/sh mechanical.
  The H1 report may pin the CIMC 4×"2028 intra-year estimate" to real months (±0.3y ≈
  ±$0.20/sh) and may slip NTS dates (a one-quarter slip on 2-3 hulls ≈ −$0.10-0.15/sh).
  Re-date per the issuer's stated schedule at this pair; `fleet_schedule` follows.
- **Expected zeros:** debt 0 at 6/30 (draws start at delivery, first Jul-2026); WC ~0;
  shares 61,923,808 (no placement in any feed since Feb — five broker feeds current through
  W33, Pareto dailies through 8/12 silent; BRUT closed kr 59.6 −0.7% today).
- **Unknowable until the note:** any undisclosed Q2 placement (dilutive at ~0.7× NAV —
  input surprise, halt path), any pre-delivery financing (debt at 6/30 ≠ 0 — big §15 news,
  roughly NAV-neutral cash+debt), vessel sales/charter-out deals.

## Registered band

**Point NAV ≈ $9.68/sh on the note-gross ledger (the more likely mode); the note-net
alternative prints ≈ $8.87. Band [8.50, 10.00]** (floor = note-net − burn − a modest slip;
ceiling = note-gross + roll + CIMC pull-forward). Landing outside → HALT and investigate
the INPUT (a missed placement, unexpected debt, a >1q delivery slip, a commitments basis
change) before accepting. Landing BETWEEN the modes (~9.0-9.4) is itself diagnostic:
a partial-deposit ledger — trace it, don't average it.

## Halt/verification conditions (standing rules restated so the run can't skip them)

1. **Subsequent-events note read FIRST**; post-6/30 events do NOT enter the H1 snapshot.
   Expected there: Mount Vision delivery (Jul) + first debt draw + the $95k/day TC
   commencement + any financing progress + any post-6/30 raise. Routing: financing /
   going-concern language → the §15 screen; fixture terms → Rider-4 (below); deliveries →
   manifest re-date at this pair.
2. **Pair lands together:** `inputs/balance_sheets/brut_2026-Q2.yaml` (provenance trio —
   required from Q2 sheets on) + manifest `report_date: 2026-Q2` bump in ONE commit; both
   halves verified in the run's own fv_report breakdown (pair guard + preflight, schema 2.7).
3. **Forward invariance: the other 24 names delta exactly 0.0** at the pair regen.
   `prices_daily.yaml` reverted before the regen (the 7/26 rule); no hand-typed prices
   (kr 59.6 is prose, not an input).
4. **Rider-4 watch — the calendar's reason for this date** (tanker_forward_print_ruling
   2026-07-14 §5): any 12M TC / FFA print in the H1 materials promotes immediately for its
   class, superseding the Stage-B schedule. Two named hooks: (a) the live VLCC 12M line IS
   BRUT's own Mount Horizon $105,700 single-print — if the report states Horizon's fixture
   terms differently, that is an input correction + Rider-4 event, NOT a tune; (b) Mount
   Vision's index-linked TC — index-linked ≈ spot stays the v1 convention, but any stated
   fixed leg or new 12M fixture on any hull promotes for VLCC.
5. **§15 / going-concern screen (the named resolution venue):** read the going-concern
   language against the $268.3M-due-2026 / $240.1M-H1-2027 wall. (a) Doubt persists,
   unfinanced → flags unchanged, `governance_discount_pct` stays 0 (a survival binary is
   not a tunable knob — owner 7/01); (b) financing secured in whole/part → record the
   terms, surface the tier call to the owner — do NOT self-upgrade; (c) worse language →
   owner same-day. AGM outcomes (today) are §15 evidence on the same screen.
6. **Tier/queue mechanics:** `cash-pending-H1-report` resolves HERE — TIER_SUBREASON
   updates, the cash `[ESTIMATE]` flag comes off with a clean citation (BRUT exits
   `NAV_FIGURE_ESTIMATE_QUEUE`; provenance guards expect exactly this transition); BRUT
   stays PROVISIONAL on going-concern §15 + max-torque. The expected drift-gate row (NAV
   +0-10%, EV up to ~+9pp, expected-direction) annotates citing THIS prereg, then
   `ratify_baseline` with cause — the 7/01 prereg pre-registered this re-ratify.
7. **The position read stays VOID regardless of the print.** POSITION_UNRELIABLE holds
   until the 8/16 toll-cliff deck re-derivation — the BUY (at any NAV this print lands)
   remains not-actionable, does NOT hand off to governance, and is NOT un-voided at this
   refresh. The scenario PW FV prints against the incoherent deck: record it, don't read it.
   No flip mechanics apply (already BUY-void; NAV-up cannot flip it away).
8. **Watchlist consensus legs stay the current vintage** (price/pnav/fwd_pe as_of
   2026-07-03; the rebase is its own staged draft — do NOT mix vintages at this refresh).

# TRMD Q2-2026 report-day refresh — PRE-REGISTRATION (written 2026-08-25 EVE, before the print)

**Reports 2026-08-26** (TORM Financial Calendar 2026, announced 2025-12-19; adherence
validated on Q1, May-13 = actual; TORM releases pre-market CET → lands overnight ET).
Frozen tonight per the INSW/BRUT/FLNG pattern. **The earnings train's second print, and the
most consequential: the LR1 anchor round (TRMD → VALIDATED-TIGHT candidacy) queues BEHIND
this refresh, and Stage B's window opens the same day.**

## Basis (current committed state)

NAV $30.22/sh · price $31.47 (8/25 close) · single FV $29.98 · BUY · tier
GOVERNED-WIDE·basis-pending (LR1 the last non-uniform product class; ruling
`PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md` frozen 7/15) · k_broker 1.17 at the stale 8/07
pnav (the 8/18 rebase draft re-pins; TRMD prints 0.89 on the 8/18 daily) · sheet vintage
2026-Q1: cash 196.4 + WC 254.9 − debt 1,081.8 (incl. the $10.0M ROU; leases 0 by
construction) − NB commitments 31.2; 103.3M diluted · fleet 95 in-water (22 LR2 + 10 LR1 +
63 MR) + 2 MR resales on-curve §9.6 delivering Q2 · figure queues ALL CLEAR (7/02
reconciliation; scrubbers 85 verified).

## Predicted Q2 drivers (knowable tonight)

- **The 2 Q1-bought MR resales DELIVER in Q2** → manifest rows flip on-curve→operating,
  the $31.2M commitment spends. ≈ NAV-neutral at delivery (§9.6 by construction).
- **The 6 post-Q1 MR resales ENTER the 6/30 sheet** (Q1's Note 11 subsequent event
  becomes an in-quarter fact): expect ~$250–290M-class new commitments, deliveries
  2027–28, wired ON-CURVE per the 7/02 TRMD convention (in-sector MR, clean). Every
  figure MUST be filing-cited — TRMD is the name whose six `[ESTIMATE]`s taught the rule.
  ≈ NAV-neutral-to-small-positive if bought at market (MR resale tape since: ~$60M/hull
  on the 8/18 daily's 2×MR print — ABOVE the likely Note-11 cost basis → potential
  positive mark-vs-cost gap, but DO NOT book it from this doc; the filing rules).
- **Cash/WC build POSITIVE, war-quarter products**: Q2 MR/LR2 spot elevated (peer prints:
  HAFN/STNG Q2 already landed strong) less the Q1 distribution paid in Q2 (TORM ~100%
  payout cadence). Net ≈ +$0.3–1.0/sh, wide because the distribution figure is not on
  file tonight.
- **Uniform ~0.5y aging** on ~$3.78B GAV ≈ −$0.50–0.62/sh.
- **Unknowable until the note**: post-6/30 S&P (the Q3 SLB purchase-option repurchases are
  ALREADY known subsequent events — they stay OUT), buybacks, the Q2 distribution
  declaration, any LR2/LR1 charter-out disclosures.

## Registered band

**Point NAV ≈ $30.40/sh; band [28.00, 32.80] (±8%).** Landing outside → HALT and
investigate the INPUT (a missed S&P event, a mis-cited resale figure, a distribution
surprise, a basis change) before accepting.

## Halt/verification conditions

1. **Subsequent-events note FIRST**; post-6/30 events (incl. the Q3 SLB buyouts) do NOT
   enter the Q2 snapshot.
2. Pair lands together: `trmd_2026-Q2.yaml` (provenance trio — the FLNG guard catch 8/25
   is fresh: `source_url`/`retrieved_at`/`filing_period_end` machine-readable, not prose)
   + manifest `report_date` bump + ages +0.5 in ONE commit.
3. **Forward invariance: the other 24 names delta exactly 0.0** at the pair regen.
4. **SEQUENCING — one FV-event at a time (the D-4 discipline):** the refresh runs FIRST on
   the HELD curves (pair flow). The LR1 contract-floor execution (TRMD → VALIDATED-TIGHT,
   frozen prereg + the mr_secondhand §5 extract-refresh rider) is its OWN post-refresh
   event, and Stage B's ±10% class-bucket re-check is its own docket — neither bundles
   into the report-day commit.
5. **Stage-B basis capture**: TORM's Q2 term-rate/coverage disclosures (LR2/LR1/MR
   bookings, TC-out cover, QTD Q3 bookings) extracted to the Stage-B class-bucket
   evidence BEFORE Stage B runs — the INSW condition-5 pattern.
6. **The 6-resale entry gates on citations**: commitment total, per-hull or aggregate
   price, advances paid, delivery windows — each to the 6-K note. An `[ESTIMATE]` on any
   of these re-queues TRMD in `NAV_FIGURE_ESTIMATE_QUEUE` (the guard enforces).
7. **Flip discipline**: TRMD is BUY. A BUY→HOLD band-mech flip on the print-day tape is
   plausible (EV +13.8% at the 8/25 close vs the ~+10% HOLD edge under a −NAV print) —
   any flip → individual eyeball; **any flip toward BUY elsewhere in the forward-invariance
   check = halt** (standing ADDENDUM rule).
8. **Distribution check**: capture the Q2 declaration; policy YAML moves only on a
   DECLARED structural change, not on the quarter's amount.
9. Watchlist consensus legs stay at their committed vintage — the 8/18 rebase draft
   promotes separately (owner); do not mix vintages in the refresh commit.
10. `prices_daily.yaml` reverted before the regen (committed 8/25 vintage = clean tree).

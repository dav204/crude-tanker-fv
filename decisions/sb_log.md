# SB — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Status:** _First snapshot — onboarding baseline._

**Decision: ONBOARDED 2026-06-27 — 4th dry-bulk validator (Safe Bulkers, NYSE: SB).**
Greek dry-bulk pure-play, Q1-2026 6-K (CIK 1434754). **43 on-curve owned vessels**
(36 Pana = 8 Panamax + 12 Kamsarmax + 16 Post-Panamax; 7 Cape) + 2 held-for-sale
off-curve at the $30.2M carrying value (Pedhoulas Commander, Xenia) + 1 chartered-in
excluded. 11 NB (10 Kamsarmax + 1 Cape). 8.00% Series C/D preferred = $100M (subtracts
from common NAV). Common shares 101.83M.

- **§15 governance — DECLINED the haircut** (`governance_discount_pct = 0`), carry with
  the related-party fee load as the headline tripwire. SB is Hajioannou-controlled
  (~47.5% via Vorini, sole voting power) and the three Managers (Safety Management
  Overseas / Safe Bulkers Management / Monaco) are family-controlled: €950/day per vessel
  + €5.0M/yr ≈ ~$22M/yr ≈ **~1.5% of GAV — the HIGHEST of the declined §15 names** (vs
  CMBT ~0.2%). But it is ~market-rate full ship-management (not an external-manager
  promote / incentive-on-NAV), dividends are pari-passu (common $0.06/qtr + preferred
  $0.50/qtr both pro-rata), and SB's discount-to-NAV is sector-wide (all dry-bulk names
  <1x), not governance-specific extraction. Held un-haircut for consistency with the
  other 3 dry-bulk validators (SBLK/GNK/CMDB, all un-haircut). Tripwires: the €950/day
  fee rising / off-market; above-market related-party drop-downs sans fairness opinion;
  common-dividend suspension while the family is paid; control → squeeze-out.
- **Reconciliation BASELINE (first-run):** tool NAV **$10.14** vs broker NAV **$7.26**
  (APPROX P/BV proxy, consensus_pnav 0.88 = price/common-book $7.30) → **gap +39.6%,
  SANITY = n/a** (APPROX cohort — NO Pareto coverage, verified 0 mentions in 135 2026
  dailies; no public VIE NAV). Scenario FV $9.52 vs price $6.39 → **EV +49%, BUY**.
- **THE +39.6% WIDE GAP — explained, not a bug** (SANITY n/a but documented per the
  "wide spread is a call or a bug" discipline): the tool marks SB's 43 on-curve vessels
  at **$1,351M vs the 6-K vessels-net book $1,061M (+27%)**. Two drivers: **(1) SB's book
  is conservative depreciated/impaired cost** — $24.7M/vessel average for a Kamsarmax/Cape
  fleet (avg age 10.5y) sits well below market in this strong dry-bulk cycle; this is most
  of the gap and is NOT a tool error (book understates, the tool marks to the transaction-
  anchored curves). Against the only external market-NAV proxy (~$8.40/sh non-broker model)
  the gap is ~+21%. **(2) Post-Panamax over-valuation — the §11.7.10 limitation, and SB
  exercises it more than any name** (16 Post-Panamax of 36 Pana-class, incl. 6 at 92-95.8k).
  The §11.7.1 collapse values Post-Panamax at the Kamsarmax "Pana" curve, and dwt-scaling
  lifts the 85-96k hulls 1.04-1.17× off the 82k baseline — generous for OLD (2006-2013)
  Post-Panamax that trade at a per-tonne discount. (Measured: the dwt-scaling itself adds
  only ~$0.20/sh; the larger effect is the base Pana curve treating Post-Panamax =
  Kamsarmax, ~$0.3-0.6/sh.) **Net: treat the +49% EV as the high end — the NAV is mark-rich
  and book-anchored; a more conservative read (model NAV $8.40 / common book $7.30) still
  has SB cheap-to-fairly-valued at $6.39.**
- **Refinement candidate:** SB makes the strongest case on the watchlist for a dedicated
  **Post-Panamax sub-class** (separating ~85-96k from the 82k Kamsarmax curve) — flagged
  in METHODOLOGY §11.7.10. Deferred (out of scope for the onboarding); revisit if the
  Post-Panamax book proves to drive a mis-call.
- Baseline re-ratified to include SB @ this first-run gap.

**Decision:** _[pending — fill in the four input YAMLs + watchlist row, then
run `python -m crude_tanker_fv.pipeline {QUARTER}`. After the first run, the
pipeline prepends a structured model-state entry above this line.]_

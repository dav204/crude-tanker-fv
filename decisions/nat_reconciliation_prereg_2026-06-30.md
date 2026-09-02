# NAT — full balance-sheet reconciliation, PRE-REGISTRATION (2026-06-30)

Clears the P0 item: NAT's headline FV was **VOID** (the ~$17M newbuild advance
was contradicted by the Q1-2026 cash flow; the ~$153M commitment traced to no
disclosure). This is the *pre-registration* — the sourced figures, the treatment
decisions, and the **predicted NAV band committed AHEAD of the recompute**. Per
the discipline: commit this, then recompute; **halt on a miss and investigate the
INPUT**; never source mid-recompute. Sourcing was completed and adversarially
verified (5-agent workflow) BEFORE this file was written.

## Sources of record (pulled from EDGAR, this session)
- **FY2025 20-F** — acc `0001140361-26-017809`, filed 2026-04-29 (audited Dec-31-2025
  balance sheet + notes; XBRL R-pages R2/R4/R5/R8/R12/R16/R18/R21/R23/R46/R50/R52/R55/R57).
- **Q1-2026 6-K** — acc `0000919574-26-003779`, filed 2026-06-01 (CONSOLIDATED CONDENSED
  BALANCE SHEET at **Mar-31-2026** = the 2026-Q1 quarter date; financing narrative; cash flow).
- **Pareto Shipping Daily 2025-11-04** — the only dated source for the newbuild price
  (`outputs/pareto_mentions_nat.md (pruned 2026-09-02 — regenerate on demand with `sp_scan --names NAT`)`): "NAT orders suezmaxes at $86m with H2'28 delivery" (LOI stage).

## Sourced reconciliation (Mar-31-2026 = 2026-Q1), each figure cited

| Field | Old (void/estimate) | **Sourced** | Citation |
|---|---|---|---|
| `cash_and_equivalents` | 75,000,000 `APPROX` | **81,120,000** | 6-K condensed BS |
| `working_capital_net` | 25,000,000 `APPROX` | **53,569,000** | 6-K: (AR 23,183 + Prepaid 20,487 + Inv 15,926 + Voyages 23,014 + Other 538) − (AP 5,654 + Accrued Voyage 14,585 + Other CL 9,340); ex-cash, ex-debt, ex-HFS |
| `held_for_sale` (NEW field) | — | **65,000,000** | 20-F Note 15 / R57: 2003-build $25M (Feb-9) + 2005-build $40M (Mar-17), firm-agreed, Q2-2026 close |
| `total_debt` | 395,000,000 `APPROX` | **415,394,000** | 6-K: 35,404 current + 379,990 non-current (gross 418.8 − 3.4 deferred fin-costs; CLMG/Beal $140.9M + Ocean Yield $277.9M) |
| `lease_liabilities` | 5,000,000 | **343,000** | 6-K Other Non-Current Liabilities Mar-31 (NAT breaks out no separate lease line; ROU asset $738K Dec-31 per 20-F) |
| `newbuild_capex_commitments` | 153,000,000 (`~$170M−$17M`) | **0 (PARKED)** | 2 Suezmax NB, delivery H2-2028, contracts signed Jan-2026. Firm price **undisclosed by NAT** (20-F Note 15 / R57 tag the order with NO price element while pricing the $25M/$40M sales + $35.9M dividend in the same table). Only source = Pareto 2025-11-04 LOI ~$86M/ship (~$172M). Parked pending a filed price. |
| `newbuild_advances_paid` | 17,000,000 | **0 (contradicted → removed)** | FY2025 "Investment in Vessels" −$134,450K = the 2 Sungdong ACQUISITIONS (ties to Vessels Additions $133,748K); Q1-2026 "Investment in Vessels" +$38K inflow; NO construction-in-progress asset anywhere |
| `diluted_shares_outstanding` | 211,750,663 | 211,750,663 ✓ | 20-F R5 parenthetical + 6-K |
| **Operating fleet** | 18 | **16** | 20-F R46 "20 vessels" Dec-31 = 18 operating + 2 HFS (Sprinter/Luna, delivered Jan-2026) → 18 operating → less 2 reclassified-HFS (2003+2005 builds) = **16 operating + 2 HFS** at Mar-31. Manifest overcounted operating by 2. |

## Owner treatment decisions (2026-06-30)
1. **Newbuilds — PARK at $0 net NAV.** Do NOT wire the §9.6 on-curve mark. The commitment
   rests on a broker LOI (Pareto), the firm price is deliberately undisclosed, so it is **not
   out of the figure-provenance queue** → the on-curve fix is unauthorized (CLAUDE.md). Both legs
   (commitment + delivered-value) parked → the reconciliation is **independent of the one number
   that can't be sourced**. Re-cite the LOI for the record; keep the price a tracked open item.
2. **Held-for-sale — $65M contracted** (not a judgment call: the sourced realizable value; both
   sales firm-agreed + sourced). Carrying $30.6M would reintroduce the depreciated-cost error the
   project exists to remove. Booked via a **dedicated `held_for_sale` field** (the model had none).
3. **De-void**: the $17M contradiction is resolved (advances→0), so NAT leaves `NAV_DERIVED_VOID`.
   NAV/FV/gap become real numbers computed off sourced figures.
4. **Tier = GOVERNED-WIDE (newbuild-indeterminate), NOT TIGHT.** Directional-only; the newbuild
   price stays an explicit open item (`NEWBUILD_PRICE_PENDING`). NAT is de-voided but not tight —
   it has 2 newbuilds carried at $0 (an acknowledged indeterminate) and a firm price NAT won't
   disclose. **NAT reads "rich · cycle position (not a short)" (§12) — NOT a new actionable long;
   the actionable-long surface stays SB + SBLK.** Clearing the void is a completeness win.

## PRE-REGISTERED PREDICTION (committed ahead of recompute)
- **NAV/sh: $2.79** — band **$2.72 – $2.86**. (Baseline txn-anchored $2.0732 reproduced exactly;
  delta +$0.72/sh = newbuild-parking +$0.642 · WC +$0.135 · debt −$0.096 · cash +$0.029 · leases
  +$0.022 · HFS-swap −$0.012.) Basis: transaction-anchored marks (default-on), HFS via the new
  field (identical additive NAV effect as folding into WC in the prediction calc).
- **NAV-only EV vs price $5.78 ≈ −51.7%.** Blended/scenario FV and EV will rise with NAV (NAT is
  w_nav-heavy at peak); position stays **rich · cycle position (not a short)**.
- **Guards:** `test_manifest_provenance` clears for NAT (no uncited estimate in the NAV equation —
  commitment=0, all lines cited); `test_newbuild_convention` no longer parametrizes NAT (no wired
  newbuild); suite stays green (315+); drift gate expects a **material, annotated** NAT move
  (NAV/EV) — re-ratify after acceptance.

## HALT criteria (investigate the INPUT, do not tune to match)
- Recomputed NAV/sh **outside $2.72 – $2.86** → halt, find the input discrepancy.
- SANITY ≠ OK (tool NAV vs broker NAV wider than ±50%) → halt.
- Any guard red that isn't the *expected* NAT clearances above → halt.

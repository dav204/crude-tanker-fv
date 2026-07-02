# STNG — full per-vessel reconciliation (the tangle), PRE-REGISTRATION (2026-07-01)

Seventh P0 reconciliation (Scorpio Tankers), and the most TANGLED — two large errors pointing in
OPPOSITE directions (a $200M debt double-count + a fleet↔HFS double-count) that nearly cancel, so a
half-fix would report a wildly wrong intermediate NAV. Owner-directed FULL per-vessel rebuild.
Sourced to the Q1-2026 6-K (EDGAR acc 0001483934-26-000042, Exhibit 99.1, as-of 2026-03-31).

## The two big errors (opposite directions)
1. **`total_debt` double-counts the $200M notes.** STNG's own "Gross debt outstanding, March 31, 2026 =
   **$589,056K**" (L90: bank $389.1M + Unsecured Senior Notes 2030 $200M; net cash $395.3M). The model's
   $789.1M took the $589.1M TOTAL as "bank" and added the $200M notes AGAIN. → total_debt $789.1M → **$589.056M**
   (+$200M NAV). (Balance-sheet carrying $581.2M net of issuance costs; use the $589.056M gross STNG reports.)
2. **The $395M HFS line double-counts operating vessels + is a wrong list.** The exhibit's 87-row fleet table
   marks **9 vessels "(22)" = "agreement to sell, close in Q2"**, so the manifest's 87 on-curve INCLUDES the HFS
   vessels. The model's HFS list is wrong: **STI Broadway/Condotti/Winnie/Lauren ($285.8M) are OPERATING** (not
   under any sale agreement); **STI Lavender** already CLOSED in Q1 ($61.2M, gone). The REAL 3/31 HFS is the
   **March 8-vessel agreement**: Solidarity LR2 $60M + Seneca/Osceola/Brooklyn/Black Hawk 4 MRs $140M +
   Aqua/Regina/Opera 3 MRs $105M = **$305M agreed** ($215M carrying = the balance-sheet "Assets held for sale").

## The per-vessel rebuild (dates reconciled)
- **6 of the 8 HFS vessels are in the manifest and double-counted** (Aqua/Regina/Opera 2014 MRs + Osceola/
  Brooklyn/Black Hawk 2015 MRs) → REMOVE from the on-curve fleet: MR 41 → 35 (2014_scr 8→6, 2014_nscr 2→1,
  2015 10→7). Seneca + Solidarity closed April (not in the report-date manifest — no double-count). The
  April Park/Sloane/Madison LR2 sale ($195M) is a SUBSEQUENT event — those 3 stay OPERATING at 3/31.
- **HFS → the `held_for_sale` field at $305M** (the 8-vessel March agreement), OUT of working_capital_net.

## Sourced figures ($k, 3/31, all cited to the Q1-2026 6-K)
| Field | Model | **Sourced** | Citation |
|---|---|---|---|
| `cash` | 984,300 | **984,321** | BS "Cash and cash equivalents" (L217) — verified |
| `total_debt` | 789,100 | **589,056** | "Gross debt outstanding 3/31 589,056" (L90) — double-count fixed |
| operating WC | 207,800 | **163,273** | AR 225,245 + inv 10,897 + prepaid 9,188 − AP 37,454 − accrued 44,603 (was missing accrued) |
| `held_for_sale` (NEW) | (in WC $395M) | **305,000** | March 8-vessel agreement (L40) — replaces the wrong $395M list |
| `newbuild_advances_paid` | 90,000 `[EST]` | **69,069** | BS "Vessels under construction" (L225) — replaces the estimate |
| `diluted_shares` | 50,030,000 | 50,025,865 ✓ | EPS table (L206) — verified |
| lease_liabilities | 0 | 0 ✓ | SLB fully repaid Q1 (L232) |

## PRE-REGISTERED PREDICTION
- **Base NAV/sh $80.97** (headline txn-anchored ~$77.5), band **$77.2 – $77.8** headline. Δ from current
  headline $80.35 ≈ **−$2.85** (debt +$200M · HFS/fleet −$280M · advances −$21M · opWC −$44.5M — the offsetting
  errors nearly cancel). Gap to broker $108 ≈ **−25%** (unchanged; a wide, documented tool↔broker spread — feature).
- **Tier:** STNG leaves `NAV_FIGURE_ESTIMATE_QUEUE` (advances sourced; no uncited estimate left), but STAYS in
  `OFF_CONVENTION_QUEUE` → **PROVISIONAL · off-curve**. Sub-reason `uncited-figure` → `off-curve`.
- **FLAGGED FOR THE OWNER (out of this rebuild's scope):** the 10-vessel newbuild is off-curve, carried as a
  **−$504M commitment-only drag** (advances $69M − commitment $573M, no offsetting asset — the §9.6 violation).
  STNG's NBs are REAL 3/31 commitments, so wiring on-curve (§9.6) would add **~+$481M NAV (~+$9.6/sh)** — a
  material separate decision, complicated by the **2 VLCC NBs** (STNG's first crude exposure — cross-sector).
- Position stays rich/cycle vs the tool's conservative marks; STNG is a deep-discount-to-BROKER net-cash name,
  but the tool NAV is even more conservative. NOT a clean actionable long on the tool's marks.

## HALT criteria
- Recomputed base NAV/sh outside **$80.5 – $81.5** → halt, investigate.
- SANITY not OK, or any guard red that isn't the expected STNG queue change → halt.

## OUTCOME (2026-07-01) — landed in band, committed
- Base NAV **$80.97** (pre-reg $80.5–81.5 ✓); headline **$77.47** (pre-reg $77.2–77.8 ✓); position **BUY→HOLD**
  (the −$2.90 base drop crossed the fairly-valued threshold — the honest read: $77.47 vs price $75.60 ≈ fair,
  not the BUY the double-counted-debt / understated-NAV made it look). SANITY OK (−28.3% to broker $108).
- Full suite 442 pass / 19 xfail; drift gate STNG **explained**, 0 unexplained; prices untouched (isolated).
- STNG **left `NAV_FIGURE_ESTIMATE_QUEUE`** (advances sourced), **stays `OFF_CONVENTION_QUEUE` → PROVISIONAL·off-curve**
  (`TIER_SUBREASON` `uncited-figure`→`off-curve`).

## §9.6 NEWBUILD — DEFERRAL DECISION (owner, 2026-07-01)
The 10-vessel order book (2 MR + 4 LR2 + 2 VLCC) is **deferred as its own pre-registered step**, NOT wired with
this rebuild. Rationale (owner):
1. **Attributable-step discipline.** Full on-curve wiring is **~+$481M NAV (~+$9.6/sh → base ~$90.6)** — the largest
   single headline move left in the queue. A +12% NAV swing on one methodology decision gets its OWN pre-registration
   + drift gate + re-ratify; it must not be bundled with a data correction.
2. **Cross-sector / unresolved-input: the 2 VLCC portion is BLOCKED on thread (d)** (`curve.newbuild` basis
   inconsistency — the crude age-0 mark is RESALE-basis, VLCC $175M plausibly stale-high, still provisional). STNG's
   VLCCs would mark on that curve, so wiring them now imports the quarantined crude-level uncertainty onto STNG's
   clean product NAV. **Thread (d) now gates STNG's VLCC portion**, alongside BRUT + the crude names.
3. **Likely structure when it's worked:** wire the **6 product hulls (2 MR + 4 LR2) on-curve** (within-sector,
   settled product curve; ~+$7/sh), **park the 2 VLCCs off-curve pending thread (d)**. Source per-hull delivered
   marks + delivery schedule, predict per-class bands AHEAD, gate as its own attributable re-ratify.
4. **Classification:** even fully wired at ~$90.6 (nominal deep BUY vs $75.60), the cheapness would rest partly on
   the provisional VLCC resale mark → **GOVERNED-WIDE at best, not TIGHT.** The §9.6 wiring does not manufacture a
   clean tight actionable long — the arc finding holds seven-for-seven (cleaner + still directional; SB/SBLK remain
   the only two tight longs).

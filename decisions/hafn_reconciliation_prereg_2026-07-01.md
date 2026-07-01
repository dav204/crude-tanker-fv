# HAFN — full balance-sheet reconciliation, PRE-REGISTRATION (2026-07-01)

Sixth P0 reconciliation, and the MOST consequential — HAFN (Hafnia) had multiple errors + genuine
forks (not a clean validate like ECO). The recurring theme: **balance-sheet-literal ≠ NAV-economic**
(three times over: subsequent-event newbuild, TORM fair-value-vs-issuer-method, pool-gross-up WC).
Workflow-sourced (12 agents) + independent read of the Q1-2026 6-K BEFORE this file.

## Source of record
Q1-2026 6-K, EDGAR acc `0001140361-26-022910`, Exhibit 99.1 (interim financials, IFRS) + 99.2 (press
release), as-of 2026-03-31. Hafnia's OWN disclosed NAV/sh = **$8.09** (the sanity anchor).

## Sourced reconciliation ($m, 2026-03-31)

| Field | Model | **Sourced/decided** | Citation | Verdict |
|---|---|---|---|---|
| `cash` | 146.5 | **146.457** | BS "Cash at bank and on hand" (Note 4 cross-check) | ✓ verified |
| `total_debt` | 943.5 | **953.932** | Note 2/Note 4 BANK borrowings (219,536 + 734,396); the model matched no line (~$10.4M light) | ⬆ corrected |
| `lease_liabilities` | 35.9 | **71.597** | Note 2 SLB (35.730) + other-lease (35.867); model captured ONLY the chartered-in piece | ⬆ corrected |
| operating WC | ~80 `[EST]` | **85.7 FLOOR** | see fork (b) — pool-gross-up-pending | ⚠ flagged floor |
| TORM stake | 395 (market) | **277.2 lower-of-cost** | see fork (a) — Hafnia's own NAV method | ⬇ corrected |
| `newbuild_capex_commitments` | 405 | **0** | 8 MR HHI order signed **3-Apr-2026** (Note 7 subsequent event) | ⬆ removed |
| `newbuild_advances_paid` | 40 `[EST]` | **0** | no CIP line at 3/31; order post-dates quarter — phantom | ⬆ removed |
| `diluted_shares` | 500 `[EST]` | **505,321,911** | Q1 EPS table (diluted); dividend-implied 499.85M | ✓ sourced |

## Owner treatment decisions (2026-07-01)
1. **Newbuild — strict 3/31: commitment $0, advances $0 (the ASC rule).** The $405M HHI order was signed
   **3 April 2026** (Note 7 subsequent event), after quarter-end — the same "double-anachronism" as ASC
   (a −$405M commitment with no offsetting asset + a $40M advance that couldn't predate the contract).
   Excluded from the 3/31 snapshot; to be wired on-curve in Q2 (§9.6, delivery Q3-28→Q2-29). +$365M NAV.
   HAFN leaves `OFF_CONVENTION_QUEUE` (no 3/31 newbuild to place on-curve).
2. **TORM 13.97% stake — $277.2M lower-of-cost (owner).** NOT $395M market / $408.5M fair value. Matches
   **Hafnia's OWN NAV methodology** ("the lower of the market value or purchase price of the Torm investment")
   → preserves comparability to Hafnia's published $8.09 NAV/sh. Precedent set: **a marketable equity stake
   inside a shipping NAV is valued at the ISSUER's own NAV-method basis (lower-of-cost) when disclosed, not
   fair value** — fair value injects market volatility + breaks the sanity-check alignment. ($277.2M is
   derived: market $395.0M − Q1 FV gain $117.8M; the only soft number, so it stays inside the flagged WC line.)
3. **Operating WC — $85.7M conservative FLOOR, pool-gross-up-pending (owner).** Do NOT book the gross
   balance-sheet $335.9M: Hafnia runs the world's largest product-tanker POOL, so the $670M receivables carry
   **custodial pass-through gross-up** (money collected on behalf of other pool owners — not a NAV-economic
   asset). The 6-K does NOT break out pool vs own-account receivables/payables, so a clean net is not
   computable → book the conservative floor ≈ the clean own-account **inventory $85.7M** (receivables/payables
   conservatively netted to ~0), reject the gross $335.9M. **HAFN STAYS PROVISIONAL on WC** (`pool-gross-up-
   pending`), resolves when a filing discloses the pool net. Precedent: **for a pool operator, gross pool
   receivables are custodial, not NAV-economic — net the gross-up out or book the conservative floor + flag.**
   (Confirms Hafnia's own $8.09 nets the pool too — no NAV counts custodial pass-through as equity.)
4. **Debt/lease corrected** (mechanical, high-confidence): total_debt → $953.9M (bank borrowings), lease →
   $71.6M (SLB + IFRS-16), disjoint (tie to the $1,025.5M Note 2 total; NAV subtracts both, no double-count).
   The model's unexplained ~$10.4M debt gap is resolved by using the primary $953.9M.
5. **Shares → 505,321,911** (diluted, EPS table). working_capital_net = $85.7M op floor + $277.2M TORM = $362.9M.

## PRE-REGISTERED PREDICTION
- **Base NAV/sh $5.69** (headline txn-anchored ~$5.57), band **$5.50 – $5.65** headline. Δ from current
  headline $5.22 ≈ **+$0.35** (newbuild +$365M · TORM −$117.8M · debt/lease −$46.1M · shares dilution).
- Gap to broker $8.11 ≈ **−31%** (narrows from −35.6%). A wide, documented tool↔broker spread (txn-anchored
  marks < broker resale) — a FEATURE, not an error. SANITY OK.
- **Tier: PROVISIONAL, sub-reason `pool-gross-up-pending`** (a WAITING state — every other figure now sourced/
  decided; only the pool-grossed operating WC is a conservative floor pending a pool-net disclosure). HAFN
  leaves `OFF_CONVENTION_QUEUE`, stays in `NAV_FIGURE_ESTIMATE_QUEUE` via the flagged WC floor. NOT handoff-ready.
- **HAFN is NOT actionable** — directional, ~fair-to-cheap vs its own $8.09 but wide to the tool's conservative
  marks. Tight-actionable-long surface stays SB + SBLK.
- Remaining (out of scope, noted): the manifest fleet is class-cohort APPROXIMATED (scrubber/eco/age + the
  HFS cohorts) — refresh vs Note 8 Fleet list; HAFN stays in `OPERATING_SCRUBBER_QUEUE`.

## HALT criteria
- Recomputed base NAV/sh outside **$5.60 – $5.80** → halt, investigate the input.
- SANITY not OK, or any guard red that isn't the expected HAFN queue changes → halt.

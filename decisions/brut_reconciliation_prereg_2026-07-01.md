# BRUT — balance-sheet trace + cash-floor + governance correction, PRE-REGISTRATION (2026-07-01)

Fourth P0 reconciliation. Unlike ASC/NAT, this one **VALIDATES the model** — the Pareto-estimate
figures were accurate; the reconciliation traces them to primary issuer docs, books a conservative
cash floor, and corrects a fabricated governance block. BRUT does NOT become actionable (it stays
PROVISIONAL, directional-only — a going-concern-doubtful, max-torque, resale-level-provisional NAV).
Sourcing done via a 9-agent workflow + an independent read of the primary docs BEFORE this file.

## Sources of record (on disk)
- **FY2025 Annual Report** — `inputs/research_issuer/2025_brut_annual_report.pdf` (audited US GAAP, PwC;
  Dec-31-2025 balance sheet + Note 8 Newbuildings + Note 10 Commitments + Note 15 Subsequent Events +
  Board Report; signed 2026-03-26). ISSUER, source of record.
- **Euronext Information Document** — `inputs/research_issuer/2024-11-26_brut_euronext_information_document.pdf`
  (Nov-2024 admission; the "prospectus" the model said was "NOT located" — it IS on disk; governance/fees
  + the original 2-VLCC contract mechanics). NOTE: Nov-2024 vintage, 2-VLCC / 15.6M-share era.
- **Pareto initiation** — 2026-04-22 (BROKER, cross-check only; demoted below issuer).

## Sourced reconciliation (as-of 2026-03-31 = Dec-2025 actual rolled through Q1 subsequent events)

| Field | YAML (Pareto est.) | **Sourced (3/31)** | Citation | Verdict |
|---|---|---|---|---|
| `newbuild_capex_commitments` | 1,370.0M | **1,373.1M** | Note 10 6-vessel base $661.7M + Note 15 Jan-order (Venture/Voyager) $236.0M + Note 15 CIMC 4-vessel $499.0M − Q1 installments $23.6M (Board Report) | ✓ confirmed |
| `total_debt` | 0 | **0** | Dec-2025 total liabilities $0.161M (trade payables+accruals only); no debt line; draws on delivery (first Jul-2026) | ✓ confirmed |
| `diluted_shares_outstanding` | 61,900,000 | **61,923,808** | Dec-2025 52,399,998 (BS p.15) + Feb-2026 placement 9,523,810 @ $5.25 (Note 15) | ✓ confirmed |
| `newbuild_advances_paid` | 0 | **0** | §9.6/FRO/CAPT convention (paid installments sunk into cash; NB at delivered-market less commitment) | ✓ convention |
| `cash_and_equivalents` | 100.0M | **66.0M (floor; band 66–116M)** | Dec-2025 $89.661M (BS p.15) + Feb placement +$50M gross (Note 15) − Q1 installments −$23.6M = $116M point; **CIMC ~$50M deposit likely paid at March execution → $66M floor** | ⚠ PROVISIONAL |

## Owner treatment decisions (2026-07-01)
1. **Trace now, defer cash (Fork 1-A).** Re-cite the 4 confirmed figures to the Annual Report (bank the
   provenance). Cash stays flagged → **BRUT stays PROVISIONAL overall**, new sub-reason
   **`cash-pending-H1-report`** (a well-specified WAITING state — sourced except one figure with a known
   resolution date — distinct from NAT's `void` or a plain `uncited`).
2. **Cash = $66M conservative FLOOR (Fork 2-C), NOT the $116M point, NOT Pareto's $100M middle.** Rationale
   (owner): the tier is PROVISIONAL either way, so book the number least likely to mislead; errors are
   asymmetric (over-stating a going-concern-doubtful max-torque name is the dangerous direction); the
   going-concern context makes "the CIMC deposit was paid at March execution" the MORE likely state (you
   don't contract 4 VLCCs without the execution installment); and $100M is an unsourced broker midpoint —
   use the conservative end of the OWN sourced range, flag it a floor, pre-register the Aug-13 resolution.
3. **Fix the fabricated governance NOW** (a provenance error, not cash-gated). The YAML's "Goodwood Ship
   Management / Koch ~26% / no >50% controller / dispersed" is INVENTED — the primary docs show managers
   **2020 Bulkers Management AS + Himalaya Shipping** (no Goodwood), **no Koch**, and a **Trøim-sponsored**
   vehicle (Drew Holdings 48.15% at the Nov-2024 admission — now diluted post four issuances, so current %
   UNRESOLVED pending the register), **Magni support agreement = ZERO fee**. Correct to the sourced facts.
4. **Going-concern doubt = the §15/risk headline, recorded not buried.** The issuer states *substantial
   doubt about the ability to continue as a going concern* — the 12-VLCC program is UNFINANCED ($268.3M due
   2026 + $240.1M H1-2027, to be covered by hoped-for equity/debt/asset sales). BRUT's NAV is a levered bet
   on financing that does not yet exist → the biggest reason it is directional-not-actionable. Recorded as
   the §15/risk basis; `governance_discount_pct` kept **0** (a specific haircut % is a §15 judgment best set
   with financing clarity at H1-2026 — surfaced to the owner, not invented).
5. **VLCC resale-mark (Thread-1B) stays its own thread** — do NOT gate this reconciliation on it; but note
   it COMPOUNDS: BRUT is the book's most input-uncertain name on three independent axes at once (max-torque
   × level-provisional resale mark × $66–116M cash range × going-concern doubt).

## PRE-REGISTERED PREDICTION (committed ahead of the pipeline recompute)
- **NAV/sh $8.80** at the $66M cash floor (band **$8.80 – $9.61** spanning cash $66M–$116M; commitment
  +$3.1M and shares +23,808 are immaterial). Δ vs current $9.40 = **−$0.60/sh** (cash −$34M dominant).
- BRUT stays **PROVISIONAL · cash-pending-H1-report**; NOT handoff-ready. Position stays a directional
  **BUY** on paper (deep P/NAV discount) but the going-concern doubt makes the +% upside conditional —
  **NOT a new actionable long; the tight-actionable surface stays SB + SBLK.**
- Guards: BRUT STAYS in `NAV_FIGURE_ESTIMATE_QUEUE` (cash is a flagged floor — intended); the 4 other
  figures carry clean citations; `TIER_SUBREASON["BRUT"]` → `cash-pending`; suite stays green; drift gate
  expects a material, annotated BRUT move → re-ratify after acceptance (owner), and RE-RATIFY AGAIN at H1-2026.

## HALT criteria (investigate the INPUT; do not tune)
- Recomputed NAV/sh **outside $8.70 – $8.90** (at the booked $66M) → halt, find the input discrepancy.
- SANITY not OK (vs the Pareto broker NAV) → halt.
- Any guard red that isn't the expected BRUT state (still-in-queue via cash; the 4 clean figures) → halt.

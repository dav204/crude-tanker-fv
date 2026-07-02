# TRMD — full balance-sheet reconciliation, PRE-REGISTRATION (2026-07-01)

Eighth P0 reconciliation (TORM plc), and the LAST of `NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL`. TRMD's
prior balance sheet was the estimate-heaviest in the book — **six `[ESTIMATE]` figures** (WC, debt, the
bank/lease split, commitments, advances) plus all-estimated scrubber counts. Sourced to the **Q1-2026 6-K**
(EDGAR acc 0000919574-26-003082, Ex-99.1 "Interim Results for the First Quarter ended 31 March 2026"),
condensed consolidated balance sheet + Note 10 (contractual obligations). Scrubber/fleet detail cross-checked
to the **FY2025 20-F** (acc 0001628280-26-011954).

## The subsequent-events catch (the ASC/HAFN pattern, THIRD time)
The prior `newbuild_capex_commitments: $360M` bundled **6 MR resales that TORM bought "AFTER the end of the
quarter"** (Business Highlights: "after the end of the quarter, TORM has purchased a total of six MR resales,
with the first two … delivery already in Q1 2027 …"). Those are a **subsequent event** — NOT a 31-Mar-2026
commitment. The ONLY Q1 vessel commitment is the **2 MR resales (TORM Dehradun/Dapitan, 2015-built, Q2-2026
delivery)** agreed DURING Q1 — captured exactly by Note 10 "Second-hand vessels commitments: Total **$31.2M**."
Subsequent-events Note 11 otherwise holds only the $0.70/sh interim dividend (~$71.5M) — not NAV-moving.

## Sourced figures ($M, 31-Mar-2026, all cited to the Q1-2026 6-K balance sheet)
| Field | Model (est.) | **Sourced** | Citation |
|---|---|---|---|
| `cash` | 196 | **196.4** | BS "Cash and cash equivalents incl. restricted cash" — verified |
| `working_capital_net` | 110 `[EST]` | **254.9** | Inv 82.5 + TradeRec 249.6 + OtherRec 32.7 + Prepaid 14.3 − TradePay 67.2 − OtherLiab 53.2 − CurTax 0.7 − Prov 0.5 − PrepayFromCust 2.6 |
| `total_debt` | 1,089.6 `[EST]` | **1,081.8** | BS Borrowings non-current 795.1 + current 286.7 (incl. $10M ROU lease) |
| `lease_liabilities` | 5 | **0** | the $10.0M ROU lease is INSIDE Total borrowings — zero here to avoid double-count |
| `newbuild_capex_commitments` | 360 `[EST]` | **31.2** | Note 10 "Second-hand vessels commitments: Total 31.2" (the 2 Q1 MR resales; 6 resales are subsequent) |
| `newbuild_advances_paid` | 50 `[EST]` | **38.9** | BS "Prepayments on vessels" (Note 4) |
| `held_for_sale` | (0) | **0** | BS "Assets held for sale — " at 31-Mar (was 24.4 at 31-Dec; TORM Maren delivered in Q1) |
| `diluted_shares` | 103.3M | **103.3M** ✓ | wtd-avg 101.5M + dilutive options 1.8M (EOP ex-treasury 102.1M) — verified |

Cross-checks disclosed by TORM: own **NAV/share $29.7** ($3,036M NAV excl NCI / 102.1M sh), broker-valued
**fleet $3,619M** (vs carrying $2,889.5M), NIBD $894M.

## PRE-REGISTERED PREDICTION
- Balance-sheet Δ vs current model (all in $M): cash +0.4 · WC **+144.9** · debt +7.8 · lease +5.0 ·
  commitments **+328.8** · advances −11.1 = **net +475.8M** ÷ 103.3M sh = **+$4.61/sh**.
- **Base NAV/sh $26.74 → predicted ~$31.35** (band **$30.8 – $31.9**). Headline (txn-anchored) $25.43 →
  predicted **~$30.0** (band **$29.5 – $30.6**). Gap to broker $33.98: −25.2% → **≈ −12%** (headline);
  the new headline ≈ TORM's OWN disclosed NAV $29.7 — a strong corroboration.
- **Position likely HOLD → BUY** (EV was +4.8% at price $26.06; +$4.6 NAV lifts the scenario FV materially).
  This is the FIRST reconciliation of the arc that moves NAV **UP** materially (prior six were flat/down) —
  because the errors here (phantom $329M commitment + understated $145M WC) both suppressed NAV.
- **Tier:** with commitments/advances/WC/debt all sourced, TRMD **leaves `NAV_FIGURE_ESTIMATE_QUEUE`**. Two
  open items decide the final tier (owner forks below).

## OPEN FORKS (owner decision — present after verification)
1. **`working_capital_net` basis.** Operating-current-only **$254.9M** (tool convention, per STNG) vs a
   book-equity-reconciling **$230.0M** (nets the non-current items: −$45.2M held-over-gains tax, other
   non-current ±). Difference $24.9M (~$0.24/sh). Recommend operating-current $254.9M for cross-name
   consistency, flag the held-over-gains tax as a known small omission.
2. **The 2 MR resales §9.6 (`OFF_CONVENTION_QUEUE`).** Off-curve (commitment −31.2 + advances +38.9, no
   vessel; net +7.7) vs on-curve (add 2 age-11 MR ~$68M − commitment 31.2, advances→0; net +36.8). Diff
   ~$29M (~$0.28/sh). UNLIKE STNG, this is small, in-sector (both MR, product curve), near-immediate
   (Q2-2026 secondhand, no construction/PV-discount, no cross-sector VLCC issue) — so wiring on-curve is
   clean. If wired → TRMD leaves `OFF_CONVENTION_QUEUE`; tier gated only by scrubber verification.
3. **Scrubber counts (`OPERATING_SCRUBBER_QUEUE`).** All estimated (LR2 57% / MR 70% / LR1 30%). Source
   TORM's disclosed scrubber-fitted count from the 20-F; if it cross-foots, move to
   `OPERATING_SCRUBBER_VERIFIED`. Required for VALIDATED-TIGHT; else GOVERNED-WIDE.

## HALT criteria
- Recomputed base NAV/sh outside **$30.8 – $31.9** → halt, investigate the input (esp. WC — the biggest mover).
- SANITY not OK, or any guard red that isn't the expected TRMD queue change → halt.
- If the workflow's independent extraction disagrees with the hand-parse on any material figure → halt,
  reconcile to the primary source before proceeding.

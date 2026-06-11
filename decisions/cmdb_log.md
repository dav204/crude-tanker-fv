# CMDB — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-06-11T03:20:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.24
- Single-point FV: $19.84
- Scenario PW FV: $19.82 (EV +15.0%)
- NAV / share: $32.23
- Position: **BUY (undervalued)**
- Broker spread: -15.7pp (k_broker 0.84)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: -0.01 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T02:59:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.25
- Single-point FV: $19.84
- Scenario PW FV: $19.82 (EV +14.9%)
- NAV / share: $32.23
- Position: **BUY (undervalued)**
- Broker spread: -15.6pp (k_broker 0.84)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:17:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.25
- Single-point FV: $19.84
- Scenario PW FV: $19.82 (EV +14.9%)
- NAV / share: $32.23
- Position: **BUY (undervalued)**
- Broker spread: -15.6pp (k_broker 0.84)
- Sector: dry_bulk

**Material deltas since last run:**
- ⚑ single-point FV -30.0%
- ⚑ scenario PW FV -30.0%
- ⚑ broker spread +6.7pp
- Δprice: no change | Δsingle FV: -30.0% | Δscenario FV: -30.0% | ΔNAV: no change | Δspread: +6.7pp

**Decision:** _**§15 GOVERNANCE HAIRCUT SET AT 30% — owner decision
2026-06-10** ("roughly equivalent to TEN: management concerns /
related-party transactions / lack of return to common"). The −30.0% FV
delta IS the haircut application, not a market move; asset NAV unchanged
at $32.23 per the §15 convention (blend layer + strip terminal only).
New headline: PW FV $19.82 vs price $17.25 → **+14.9% EV, mild BUY**
(was +64.2% pre-haircut). With payout at 0, the entire strip is terminal
NAV, so the haircut passes through ~1:1 — the cleanest §15 application
yet. CMDB is now the second §15 case (METHODOLOGY §15.3 updated).
Calibration note: no external anchor exists to triangulate the 30%
(unlike TEN's VIE Bullish cross-check) — it is a TEN-equivalence
judgment. Revisit trigger: any dividend/buyback initiation (the natural
catalyst on a net-cash balance sheet) → re-examine drivers 2 and 4._

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.25
- Single-point FV: $28.35
- Scenario PW FV: $28.32 (EV +64.2%)
- NAV / share: $32.23
- Position: **BUY (undervalued)**
- Broker spread: -22.3pp (k_broker 0.84)
- Sector: dry_bulk

**Status:** _First snapshot — no prior state to compare._

**Decision:** _Annotated below in the onboarding entry — read the +64% EV
through the §15-candidate lens before acting._

---

## 2026-06-10 — Onboarded. Third dry-bulk validator (APPROX-anchored); Week 2 checklist CLOSED

**State at commit:**

- **4 input YAMLs filled** from the Q1 2026 6-K (filed 2026-05-13, accession
  0001171843-26-003334: PR exh_991 + financials/MD&A exh_992) + FY2025 20-F
  (filed 2026-03-30, accession 0001140361-26-011994: per-vessel fleet table).
  Manifest: **29 owned vessels at Mar-31** (6 Cape / 7 Pana-Kamsarmax /
  16 Supra-Ultra; old fleet — class avg ages 14.5 / 14.7 / 13.3). Clara +
  Miracle sold in Q1 (out); Astros (2018 Ultramax) advance-only at Mar-31,
  closed Q2 (out; enters at the Q2 refresh). **The CBI chartered-in trading
  platform (~20 third-party Kamsarmax-focused vessels; trading book majority
  transferred to Cargill) is EXCLUDED from the asset base** — P&L-only
  (charter-hire $46.0M in Q1). BS: cash $258.5M (incl. restricted), debt
  $141.4M (**net cash +$117M ex-margin**), op-lease liab $20.6M, shares
  24,180,472. Cost: opex Cape $7,600 / Pana $6,300 / Supra-Ultra $5,450
  (weighted to disclosed $6,091/d over 2,742 ownership days), G&A $34.4M
  all-in (incl. $21.6M/yr related-party management fees — see §15 flag),
  interest $10.4M gross, tax 0%. Dividend: NONE (build-out phase,
  accumulated deficit) — variable / payout 0.0.
- **Watchlist row (all APPROX):** price $17.25 (stockanalysis.com
  2026-06-10 — Pareto's share-price table does not carry CMDB);
  target = book value/share $27.98; consensus_pnav 0.62 = P/BV proxy
  (defensible because the 2025 spinoff contributed vessels at fair value,
  so book ≈ recent marks); fwd P/E 10.5 (annualised Q1 EPS).
- **Name-sweep:** 1 incidental mention in 280 dailies (CMDB as a
  *charterer* in 2020B/HSHP commentary) — zero coverage, the APPROX
  taxonomy's emptiest case after CCEC (0). `NAME_ALIASES` carries
  CMDB/Costamare-Bulk/CBI (bare "Costamare" deliberately excluded — that's
  CMRE, the containership parent). CMDB added to `APPROX_PNAV_TICKERS` in
  reconcile.py (it was missing → briefly polluted the lock denominator;
  fixed same session).

**Headline FV reading (transaction-anchored marks):**

| Metric | Value |
|---|---:|
| Tool NAV / share | **$32.23** |
| APPROX anchor (book value / share) | **$27.98** |
| Tool / book gap | **+15.8%** (tool ABOVE book) |
| SANITY | n/a (APPROX) — magnitude well inside ±50% |
| Price / tool NAV | **0.54×** |
| Scenario PW FV | **$28.32** |
| EV vs price | **+64.2%** |
| Position | **BUY (undervalued)** — read through the §15 flag below |

**The reading:** our transaction-anchored curves (fit to the hot 2025-26
S&P tape) mark CMDB's 29 old bulkers ~16% ABOVE their spinoff-vintage book
values — directionally sensible (book was struck off an earlier, softer
market). At 0.54× tool NAV / 0.62× book, CMDB is the deepest discount on
the watchlist. The +64% EV is the headline BUT:

**§15 REVIEW CANDIDATE (owner decision pending — haircut NOT applied):**
the discount has the §15 driver fingerprint: (1) related-party
management/agency fees $21.6M/yr to Costamare-affiliated managers on a
$418M mcap; (2) zero dividends + zero buybacks with a net-cash balance
sheet; (3) Konstantakopoulos-family control post-spinoff; (4) persistent
~0.6× P/BV. TEN's analogous case carries a 30% haircut. At 30%, CMDB's
blend-layer FV would compress materially (asset NAV untouched per §15
convention). **Recommendation: owner to size a §15 haircut before
treating the +64% EV as actionable** — until then this is a NAV-discount
observation, not a position signal.

**Known caveats:** (1) §9.11 EPS-xref (+137%) is structurally inflated —
consolidated EPS includes the CBI trading platform our strip doesn't
model; (2) scrubbers: 8 of the owned fleet fitted but unidentified
per-vessel → all marked false, ~$0.55/sh NAV understatement; (3) charter
rates undisclosed (index-linked majority = spot economics; fixed
conversions unknown) → all-spot manifest approximation.

**Prints:** NONE promotable — Clara + Miracle sold for an aggregate $7.7M
GAIN with no per-vessel price disclosure (gains ≠ prices; no split → no
print per the no-back-solve rule); Astros purchase price undisclosed.
Documented here only. Watch the Q2 6-K for the Astros price (would be a
clean 2018-Ultramax age-8 print).

**Week 2 checklist (§11.7.8) — CLOSED with this onboarding:** all three
dry-bulk validators live (SBLK mark-driven −20.8% / GNK validating −4.9% /
CMDB APPROX +15.8% vs book). Calibration lock unchanged at **1/2 (50%)
FAIL-with-explanation** — CMDB correctly excluded from the denominator
(APPROX anchor). Q3 tightening pass is the next sector gate.

**Gate status:** pytest **210 passed** (3 CMDB tests activated).
`reconcile CMDB`: n/a/approx, first-run baseline +15.8% vs book recorded
for drift.

**2026-Q2 refresh items:**
1. Astros enters the fleet (+ price disclosure → print candidate).
2. Dividend initiation watch (net-cash balance sheet; natural catalyst).
3. §15 haircut decision (owner).
4. CBI platform evolution post-Cargill transfer (charter-in book shrinking?).

**Decision:** _CMDB on the watchlist as the 16th name + third dry-bulk
validator; Week 2 dry-bulk onboarding sequence complete. Position signal
BUY (+64.2%) explicitly NOT endorsed pending the §15 sizing decision —
the same NAV-vs-realisation question that produced TEN's 30% haircut._

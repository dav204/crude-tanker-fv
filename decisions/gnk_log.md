# GNK — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.69
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.6%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +3.7pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.69
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.6%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +3.7pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T02:42:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.69
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.6%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +3.7pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T00:38:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.69
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.6%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +3.7pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: -0.11 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T23:54:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.80
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.1%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.1pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-11 — §15.7 retro screen (formalised today): **N/A (gated)** — Pareto P/NAV 0.87×, currently tender-pinned (deal overlay, not governance); widely held, formula dividend. Re-gate after the Diana event resolves.

---

## 2026-06-11T15:40:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.80
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +8.1%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.1pp (k_broker 1.03)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: +0.30 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +1.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-11 — §9.11 EPS-xref anomaly: rate-level explanation REJECTED by the FFA curve

The +149% tool-vs-consensus forward-EPS gap flagged at onboarding had a
standing hypothesis: the synthesised-from-spot dry-bulk strip runs hot.
The first FFA-vs-strip diagnostic (`outputs/ffa_vs_strip.md`, FFA-OCR
Stage 1 curve, 5-day mean Jun-03→Jun-11) rejects that: Bulk Set A PW
mids are within ±5% of the traded forward curve on 8 of 9 legs (Cape
+3.5% avg, Pana −3.0%, Supra-Ultra +2.3%), and the market curve's
backwardation matches the strip's mean-reversion shape.

So the +149% lives in the xref's OTHER legs — candidates, in rough
order of suspicion: (a) consensus_fwd_pe vintage/denominator (Pareto
P/E at the Jun-4 static, NTM window mismatch vs strip quarters);
(b) days/utilization and cost assumptions between rate and EPS;
(c) index-vs-earned premia (GNK's scrubber Capes + Ultramaxes earn
over the 5TC/Smax indices — which would push tool EPS UP, widening
not closing the gap); (d) tender-period consensus staleness.
Investigate at the Q2 refresh alongside the §11.7 Q3 tightening pass —
NOT by touching the validated rate paths.

**Decision:** rate paths stand (market-validated). The xref anomaly is
re-classified from "suspected hot strip" to "xref-construction or
estimate-vintage question," parked for the Q2 refresh.

---

## 2026-06-11T03:20:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $23.50
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +9.5%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +2.9pp (k_broker 1.02)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: -0.50 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.0pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T02:59:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +7.2%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.9pp (k_broker 1.04)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:17:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +7.2%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.9pp (k_broker 1.04)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +7.2%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.9pp (k_broker 1.04)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T18:16:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.28
- Scenario PW FV: $25.73 (EV +7.2%)
- NAV / share: $26.24
- Position: **BUY (undervalued)**
- Broker spread: +4.9pp (k_broker 1.04)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.3% | Δscenario FV: +0.3% | ΔNAV: +0.3% | Δspread: -0.3pp

**Decision:** _Prints pass (4 recovered sentence-splitter misses + Pana
disambiguation — see sblk_log.md same-timestamp entry for detail).
Supra-Ultra fit softens ~1.2pp → GNK NAV +0.3%, gap −4.9%, still inside
the v1 ±10% bar. §6 GNK entry PROMOTED into METHODOLOGY this run.
Deal-lens caveat unchanged (tender deadline Jun-26)._

---

## 2026-06-10T13:25:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.20
- Scenario PW FV: $25.65 (EV +6.9%)
- NAV / share: $26.16
- Position: **BUY (undervalued)**
- Broker spread: +5.2pp (k_broker 1.04)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10 — Pareto free-text retro-sweep (94 mentions, 2025-01 → 2026-06)

The GNK sweep ran DURING onboarding (it's what surfaced Pareto's stated
NAV $27.6, the tender-at-0.9×-NAV line, and the 0.66-0.75× pre-bid P/NAV
regime) — findings already distilled into the onboarding entry below.
Review file archived at `outputs/pareto_mentions_gnk.md`. Additional
color from the full file: the Diana saga timeline runs continuously from
2026-01-16 (Diana nominates six directors to replace the entire board)
through the raised $24.80 tender (May-27) — the board-control fight
predates the tender by months, so a tender lapse does NOT end the event
overhang (proxy outcome from the Jun-18 AGM persists either way).

---

## 2026-06-10T12:59:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $24.00
- Single-point FV: $25.20
- Scenario PW FV: $25.65 (EV +6.9%)
- NAV / share: $26.16
- Position: **BUY (undervalued)**
- Broker spread: +5.2pp (k_broker 1.04)
- Sector: dry_bulk

**Status:** _First snapshot — no prior state to compare._

**Decision:** _Annotated below in the onboarding entry. This is the first-run
baseline at transaction-anchored marks (the pipeline default since the
2026-06-09 Part 4 owner decision)._

---

## 2026-06-09/10 — Onboarded. Second dry-bulk validator; VALIDATES the transaction-anchored curves at −5.2%; v1 lock outcome recorded

**State at commit:**

- **4 input YAMLs filled** from GNK Q1 2026 10-Q (filed 2026-05-06, accession
  0001104659-26-056337). Per-vessel manifest of 44 vessels at the Mar-31
  quarter-end convention (2 Newcastlemax + 17 Capesize → 19 Cape; 15 Ultramax
  + 10 Supramax → 25 Supra-Ultra per §11.7.1 class collapse; **no Pana
  exposure**); includes the held-for-sale Genco Predator (sold Apr 15 for
  $10.6M — excluded from working capital to avoid double-count). BS: cash
  $54.8M, debt $330M face ($680M revolver), op-lease liab $5.6M, NB
  commitments 0 (both Nov-25 nmaxes delivered in March; the Apr-16 $65M
  cape agreement is post-Q — pick up in 2026-Q2), diluted shares
  44,411,222. Cost: opex Cape $8,000 / Supra-Ultra $5,900 per day (weighted
  to disclosed $6,805/d fleet avg), G&A $35.5M (EXCLUDES the $3.8M one-off
  proxy-fight cost), interest $18.0M annualised, tax 0%. Dividend:
  formulaic variable (operating cash flow less voluntary reserve; Q2
  declared $0.35), modeled as variable / payout 1.00 / no floor.
- **Watchlist row**: price $24.00, target $24.80 (Diana live cash tender),
  Pareto P/NAV 0.87, fwd P/E 13.9 (all Pareto Jun-4 2026).

**Headline FV reading (transaction-anchored marks, the pipeline default):**

| Metric | Value |
|---|---:|
| Tool NAV / share | **$26.16** |
| Pareto-implied broker NAV (= $24.00 / 0.87) | **$27.59** |
| Tool / broker gap | **−5.2%** |
| `k_broker` | **1.04** |
| SANITY check (±50%) | ✓ PASS |
| v1 calibration-lock bar (±10%) | ✓ **PASS** |
| Scenario PW FV | **$25.65** |
| EV vs price | **+6.9%** |
| Position recommendation | **BUY (undervalued)** |

**The validation read — why GNK matters beyond itself:** GNK and SBLK run on
the IDENTICAL dry-bulk class curves. GNK reconciles at −5.2% (k 1.04);
SBLK at −21.1% (k 1.27). The curves are therefore NOT systematically
miscalibrated — GNK proves the transaction-anchored Cape/Supra-Ultra marks
recover Pareto's NAV for a no-Pana, Cape-heavy fleet almost exactly. SBLK's
gap is name-specific (likely concentrated in its 46-vessel Pana book — the
thinnest fit at 4 prints — and/or Pareto's richer view of SBLK's specific
mix), confirming the §6 mark-driven classification from the 2026-06-09
SBLK entry rather than indicting the marks layer.

**v1 calibration-lock outcome (§11.7.6, recorded NOT tuned):**

- `reconcile --calibration-lock dry_bulk`: **1/2 within ±10% (50%) — FAIL**
  vs the ≥70% new-sector bar.
- The miss is entirely the documented SBLK mark-driven case (§6 taxonomy,
  k 1.27 surviving transaction anchoring). Per the 2026-06-09 CLAUDE.md
  rule, a lock-test failure surfaces a methodology question — it is NOT a
  license to tune curves toward broker. The methodology answer was already
  given: the transaction-anchored work was done first (47 dry-bulk prints),
  and the gap survived. **Recorded outcome: v1 lock FAIL-with-explanation;
  GNK validates the curve layer; SBLK divergence is the call.** Third
  Pareto-covered bulk name (HSHP) is outside the validator pool per §11.7.3.
- Revisit at the Q3 tightening pass (existing-tier bar ≥80%/±5%) with one
  more quarter of prints — the Pana fit (4 prints, possible duplicate pair)
  is the weakest leg and the most likely SBLK-gap contributor.

**DEAL OVERLAY — read every GNK position signal through the tender:** Diana
Shipping's hostile all-cash tender at $24.80 (raised from $23.50 on May 27;
deadline Jun 26 2026; board rejected; proxy fight at the Jun-18 AGM; SBLK
has a conditional agreement to buy 16 GNK vessels for $470.5M if Diana
succeeds). The market price ($24.00) is pinned to deal odds, NOT to NAV —
the +6.9% EV / BUY reading is really "price ≈ tender, tender ≈ 0.9× Pareto
NAV, tool NAV ≈ Pareto NAV − 5%." If the tender lapses, expect the price to
trade back toward the pre-bid NAV-discount regime (Pareto had GNK at
0.66-0.75× NAV through 2025); if it succeeds at $24.80, the upside is
capped ~3%. The BUY is therefore a deal-arb-flavored reading, not a clean
NAV-discount signal. NO §15 haircut applied — the discount mechanism here
is event risk, not governance/realisation impairment.

**Transaction prints harvested during onboarding (per the 2026-06-09 loop
rule):** 4 new in-window Cape prints + 2 out-of-window Supra prints landed:
2× GNK Newcastlemax 2020-built @ $72.75M (10-Q Note 5), Genco Courageous
2020-built Capesize @ $63.55M (Note 5), Maran 2009-built SWS capesize @
$30M (Pareto Jun-5; 2008 sister documented out-of-window), Picardy +
Predator 2005-built Supramaxes @ $10.6M each (Note 5, age 21,
documentation — validates the old-age leg ~60% above scrap). The Apr-16
Imabari cape print upgraded from broker-report to issuer-confirmed. Cape
fit moved +18.2%/+12.3% → **+16.0%/+12.7%** (n 21→25; the Courageous
standard-cape print tempers the nmax-heavy 5yr cluster). Drift impact on
SBLK: txn NAV $26.19 → $26.17 (−0.1%, under the 2pp gate — no SBLK
annotation required).

**Gate status:** pytest **201 passed** (3 GNK tests activated: schema load,
fleet shape 19/25, sanity band). `reconcile GNK`: SANITY = OK. Baseline
gap **−5.2%** recorded for future drift detection.

**Open items for the 2026-Q2 refresh:**
1. Tender resolution (Jun 26) — price anchor regime changes either way;
   re-read the position signal then.
2. The Apr-16 2026 Capesize ($65M, June delivery) enters the fleet or
   commitments at Q2.
3. If Diana succeeds: SBLK's 16-vessel $470.5M purchase closes — per-vessel
   allocations (if disclosed) are a major Cape/Supra print batch.
4. Pana fit strengthening (the weakest leg; 4 prints with a possible
   duplicate) — most likely SBLK-gap contributor to investigate at Q3.

**Decision:** _GNK on the watchlist as the 15th name + second dry-bulk
validator. Position signal BUY (+6.9%) but READ THROUGH THE DEAL LENS —
price is tender-pinned until Jun-26. The structural takeaway is the
validation: transaction-anchored dry-bulk curves recover Pareto NAV within
5% on a clean no-Pana fleet. v1 lock outcome recorded as 50% FAIL-with-
explanation (SBLK = documented mark-driven miss; no curve tuning)._

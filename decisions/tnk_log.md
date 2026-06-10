# TNK — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $73.92
- Scenario PW FV: $73.70 (EV +4.1%)
- NAV / share: $77.45
- Position: **HOLD (fairly valued)**
- Broker spread: +19.8pp (k_broker 1.34)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T18:16:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $73.92
- Scenario PW FV: $73.70 (EV +4.1%)
- NAV / share: $77.45
- Position: **HOLD (fairly valued)**
- Broker spread: +19.8pp (k_broker 1.34)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T13:25:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $73.92
- Scenario PW FV: $73.70 (EV +4.1%)
- NAV / share: $77.45
- Position: **HOLD (fairly valued)**
- Broker spread: +19.8pp (k_broker 1.34)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.1% | Δscenario FV: -0.1% | ΔNAV: -0.1% | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10 — Pareto free-text retro-sweep (59 mentions, 2025-01 → 2026-06)

Distilled from `outputs/pareto_mentions_tnk.md`.

**Pareto NAV/stance trajectory:** "obscene NAV discount" era ends — re-rated
to 0.93-0.96× by Q1-26. NAV $70 → $72 (2026-01-19, deleveraging means
less NAV-impact, "Q1 cashflow adds $3-4/share") → "20% up would be
~$93/share (up from $83)" (2026-05-04, post-suezmax revisions). Our
watchlist-implied broker NAV $93.16 matches the May-4 upper statement ✓.

**Cross-checks vs our model:** TNK's own H2-25 disposals (4x suezmax +
1x LR2, $158.5M gross; Los Angeles Spirit mid-$30s) are in our transaction
YAMLs — the curve partially reflects TNK's own realized prices, which is
why our txn-anchored BUY→HOLD flip is a marks-vs-momentum statement, not a
fleet-quality disagreement. Net cash ~$1bn YE'25 repeatedly cited; the
earnings/net-cash legs carry whatever bull case remains at these marks.

---

## 2026-06-10T12:59:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $73.96
- Scenario PW FV: $73.74 (EV +4.2%)
- NAV / share: $77.49
- Position: **HOLD (fairly valued)**
- Broker spread: +19.8pp (k_broker 1.34)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:49:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $73.96
- Scenario PW FV: $73.74 (EV +4.2%)
- NAV / share: $77.49
- Position: **HOLD (fairly valued)**
- Broker spread: +19.8pp (k_broker 1.34)
- Sector: crude

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- ⚑ broker spread +7.4pp
- ⚑ NAV/sh -7.0%
- Δprice: no change | Δsingle FV: -6.5% | Δscenario FV: -6.5% | ΔNAV: -7.0% | Δspread: +7.4pp

**Decision:** _METHODOLOGY RE-BASE (txn-anchored marks default-on, owner
decision 2026-06-09) — not a market move. BUY → HOLD is the txn-anchored
reading detailed in the 02:09:54 annotation below; the residual BUY case
rests on net-cash + earnings, not marks. METHODOLOGY Appendix A Part 4._

---

## 2026-06-10T02:09:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $78.90 (EV +11.4%)
- NAV / share: $83.32
- Position: **BUY (undervalued)**
- Broker spread: +12.4pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _2026-06-09 Pareto S&P sweep: Aframax 10yr −10.4% and
Suezmax −6.6%/−12.9% recalibrations hit TNK's Atlantic-skewed mid-age
fleet. Txn-anchored reading NAV $77.49 / EV +4.1%, a **BUY → HOLD flip**
(the +11.4% baseline EV was roughly half a marks story). TNK's own
disposals are IN the new sample (4x suezmax + 1x LR2 H2'25 disposals,
$158.5M gross; Los Angeles Spirit mid-$30s) so the curve now partially
reflects TNK's own realised prices — the BUY thesis must rest on the
net-cash + earnings legs, not marks. §6 both-mark-and-weight-driven
classification stands. Duplicate 02:09:49 entry below covered by this
annotation._

---

## 2026-06-10T02:09:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $78.90 (EV +11.4%)
- NAV / share: $83.32
- Position: **BUY (undervalued)**
- Broker spread: +12.4pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T01:33:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $78.90 (EV +11.4%)
- NAV / share: $83.32
- Position: **BUY (undervalued)**
- Broker spread: +12.4pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T23:27:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $78.90 (EV +11.4%)
- NAV / share: $83.32
- Position: **BUY (undervalued)**
- Broker spread: +12.4pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T19:14:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $78.90 (EV +11.4%)
- NAV / share: $83.32
- Position: **BUY (undervalued)**
- Broker spread: +12.4pp (k_broker 1.19)
- Sector: crude

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → BUY (undervalued)
- ⚑ scenario PW FV +13.8%
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +13.8% | ΔNAV: no change | Δspread: +2.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-09T15:13:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -2.1%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +10.1pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-07T15:11:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.80
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -2.1%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +10.1pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.30 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:24:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:10:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:08:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:03:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-03T21:01:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T21:03:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:33:10+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:28:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:22:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $70.50
- Single-point FV: $79.13
- Scenario PW FV: $69.31 (EV -1.7%)
- NAV / share: $83.32
- Position: **HOLD (fairly valued)**
- Broker spread: +9.7pp (k_broker 1.18)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---


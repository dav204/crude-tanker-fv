# TEN (Tsakos Energy Navigation) — decision log

## 2026-06-11 — §15 haircut recalibration review (§15.7 retro screen): HOLD at 30%

First formal recalibration since the haircut was set at onboarding
(2026-06-06). The calibration triangle today (per §15.7 Step 2):

- **Owner haircut: 30%.**
- **VIE-implied: 36.3%** (1 − 51.50/80.79). NOTE the drift: at
  onboarding this read ~42% against the pre-recalibration NAV $88.56;
  the txn-anchored re-base LOWERED our NAV, narrowing the VIE-implied
  discount toward our 30%. The two anchors are converging, not
  diverging.
- **Market: ~53%** (price $37.99 / NAV $80.79 = 0.47× — squarely inside
  TEN's decades-long 0.4-0.5× band). Floor-side reference only, never
  the calibration (§15.7: haircutting to market deletes the signal).

**Directional evidence since onboarding:** payout RAISED — $1.50/sh
2026 aggregate, "highest in 10+ years," declared and paid on schedule
(~19% of EPS, yield ~4% at spot). The realisation channel is opening,
which argues against moving UP toward the VIE anchor. Nothing on the
other side: no new related-party expansion observed (TCM fee-load
anchor NOT yet computed — pull the TCM fees from the 20-F related-party
note at the Q2 refresh and add the capitalized-fee-drag number per
§15.7; CMDB now has one and TEN should too).

**Decision: HOLD 30%, working band 30-36%.** Sensitivity: at 36% the
PW FV falls roughly $3-4 (≈ $54 vs $57.61) — BUY intact at ~+42%; the
call only flips near the market-implied ~50%+. Signal not
haircut-sensitive inside the band.

**Reopen triggers:** next dividend action in either direction (a second
consecutive raise → consider 25%; a cut → move to the VIE anchor 36%),
preferred refinancing/redemption activity, any VIE stance change, the
20-F fee-load computation landing outside ~1%/yr of GAV.

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $50.92 (EV +44.0%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +22.8pp (k_broker 1.12)
- Sector: crude

**Material deltas since last run:**
- ⚑ scenario PW FV -20.9%
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -20.9% | ΔNAV: no change | Δspread: -4.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $64.35 (EV +81.9%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.2pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $64.35 (EV +81.9%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.2pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -1.7% | ΔNAV: no change | Δspread: -0.4pp

**Decision (2026-07-02, review C-3 — multi-sleeve aggregation fix):** ACCEPT the −3.2pp EV /
−1.7% scenario-FV correction (PW FV $65.49→$64.35, BUY intact at +81.9%). Bug fix, not a market
or weight move: the 3-sleeve aggregator applied the CRUDE sleeve's probability weights to TEN's
product and LNG sleeves; fixed to per-sleeve sector weights (cross-sector independence,
`pipeline._aggregate_multi_sleeve_report`, regression-tested). ΔNAV 0.0% — scenario-layer only.
See `decisions/crude_reweight_proposal_2026-07-02.md` §14 + the 2026-07-02 review addendum. The
pending post-stand-down vintage takes TEN to ~+44% (still BUY, §15 haircut applies downstream).
No trade.

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.37
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +85.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +27.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.39 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -1.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $35.76
- Single-point FV: $61.29
- Scenario PW FV: $65.49 (EV +83.2%)
- NAV / share: $88.70
- Position: **BUY (undervalued)**
- Broker spread: +29.3pp (k_broker 1.13)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -7.2pp
- Δprice: -0.96 | Δsingle FV: +1.6% | Δscenario FV: +1.5% | ΔNAV: +2.0% | Δspread: -7.2pp

**Decision:** Amendment B — crude age-0 reverted to xclusiv Resale; TEN NAV +2.0% on its young Suezmax/Aframax/LR2 lift (xclusiv Resale > old). Dry-bulk/other sleeves unchanged.

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.34
- Scenario PW FV: $64.54 (EV +75.8%)
- NAV / share: $86.95
- Position: **BUY (undervalued)**
- Broker spread: +36.5pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.7% | Δscenario FV: -0.6% | ΔNAV: -0.9% | Δspread: +1.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.72
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +76.8%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +35.2pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.96 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.9pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.68
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +72.3%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +39.1pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.61 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +69.6%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +41.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $60.74
- Scenario PW FV: $64.93 (EV +69.6%)
- NAV / share: $87.70
- Position: **BUY (undervalued)**
- Broker spread: +41.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: +0.1% | ΔNAV: +0.2% | Δspread: -0.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $60.66
- Scenario PW FV: $64.84 (EV +69.3%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +41.7pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $60.66
- Scenario PW FV: $64.84 (EV +69.3%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +41.7pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +5.1% | Δscenario FV: +4.2% | ΔNAV: no change | Δspread: -0.8pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $57.74
- Scenario PW FV: $62.23 (EV +62.5%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +42.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $57.74
- Scenario PW FV: $62.23 (EV +62.5%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +42.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $57.74
- Scenario PW FV: $62.23 (EV +62.5%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +42.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $38.29
- Single-point FV: $57.74
- Scenario PW FV: $62.23 (EV +62.5%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +42.5pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T21:55:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $57.74
- Scenario PW FV: $62.23 (EV +67.7%)
- NAV / share: $87.56
- Position: **BUY (undervalued)**
- Broker spread: +37.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.6% | Δscenario FV: -0.5% | ΔNAV: -0.6% | Δspread: +1.0pp

**Decision:** _[pending annotation]_

---

## 2026-06-12T18:49:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T14:28:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T02:42:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T00:38:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.11
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +68.6%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.16)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -16.0pp
- ⚑ NAV/sh +9.1%
- Δprice: -0.88 | Δsingle FV: +8.9% | Δscenario FV: +8.6% | ΔNAV: +9.1% | Δspread: -16.0pp

**Decision:** Local-state resync at Week 4 open — this machine's gitignored
pipeline state predated the merged June-5 data-kit fix (PR #1), so the drift
re-detected here is the same manifest-omission correction already annotated
in the 2026-06-11 entries below (plus a −$0.88 live close). No new decision.

---

## 2026-06-11T23:54:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.99
- Single-point FV: $58.09
- Scenario PW FV: $62.56 (EV +64.7%)
- NAV / share: $88.13
- Position: **BUY (undervalued)**
- Broker spread: +40.3pp (k_broker 1.18)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -12.4pp
- ⚑ NAV/sh +9.1%
- Δprice: no change | Δsingle FV: +8.9% | Δscenario FV: +8.6% | ΔNAV: +9.1% | Δspread: -12.4pp

**Decision:** Drift is the fleet-manifest omission fix from the June-5 data
kit reconcile (entry below) — data correction, not a market move. Position
unchanged (BUY); gap to APPROX broker NAV tightened −26.0% → −19.3%.

---

## 2026-06-11 — June-5 Data Kit reconciled against project state. ONE input bug found + fixed; Q2-vintage deltas documented for the Q2 refresh.

Source: TEN Data Kit (June 5, 2026) — user-supplied PDF (tenn.gr blocks
agent fetching: the WAF 403s the fetch service and the sandbox egress
allowlist blocks curl). 63 in-water vessels, 7,701,519 DWT + 19 NB =
82 vessels, 10,658,624 DWT.

### Bug found and FIXED (Q1-vintage — belongs in the Mar-31 snapshot)

**Dr Irene Tsakos (Jun-25, 156,838 DWT) and Silia T (Oct-25, 156,838 DWT)
were missing from the fleet manifest.** Both are 2025-delivered conventional
Suezmaxes, in-water well before Mar-31 (6-K confirms 64.0 end-of-quarter
vessels). Root cause: the 2026-06-05 onboarding build plan wrote "14
conventional Suezmax" — an arithmetic slip against the same entry's own
data-kit table (Suezmax 20 − 4 off-curve shuttles = 16); the manifest was
built to plan. The slip was probably seeded by the May-kit note calling
Dr Irene Tsakos a "shuttle-rate vessel" — but the Q1 PR NB-table analysis
(2026-06-06 entry) is explicit that the DP2 set is Brasil 2014 + Rio 2016 +
Athens 04 + Paris 24 only; Dr Irene Tsakos's $33,000-min + 50-50 p/s
structure is a conventional Suezmax TC (cf. Popi Sazaklis). The manifest's
own `fleet_summary` claimed 60 on-curve while only 58 vessels were listed —
internally inconsistent, now reconciled (16 conv. Suezmax, crude sleeve 41,
on-curve 60 + 4 shuttle = 64 ✓).

Fix: added both vessels (TC $33,000 / $43,750, active at Mar-31), Suezmax
spot coverage 0.143 → 0.125 (2 of 16), cosmetic dwt alignments to the
June-5 kit table (Decathlon 158,475; Marathon TS 113,651; Aspen/Alpes;
Handies 39,589 — dwt is schema-only, not in valuation math).

Impact (txn-anchored): NAV/sh $80.79 → $88.13 (+9.1%); un-anchored asset
NAV $88.56 → $95.95; scenario PW FV +8.6% to $62.56; EV +51.7% → +64.7%
at $37.99. Tool↔broker gap −26.0% → −19.3% (APPROX anchor). Drift gate:
>2pp move, cause = data omission fix (this entry). 243 tests green;
reconcile SANITY n/a-APPROX as expected.

### Vintage deltas (June-5 kit vs our Mar-31 snapshot) — DOCUMENTED, not applied

All are Q2 events; the Q1 manifest/balance sheet correctly reflects Mar-31.
Apply at the Q2-2026 refresh (TEN reports H1 in SEPTEMBER):

1. **Ulysses gone from the kit** — VLCC count 3 → 2. Confirms the 20-May
   sale ("$83M free cash after debt repayment", already in this log +
   data_sources). **No gross price disclosed → NOT promotable** to
   transactions/vlcc.yaml (no-back-solve rule). Watch the Q2 6-K for the
   gross figure — a 2016-built VLCC print would be valuable.
2. **Sola TS** stepped up $25,651 → $26,651 (2-yr period agreed from
   May-1-2026, +1 optional yr at $27,654).
3. **Dimitris P** spot → TC, $40,000 min + 50-50 p/s capped $105,000,
   expiry min Oct-27 / max Dec-27. Meaningful coverage add on a 2011 vessel.
4. **Alaska + Archangel** rolled from fixed TCs ($50,000 / $102,000) to
   spot-indexed TCs ("Time-Charter Spot Market rate") — the Q1 rates were
   Hormuz-era; effective spot exposure on the 1A ice cohort rises in Q2.
   (Archangel notes still carry $110,000 East / $95,000 West redelivery.)
5. **Hercules I** still at $140,000 "until the situation in the Straits of
   Hormuz is resolved" — unchanged, expiry Nov-26.

### Confirmations (no action)

- **NB program identical to May kit:** 19 vessels, $2,403M contracts
  (Anfield $149.1M Q3-26; HN2733-41 $148.1M each, Q3-27→Q4-28; 5 LR1
  $56-56.6M, Q2-27→Q3-28; 3 VLCC $128.5M each 320k DWT, Q3-27→Q2-28;
  HN3643 LNG $254.4M Q3-28). Equity contribution $232.3M (unchanged);
  Anfield debt $111.8M agreed / $44.7M drawn; nine-shuttle facility $1.1B
  agreed / $148.12M drawn (all unchanged vs May/April kits).
- **Paid-to-date $430.5M at Jun-5 (contract basis).** FLAG for owner at Q2:
  our `newbuild_advances_paid` $400M is a documented Mar-31 estimate; the
  6-K BS line was $442.7M (incl. extras/capitalised interest) and the
  onboarding build plan had specified that figure. Worth deciding which
  basis the convention wants — ~$42.7M ≈ $1.4/sh on 30.1M shares.
- **FLOPEC 49% JV also flagged on Selini + Salamina** (not just the two
  Handies). Counted at full per the data-kit convention, consistent with
  current treatment; noted for completeness.
- Shuttle book anchors unchanged: Brasil 2014 $58,908 → Nov-28, Rio 2016
  $58,403 → Oct-28 (+$200/day annual adjustments to 2028), Athens 04 /
  Paris 24 $58,569 → 2032 (Paris 24 +$2,750/day Brazilian trade costs).
  `shuttle_contracted_book` $453.1M stands.

---

## 2026-06-10 — PRICE INPUT ERROR corrected: $44.00 → $37.14 (−16%)

Caught by the first `/news-pull` digest (2026-06-10), verified
independently against Yahoo (NYSE close $37.14, prior close $36.92) and
stockanalysis.com/stockinvest.us ($36.16–$37.54 range Jun-5→Jun-10).

**What went wrong:** the 2026-06-05 watchlist entry read the Q1 6-K
prose "~$44" as a live Jun-5 price. It wasn't — it was a stale/loose
reference in the filing text; the market was at ~$37 all week. Every TEN
signal between 06-05 and 06-10 was computed against a denominator ~16%
too high. Classic absence-of-verification miss: a price typed from
filing prose, never checked against a quote source.

**Fix applied (watchlist.yaml):**
- `current_price` 44.00 → 37.14 (`as_of` → 2026-06-10).
- `consensus_pnav` 0.40 → 0.34 — REBASED to preserve the implied broker
  NAV anchor (~$110, VIE-stale): broker_nav = price/pnav in reconcile,
  so leaving pnav at 0.40 would have silently moved the broker NAV to
  $92.85 on a price fix. Anchor preservation confirmed by reconcile:
  broker NAV $109.24, NAV-gap drift +0.5pp (stable).
- `consensus_fwd_pe` 5.5 → 4.6 (price-derived APPROX field, same error).

**Signal impact (pipeline 2026-06-11T02:59Z delta):** PW FV $57.61
unchanged (price doesn't enter the valuation), EV +55.1% at $37.14 vs
+30.9% at the erroneous $44; position BUY unchanged; broker spread
+6.6pp (material flag — this entry is the drift-gate annotation; cause
is the input fix, not a market move or methodology change). The BUY call
survives the correction and strengthens; the VIE Bullish $51.50
cross-check now reads as +39% upside from spot instead of +17%.

**Process fix:** daily automated price refresh being built same session
(prices land in an automation-writable `prices_daily.yaml`, loader
prefers them over watchlist statics) — no watchlist price should ever
again be hand-typed from filing prose.

## 2026-06-10 — Pareto free-text retro-sweep (5 mentions, 2025-01 → 2026-06)

Distilled from `outputs/pareto_mentions_ten.md`. **Only 5 mentions —
confirms the APPROX/no-Pareto-coverage status** (VIE remains TEN's only
external anchor).

The sweep PAID here despite the low count: the 2025-03-14 line ("Chinese
buyers... bought a Tsakos suezmax built 2009 for ~$40m, our value ~$35m")
is a disclosed TEN disposal the original class-keyword scan missed —
**promoted to suezmax.yaml** (age-16 in-window print; Suezmax fit moved
−6.6%→−6.2% at 5yr / −12.9%→−13.1% at 10yr — under the 2pp drift gate for
all holders). Also confirmed: TEN's 2x (+1 option) VLCC order at Hanwha,
$123-128.5M, 2027 delivery (Jun/Jul-25) — inside the $2.4B orderbook
documented at onboarding; conventionally fuelled, so an age-(-1) NB
reference consistent with our $130M-area VLCC NB market read.

---

## 2026-06-11T15:40:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.99
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +51.6%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +52.7pp (k_broker 1.25)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.85 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +3.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T03:20:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.14
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +55.1%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +49.5pp (k_broker 1.23)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-11T02:59:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $37.14
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +55.1%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +49.5pp (k_broker 1.23)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +6.6pp
- Δprice: -6.86 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +6.6pp

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:17:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +42.9pp (k_broker 1.24)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +42.9pp (k_broker 1.24)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T18:16:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +42.9pp (k_broker 1.24)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T13:25:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.32
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.79
- Position: **BUY (undervalued)**
- Broker spread: +42.9pp (k_broker 1.24)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-06 — Onboarded. §15 governance haircut at 30%. First reconcile baseline.

**Decision:** TEN is **on the watchlist** as the 13th name + first 3-sleeve hybrid +
first §15 case. The full architectural + data-assembly path closed in one session
after the unblock. Recording the build choices + reconcile baseline for the next
quarter's drift comparison.

### §15 governance / value-trap haircut — 30%

Per user analysis (TEN's persistent market discount-to-NAV is driven by management
concerns + low common return policy + related-party transactions + preferred
structure misalignment), set `governance_discount_pct: 0.30` on the TEN balance
sheet. Drivers explicitly named:

1. **Controlled-shareholder structure** — Tsakos family control, no hostile takeover
   premium, capital allocation discretion concentrated in management whose
   interests are not 1:1 with common.
2. **Related-party transactions** — management fees to Tsakos Columbia
   Shipmanagement (TCM, family-controlled service entity); historical pattern of
   related counterparties on charters and yard sourcing.
3. **Low common payout** — $1.50/share aggregate 2026 dividend vs ~$8 EPS = ~19%
   payout. "Highest dividend in 10+ years" per the Q1 6-K, but still well below
   peer payout norms (DHT/NAT ~100%; FRO 80%; STNG buyback-heavy).
4. **No buyback program** — retained capital channelled into the $2.4B newbuild
   orderbook; market is implicitly being told "we will reinvest, not return."
5. **Preferred-share structure** — Series E ($118.6M @ 9.25%) + Series F ($168.7M
   @ 9.50%) with Tsakos-affiliated entities holding meaningful slugs (0.95% E +
   1.5% F per 20-F). Preferred dividends mandatory while common is discretionary.

**Calibration logic** (METHODOLOGY §15.4 calibration table):
- VIE Bullish target $51.50 implies VIE itself applies ~47% discount vs
  unconstrained NAV ($51.50 / $98 stale = 0.53).
- 30% sits between full-realisation (0%) and VIE Bullish (47%), leaving room for
  partial governance improvement vs full continuation of the historical discount.
- Result: tool PW FV $49.37 lands within **$2.13 of VIE Bullish $51.50** —
  independent external confirmation that the anchor is ~$50, not ~$68.

**Applied at:** blend layer (NAV term) + dividend strip terminal. NOT applied
to `compute_nav` or to the broker-NAV sweep / `k_broker` — those answer the
asset-side question, which is independent of governance realisation.

### First-reconcile baseline (2026-06-06)

| Metric | Value | Read |
|---|---:|---|
| Tool asset NAV/sh (undiscounted) | $88.56 | The asset-side answer |
| Broker NAV/sh (consensus_pnav 0.40 APPROX) | $110.00 | Higher; market agrees on the assets |
| Tool↔broker gap | **−19.5%** | Within ±50% sanity bar |
| SANITY | n/a (APPROX consensus_pnav) | Same convention as NAT / CCEC / ASC |
| DRIFT | first-run | Baseline for next quarter's comparison |
| Effective NAV (post-§15 30% haircut) | $61.99 | The realisation-side answer |
| Scenario PW FV (post-haircut) | **$49.37** | Position: BUY (EV +12.2%) |
| VIE Bullish target | $51.50 | Independent external anchor; tool within $2 |

### Build-time inputs (refresh checklist for next quarter)

All inputs sourced from Q1 2026 6-K (filed 2026-05-22) + 2025 20-F (filed
2026-04-06) + TEN Data Kit (May 11, 2026):

- `cash_and_equivalents`: $321,416K (6-K explicit Mar 31)
- `working_capital_net`: $28,000K (rolled forward from 20-F Dec 2025 $28,157K)
- `total_debt`: $2,148,200K (data kit narrated Mar 31 estimate)
- `lease_liabilities`: 0 (op leases offset by RoU asset; Tenergy SL is financing
  arrangement in total_debt)
- `newbuild_capex_commitments`: 0 (delivered = contract convention per §3.1 +
  §11.6 read; netted against advances)
- `newbuild_advances_paid`: $400,000K (estimate between 20-F Dec $301.9M and data
  kit May $430M; refresh on next 6-K)
- `diluted_shares_outstanding`: 30,127,603 (20-F Dec 2025; no Q1 buyback)
- `preferred_equity`: $287,328K (Series E 4,745,947 × $25 + Series F 6,747,147 × $25)
- `shuttle_contracted_book`: $453,100K (per-vessel NPV at WACC 11%, utilization
  98.3%, opex $11k/d, residual = Suezmax curve at expiry age — see ten_log.md
  earlier entries for the per-vessel breakdown)
- `governance_discount_pct`: 0.30 (this entry)

### APPROX flags + refresh-when-resolved items

1. **Brasil 2014 / Rio 2016 extension rate $60k/day** — APPROX of 6-K Apr-23
   subsequent event "increased rate" disclosure. Material upside if actual rate
   is materially higher (gross revenue $200M+ over 2 vessels × 5 years implies
   ~$55k base; "increased" relative to current $58k could be 65k+).
2. **NB advances $400M** — interpolated between 20-F and data kit; refresh from
   next 6-K balance sheet.
3. **TEN `consensus_pnav: 0.40`** — APPROX; VIE-stale anchor. No Pareto coverage
   for TEN. Refresh if VIE Coverage Universe updates or a sell-side broker
   begins publishing P/NAV.
4. **Cost structure per-class opex** — derived from 6-K fleet-average $9,952/d;
   no per-class disclosure available. Refresh if TEN publishes per-class.

### Drift watchlist for next quarter

The reconcile compares against this baseline. Trigger an entry in this log if any
of the following move >2pp:
- Tool↔broker gap (currently −19.5%)
- Headline position (currently BUY +12%)
- Asset NAV/sh
- Effective NAV/sh

Or any of:
- TEN's `governance_discount_pct` is reconsidered (governance signal change)
- Shuttle extension rate disclosed (changes shuttle_contracted_book)
- NB delivery (shifts fleet manifest + reduces advances/commitments)
- Material dividend / buyback policy change

---

## 2026-06-10T12:59:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.31
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.78
- Position: **BUY (undervalued)**
- Broker spread: +43.0pp (k_broker 1.24)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:49:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $53.31
- Scenario PW FV: $57.61 (EV +30.9%)
- NAV / share: $80.78
- Position: **BUY (undervalued)**
- Broker spread: +43.0pp (k_broker 1.24)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +11.4pp
- ⚑ NAV/sh -8.8%
- Δprice: no change | Δsingle FV: -8.7% | Δscenario FV: -8.2% | ΔNAV: -8.8% | Δspread: +11.4pp

**Decision:** _METHODOLOGY RE-BASE (txn-anchored marks default-on, owner
decision 2026-06-09) — not a market move. Still solidly BUY (EV +30.9%);
the §15 30% governance haircut already absorbs far more than this marks
delta (see 02:09:54 annotation below). METHODOLOGY Appendix A Part 4._

---

## 2026-06-10T02:09:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $62.79 (EV +42.7%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +31.6pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _2026-06-09 Pareto S&P sweep: Suezmax/Aframax/LR2/MR
recalibrations hit TEN's 3-sleeve book. Txn-anchored asset NAV $80.78 /
EV +30.9% (from $88.56 / +42.7%) — still solidly **BUY** at both mark
sets even before considering that the §15 30% governance haircut already
absorbs far more than this marks delta. The BUY call is robust to the
marks question. Duplicate 02:09:49 entry below covered by this
annotation._

---

## 2026-06-10T02:09:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $62.79 (EV +42.7%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +31.6pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T01:33:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $62.79 (EV +42.7%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +31.6pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T23:27:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $62.79 (EV +42.7%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +31.6pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T19:14:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $62.79 (EV +42.7%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +31.6pp (k_broker 1.17)
- Sector: crude

**Material deltas since last run:**
- ⚑ scenario PW FV +27.2%
- ⚑ broker spread +5.2pp
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +27.2% | ΔNAV: no change | Δspread: +5.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-09T15:13:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $49.37 (EV +12.2%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +26.4pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-05 evening — Architecture unblocked. Only data-assembly remains.

**Decision:** TEN's methodology blockers are now closed. The remaining work
is data assembly — per-vessel shuttle NPV math, 4 YAMLs, watchlist entry,
integration test, §6 entry. **Still not actually onboarded** (no
`inputs/fleet_manifests/ten.yaml` yet), but the next session can build
TEN end-to-end without further architectural decisions.

### What landed today (2026-06-05 PM)

- **METHODOLOGY §11.6**: off-curve-at-contracted-book convention for DP2
  shuttle sleeves. In-water = NPV of contracted day rates + Suezmax residual
  at TC expiry. NBs = delivered-at-contract-price (no §3.1 hot-market markup).
- **Schema**: `shuttle_contracted_book` line added to `BalanceSheet`
  (adds to NAV like working capital; defaults to 0; pro-rates by sleeve in
  hybrid carve-outs).
- **carveout.py**: `lng_carve_out()` function added; all three sleeve
  functions now share a `sleeve_values()` denominator (crude + product + lng)
  so 3-sleeve shares sum to 1.0. INSW behaviour preserved (LNG share = 0).
- **pipeline.py**: `_aggregate_three_sleeve_report` + `THREE_SLEEVE_TICKERS`
  dispatch added. Aggregator pairs scenarios by index across the three
  sectors (same convention as the 2-sleeve `_aggregate_hybrid_report`).
- **Tests**: 4 new tests covering 3-sleeve share summation, corporate-stack
  aggregation, fleet-split cleanliness, and the per-scenario aggregator.
  Total now **174 passing**.

### Revisit-criteria status (final)

1. ~~DP2 shuttle handling decision~~ **DONE 2026-06-05 PM** — off-curve-at-
   contracted-book convention; the cheap path is now production-ready.
2. ~~`preferred_equity` schema line~~ **DONE 2026-06-05.**
3. ~~Fetch Q1 2026 6-K~~ **DONE 2026-06-05 PM.**
4. ~~3-or-4 sleeve carve-out extension~~ **DONE 2026-06-05 PM** — 3-sleeve
   (`crude_carve_out` + `product_carve_out` + `lng_carve_out`) ships with
   `_aggregate_three_sleeve_report`. Shuttle handled via
   `shuttle_contracted_book` at the corporate level (no 4th sleeve needed).
5. **Standard onboarding** (the actual TEN build) — *pending*:
   - Compute per-vessel shuttle NPV using §11.6 formula + 6-K + data kit
     anchors. Inputs:
     - Brasil 2014: $58,908/d, escalating, expires Nov-2028 (originally
       Oct-2028 per data kit; extension agreed Q2-2026 for further 5 years
       at higher rate starting H2-2028 with > $200M cumulative gross revenue)
     - Rio 2016: $58,403/d, escalating, expires Oct-2028 (same extension)
     - Athens 04: $58,569/d through 2032
     - Paris 24: $58,569/d through 2032 (+$2,750/d Brazilian trade costs)
     - WACC: 11%, utilization: 98.3% (6-K), offhire: 1%
     - Residual at expiry: Suezmax-curve value at age-at-expiry (~age 20-23)
   - Build `inputs/fleet_manifests/ten.yaml`:
     - Crude sleeve: 3 VLCC + 14 conventional Suezmax + 22 Aframax
     - Product sleeve: 4 Aframax LR + 9 Panamax LR1 + 2 MR + 2 Handysize
     - LNG sleeve: Tenergy + Maria Energy
     - Shuttle sleeve EXCLUDED from fleet manifest (handled via
       `shuttle_contracted_book` line; 4 in-water vessels)
     - NBs (8 conventional + 10 shuttle + 1 LNG + 1 optional LNG via
       `newbuild_capex_commitments` and `newbuild_advances_paid`)
   - Build `inputs/balance_sheets/ten_2026-Q1.yaml`:
     - cash_and_equivalents: $321,416K
     - working_capital_net: $174,654K (Other assets − Other liabilities)
     - total_debt: $2,136,109K
     - lease_liabilities: parse from 6-K footnotes / 20-F
     - newbuild_capex_commitments: ~$1,960M (data kit $2,403M − advances $442.7M)
     - newbuild_advances_paid: $442,740K
     - diluted_shares_outstanding: 29,971,603
     - preferred_equity: ~$285,000K
     - shuttle_contracted_book: per-vessel NPV sum (to be computed)
   - Build `inputs/cost_structures/ten.yaml`:
     - opex_per_day per class
     - annual_G_and_A: ~$50M
     - annual_interest_expense: ~$83M
     - effective_tax_rate: **0%** (no corporation tax per Ex 99.1)
   - Build `inputs/dividend_policies/ten.yaml`:
     - policy_type: base_plus_variable (semi-annual)
     - 2026 aggregate $1.50/share
   - Add TEN to watchlist.yaml (sector: crude default; ticker added to
     `THREE_SLEEVE_TICKERS`)
   - Integration test: TEN NAV reconciles within band; scenario aggregator
     produces a sensible headline FV
   - METHODOLOGY §6 TEN entry documenting the build choices

### What I want to do NEXT session

If the user is up for it, the actual TEN build follows. Estimated 4-6 hours
of focused work. Output: TEN on the watchlist, scenario report, fair-value
diagnostic, §6 entry.

---

## 2026-06-07T15:11:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $44.00
- Single-point FV: $58.42
- Scenario PW FV: $49.37 (EV +12.2%)
- NAV / share: $88.56
- Position: **BUY (undervalued)**
- Broker spread: +26.4pp (k_broker 1.17)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---

## 2026-06-05 PM — Q1 2026 6-K pulled. Build is now fully data-unblocked.

**Decision:** **Still deferred** on the methodology side (DP2 Shuttle class
remains the binding architectural blocker). **Data side is now closed** —
SEC EDGAR Q1 2026 6-K Exhibit 99.1 (filed 2026-05-22, accession
0001193125-26-236934) provides every balance-sheet, income-statement, and
share-count line the schema needs.
[6-K filing index](https://www.sec.gov/Archives/edgar/data/1166663/000119312526236934/0001193125-26-236934-index.html)
· [Ex 99.1 press release](https://www.sec.gov/Archives/edgar/data/1166663/000119312526236934/d143886dex991.htm)

### Q1 2026 income statement (USD thousands, unaudited)

| Line | Q1 2026 | Q1 2025 |
|---|--:|--:|
| Voyage revenues | 252,963 | 197,051 |
| Voyage expenses | (29,847) | (36,063) |
| Charter hire expense (op-lease bareboats) | (3,386) | (3,282) |
| Vessel operating expenses | (53,264) | (49,606) |
| Depreciation and amortization | (44,147) | (41,131) |
| General and administrative expenses | (12,443) | (9,906) |
| Gain on vessel sales | 0 | 3,553 |
| **Operating income** | **109,876** | **60,616** |
| Interest and finance costs, net | (20,788) | (24,002) |
| Interest income | 2,201 | 2,307 |
| Other, net | (21) | (19) |
| **Net income** | **91,268** | **38,902** |
| Noncontrolling interest (FLOPEC JV) | (2,425) | (1,191) |
| NI to TEN | 88,843 | 37,711 |
| Preferred dividends | (6,750) | (6,750) |
| Restricted-stock allocation | (422) | (201) |
| **NI to common** | **81,671** | **30,760** |
| **EPS (basic = diluted)** | **$2.72** | **$1.04** |
| Weighted avg diluted shares | 29,971,603 | 29,661,103 |

**Tax: 0%.** "The Company does not incur corporation tax" (Ex 99.1 footnote).
For our schema this overrides the default 2% tonnage-tax assumption.

### Q1 2026 balance sheet (USD thousands, 31-Mar-2026)

| Line | 31-Mar-2026 | 31-Dec-2025 |
|---|--:|--:|
| Cash | **321,416** | 298,129 |
| Other assets (AR + inventory + ROU + prepaid + restricted) | 331,398 | 197,009 |
| Vessels, net | 3,145,164 | 3,156,075 |
| Advances for vessels under construction | 442,740 | 301,868 |
| **Total assets** | **4,240,718** | 3,953,081 |
| Debt and other financial liabilities (net of deferred finance costs) | **2,136,109** | 1,920,975 |
| Other liabilities (op-lease + accrued + deferred) | 156,744 | 169,101 |
| Stockholders' equity | 1,947,865 | 1,863,005 |

**Reconciliations vs data-kit (data kit p.3):**
- Data kit said "expected total debt at 31-Mar-2026: $2,148.2M". Actual = $2,136.1M ($12M lower; difference is deferred finance cost amortization).
- Data kit said "equity contribution for 19 NBs: $232.3M" as of May 11; 6-K shows advances for vessels under construction at $442.7M (the data kit's $232M is the *equity portion*; the $442.7M is equity + drawn debt + accrued instalments).

### Cash flow Q1 2026 (USD thousands)

| | Q1 2026 | Q1 2025 |
|---|--:|--:|
| Net cash from operating | 97,181 | 52,150 |
| Net cash used in investing | (252,075) | (2,645) |
| Net cash from financing | 178,181 | (48,239) |

### Preferred equity — share counts inferred

Q1 preferred dividends $6,750K = $27,000K annualised. With known coupons:
- **Series E:** 9.25% × $25 par = $2.3125/sh/yr
- **Series F:** 9.50% × $25 par = $2.3750/sh/yr

Tsakos-affiliated holdings (from 2025 6-K via StockTitan): 45,000 Series E
shares = 0.95% of outstanding → **Series E ≈ 4.74M shares = $118M liquidation
preference**. 100,000 Series F shares = 1.5% of outstanding → **Series F ≈
6.67M shares = $167M liquidation preference**. **Aggregate ≈ $285M** —
matches the stale-VIE ~$287M estimate within rounding.

Implied annual preferred dividend cost: 4.74M × $2.3125 + 6.67M × $2.3750
= $10.96M + $15.84M = **$26.8M ≈ $27.0M actual** ✓ — share counts validate
by reproducing the disclosed dividend stream within $200K.

### Fleet Q1 2026

- End-of-quarter vessels: **64.0** (avg 63.4 during period)
- Total DWT: **8,003K** (matches data kit 8,001,513 within rounding)
- Average age: **10.3 years**
- Utilization: **98.3%**
- **TCE per ship per day: $40,960** (vs Q1 2025 $30,741; +33%)
- Opex per ship per day: $9,952; vessel overhead per ship per day: $2,180

Employment day mix:
| Bucket | Days | Share |
|---|--:|--:|
| Time charter — fixed rate | 3,808 | 67.9% |
| Time charter / pool — variable rate | 1,288 | 23.0% |
| Spot voyage at market rates | 513 | 9.1% |
| **Total operating days** | **5,609** | 100% |

**Implication for the dividend strip:** 90.9% of operating days are on time
charter or pool — `spot_coverage_pct` should be ~0.09 fleet-wide, materially
lower than spot-heavy crude names. This compresses the strip's sensitivity to
FFA/spot forwards — TEN earnings are heavily contract-locked.

### DP2 Shuttle composition — refined

Press release narrative explicitly classifies the 22-vessel NB program as
"**ten DP2 shuttle tankers**, three VLCCs, five scrubber-fitted LR1 tankers
and one LNG carrier under construction" (1 optional LNG vessel makes 22 in
the table). Plus the NB table reveals Athens 04 (Apr-25) and Paris 24
(Aug-25) are **also classified as DP2 shuttle tankers** (vs the prior log's
guess based on Brazilian-trade callout).

In-water DP2 shuttle tankers (revised):
- **Brasil 2014** (Apr-13, 155,721 DWT) — confirmed by data kit notes
- **Rio 2016** (Mar-13, 155,709 DWT) — confirmed by data kit notes
- **Athens 04** (Apr-25, 154,350 DWT) — confirmed by Q1 press release NB table
- **Paris 24** (Aug-25, 154,350 DWT) — confirmed by Q1 press release NB table

**4 in-water + 10 NB = 14 total DP2 shuttle tankers** in TEN's program.
Lisboa (Mar-17) and Porto (Jul-22) are *not* explicitly tagged as DP2 in
either source — best treated as conventional suezmax on Brazilian charters
unless contradicted (prior log's "6 in-water" appears to have been a guess).

### Q2-26 subsequent events affecting the balance sheet

- **7-Apr-2026:** agreed to repurchase 2 × 2007-built suezmaxes from 5-year
  leases at below-FMV — these are Arctic + Antarctic (the Jun-2021 SLB that
  was set to expire Jun-2026). Lease-liability bucket will drop; on-curve
  fleet will gain 2 vessels.
- **20-May-2026:** 10-year VLCC sale completed — generated **$83M free cash
  after debt repayment**. Likely Ulysses (May-16 build = age 10 in 2026).
- **23-Apr-2026:** 5-year employment extensions agreed on Brasil 2014 and
  Rio 2016 at higher rates commencing H2 2028 — "expected to generate more
  than $200M in gross revenues." Extends shuttle TC visibility through 2033.

### Common dividend — full 2026 picture

- 2025: $1.10/share aggregate (semi-annual)
- 2026 H1 (paid): $0.50/share
- 2026 H2 (declared, paid July 2026): **$1.00/share**
- **2026 aggregate: $1.50/share** (+36% YoY, "highest in 10+ years")

For the dividend strip, this is a base + variable structure — closer to
INSW / FRO than to NAT-style 100% payout. Cumulative common + preferred
dividends "over $1 billion since 2002 NYSE listing" per the release.

### Now-complete schema readiness

Every required field for a TEN balance sheet YAML now has a primary source:

| schema field | Q1 2026 value | Source |
|---|---|---|
| cash_and_equivalents | $321,416K | 6-K BS line |
| working_capital_net | ≈ +$174,654K | 6-K (Other assets $331,398 − Other liabilities $156,744; treat as composite per §4.2) |
| total_debt | $2,136,109K | 6-K BS line |
| lease_liabilities | partly in Other assets (ROU) / Other liabilities; split needs 20-F | 6-K narrative + footnotes |
| newbuild_capex_commitments | ≈ $2,403M − $442.7M = ~$1,960M | data kit contracts − 6-K advances |
| newbuild_advances_paid | $442,740K | 6-K BS line |
| diluted_shares_outstanding | 29,971,603 | 6-K |
| **preferred_equity** | ≈ $285,000K | inferred from $6.75M Q dividend + share-count math |

Cost structure (for cost_structures/ten.yaml):
- Opex per day per vessel: $9,952 (multi-class; would split per-class in build)
- G&A: $12.44M Q1 → ~$50M annualised; data kit normalisation needed
- Interest expense: $20.79M Q1 → ~$83M annualised (down from prior $87M)
- **Tax rate: 0% (no corporation tax)**

Dividend policy (for dividend_policies/ten.yaml):
- `policy_type: base_plus_variable`
- 2026 aggregate $1.50/share; semi-annual cadence
- Preferred dividend overhead: $27M/yr deducted at the corp level

### Remaining methodology blockers (unchanged)

1. **DP2 Shuttle vessel class** — binding. The cheap-unblock path is
   off-curve-at-contracted-book: in-water sleeve (Brasil 2014 + Rio 2016 +
   Athens 04 + Paris 24) at NPV of contracted bareboat/TC cash flows; NB
   sleeve (Anfield + 9 others) at advances paid + delivered-NB-value-less-
   remaining-commitment. The data kit + 6-K give every number to do this
   properly: contracted day-rates per vessel, NB contract prices, debt
   already drawn, remaining capex schedule.
2. **3-or-4 sleeve carve-out** — once shuttle is on-curve, `carveout.py`
   needs extension. Concrete sleeves: crude (VLCC + Suezmax + Aframax),
   product (Aframax LR + Panamax + MR + Handysize), LNG (Tenergy + Maria
   Energy), shuttle (4 in-water + 10 NB).

### Revisit-criteria status (updated)

1. **DP2 shuttle handling decision** — *still binding*, but the data anchor
   is now fully concrete (contracted rates + NB structures known).
2. ~~`preferred_equity` schema line~~ **DONE 2026-06-05.**
3. ~~Fetch Q1 2026 6-K~~ **DONE 2026-06-05 PM** — all numbers extracted above.
4. **3-or-4 sleeve carve-out extension** — pending; design once shuttle
   class decision is made.
5. Then standard onboarding: assemble 4 YAMLs (data is ready) → run → tests
   → §6 entry.

### Cross-references
- 6-K filing: [SEC EDGAR accession 0001193125-26-236934](https://www.sec.gov/Archives/edgar/data/1166663/000119312526236934/d143886dex991.htm) (filed 2026-05-22)
- Data kit: [tenn.gr/TEN-Data-Kit-May-11_26.pdf](https://www.tenn.gr/wp-content/uploads/2026/05/TEN-Data-Kit-May-11_26.pdf) (May 11, 2026)
- VIE stance: **Bullish $51.50** (`outputs/vie_coverage_universe_xref.md`) — divergence-from-tool unresolved (no tool value).
- Shuttle-tanker gap logged in LIMITATIONS.md §2 (Coverage gaps — vessel classes).

---

## 2026-06-05 — Data-kit ingest. Materially warmer start for any future build.

**Decision:** **Still deferred** — the binding blocker (DP2 Shuttle vessel
class) is unchanged, but the May-2026 TEN Data Kit
([tenn.gr/TEN-Data-Kit-May-11_26.pdf](https://www.tenn.gr/wp-content/uploads/2026/05/TEN-Data-Kit-May-11_26.pdf))
closes ~70% of the data gaps the 2026-06-04 entry flagged. Recording the new
data so a future build starts with concrete inputs, not estimates.

### Corrections to the 2026-06-04 orderbook entry

- **19 newbuilds, not 18.** Missed a 1× LNG carrier (HN3643, 81,755 DWT,
  Q3 2028, $254.4M contract).
- **10 DP2 shuttle suezmaxes, not 9.** Anfield (Q3 2026, $149.1M, "long-term
  employment upon delivery") + HN2733-2741 (Q3 2027 → Q4 2028 deliveries,
  ~$148.1M each, **15-year bareboat charter upon delivery** — concrete
  contracted-book anchor for the proposed off-curve convention).
- **Total NB contract value $2,403M** (not $2.0B). Equity contribution paid
  to date $232.3M.
- Remaining NB delivery cadence: 10 in 2026, 431 in 2027, 222 in 2028,
  679 in 2028, 1,080 in 2028 (US$M; see data kit p.2).

### Balance sheet (the big unlock)

- **Expected total debt at 31-Mar-2026: $2,148.2M** (was estimate). Movement:
  $1,930.4M (31-Dec-2025) + $344.8M drawdowns − $127.0M repayments.
- **Loan amortization schedule through 2040 fully tabulated** (data kit p.3,
  including balloons assumed to be refinanced).
- Q1 2026 finance costs: $20.8M total — loan interest $26.2M, capitalised
  interest $(2.9)M, IRS valuation non-cash $(0.5)M, bunker/EUA hedges non-cash
  $(2.6)M, other items.
- Interest income Q1 2026: $2.3M.
- **Shuttle NB debt agreed: $1.1B** (9 vessels, $148.12M drawn) + Anfield
  $111.8M agreed ($44.7M drawn). Total NB debt agreed $1.21B.

### Preferred equity — structure confirmed, share counts still missing

- **Series E: 9.25% coupon**, $25 par, dividends 28th of Feb/May/Aug/Nov.
- **Series F: 9.50% coupon**, $25 par, dividends 30th of Jan/Apr/Jul/Oct.
- Both series fixed-rate from the data kit reading; floating-rate spreads
  in the stale VIE tracker (TEN-E L+688.1bp May-2027; TEN-F L+654bp Jul-2028)
  may indicate fixed-to-float at the callable dates — verify against the
  prospectuses if/when onboarded.
- **Share counts not in the data kit** — needs the 6-K or 20-F. Prior
  ~$287M aggregate estimate stays as the working number until a primary
  source replaces it. With the new schema line ([preferred_equity](../src/crude_tanker_fv/schemas.py)),
  the $ figure flows in directly.

### Fleet — full per-vessel detail now available (was missing)

**64 in-water + 19 NBs = 83 vessels, 10,958,618 DWT.** Data kit ships a full
per-vessel table (name, built date, DWT, ice class, scrubber, current
employment, TC rate, expiry). Per-class counts vs prior estimate:

| Class | Data kit | Prior estimate | Notes |
|---|--:|--:|---|
| VLCC | 3 | 2 | Dias I + Hercules I + Ulysses |
| Suezmax | 20 | 15 | Includes 5 new 2025 deliveries (Athens 04, Paris 24, Dr Irene Tsakos, Silia T; Dr Irene Tsakos is a shuttle-rate vessel) |
| Aframax | 22 | 25 | 4 DF LNG-powered (Ithaki/Chios/Njord/Ran DF) |
| Aframax LR (products) | 4 | included above | DF Mystras + DF Montmartre DF + 2 conventional |
| Panamax (products) | 9 | 9 | 2 vessels 49% FLOPEC JV |
| MR | 2 | 0 | Delos T, Dion (delivered Jan-Feb 2026) |
| Handysize (products) | 2 | 2 | Bosporos + Byzantion, 49% FLOPEC JV |
| LNG | 2 | 2 | Tenergy + Maria Energy |

### Shuttle TC rate anchor (the methodology unlock for the cheap path)

The data kit gives **per-vessel TC rates for the shuttle / Brazil-trade
sleeve**. This makes the previously-proposed "off-curve-at-contracted-book
convention" concrete:

- **Brasil 2014** (Apr-13 build, 155,721 DWT): $58,908/day TC through
  Nov-2028; annual rate escalation +$200/day until 2028 (data kit notes).
  Explicitly identified as a shuttle tanker.
- **Rio 2016** (Mar-13 build, 155,709 DWT): $58,403/day TC through Oct-2028;
  same escalation clause. Explicitly identified as a shuttle tanker.
- **Athens 04 + Paris 24** (Apr-25, Aug-25, 154,350 DWT each): $58,569/day
  TC through 2032; Paris 24 has explicit "$2,750/day Brazilian trade costs"
  callout (Brazil = Petrobras shuttle trade).
- **Dr Irene Tsakos** (Jun-25, 156,833 DWT): $33,000 min + 50-50 p/s up to
  $80,000 ceiling through Jun-2030.

If the off-curve-at-contracted-book convention is adopted, the anchor
becomes: in-water shuttle sleeve at contracted-rate cash flows discounted at
WACC; 10 NB shuttle sleeve at delivered NB price ($148.1M each) less remaining
commitment, plus a contracted-bareboat cash-flow strip (15-year terms).

### Lease liabilities — now-concrete numbers

- Sakura Princess: $10,500/day bareboat (extended 1y from Dec-2025 at lower
  rate from previous $11,800).
- Arctic + Antarctic: $13,870/day bareboat (5y from Jun-2021 — **expires
  Jun-2026**, so Q2-2026 will see them roll off or refresh).
- Tenergy LNG: $177.2M sale-leaseback financing, **classified as financing
  arrangement** (not operating lease); 40 × $2.3M quarterly + $84M purchase
  obligation at term. Treat as debt-equivalent in our schema.

### Still missing (would need 6-K / 20-F)

- Cash and equivalents at 31-Mar-2026 (data kit gives debt + interest only).
- Working capital line items (AR, AP, inventory, accruals).
- Operating-lease vs finance-lease split for `lease_liabilities` aggregate
  (data kit narrates the structure but doesn't sum the carrying values).
- **Preferred share counts** per series.
- Diluted shares outstanding (used ~30M common in prior research; refresh
  against the Q1 6-K).
- Quarterly EPS, NI, segment revenue.
- Q1 2026 dividend declarations (common + preferred).

### Revisit-criteria update

1. **DP2 shuttle handling decision** — *unchanged binding blocker*, but the
   off-curve-at-contracted-book path is now well-anchored (see "Shuttle TC
   rate anchor" above). The shuttle sleeve becomes valuable at: in-water
   sleeve = NPV of contracted bareboat/TC cash flows; NB sleeve = paid-to-date
   advances + delivered contract value less remaining commitment.
2. ~~`preferred_equity` schema line~~ **DONE 2026-06-05.**
3. **Fetch Q1 2026 6-K** for cash + working capital + share counts + segment
   detail; everything else in the schema is now coverable from data kit + 6-K.
4. Then standard onboarding: build 4 YAMLs (fleet + balance sheet + cost
   structure + dividend policy) → 3-or-4 sleeve carve-out extension → run →
   tests → §6 entry.

### Cross-references
- Data kit: [tenn.gr/TEN-Data-Kit-May-11_26.pdf](https://www.tenn.gr/wp-content/uploads/2026/05/TEN-Data-Kit-May-11_26.pdf) (May 11, 2026)
- VIE stance: **Bullish $51.50** (`outputs/vie_coverage_universe_xref.md`) — divergence-from-tool unresolved (no tool value).
- Shuttle-tanker gap logged in LIMITATIONS.md §2 (Coverage gaps — vessel classes).

---

## 2026-06-04 — DEFERRED (not onboarded). Shuttle-tanker coverage gap.

**Decision:** **Defer onboarding.** TEN was assessed as the next VIE-Bullish
candidate and **deliberately not built** — its fair value is dominated by asset
types the framework cannot spot-value, so onboarding it now would produce a
headline number resting on hand-waved sleeves. Kept on the candidate list;
revisit criteria below. This entry preserves the research so a future build
starts warm.

### Why deferred — the blockers

TEN is the **most complex name in the coverage universe**: a four-asset-type
hybrid, not the clean crude+product 2-sleeve that INSW is.

1. **DP2 shuttle tankers — the binding blocker.** 6 in-water (2013-2025,
   ~154-155k DWT) + **9 of 18 newbuilds** on order (2026-2028). These are
   offshore, dynamic-positioning, contract-backed logistics assets — **no spot
   rate, no FFA curve, no value curve** in our system, and they anchor most of
   TEN's $3.6B contracted backlog. They are ~15-20% of company value and the
   single largest slice of the newbuild book. The framework has no honest way to
   spot-value them; treating them as Suezmax-equivalent would be wrong (they
   carry a large specialised-equipment premium and trade on contracts, not spot).
2. **Preferred equity** (~$287M, multiple series per stale VIE ref) — a NAV
   subtraction with **no dedicated schema field** ~~(same gap flagged for
   HAFN's TORM stake; `marketable_equity_investments` / `preferred_equity` are
   both unmodelled lines)~~. **RESOLVED 2026-06-05:** `preferred_equity`
   added to the `BalanceSheet` schema (defaults to 0, pro-rates by sleeve in
   carve-outs — METHODOLOGY §4.2); when TEN is onboarded its preferred series
   sum can flow directly into the new line. HAFN's `marketable_equity_investments`
   remains an unmodelled line.
3. **$2.0B newbuild book / 18 vessels** — larger than the entire ~$1.33B market
   cap; half of it is shuttle tankers. Newbuild handling (§3.1 delivered-value-
   less-commitment) would be dominated by the un-curveable shuttle sleeve.
4. **Tri+-sector carve-out** — crude + product + LNG + shuttle. `carveout.py`
   currently handles a 2-sleeve (crude+product) split for INSW only. TEN needs a
   3-or-4-sleeve extension, which is real architecture work, not data entry.

### What we'd be onboarding into a deep-discount name

TEN trades at a steep discount to its own NAV (stale VIE P/NAV ≈ 0.37; price
~$44 vs VIE NAV/sh ~$98 — though that VIE figure is >1yr stale). The framework
would almost certainly read it as a deep BUY on NAV — but **that NAV is exactly
the part dominated by assets we can't value** (shuttle tankers + preferreds +
newbuild book). Onboarding without a shuttle module would produce a confident-
looking BUY built on the framework's weakest foundation. Deferring is the
honest call.

### Research gathered 2026-06-04 (so a revisit starts warm)

- **Status:** still public (NYSE: TEN), no take-private; AGM 27 May 2026. The
  stale VIE coverage (financials ref Q4-24, last update 15 Apr 25) was NOT a
  take-private signal — TEN is operating normally.
- **Q1 2026 (strong):** revenue $253M (+22% YoY), net income $89M (+136%),
  operating income $110M, EPS $2.72 (vs $1.35 est), adj. EBITDA $154M,
  utilization 98.3%. Vessel opex $53.3M, voyage expense $29.8M (quarter).
  ~30M common shares; market cap ~$1.33B; price ~$44.
- **Guidance:** Q2 EPS ~$2.37, Q3 ~$1.88 (management). Contracted backlog
  $3.6B. ~$83M free cash from May 2026 asset sales.
- **Fleet (~65 in-water + 18 NB):**
  - Crude: 2 VLCC (2017-2020, eco scrubber) + 15 Suezmax (2006-2025, 4 ice-class)
    + 25 Aframax (2007-2024, incl. 4 LNG-powered DF)
  - Product: 9 Panamax/LR1 (2008-2016) + 4 "Aframax LR"/LR2 (incl. 2 LR2 DF NB)
    + 2 Handysize (2007, ice-class 1B)
  - LNG: 2 LNG carriers (2016, 2022; ~93k DWT)
  - **Shuttle (DP2): 6 in-water (2013-2025)**
  - Newbuilds (~2.96M DWT, ~$2.0B): 9 shuttle (2026-2028), 3 VLCC (2027-2028),
    4 Panamax (2027-2028), 2 MR (2027)
- **Still needed for a build:** exact cash, total debt, preferred series +
  liquidation value, precise share count, per-vessel fleet table, dividend per
  share. The Q1 2026 6-K (StockTitan 403'd via WebFetch; pull direct from
  tenn.gr IR or SEC EDGAR) has these.

### Revisit criteria (what unblocks TEN)

1. **A DP2 shuttle-tanker handling decision** — either (a) a `Shuttle` vessel
   class + value curve + contracted-rate treatment in `vessel_value_curves.yaml`
   / scenarios, or (b) an explicit off-curve-at-contracted-book convention for
   the shuttle sleeve (the "Pragmatic hybrid" option), documented as a §11.5-
   style framework gap. Until one exists, TEN's NAV is not honestly computable.
2. ~~A `preferred_equity` schema line~~ **DONE 2026-06-05** — schema field
   added with sleeve pro-rating + tests (METHODOLOGY §4.2). Available to
   future preferred-bearing names.
3. Then the standard onboarding (fetch 6-K detail → build 4 YAMLs → 3-sleeve
   carve-out → run → tests → §6 entry).

### Cross-references
- VIE stance: **Bullish $51.50** (`outputs/vie_coverage_universe_xref.md`) — the
  divergence-from-tool question is unresolved because we have no tool value.
- Shuttle-tanker gap logged in LIMITATIONS.md §2 (Coverage gaps — vessel classes).

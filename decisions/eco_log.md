# ECO — Decision Log

## 2026-08-31T15:03:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.0pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-31T14:32:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.0pp (k_broker 1.12)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -5.9pp
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -5.9pp

**Decision:** _[pending annotation]_

---

## 2026-08-29T21:35:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-29T20:49:33+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-29T20:44:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-29T20:38:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $66.86
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -37.6%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +1.82 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +1.5pp

**Decision:** _[pending annotation]_

---

## 2026-08-25T22:33:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $65.04
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -35.9%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.4pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-25T22:30:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $65.04
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -35.9%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.4pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-16T20:06:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.29
- Single-point FV: $39.73
- Scenario PW FV: $41.71 (EV -30.8%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.1pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -3.63 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.4pp

**Decision:** **THE SIGN-OPPOSITE ROW (+3.3pp EV, k −0.04): ECO FELL while the book rallied** ($63.81 → $60.29, −5.5% over the two sessions). Gate absorb, TWO causes (adversarially verified two-cause, max residual 0.05pp — workflow wf_8b0d1184, 2026-08-16): (1) toll-cliff C2 reweight, crude-only (decisions/crude_day60_toll_cliff_2026-08-16.md, owner ruling R1); (2) the 8/12→8/14 price-vintage absorb (8/13 fetch committed 55b3a75; 8/14 Friday close fetched manually 2026-08-16 after Fri/Sat cron DNS stand-downs, committed e92fa8a). ΔNAV 0.0%. A rich name getting cheaper compresses toward fair — EV improves mechanically. TRIM/SHORT (rich · cycle position, §12 relabel) stands; VALIDATED-TIGHT unchanged. NAV unchanged $39.54.

---

## 2026-08-14T15:08:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.5pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T21:00:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.5pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T20:46:39+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.5pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.5pp

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:32:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:28:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:24:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:15:23+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:11:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T17:07:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-13T16:58:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $62.88
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -34.1%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +1.02 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.9pp

**Decision:** _[pending annotation]_

---

## 2026-08-13 (PM) — Pareto name-text triage (July-hole audit sweep, issues 7/14→8/13)

- OET Q2 (reported 8/04 after close): Pareto 8/05–8/06 — "out of the park"; possible 2026 EPS ~$18,
  payout ~$15/sh; NAV path stated 1.5× (Q2 basis) → just below 1.3× (post-beat + Q3 cashflow) → 1.15×
  with +10% asset values; HOLD reiterated (with FRO/INSW). 7/28: Q2 NAV $39.2 → scenario $43.3 at
  $125k/d VLCC / $90k/d Suezmax.
- **8/13: OET trades ex-dividend $5.25 in Oslo TODAY (New York tomorrow 8/14)** — tonight's price
  refresh will print the drop; do NOT read it as drift, and note the STAGED watchlist rebase draft
  (8/07 vintage) pre-dates the ex-date.
- 8/03 color: Pareto pre-flagged "one of the most spectacular quarterly tanker reports ever"; OET
  lifted CPC cargoes in July near $300k/d.

## 2026-08-10T19:51:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -33.0%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.1pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-10T19:35:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -33.0%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.1pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-10T19:34:48+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -33.0%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.1pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** STAGE A TANKER RE-ANCHOR 2026-08-10 (one ratify; prereg frozen 7/15, four owner rulings; the Jun-7 war vintage RETIRED): EV increment via the scenario legs' re-expression against the new base (NAV 0.0 by construction — rates never touch NAV). The book-wide BUY-ward drift is the KNOWN deck-incoherence documented in stage_a_halt_investigation_2026-08-10.md — three names VOIDed (BRUT/CAPT/TNK), every other read stands with this increment explained; the deck re-expresses at the 8/16 toll-cliff re-derivation.

---

## 2026-08-10T18:06:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -33.0%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.1pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-10T18:05:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $39.73
- Scenario PW FV: $41.44 (EV -33.0%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.1pp (k_broker 1.13)
- Sector: crude

**Material deltas since last run:**
- ⚑ scenario PW FV +11.1%
- Δprice: no change | Δsingle FV: -5.5% | Δscenario FV: +11.1% | ΔNAV: no change | Δspread: +0.8pp

**Decision:** _[pending annotation]_

---

## 2026-08-10T17:59:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T22:35:33+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T22:28:43+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T14:17:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:43:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:39:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:37:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:34:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:29:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:22:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $42.03
- Scenario PW FV: $37.31 (EV -39.7%)
- NAV / share: $39.54
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: +0.1% | ΔNAV: +0.1% | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T12:12:00+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $41.99
- Scenario PW FV: $37.27 (EV -39.8%)
- NAV / share: $39.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +4.3% | Δscenario FV: +4.4% | ΔNAV: +4.9% | Δspread: -2.4pp

**Decision:** MARKS-TRAIL PROMOTION 2026-08-09 (triage §A #1-5): VLCC prints ($120-130M at 9-13y) + the TNK Suezmax age-17 realization ($53.5M) move the crude mid-age anchors. NAV +4.9% -> $39.49, EV +2.5pp -> -39.7%. NO FLIP - TRIM/SHORT stands. Print-driven, same event as DHT/FRO/INSW.

---

## 2026-08-09T02:55:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T02:48:48+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T02:36:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-09T02:28:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T23:52:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T23:45:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T23:19:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T23:10:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T22:31:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T22:30:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T22:13:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T22:04:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T21:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T21:41:39+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T21:31:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T21:23:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T20:42:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T20:34:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** CCEC-refresh run (0-material for ECO) — ECO's substantive record is its dated Q2 REPORT-DAY REFRESH entry below (2026-08-08, band HIT). Baseline ratified same day (ECO+CCEC row in RATIFY_LOG; the batch-to-end-of-drain plan was dropped — the gate re-reds un-ratified names at every subsequent run, so ratifies are per-name from here on).

---

## 2026-08-08T20:09:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Clean-stamp regen of the annotated Q2 refresh (0-material vs the refresh run) — the substantive record is the dated Q2 REPORT-DAY REFRESH entry below (2026-08-08, band HIT, both halves verified). Baseline re-anchor batched to the end-of-drain ratify.

---

## 2026-08-08T19:57:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $40.24
- Scenario PW FV: $35.69 (EV -42.3%)
- NAV / share: $37.65
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.17)
- Sector: crude

**Material deltas since last run:**
- ⚑ NAV/sh +9.4%
- Δprice: no change | Δsingle FV: +8.2% | Δscenario FV: +9.6% | ΔNAV: +9.4% | Δspread: -4.2pp

**Decision:** Q2 REPORT-DAY REFRESH (backlog drain #1, under the 2026-08-08 transition
mechanism — sheet + manifest landed TOGETHER, preflight clean, pair guard green).
Source: H1 6-K acc 0001104659-26-090429 (filed 8/4), subsequent-events note audited
FIRST — excluded from the snapshot: the $5.25/sh dividend (declared post-Q2), the 7/2
$45M facility draw, the 7/8 Nissos Vous delivery (Vous stays the one NB row at 6/30,
commitment $79.4M issuer-disclosed / advances embedded). NAV $34.42→$37.65 (+9.4%) —
INSIDE the pre-registered band [35.8, 40.4] (point ~$38.1; prereg in the refresh
commit): BS delta +$4.17/sh (cash +71.3M, WC +51.6M, debt +39.4M, commitments −79.5M)
less ~$0.5 fleet-side (fractional-age basis ~+0.5y uniform, offset by Tigani
NB→operating + Vous PV + issuer-evidenced scrubber premiums). Both halves VERIFIED in
this run's breakdown (247.8/722.5/79.4). Forward invariance held (24 other names
delta 0.0). NO FLIP — TRIM/SHORT stands (§12 relabel: rich · cycle position, not a
short), EV −47.4%→−42.3%; k_broker second-diff −0.06 = FV-side vs static pnav —
VALIDATED-TIGHT stands. Scrubber ledger 16→17 (Tigani operating; issuer aggregate
8/4 ex-99.1 covers Tigani+Vous — flags upgraded from peer-trap false to
issuer-evidenced true). The 7.1× spot-TCE sanity warn = the genuine war spike
(release actual: VLCC $213.6k/day Q2 TCE). STAGE-A BASIS CAPTURED: Q3 QTD VLCC 48%
booked @ $206,600/day + Suezmax 42% @ $133,000/day (stage_a_basis §6 updated).
Baseline re-anchor batched to the end-of-drain ratify.

---

## 2026-08-08T18:13:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -47.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.9pp (k_broker 1.23)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T18:01:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -47.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.9pp (k_broker 1.23)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T17:55:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -47.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.9pp (k_broker 1.23)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T17:29:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $61.86
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -47.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.9pp (k_broker 1.23)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +1.38 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +1.0pp

**Decision:** _[pending annotation]_

---

## 2026-07-31T19:45:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) final clean-stamp regen — stamp at clean HEAD; no movement.

---

## 2026-07-31T19:39:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) clean-stamp regen at the coherence-restore commit — no movement.

---

## 2026-07-31T19:31:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) coherence-restore regen — the three staged Q2 refreshes were REVERTED on the manifest side (see the VOID banner at the top of sb/tnk/asc logs + decisions/q2_cluster_transition_2026-07-31.md); this run is coherent Q1-manifest-on-Q1-balance-sheet. No movement vs the pre-refresh state.

---

## 2026-07-31T19:27:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T19:18:35+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31) clean-stamp regen (TNK Q2 refresh arc close) — no movement; the refresh records stand.

---

## 2026-07-31T19:11:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T19:01:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T18:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) clean-stamp regen (SB Q2 refresh arc) — no movement; the refresh + band-miss records stand.

---

## 2026-07-31T18:24:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31 — FILING-LANDED triage: two 7/30 6-Ks (neither is earnings)

**Decision:** TRIAGED, no input change. (1) 088444 = **Nissos Sifnos drone strike 7/30** at
the CPC terminal (Kazakh crude, Black Sea) — crew safe, no spill, minor damage, voyage
continuing. Operational event, no financial quantification; NOTE CAREFULLY: Black Sea/CPC
theater, NOT Hormuz — this is Ukraine-war-adjacent war-risk evidence, kept OUT of the Iran
scenario observations. Watch the Q2 call (8/5) for repair/off-hire quantification. (2)
088713 = webcast notice confirming **Q2 results 8/4 after NYSE close** (calendar already
confirmed). Fleet boilerplate: 10 Suezmax + 8 VLCC sailing, all scrubber-fitted ✓.

---

## 2026-07-31T18:06:00+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31) clean-stamp regen (B' arc close) — no movement; the two-cause annotations below stand.

---

## 2026-07-31T18:03:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $60.48
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -46.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.9pp (k_broker 1.21)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +6.4pp
- Δprice: +7.38 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +6.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-31T18:00:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.10
- Single-point FV: $37.19
- Scenario PW FV: $32.57 (EV -38.7%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +7.5pp (k_broker 1.10)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -4.78 | Δsingle FV: no change | Δscenario FV: +1.5% | ΔNAV: no change | Δspread: -4.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-28T19:32:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28 EVE) clean-stamp regen at a9b99dc — the parked stamp refresh, unblocked by the anchor-fix commit; no number movement, the day's annotations below stand.

---

## 2026-07-28T16:42:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28, later) Compass-W30 correction pass (owner fetch + review — triage §H): Oldendorff pair 37.5→37.0 forward-delivery (flag corrected, in_fit false unchanged), AASHNA trade-press cross-checked (AANYA = the unsold sister), the 'third Meghna vessel' withdrawn (= WF Artemis, promoted 7/18). ZERO number movement (fit byte-identical 30.86/24.42, n=33; corrections touched excluded rows + notes only). NAV state unchanged from the promotion entry below.

---

## 2026-07-18 — price-vintage drift (7/17 close row): EV-only, accepted at the Week-close gate

**Decision:** price-vintage drift ACCEPTED-as-mechanical (2026-07-18 Week-close gate): the 2026-07-17 close row landed via the daily price-refresh — EV%-only move, **ΔNAV +0.0%** (no model input changed; the FV stands at the 7/15 regen basis). Baseline re-ratify NOT executed — the batch absorb is the owner's deliberate step (2026-06-30 standing-thread discipline); recross of any band on a later vintage = a NEW eyeball.

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

---

## 2026-07-28T15:58:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28) family-sidecar re-stamp regen (promotion arc, final) — no movement; annotations below stand.

---

## 2026-07-28T15:51:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28) clean-stamp regen at 71e7020 (marks-promotion arc close) — no movement; the promotion annotations below stand.

---

## 2026-07-28T15:36:23+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-26T21:26:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-26) week-close clean-stamp regen at d1fe786 — no movement; the week-close annotations below stand.

---

## 2026-07-26T21:20:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-26T21:19:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.5%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +3.64 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +3.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-24T16:05:00+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-24T16:04:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-24T15:56:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -3.22 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-24T15:55:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $57.46
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -44.1%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +3.22 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-22T22:01:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:56:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:50:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:48:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T18:14:30+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.24
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.8%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.5pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.36 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-18T20:22:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the PPMX seed — same state as the dated entries below; no new movement.

---

## 2026-07-18T20:21:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-18T20:07:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the 2026-07-18 marks promotion + family re-run — same state as the dated entries below; no new movement.

---

## 2026-07-18T20:06:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the 2026-07-18 marks promotion — same state as the dated entry below; no new movement.

---

## 2026-07-18T19:59:08+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.19
- Scenario PW FV: $32.10 (EV -40.4%)
- NAV / share: $34.42
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: +0.2% | Δspread: -0.1pp

**Decision:** _[pending annotation]_

---

## 2026-07-18T19:38:05+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18, final) — same state as the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:36:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18, family sidecar re-run at the current EV state) — same state as the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:35:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18) — identical state to the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:23:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-18T19:22:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.88
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.3pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:42:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:24:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:23:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:15:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T17:46:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T16:48:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T16:47:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T15:45:30+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T14:33:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $56.73
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -43.4%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.9pp (k_broker 1.16)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +2.53 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-14T21:24:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.20
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.8%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:56:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.20
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.8%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:51:05+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.20
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.8%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:49:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.20
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -40.8%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +8.6pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:44:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.94
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -41.6%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:31:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.94
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -41.6%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.3pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T13:00:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $54.94
- Single-point FV: $37.18
- Scenario PW FV: $32.09 (EV -41.6%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +9.3pp (k_broker 1.13)
- Sector: crude

**Material deltas since last run:**
- ⚑ scenario PW FV +24.7%
- Δprice: +2.71 | Δsingle FV: no change | Δscenario FV: +24.7% | ΔNAV: no change | Δspread: +3.3pp

**Decision:** Drift explained (2026-07-12): the pre-registered Jun-9 war-tilt RESTORE — trigger crude_doha_talks_resumption fired Jul-7/8, executed at owner go (decisions/doha_check_2026-07-12.md; commit precedes this run). Crude PW-FVs re-weighted UP; NAV unchanged (weights never touch asset NAV). Plus the Friday-close price vintage in the EV denominator. Ratify staged pending the owner's flip eyeball.

---

## 2026-07-10T20:34:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:29:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:27:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:20:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:12:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:06:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:04:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.23
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -50.7%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.0pp (k_broker 1.09)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.87 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.7pp

**Decision:** _[pending annotation]_

---

## 2026-07-06T19:23:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.8pp (k_broker 1.10)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:55:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +6.8pp (k_broker 1.10)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -6.1pp
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -6.1pp

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:40:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:18:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:42:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:35:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T02:11:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:55:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:54:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:14:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:04:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:56:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:30:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:10:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +3.17 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:59:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -48.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -3.17 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:58:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $53.11
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -51.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.9pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +3.17 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $25.73 (EV -48.5%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.0pp (k_broker 1.14)
- Sector: crude

**Material deltas since last run:**
- ⚑ scenario PW FV -35.7%
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -35.7% | ΔNAV: no change | Δspread: -2.8pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -19.9%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.8pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -19.9%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.8pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -19.9%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.8pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -19.9%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.8pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.18 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -20.2%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -20.2%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -20.2%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -20.2%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.18 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.94
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -19.9%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.8pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.18 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.18
- Scenario PW FV: $40.02 (EV -20.2%)
- NAV / share: $34.35
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.0pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.4% | Δscenario FV: -0.4% | ΔNAV: -0.6% | Δspread: +0.4pp

**Decision:** (2026-07-01) §9.6 on-curve fix + operating-scrubber verification — ECO CLEARED PROVISIONAL →
**VALIDATED-TIGHT** (the first TIGHT of the reconciliation arc). Fifth P0 name, and the cleanest — no forks.
Pre-reg `decisions/eco_reconciliation_prereg_2026-07-01.md`. ALL figures VERIFIED vs the Q1-2026 6-K (EDGAR
acc 0001104659-26-060273, Exhibit 99.1): debt $683.1M (incl. sale-leasebacks), cash $176.5M, advances
$39,737,420 → commitment $158.86M, 2 Suezmax NBs $99.3M each (Tigani May-2026, Vous Jul-2026), shares
39,044,655, fleet 8 VLCC + 8 Suezmax (no phantoms). The ONLY issue was OFF_CONVENTION: the 2 Suezmax NBs sat
at delivered market with no `years_to_delivery`. FIX: split into Tigani (0.12) + Vous (0.29) so they PV-discount
on the §9.6 curve → ECO leaves `OFF_CONVENTION_QUEUE`. Also verified the 16 on-water scrubbers ("all
scrubber-fitted", 6-K L76) → `OPERATING_SCRUBBER_VERIFIED{ECO:16}`, leaves `OPERATING_SCRUBBER_QUEUE`.
PROVENANCE CATCH: the guard blocked defaulting scrubber=true on the NBs — the 6-Ks' scrubber statements are
existing-fleet-scoped, never newbuild-specific (the SB trap), so the NBs are booked **scrubber=false**
(conservative, registered in newbuild_specs.yaml; upgradeable on a delivery-6-K disclosure). NAV $34.56→$34.35
(−0.6%, §9.6 PV discount + conservative NB scrubber) — BELOW the drift threshold (gate stable, no re-ratify
required). ECO stays **rich · cycle position (not a short)** (price ~1.39× NAV) — VALIDATED-TIGHT means the NAV
is SOLID, NOT that ECO is cheap: it is validated-but-RICH, **NOT a new actionable long. Tight-actionable surface
stays SB + SBLK.** SANITY OK (−12.9% to Pareto NAV). Five reconciliations, still zero new tight actionable longs.

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.9%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.6pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.9%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.6pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.9%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.6pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.9%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.6pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.12
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.9%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.6pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.52 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.60
- Single-point FV: $37.33
- Scenario PW FV: $40.17 (EV -19.0%)
- NAV / share: $34.56
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.9pp (k_broker 1.13)
- Sector: crude

**Material deltas since last run:**
- ⚑ NAV/sh +7.5%
- Δprice: -0.28 | Δsingle FV: +5.4% | Δscenario FV: +5.2% | ΔNAV: +7.5% | Δspread: -4.9pp

**Decision:** Amendment B — crude age-0 = xclusiv Resale (VLCC 175, Suezmax 114.3). ECO NAV +7.5% to ~$34.56, a touch above pre-Thread-1 (xclusiv Suezmax Resale 114.3 > old 108); its scenario position moves TRIM/SHORT->HOLD on the directed Suezmax lift. Read straight off the curve. PROVENANCE (the flip is a VINTAGE refresh, not a basis change): the old $108 was the xclusiv 2026Q1 Resale (2026-03-30); the new $114.3 is the xclusiv 2026Q2 Resale (2026-06-22) — same xclusiv-Resale basis, one quarter fresher. The firm Suezmax market rose ~6% Q1->Q2, lifting ECO into the fairly-valued band. ECO's call is ANCHORED to the dated xclusiv Resale curve; if a future quarter moves Suezmax again, the call moves with it (neither $108 nor $114.3 was an error — both are xclusiv Resale, different vintages).

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $35.41
- Scenario PW FV: $38.18 (EV -23.5%)
- NAV / share: $32.16
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +16.8pp (k_broker 1.19)
- Sector: crude

**Material deltas since last run:**
- ⚑ NAV/sh -5.1%
- Δprice: no change | Δsingle FV: -3.7% | Δscenario FV: -3.6% | ΔNAV: -5.1% | Δspread: +3.2pp

**Decision:** Thread 1 basis correction (not a market move). VLCC/Suezmax age-0 corrected to dated prompt-resale ($175M->$145M / $108M->$95M). ECO's young crude tonnage reprices -> NAV -5.1%, pre-registered. Accepted pending owner review; re-ratify deferred.

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -20.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -2.00 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $51.88
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -23.7%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +16.0pp (k_broker 1.18)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.60 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -24.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +16.7pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.78
- Scenario PW FV: $39.59 (EV -24.6%)
- NAV / share: $33.88
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +16.7pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.5% | Δscenario FV: +0.5% | ΔNAV: +0.5% | Δspread: -0.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.60
- Scenario PW FV: $39.41 (EV -24.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.0pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.60
- Scenario PW FV: $39.41 (EV -24.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.0pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.2% | Δscenario FV: +0.2% | ΔNAV: no change | Δspread: -0.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -25.1%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.4pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -25.1%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.4pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -25.1%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.4pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $52.48
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -25.1%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +17.4pp (k_broker 1.20)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T21:55:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T18:49:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T14:28:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T02:42:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T00:38:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.76
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.9%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.1pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.81 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -1.0pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T23:54:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.57
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -22.2%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-11 — §15.7 retro screen (formalised today): **N/A (gated)** — Pareto P/NAV 1.21×, premium VLCC name (Alafouzos control is irrelevant at a premium — §15.7 Step 0 doctrine).

---

## 2026-06-11T15:40:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $50.57
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -22.2%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +1.37 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +1.8pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T03:20:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $49.20
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -20.1%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +1.50 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.0pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T02:59:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -17.5%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:17:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -17.5%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -17.5%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T18:16:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -17.5%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T13:25:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.67
- Scenario PW FV: $39.33 (EV -17.5%)
- NAV / share: $33.71
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10 — Pareto free-text retro-sweep (64 mentions, 2025-01 → 2026-06)

Distilled from `outputs/pareto_mentions_eco.md`. Pareto covers ECO as OET
(Oslo line) — the alias map in sp_scan.py handles this.

**Pareto NAV/stance trajectory:** NAV NOK 247 (Jun-25) → NOK 263 (Jun-20-25
revision); premium expanded 1.05× (May-25) → 1.44× (2026-03-27) → ~1.55×
(2026-05-04) — the richest tanker name on their numbers. **Lowered to HOLD
2026-05-26** after Q1.

**The implied-pricing flags are the best part:** 2026-02-19: "A 5Y old VLCC
is currently bought at ~$154m in the OET share" (vs their own regression
fair level); 2026-05-11: "a suezmax resale is implicitly bought at ~$150m
in FRO and OET." Pareto's own arithmetic was flagging froth months before
their downgrade — and our txn-anchored TRIM/SHORT (EV −17.6%) is the same
read with a sharper pencil. OET's "well-earned NAV premium" franchise
(consistently strong realized TCEs) is the bull counter-argument they cite.

---

## 2026-06-10T12:59:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.66
- Scenario PW FV: $39.32 (EV -17.6%)
- NAV / share: $33.70
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:49:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $36.66
- Scenario PW FV: $39.32 (EV -17.6%)
- NAV / share: $33.70
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.3pp (k_broker 1.12)
- Sector: crude

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → TRIM/SHORT (overvalued)
- ⚑ single-point FV -13.9%
- ⚑ scenario PW FV -13.4%
- ⚑ broker spread +12.3pp
- ⚑ NAV/sh -15.6%
- Δprice: no change | Δsingle FV: -13.9% | Δscenario FV: -13.4% | ΔNAV: -15.6% | Δspread: +12.3pp

**Decision:** _METHODOLOGY RE-BASE (txn-anchored marks default-on, owner
decision 2026-06-09) — not a market move. HOLD → TRIM/SHORT is the
txn-anchored reading detailed in the 02:09:54 annotation below. See
METHODOLOGY Appendix A Part 4._

---

## 2026-06-10T02:09:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $45.41 (EV -4.8%)
- NAV / share: $39.93
- Position: **HOLD (fairly valued)**
- Broker spread: -1.0pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _2026-06-09 Pareto S&P sweep: VLCC fit dropped −18% at both
mid-age anchors (see dht_log.md for the fit detail). ECO is VLCC-heavy
modern fleet → txn-anchored reading NAV $33.70 / EV −17.6%, a
**HOLD → TRIM/SHORT flip**. Baseline headline above unchanged (toggle
opt-in); default-on decision pending with owner. Duplicate 02:09:49
entry below covered by this annotation._

---

## 2026-06-10T02:09:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $45.41 (EV -4.8%)
- NAV / share: $39.93
- Position: **HOLD (fairly valued)**
- Broker spread: -1.0pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T01:33:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $45.41 (EV -4.8%)
- NAV / share: $39.93
- Position: **HOLD (fairly valued)**
- Broker spread: -1.0pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T23:27:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $45.41 (EV -4.8%)
- NAV / share: $39.93
- Position: **HOLD (fairly valued)**
- Broker spread: -1.0pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T19:14:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $45.41 (EV -4.8%)
- NAV / share: $39.93
- Position: **HOLD (fairly valued)**
- Broker spread: -1.0pp (k_broker 0.99)
- Sector: crude

**Material deltas since last run:**
- ⚑ position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- ⚑ scenario PW FV +39.6%
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +39.6% | ΔNAV: no change | Δspread: -0.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-09T15:13:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -31.8%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-07T15:11:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $47.70
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -31.8%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.40 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:24:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:10:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:08:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:03:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-03T21:01:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T21:03:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:33:10+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:28:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:22:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $48.10
- Single-point FV: $42.56
- Scenario PW FV: $32.53 (EV -32.4%)
- NAV / share: $39.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -0.8pp (k_broker 0.99)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---


# DHT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

---

## 2026-06-10T02:49:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $14.31
- Scenario PW FV: $15.08 (EV -8.1%)
- NAV / share: $12.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.0pp (k_broker 1.14)
- Sector: crude

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → TRIM/SHORT (overvalued)
- ⚑ single-point FV -13.2%
- ⚑ scenario PW FV -12.9%
- ⚑ broker spread +13.4pp
- ⚑ NAV/sh -15.4%
- Δprice: no change | Δsingle FV: -13.2% | Δscenario FV: -12.9% | ΔNAV: -15.4% | Δspread: +13.4pp

**Decision:** _METHODOLOGY RE-BASE, not a market move: owner decision
2026-06-09 flipped `use_transaction_anchored` to pipeline DEFAULT —
transaction-validated marks are now the headline marks (rationale incl.
"Sinokor's bid IS the VLCC market"). The position flip BUY → TRIM/SHORT
is the txn-anchored reading detailed in the 02:09:54 annotation below.
k_broker 1.14 now reads as the broker premium over transaction levels —
uniform ~1.12-1.14 across DHT/ECO/FRO. See METHODOLOGY Appendix A
2026-06-09 Part 4._

---

## 2026-06-10T02:09:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $17.32 (EV +5.6%)
- NAV / share: $15.29
- Position: **BUY (undervalued)**
- Broker spread: -1.4pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _2026-06-09 Pareto archive S&P sweep expanded the VLCC
transaction sample 6 → 11 in-window prints (2025 Dalian/Bohai/DHT Lotus
prints added). New VLCC fit: 5yr $138M → $112.7M (−18.3%), 10yr $111M →
$90.9M (−18.1%). Headline above is at BASELINE marks (toggle opt-in);
under `use_transaction_anchored=True` DHT reads NAV $12.93 / EV −8.1% —
a **BUY → TRIM/SHORT flip**. DHT is the single-class methodology
validator, so this is the sweep's most consequential reading: the
broker-resale curve we anchored to runs ~18% above arm's-length 2025-26
VLCC disposals. Default-on decision deliberately NOT taken unilaterally —
flagged to owner (changes headline calls on 5 names). The 02:09:49
duplicate entry below is the same run double-invoked; this annotation
covers both._

---

## 2026-06-10T02:09:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $17.32 (EV +5.6%)
- NAV / share: $15.29
- Position: **BUY (undervalued)**
- Broker spread: -1.4pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T01:33:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $17.32 (EV +5.6%)
- NAV / share: $15.29
- Position: **BUY (undervalued)**
- Broker spread: -1.4pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T23:27:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $17.32 (EV +5.6%)
- NAV / share: $15.29
- Position: **BUY (undervalued)**
- Broker spread: -1.4pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T19:14:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $17.32 (EV +5.6%)
- NAV / share: $15.29
- Position: **BUY (undervalued)**
- Broker spread: -1.4pp (k_broker 0.99)
- Sector: crude

**Material deltas since last run:**
- ⚑ position TRIM/SHORT (overvalued) → BUY (undervalued)
- ⚑ scenario PW FV +29.8%
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +29.8% | ΔNAV: no change | Δspread: -0.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-09T15:13:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-07T15:11:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:24:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:10:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:08:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:03:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-03T21:01:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T21:03:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:33:10+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:28:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:22:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.40
- Single-point FV: $16.49
- Scenario PW FV: $13.34 (EV -18.7%)
- NAV / share: $15.29
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: -1.1pp (k_broker 0.99)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---


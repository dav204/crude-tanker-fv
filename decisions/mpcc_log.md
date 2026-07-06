# MPCC — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

---

## 2026-07-06T18:40:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.52
- Single-point FV: $2.21
- Scenario PW FV: $2.06 (EV -18.1%)
- NAV / share: $2.04
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.0pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06 — Container determinant refresh (MB W27 ingest; trigger container_mb_refresh)

- Model state: NAV/share $2.02 → **$2.04** (+1.0%); scenario PW FV $2.06; EV −13.7pp → **−18.1%** (ΔEV −4.4pp, gate-annotated)
- Position: **TRIM/SHORT (unchanged)**

**Cause (both legs of the move are the ingest, not price):** (1) NAV +1.0% —
MB feeder 10-yr assessment 28.0→29.0 ($M, the only mark that moved since the
Apr-01 freeze; matches the pre-registered +0.92% prediction in
decisions/container_ingest_prep_2026-07-03.md). (2) EV −4.4pp — the 12M TC
refresh (feeder +15.9%, A3 intermediate 43,400→46,350, large +0.8%) lifts the
CURRENT-rate read, which RICHENS the cycle position; with ~99% of 2026 days
already contracted the strip lift barely flows near-term, while the
cycle-conditional terminal multiple and blend weights tighten — the designed
§2.3/§10 mechanics: better spot ≠ better value for a fully-covered name at an
elevated position. Direction and split cross-checked against the prep note's
prediction (rate story, not marks story).

**Decision:** Accept the move with the ingest; TRIM/SHORT stands. Watch item:
the A3 re-derivation (46,350) now weights the live combined fleets (72
intermediates, 41.4% of TEU in the 4,250 bucket) — re-derive at each monthly
re-capture if either validator's intermediate mix shifts.

---

## 2026-07-06T18:18:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.52
- Single-point FV: $2.21
- Scenario PW FV: $2.06 (EV -18.1%)
- NAV / share: $2.04
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +12.0pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.08 | Δsingle FV: +0.9% | Δscenario FV: -2.4% | ΔNAV: +1.0% | Δspread: +1.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:42:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:35:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T02:11:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:55:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:54:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:14:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:04:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:56:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:30:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:10:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.02 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.6pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:59:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: -0.02 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.6pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:58:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.44
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.7%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.7pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.02 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.6pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: -0.13 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.5pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.13 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +3.5pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.42
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -13.0%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +10.1pp (k_broker 1.09)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: -0.13 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.5pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.55
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.4%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.6pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: -0.07 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -1.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.62
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.6%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.3pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.01 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.61
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -19.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +15.1pp (k_broker 1.14)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: +0.07 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +1.8pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.1%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.1%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.1%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.1%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.19
- Scenario PW FV: $2.11 (EV -17.1%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.3pp (k_broker 1.12)
- Sector: containerships

**Material deltas since last run:**
- ⚑ single-point FV +10.1%
- ⚑ scenario PW FV +14.1%
- Δprice: no change | Δsingle FV: +10.1% | Δscenario FV: +14.1% | ΔNAV: no change | Δspread: -0.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $1.99
- Scenario PW FV: $1.85 (EV -27.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.4pp (k_broker 1.12)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22 — DRIFT ALERT (−9.4pp): §9.6 time-to-delivery discount rolled out (NOT a market move)

NAV/sh moved **$2.27 → $2.02** (−9.4pp gap) — cause is the §9.6 time-to-delivery
PV discount (proven on BRUT) rolled out to MPCC's 15 owned newbuilds, which
deliver ~q1-q13 out (0.25-3.25yr); each is now discounted by
`1.11^(−years_to_delivery)`, trimming ~$0.25/sh. The 51 on-water vessels are
unchanged. MPCC is APPROX (n/a SANITY); the company-implied NAV anchor is itself
stale. Position read unchanged-direction (TRIM/SHORT). The NB `years_to_delivery`
uses the deck's ~delivery-quarter estimates — refine with the issuer fleet list
at the Q2 report (2026-08-26). test_mpcc_gsl baseline re-pinned $2.27 → $2.02.

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $1.99
- Scenario PW FV: $1.85 (EV -27.3%)
- NAV / share: $2.02
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +13.4pp (k_broker 1.12)
- Sector: containerships

**Material deltas since last run:**
- ⚑ broker spread +8.1pp
- ⚑ NAV/sh -11.0%
- Δprice: no change | Δsingle FV: -6.6% | Δscenario FV: -5.6% | ΔNAV: -11.0% | Δspread: +8.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -22.9%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +5.3pp (k_broker 1.05)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.54
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -22.9%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +5.3pp (k_broker 1.05)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T21:55:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.78
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -29.6%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T18:49:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.78
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -29.6%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T14:28:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.78
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -29.6%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.78
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -29.6%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.11)
- Sector: containerships

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12 — ONBOARDED (1st containerships validator, §11.8) + §15.7 screen DECLINED + calibration-lock substitutes run

**Sources:** Q1 2026 financial report + earnings deck (mfn.se, 2026-05-27;
per-vessel employment table rows 1-68), Pareto quarterly review 2026-05-28
(HOLD, TP NOK 25, EV/EBITDA basis — on disk via linked-report harvest).

**Baseline (Jun-12, NOK 26.42 / $2.78):** NAV/sh $2.27 (fleet $1,636M, 51
on-water + 15 owned NB rows net of $633.7M commitments), PW FV $1.96,
EV −29.6% TRIM/SHORT. Gap to APPROX anchor (company-implied NAV ~NOK 25.5,
Jul-2025 vintage) −15.1%, n/a-APPROX. k_broker 1.11.

**Known input softness (refine at Q2 refresh, 2026-08-26):** cohort age
ESTIMATES (built years not in the deck; AS Anne widest); NB delivery
quarters ESTIMATED from the 1/5/9/2 schedule; Uthalden JV (Maike/Marthe)
excluded both sides; net interest will rise with NB drawdowns.

**§15.7 screen — Step 0 gate FAILS (multi-year P/NAV ran 0.5-0.9× through
2023-25), Step 1 DECLINED, no haircut:**
1. Control/share structure: no controlling block; Oslo free float. CLEAN.
2. Related-party fee load: MPC Capital ship-management fees ~$10M/yr on
   ~$1.75bn GAV ≈ 0.6%/yr — CAPT-zone (near market), nowhere near CMDB's 4%.
3. Distribution: ~50%-of-adjusted-profit recurring dividend, 17+ consecutive
   quarters — channel WIDE OPEN (the §15 doctrine's strongest decliner).
4. Natural experiment: GSL (different sponsor, same sector) trades at a
   comparable-or-deeper discount → sector-level marks question, not
   governance.
5. External anchor: none exists (§11.8.2).
6. Charter-counterparty relatedness (dimension 6): charterers are unrelated
   liners (Maersk/MSC/Hapag/COSCO/ZIM...). CLEAN.
**Tripwires:** MPC Capital fee escalation above ~1%/yr GAV; payout
walk-back below ~40% adj. profit; Uthalden JV expansion or cross-dealing
(watch any vessel transfers at non-market marks); event-driven
distributions replacing the recurring anchor.

**Calibration lock (§11.8.7): N/A-BY-CONSTRUCTION, machine-confirmed**
(`reconcile --calibration-lock containerships`: "No Pareto-anchored names").
Substitutes run:
1. PRIMARY — issuer-S&P print cross-check on MPCC's three disclosed sales:
   Felicia (1,300/2006) tool ~$12.8M vs $12.3M sold (+4%); Alva (2,000/2008)
   tool ~$15.2M vs $22.3M (−32%); Clementina (2,800/2006) tool ~$16.2M vs
   $24.0M (−33%). Read: the tool's old-age marks run 0-30%+ BELOW realized
   boom prints — the DELIBERATE §11.8.5(b) anti-boom-import choice made
   visible. Direction conservative; spread vs prints is the documented
   trade-off, not a fitting error. (Prints NOT promoted — §11.8.8,
   charter-attached.)
2. VIE APPROX gap: −15.1% vs the stale company-implied NAV. Directional.
3. Fitting sanity (circular): curve reproduces the MB Apr-01 assessments
   it was fit to. PASS.

**Overlay ledger:** MPCC §11.8.5(b) marks-tilt row ACTIVE (founding
container entry) — old-age boom-flat bias deliberately not imported;
retire on fresh MB assessment set.

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $2.78
- Single-point FV: $2.13
- Scenario PW FV: $1.96 (EV -29.6%)
- NAV / share: $2.27
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +11.4pp (k_broker 1.11)
- Sector: containerships

**Status:** _First snapshot — no prior state to compare._

**Decision:** Onboarding baseline — see the onboarding entry above. TRIM at
the conservative §11.8.5(b) marks; the company-implied NAV and Pareto's
EV/EBITDA HOLD both sit ABOVE the tool. Calibration counter starts here.

---

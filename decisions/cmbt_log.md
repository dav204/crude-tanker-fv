# CMBT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-07-02T23:59:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.19
- Scenario PW FV: $13.34 (EV -5.0%)
- NAV / share: $15.87
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +18.2pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.51 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:58:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.56
- Single-point FV: $15.19
- Scenario PW FV: $13.34 (EV -8.4%)
- NAV / share: $15.87
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +21.4pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.51 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +3.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.19
- Scenario PW FV: $13.34 (EV -5.0%)
- NAV / share: $15.87
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +18.2pp (k_broker 1.11)
- Sector: crude

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → TRIM/SHORT (overvalued)
- ⚑ scenario PW FV -14.3%
- Δprice: no change | Δsingle FV: -0.5% | Δscenario FV: -14.3% | ΔNAV: no change | Δspread: -1.3pp

**Decision (2026-07-02, vintage — band flip eyeballed):** ACCEPT BUY→TRIM/SHORT at face value but READ AS HOLD-BAND STRADDLE: EV −5.05%, five basis points past the −5% line, and the final push was the −$0.39 dry-bulk RATES nudge (2-Jul FFA promotion), not a judgment layer. Decomposition: $16.07→$13.34 = C-3 fix −$0.51 / crude+leg −$1.83 / rates −$0.39 (proposal §10). Post-stand-down vintage (2026-07-02): crude 0.10/0.20/0.45/0.25 + MoU-ineffective leg recalibrated (0.15-flare mixture) + product v2-restore + LNG v3-restore + F-5 rate refresh. Full attribution: decisions/crude_reweight_proposal_2026-07-02.md §10/§15 + the 2026-07-02 review sign-off chain. ΔNAV 0.0% — scenario/rate layer only. W-frag ⚠ already flags the name; treat the label as boundary noise until it clears ±2pp of the line. No trade.

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.26
- Scenario PW FV: $15.56 (EV +10.7%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.26
- Scenario PW FV: $15.56 (EV +10.7%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -3.2% | ΔNAV: no change | Δspread: -0.4pp

**Decision (2026-07-02, review C-3 — multi-sleeve aggregation fix):** ACCEPT the −3.6pp EV /
−3.2% scenario-FV correction (PW FV $16.07→$15.56, stays BUY). This is a BUG FIX, not a market
or weight move: the aggregator paired sleeve scenario ladders by index and applied the CRUDE
sleeve's probability weights to ALL sleeves — CMBT's dry-bulk sleeve (72.7% of vessel value)
was being probability-weighted by the Hormuz state, inflating it while crude weights sat
war-heavy (0.25 escalation / 0.45 pre-MoU). Fixed to per-sleeve sector weights (cross-sector
independence; `pipeline._aggregate_multi_sleeve_report`, regression-tested — a 100% dry-bulk
sleeve is now invariant under a crude-only reweight). ΔNAV 0.0% — the fix is scenario-layer
only. See `decisions/crude_reweight_proposal_2026-07-02.md` §14 and the 2026-07-02 review
addendum. NOTE: the pending post-stand-down vintage (crude/product/LNG, awaiting owner
sign-off) takes CMBT further, to ~−2.3% HOLD — the two effects are deliberately separate
layers for attribution. No trade.

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.4%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.9pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.4%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.9pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.06 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.06 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.05
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.4%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.9pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.06 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.99
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.9%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +19.5pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.09 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.6pp

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.08
- Single-point FV: $15.26
- Scenario PW FV: $16.07 (EV +14.1%)
- NAV / share: $15.87
- Position: **BUY (undervalued)**
- Broker spread: +20.1pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.02 | Δsingle FV: +2.2% | Δscenario FV: +2.4% | ΔNAV: +3.1% | Δspread: -3.2pp

**Decision:** Amendment B — crude age-0 reverted to xclusiv Resale (dry-bulk holds its Thread-1 Resale levels). CMBT NAV +3.0% net (crude sleeve up; dry-bulk unchanged).

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.93
- Scenario PW FV: $15.69 (EV +11.3%)
- NAV / share: $15.40
- Position: **BUY (undervalued)**
- Broker spread: +23.3pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +1.7% | Δscenario FV: +0.3% | ΔNAV: +0.9% | Δspread: -0.9pp

**Decision:** _[pending annotation]_

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.68
- Scenario PW FV: $15.64 (EV +10.9%)
- NAV / share: $15.27
- Position: **BUY (undervalued)**
- Broker spread: +24.2pp (k_broker 1.14)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.1% | Δscenario FV: -0.1% | ΔNAV: +0.1% | Δspread: -0.1pp

**Decision: NMax dwt-scaling landed — CMBT ~FLAT (+0.1%), a correctness fix, NOT a
gap-closer (METHODOLOGY §11.7.x).** "Splitting Newcastlemax properly" was implemented as
**dwt-scaling** the dry-bulk value curves (owner decision: value ∝ dwt, no separate
class — NMax and Cape trade at the same $/dwt, so the difference is pure size). For CMBT
(38 NMax + 37 standard Capesize): the young NMax rise (now ~$85-88M at age 0-2, fixing
the too-low newbuild anchor) is OFFSET by the standard Capesize correcting DOWN to their
own transaction level — net NAV $15.26→$15.27, k_broker still 1.14, gap −24.2%.
**This RETRACTS the 2026-06-27T00:31 entry's claim that "splitting Newcastlemax from
Cape raises the dry-bulk sleeve toward Pareto."** The measurement disproves it: the −24%
gap is a *uniform* in-band mark conservatism amplified by ~55% leverage, not an NMax-
specific undervaluation. The split's real value was **cross-name accuracy** — the
standard-Capesize/Supramax-heavy names corrected down to transaction-grounded marks
(GNK −6.2%, CMDB −3.6%) while the NMax-heavy names stayed ~flat (CMBT +0.1%, SBLK +1.3%).
Baseline re-ratified.

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.10
- Single-point FV: $14.69
- Scenario PW FV: $15.66 (EV +11.0%)
- NAV / share: $15.26
- Position: **BUY (undervalued)**
- Broker spread: +24.3pp (k_broker 1.14)
- Sector: crude

**Material deltas since last run:**
- ⚑ position TRIM/SHORT (overvalued) → BUY (undervalued)
- ⚑ broker spread +10.3pp
- Δprice: -1.86 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +10.3pp

**Decision: CORRECTION — CMBT is Pareto-anchored, NOT APPROX (supersedes the
2026-06-26 onboarding baseline below).** The onboarding read "no clean broker NAV →
APPROX" was WRONG: Pareto publishes a real, monthly-tracked CMB.TECH P/NAV + NAV/sh
in the Shipping Daily. The 11-Jun-2026 daily prints CMB.TECH at **price $14.90,
P/NAV 0.74x, fwd P/E 9.7x**, with NAV pegged at **~$20/sh (NOK 189)** and the prose
"sub-0.75x NAV, the lowest priced name in our drybulk coverage." Corrected the
watchlist row to that same-vintage Pareto pairing and removed CMBT from
`APPROX_PNAV_TICKERS`. The two drift drivers are both **accepted, not bugs**:
(1) the −1.86 price move is the watchlist anchor rebasing from a stale Yahoo $15.96
(2026-06-24) to the Pareto $14.90 vintage; (2) the +10.3pp broker-spread widening is
the consensus_pnav fix (0.90 placeholder → 0.74 real Pareto), moving broker NAV
$17.73 → $20.14.

- **Corrected reconciliation BASELINE:** tool NAV **$15.26** vs Pareto broker NAV
  **$20.14** (= 14.90/0.74) → **gap −24.2%, SANITY = OK** (a REAL Pareto gate now).
  At the live $14.10 close, scenario FV $15.66 → **EV +11.0%, BUY**. k_broker **1.14**
  is **INSIDE the validated pure-play band (1.05-1.25)**.
- **§6 thesis for the −24% spread — mark-validated-with-a-NMax-caveat, not mark-driven:**
  k_broker 1.14 says the per-vessel mark gap vs Pareto is the *normal ~12-14% broker
  premium*, not a gross disagreement; the larger equity-NAV gap is **leverage
  amplification** (CMBT runs ~$5.2bn debt / ~55% LTV per Pareto, so a within-band
  vessel-mark premium translates to a big equity swing). The residual mark
  conservatism is the **§11.7.1 Cape-class collapse** — the single "Cape" curve does
  not capture the modern-Newcastlemax premium, and CMBT carries the **largest NMax
  book on the watchlist (38, many 2024-26 built)**, so it exposes that limitation more
  than any other name. Splitting Newcastlemax from Cape is the highest-value refinement
  for CMBT (raises the dry-bulk sleeve toward Pareto). The correction also RESOLVED the
  onboarding's apparent tool↔Pareto disagreement: at the live price both now read CMBT
  cheap (tool BUY +11% / Pareto "deep value 0.74x"), directionally aligned.
- **Baseline re-ratified** at the corrected −24.2% gap (the −13.9% APPROX figure below
  is superseded). Pareto's monthly P/NAV trail (0.62x Dec-25 → 0.77x May → 0.74x
  Jun-26) is the live anchor going forward; refresh it each report cycle.

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.96
- Single-point FV: $14.69
- Scenario PW FV: $15.66 (EV -1.9%)
- NAV / share: $15.26
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.0pp (k_broker 1.09)
- Sector: crude

**Status:** _First snapshot — onboarding baseline._

**Decision: ONBOARDED 2026-06-26 — first crude+dry_bulk+containerships MULTI-SLEEVE
hybrid (METHODOLOGY §11.9).** CMB.TECH (ex-Euronav) is a five-segment conglomerate
after the 20-Aug-2025 Golden Ocean merger (+95.95M shares → 290.17M ex-treasury);
dry bulk is **72% of vessel value**, crude 24%, container 3%. Build record +
sourced fact pack in `outputs/cmbt_multisleeve_methodology_2026-06-26.md` +
`outputs/cmbt_onboarding/`.

- **Architecture:** crude + dry_bulk + containerships on-curve (the engine's
  carve-out + aggregator were generalised to arbitrary sectors — `sector_carve_out`
  + `_aggregate_multi_sleeve_report` + `MULTI_SLEEVE_TICKERS`; a latent bug where
  dry_bulk/container classes fell through to the crude sleeve was fixed). Off-curve
  at the balance-sheet level: 2 FSO (shuttle_contracted_book $100M APPROX), 8
  chemical + 47 owned Windcat at segment book + equity-JV stakes + 3 HFS at agreed
  price (working_capital_net $912M), the multi-segment newbuild book
  (newbuild_advances_paid $760M, conservative net = advances). Goodwill ($190.7M) excluded.
- **§15 governance — DECLINED the haircut** (`governance_discount_pct = 0`), carry
  with tripwires. Fee load immaterial (~0.18-0.21% of GAV, cost-plus); distributions
  pro-minority; the 2021-24 Euronav-saga natural experiment shows equal-price
  treatment ($18.43 mandatory bid, court-upheld). Strategy/agency-drift risk
  (hydrogen/ammonia capex) priced through conservative NB/off-curve marks, not a
  multiplier. Tripwires: GOGL Bermuda appraisal / FourWorld Antwerp outcomes; fee
  creep off cost-plus; distribution backsliding < ~50%; multi-year median P/NAV < 0.85
  alongside any of those; loss of the independent Audit-Committee majority.
- **Reconciliation BASELINE (first-run):** tool NAV **$15.26** vs broker NAV
  **$17.73** (APPROX, consensus_pnav 0.90 anchored to the "discount-to-NAV"
  narrative) → **gap −13.9%, SANITY = n/a** (APPROX cohort; book is depreciated
  cost and understates, so SANITY is a self-consistency read, not a Pareto anchor).
  Scenario PW FV $15.66 vs price $15.96 → **EV −1.9%, TRIM/SHORT (marginally rich)**.
  This gap is the baseline for future drift detection. Drift gate re-ratified incl.
  CMBT @ 357c74e; 20 existing names +0.0pp (the engine generalisation is byte-identical
  for INSW/TEN).
- **Pareto name-sweep (71 mentions) — independent NAV cross-checks (no clean current
  P/NAV, hence APPROX):** the GOGL merger was struck **"NAV-for-NAV at $15.23/share
  for CMB"** (Pareto 2025-04-23) — the tool's $15.26 NAV lands essentially on it
  (different vintage/entity, but a strong sanity confirmation). Pareto flagged
  **"CMB.TECH at sub-0.7x NAV"** (2025-10-24) and the tanker peer group at ~0.81x —
  i.e. CMBT genuinely trades at a DISCOUNT to broker NAV, so the 0.90 consensus_pnav
  (broker NAV $17.73) is, if anything, conservative on the discount. The tool reads
  CMBT as roughly fairly-valued (the strip pulls FV to ≈ price) while the sell-side
  sees NAV upside — a documented mark-driven divergence (the tool is more conservative
  on the dry-bulk-heavy marks). Distilled prints in `outputs/pareto_mentions_cmbt.md`.
- **Open items / refinements (Q3 / next refresh):** yard-quality discount (§9.4) not
  applied to the China-heavy dry-bulk book (v1 = "without discount" leg); scrubber
  fitment undisclosed (default false); FSO owned-vs-JV status (zero shuttle_contracted_book
  if the FSOs sit in the equity-JV line); G&A / interest are Q1-annualised estimates;
  chemical/Windcat segment books are Dec-2025 vintage; consensus_fwd_pe APPROX (Q1 EPS
  distorted by ~$290M one-off vessel-sale gains).

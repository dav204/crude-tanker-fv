# CAPT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-07-03T01:14:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:04:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:56:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:30:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:10:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +5.4pp
- Δprice: +0.79 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +5.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:59:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -19.4%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +18.5pp (k_broker 1.11)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -5.4pp
- Δprice: -0.79 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -5.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:58:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.28
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -24.2%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +23.9pp (k_broker 1.15)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +5.4pp
- Δprice: +0.79 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +5.4pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $10.07 (EV -19.4%)
- NAV / share: $15.49
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +18.5pp (k_broker 1.11)
- Sector: crude

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → TRIM/SHORT (overvalued)
- ⚑ scenario PW FV -41.3%
- ⚑ broker spread -5.3pp
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -41.3% | ΔNAV: no change | Δspread: -5.3pp

**Decision (2026-07-02, vintage — band flip eyeballed):** ACCEPT BUY→TRIM/SHORT (EV +37.4%→−19.4%). Post-stand-down vintage (2026-07-02): crude 0.10/0.20/0.45/0.25 + MoU-ineffective leg recalibrated (0.15-flare mixture) + product v2-restore + LNG v3-restore + F-5 rate refresh. Full attribution: decisions/crude_reweight_proposal_2026-07-02.md §10/§15 + the 2026-07-02 review sign-off chain. ΔNAV 0.0% — scenario/rate layer only. CAPT is one of the TWO genuine war-premium false-BUYs (with BRUT): a newbuild-heavy torque book whose modeled margin was concentrated in the escalation/pre-MoU legs. GOVERNED-WIDE·newbuild-heavy; the crude TRIM read is cycle-adjacent — resolve as hulls deliver. No trade.

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +37.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +23.8pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +37.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +23.8pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +37.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +23.8pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +37.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +23.8pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.09 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.09 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.49
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +37.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +23.8pp (k_broker 1.11)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.09 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.9pp

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.58
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +36.4%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +24.7pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: -0.15 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -1.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +34.8%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +26.0pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +34.8%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +26.0pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +34.8%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +26.0pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +34.8%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +26.0pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.03
- Scenario PW FV: $17.16 (EV +34.8%)
- NAV / share: $15.49
- Position: **BUY (undervalued)**
- Broker spread: +26.0pp (k_broker 1.13)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.6% | Δscenario FV: -0.6% | ΔNAV: -0.6% | Δspread: +0.7pp

**Decision:** CAPT scrubber correction COMPLETE — 18/30 scrubber-fitted (NOT a market move). The
blanket scrubber=true was over-broad: verified vs CAPT's own sources (Pareto initiation 2026-04-20
per-vessel ledger + Euronext Information Doc §7.3.2 + Q1 release) = **18/30 (~60%)** — VLCC 6/12,
Suezmax 10/10, Aframax 0/4, LR2 2/4. Two slices: the **Aframax 0/4** landed via PR #3 (AFRA_2018,
merged), and this run wires the **VLCC/LR2** slice — VLCC_nb_2027 7→3+4, VLCC_nb_2028 4→2+2,
LR2_2026 2→0 (6 VLCC + 2 LR2 lose the fabricated scrubber premium). **NAV impact is basis-dependent:**
on the **anchored (headline) basis** the combined CAPT move is **−0.63%** ($15.59→$15.49); the
Aframax slice is +0.08% anchored / −0.27% un-anchored (anchoring steepens the Aframax 10yr leg
$68M→$61M, flipping that slice's sign), VLCC/LR2 −0.71% on both. Reconcile SANITY **OK** (−14.9% vs
broker $18.21). Process fix recorded: headline NAV must be read on the anchored basis (raw
`compute_nav` is un-anchored). CAPT cleared the scrubber-verification queue (BRUT/CAPT/FRO all
verified); registry CAPT→`scrubber: mixed`, NB count 13. Re-ratifying the combined move.

---

## 2026-06-30 — Aframax rows corrected: build years (2018–19, not 3× age-10 + 1× age-0) and scrubber (false, not true)

**What was wrong:** the manifest split the 4 Aframax into `AFRA_2016` (age 10,
count 3) + `AFRA_2026` (age 0, count 1, "fresh Mar-2026 delivery"), all
`scrubber: true`. Both the age split and the scrubber flag were wrong.

**Verified against two primary sources:**
- **Issuer Q1-2026 earnings release, sailing-fleet table p6**
  (`inputs/research_issuer/2026-Q1_capt_earnings_release.pdf`): all 4 Aframax are
  2018–2019 HD Hyundai Samho sisters — Alimedon (Jul-2018), Andreios (Oct-2018),
  Areios (Nov-2018), Ameinon (Apr-2019). **There is no 2026-built Aframax.**
  Per-vessel prose marks Alimedon "Dual Fuel LNG capable" with no scrubber
  (contrast Alkinoos "Dual Fuel LNG capable **and** scrubber-fitted"); the p5 fleet
  note "five scrubber-fitted, four LNG dual-fuel" maps the four DF-only vessels to
  exactly these Aframax.
- **Pareto initiation per-vessel fleet table, p2**
  (`inputs/research_pareto_other/linked/2026-04-20_linked-488376.pdf`):
  Scrubber = No on all four.

**Fix:** collapsed to one cohort — `AFRA_2018`, class Aframax, count 4, **age 7.4**,
**scrubber: false**, eco: true, **years_to_delivery 0.0** (all delivered / on the
water — no §9.6 [time-to-delivery PV] discount). Mean build ≈ late-Oct-2018 → 7.4 yr
as of the Mar-31-2026 snapshot; the age curve is piecewise-linear over the [5,10]-yr
anchors, so a single count-4 cohort at 7.4 reproduces the exact aggregate value of the
four individual ages (6.9–7.75). (Pareto's review class-table cited avg 7.8; the issuer
per-vessel build dates give 7.4 — the issuer governs.)

**Model impact — small, and basis-dependent (corrected per PR #3 review, which
caught a sign error in the first draft of this entry):** the NAV move depends on
which curve set you measure, and the two disagree in sign — both verified by direct
`compute_nav` (precise, not cent-rounded):

| Basis | OLD (pre) | NEW (post) | Δ/sh | Δ% |
|---|--:|--:|--:|--:|
| **Transaction-anchored** (headline — the decision-log "NAV / share" + reconcile tool-NAV; `use_transaction_anchored` default-on) | $15.5919 | $15.6042 | **+$0.012** | **+0.08%** |
| **Un-anchored** (raw broker-resale curves; the diagnostic alternative) | $15.7616 | $15.7190 | **−$0.043** | **−0.27%** |

The first draft reported only **+$0.01 / +0.06%** (the anchored headline) with a
muddled "nearly offsets" decomposition — wrong on the un-anchored basis, where the
move is **−0.27%**. The reviewer's base-NAV flag ($15.59 vs $15.762) is exactly this
anchored-vs-unanchored split, not stale data. Un-anchored Aframax decomposition (ties
to −$5.70M fleet, −$0.043/sh): the old `AFRA_2026` age-0 newbuild ($98.1M) re-ages to
7.4 (**−$20.7M**), the three old age-10 vessels lift to 7.4 (**+$18.0M**), so the **age
effect is −$1.7M** (not a wash), and **scrubber removal is −$4.0M** (4 × $1.0M Aframax
premium) → **−$5.7M total**. The sign flips on the anchored curve because anchoring
steepens the Aframax mid-age leg (10-yr benchmark $68.0M → $61.0M): the three age-10
vessels are valued low there, so re-aging them to 7.4 lifts them **+$26.1M**, outweighing
the newbuild's −$24.4M → **+$1.65M** (positive).

Unchanged on both bases: single-point FV $16.13, scenario PW FV ≈$17.27, **EV +35.6%**,
band **BUY → BUY**, **k_broker 1.12**, broker gap −14.3%, **SANITY OK**. Full pytest
**416 passed**; the drift gate (which reads the anchored headline) is green for this slice
in isolation (+0.08%, sub-2pp, no band flip).

**Re-ratify (corrected):** NOT "no re-ratify." This Aframax row is one slice of a wider
CAPT scrubber correction — the VLCC (6-of-12) and LR2 (2-of-4) rows are also over-broad
(CAPT is **18/30 ≈ 60% scrubber-fitted** per the Pareto per-vessel ledger) and are being
corrected separately on `main` (≈ −0.71%). Combined, CAPT moves **≈ −1%** (un-anchored),
which warrants a re-ratify — to be done **once, after all slices land**, not per-slice.

**Out-of-scope observation for the Q2 refresh (NOT actioned):** the issuer p6 delivery
dates show only 1 of the 4 Aframax (Alimedon, delivered to CAPT Mar-9) was on the water
at the Mar-31-2026 quarter-end; Andreios / Areios / Ameinon transferred Apr-8 / 15 / 16.
The manifest's `fleet_summary: on_water_at_quarter_end: 9` (Pareto's count, as of a later
date) appears to overstate the Mar-31 on-water tally — the issuer reports 6 Q1 deliveries.
The `fleet_schedule` [4,4,…] from q3-2026 is unaffected (all 4 on the water well before
Q3). Left as-is — fleet-summary counts are outside this task's scope; resolve at the Q2
refresh.

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.13
- Scenario PW FV: $17.26 (EV +35.6%)
- NAV / share: $15.59
- Position: **BUY (undervalued)**
- Broker spread: +25.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.13
- Scenario PW FV: $17.26 (EV +35.6%)
- NAV / share: $15.59
- Position: **BUY (undervalued)**
- Broker spread: +25.3pp (k_broker 1.12)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.73
- Single-point FV: $16.13
- Scenario PW FV: $17.26 (EV +35.6%)
- NAV / share: $15.59
- Position: **BUY (undervalued)**
- Broker spread: +25.3pp (k_broker 1.12)
- Sector: crude

**Material deltas since last run:**
- ⚑ single-point FV +28.1%
- ⚑ scenario PW FV +26.7%
- ⚑ broker spread -30.6pp
- ⚑ NAV/sh +34.6%
- Δprice: -0.06 | Δsingle FV: +28.1% | Δscenario FV: +26.7% | ΔNAV: +34.6% | Δspread: -30.6pp

**Decision:** Amendment B — crude age-0 reverted to xclusiv Resale (VLCC 175, Suezmax 114.3). CAPT NAV $11.58->$15.59 (+34.6%, a touch above pre-Thread-1 $15.03 because xclusiv Suezmax Resale 114.3 > the old 108 — read straight off the curve). Provisional flag clears (reverted).

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $12.59
- Scenario PW FV: $13.62 (EV +6.5%)
- NAV / share: $11.58
- Position: **BUY (undervalued)**
- Broker spread: +55.9pp (k_broker 1.31)
- Sector: crude

**Material deltas since last run:**
- ⚑ single-point FV -19.6%
- ⚑ scenario PW FV -18.8%
- ⚑ broker spread +25.9pp
- ⚑ NAV/sh -23.0%
- Δprice: no change | Δsingle FV: -19.6% | Δscenario FV: -18.8% | ΔNAV: -23.0% | Δspread: +25.9pp

**Decision:** Thread 1 basis correction (not a market move). VLCC $175M->$145M and Suezmax $108M->$95M age-0 marks corrected to dated prompt-resale. CAPT carries 21/30 newbuild crude at age-0 delivered-market (§9.6), so NAV -22.9%. Pre-registered direction (PRE_REGISTRATION_NAV_RESALE_ANCHOR.md). Owner-approved 2026-06-29; re-ratified with crude resale LEVELS flagged PROVISIONAL. **LEVEL-PROVISIONAL:** the $145M/$95M age-0 levels are validated for depreciation slope (guard #2), NOT level (A1.5 open). CAPT is newbuild-heavy, so its −22.9% is slope-validated, level-provisional pending a dated current crude resale source (Thread 1B).

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +31.1%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +30.0pp (k_broker 1.15)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -6.7pp
- Δprice: -0.82 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -6.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.61
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +23.2%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +36.7pp (k_broker 1.19)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.37 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.9pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +26.7%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +33.8pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.66
- Scenario PW FV: $16.77 (EV +26.7%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +33.8pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.65
- Scenario PW FV: $16.77 (EV +26.7%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +33.8pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.65
- Scenario PW FV: $16.77 (EV +26.7%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +33.8pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +2.6% | Δscenario FV: +3.5% | ΔNAV: no change | Δspread: -0.9pp

**Decision:** _[pending annotation]_

---

## 2026-06-22 — CAPT NB cohorts refined to the exact Q1-release delivery dates (estimate confirmed)

Replaced the rollout's estimated cohorts (2/6/4 VLCC @ 0.4/1.2/2.0; flat 0.8 on
the 8 Suezmax NB) with the per-vessel Q1-release dates, `years_to_delivery` from
the Mar-31-2026 snapshot:
- **VLCC:** 1 delivered (Aristotelis II, Feb-10-26 → ytd 0) / 7 in 2027 (Alterego,
  Amfitrion, Alexandros Apr, Apollonas May, Anemos Sep, Akadimos Nov + 1 → ~1.25) /
  4 in 2028 (Amyntas Jan, Arkesios Feb, Atromitos Apr, Aktor Jun → ~2.0).
- **Suezmax NB:** 6 near-term 2026 (Ataraktos/Aristoklis Apr → Amor Nov, ~0.3) /
  2 in 2028 (Akeraios Feb, Alkaios Mar, ~1.9).

NAV/sh $15.05 → **$15.03** (−0.1pp, *stable*) — the estimate was already accurate,
so this is a provenance/precision upgrade, not a re-rate. CAPT's −17.5% divergence
to Pareto and BUY (EV +22.4%) stand. The cohort timings are now issuer-dated.

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.25
- Scenario PW FV: $16.20 (EV +22.4%)
- NAV / share: $15.03
- Position: **BUY (undervalued)**
- Broker spread: +34.7pp (k_broker 1.17)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: no change | ΔNAV: -0.1% | Δspread: +0.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-22 — DRIFT ALERT (−14.8pp): §9.6 time-to-delivery discount rolled out (NOT a market move)

The gap to Pareto moved **−2.6% → −17.3%** (NAV/sh $17.74 → $15.05) — a drift
alert, but the cause is a **methodology change, not the tape**: the §9.6
time-to-delivery PV discount (proven on BRUT) was rolled out to CAPT's newbuilds.
CAPT's 12 VLCC NB (split 2026/2027/2028 cohorts, avg ~1.4yr) + 8 Suezmax NB
(~0.8yr) are now PV-discounted by `1.11^(−years_to_delivery)`; the Mar-2026-
delivered Suez/Afra/LR2 rows stay on-water (no discount). SANITY still **OK**.

**Observation worth recording:** the discount makes the tool **more conservative
on NB timing than Pareto**. For BRUT (pure-NB) this CLOSED the gap (Pareto was
already discounting heavily, 0.75×); for CAPT it OPENED one (−2.6% → −17.3%) —
i.e. Pareto appears to book CAPT's cheaply-contracted NBs closer to delivered
value, while the tool now haircuts them for the wait. So CAPT shifts from a
tight reconcile (k 1.04) to a documented **−17% methodological divergence** (the
tool's more conservative NB-timing view) — SANITY-OK, a call not a bug. Position
held **BUY** (NAV $15.05 still > price ~$13.24). Owner may reconsider the cohort
`years_to_delivery` against CAPT's actual Q1-release delivery dates at the Q2
refresh (the cohort split here is an estimate).

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $15.24
- Scenario PW FV: $16.20 (EV +22.4%)
- NAV / share: $15.05
- Position: **BUY (undervalued)**
- Broker spread: +34.6pp (k_broker 1.17)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +20.4pp
- ⚑ NAV/sh -15.2%
- Δprice: no change | Δsingle FV: -8.8% | Δscenario FV: -8.4% | ΔNAV: -15.2% | Δspread: +20.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +33.5%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +14.2pp (k_broker 1.07)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $13.24
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +33.5%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +14.2pp (k_broker 1.07)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22 — Q1 PRIMARY-SOURCE CONFIRMATION DONE — build validated, broker-sourced caveat CLEARED

Pulled CAPT's issuer Q1 2026 earnings release (the deferred primary source) from
the Oslo release and reconciled it against the Pareto-derived balance sheet.
Archived: `inputs/research_issuer/2026-Q1_capt_earnings_release.pdf`. **Every
material line matches:**

| Line | YAML (Pareto) | Issuer Q1 | |
|---|--:|--:|---|
| Cash | $405.0M | $404.9M unrestricted (+$3.0M restricted = $407.9M) | ✓ |
| Total IB debt | $217.0M | $217.0M (205.1 + 11.9); **net CASH $189.5M** | ✓ |
| Diluted shares | 133.70M | 133,692,593 (131.05M Mar-31 + over-allotment) | ✓ |
| Leases | 0 | none (NB financing is mortgage debt) | ✓ |
| Preferred | 0 | none issued | ✓ |
| Fleet | 30 (12/10/8) | 30: 12 VLCC / 10 Suez / 8 Afra-LR2; 12 sailing + 18 NB | ✓ |
| NB capex | $1,880M | per-vessel CAPEX table, sums ≈$1.88-1.9bn | ✓≈ |

**The "broker-built, not issuer-confirmed" caveat (the biggest CAPT caveat) is
CLEARED.** No valuation change — numbers held (confirmed accurate); only the YAML
provenance comment updated, $0 NAV move.

**New from the primary (not in the Pareto proxy):**
- **$9.0M dividend declared to Capital Maritime** alongside the NOK 0.50/sh common
  Q1 dividend — a sponsor-directed distribution; note for §15 (distribution
  behaviour). Likely a pre-IPO accrued/parent dividend — verify nature at Q2.
- **Net CASH $189.5M** (cash $407.9M vs $218.4M debt) + **$314.1M secured undrawn
  financing** — strong liquidity into the NB programme (eases tripwire 6, though
  the Jun-16 sponsor VLCC $111.8M upfront still lands against it).
- **Full per-vessel NB CAPEX schedule** (vessels 1-21, staged to 2028) now on file
  — supersedes the Pareto $1,880M aggregate; rebuild the NB schedule precisely at
  Q2. **Optional Fleet** detailed: 11 VLCC (Hengli) + 2 Suezmax = the 13 options.
- M/T Aristotelis II (VLCC) fixed a 1-yr TC at **$100,000/day**; Q2 ~71% of spot
  days booked at **$153,059/day** — supports the forward strip.
- Total shareholders' equity $1,609.8M (book ~$12.04/sh vs tool NAV $17.74 — the
  NB-uplift gap, as designed).

**Open reconciliation item (Q2 nicety):** `working_capital_net` $13M (Pareto
bridge) vs issuer prepayments $1.1M — ~$0.09/sh, immaterial; resolve to the issuer
line items at the Q2 refresh, along with the exact NB-capex sum.

**Decision:** Q1 inputs ratified as issuer-confirmed; CAPT's BUY (+33.5% EV at live
price) no longer carries the broker-sourced-inputs caveat. Remaining live caveats
unchanged — Marinakis control + the six §15 tripwires; the Jun-16 sponsor VLCC deal
funding still to verify; NOK/FX.

---

## 2026-06-21 — Sponsor VLCC asset transfer (from news-pull) — §15 tripwires 4/6 (and 1, conditional) REVIEWED; no haircut change

**Source:** 2026-06-21 news-pull web sweep — Splash247, 2026-06-16
(https://splash247.com/capital-tankers-adds-three-vlcc-newbuilds-from-marinakis-affiliate/).
**NOT issuer-confirmed** — verify against the CAPT primary filing at the Q2
refresh before any input action.

**Event:** Capital Tankers acquired **3× VLCC newbuild contracts from Capital
Maritime** (the Marinakis sponsor affiliate) at **$122M each** (Hengli, deliveries
Sep–Nov 2027), with **$111.8M upfront due by Jun-30-2026**. Reported indicative
appraisals ~$150M each → ~$82M of stated value accretion to CAPT. CAPT separately
retains 13 unexercised options (11 VLCC / 2 Suezmax) at original contract prices
through Dec-31-2026.

**§15 mapping (the tripwire list below):**
- **Tripwire 4 (sponsor merger/reshuffle) — FIRES as a related-party asset
  transfer**, the sponsor→listco shuffle this group structure enables. Per the §15
  doctrine (a haircut prices EVIDENCE of realisation impairment; the mechanism only
  generates tripwires), *direction* matters: the stated terms ($122M paid vs ~$150M
  appraised) are **accretive to CAPT minorities** — a sponsor selling below appraisal
  cuts AGAINST a value-extraction haircut, not for one. **§15 read stays 0%** on the
  current information.
- **Tripwire 6 (Q1-2027 NB-debt landing) — pressure.** The $111.8M upfront (due
  Jun-30) plus three more VLCCs deepen the ~$385M NB-debt requirement; the liquidity
  tripwire sits closer to the surface. Confirm financing at Q2.
- **Tripwire 1 (option-funding dilution) — CONDITIONAL.** Not an option exercise, but
  the same risk: if the $111.8M upfront is funded by equity issued below NAV with no
  pre-emptive rights, T1 fires. **Funding method is the key unknown — verify it.**

**Decision (documented, NOT actioned):** No §15 haircut change (the transfer reads
accretive, not extractive, on stated terms). No input edit — the 3 VLCCs are a
fleet / NB-schedule change that enters via the Q2 refresh from the issuer report,
not from a trade-press line (CAPT primary-source confirmation was already deferred
to Q2). **Q2 verification asks:** (1) appraisal basis + actual transfer terms;
(2) funding method for the $111.8M (equity-below-NAV → T1 fires); (3) updated
NB-debt schedule (T6). Watchlist untouched (human-only promotion).

---

## 2026-06-12T21:55:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T18:49:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T14:28:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T02:42:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T00:38:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.79
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.2%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.8pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: +0.05 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +0.5pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T23:54:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.74
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.8%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.3pp (k_broker 1.04)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-11T15:40:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $12.74
- Single-point FV: $16.71
- Scenario PW FV: $17.68 (EV +38.8%)
- NAV / share: $17.74
- Position: **BUY (undervalued)**
- Broker spread: +9.3pp (k_broker 1.04)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _Onboarding baseline — see the 2026-06-11 entry below._

---

## 2026-06-11 (later still) — listing venue & liquidity: assessed, NO haircut

Owner asked whether Oslo-vs-US liquidity needs pricing in. Measured:
~218k sh/day over the first 36 listed days ≈ **$2.8M/day, ~0.7% of the
~$450M free float** — 10-20× thinner than DHT/FRO/INSW (~$30M+/day).
Binding for institutions; immaterial for tool-signal quality or
personal-scale positioning.

Assessment: **no model change.** (a) Price-discovery quality — the thing
the model consumes — is strong: Oslo is the specialist shipping venue
(four dedicated research desks), and BRUT trading the same sub-0.8× NAV
shows the market is pricing the newbuild profile, not the postcode.
(b) The relevant venue fact is the **Euronext Growth junior tier** (no
index inclusion/passive flows, some mandates excluded) — plausibly a
slice of the 0.67×, and an embedded UPSIDE catalyst rather than a FV
haircut: OET and HAFN both re-rated on adding NYSE listings, the
natural CAPT path post-delivery. (c) Exit friction on a $450M-float
public equity is negligible at our horizon; any venue discount sits in
the market price, where it correctly widens EV rather than biasing FV.

Operating caveats: thinner tape → noisier daily closes → expect larger
band-edge wiggle than US names; and prices_daily mixes vintages for
CAPT (Oslo 16:25 CET close + FX vs 4pm ET closes) — known, cosmetic.
Watch-item: a US dual-listing announcement is a re-rating event worth
flagging in the weekly digest if it appears.

---

## 2026-06-11 (later) — §15 governance deep-dive: 0% CONFIRMED, with tripwires

Owner challenged the onboarding-day §15 decline ("does it plausibly need
a shitco discount like TEN/CMDB?") — fair, because the decline leaned on
Pareto reports, which don't scrutinize related-party plumbing. Full
Euronext Growth Information Document (159pp) pulled + parsed (archived:
`inputs/research_issuer/2026-03_capt_euronext_information_document.pdf`).

**Verified clean:** single share class, one vote per share, no founder
shares, no shareholder agreement. IPO sponsor transfers marked to
third-party broker valuations (Level 2, $872.5M fleet / $790M net), not
sponsor cost. The 13 options at cost run in the MINORITY's favor.
Related-party fee load is light and near-market: $550/day/vessel
technical (Capital Ship Management, CPI-escalating, 6-mo notice),
$300/day + 1.25% freight commission commercial (Heidmar, 3-mo notice),
$350k/vessel NB supervision — ~$15M/yr fully delivered ≈ 0.4% of GAV
vs CMDB ~4% and TEN's similarly heavy pattern. Sponsor track record
(CPLP/CCEC): process-driven related-party deals (conflicts committees,
broker marks, premiums), no litigation found.

**Verified concerning (mechanism, not evidence):** 76.3% control PLUS
100M authorized blank-check preferreds (board-issuable, rights fixed
per series, no shareholder vote); majority action by WRITTEN CONSENT
(sponsor can approve anything without a meeting); no pre-emptive
rights; board may amend bylaws unilaterally; no takeover code; not
subject to the Norwegian governance code; **no board committees at all**
(no audit, no conflicts); CEO Kalogiratos simultaneously CEO of Capital
Maritime + CCEC; director Miltiadis Marinakis owns 44.9% of Heidmar
(the commercial manager). Closest precedent: **Crude Carriers Corp** —
Marinakis's 2010 NYSE pure-crude vehicle, folded back into CPLP within
18 months at below IPO price (35% premium to pre-deal market;
unaffiliated-class vote held, 60.3% approved). Also disclosed: ~$65M
working-capital shortfall projected Q1-2027 pending ~$385M NB debt
(term sheets for $300M secured) — financing execution risk.

**Decision: `governance_discount_pct` stays 0.0.** §15 prices
DEMONSTRATED realisation impairment (TEN: decades at 0.4-0.5×; CMDB:
no-payout 0.6× book). CAPT: 3 months listed, pays ~50% from quarter
one, fees near-market, transfers at broker marks, and the BRUT natural
experiment (non-Marinakis Oslo newbuild vehicle at the same sub-0.8×
NAV) attributes the discount to the delivery phase, not the sponsor.
Sensitivity: a precautionary 10% haircut would read PW FV $17.68 →
~$16.2, BUY intact at ~+27% — the call is not haircut-sensitive today.

**§15 TRIPWIRES (any one reopens this decision):**
1. Option exercise funded by equity issued at a discount to NAV (no
   pre-emptive rights; the lock-up explicitly carves out option-funding
   shares — the likeliest dilution path).
2. Any blank-check preferred issuance.
3. Payout walked back below the guided 30-40% construction band.
4. Any merger/reshuffle proposal involving the sponsor (Crude Carriers
   replay) — switch to deal-arb framing immediately, as with GNK.
5. Fee escalation beyond CPI or new related-party service agreements.
6. Q1-2027 liquidity: the ~$385M NB debt must land on schedule.
7. Any CAPT↔CCEC cross-dealing (added at the 2026-06-11 CCEC §15.7
   screen — the two share a CEO and sponsor; an asset shuffle between
   them is the novel conflict this group structure enables).

---

## 2026-06-11 — ONBOARDED (17th name; first Oslo/NOK listing; Week 3 stretch goal)

**What CAPT is:** Capital Tankers — Marinakis (~75%), listed Oslo
2026-03-17 at NOK 134 after a $500M raise. 30 firm vessels: 12 VLCC
(310k) / 10 Suezmax (156k) / 4 Aframax (113k, only non-new sleeve, avg
age 7.8) / 4 LR2 (114k, crude-routed per the FRO §9.3 precedent). Only
9 on-water at Mar-31; 21 newbuilds deliver "one every ~six weeks"
through mid-2028 (Pareto-confirmed waypoints: 11 end-Apr-26 → 17 Nov-26
→ 24 YE-27 → 30 mid-28, "ahead of schedule"). 13 options at cost
(11 VLCC + 2 Suez, lapse YE'26) EXCLUDED from our NAV — we don't value
optionality (Pareto adds ~$204M ≈ $1.5/sh; a standing reconciliation
wedge to remember). All-spot, scrubber and/or LNG-DF throughout; our
curves carry no DF premium (Pareto adds $14-18M/vessel — their no-LNG
NAV NOK 138 vs headline 158 at initiation brackets that wedge too).

**Data provenance (unusual):** assembled from Pareto's initiation
(2026-04-19) + Q1 quarterly review (2026-05-27) — both already archived
by the linked-report harvest — NOT from issuer filings (Oslo-listed, no
EDGAR; IR site unverified). Q1'26 actuals from the review: cash $405M,
IB debt $217M, remaining capex $1,880M, 133.7M shares. **Follow-up: pull
the issuer Q1 report at the Q2 refresh for primary-source confirmation.**
The fleet_schedule per-class split between Pareto's waypoints is our
estimate (VLCC back-loaded / Suezmax front-loaded per class avg
own-years −1.3 / −0.3).

**First reconcile (the headline): tool NAV $17.74 vs Pareto-implied
broker NAV $18.21 — gap −2.6%, SANITY OK, k_broker 1.04.** The tightest
first-run gap of any name onboarded, on a REAL Pareto pnav print
(0.67×, Jun-10 daily, vintage-matched with price NOK 116.2 / USDNOK
9.5221 = $12.20). With 21 of 30 vessels valued through the
§3.1/§9.6 delivered-market-less-commitment convention on txn-anchored
age-0 marks, this is strong external validation of both the NB
convention and the crude curves — CAPT joins GNK (1.04) as a
near-1.0x k_broker validator. Note the wedges that happen to net out:
we exclude options (−$1.5/sh vs Pareto) and DF premia, txn-anchored
age-0 marks differ from Pareto's unit values — the −2.6% is a net, not
a term-by-term match.

**Signal:** PW FV $17.68 vs $12.74 live → **BUY, EV +38.8%** — the
deepest-discount name in the crude book, consistent with Pareto's
framing ("lowest priced crude tanker name", 0.67-0.84x NAV since
listing vs VLCC incumbents ~1.3x). The thesis is mechanical: NAV
accretes as newbuilds deliver into a delivered-market value above
remaining cost. Risks running the other way: 75% control + Capital
Maritime related-party management (§15 considered and NOT applied —
dividends from quarter one (~50% payout declared vs 30-40% guided),
live Pareto anchor, delivery-phase discount ≠ realisation trap; revisit
on payout walk-back or fee scaling), delivery-window rate risk into a
crude orderbook now ~25% of fleet, and the May-27 review's explicit
demand-destruction caveat.

**Quirks for future sessions:** Oslo/NOK — watchlist carries USD
(price_refresh fetches `yahoo_symbol: CAPT.OL`, converts via NOK=X;
bare "CAPT" on Yahoo is Captivision, the wrong issuer). Breakeven-TCE
solve returns $0/day (net cash + NB-heavy NAV exceeds price at zero
rates), making the scenario report's Assumed/Breakeven column garbage —
cosmetic, known. Earnings: expected late-Aug (no published calendar;
watch the dailies).

**Baseline for drift detection: gap −2.6% (Jun-10 vintage).**

---

## Scaffolded 2026-06-11 — superseded by the onboarding entry above

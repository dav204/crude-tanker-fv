# LPG — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-07-14T15:56:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.14
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.9%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.3pp (k_broker 1.34)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:51:05+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.14
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.9%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.3pp (k_broker 1.34)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:49:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.14
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.9%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.3pp (k_broker 1.34)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:44:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.05
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.7%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.2pp (k_broker 1.33)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:31:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.05
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.7%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.2pp (k_broker 1.33)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T13:00:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $40.05
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -23.7%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +28.2pp (k_broker 1.33)
- Sector: lpg

**Material deltas since last run:**
- ⚑ broker spread +8.0pp
- Δprice: +4.05 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +8.0pp

**Decision:** Drift explained (2026-07-12): Friday-close price vintage only — FV/NAV byte-identical (the doha reweight touched crude weights only; this name's sector is un-reweighted). k_broker rows where present = the pinned-P/NAV mechanical artifact of the price move. Ratify staged pending the owner's flip eyeball. LPG price $36→$40.05 (+11% vs the Jul-3 pair vintage; Pareto printing is seasonal-sparse, so the pair ages) — EV −8.6pp, k_broker +0.12 both price-mechanical; PROVISIONAL·v1-lock-miss unchanged, handoff NO.

---

## 2026-07-10 — v1 LOCK RULING: option (a) ACCEPTED by owner (PLAN decision #1b)

**Decision:** _Owner ruled 2026-07-10 ("let's go with (a)"): the 0/2 v1 lock miss is accepted
as documented — the lpg sector HOLDS at PROVISIONAL·v1-lock-miss (SECTOR_V1_UNLOCKED),
handoff NO, per the WO3 pre-registered letter. This closes WO3 Phase 5 on the
"miss documented" branch of its definition-of-done. Re-run path registered as trigger
`lpg_v1_lock_rerun` (due 2026-11-13, sentinel-paged): trio per-vessel splits → §9.9 re-fit
→ re-run `/reconcile --calibration-lock lpg` → readout back to the owner. If the re-fit
still misses on the residual broker premium (~−15%/−12% sketch), the GOVERNED-WIDE question
returns WITH evidence as a logged amendment. No tuning toward Pareto at any step._

---


## 2026-07-10T20:34:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:29:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:27:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10 — ONBOARDING (WO3 Phase 4, validator 1 of 2): sourced, reconciled, SANITY=OK

**Authority:** WO3_LPG_ONBOARDING.md Phase 4 (charter `fd0277f`). Source of record: FY2026
10-K (year ended 2026-03-31, filed 2026-05-27, acc 0001596993-26-000025) — the fiscal
year-end IS the 2026-Q1 calendar snapshot (no date-mix by construction).

**Subsequent events audited FIRST (Note 25), all kept OUT of the snapshot:** Apr-20 $16.5M
2023-A&R prepayment (Cobra tranche); May-6 Cobra sale COMPLETED, $81.9M net (the filed
figure REPLACED the broker-reported $83.5M in transactions/vlgc.yaml — the pre-registered
watch item; date corrected to 2026-05-06); May-7 $1.00/sh irregular dividend ($42.8M).
PLUS the Jun-23 8-K: Corsair (2014) + TWO unnamed 2015-builts agreed sold, $256M en bloc,
delivery "by" Q4-2026 — post-quarter, NO per-vessel split (no back-solve; prints wait for
the delivery filings). At the Q2 refresh: Cobra leaves the fleet; the trio goes HFS.

**Manifest (22 hulls):** the Item 5 carrying-value table (as-of 3/31, ties at 1,855,000 cbm,
"none held for sale"); scrubber/ECO/DF flags from the Item 4 fleet-table columns (per-vessel
issuer disclosure -> OPERATING_SCRUBBER_VERIFIED{LPG:16}); 6 TC-in hulls excluded. Areion
(93k-cbm VLAC, delivered 3/20) age 0. Cobra scrubber=false (no claim exists; value-neutral).

**Balance sheet:** cash $327.4M; WC net $100.84M (incl the $97.0M Helios Pool due-from-
related — Dorian's OWN earned share, NAV-economic, NOT the HAFN custodial gross-up; the
$26.4M non-current pool advance EXCLUDED conservatively); debt $565.81M GROSS per Note 10
(incl $288.0M Japanese SLB financings — inside debt, NOT lease_liabilities; ECO/GSL rule);
operating leases $148.7M = the chartered-in book + office (CMDB/SBLK convention: liability
subtracts, RoU not added — LARGEST charter-in book in the model at ~$3.5/sh, a flagged
convention-sensitivity item); newbuilds 0/0 (Note 20: none; Areion delivered); shares
42,782,681 outstanding at 3/31.

**Cost/dividend:** opex $10,557/day (issuer-disclosed daily figure); G&A $53.0M (FY2026
actual); interest $29.25M (FY2026 actual, debt near average); tax 0.0 (Marshall Islands,
no tax line). Dividend: IRREGULAR, no formula — payout_ratio 0.60 [ESTIMATE: FY2026
realized 0.54, trailing-declarations 0.65; strip-only consumer; revisit at the FQ1 refresh].

**Watchlist vintage (all 2026-07-03 Pareto daily, same-vintage):** price $36.00 / P/NAV
0.84 / fwd P/E 9.3 + TP $54 (BUY, the Jul-3 research note — supersedes Nov-25 HOLD/$30).
NOTE: the Jul-3 LPG/BWLP share-price rows were MISSING from pareto_share_prices.csv
(parser gap; re-extracted from the PDF) — flag for the next CSV harvest pass.

**Reconciliation baseline (first-run):** tool NAV $34.11 vs broker $42.86 -> gap −20.4%,
SANITY=OK, k_broker 1.21. Single-point FV $32.76 / PW FV $30.55 (EV −15.2% at $36.00).
Cycle 1.59x war-elevated (w_nav 0.70) -> position relabeled "rich · cycle position (not a
short)" (POSITION_CYCLE_RELABEL, the §12 shape). Weight-family: WEIGHT-ROBUST (TRIM sign
stable across LPG Sets A/B/C).

**v1 LOCK PRE-READ — MISS:** 0/2 validators within ±10% of broker (this name −20.4%).
Per the WO3 letter the sector is HELD AT PROVISIONAL (SECTOR_V1_UNLOCKED{"lpg"} caps the
tier; sub-reason v1-lock-miss; handoff_ready=False). The gap direction is consistent with
the txn-anchored curve sitting below Pareto's May-2026 raised quotes (k_broker ~1.2 = the
LPG broker premium; crude runs ~1.12-1.14). Do NOT tune marks toward Pareto — recent
prints (Cobra $81.9M filed at age-11; $84M age-10 auction; the trio ~$85.3M avg "3% above
Pareto quotes" per the 6-24 daily) suggest the fit's OLD end may be LIGHT; the sanctioned
re-fit path is the trio per-vessel splits (transactions/vlgc.yaml watch item).

**OWNER ITEMS (Phase 5, staged):** (1) rule on the v1 lock — accept the documented miss
(sector stays PROVISIONAL) or wait for the trio splits re-fit; (2) baseline ratify
`./scripts/ratify_baseline.sh "WO3 Phase-4 LPG+BWLP onboarding"` (adds both names; NOTE it
would also absorb the pending decision-#1 price drift — sequence with that call); (3) the
charter-in convention sensitivity above.

---

## 2026-07-10T20:20:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:12:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:06:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:04:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $36.00
- Single-point FV: $32.76
- Scenario PW FV: $30.55 (EV -15.2%)
- NAV / share: $34.11
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +20.2pp (k_broker 1.21)
- Sector: lpg

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---

## Scaffolded — pending first pipeline run

**Confidence tier (governance handoff): PROVISIONAL** _(scaffold — every NAV-driving figure is
still a FIXME/estimate, so the FV is not handoff-ready by construction). Once filled + reconciled,
the tier is computed from the validation state by `crude_tanker_fv.provenance.confidence_tier` and
emitted in the scorecard. A PROVISIONAL name must NOT hand off a governed FV — flag, don't pass._

**Decision:** _[pending — fill in the four input YAMLs + watchlist row, then
run `python -m crude_tanker_fv.pipeline {QUARTER}`. After the first run, the
pipeline prepends a structured model-state entry above this line.]_

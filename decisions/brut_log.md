# BRUT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.79
- Scenario PW FV: $10.65 (EV +97.3%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -40.7pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.79
- Scenario PW FV: $10.65 (EV +97.3%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -40.7pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22 — ONBOARDED (20th name) via the §9.6 time-to-delivery discount — SANITY OK after a +116% FAIL

**What BRUT is:** pure-play VLCC newbuild vehicle (Magni Partners / Tor Olav
Trøim; Koch ~26% / Trøim ~20% / free float ~54%), Oslo Growth-listed late-2024,
Bermuda-incorporated. 12 firm VLCC NB (8 NTS 300k + 4 CIMC Raffles 319k), **ZERO
on the water** at the snapshot — first (Mount Vision) delivers Jul-2026 on an
index-linked TC ($95k/day); last (Mount Voyager) Q3-2029; mid-point ~Apr-2028.

**Data provenance:** real per-vessel fleet from bruton-ltd.com/fleet/ (PRIMARY);
financials from the Pareto initiation 2026-04-22 (archived). Bruton reports
HALF-YEARLY — no Q1; **H1-2026 due 2026-08-13** (owner-confirmed) is the issuer
confirmation point for the Pareto-estimate balance sheet (cash ~$100M / net cash;
~$1.37bn remaining capex; 61.9M shares; zero dividend pre-operational).

**The onboarding first hit SANITY=FAIL +116%** (tool NAV $15.59 vs Pareto broker
NAV $7.20). Diagnosis (NOT a data error): the §3.1/§9.6 delivered-less-commitment
convention credited every NB the FULL delivered-today VLCC mark ($175M, ~$186M
blended with the 319k ships) regardless of delivery date — but only 1 of 12
arrives within a year; the rest stretch to 2029. On a 100%-newbuild balance sheet
(NAV = a small difference of large numbers) the tool's ~30% mark premium over
Pareto's implied ~$143M/VLCC levered ~2.5x into +116% (the "max torque" Pareto
flagged).

**Resolution — §9.6 time-to-delivery PV discount (owner-directed, BRUT-first):**
resolved the long-open §9 decision #6. `compute_nav` now PV-discounts a not-yet-
delivered NB's delivered value by `1.11^(−years_to_delivery)`, per-vessel from the
real delivery schedule (`NEWBUILD_DELIVERY_DISCOUNT_RATE` 11%; the remaining capex
commitment is kept at face = conservative). The strip terminal advances
`years_to_delivery` so ships delivered before the terminal de-discount and age in.
Backward-compatible: `years_to_delivery` defaults to 0 (on the water) → factor 1.0,
so the other 19 names are byte-identical (**286 tests green, all pins held**).

**Post-discount read:** NAV/sh **$9.40** (was $15.59); gap to Pareto **+30.6%**
(SANITY **OK**, k_broker 0.93); scenario PW FV $10.65 → **BUY (EV +97%)** at price
$5.40. The deep discount matches Pareto's own call (0.75× NAV "too excessive," BUY
TP NOK 66). BRUT is a pre-operational, max-torque NAV play — not an operating
validator.

**§15 — PARTIAL screen, provisional 0%:** gate cannot pass (<12 months listed,
0.73-0.79× P/NAV) → structured screen applies. Known: dispersed-ish ownership
(NO >50% controller, unlike CAPT's Marinakis 75%); zero distribution is
build-phase-appropriate. MISSING (need the Euronext admission prospectus): the
Goodwood Ship Management fee load + board/control terms. Complete at H1-2026.

**BRUT ↔ CAPT natural experiment (strategic value):** BRUT is the non-Marinakis
VLCC-NB comp capt_log leans on. Now modeled side by side — both pure-VLCC-NB at
sub-0.8× Pareto NAV, but BRUT dispersed (Koch/Trøim/54% float) vs CAPT 75%
Marinakis; both reconcile fine under §9.6 → supports "discount is delivery-phase,
not governance."

**Caveats (live):** pre-operational max-torque (10% asset move ≈ 40% NAV move);
~75% LTV, fleet-wide financing not yet secured (equity-raise/dilution risk); the
4x CIMC-2028 `years_to_delivery` is an intra-year estimate; NOK/FX; everything
Pareto-estimate until H1-2026 (Aug-13).

**Decision:** BRUT onboarded as the 20th name, SANITY OK at +30.6%; baseline gap
+30.6% recorded for drift. The §9.6 discount is **BRUT-first** — **ROLLOUT to the
other newbuild names (CAPT/FRO/MPCC/GSL/CMDB) is a pending owner decision** (it
will move their NAVs; needs a re-validation pass).

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.79
- Scenario PW FV: $10.65 (EV +97.3%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -40.7pp (k_broker 0.93)
- Sector: crude

**Material deltas since last run:**
- ⚑ single-point FV -26.2%
- ⚑ scenario PW FV -25.1%
- ⚑ broker spread +103.2pp
- ⚑ NAV/sh -39.7%
- Δprice: no change | Δsingle FV: -26.2% | Δscenario FV: -25.1% | ΔNAV: -39.7% | Δspread: +103.2pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $13.26
- Scenario PW FV: $14.22 (EV +163.4%)
- NAV / share: $15.59
- Position: **BUY (undervalued)**
- Broker spread: -143.9pp (k_broker 0.77)
- Sector: crude

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---

## Scaffolded — pending first pipeline run

**Decision:** _[pending — fill in the four input YAMLs + watchlist row, then
run `python -m crude_tanker_fv.pipeline {QUARTER}`. After the first run, the
pipeline prepends a structured model-state entry above this line.]_

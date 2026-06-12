# MPCC — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

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


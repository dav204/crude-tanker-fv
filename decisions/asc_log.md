# ASC — Decision Log

## 2026-08-08T19:57:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.71
- Single-point FV: $17.13
- Scenario PW FV: $17.11 (EV +2.4%)
- NAV / share: $17.37
- Position: **HOLD (fairly valued)**
- Broker spread: +26.3pp (k_broker 1.27)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T18:13:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.71
- Single-point FV: $17.13
- Scenario PW FV: $17.11 (EV +2.4%)
- NAV / share: $17.37
- Position: **HOLD (fairly valued)**
- Broker spread: +26.3pp (k_broker 1.27)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T18:01:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.71
- Single-point FV: $17.13
- Scenario PW FV: $17.11 (EV +2.4%)
- NAV / share: $17.37
- Position: **HOLD (fairly valued)**
- Broker spread: +26.3pp (k_broker 1.27)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +2.1% | Δscenario FV: +1.5% | ΔNAV: -2.5% | Δspread: +2.9pp

**Decision:** Q2 CLUSTER TRANSITION, block 1 — the first run consuming BOTH halves
(manifest at the 4b444f9 state + `asc_2026-Q2.yaml`; both-halves VERIFIED in this run's
own NAV breakdown: debt 33.4, leases 1.6, newbuild commitments 183.6, advances 0.0).
NAV $17.82→$17.37 (−2.5%) vs the pre-registered ~$17.31 (−2.9%) ±6% — inside band,
within 0.4% of the point, and SIGN-OPPOSITE to the VOIDed +16.9% artifact exactly as
the prereg predicted: the $183.6M Handysize-newbuild commitment the 7/31 half-application
hid is now in the number. The VOID banner stands as history. No flip (HOLD). Spread
+2.9pp = the FV-side move against a static consensus pnav; Δprice exactly 0 (frozen tape
by design). Baseline re-anchored via ratify same day (owner-authorized sequence
2026-08-08).

---

## 2026-08-08T17:55:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.71
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +0.8%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +23.4pp (k_broker 1.29)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-08-08T17:29:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.71
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +0.8%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +23.4pp (k_broker 1.29)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: -0.69 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -3.7pp

**Decision:** _[pending annotation]_

---

## 2026-07-31T19:45:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) final clean-stamp regen — stamp at clean HEAD; no movement.

---

## 2026-07-31T19:39:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) clean-stamp regen at the coherence-restore commit — no movement.

---

## 2026-07-31 (EVE) — ⚠ THE Q2 REFRESH BELOW IS **STAGED, NOT APPLIED** — see decisions/q2_cluster_transition_2026-07-31.md

The `asc_2026-Q2.yaml` balance sheet is written, sourced and kept; the fleet-manifest edits
were **REVERTED** the same evening. Reason: `load_balance_sheet` resolves an exact
`{{ticker}}_{{quarter}}.yaml` (no fallback) while the fleet manifest is quarter-agnostic, so
with the pipeline running `2026-Q1` the manifest half went live and the balance-sheet half
did not — asset counted, liability ignored. **The NAV/band results recorded below were
computed on MIXED inputs and are therefore VOID as measurements.** The attributions in them
(young-Panamax anchor; VLCC old-age level) are retained as HYPOTHESES to re-test, not as
findings. This name re-runs as part of the Q2 cluster transition once the vintage mechanism
is ruled.

---

## 2026-07-31T19:31:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- ⚑ single-point FV -17.4%
- ⚑ scenario PW FV -17.1%
- ⚑ broker spread +15.0pp
- ⚑ NAV/sh -14.5%
- Δprice: no change | Δsingle FV: -17.4% | Δscenario FV: -17.1% | ΔNAV: -14.5% | Δspread: +15.0pp

**Decision:** (2026-07-31 EVE) coherence-restore regen — the three staged Q2 refreshes were REVERTED on the manifest side (see the VOID banner at the top of sb/tnk/asc logs + decisions/q2_cluster_transition_2026-07-31.md); this run is coherent Q1-manifest-on-Q1-balance-sheet. No movement vs the pre-refresh state.

---

## 2026-07-31T19:27:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $20.31
- Scenario PW FV: $20.32 (EV +16.8%)
- NAV / share: $20.84
- Position: **BUY (undervalued)**
- Broker spread: +12.1pp (k_broker 1.13)
- Sector: product

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → BUY (undervalued)
- ⚑ single-point FV +21.1%
- ⚑ scenario PW FV +20.6%
- ⚑ broker spread -15.0pp
- ⚑ NAV/sh +16.9%
- Δprice: no change | Δsingle FV: +21.1% | Δscenario FV: +20.6% | ΔNAV: +16.9% | Δspread: -15.0pp

**Decision:** _[pending annotation]_

---

## 2026-07-31 — Q2 REPORT-DAY REFRESH (pre-registered BEFORE recompute; 6-K pair acc -087834/-087836)

**Snapshot moved 2026-03-31 → 2026-06-30.** Deltas: **debt 103.4 → 33.4** (−$70.0M of Q2
paydown, funded by the Engineer proceeds + operating cash; all non-current, nothing due
before 2030) · cash 47.2 → 48.1 · operating WC 46.6 → 53.8 · chem sleeve 73.1 → 72.1
(0.25y depreciation on the cited carrying basis) · **held_for_sale 35.5 → 0** (Ardmore
Engineer SOLD, delivered June, gain $12.2M, net proceeds $35.1M) · **newbuild commitments
0 → 183.6M with advances 0** · shares ~flat · ages +0.25 · TC book 4 product → 5 product +
1 chemical (MR spot coverage 0.78 → 0.72).

**THE FIGURE-PROVENANCE CATCH (source-verified, not inferred):** the release's remaining-
installment table totals $165.2M but is explicitly dated **"as of July 29, 2026"** — after
the Company "paid $18.4 million as installments for two of the newbuildings" in Q3. The
6/30 commitment is therefore **165.2 + 18.4 = 183.6**. Advances at 6/30 = **ZERO**, verified
twice: the MD&A lists "first installment payments for the four newbuildings" under
SHORT-TERM liquidity (still upcoming at the balance-sheet date), and H1 investing cash flow
shows only $2.2M vessel/equipment + $0.5M equipment advances — no newbuild outflow. Taking
the table at face value would have understated the commitment by $18.4M (~$0.45/sh).

**Order is now 4 vessels, not 2** (April order + June option exercise on the same terms),
plus 2 further options SECURED BUT EXCLUDED — an option is not a commitment.

**PRE-REGISTERED EXPECTATION (before recompute):** +70.0 (debt) + 0.9 (cash) + 6.1 (WC net
of chem dep) − 35.5 (HFS retired) − 12.3 (ages +0.25 on 20 on-curve hulls) and the §9.6
newbuild leg **NEGATIVE**: 4 hulls at the $44.9M issuer-contract age-0 basis, PV-discounted
1.11^−2.4 / 1.11^−3.0 ≈ $133.4M delivered value against a $183.6M unpaid commitment ⇒
≈ −$50.2M. Net ≈ **−$21.0M ⇒ NAV/sh $17.82 → ~$17.31, i.e. ≈ −2.9%; band ±6% →
[16.75, 18.89]. No tier change expected (GOVERNED-WIDE·structural-class stands — the 4
off-curve chem hulls are unchanged). SANITY must stay OK.**

**DISCREPANCY FLAGGED AHEAD OF THE RUN:** PLAN.md carries a pre-booked expectation of a
"**~+1.9%** Handysize correction" at this refresh, written 2026-07-15 when the order was
2 vessels and before the commitment/advance split was known. My computed expectation is the
opposite SIGN. The mechanism is the §9.6 convention itself: an unpaid, far-dated newbuild is
NAV-NEGATIVE (you owe ~$46M face for an asset worth ~$33M in PV at the locked 11% rate) —
unlike SB, whose NBs are ~40% pre-paid so its remaining commitment sits far below delivered
PV. If the recompute lands near −2.9%, the PLAN note was about the Thread-1A age-0 re-source
in isolation, not the whole NB entry, and PLAN should be corrected rather than the model.

## 2026-07-31T19:18:35+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31) clean-stamp regen (TNK Q2 refresh arc close) — no movement; the refresh records stand.

---

## 2026-07-31T19:11:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T19:01:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T18:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31 EVE) clean-stamp regen (SB Q2 refresh arc) — no movement; the refresh + band-miss records stand.

---

## 2026-07-31T18:24:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-31T18:06:00+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-31) clean-stamp regen (B' arc close) — no movement; the two-cause annotations below stand.

---

## 2026-07-31T18:03:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV -3.2%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +27.1pp (k_broker 1.35)
- Sector: product

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- ⚑ broker spread +15.0pp
- Δprice: +2.50 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +15.0pp

**Decision:** (2026-07-31) TWO-CAUSE regen — (1) B' reweight EXECUTED (owner go; 7/22 frozen conditional; decisions/ceasefire_mediation_check_2026-07-31.md — crude scenario FVs +0.5-0.6%, per the proposal's B' column) + (2) the 7/31 live price vintage (deliberate absorb b9aa18a — the committed 7/24 vintage aged past the overlay freshness gate and one regen fell back to stale watchlist prices; those outputs were DISCARDED, never committed). ΔNAV +0.0% every row. Earnings-week tape: the shipping complex rallied on the Q2 prints. EV%-only (price +17% on the week; Q2 landed 7/29, refresh queued).

---

## 2026-07-31T18:00:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.90
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +13.1%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +12.1pp (k_broker 1.13)
- Sector: product

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → BUY (undervalued)
- ⚑ broker spread -10.8pp
- Δprice: -1.71 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -10.8pp

**Decision:** _[pending annotation]_

---

## 2026-07-28T19:32:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28 EVE) clean-stamp regen at a9b99dc — the parked stamp refresh, unblocked by the anchor-fix commit; no number movement, the day's annotations below stand.

---

## 2026-07-28T16:42:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

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
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28) family-sidecar re-stamp regen (promotion arc, final) — no movement; annotations below stand.

---

## 2026-07-28T15:51:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-28) clean-stamp regen at 71e7020 (marks-promotion arc close) — no movement; the promotion annotations below stand.

---

## 2026-07-28T15:36:23+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-26T21:26:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-26) week-close clean-stamp regen at d1fe786 — no movement; the week-close annotations below stand.

---

## 2026-07-26T21:20:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-26 week-close) FLIP EYEBALL — BUY→HOLD, the pre-warned oscillation (7/13 ratify note: 'the staged product re-tilt may flip it back — NEW eyeball then'): +8% product tape, shallow boundary crossing, ΔNAV 0.0. Accepted individually at the ratify; the Q2 print (~7/28-30 window) rebuilds the FV with the +1.9% Handysize correction anyway.

---

## 2026-07-26T21:19:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.61
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.4%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.9pp (k_broker 1.28)
- Sector: product

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- Δprice: +0.79 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +4.7pp

**Decision:** _[pending annotation]_

---

## 2026-07-24T16:05:00+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-24T16:04:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-24T15:56:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → BUY (undervalued)
- Δprice: -0.76 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -4.5pp

**Decision:** _[pending annotation]_

---

## 2026-07-24T15:55:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.58
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +1.6%)
- NAV / share: $17.82
- Position: **HOLD (fairly valued)**
- Broker spread: +22.7pp (k_broker 1.28)
- Sector: product

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- Δprice: +0.76 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +4.5pp

**Decision:** _[pending annotation]_

---

## 2026-07-22T22:01:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:56:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:50:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T21:48:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-22T18:14:30+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.82
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +6.5%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +18.2pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.42 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.7pp

**Decision:** _[pending annotation]_

---

## 2026-07-18T20:22:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +9.4%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +15.5pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the PPMX seed — same state as the dated entries below; no new movement.

---

## 2026-07-18T20:21:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +9.4%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +15.5pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-18T20:07:52+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +9.4%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +15.5pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the 2026-07-18 marks promotion + family re-run — same state as the dated entries below; no new movement.

---

## 2026-07-18T20:06:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +9.4%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +15.5pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** clean-stamp regen after the 2026-07-18 marks promotion — same state as the dated entry below; no new movement.

---

## 2026-07-18T19:59:08+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.77
- Scenario PW FV: $16.85 (EV +9.4%)
- NAV / share: $17.82
- Position: **BUY (undervalued)**
- Broker spread: +15.5pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: +0.1% | ΔNAV: +0.1% | Δspread: -0.1pp

**Decision:** _[pending annotation]_

---

## 2026-07-18T19:38:05+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +9.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +15.6pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18, final) — same state as the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:36:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +9.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +15.6pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18, family sidecar re-run at the current EV state) — same state as the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:35:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +9.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +15.6pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** Week-close clean-stamp regen (2026-07-18) — identical state to the dated 2026-07-18 annotation(s) below; no new movement.

---

## 2026-07-18T19:23:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +9.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +15.6pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-18T19:22:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.40
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +9.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +15.6pp (k_broker 1.18)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:42:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:24:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:23:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T19:15:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T17:46:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T16:48:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T16:47:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T15:45:30+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-15T14:33:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.18
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +4.0%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +20.5pp (k_broker 1.25)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.35 | Δsingle FV: no change | Δscenario FV: +3.4% | ΔNAV: no change | Δspread: +2.8pp

**Decision:** _[pending annotation]_

---

## 2026-07-14T21:24:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.83
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +2.8%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +17.7pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:56:09+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.83
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +2.8%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +17.7pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:51:05+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.83
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +2.8%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +17.7pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-14T15:49:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.83
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +2.8%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +17.7pp (k_broker 1.21)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:44:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.39
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV -0.7%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +21.0pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T15:31:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.39
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV -0.7%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +21.0pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-13T13:00:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.39
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV -0.7%)
- NAV / share: $17.80
- Position: **HOLD (fairly valued)**
- Broker spread: +21.0pp (k_broker 1.26)
- Sector: product

**Material deltas since last run:**
- ⚑ position BUY (undervalued) → HOLD (fairly valued)
- ⚑ broker spread +6.4pp
- Δprice: +1.07 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +6.4pp

**Decision:** Drift explained (2026-07-12): Friday-close price vintage only — FV/NAV byte-identical (the doha reweight touched crude weights only; this name's sector is un-reweighted). k_broker rows where present = the pinned-P/NAV mechanical artifact of the price move. Ratify staged pending the owner's flip eyeball.

---

## 2026-07-10T20:34:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** EV%-only drift explained, NOT accepted (2026-07-10, WO3 Phase-4 clean-HEAD regen): FV/NAV unchanged; EV denominators at live Jul-9/10 prices vs the Jul-6-committed baseline — the KNOWN price-vintage drift, PENDING OWNER DECISION #1 (PLAN.md). Re-ratify stays with the owner.

---

## 2026-07-10T20:29:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** EV%-only drift explained, NOT accepted (2026-07-10, WO3 Phase-4 clean-HEAD regen): FV/NAV unchanged; EV denominators at live Jul-9/10 prices vs the Jul-6-committed baseline — the KNOWN price-vintage drift, PENDING OWNER DECISION #1 (PLAN.md). Re-ratify stays with the owner.

---

## 2026-07-10T20:27:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** EV%-only drift explained, NOT accepted (2026-07-10, WO3 Phase-4 clean-HEAD regen): FV/NAV unchanged; EV denominators at live Jul-9/10 prices vs the Jul-6-committed baseline — the KNOWN price-vintage drift, PENDING OWNER DECISION #1 (PLAN.md). Re-ratify stays with the owner.

---

## 2026-07-10T20:20:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:12:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** EV%-only drift explained, NOT accepted (2026-07-10, WO3 Phase-4 onboarding run): FV/NAV unchanged (delta report: every FV 'no change'); the EV denominator moved with live Jul-9/10 prices vs the Jul-6-committed book — the KNOWN price-vintage drift already recorded as PENDING OWNER DECISION #1 (PLAN.md). Explain-not-accept: the committed-price re-ratify stays with the owner.

---

## 2026-07-10T20:06:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:04:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.32
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +6.3%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +14.6pp (k_broker 1.17)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.42 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.8pp

**Decision:** _[pending annotation]_

---

## 2026-07-06T19:23:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:55:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:40:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-06T18:18:04+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:42:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T13:35:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T02:11:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:55:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:54:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:14:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T01:04:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:56:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:30:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-03T00:10:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.61 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +4.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:59:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +14.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.2pp (k_broker 1.08)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: -0.61 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -4.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T23:58:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.86
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +9.6%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +11.5pp (k_broker 1.13)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.61 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +4.3pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T18:27:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.28 (EV +14.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.2pp (k_broker 1.08)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: -3.3% | ΔNAV: no change | Δspread: -0.2pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T16:43:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +18.1%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.4pp (k_broker 1.08)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:56:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +18.1%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.4pp (k_broker 1.08)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T15:34:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +18.1%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.4pp (k_broker 1.08)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:53:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $14.25
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +18.1%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +7.4pp (k_broker 1.08)
- Sector: product

**Material deltas since last run:**
- ⚑ broker spread -12.0pp
- Δprice: -1.75 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -12.0pp

**Decision:** _[pending annotation]_

---

## 2026-07-02T14:44:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T04:32:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-02T00:21:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:28:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T23:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T21:16:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-01) no-change re-run to regenerate outputs after the ASC read-flip fix — ASC left
`POSITION_CYCLE_RELABEL`, so the scorecard now shows raw **BUY**, not the stale "rich · cycle position" label
(that label described the pre-reconciliation overvalued state; corrected NAV $17.80 > price = 0.90× makes it
mildly cheap). The reconciliation itself is annotated on the 18:08:59 entry below (NAV $15.96→$17.80,
PROVISIONAL → GOVERNED-WIDE·structural-class; drift vs baseline explained there; ASC-only re-ratify pending — owner).

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $16.75
- Scenario PW FV: $16.83 (EV +5.2%)
- NAV / share: $17.80
- Position: **BUY (undervalued)**
- Broker spread: +19.4pp (k_broker 1.23)
- Sector: product

**Material deltas since last run:**
- ⚑ position TRIM/SHORT (overvalued) → BUY (undervalued)
- ⚑ single-point FV +11.0%
- ⚑ scenario PW FV +11.1%
- ⚑ broker spread -10.2pp
- ⚑ NAV/sh +11.7%
- Δprice: no change | Δsingle FV: +11.0% | Δscenario FV: +11.1% | ΔNAV: +11.7% | Δspread: -10.2pp

**Decision:** (2026-07-01) full balance-sheet reconciliation — ASC cleared PROVISIONAL → GOVERNED-WIDE.
The +11.7% NAV move + TRIM/SHORT→BUY band flip are EXPLAINED and INTENDED — the P0 reconciliation
(pre-reg: `decisions/asc_reconciliation_prereg_2026-07-01.md`), sourced to the Q1-2026 6-K
(acc 0001104659-26-056715), FY2025 20-F (acc …024690), and the 2013 order 6-K (acc 0000919574-13-005339).
Drivers of NAV $15.96→$17.80: (1) the 2×40,500 DWT Handysize newbuild was EXCLUDED from Q1 — the
contracts were signed **April 2026** (6-K Note 8 subsequent event), so the −$88.8M commitment-only drag
did not exist at 3/31 (+$2.15; also a §9.6 violation — commitment with no offsetting asset); (2) phantom
`Ardmore_Patriot` removed (never an Ardmore vessel, 0 mentions in 6-K/20-F; −$0.90); (3) the 4 chemical
Handies re-marked from an uncited ~$13M/hull estimate to a cited **20-F carrying-value floor** (~$18.3M/hull,
+$0.58); (4) balance sheet re-sourced (cash/debt/leases/WC/shares; net small). HFS Ardmore Engineer ($35.5M,
agreed sale, June-2026 delivery) relocated to the dedicated `held_for_sale` field. ASC leaves
`NAV_FIGURE_ESTIMATE_QUEUE` + `OFF_CONVENTION_QUEUE` → tier PROVISIONAL → **GOVERNED-WIDE** (structural-class:
chemical-Handy carrying-value floor, no clean resale curve). **READ FLIPPED:** position moved TRIM/SHORT →
**BUY (+5.2%)** — the overvalued read was partly the erroneous newbuild drag. ASC is now mildly CHEAP on
corrected NAV (price 0.90× NAV; −16.6% to APPROX broker, SANITY n/a-OK), so it LEFT `POSITION_CYCLE_RELABEL`
(no longer rich). The §12 product-cycle caveat still applies to the EARNINGS leg (the strip embeds near-peak
product rates; the Q2 newbuild on-curve will trim NAV ~$0.49), but that is not a rich-NAV read. NOT a new
VALIDATED-TIGHT actionable long (GOVERNED-WIDE · structural-class). Newbuild to be wired on-curve in Q2
(§9.6, issuer-announced $44.9M/ship). **Baseline re-ratify (ASC-only) recommended** — owner action.

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -5.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.6pp (k_broker 1.33)
- Sector: product

**Material deltas since last run:**
- ⚑ position HOLD (fairly valued) → TRIM/SHORT (overvalued)
- ⚑ broker spread +5.1pp
- Δprice: +0.88 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +5.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.12
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV +0.2%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +24.5pp (k_broker 1.26)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: -0.81 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -4.7pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $15.93
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -4.9%)
- NAV / share: $15.93
- Position: **HOLD (fairly valued)**
- Broker spread: +29.2pp (k_broker 1.33)
- Sector: product

**Material deltas since last run:**
- ⚑ position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- ⚑ broker spread -5.9pp
- Δprice: -1.14 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -5.9pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -11.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.1pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -11.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.1pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -11.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.1pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $15.09
- Scenario PW FV: $15.15 (EV -11.3%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.1pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +1.4% | Δscenario FV: +0.7% | ΔNAV: no change | Δspread: -0.6pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:25:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -11.8%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.7pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T16:04:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -11.8%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.7pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:33:40+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -11.8%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.7pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T15:15:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $17.07
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -11.8%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +35.7pp (k_broker 1.42)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T21:55:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T18:49:44+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T14:28:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:50:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T13:44:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T02:42:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-12T00:38:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.38
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.1%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.2pp (k_broker 1.36)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: -0.51 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -2.6pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T23:54:55+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.89
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -10.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +34.8pp (k_broker 1.40)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-11 — §15.7 retro screen (formalised today): **N/A (gated vs tool NAV)** — no Pareto print (APPROX); price ≈ 1.03× tool NAV. Widely held, payout recently doubled. No discount to explain.

---

## 2026-06-11T15:40:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.89
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -10.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +34.8pp (k_broker 1.40)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.46 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.3pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T03:20:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.43
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -8.4%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +32.5pp (k_broker 1.37)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: +0.43 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +2.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-11T02:59:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:17:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T20:00:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T18:16:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T13:25:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10 — Pareto free-text retro-sweep (6 mentions, 2025-01 → 2026-06)

Distilled from `outputs/pareto_mentions_asc.md`. **Pareto states "We don't
cover ASC" verbatim (2025-02-20)** — APPROX consensus_pnav confirmed from
the horse's mouth.

Timeline color: a tanker peer took a passive 5% stake in Ardmore (Feb-25;
Pareto scathing about cash-rich NAV-discount names buying peer equity) and
exited fully by Feb-26. 2026-04-30: ASC "doubling of its dividend payout
ratio (now distributing 2/3rds of earnings)" — already captured in
dividend_policies/asc.yaml (0.667) ✓ — plus an order for 2x 40.5k dwt
handysize at $44.9M each (Wuhu, late-2028 delivery). **Refresh flag:** the
handysize NB order is post-Q1 → enters the Q2 balance sheet as
commitments; also a future age-0 print for the clean-Handy class if we
ever curve it. Off-curve chemical-Handy residual treatment unchanged.

---

## 2026-06-10T12:59:17+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:49:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.88
- Scenario PW FV: $15.05 (EV -5.9%)
- NAV / share: $15.93
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.1pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -0.1% | Δscenario FV: -0.1% | ΔNAV: -0.2% | Δspread: +0.1pp

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:09:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $15.07 (EV -5.8%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T02:09:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $15.07 (EV -5.8%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-10T01:33:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $15.07 (EV -5.8%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T23:27:18+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $15.07 (EV -5.8%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-09T19:14:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $15.07 (EV -5.8%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +30.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +3.9% | ΔNAV: no change | Δspread: +1.0pp

**Decision:** _[pending annotation]_

---

## 2026-06-09T15:13:20+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $14.50 (EV -9.4%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.0pp (k_broker 1.33)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-07T15:11:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $16.00
- Single-point FV: $14.90
- Scenario PW FV: $14.50 (EV -9.4%)
- NAV / share: $15.96
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +29.0pp (k_broker 1.33)
- Sector: product

**Material deltas since last run:**
- ⚑ broker spread -12.4pp
- Δprice: -2.50 | Δsingle FV: +2.1% | Δscenario FV: +1.8% | ΔNAV: +1.1% | Δspread: -12.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:26:22+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:24:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T19:10:02+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:08:46+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-04T18:03:41+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-03T21:01:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $14.24 (EV -23.0%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +41.4pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: +4.8% | ΔNAV: no change | Δspread: +1.8pp

**Decision:** _[pending annotation]_

---

## 2026-06-01T21:03:19+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:33:10+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:28:51+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T20:22:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:50+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:48:27+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:45+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-01T19:45:29+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.50
- Single-point FV: $14.59
- Scenario PW FV: $13.59 (EV -26.5%)
- NAV / share: $15.78
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +39.6pp (k_broker 1.59)
- Sector: product

**Status:** _First snapshot — no prior state to compare._

**Decision:** _[pending annotation]_

---


## 2026-07-14 EVE — hormuz re-tilt boundary eyeball: NO flip

**Decision:** the promised ASC eyeball at the re-tilt execution (the Jul-13 ratify note
anticipated "the staged product re-tilt may flip it back"): PW FV $16.30→$16.85 as
predicted, but at tonight's $16.18 close EV lands +4.0% — UNDER the BUY line. ASC stays
HOLD; no flip fired; the anticipated re-eyeball is hereby closed without a band change.

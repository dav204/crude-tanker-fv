# BRUT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-07-01T19:50:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.27
- Scenario PW FV: $10.24 (EV +96.6%)
- NAV / share: $8.80
- Position: **BUY (undervalued)**
- Broker spread: -34.5pp (k_broker 0.94)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** (2026-07-01) no-change re-run to regenerate outputs after two owner-directed rendering fixes —
(1) BRUT added to `POSITION_UNRELIABLE`, so the verdict position cell now reads **"unreliable read (not
actionable)"** instead of a raw BUY: a 0.59× "BUY" sitting next to `PROVISIONAL ⛔ NO` was the ASC
"rich·cycle" holdover trap in reverse (the eye-catching discount and the untrustworthiness are the SAME
max-torque fact). (2) The §15 going-concern haircut stays **0% — deliberately** (owner): a going-concern
doubt is a BINARY survival question, not a tunable %; a made-up 25/30% would fabricate precision, so it is
a prominent QUALITATIVE flag that resolves with H1-2026 financing clarity. NAV unchanged $8.80. The
reconciliation itself is annotated on the 19:39:53 entry below; BRUT-only re-ratify follows this run.

---

## 2026-07-01T19:39:53+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.27
- Scenario PW FV: $10.24 (EV +96.6%)
- NAV / share: $8.80
- Position: **BUY (undervalued)**
- Broker spread: -34.5pp (k_broker 0.94)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +11.3pp
- ⚑ NAV/sh -6.4%
- Δprice: no change | Δsingle FV: -5.8% | Δscenario FV: -5.3% | ΔNAV: -6.4% | Δspread: +11.3pp

**Decision:** (2026-07-01) balance-sheet TRACE + cash FLOOR + governance correction — EXPLAINED, INTENDED.
Fourth P0 reconciliation (pre-reg `decisions/brut_reconciliation_prereg_2026-07-01.md`), workflow-sourced to
the FY2025 Annual Report (`inputs/research_issuer/2025_brut_annual_report.pdf`, audited US GAAP), the Euronext
admission doc, and Pareto (cross-check). **The reconciliation VALIDATES the model** — the Pareto estimates were
accurate: commitment $1,373.1M (Note 10 $661.7M + Note 15 Jan $236.0M + CIMC $499.0M − $23.6M Q1 installments)
≈ prior $1,370M; debt $0 (Dec-2025 total liab $0.161M, equity-financed); shares 61,923,808 (Dec 52,399,998 +
Feb placement 9,523,810). These 4 now TRACE to the issuer (banked). NAV $9.40→$8.80 is ENTIRELY the cash line:
booked at the **$66M conservative FLOOR** (owner decision) not the $116M itemized point nor Pareto's $100M — the
Mar-2026 CIMC ~$50M execution deposit likely hit Q1, and a going-concern-doubtful issuer doesn't contract 4
VLCCs without it; band $66–116M, resolves at the H1-2026 report (2026-08-13). **Cash keeps BRUT PROVISIONAL**
(stays in `NAV_FIGURE_ESTIMATE_QUEUE`), new sub-reason **`cash-pending-H1-report`** (a WAITING state — sourced
except one figure with a known resolution date — not `void`/`uncited`). Also corrected the **FABRICATED
governance** block (no "Goodwood"/no "Koch"/not "dispersed" — managers 2020 Bulkers + Himalaya; Trøim-sponsored;
Magni zero-fee) and recorded the **going-concern doubt** as the §15/risk headline (`governance_discount_pct` 0,
% pending a §15 judgment at H1). BRUT is NOT actionable — the +96% EV is upside to a going-concern-doubtful,
max-torque, resale-level-provisional NAV → directional-only; the tight-actionable surface stays SB + SBLK.
SANITY OK (+22.2% to Pareto NAV $7.20). **Baseline re-ratify (BRUT-only) recommended; RE-RATIFY AGAIN at H1-2026** — owner.

---

## 2026-07-01T18:24:03+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T18:08:59+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-01T02:12:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:56:31+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:38:24+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T17:32:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T15:35:07+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.21
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +107.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -45.8pp (k_broker 0.92)
- Sector: crude

**Material deltas since last run:**
- ⚑ single-point FV +90.7%
- ⚑ scenario PW FV +80.5%
- ⚑ broker spread -96.5pp
- ⚑ NAV/sh +116.6%
- Δprice: -0.13 | Δsingle FV: +90.7% | Δscenario FV: +80.5% | ΔNAV: +116.6% | Δspread: -96.5pp

**Decision:** Amendment B (deliberate correction) — reverted Thread-1's crude age-0. VLCC age-0 = xclusiv RESALE $175M (2026-06-22 PDF); the Thread-1 $145M was the xclusiv 5-YEAR value, mislabeled 'prompt resale'. BRUT NAV $4.34->$9.40 = EXACTLY pre-Thread-1; the -53.8% is fully unwound. LEVEL-PROVISIONAL flag CLEARS — not by confirming a level, but by reverting to the Resale line. Basis LOCKED: age-0 = xclusiv Resale, mid-age = transaction prints (§9.9).

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $5.16
- Scenario PW FV: $5.99 (EV +12.2%)
- NAV / share: $4.34
- Position: **BUY (undervalued)**
- Broker spread: +50.7pp (k_broker 1.11)
- Sector: crude

**Material deltas since last run:**
- ⚑ single-point FV -47.6%
- ⚑ scenario PW FV -44.6%
- ⚑ broker spread +92.2pp
- ⚑ NAV/sh -53.8%
- Δprice: no change | Δsingle FV: -47.6% | Δscenario FV: -44.6% | ΔNAV: -53.8% | Δspread: +92.2pp

**Decision:** Thread 1 (uniform prompt-resale age-0 NAV anchor) — methodology/basis correction, NOT a market move. VLCC age-0 mark corrected from the stale-high $175M to the dated prompt-resale $145M (-17%). BRUT is 100% VLCC newbuilds carried at age-0 delivered-market (§9.6), so the -17% asset move levers into -53.8% NAV (Pareto 'max torque' — small difference of large numbers vs the ~$1,370M commitment). Direction pre-registered (PRE_REGISTRATION_NAV_RESALE_ANCHOR.md §6/§7; largest single mover). Owner-approved 2026-06-29; re-ratified with crude resale LEVELS flagged PROVISIONAL. **LEVEL-PROVISIONAL:** guard #2 validated the depreciation SLOPE ($145M->$113M production 5yr, 22%, from independent S&P prints), NOT the $145M age-0 LEVEL (A1.5 open — the crude resale series may carry inflation). BRUT is the name where this does the most damage: NAV = delivered-market(resale) − fixed $1,370M commitment, the widest asset-vs-commitment spread and closest broker divergence (−40%, near the ±50% SANITY gate) in the book. The −53.8% move is slope-validated, level-provisional pending a dated current VLCC resale source (Thread 1B). If a dated mark lands at ~$138M, BRUT moves materially again.

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T23:38:06+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-27T00:31:14+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.34
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +102.4%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -41.5pp (k_broker 0.92)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread -7.4pp
- Δprice: -0.24 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -7.4pp

**Decision:** _[pending annotation]_

---

## 2026-06-26T20:14:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.58
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +93.7%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -34.1pp (k_broker 0.93)
- Sector: crude

**Material deltas since last run:**
- ⚑ broker spread +5.5pp
- Δprice: +0.18 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: +5.5pp

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:52:36+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +100.1%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -39.6pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:46:42+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.84
- Scenario PW FV: $10.81 (EV +100.1%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -39.6pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.1% | Δscenario FV: +0.1% | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T19:34:34+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.83
- Scenario PW FV: $10.80 (EV +100.1%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -39.6pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-22T18:59:57+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $5.40
- Single-point FV: $9.83
- Scenario PW FV: $10.80 (EV +100.1%)
- NAV / share: $9.40
- Position: **BUY (undervalued)**
- Broker spread: -39.6pp (k_broker 0.93)
- Sector: crude

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +0.4% | Δscenario FV: +1.4% | ΔNAV: no change | Δspread: +1.1pp

**Decision:** _[pending annotation]_

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

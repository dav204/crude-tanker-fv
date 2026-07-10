# BWLP — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-07-10 — v1 LOCK RULING: option (a) ACCEPTED by owner (PLAN decision #1b)

**Decision:** _Owner ruled 2026-07-10: sector-level lock miss accepted as documented;
BWLP holds at PROVISIONAL·v1-lock-miss (handoff NO) until the lock re-runs off the Dorian
trio splits (trigger `lpg_v1_lock_rerun`, due 2026-11-13). Full rationale in lpg_log
(same ruling). BWLP-specific: the NCI-via-preferred_equity convention ($199.0M) remains a
SEPARATE open owner-review item (onboarding entry, item #1) — not covered by this ruling._

---


## 2026-07-10T20:34:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:29:54+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:27:58+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10 — ONBOARDING (WO3 Phase 4, validator 2 of 2): sourced, reconciled, SANITY=OK

**Authority:** WO3_LPG_ONBOARDING.md Phase 4 (charter `fd0277f`). Sources of record: Q1-2026
interim report (6-K filed 2026-06-03, acc 0001213900-26-064314; IFRS balance sheet as of
31-Mar-2026) + FY2025 20-F (filed 2026-03-31, acc 0001104659-26-037215) for fleet tables,
borrowings composition, dividend policy, ownership.

**Subsequent events audited FIRST, kept OUT:** 30-May-2026 EIGHT 90'cbm Panamax-VLGC
newbuild contract, ~$940M, deliveries 2029->Q2-2030 (6-K acc 0001213900-26-063117) — the
ASC/HAFN/TRMD subsequent-event pattern, 4TH instance; zero commitment/advance at 3/31.
§9.6 on-curve wiring at the Q2 refresh. Also 3-Jun Confidence Petroleum stake exit (stake
stays at its 3/31 FVOCI/FVPL marks). R-2 NOTE: the order adds 8 hulls to the VLGC
orderbook the consumer's R-2 kill-switch watches (last-known ~30% vs the 38% void bar).

**Manifest (39 hulls):** 28 parent-owned (20-F owned table) + 3 lease-financed bareboat
(Capella/Polaris/Kyoto — the 20-F borrowings note carries "Lease financing arrangement"
INSIDE borrowings: the Dorian-Japanese-financing pattern, hulls in NAV) + 8 BW LPG India
(52%-owned CONSOLIDATED sub). Chartered-in book excluded (11 in the 20-F chartered table
+ 4 India-operated charters; RoU/lease-liability treatment per CMDB/SBLK). Scrubber from
the propulsion column per-vessel -> OPERATING_SCRUBBER_VERIFIED{BWLP:12}. India hulls
time_charter ("mainly fixed-rate time charters", Q1 report).

**Balance sheet:** cash $273.1M (incl $96.9M broker margin — posted collateral for hedge
positions whose fair values net in WC; counted, documented); WC net $176.6M (the gross
derivative books 283.4/190.6 net +92.8 — Product Services hedges; trading inventory
$106.9M); debt $763.9M (captions; bank + lease financing + trust receipts + interest
payable); lease liabilities $133.9M (chartered-in); newbuilds 0/0; shares 151,814,600
(159,282.0k − 7,467.4k treasury).

**THE CONVENTION DECISION — NCI via preferred_equity ($199.0M), OWNER-REVIEW ITEM #1:**
the schema has no NCI field; preferred_equity subtracts ahead of common, which is exactly
the minority claim's seniority. Book NCI $118.5M UNDERSTATES the minority's claim on a
marked-to-curve NAV, so the deduction is NAV-BASIS: India (48% NCI) 8 hulls at curve marks
(≈$515.9M) + India WC − India borrowings ≈ sub-NAV $355.4M -> $170.6M; Product Services
(19% NCI) at book net assets $149.5M -> $28.4M. MARKS-DEPENDENT (re-derive on VLGC curve
re-fits; the drift gate catches the move) and STATIC under scenario vessel_scale (known
second-order limit, India ≈13% of fleet value). Alternatives considered: book NCI ($118.5M
— anti-conservative, overstates attributable NAV); full India exclusion (distorts a
consolidated, operationally-integrated sub); a §11.9 multi-sleeve dispatch (heavy for one
name — revisit if NCI names multiply).

**Known limit (documented):** Product Services' trading EARNINGS sit outside the strip
(the engine models shipping TCE only) while its net assets/G&A are carried — deliberately
conservative; Q1-2026 PS NPAT was $97.9M (mostly unrealized MTM swing).

**Cost/dividend:** opex $8,800/day (issuer KPI, FY2025 per-calendar-day-owned); G&A $76.5M
(FY2025, whole-group incl PS — conservative); interest $38M (Q1-2026 annualized; FY2025's
$55M reflected since-repaid borrowings); tax 0.005 (shipping leg ~0.3-0.5%; the Q1 $24.3M
group tax is almost entirely PS Singapore trading + India). Dividend: the FORMAL 20-F
policy — 50% of Shipping NPAT, enhanced to 75%/100% below 30%/20% net leverage; at 26.3%
net leverage -> payout_ratio 0.75 of (shipping-only, = modeled) EPS.

**§15 screen (BW Group bloc), run at onboarding — N/A-GATED, no haircut:** BW Group
(Sohmen) 31.99% (48,407,126 sh, 20-F Item 7) — a bloc, NOT majority; BWLP trades ~1.0x
P/NAV (0.97 Jul-3) so the §15.7 median-P/NAV gate records N/A. Related-party vessel sales
INTO the 52%-owned India sub (Chinook/Pampero Mar-2025 ~$75M) = TRIPWIRES (watch pricing
of future drop-downs vs broker marks), not evidence of extraction — kept quality_flag
standard + recency-downweighted in the §9.9 sample.

**Watchlist vintage (2026-07-03 Pareto daily, same-vintage):** kr 181.9 -> $18.52 (Jul-3
FX 0.101838, the MPCC/BRUT convention; yahoo_symbol BWLP.OL + quote_currency NOK for the
feed); P/NAV 0.97; fwd P/E 9.9. analyst_target = Pareto TP NOK 172 (2025-09-02, STALE —
flagged; NAV re-pegged NOK 171 on 2026-05-13; refresh at the next research note).

**Reconciliation baseline (first-run):** tool NAV $15.80 vs broker $19.09 -> gap −17.2%,
SANITY=OK, k_broker ~1.2. FV $15.43 / PW $14.46 (EV −21.9% at $18.52). Position relabeled
"rich · cycle position (not a short)"; WEIGHT-ROBUST (sign stable A/B/C).

**v1 LOCK PRE-READ — MISS (0/2; this name −17.2%):** sector held PROVISIONAL·v1-lock-miss
(SECTOR_V1_UNLOCKED), handoff_ready=False. Same direction as Dorian — see lpg_log for the
lock analysis + the no-tuning rule. OWNER ITEMS: the lock ruling; the NCI convention
(#1 above); the baseline ratify (sequenced with pending decision #1).

---

## 2026-07-10T20:20:47+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:12:11+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:06:28+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
- Sector: lpg

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-07-10T20:04:32+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $18.52
- Single-point FV: $15.43
- Scenario PW FV: $14.46 (EV -21.9%)
- NAV / share: $15.80
- Position: **TRIM/SHORT (overvalued)**
- Broker spread: +14.8pp (k_broker 1.16)
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

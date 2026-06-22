# CAPT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

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

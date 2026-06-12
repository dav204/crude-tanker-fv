# CAPT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

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

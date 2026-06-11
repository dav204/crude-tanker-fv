# CAPT — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

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

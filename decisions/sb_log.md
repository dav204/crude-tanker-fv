# SB — Decision Log

Chronological record of model state at each pipeline run plus the investment
decisions taken (or explicitly not taken). Newest entries appear at the top.
Auto-prepended sections capture model state; the `**Decision:**` line is
where you annotate what you actually did and why.

(METHODOLOGY §7.8 + decisions/README.md describe the auto-prepend convention.)

---

## 2026-06-30T14:55:13+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.36
- Single-point FV: $10.17
- Scenario PW FV: $9.97 (EV +56.8%)
- NAV / share: $10.47
- Position: **BUY (undervalued)**
- Broker spread: -44.2pp (k_broker 0.81)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-30T13:41:38+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.36
- Single-point FV: $10.17
- Scenario PW FV: $9.97 (EV +56.8%)
- NAV / share: $10.47
- Position: **BUY (undervalued)**
- Broker spread: -44.2pp (k_broker 0.81)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -1.3% | Δscenario FV: -1.3% | ΔNAV: -1.3% | Δspread: +1.9pp

**Decision:** Newbuild Amendment 2 — eco/scrubber spec VERIFIED against SB's own 6-K (NOT a
market move). The interim run below (+2.9%) carried scrubber=true on the 8 NBs, set on
peer-consistency (BRUT/CAPT/FRO do). On re-check that was the peer-number trap: SB's 6-K
discloses scrubbers ONLY on the existing 45-vessel fleet ("20 vessels, incl all Capesize"),
makes NO scrubber claim about the Kamsarmax newbuilds (no scrubber column in the orderbook
table), and 2 NBs are dual-fuel methanol (no scrubber). Adversarially verified vs the live
6-K — could not overturn. **Corrected scrubber→false**, backing out a fabricated +$0.14/sh.
**eco stays true** (§3.1 post-2014 rule + disclosed "IMO GHG Phase 3 - NOx Tier III"). So SB's
true newbuild-convention move is **+1.6%** ($10.31→$10.47, eco premium only), not +3.0% — much
closer to the registered "flat" prediction; the +1.4% over-shoot was the peer-borrowed flag.
**Combined-with-Thread-1, corrected:** Thread-1 age-0 (+5%) + newbuild (+1.6%) ⇒ SB ~**+6.6%**
less cheap than pre-Thread-1 (not +8%), **still robustly cheap (BUY)** — and the cheap margin is
wider than the interim framing implied. Durable fix: newbuild_specs.yaml + provenance guard now
require every on-curve NB's value flags to trace to the name's own filing. SANITY n/a (approx).

---

## 2026-06-30T13:13:01+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.36
- Single-point FV: $10.30
- Scenario PW FV: $10.10 (EV +58.8%)
- NAV / share: $10.61
- Position: **BUY (undervalued)**
- Broker spread: -46.1pp (k_broker 0.80)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: +5.1% | Δscenario FV: +4.4% | ΔNAV: +2.9% | Δspread: -4.5pp

**Decision:** Newbuild convention standardized to §9.6 on-curve delivered-less-commitment
(2026-06-30) — NOT a market move. SB was the lone dry-bulk advances-only name (+$100M, no
delivered value, no obligation). The 8 Kamsarmax in the orderbook AT 2026-03-31 are now on
the curve at age-0 delivered-market PV (sb.yaml NB rows), with the REMAINING commitment
$227.5M subtracted and advances → 0 (6-K accession 0001317861-26-000033; 8-NB quarter-end
state, not the 11-NB June orderbook). NAV +2.9% ($10.61). **Direction note:** I pre-registered
SB ~FLAT; it came in modestly UP (+3.0%) because my hand-prediction omitted the eco+scrubber
premium the curve applies to newbuilds (BRUT/CAPT/FRO all carry eco=true on NB rows — the input
is correct and required for consistency, my arithmetic was short; NB pre-reg Amendment 1).
**Combined-with-Thread-1 (the SB canary, in one place):** Thread-1 dry-bulk age-0 (+5%, less
cheap on the NAV denominator) + this newbuild move (+3%) ⇒ SB ~+8% less cheap than pre-Thread-1,
**still robustly cheap on both bases (BUY)** — the cheap read survives both adjacent basis moves.
Reconcile SANITY n/a (approx-pnav; +46% gap within the ±50% bug gate). PAUSE for owner review
before re-ratify.

---

## 2026-06-29T23:45:25+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.36
- Single-point FV: $9.80
- Scenario PW FV: $9.67 (EV +52.0%)
- NAV / share: $10.31
- Position: **BUY (undervalued)**
- Broker spread: -41.6pp (k_broker 0.77)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: -0.03 | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: -0.6pp

**Decision:** _[pending annotation]_

---

## 2026-06-29T22:10:56+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.80
- Scenario PW FV: $9.67 (EV +51.3%)
- NAV / share: $10.31
- Position: **BUY (undervalued)**
- Broker spread: -41.0pp (k_broker 0.77)
- Sector: dry_bulk

**Material deltas since last run:**
- ⚑ broker spread -6.3pp
- Δprice: no change | Δsingle FV: +3.4% | Δscenario FV: +3.4% | ΔNAV: +5.0% | Δspread: -6.3pp

**Decision:** Thread 1 basis correction (not a market move). Dry-bulk age-0 moved from CONTRACT to RESALE basis (Pana $38M->$46M, Post-Panamax $38.5M->$46M) — the cross-sector comparability fix. Only SB's <5yr Pana/Post-Panamax tonnage reprices UP (its older Pana/PPMX bulk is unaffected by an age-0 change), so NAV +5.0%: SB becomes modestly LESS cheap on the NAV denominator — the honest direction, pre-registered. Accepted pending owner review; re-ratify deferred.

---

## 2026-06-29T14:48:15+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.48
- Scenario PW FV: $9.35 (EV +46.3%)
- NAV / share: $9.82
- Position: **BUY (undervalued)**
- Broker spread: -34.7pp (k_broker 0.80)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: -2.4% | Δscenario FV: -1.8% | ΔNAV: -3.2% | Δspread: +4.3pp

**Decision:** ΔNAV -3.2% ($10.14 → $9.82) is the **P2 dry-bulk fidelity fix (§11.7.10),
not a market move or bug.** SB's 16 old/large 85-95.8k hulls were split out of the
collapsed 82k "Pana" class into their own issuer-classified **Post-Panamax** class on a
FLAT value curve, removing the dwt-scaling 1.12-1.17× over-mark on the 92-95.8k cohort
(it had them ABOVE modern Kamsarmax; they trade at a per-tonne discount). The new curve
is anchored on the Pareto SBLK NAV table broker value mark ($19.0M at 96k/15.3yr); no S&P
print of an 85-96k hull exists in the archive. Also wired the disclosed 6-K charter rates
(Pana avg $17.3k, Post-Panamax $18.5k gross/day) — covered-leg revenue now reflects
contracted rates vs the FFA front ($20.8k); consensus-EPS gap +126% → +118% (the residual
is the structural FFA-peak-vs-Street-mean-reversion gap, mitigated by low w_earn, not a
class artifact). SANITY still OK (tool NAV +39.6% over book is mark-driven, §11.7.10).
Accepted; baseline to be re-ratified ("P2 Post-Panamax split + SB charter rates").

---

## 2026-06-28T19:30:21+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T18:45:16+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T13:49:49+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:21:26+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Deltas since last run:** _(no material moves)_
- Δprice: no change | Δsingle FV: no change | Δscenario FV: no change | ΔNAV: no change | Δspread: no change

**Decision:** _[pending annotation]_

---

## 2026-06-28T03:18:37+00:00 — Pipeline run (auto)

**Model state:**
- Current price: $6.39
- Single-point FV: $9.71
- Scenario PW FV: $9.52 (EV +49.0%)
- NAV / share: $10.14
- Position: **BUY (undervalued)**
- Broker spread: -39.0pp (k_broker 0.78)
- Sector: dry_bulk

**Status:** _First snapshot — onboarding baseline._

**Decision: ONBOARDED 2026-06-27 — 4th dry-bulk validator (Safe Bulkers, NYSE: SB).**
Greek dry-bulk pure-play, Q1-2026 6-K (CIK 1434754). **43 on-curve owned vessels**
(36 Pana = 8 Panamax + 12 Kamsarmax + 16 Post-Panamax; 7 Cape) + 2 held-for-sale
off-curve at the $30.2M carrying value (Pedhoulas Commander, Xenia) + 1 chartered-in
excluded. 11 NB (10 Kamsarmax + 1 Cape). 8.00% Series C/D preferred = $100M (subtracts
from common NAV). Common shares 101.83M.

- **§15 governance — DECLINED the haircut** (`governance_discount_pct = 0`), carry with
  the related-party fee load as the headline tripwire. SB is Hajioannou-controlled
  (~47.5% via Vorini, sole voting power) and the three Managers (Safety Management
  Overseas / Safe Bulkers Management / Monaco) are family-controlled: €950/day per vessel
  + €5.0M/yr ≈ ~$22M/yr ≈ **~1.5% of GAV — the HIGHEST of the declined §15 names** (vs
  CMBT ~0.2%). But it is ~market-rate full ship-management (not an external-manager
  promote / incentive-on-NAV), dividends are pari-passu (common $0.06/qtr + preferred
  $0.50/qtr both pro-rata), and SB's discount-to-NAV is sector-wide (all dry-bulk names
  <1x), not governance-specific extraction. Held un-haircut for consistency with the
  other 3 dry-bulk validators (SBLK/GNK/CMDB, all un-haircut). Tripwires: the €950/day
  fee rising / off-market; above-market related-party drop-downs sans fairness opinion;
  common-dividend suspension while the family is paid; control → squeeze-out.
- **Reconciliation BASELINE (first-run):** tool NAV **$10.14** vs broker NAV **$7.26**
  (APPROX P/BV proxy, consensus_pnav 0.88 = price/common-book $7.30) → **gap +39.6%,
  SANITY = n/a** (APPROX cohort — NO Pareto coverage, verified 0 mentions in 135 2026
  dailies; no public VIE NAV). Scenario FV $9.52 vs price $6.39 → **EV +49%, BUY**.
- **THE +39.6% WIDE GAP — explained, not a bug** (SANITY n/a but documented per the
  "wide spread is a call or a bug" discipline): the tool marks SB's 43 on-curve vessels
  at **$1,351M vs the 6-K vessels-net book $1,061M (+27%)**. Two drivers: **(1) SB's book
  is conservative depreciated/impaired cost** — $24.7M/vessel average for a Kamsarmax/Cape
  fleet (avg age 10.5y) sits well below market in this strong dry-bulk cycle; this is most
  of the gap and is NOT a tool error (book understates, the tool marks to the transaction-
  anchored curves). Against the only external market-NAV proxy (~$8.40/sh non-broker model)
  the gap is ~+21%. **(2) Post-Panamax over-valuation — the §11.7.10 limitation, and SB
  exercises it more than any name** (16 Post-Panamax of 36 Pana-class, incl. 6 at 92-95.8k).
  The §11.7.1 collapse values Post-Panamax at the Kamsarmax "Pana" curve, and dwt-scaling
  lifts the 85-96k hulls 1.04-1.17× off the 82k baseline — generous for OLD (2006-2013)
  Post-Panamax that trade at a per-tonne discount. (Measured: the dwt-scaling itself adds
  only ~$0.20/sh; the larger effect is the base Pana curve treating Post-Panamax =
  Kamsarmax, ~$0.3-0.6/sh.) **Net: treat the +49% EV as the high end — the NAV is mark-rich
  and book-anchored; a more conservative read (model NAV $8.40 / common book $7.30) still
  has SB cheap-to-fairly-valued at $6.39.**
- **Refinement candidate:** SB makes the strongest case on the watchlist for a dedicated
  **Post-Panamax sub-class** (separating ~85-96k from the 82k Kamsarmax curve) — flagged
  in METHODOLOGY §11.7.10. Deferred (out of scope for the onboarding); revisit if the
  Post-Panamax book proves to drive a mis-call.
- Baseline re-ratified to include SB @ this first-run gap.

**Decision:** _[pending — fill in the four input YAMLs + watchlist row, then
run `python -m crude_tanker_fv.pipeline {QUARTER}`. After the first run, the
pipeline prepends a structured model-state entry above this line.]_

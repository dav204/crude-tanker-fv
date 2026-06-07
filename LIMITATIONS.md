# Limitations & Validation Status

The "where does this go wrong?" doc. Designed to be the first thing a
sceptical external reader looks for after [the README](README.md) — explicit
documentation of where the framework breaks down, what's deliberately out of
scope, and what's known to be approximate. Long-form treatment lives in
[METHODOLOGY.md](METHODOLOGY.md); this doc summarises and points there for
depth.

## 1. Hard framework limitations (acknowledge, don't act on the signal)

### §15 — governance / structural-NAV-trap discount (new 2026-06-06)

The framework's NAV machinery answers **"what are the assets worth?"** It does
NOT answer **"what will the market pay given how the controlling shareholders
will allocate them?"** For controlled-FPI / low-payout / related-party structures
the two questions diverge persistently — the market clears at 0.4-0.6x asset NAV
across cycles, not just at a single quarterly snapshot. The framework's pre-
haircut BUY signal on these names is **structurally unreliable** without an
explicit governance overlay.

**The schema knob:** `BalanceSheet.governance_discount_pct` ([0, 1], default 0).
When set, haircuts the NAV term in `blend_fair_value` and the strip's terminal
value. Broker-NAV sweep / `k_broker` operate on UNDISCOUNTED asset NAV (those
diagnostics answer the asset-side question).

**Names exhibiting the pattern:** TEN (first case, onboarded 2026-06-06 with
30% haircut). Other archetypes if onboarded: DSX, SBLK, CMRE, smaller
Greek-family-controlled FPIs.

**Symmetric to §12** (high-payout pure-plays at peak — framework UNDERvalues
because dividend stream is the thesis). Here the framework OVERvalues because
asset NAV won't be realised for common shareholders at full face value.

Full discussion: [METHODOLOGY §15](METHODOLOGY.md#15-framework-limitation--governance--structural-nav-trap-discount-added-2026-06-06).

### §13 — scenario-weight stability under infrastructure shocks (new 2026-06-01)

The scenario weights in any sector are **conditional on the supply regime
observed at the time of the lock** — they don't auto-update. A major
infrastructure event (multi-train LNG facility offline / online, sustained
Hormuz disruption, sanctioned-flow re-routing, new LNG basin operations)
can render the locked weights stale faster than the per-scenario forwards.
Treat any weight lock as **point-in-time best estimate**, not a stable
parametric calibration. Methodology owner must re-evaluate after material
infrastructure shocks.

Worked example: LNG Set B → Set B-revised transition (2026-06-01). Set B's
55% on `glut_base` was overrun by the Ras Laffan Trains 4 & 6 disclosure
landing within weeks of the lock; Set B-revised shifted 10pp toward the
constructive band. **CCEC's position flipped HOLD → BUY** as a direct
consequence — a real weight-driven sensitivity, not a calibration error.

**Diagnostic surface:** `outputs/lng_weight_robustness.md` (refresh quarterly
via `python scripts/lng_weight_comparison.py`) shows per-LNG-name PW FV and
position under both Set B and Set B-revised. Weight-robust names (small
EV%-spread, no position flip) are robust under reasonable alternative
weights; weight-driven names (large spread or position flip) require sizing
discipline against the call's dependence on which weight set you trust.

Full discussion: [METHODOLOGY §13](METHODOLOGY.md#13-framework-limitation--scenario-weight-stability-under-infrastructure-shocks).

### §12 case — high-payout pure-plays during cycle peaks

The NAV + dividend-strip framework **systematically undervalues high-payout
single-asset-class equities during cycle peaks**. This is a structural feature
of the model, not a calibration error — closing the gap would require a
separate cycle-aware dividend-window model layered on top of the current
strip, which is out of scope.

Currently affected names on the watchlist:

- **NAT** (Nordic American Tankers — pure Suezmax, ~100% payout). Tool reads
  P/NAV ≈ 2.0× during 2026-Q2 spot strength as "rich"; market is pricing the
  near-term dividend stream as the investment thesis. Don't act on the
  tool's TRIM signal for NAT without an explicit dividend-window overlay.
- **STNG** (Scorpio Tankers — buyback-channel variant). The dividend strip
  captures only the $0.45/qtr fixed dividend; aggressive buybacks (~$300M /
  Q1+April) flow through terminal NAV but not the cash-flow strip. Tool FV
  is **structurally conservative** on buyback-dominated names.

Other archetypes that would exhibit the pattern if onboarded: SBLK (peak dry
bulk), DLNG / HSHP (peak VLGC). Full discussion: [METHODOLOGY §12](METHODOLOGY.md#12-framework-limitation--high-payout-pure-plays-during-cycle-peaks).

### Vessel-mark uncertainty — mark-driven vs mark-validated bucket

The broker-NAV sweep classifies every name as mark-validated (tool and broker
agree on direction; ≤10pp EV%-spread) or mark-driven (the call would flip
under reasonable vessel-mark choices; >10pp spread). For mark-driven names
the tool FV signal is genuinely sensitive to mark assumptions — don't size
positions based on tool output alone.

Current mark-driven names (broker NAV from Pareto Shipping Daily 4 Jun 2026):
TNK (+10pp), TRMD (+22pp), INSW (+22pp), STNG (+27pp), ASC (+29pp), HAFN (+31pp),
NAT (+51pp), FLNG (-20pp, tool above broker), CCEC (-15pp, tool above broker).
The wide-spread cases (NAT, HAFN, ASC) are explicit "trust the marks you trust"
decisions. See [the broker sweep section of the README](README.md#sample-output-broker-nav-sweep)
for the live table.

> **STNG + TRMD reclassified mark-validated → mark-driven (2026-06-04).** A check
> against the Pareto Shipping Daily 4-Jun P/NAV column found our `consensus_pnav`
> inputs for STNG (0.87) and TRMD (1.00) were stale APPROX values, materially
> above Pareto's actual 0.70 / 0.83. Correcting them raised broker NAV (STNG
> $90.80 → $108.00; TRMD $27.25 → $33.98) and widened the tool→broker spread
> (STNG +8pp → +27pp; TRMD +2pp → +22pp). STNG is no longer a mark-validated
> name. The reclassification is confirmed independently by VIE NAV
> (`outputs/vie_nav_xref.md`): VIE ≈ broker on both. **Pareto publishes no P/NAV
> for NAT, ASC, or CCEC** — those broker NAVs remain unanchored APPROX estimates.

### Forward-earnings uncertainty — consensus-EPS cross-check (added 2026-06-04, §9.11)

The earnings-leg analog of the broker-NAV sweep. Our dividend strip's near-term
EPS is FFA-forward-curve-implied; at a cycle peak that runs **structurally hotter
than sell-side consensus**, which prices mean-reversion. The 2026-06-04 run shows
**every name's tool NTM EPS above consensus by +72% to +462%** (`outputs/consensus_eps_xref.md`).
This is not a bug — the cycle weighting down-weights the strip (`w_earn` 0.30 at
peak) precisely when the gap is widest, so the hot earnings barely reach the
headline FV. The names to watch are the *below-mid-cycle* ones where `w_earn` is
high and the gap is therefore *least* mitigated: **CCEC (+219%, w_earn 0.60)** and
FLNG (+83%, w_earn 0.60). CCEC's earnings gap is an independent corroboration of
its weight-driven-BUY fragility (see below) — its BUY leans partly on forward
earnings the street doesn't share. Don't read the per-name EPS gap as a
calibration error; read the gap-vs-`w_earn` pairing.

### Weight-driven names — LNG sector (added with §13)

Mirroring the mark-driven discrimination, names whose position would flip
under a reasonable alternative weight set are flagged as **weight-driven**.
Currently identified:

- **CCEC** — flips HOLD → BUY between Set B and Set B-revised (EV spread
  +15.1pp; alpha = 0.40 to flip). CCEC's $2.25B newbuild orderbook
  provides ~2× the scenario torque of FLNG's mature TC-heavy book; the
  same weight shift moves CCEC's PW FV 2× as much as FLNG's. The BUY signal
  under Set B-revised is a leveraged expression of the LNG-tight thesis,
  not a NAV-anchored value play.

Weight-robust names in the same comparison: FLNG (EV improves +6.2pp,
position TRIM/SHORT in both weight sets — does not flip even under
Set B-revised).

## 2. Coverage gaps (deliberately out of scope)

### Vessel classes

- **Clean-product Handysize (~37-40k DWT)** — *resolved 2026-06-05.* A Handysize
  class was added to `vessel_value_curves.yaml`; HAFN's 22 Handies and ASC's 2
  product Handies moved from off-curve `working_capital_net` onto their fleet
  manifests (METHODOLOGY §11.5). NAV effect small and as-forecast (HAFN +$0.04/sh,
  ASC +$0.18/sh; no position flips). Earnings proxy to MR in v1 (flagged).
- **Chemical Handymax (38k IMO-II coated)** — *resolved 2026-06-05.* A
  Handymax class was added to `vessel_value_curves.yaml` anchored on STNG's
  disclosed marks ($14.3M/vessel at avg-age 15); curve NB $45M / 5yr $32M /
  10yr $20M / scrap_25 $4M. STNG's 14 Handymax migrated from off-curve
  `working_capital_net` ($200M) onto the fleet manifest (on-curve $205M, net
  NAV +$0.10/sh). Rate path = MR proxy, empirically validated by STNG Q1+Q2
  2026 disclosed Handymax pool/spot rates ≈ MR rates (METHODOLOGY §11.5).
  Earnings routing v1; APPROX-flagged mid-age anchors (single-anchor inference).
- **Sub-25k stainless chemical Handy** — *still a gap, now narrower.* ASC's 4 ×
  25k Japan-built 2015 stainless chemical hulls stay OFF-CURVE in
  `working_capital_net`: sub-25k stainless is a structurally smaller specialty-
  chemical pool, and the new 38k IMO-II coated Handymax curve would overvalue
  them (~$60M aggregate at age 11 vs ASC-disclosed ~$13M/vessel). Bounded
  (<5% of ASC NAV). Pure-chemical parcel operators above Handysize (Stolt-
  Nielsen / Odfjell) remain un-onboardable until a stainless-steel chemical
  Handymax curve + chemical-specific rate economics land — Odfjell's 2027-29
  NB at $72.5M/vessel anchors the higher-priced stainless curve but no
  watchlist name has that exposure yet.
- **DP2 shuttle tankers** — *resolved via convention 2026-06-05 PM.* No full
  `Shuttle` value class (no observable disposal market, no spot rate, no FFA),
  but METHODOLOGY §11.6 documents an **off-curve-at-contracted-book convention**:
  in-water shuttle vessels carry at NPV of disclosed contracted cash flows (Σ
  day_rate × earning days, discounted at WACC) + a Suezmax-curve residual at
  TC expiry; NB shuttle hulls flow through `newbuild_capex_commitments` at
  contract price (no §3.1 hot-market markup). The figure lives in a dedicated
  `shuttle_contracted_book` line on the balance sheet (`BalanceSheet` schema)
  and adds to NAV like working capital. **The TEN onboarding architectural
  blocker is now methodologically closed**; remaining TEN work is data
  assembly (4 YAMLs, integration test, §6 entry) — see `decisions/ten_log.md`.
  Same convention available to any future name with contracted-book vessel
  sleeves the framework cannot spot-value (FPSO operators, etc., would need
  the convention extended or their own asset class).
  **Onboarded 2026-06-06:** TEN now on the watchlist as the first 3-sleeve
  hybrid + first name with `shuttle_contracted_book` populated ($453.1M
  in-water NPV) + first §15 case (30% governance haircut). Post-§15 tool
  PW FV $49.37 vs price $44 (EV +12%, **BUY**) — consistent with VIE
  Bullish $51.50. The shuttle convention is APPROX on the Brasil 2014 /
  Rio 2016 extension rate ($60k/day estimate of the 6-K "increased rate"
  disclosure); refresh when actual rate disclosed.

### Sectors

- **Dry bulk** — would be greenfield: new value curves, different cycle
  drivers (Chinese steel demand, BDI), different scenario set. Not on
  roadmap.
- **Offshore** (drillships, OSVs, FPSOs) — entirely different value
  structure. Out of scope.
- **Chemical tankers above Handysize** — partially covered via the LR2_clean
  rate keys for dual-use vessels, and via the new 38k IMO-II coated Handymax
  curve (2026-06-05) for STNG. Pure-chemical operators (Stolt-Nielsen,
  Odfjell) would still need their own scenario set and a stainless-Handymax
  curve anchored at the Odfjell-NB ~$72.5M/vessel level.

### Pure-product names — onboarding status

- **TRMD** (Torm — full 3-class MR + LR1 + LR2_clean) and **HAFN** (Hafnia,
  large diversified product) are now **onboarded** (2026-06-03 / -04) via the
  existing `sectors.product` infrastructure. HAFN's 22 Handysize and ASC's 2
  product Handies moved on-curve 2026-06-05 (§2 vessel-classes above). The
  product-universe gap that remains is the chemical Handy/Handymax residual
  (§2) and pure-chemical parcel operators. See METHODOLOGY §1.

## 3. Known approximations (documented, not blockers)

### Per-ticker

- **MR curve eco/scrubber treatment.** The MR curve is "eco-inclusive
  modern-spec" with both premiums = 0. Older / non-eco MRs (ASC's 5×2013
  Eco-Mod hulls, STNG's 5×2013 MRs) are valued at the modern-spec curve and
  modestly over-valued (~$15M aggregate per name, <1% of NAV). Flagged in
  METHODOLOGY §6 per-ticker entries.
- **STNG's 2 VLCC newbuilds (2H 2028 delivery).** STNG's first crude
  exposure. Currently valued newbuild-at-market via balance sheet (they
  deliver past the 8-quarter strip horizon, no scenario impact). When they
  enter service, the hybrid carve-out architecture (today INSW-only) will
  need to extend to STNG.

### Per-input

- **APPROX consensus_pnav entries** on **NAT, ASC, CCEC** — Pareto Shipping
  Daily does **not** publish a P/NAV for these three (shown as "-" in the 4-Jun
  report), so their broker NAVs remain unanchored estimates (NAT 0.85 band-
  midpoint, ASC 0.75 aggregator commentary, CCEC 0.90 ~book). The broker-NAV
  sweep's EV @ broker columns for these three carry meaningful uncertainty.
  *(STNG, TRMD, HAFN were APPROX until 2026-06-04; now real Pareto 4-Jun prints
  of 0.70 / 0.83 / 0.95 — the STNG/TRMD corrections reclassified both as
  mark-driven, see §1.)*

### Framework-level

- **Cycle weighting curve shape.** Step function across five bands.
  Could be a continuous logistic but step function is more interpretable.
  Open methodology decision in §9.
- **Terminal value at quarter 9 = 1.0× NAV.** Arguably should be 0.9× NAV
  (mid-cycle discount) or 1.1× NAV (structural undersupply). **Sensitivity
  swept 2026-06-05** (`outputs/terminal_value_sensitivity.md`): 3 names
  flip position at the literal §9.2 priors — TNK and STNG flip HOLD →
  TRIM/SHORT at 0.9×; FLNG flips TRIM/SHORT → HOLD at 1.1×. Other 9 names
  multiple-robust. Decision-relevant for those 3 names; informational
  elsewhere. Resolution still pending — needs a methodological prior, not
  more data. §9 open decision.
- **Discount rate = 11% flat.** Chosen heuristically. CAPM-derived rate
  with high beta + cyclical premium probably lands in the same range, but
  hasn't been validated. §9 open decision.
- **10-year mean TCEs are TC-anchored, not spot-anchored.** Our
  `historical_tce_means.yaml` reflects what a 1-year TC would have locked
  in over the 10-year window; spot-anchored means (e.g. VIE's published
  series) include deep-negative spot periods (VLCC TD3C spot was reported
  near −$34,845/day in 2020-2022 per SpotMarketCap) and are therefore
  structurally lower. **Both conventions are internally consistent; they
  answer different questions.** Our convention is the methodologically
  correct denominator for our cycle-position ratio because the numerator
  is also a TC (12M Compass). Cross-references to external "vs 10y
  average" multipliers (VIE, raw Baltic publications) are directionally
  useful but **numerically non-composable** with our cycle ratios. See
  METHODOLOGY §10 and `outputs/vie_market_rates_xref.md` for the worked
  example.
- **VIE methodology comparison — within-window structural adjustments
  (refinement 2026-06-04 PM).** VIE's published "Vs. 10y Avg" multipliers
  apply **class-specific structural-adjustment factors** on the denominator
  (1.0 dry bulk, **0.9 tankers + VLGC**, **0.7 LNG TFDE**) — explicit
  compensation for within-window structural changes (notably the TFDE →
  X-DF2.1 propulsion transition). Applying the factors and back-computing
  collapses the apparent gaps to within **~7%** for Suezmax / Aframax /
  MR / LNG, meaningful cross-methodology corroboration. The two
  approaches differ in whether structural adjustment is **implicit** (our
  TC anchor, captured via contemporaneous market-clearing prices) or
  **explicit** (VIE's class-specific factor application). Both
  methodologically defensible; converge on most classes. VLCC and LR2
  retain residual gaps (+42% / +24%) warranting separate investigation if
  calibration discipline ever calls for it. See METHODOLOGY §10 and
  `outputs/vie_market_rates_xref.md` for back-computed values.

## 4. What the tool was validated against

- **Per-sector validators:** DHT (pure VLCC) for crude; FLNG (pure modern
  LNGCs) for LNG; ASC (pure MR) for product. Each validator's fair value
  is band-locked in tests so structural regressions surface immediately
  (`test_dht_*`, `test_flng_v2_locked_weights_fv_band`,
  `test_asc_whole_company_fv_in_expected_band`).
- **Transaction anchoring:** Aframax curve recalibrated against TNK sale-
  leaseback prints (~$47.2M for 2016 builds); Suezmax against the TNK
  $53.5M disposal (NAT validator residual: +0.6%). Both stored in
  `inputs/market_data/transactions/{class}.yaml`; opt-in toggle in the
  pipeline.
- **Hybrid carve-out preservation:** INSW whole-company FV pinned within
  $0.20/sh across the v2 product-sector refactor. The refactor swapped the
  v1 shortcut (MR forwards under `sectors.crude`) for the clean
  `sectors.product` routing — proves the architectural change didn't
  disturb the answer.
- **Cross-name consistency:** the broker-NAV sweep's mark-validated bucket is
  **DHT, ECO, FRO** (k_broker 0.99-1.00, tool→broker spread ≤1pp), confirming
  the tool's VLCC/Suezmax/Aframax curves are consistent with broker consensus.
  (STNG was previously listed here; the Pareto 4-Jun P/NAV check reclassified it
  mark-driven at +27pp — see §1. No pure-product name is mark-validated: broker
  and VIE both mark product ~25-50% above our curves, the §14.6.1 LR2 cargo-
  switching option gap.)

## 5. What the tool was NOT validated against

- **Out-of-sample backtest.** The framework has not been run against
  historical quarters to test whether its TRIM/BUY/HOLD signals would have
  added value over time. The decision logs (§7.8) are the in-sample feedback
  loop being built up from 2026-Q1 forward.
- **M&A / sanctioned-flow / regulatory shock.** These are idiosyncratic
  risks the model doesn't see. Documented as caveats (§10).

## 6. License & advice disclaimer

This is research scaffolding, **not investment advice**. Outputs are model
estimates with uncertainty bands wider than the point numbers suggest,
especially on vessel marks without paid broker access. Don't treat the
tool's position recommendations as actionable signals on their own.

---

For long-form treatment of any item above, see:
- [METHODOLOGY §10 Caveats](METHODOLOGY.md#10-caveats)
- [METHODOLOGY §12 Framework limitation](METHODOLOGY.md#12-framework-limitation--high-payout-pure-plays-during-cycle-peaks)
- [METHODOLOGY §11.5 Product sector + Handysize gap](METHODOLOGY.md#115-product-sector--formalised-2026-06-01)
- [METHODOLOGY §9 Open methodology decisions](METHODOLOGY.md#9-open-methodology-decisions)
- [METHODOLOGY §6 Company-specific notes](METHODOLOGY.md#6-company-specific-notes) — per-ticker validation status and known gaps

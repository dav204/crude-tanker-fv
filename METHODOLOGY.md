# Crude Tanker Fair Value Tool — Methodology

## 1. Purpose & Scope

This tool produces an **independent fair value estimate per share** for crude tanker equities, used to validate and stress-test existing target prices on the watchlist. It is not a buy/sell recommendation engine; it is a structured methodology applied consistently across names so that disagreements between the tool and analyst targets can be diagnosed (input differences vs. weighting differences vs. genuine methodology divergence).

**Current coverage (8 names across 2 sectors as of 2026-06-01):**

*Crude tanker sector (`sectors.crude` — three-phase MoU framework):*

| Ticker | Company | Fleet focus | Notes |
|---|---|---|---|
| FRO | Frontline | VLCC + Suezmax + LR2 | Largest Western pure-play; absorbed 24 Euronav VLCCs; 9 Hemen VLCC NBs valued newbuild-at-market |
| ECO | Okeanis Eco Tankers | Modern VLCC + Suezmax | Youngest fleet, all-spot, eco design |
| DHT | DHT Holdings | Pure VLCC | ~22 VLCCs, simplest single-class structure; methodology validator |
| INSW | International Seaways | Crude + Product (whole-company) | Hybrid operator; v2 carve-out aggregates crude + product sleeves against tape price (§6, §11) |
| TNK | Teekay Tankers | Suezmax-heavy + Aframax/LR2 + 1 VLCC | Atlantic-skewed; 2 Suezmax NBs (S. Korean, 2027); active disposals + acquisitions; mostly spot |
| NAT | Nordic American Tankers | Pure Suezmax (18 vessels) | High-payout single-class — §12 framework limitation case |

*LNG sector (`sectors.lng` — glut-cycle framework):*

| Ticker | Company | Fleet focus | Notes |
|---|---|---|---|
| FLNG | Flex LNG | 13 modern 174k cbm LNGCs (MEGI / X-DF) | Mature TC-heavy fleet, no NBs; first sector port name |
| CCEC | Capital Clean Energy Carriers | 12 in-water LNGCs + 9 LNG NBs + 1 MGC + 8 gas NBs (MGC + LCO2) | Two-class operator (LNGC + MGC); aggressive newbuild program ($2.25B commit) |

*Product sector (`sectors.product` — five-scenario refining-margin / glut framework):*

| Ticker | Company | Fleet focus | Notes |
|---|---|---|---|
| ASC | Ardmore Shipping (NYSE:ASC) | 19 active MRs + 2 on-curve Handysize + 4 off-curve 25k chem + 1 MR HFS + 2 Handy NBs | First product-sector validator (2026-06-01); zero scrubbers; 2/3 of Adj. Earnings payout; clean-product Handies on-curve (2026-06-05), 4× 25k stainless chem remain off-curve as §11.5 chemical-Handy residual |
| STNG | Scorpio Tankers (NYSE:STNG) | 32 LR2 + 41 MR on-curve + 14 Handymax off-curve + 9 HFS + 10 NBs (4 MR + 4 LR2 + 2 VLCC) | First multi-class product name; ~95% scrubber-fitted; fixed $0.45/qtr dividend + aggressive buyback ($500M auth); §12 buyback-channel limitation; 2 VLCC NBs 2028 = first crude exposure |
| TRMD | Torm Plc (NASDAQ:TRMD) | 22 LR2 + 10 LR1 + 63 MR (95 total) + 8 MR NB resale program | First full-3-class product name (2026-06-03); first `lr1_clean` rate-forward use outside INSW; UK tonnage tax; variable Board-discretion dividend (~75% NI smoothed); mark-validated narrowest spread; VIE Bullish counter-signal |
| HAFN | Hafnia Limited (NYSE:HAFN / OSL:HAFNI) | 10 LR2 + 25 LR1 + 49 MR (84 on-curve) + 22 Handy off-curve + 12 chartered-in + 8 firm MR NBs | First IFRS-reporting name (2026-06-04); first pool-operator; largest product fleet on watchlist; Bermuda+Singapore tonnage tax; explicit 80% NPAT dividend policy; BW Group 44.18% controlling holder; $395M TORM equity stake; VIE Bullish counter-signal |

**v2 milestones already completed:**

- Hybrid carve-out for INSW (crude + product sleeves), aggregated to whole-company FV (§6)
- Sector portability layer (`sectors.crude` / `sectors.lng`) with per-sector scenario sets and cycle anchors (§11)
- LNG sector live with sector-specific weights (Set B), `structural_reset` scenario curated, `vessel_scale_multiplier` mechanism (§11.3)
- Transaction-anchored curve recalibration for Aframax + Suezmax (§9.9)
- Broker-NAV sweep diagnostic (mark-robust vs mark-driven classification, §9.9)
- LNGC X-DF2.1 propulsion-premium recalibration + MGC gas-carrier sub-class (§3.1)
- §12 framework limitation documented for high-payout pure-plays during cycle peaks

**Out of scope for current build:** Pure chemical tankers — IMO-II/III stainless parcel trade (Stolt-Nielsen / Odfjell) and the **sub-25k stainless chemical Handy** residual (ASC's 4 × 25k stainless chem stay off-curve; the new Handymax curve covers 38k IMO-II coated only — §11.5 / LIMITATIONS §2). NOTE: **chemical Handymax (38k IMO-II coated) is now ON-curve** (Handymax class added 2026-06-05; STNG's 14 hulls migrated from `working_capital_net` $200M to on-curve $205M; rate path = MR-proxy validated by STNG Q1+Q2 2026 disclosed rates ≈ MR — §11.5). NOTE: **clean-product Handysize (~37-40k) is now ON-curve** (Handysize class added 2026-06-05; HAFN's 22 + ASC's 2 product Handies migrated from off-curve — §11.5). **Dry bulk is now methodology-unlocked as of 2026-06-09** via `sectors.dry_bulk` (see §11.7) — first fully greenfield sector after the v1 crude/LNG/product builds; ships with three classes (Cape / Pana / Supra-Ultra), the four-scenario Bulk Set A weight family, and a 22-month Pareto-archive-derived empirical cycle anchor (Cape $23,650, Pana $11,900, Supra-Ultra $13,930 USD/day). Validators v1: SBLK + GNK (Pareto-anchored) + CMDB (APPROX-anchored). Code wire-up + name onboarding Week 2. Offshore. (Standalone product tankers — STNG / TORM / HAFN / ASC — are **unlocked** as of 2026-06-01 via `sectors.product`; see §11.5. **ASC onboarded 2026-06-01** as the product-sector methodology validator; **STNG onboarded 2026-06-01** as the first multi-class product name; **TRMD (Torm) onboarded 2026-06-03** as the first full-3-class product name; **HAFN (Hafnia) onboarded 2026-06-04** as the first IFRS-reporting + first pool-operator + largest product fleet on the watchlist. **TEN (Tsakos) onboarded 2026-06-06** — first 3-sleeve hybrid on the watchlist (crude + product + LNG, with the DP2 shuttle sleeve handled OFF-CURVE via `shuttle_contracted_book` per METHODOLOGY §11.6) **and first §15 case** (governance / value-trap haircut). The 2026-06-04 deferral closed in one session after the architectural unblock (2026-06-05 PM) shipped: (1) `preferred_equity` schema; (2) §11.6 off-curve-at-contracted-book convention + `shuttle_contracted_book` schema; (3) `lng_carve_out()` + 3-sleeve aggregator. A §15 governance haircut (30%) was added 2026-06-06 to account for the persistent market discount on controlled-FPI structures with related-party transactions and low common payout. TEN's headline (post-§15): asset NAV $88.56, PW FV $49.37 vs price $44.00 (EV +12%, **BUY**) — consistent with VIE Bullish $51.50. Full §6 entry below.)

## 2. Core Valuation Framework

### 2.1 The blended formula

```
Fair Value per share = w_nav × NAV/share + w_earn × DivStrip_implied_price
```

Two independent valuation lenses are computed, then blended. The blending weight is determined by cycle position, not picked manually per name.

### 2.2 Why blend NAV and dividend strip for crude tankers

- **NAV alone** underweights what makes crude tankers special: when rates spike, cash conversion is so fast that 12–18 months of peak dividends can equal 40%+ of market cap. Ship values rerate to reflect this, but they lag — NAV captures the asset re-pricing late.
- **Pure DCF / earnings perpetuity** overweights cycle peaks and ignores mean reversion. Tanker rates are explicitly cyclical, with structural overbuild → undersupply cycles measured in 5–10 year arcs.
- **Blending** forces honesty about cycle position: at peaks, the dividend strip provides large near-term cash but the terminal value should not assume peak-forever; at troughs, NAV becomes the floor as ships trade below replacement cost.

Crude tanker equities also have a structural feature that justifies the blend: most public crude tanker companies operate **variable dividend policies** (60–100% of net income), so dividends are mechanically close to free cash flow. The dividend strip is therefore a reasonable cash-flow proxy without needing to model working capital or reinvestment separately.

### 2.3 Cycle position weighting

The weight on each lens flexes with current cycle position, measured as the ratio of the **12-month time-charter (TC) rate** to the **10-year historical mean TCE** for the relevant vessel class.

> **Cycle input = TC, not FFA (revised).** The cycle ratio uses the 12-month *fixed-rate TC* (what a charterer will pay to lock a year), not the FFA forward strip. The TC is a more conservative, less spike-prone read of the forward environment, and keeping it distinct from the FFA avoids double-using one curve. The **FFA forward curve remains the input to the dividend strip** (the actual cash-flow projection, §3.2). The two are deliberately different inputs with different roles.

| Cycle position (12M TC / 10yr mean) | w_nav | w_earn | Interpretation |
|---|---|---|---|
| > 1.5× | 0.70 | 0.30 | Late-cycle / peak — discount the cash but don't extrapolate it |
| 1.2× – 1.5× | 0.60 | 0.40 | Elevated — still cycle-aware |
| 0.8× – 1.2× | 0.50 | 0.50 | Mid-cycle balance |
| 0.5× – 0.8× | 0.40 | 0.60 | Below-mid — earnings depressed, NAV anchors |
| < 0.5× | 0.30 | 0.70 | Trough — NAV is floor; earnings rebuild dominates forward value |

Current cycle position as of model build (Q2 2026): VLCC spot rates running well above 10-year mean → late-cycle / peak weighting expected.

For multi-class operators (FRO, ECO, INSW), cycle weighting is computed at the **fleet-weighted-average** level using each class's own TC / 10yr ratio, weighted by class share of vessel value.

## 3. Component Methodology

### 3.1 NAV per share

```
NAV/share = (Σ vessel_market_values
             + cash_and_equivalents
             + working_capital_net
             − total_debt
             − lease_liabilities
             − newbuild_capex_commitments
             + advances_paid_on_newbuilds)
            / diluted_shares_outstanding
```

> **Newbuild treatment — value at market for material orderbooks (revised, decision 9.6).** The face-value form above (advances paid − remaining commitment) treats committed newbuildings at sunk cost. For names with a material orderbook in a market where newbuild contract prices sit below resale values (e.g. FRO's 9 Hemen VLCCs), this materially *understates* NAV by the embedded value of cheaply-contracted ships. In that case, include the committed newbuilds in the fleet at their **delivered market value** (curve value at age 0, with yard/eco/scrubber adjustments) and subtract only the **remaining commitment**; the advances are then embedded in that market value (set the advances term to 0 to avoid double-counting). For a single trivial newbuild (e.g. DHT) the face-value form is fine.

**Vessel market values** are looked up from a market value table keyed by (vessel class, age). Curve construction (revised):

- Four broker anchors per class — newbuild/prompt-resale (age 0), 5-year (age 5), 10-year (age 10), scrap (age 25) — taken from the broker term structure; the curve is **piecewise-linear** between them.
- Old-age acceleration falls out of the data (the 10→25 leg is steeper than 5→10) rather than from a free parameter; this fixed the mid-life over-valuation of the original 3-anchor + accelerating-discount form.

Indicative 5-year benchmarks (refresh quarterly from company disclosed sales, newbuild orders, and broker reports):

| Class | DWT (~) | 5-yr SH benchmark | Newbuild | 25-yr scrap |
|---|---|---|---|---|
| VLCC | 300,000 | ~$110M | ~$135M | ~$25M |
| Suezmax | 150,000 | ~$75M | ~$95M | ~$15M |
| Aframax | 110,000 | ~$65M | ~$80M | ~$12M |
| LR2 | 115,000 | ~$60M | ~$75M | ~$12M |

**Scrubber adjustment:** add a per-vessel premium (currently ~$2–3M for VLCC) for scrubber-fitted vessels, reflecting captured HSFO/VLSFO spread.

**Ice-class / eco-design:** apply +5% to base vessel value if eco-design (post-2014, fuel-efficient hulls and engines). Apply +5–10% for ice-class where present.

> **LNGC reinterpretation of `eco_premium_pct` (2026-06-01).** For the LNGC class only, the `eco_premium_pct` field denotes the **latest-generation propulsion premium** rather than the tanker-style "eco-design" hull/engine premium. The current LNG fleet is uniformly gas-fueled by construction (boil-off-gas LNG fuel), so the original semantics don't apply. Instead, `eco: true` marks **X-DF2.1** vessels (current latest WinGD evolution, +5% premium over the X-DF / MEGI / TFDE baseline curve); `eco: false` marks X-DF / MEGI / older-tech (TFDE) vessels priced at the baseline. The +5% reflects 2025-26 broker quotes ($12-15M premium on newbuild, narrowing modestly with age). Documented in the LNGC curve comments in `inputs/market_data/vessel_value_curves.yaml`. Forward-compatible: if a successor generation supersedes X-DF2.1, retag the relevant vessels' `eco` field — no curve change needed.

> **MGC gas-carrier sub-class (2026-06-01).** A second LNG-sector vessel class — `MGC` (Medium Gas Carrier) — covers 22-45k cbm dual-fuel multi-gas / LCO2 carriers. Added to capture CCEC's gas fleet (1 in-water LCO2 vessel `Active` + 8 NBs comprising 2 LCO2 incl `Amadeus` + 6 dual-fuel MGCs delivering Q2'26-Q1'29). The class routes through `sectors.lng.scenarios.<scenario>.mgc` forwards (LPG / ammonia / multi-gas trade cycle — less volatile than 174k LNGC, with a $20k/day 10yr mean vs $85k for LNGC) and `sectors.lng.cycle_anchors.mgc`. Curve anchors: newbuild $65M / 5yr $58M / 10yr $48M / scrap25 $10M (Korean dual-fuel modern). No propulsion-premium differentiation at v1 (MGCs are uniformly dual-fuel by construction); the `eco_premium_pct` field stays at 0. LCO2-capability premium is currently not separately priced (would be a vessel-level flag in a future iteration if the CO2 transport trade matures into a liquid resale-price segment).

**Yard-quality discount:** broker benchmarks reflect good-spec (effectively Korean/Japanese) tonnage, so apply a per-vessel haircut to lower-tier yards (multiplicative on hull value, by yard name). Indicative tiers: modern top-tier Chinese (Hengli, Dalian, SWS) ~5%; older Chinese (New Times, Longxue, Cosco) ~10%; distressed-era Chinese (Rongsheng) ~13%; ex-Hanjin-Subic / Philippines ~10% (yard bankrupt, no warranty/parts support). Korea/Japan yards: 0%. Report NAV both **with and without** the discount so it is a transparent assumption. (Material for FRO's Suezmax/LR2 sleeves; n/a for DHT's all-Korean fleet.)

### 3.2 Forward dividend strip (DivStrip_implied_price)

```
DivStrip_implied_price = Σ_{q=1..8} [DPS_q / (1 + r)^(q/4)]
                       + TerminalValue_{q=9} / (1 + r)^(9/4)
```

Where:

- **DPS_q (dividend per share, quarter q):** depends on the policy type (§4.3), where `floor` is the EPS threshold deducted before payout:
  ```
  variable          (DHT, FRO, ECO, NAT):       DPS_q = max(base_dividend, payout_ratio × max(0, EPS_q − floor))
  base_plus_variable (INSW, TNK, FLNG, CCEC):   DPS_q = base_dividend + payout_ratio × max(0, EPS_q − floor)
  ```
  In the **variable** form the base is a *minimum floor under* the dividend (e.g. DHT pays 100% of EPS but never less than its ~$0.025 nominal base; NAT pays ~100% with a small fixed floor). In the **base_plus_variable** form the base is paid *in addition to* the variable part. INSW pays $0.12 base + supplemental. TNK / FLNG / CCEC use the base_plus_variable wrapper with `payout_ratio: 0.0` — i.e. fixed-only dividend, no variable component, because each retains the bulk of earnings for fleet renewal / NB programs (TNK $0.25/qtr, FLNG $0.75/qtr, CCEC $0.15/qtr). (Earlier drafts used a single additive form, which over-pays a floor-type policy by the base every quarter.)
  ```
  EPS_q = (NetTCE_revenue_q − OPEX_q − G&A_q − interest_q − tax_q) / shares
  NetTCE_revenue_q = Σ_class (vessels_class × days_class × TCE_class_q × (1 − offhire_rate))
  ```

- **TCE_class_q:** blended from FFA forward curve and any disclosed time-charter coverage:
  ```
  TCE_class_q = spot_pct × FFA_class_q + charter_pct × disclosed_charter_rate
  ```

- **r (discount rate):** equity cost of capital, 10–12% for crude tankers (high-beta cyclical sector). Default 11%, sensitivity ±2%.

- **TerminalValue_{q=9}:** modeled as **1.0× NAV** at quarter 9, projected forward using vessel depreciation curve. This is the explicit handoff from the dividend strip back to NAV.

**Strip horizon = 8 quarters** because: FFA crude tanker liquidity drops sharply beyond 12–18 months; modeling beyond that pretends to a precision the market doesn't offer.

**Scenario TCE forwards do not parametrically reflect MEG export capacity recovery lag** (§14). The Q3-Q4 2026 forwards in `pre_mou_baseline` / `moderate_tightening` / `glut_base` scenarios assume MEG export volumes ramp in step with vessel transit capacity post-MoU; the empirical picture is that volumes lag transit by 1-2 quarters. Treat near-term Phase 2 strip cash flows as conservative on rate level; see §14.4 for the recommended qualitative overlay.

**Time-varying earning fleet (material orderbooks).** `vessels_class` in NetTCE_revenue is not necessarily static: for names with a material orderbook or announced sales, the *earning* fleet changes over the strip horizon (e.g. FRO takes 9 VLCC newbuild deliveries Q2'26–Q1'27 and sells 2 Suezmax). Supply a per-class, per-quarter fleet count (a `fleet_schedule`) so the strip captures forward earnings as deliveries land; a static count would understate them. NAV stays anchored at the report date (with newbuilds valued per §3.1), and the newbuild balance-sheet lines handle the cash side — so the asset and earning sides stay consistent without double-counting.

### 3.3 Implied breakeven TCE

The sanity check: how extreme must rates be to justify the current price? Solve for a single uniform **multiplier on the current forward curve** (holding cycle weights at base, NAV fixed) at which the tool's blended fair value equals the price. Scaling the forward — rather than flattening every class to one flat rate — **preserves the inter-class rate structure** (a VLCC earns more than a Suezmax in every state), which matters for blended fleets (INSW, TNK, EURN). The earlier flat-rate-across-all-classes form distorted blended breakevens upward and was not comparable between names with different fleet mixes. Report:

- a **value-weighted blended breakeven TCE** = Σ_class value_weight · (m · FFA_12M_class) — the headline, comparable across names and to each scenario's value-weighted "assumed TCE", and
- the **per-class** implied rate (m · FFA_12M_class), in each class's own units.

Compare to the value-weighted 10-year mean / current spot / 12-month FFA. If implied breakeven >> mean, the market is pricing in extended peak rates; if < mean, distress. For single-class names (DHT) the blended breakeven is just that class's rate and `m` is the multiple of its forward.

### 3.4 Sensitivity grid

For each name, compute fair value across:

- TCE rates: −30%, −15%, base, +15%, +30%
- Vessel values: −20%, −10%, base, +10%, +20%

Output as a 5×5 heatmap of fair value vs. current price. The shape of the heatmap reveals which lever the valuation is most sensitive to — useful for understanding what would need to change to justify a different position.

**Dividend payout scenarios.** Payout is a structural lever at cycle peaks, not a rounding choice: tanker boards distribute near 100% of earnings at peaks (cash accumulates faster than reinvestment, majority owners want it out, everyone expects the next trough to cut it anyway), and revert toward the stated 75–80% floor as the cycle softens. Model a **base payout ~0.95** (recent peak behaviour with some conservatism) and report fair value across **0.80 (stated-floor / discipline-reasserts)** and **1.00 (peak-persists)** as an explicit scenario. Modeling the stated 0.80 as base would systematically understate the strip in a peak environment. (A future enhancement: make payout cycle-linked to the TCE strip.)

## 4. Required Inputs (per company)

### 4.1 Fleet manifest (`inputs/fleet_manifests/{ticker}.yaml`)

```yaml
ticker: FRO
report_date: 2026-Q1
vessels:
  - id: VLCC_001
    class: VLCC
    dwt: 300000
    age: 7
    scrubber: true
    eco: true
    charter_status: spot  # spot | time_charter
    charter_rate: null    # USD/day if time_charter, else null
    charter_end: null     # date if time_charter
  # ... one entry per vessel
spot_coverage_pct:
  VLCC: 0.82
  Suezmax: 0.75
fleet_summary:
  VLCC_count: 41
  Suezmax_count: 23
  LR2_count: 18
  avg_age_VLCC: 6.8
```

### 4.2 Balance sheet snapshot (`inputs/balance_sheets/{ticker}_{quarter}.yaml`)

```yaml
ticker: FRO
quarter: 2026-Q1
cash_and_equivalents: 350_000_000
working_capital_net: 80_000_000
total_debt: 2_200_000_000
lease_liabilities: 50_000_000
newbuild_capex_commitments: 180_000_000
newbuild_advances_paid: 60_000_000
diluted_shares_outstanding: 222_600_000
# Optional. Liquidation-preference value of all preferred series, subtracted
# from NAV as a creditor-like claim ahead of common (defaults to 0 when
# omitted; pro-rates by sleeve in hybrid carve-outs the same way corporate/
# unsecured debt does). Added 2026-06-05 to pre-position TEN onboarding;
# none of the 12 current watchlist names use it.
preferred_equity: 0
```

### 4.3 Dividend policy (`inputs/dividend_policies/{ticker}.yaml`)

```yaml
ticker: FRO
policy_type: variable        # variable | base_plus_variable (see §3.2)
payout_ratio: 0.80           # 80% of net income
base_dividend_per_share: 0   # variable: minimum floor UNDER DPS; base_plus_variable: additive base
floor: 0                     # EPS threshold deducted before payout (e.g. ECO breakeven)
```

Known policies across current coverage:

| Ticker | Sector | `policy_type` | Policy detail |
|---|---|---|---|
| FRO | crude | variable | ~75–95% of net income, no fixed base; modeled at 0.95 base case + payout sensitivity |
| DHT | crude | variable | 100% of net income, $0.025/qtr nominal floor |
| ECO | crude | variable | 0.85 payout of EPS above breakeven floor |
| INSW | crude (hybrid) | base_plus_variable | $0.12/qtr base + supplemental variable on excess earnings |
| TNK | crude | base_plus_variable | $0.25/qtr fixed + 0.25 payout on excess (specials are lumpy; retains cash for renewal) |
| NAT | crude | variable | ~100% of net income, low fixed floor; the §12 framework-limitation archetype |
| FLNG | lng | base_plus_variable | $0.75/qtr fixed, **payout 0** (no variable; FLNG does not pay specials) |
| CCEC | lng | base_plus_variable | $0.15/qtr fixed, **payout 0** (no variable; retains cash for $2.25B NB program + $20M buyback) |

(Verify against latest filings each quarter; policies evolve.)

### 4.4 Cost structure (`inputs/cost_structures/{ticker}.yaml`)

```yaml
ticker: FRO
opex_per_day:
  VLCC: 8200
  Suezmax: 7100
  Aframax: 6500
  LR2: 6800
annual_G_and_A: 45_000_000
annual_interest_expense: 110_000_000
effective_tax_rate: 0.02    # tanker shipping is largely tax-advantaged
```

### 4.5 Market data (`inputs/market_data/`)

- `vessel_value_curves.yaml` — by class × age
- `spot_tce.yaml` — current spot TCE by class
- `ffa_forward_curve.yaml` — 8 quarters forward by class
- `historical_tce_means.yaml` — 10-year means by class for cycle position

## 5. Data Sources

| Input | Source | Cost | Refresh cadence |
|---|---|---|---|
| Fleet manifests | Company IR sites, 20-F / 10-K filings, fleet pages | Free | Quarterly |
| Balance sheet | SEC EDGAR (US listings), Oslo Børs filings (Norwegian listings) | Free | Quarterly |
| Vessel market values | Triangulate from: disclosed company sales transactions, newbuild order prices, broker indices in industry press (Hellenic Shipping News, TradeWinds, Splash247) | Free with effort | Quarterly |
| Spot TCE rates | Baltic Exchange daily indices: TD3C (VLCC MEG-China), TD20 (Suezmax W. Africa-UKC), TD25 (Aframax US Gulf-UKC). Free tier exists; company weekly reports (FRO Friday updates) as cross-check | Free (limited) | Weekly |
| FFA forward curve | Baltic settlement data (public lag), broker indications in industry press | Partial (delayed) | Weekly |
| Historical TCE means | Computed from Baltic historical indices, supplemented with academic / industry datasets | Free with effort | Annual update |
| Dividend policies | Company quarterly earnings releases, capital allocation policies | Free | Quarterly |
| Diluted share counts | Latest 10-Q / 6-K cover page | Free | Quarterly |

**The hard one is vessel values.** Clarksons / VesselsValue are the gold standard but paid. The free-source triangulation approach is workable but produces a band, not a point. The sensitivity grid (±20% on vessel values) is designed to absorb this uncertainty.

## 6. Company-Specific Notes

### FRO (Frontline)
- Listed both NYSE and Oslo (FRO / FRO.OL); use NYSE for primary price
- Post-Euronav VLCC absorption: 24 VLCCs added in 2024, fleet is now ~41 VLCC + 23 Suezmax + 18 LR2
- LR2 is technically a product tanker class; for crude-pure analysis either include LR2 in fleet (since FRO trades them across crude/clean) or carve out — flag the choice in the output
- High dividend payout (often 75–80%) means dividend strip drives near-term value heavily at peak rates

### ECO (Okeanis Eco Tankers)
- Modern fleet (avg age ~4 years), all eco-design, predominantly scrubber-fitted
- All-spot exposure means full upside to spot rates, full downside to weak rates
- Lower OPEX per day vs. peers due to eco design (~10–15% fuel savings)
- Smaller fleet (~14 vessels) means dividend volatility is high
- Premium valuation on P/NAV is justified by fleet quality, but the model should still apply baseline class market values and then add eco premium explicitly

### DHT (DHT Holdings)
- Pure VLCC, ~24 vessels
- Simplest model — single class, single rate driver (TD3C)
- 100% net income payout policy makes dividend strip exceptionally clean
- Use as methodology validator: if the model produces a weird answer for DHT, the methodology has a bug because there are fewer moving parts

### INSW (International Seaways) — whole-company (v2 → v2.1 product-sector refactor)
- Hybrid crude + product operator post-Diamond S merger
- v2 carve-out aggregates **both sleeves**: crude (VLCC + Suezmax + Aframax + LR1 30% crude leg) and product (MR + LR2 + LR1 70% product leg) via separate carve-outs, then sums to whole-company FV against the actual tape price (§6 in original sense, now superseded by v2 whole-company aggregation)
- Allocation: by vessel **market value** (not count, not EBITDA); vessel-secured debt assigned directly to its sleeve; corporate/unsecured debt pro-rated by sleeve value share
- Product sleeve uses CLEAN trading rates: **crude sleeve routes through `sectors.crude`** (four MoU scenarios, crude class map: VLCC/Suezmax/Aframax_dirty/LR2_clean/LR1→aframax_dirty); **product sleeve routes through `sectors.product`** (five product scenarios — refinery_squeeze / moderate_correction / glut_base / demand_softening / structural_decline — with product class map: MR/LR1_clean/LR2_clean). See §11.5 for the product sector that closed the v2 shortcut.
- Scenario aggregation: per-INDEX pairing (crude scenario N + product scenario N → whole-co scenario N), preserving the per-scenario diagnostic table. Implicit perfect-correlation assumption between the two sleeves, defensible because both respond to the same macro tape (refining margins, OPEC barrels, ton-mile demand)
- v2.1 (sector refactor, 2026-06-01) preserved the INSW whole-co FV to within ~$0.05/sh of pre-refactor (tiny shift from `LR1_clean` cycle anchor moving from `lr2_clean`'s $27k to its own $25k)
- The single-point FV report still shows the crude sleeve detail (NAV breakdown, dividend strip, breakeven); the scenario report is the whole-company headline with a per-sleeve breakdown appended
- **2026-06-09 footnote: the "v2.1 preserved INSW FV exactly" invariant was broken intentionally** by the Jun-9 product-sector Issue #1 fix (§11.5 v3). The q3_2026 LR1/LR2 forwards in product's `glut_base / demand_softening / structural_decline` had inherited a Phase-1 MoU spike from `sectors.crude.scenarios.{mou_base,mou_bear}.lr2_clean` via the v2 INSW shortcut — the "preserved exactly" guarantee was preserving a copy bug. Post-fix isolated effect on INSW Q3-2026 product-sleeve LR2 weighted: $114.5k → $86.0k. Combined with the parallel Jun-9 crude/product weight reset, INSW whole-co PW FV moves $52.08 → $64.59 (TRIM/SHORT narrows; the §6 mark-driven thesis is unchanged but the cyclical setup is materially less bearish).

#### VIE Watch — broker-consensus corroboration of the mark-driven gap (added 2026-06-03)

The VIE Coverage Universe (Catlin / Mintzmyer, accessed 2026-06-03) carries INSW at **Watch** with FV **$79.50** vs price $78.69 (essentially fair). Our tool: PW FV $52.08 at price $76.80 (EV −32.2%, TRIM/SHORT).

**The $27/sh tool-vs-VIE gap is structurally the mark-driven hybrid issue this entry already documents** (k_broker 1.37 / +22pp tool→broker spread per §9.9). VIE's $79.50 ≈ broker-implied NAV (price $78.69 / consensus_pnav 0.97 ≈ $81). **Three-way ordering: tool $52 << broker $81 ≈ VIE $79.50.** VIE matches broker consensus.

**Operational reading:** VIE's view is *external validation that the broker-NAV anchor for INSW is mainstream sell-side consensus, not an outlier mark.* The discrimination IS the call — if you trust broker NAVs, INSW is fair (VIE Watch); if you trust tool NAVs, INSW is deeply TRIM (us). **Nothing to fix** — the framework's mark-driven flag already surfaces this as an interpretive divergence. The VIE confirmation is documentary support for the existing classification, not a methodology gap. See `outputs/vie_coverage_universe_xref.md`.

### TNK (Teekay Tankers)
- Atlantic-skewed crude operator: ~14 Suezmax + 18 Aframax/LR2 + 1 VLCC at Q1 2026 (the VLCC being sold)
- Active fleet renewal: bought 3× 2016 Aframax (Q1 2026 sale-leaseback at $47.2M ea — the primary Aframax transaction anchor in `transactions.yaml`); 2 Suezmax NBs ordered Q1 2026 (S. Korean yard, 2027 delivery)
- Disclosed mid-age Aframax prints from TNK drove the Aframax curve recalibration (10yr anchor −12.8%)
- Mostly spot; modest TC coverage; high near-term cash generation
- Dividend: $0.25/qtr fixed + occasional supplemental specials (modeled as base_plus_variable with low payout)
- One of the **mark-driven** names (k_broker 1.18, spread +10pp)

### NAT (Nordic American Tankers)
- Pure Suezmax (18 vessels at Q1 2026); recently sold 2 oldest (2004/2005) for $50M total
- 2 Suezmax NBs ordered Jan 2026 (S. Korean yard, 2028 delivery)
- ~100% payout policy is the defining feature: dividend tracks earnings up and down with a small fixed floor
- **§12 framework limitation archetype** — at peak cycle the model returns FV ≈ NAV, treating dividends as value extraction rather than as the investment thesis. The market prices the near-term dividend stream as the dominant value driver, producing P/NAV > 1.5× during peak conditions that the model reads as "rich"
- **Recommended usage:** treat tool FV as NAV floor; apply qualitative dividend-stream overlay; do NOT act on the model's TRIM signal without explicit dividend-window framing. See §12.

### FLNG (Flex LNG)
- Pure-LNG operator: 13 modern 174k cbm two-stroke LNG carriers (4× 2018 + 2× 2019 + 4× 2020 + 3× 2021), all Korean (Hanwha Ocean / Samsung / HSHI)
- Mixed MEGI / X-DF / X-DF2.1-adjacent propulsion — but none are explicit X-DF2.1, so all carry `eco: false` and sit at the LNGC baseline curve (no propulsion premium applied)
- No newbuild orderbook — mature TC-heavy fleet (~91% of 2026 fleet days fixed at Q1)
- $0.75/qtr fixed dividend (no specials)
- First sector-port name (FLNG v1 → sector layer refactor → Set B v2 lock; the v1→v2 FV transition is pinned by `test_flng_v2_locked_weights_fv_band`)
- **Tool above broker** (k_broker 0.87, −20pp spread) — broker analyst NAVs apply orderbook-glut cycle haircuts; tool curve is more anchored

#### VIE Avoid — extends the three-way ordering (added 2026-06-03)

The VIE Coverage Universe (Catlin / Mintzmyer, accessed 2026-06-03) carries FLNG at **Avoid** with FV **$16.50** vs price $29.85 (−45% downside). Our framework is already "tool above broker" (k_broker 0.87, −21pp spread): tool $28.04 > broker-implied $21 (at consensus_pnav 1.42). **VIE extends the ordering: tool $28 > broker $21 > VIE $16.50.** All three reads agree on direction (TRIM/Avoid); VIE is the most bearish.

**Mechanistic interpretation:** VIE is weighting the LNG glut thesis more heavily than the sell-side consensus does — likely activating the equivalent of our `structural_reset` scenario (METHODOLOGY §11.3, currently weight 0.0 sector-wide). If we applied a non-zero structural_reset weight specifically for FLNG (its mature TC-heavy book is more exposed to structural demand reset than CCEC's NB-heavy book, which has cheaply-contracted modern X-DF2.1 hulls), our FLNG FV would compress toward VIE's view.

**This is the cleanest case on the watchlist for considering a name-specific structural_reset weight overlay.** Not actioning yet — flagged as a candidate methodology extension if Q2 FLNG fleet-employment data confirms continued TC-rate softening into 2027.

### CCEC (Capital Clean Energy Carriers)
- Pure-LNG operator post-2024 CPLP restructuring: 12 in-water LNGCs (174k cbm; 2019-2025 deliveries) + 9 LNG NBs (X-DF2.1) + 1 in-water MGC (22k cbm LCO2/multi-gas Active) + 8 gas NBs (2 LCO2 incl Amadeus + 6 dual-fuel MGCs)
- The 2024-2025 LNG/Cs and all 9 LNG NBs are X-DF2.1 — tagged `eco: true` per the LNGC propulsion premium (§3.1)
- Two-class operator (LNGC + MGC) — first watchlist name using the MGC gas-carrier sub-class (§3.1)
- All committed newbuilds (LNG + gas) valued newbuild-at-market per §3.1; total NB commit $2,251.5M outstanding
- $0.15/qtr fixed dividend (no specials; retains cash for the NB program + $20M repurchase authorization)
- 1 legacy Neo-Panamax container ship is the only non-fleet vessel still excluded from valuation (single non-core hull, no LNG-sector class)

#### CCEC scenario torque — weight-driven signal (added 2026-06-01, §13 limitation + §9.10 diagnostic)

CCEC has materially higher scenario torque than FLNG due to its newbuild orderbook ($2,251.5M committed). The newbuild option value compresses brutally in glut scenarios (NB carrying value of cheaply-contracted ships is heavily discounted when delivered into a soft market) and expands materially in tight scenarios (those same NBs become deep-in-the-money options on tight-market rate environments). Per-scenario FV under Set B-revised:

| Scenario | CCEC FV | FLNG FV | CCEC range / FLNG range |
|---|---:|---:|---|
| tight_resurgence | $48.52 | $39.76 | wider upside |
| moderate_tightening | $35.36 | $32.82 | comparable |
| glut_base | $19.76 | $24.49 | CCEC lower in base |
| glut_intensifies | $9.59 | $19.03 | CCEC much lower |
| structural_reset | $1.05 | $14.58 | CCEC near-zero in tail |
| **Range (max − min)** | **$47.47** | **$25.18** | **CCEC ~1.9× FLNG** |

Implication: the same weight shift moves CCEC's PW FV roughly 2× as much as FLNG's. CCEC's BUY signal under Set B-revised is therefore a **leveraged expression of the LNG-tight thesis**, not a NAV-anchored value play. Under Set B (the prior weight lock) CCEC was HOLD; under Set B-revised it's BUY; under a more bearish weight set it would slide back to HOLD or TRIM/SHORT. See `outputs/lng_weight_robustness.md` for the current per-set per-name diagnostic and `outputs/ccec_buy_diagnostic.md` for the BUY-actionability review (NB orderbook validation + three-weight-set classification + k_broker spread).

**Position-sizing recommendation:** treat CCEC's BUY as a high-torque LNG-tight expression that should be sized smaller than a mark-validated, weight-robust BUY would warrant. The framework distinction is:
- *Weight-robust BUY* (none currently on the watchlist) — would survive across all reasonable weight sets; full sizing per allocation policy
- *Weight-driven BUY* (CCEC currently) — survives Set B-revised but doesn't survive Set B or a bearish alt; size with explicit acknowledgement that the call's signal depends on which weight set you trust
- *Cross-check:* k_broker spread −9pp (mark-validated, narrow). So CCEC is mark-validated but weight-driven — the call's risk is on the scenario probability assignment, not on the vessel-mark calibration

#### VIE Avoid — external counter-signal (added 2026-06-03, §13 trigger)

The VIE Coverage Universe (Catlin / Mintzmyer, accessed 2026-06-03) carries CCEC at **Avoid** with FV $17.50 vs price $23.76 (−26% downside). This is the **strongest external counter-signal possible to a weight-driven BUY** — it triggers the §13 quarterly re-evaluation discipline directly. Per §13.3, an independent-analyst opposite-direction call is among the explicit "when to re-evaluate" criteria.

**Revised position-sizing recommendation (supersedes earlier "smaller than weight-robust BUY would warrant"):** treat CCEC's BUY as **neutral / small allocation pending Q2 confirmation or independent corroboration**. The framework's discipline isn't to disregard the tool's BUY signal but to recognize that a weight-driven BUY contradicted by an independent analyst has materially less conviction than a weight-driven BUY corroborated by one. See `outputs/vie_coverage_universe_xref.md` for the full cross-reference matrix and §9.10 combined mark × weight × VIE conviction table.

### ASC (Ardmore Shipping, NYSE:ASC) — first pure-product validator
- Pure-product operator (Irish-domiciled, NYSE:ASC): 19 active MRs + 2 on-curve Handysize (product, on-curve since 2026-06-05) + 4 off-curve 25k stainless-chemical hulls + 1 MR held for sale + 2 Handysize NB orders. **First watchlist name tagged `sector: product`** (METHODOLOGY §11.5); routes through `sectors.product` with the product class map (MR → `mr`, no crude-rate contamination)
- MR fleet age profile: 5× 2013 Eco-Mod (eco: false, age 13) + 5× 2014 Eco (age 12) + 4× 2015 Eco (age 11) + 4× 2017 Eco (age 9) + 1× 2020 Eco (age 6). Average age ~10.9 yrs; fleet sits near the MR 10yr anchor of $34.5M
- **Zero scrubbers fleet-wide** — Ardmore's decarbonisation strategy is Eco-design + biofuel trials + carbon-capture pilot, not scrubber retrofit. Different archetype from the DHT / TNK scrubber-heavy fleets
- Dividend policy: variable, **2/3 of Adjusted Earnings** (doubled from 1/3 effective Q1 2026); no fixed base, no floor. Q1 2026 DPS $0.39
- Plays the same methodology-validator role for the product sector that DHT plays for crude and FLNG plays for LNG: single class, simple capital structure, clean dividend strip — if the tool produces a weird answer for ASC the product machinery has a bug
- **Off-curve fleet adjustment (§11.5, NARROWED 2026-06-05):** the 2× 37k Korea-built product Handies (Defender/Dauntless, 2015) moved ON-CURVE via the new Handysize class (~$24.6M each at age 11). Remaining off-curve: the 4× 25k Japan-built STAINLESS CHEMICAL hulls (~$13M each → $49.4M after a 5% liquidity discount) — a 38k product Handysize curve would overvalue these smaller chemical hulls, so they stay in `working_capital_net` as a narrower chemical-Handy residual (the small end of the chemical-sector gap). ASC `working_capital_net` $172.6M→$131.0M; NAV +$0.18/sh. Same off-curve treatment pattern as DHT-Bauhinia (held-for-sale at agreed sale price)
- **Tool below broker** (k_broker 1.33, +29pp spread) — joins TNK/INSW/NAT as a mark-uncertain product-tanker name where broker NAV consensus (~$21.3/sh at P/NAV 0.75 on the refreshed $16.00 price) sits well above the tool's MR-curve-anchored NAV ($15.96). The spread is the dominant call driver — at tool marks ASC is TRIM/SHORT (price $16.00); at broker marks it flips to a BUY. *(Synced 2026-06-05: the prior "1.59 / +40pp / NAV $15.78 / price $18.50" predated the 4-Jun price refresh + Pareto P/NAV reclassification and the Handysize on-curve move.)*
- **Methodology gap to revisit:** the 5× 2013 Eco-Mod MRs are flagged `eco: false` per §3.1 (built pre-2014), but the MR curve is "eco-inclusive modern-spec" — so these 5 vessels are valued at the modern-spec curve and modestly over-valued vs. a true age-13 conventional-MR transaction print. Minor (~$15M aggregate over-valuation, <1% of NAV) but flagged for future MR-curve calibration work

#### VIE Bullish — external counter-signal on the TRIM call (added 2026-06-03)

The VIE Coverage Universe (Catlin / Mintzmyer, accessed 2026-06-03) carries ASC at **Bullish** with FV **$21.50** vs VIE-reported price $15.91 (+35% upside). Our tool: PW FV $14.24 at price $18.50, TRIM/SHORT (EV −23.0%) under Product Set B v2. **First watchlist name where VIE materially overrules our framework on direction.**

**Three factors partially explain the gap, none fully close it:**
- *Price snapshot drift:* VIE $15.91 < our $18.50. Refresh checklist should pull the latest Pareto print; even adjusting our price to $15.91 our FV $14.24 implies EV −10.6%, still TRIM/SHORT.
- *§11.5 Handysize sleeve (partly retired 2026-06-05):* ASC's 2 product Handies moved on-curve via the new Handysize class, realizing **+$0.18/sh** — the low end of the prior $0.25-0.50/sh estimate, since only the clean-product portion moved (the 4× 25k stainless-chem hulls stay off-curve as the chemical-Handy residual). Narrows but doesn't close the VIE gap: ASC PW FV is now $14.50 vs VIE $21.50.
- *Product Set B v2 (locked same day, 2026-06-03):* added +$0.65/sh constructive reweighting already. VIE's view implies product-sector tightness goes materially beyond what Set B captures.

**Combined mark-driven (+40pp k_broker spread) + VIE Bullish:** under §9.10's combined-conviction framework, this is the **weakest TRIM signal on the watchlist**. Recommended overlay: **soften the TRIM signal to "qualified TRIM"** — the framework's product-sector valuation may be too conservative on Handysize handling, and the mark-driven flag combined with an independent Bullish call means position decisions on ASC should not treat the TRIM as decisive. See `outputs/vie_coverage_universe_xref.md` for the combined-conviction matrix.

### STNG (Scorpio Tankers, NYSE:STNG) — first multi-class pure-product
- Largest US-listed product tanker by fleet count: **73 on-curve vessels (32 LR2 + 41 MR)** + 14 off-curve Handymax + 9 held-for-sale + 10-vessel newbuild book ($572.8M at Q1; $641.5M post-April). First **multi-class** name in `sectors.product` — exercises both LR2_clean and MR routing through the product class map simultaneously
- **Modern fleet, ~95% scrubber-fitted** — built 2013-2020 at Korean (Hyundai Mipo / SPP / DSME / Samsung) and Chinese (SWS) yards. Average age ~10 yrs. LR2s sit on the (Aframax-equivalent) LR2 curve with the standard $1M scrubber premium + 5% eco premium; MRs on the eco-inclusive MR curve
- **Heavily levered to product-sector cycle peak via spot/TC mix:** ~75% spot fleet-wide (88% MR / 61% LR2 — LR2 has more long-dated TC out at $29-35k/d). Q1 2026 produced $216M net income (+272% YoY) at LR2 spot ~$75k and MR ~$22k
- **Dividend policy: fixed $0.45/qtr (no specials in 2025-2026)** wrapped as `base_plus_variable` with `payout_ratio: 0` — identical wrapper to TNK / FLNG / CCEC. Primary capital return is the **buyback program ($500M auth refreshed May-26; ~$300M executed in Q1 + April)**, not the dividend
- **§12 framework limitation — BUYBACK CHANNEL variant:** STNG is the buyback-channel analogue of NAT's dividend-channel §12 case. The dividend strip captures only the $0.45/qtr fixed dividend; aggressive buybacks (retained earnings → share-count reduction → per-share NAV growth) flow through the terminal NAV but NOT through the cash-flow strip. Tool FV is structurally **conservative** on buyback-dominated names. At Q1 2026: tool blended FV $77.35 vs price $79 ≈ 2% discount; tool NAV $83.76 (above price). The market is plausibly valuing the buyback channel that the strip cannot price
- **Clean balance sheet (Q1 2026 milestone):** STNG repurchased all remaining sale-leaseback obligations in Q1, taking `lease_liabilities` from a multi-billion 2022 peak to **zero**. Material vs the historical SLB-heavy structure. Net cash $395M actual / $876M pro-forma after the April convert. Share count down from 78M (2022 peak) to 50.4M today — ~35% retirement via buybacks
- **Off-curve adjustments ($602.8M aggregate in `working_capital_net` after the 2026-06-05 Handymax migration; was $802.8M):** (1) operating WC $208M; (2) 9 vessels held-for-sale at agreed $395M sale price (Q2 close expected, $200M gain pending). The 14 IMO-II chemical Handymax (formerly the third $200M entry) moved on-curve 2026-06-05 via the new Handymax class — see [STNG fleet manifest](../inputs/fleet_manifests/stng.yaml); on-curve value $205M ≈ off-curve $200M within ~$5M, net +$0.10/sh NAV. The sleeve now responds to scenario rate forwards (MR-proxy validated by STNG Q1+Q2 2026 disclosed Handymax pool/spot ≈ MR)
- **First crude exposure planned:** 2 VLCC newbuilds at Hanwha Ocean (2H 2028 delivery) — currently valued newbuild-at-market via `newbuild_capex_commitments` + `newbuild_advances_paid` lines (deliver past the 8-quarter strip horizon, so no scenario impact). When they enter service the hybrid carve-out architecture (today INSW-only) will need to extend to STNG
- **Mark-validated** (k_broker 1.10, **+7pp spread** — narrowest of the mark-uncertain product names; tighter than ASC +40pp / NAT +53pp / INSW +22pp). Tool LR2 + MR curves are well-calibrated relative to broker consensus on this large, mark-rich fleet. Tool and broker agree on direction: TRIM/SHORT at $79 in both views

#### STNG LR2 cargo-switching option value (added 2026-06-03, §14.6.1 framework gap)

STNG's 32-vessel coated-LR2 fleet carries an **embedded option to switch between clean and dirty trades** based on relative earnings — directly analogous to CCEC's $725M / +$14.40/sh NB orderbook embedded option value (§6 CCEC entry, `outputs/ccec_buy_diagnostic.md`), but mechanically distinct: CCEC's option is *contract-vs-current-market* on uncommitted hulls; STNG's option is *clean-vs-dirty earnings spread* on operating hulls. **The current framework does not capture this optionality** — STNG's LR2s route earnings exclusively through `lr2_clean` rate forwards via the product class map (`carveout.py` `_PRODUCT_RATE_REMAP`).

**Empirical magnitude (Kpler / Catlin VIE June-2026 macro update):** between early March and mid-April 2026, clean LR2 earnings traded at an **average discount of $87,000/day to dirty equivalents** because of MEG-volume collapse (MEG was 44% of LR2 ton-miles in 2025) and West-of-Suez Aframax demand surge. Coated LR2 owners redeployed rapidly into crude + fuel-oil trades.

**Sizing the gap for STNG:**

- 32 LR2 vessels × ~95% scrubber coverage = ~30 effective switchable hulls
- Q1 2026 disclosed Q2-expected LR2 spot days: 1,708; TC days: 1,088 — i.e. ~28 vessels spot-equivalent, ~5-6 vessels TC-locked
- If even ~50% of the ~$87k/d clean-vs-dirty premium were captured across the ~6-week early-March-to-mid-April window on the 28 spot-equivalent LR2s: ~28 × 40 days × $43k ≈ **$48M of Q2 earnings power above what the framework's `lr2_clean` forwards model**
- Per 50.4M shares: ~**$0.95/sh of additional Q2 EPS** if optimally captured — equivalent to ~2 quarters of the regular $0.45/qtr dividend, or ~1.2% of the tool $77.35 single-point FV
- **This is upside the framework's TC-driven scenarios do not see.** The mechanism is real for any LR2-heavy product operator — STNG is the most concentrated case on the watchlist (TORM and HAFNI, if onboarded, would carry the same flag)

**Why the framework can't easily parametrise this:**

- The switch is an operating decision per vessel-quarter, not a structural class assignment. Modelling it parametrically would require either (a) a per-vessel optionality module that re-estimates each quarter, or (b) a market-wide "clean-LR2-vs-dirty spread" forward curve that the framework would consume alongside the `lr2_clean` curve.
- Neither is in scope for v1. Both are natural v2 extensions if the cargo-switching dynamic persists past the SoH-reopen normalisation.

**Position-sizing implication:** STNG's TRIM/SHORT signal under Set A locked product weights is at EV −13.0% — but the framework's Q2-Q3 2026 EPS estimates likely understate actual earnings power by ~$0.50-1.00/sh if the LR2 fleet captures even a fraction of the cargo-switching upside. **The signal is mark-validated (+7pp spread) and weight-robust within the current product weight set, but the operating-mode optionality (§14.6.1) is a separate unmodeled positive bias that should attenuate the strength of the TRIM signal.** Treat STNG's TRIM as "mildly TRIM, with framework-known upside bias" rather than "decisively TRIM."

**What would close this gap:**

- Two-three quarters of post-Iran-crisis disclosed STNG LR2 trade mix (clean vs dirty days actually operated) — would either confirm material capture (and demand a §14.6.1 parametric extension) or show the optionality wasn't exercised (and §14.6.1 collapses to a noted-but-immaterial flag for STNG).
- Kpler / Clarksons / VV publication of a clean-vs-dirty LR2 earnings spread time series with a forward strip would enable curve-level modelling.

### HAFN (Hafnia Limited, NYSE:HAFN / OSL:HAFNI) — first IFRS-reporting product + largest by fleet
- Largest product-tanker watchlist name by vessel count: **109 OWNED vessels (10 LR2 + 25 LR1 + 49 MR + 22 Handy off-curve)** plus 12 chartered-in (operating leases via IFRS 16) and 8 firm + 2 option MR newbuilds at Hyundai Heavy Industries (delivery Q3 2028 - Q2 2029). Second full-3-class product name (after TRMD) — exercises every branch of `PRODUCT_SCENARIO_CLASS_MAP` end-to-end
- **First IFRS-reporting name on the watchlist** (TRMD is dual-listed but US-equivalent; HAFN is Bermuda-incorporated + Singapore-headquartered with IFRS presentation). Schema convention held — IFRS 16 vessel lease liabilities small ($35.9M), kept separate from bank_debt; IAS 16 vessel accounting no delta vs US GAAP; IFRS 5 held-for-sale measurement matches ASC 360
- **First pool-operator name on the watchlist.** Hafnia runs the world's largest product-tanker pool. All "spot" earnings disclosed are pool-derived (net of pool admin fees, bunker volatility, voyage operations costs). This is functionally similar to direct-spot for our framework's rate-input convention but worth noting that Q1 LR1 TCE ($38,194) actually **outperformed LR2 TCE** ($35,316) — a §14.6.1-related dynamic: when LR2s defected to dirty trade (Catlin VIE June 2026 macro update), the residual clean LR2 supply tightened LR1 rates as the substitute clean class
- **Strategic Handysize wind-down.** Hafnia is exiting the Handy segment over time; 4 of 22 Handys are pending Q2 2026 sale. As of 2026-06-05 the 22 Handies are ON-CURVE via the new Handysize class (modelled age-18 cohort, ~$14.5M/vessel ≈ $320M; `working_capital_net` $775M→$475M). Moving them on-curve dropped the prior 10% wind-down liquidity haircut (the framework has no on-curve liquidity-discount mechanism) — a small ~+$0.04/sh uplift, flagged. The on-curve count will shrink quarterly as the wind-down disposals close
- **TORM equity stake $395M** (Hafnia owns a meaningful TRMD position generating $9.9M Q1 dividend income). **Schema gap (flagged):** our YAML schema has no dedicated `marketable_equity_investments` line; rolled into `working_capital_net` at full disclosed value per Hafnia's mgmt NAV. Bounded impact: $395M / 500M shares ≈ $0.79/sh. Adding a dedicated schema line is a candidate future methodology refinement; deferred
- Dividend policy: variable, **80% of net profit target** (minimum 50%); Q1 2026 DPS $0.2877 USD. 17th consecutive quarterly dividend. Higher payout ratio than TRMD's smoothed ~75% (Hafnia explicit policy vs TRMD Board-discretion). §12-archetype similar to NAT but with material retained-earnings buffer at 80% vs NAT's ~100%
- **BW Group ownership 44.18%** (controlling-but-not-majority); free float ~55%. BW Group has been a net buyer 2025-26, which tightens float and supports premium-to-pure-float-peer P/NAV reads
- **Mark-driven (k_broker 1.45, +29pp tool→broker spread).** Tool NAV materially below broker-implied NAV (consensus P/NAV ≈ 1.00 at price $8.05). Joins ASC (+40pp), INSW (+22pp), STNG (+7pp residual) in the mark-driven product/hybrid bucket — broker-NAV consensus reads HAFN as ~fair while tool reads it as deeply discounted. Two structural drivers of the tool-vs-broker gap on HAFN specifically: (a) the framework's MR / LR1 / LR2 curves are conservative against Hafnia's mgmt-disclosed asset values; (b) the TORM equity stake rolled into `working_capital_net` at full $395M is correct in level but our tool NAV still ends up below broker because of the curve-side conservatism. Current consensus_pnav is APPROX (mgmt-NAV-implied); refresh with Cleaves / Pareto / Clarksons charter-free NAV print
- **VIE Bullish ($9.00) vs our TRIM ($5.27).** Third product name where VIE's structurally-more-bullish view overrules our framework on direction, after ASC and TRMD. Pattern consistent across product sector. **Three-way ordering: tool $5.27 < broker ~$7.66 (implied at P/NAV 1.00 × price discount) < VIE $9.00.** All three diverge but in a coherent pattern — tool most conservative, broker median, VIE most bullish. Suggests VIE is using more constructive forward-curve assumptions on product than our scenario forwards + Set B v2 weights capture. Position-sizing implication: HAFN TRIM is **mark-driven AND opposed by VIE Bullish** — the same combined-conviction signature as ASC. Treat as **weakest TRIM** on the product watchlist alongside ASC; more decisive TRIM than CCEC's HOLD-boundary BUY

### TRMD (Torm Plc, NASDAQ:TRMD / XCSE:TRMD A) — first full-3-class product
- Pure-product operator (UK-incorporated; dual-listed Nasdaq Copenhagen + New York): **95 in-water vessels (22 LR2 + 10 LR1 + 63 MR)** at 2026-03-31 + 8-vessel newbuild resale program (2 × MR Q2 2026 delivery + 6 × MR 2027-2028 delivery). **First watchlist name with all three product classes** — exercises every branch of `PRODUCT_SCENARIO_CLASS_MAP` end-to-end (MR → `mr`, LR1 → `lr1_clean`, LR2 → `lr2_clean`). The `lr1_clean` rate forwards previously only saw use via INSW's 30/70 product carve-out split; TRMD is the first pure-product name to drive them directly
- Modern-ish fleet (avg 11.5 yrs); LR2 ~10.5 yrs, LR1 ~13 yrs, MR ~11.5 yrs. The vintage 2012-2013 LR1 cohort (10 of 95 vessels) is the oldest segment — eco: false per §3.1, valued at the LR1 baseline curve (eco-inclusive) with the same minor over-valuation flag as ASC's Eco-Mod MRs and STNG's 2013 MRs. Scrubber coverage estimated ~57% LR2 / ~70% MR / ~30% LR1
- **Dividend policy: variable, quarterly Board-discretion (modelled at 75% of EPS).** VIE Coverage Universe tags TRMD as "100% FCF" but per Torm IR the policy is NOT a fixed % of NI or FCF — it's a Board assessment per quarter targeting **net LTV ~25%** (where TRMD currently sits at 25.1%). Recent payout ratios have varied **58% (Q1 2026) to 82% (Q4 2025)** of net income; trailing 4Q DPS $2.42. Modelled at smoothed midpoint 0.75 — refresh upward toward 0.78 if Q2 2026 reverts as management indicated
- **UK tonnage tax regime** (pre-2024 was Danish tonnage tax). Q1 2026 effective rate ~1.3% — modelled 1.5%
- **Mark-validated, narrowest spread on watchlist** (k_broker 1.01, +2pp tool→broker spread). Tool LR2 + LR1 + MR curves are well-calibrated against broker consensus on this large, mark-rich fleet. Tool and broker agree on direction: TRIM/SHORT at tool marks (EV −6.1%, just below the −5% HOLD threshold); HOLD at broker marks (EV −4.5%)
- **Methodologically similar to NAT on the §12 dimension but materially less exposed:** Torm's 75% payout ratio leaves a meaningful retained-earnings buffer vs NAT's ~100%. The framework's §12 limitation applies less severely — TRMD's tool FV is closer to a "true call" than NAT's, but the high-payout-on-cyclical-peak dynamic still partially applies. **Recommended usage:** treat the TRIM signal as more decisive than for NAT, less decisive than for DHT/ECO/FRO (where retained earnings rebuild NAV at lower payout ratios)

#### VIE Bullish — opposite-direction external counter-signal (added 2026-06-03)

The VIE Coverage Universe (Catlin / Mintzmyer, accessed 2026-06-03) carries TRMD at **Bullish** with FV **$34.00** vs VIE-reported price $28.29 (+20% upside). Our tool: PW FV $25.59 at price $27.25, TRIM/SHORT (EV −6.1%) under Product Set B v2. **Third product name (after ASC and CCEC) where VIE Bullish overrules our framework on direction** — but unlike ASC and CCEC, **our tool agrees with broker consensus** on TRMD (k_broker 1.01, +2pp spread): tool $25.59 ≈ broker-implied $26 ≈ price $27.25. **VIE is the outlier on the bullish side**, sitting +$8 above both us and the broker.

**Methodological interpretation:** the consistent VIE-Bullish-on-product-names pattern (ASC, STNG marginal, TRMD, plus the un-onboarded HAFN and TEN candidates) suggests VIE is structurally more constructive on product-tanker rates through 2026-2027 than either sell-side broker consensus or our scenario-weighted framework. The Product Set B v2 reweighting (locked same day, 2026-06-03) added constructive weight (+10pp on tight + moderate); VIE's view implies still more upside. Without VIE's underlying per-name forward curves or charter assumptions we can't decompose the gap further. See `outputs/vie_coverage_universe_xref.md` for the combined-conviction matrix.

**Position-sizing recommendation:** treat TRMD's TRIM as a **"qualified TRIM with mark-validated coherence but external Bullish overlay"** — meaningfully different from ASC's mark-driven TRIM (where the framework lacks broker consensus to anchor against) and from a hypothetical TRIM where both broker and VIE agree. **Lower-confidence than DHT/ECO/FRO; higher-confidence than ASC.**

### TEN (Tsakos Energy Navigation, NYSE:TEN) — first 3-sleeve hybrid

- Bermuda-incorporated FPI; **first name in `THREE_SLEEVE_TICKERS`** — crude (39 vessels) + product (17) + lng (2) sleeves split via `crude_carve_out` + `product_carve_out` + `lng_carve_out` against a single whole-company denominator. Onboarded 2026-06-06 (architecturally unblocked 2026-06-05 PM by §11.6).
- **Shuttle sleeve OFF-CURVE** (4 in-water DP2 vessels — Brasil 2014, Rio 2016, Athens 04, Paris 24): per METHODOLOGY §11.6 off-curve-at-contracted-book convention. `shuttle_contracted_book = $453.1M` (NPV of disclosed TC rates + Suezmax-curve residual at expiry, discounted at WACC 11%, utilization 98.3%, daily opex $11,000/day). Brasil 2014 / Rio 2016 include the 5-year extension agreed Q2-2026 (data kit + 6-K April subsequent event) at an APPROX $60k/day rate — refresh when the actual rate is disclosed.
- **Newbuild orderbook (19 vessels, $2,403M contract value):** treated as delivered-value = contract-price across the board (no hot-market markup). Convention: `newbuild_advances_paid = $400M` (the only NAV contribution from the NB program); `newbuild_capex_commitments = 0` (the future cash buys delivered vessels of equal value; net zero NAV impact). Equivalent to FRO-style "list NBs in fleet at delivered" when delivered = contract, but cleaner since we have no Shuttle vessel class to put 10 of the 19 NBs on. **Refresh per quarter** as advances grow and NBs deliver.
- **Preferred equity $287.3M:** 4,745,947 Series E (9.25%, $25 par) + 6,747,147 Series F (9.50%, $25 par). Subtracted from NAV (METHODOLOGY §4.2). Tsakos-affiliated entities hold 0.95% Series E + 1.5% Series F per 20-F.
- **Cycle position:** crude sleeve at 1.98× (late-cycle/peak; w_nav = 0.70, w_earn = 0.30) — drives the headline. Product and LNG sleeves carry their own cycle positions through the per-sleeve scenarios.
- **Governance / value-trap haircut (§15, applied 2026-06-06):** TEN is the framework's **first §15 case** — `governance_discount_pct: 0.30` on the balance sheet. Drivers: controlled-shareholder structure (Tsakos family), related-party transactions (Tsakos Columbia management fees), low common payout (~19% of EPS in 2026), no buyback program, preferred-share structure with affiliated holders. The 30% haircut applies at the blend layer (NAV term) and on the strip's terminal value; broker-NAV sweep / k_broker continue operating on undiscounted asset NAV.
- **Build output (2026-06-06, Q1 2026 inputs, post-§15 haircut):**
  - Asset NAV/sh (undiscounted): **$88.56** (close to VIE stale ~$98)
  - Single-point FV: **$58.42** vs price $44.00 (EV +32.8%); pre-haircut would have been $82.29
  - Scenario PW FV: **$49.37** (EV +12.2%); pre-haircut would have been $68.16
  - **Position: BUY (undervalued)** — milder than pre-haircut; lands near **VIE Bullish $51.50** (independent external confirmation that the right anchor is ~$50 post-discount, not ~$68 pre-discount)
- **Sources:** Q1 2026 6-K (filed 2026-05-22), 2025 20-F (filed 2026-04-06), TEN Data Kit (May 11, 2026). Per-vessel TC rates and NB schedule refresh from the **monthly data kit**; balance sheet detail from 6-K + 20-F. See `decisions/ten_log.md` for the full architectural-unblock history.
- **APPROX flags / refresh items:** (1) Shuttle extension rate $60k/day APPROX from 6-K "increased rate" disclosure; (2) NB advances paid $400M estimated between 20-F Dec $301.9M and data kit May $430M; (3) Working capital $28M rolled forward from 20-F; (4) Common diluted shares 30,127,603 from 20-F at Dec 2025 (no Q1 2026 buyback disclosure). Refresh all when next quarter's 6-K lands.
- **Status vs prior log:** the entire `decisions/ten_log.md` revisit-criteria checklist is **closed**. TEN is no longer a deferred candidate — it is the watchlist's 13th name and the first 3-sleeve hybrid.

### SBLK (Star Bulk Carriers, NASDAQ:SBLK) — first dry-bulk validator; mark-driven (added 2026-06-10, promoted from decisions/sblk_log.md)
- Post-Eagle-Bulk fleet: 135 operating (Cape 31 / Pana 46 / Supra-Ultra 58 per §11.7.1 class collapse) + 8 Kamsarmax NBs (Apr-Sep 2026 delivery, §3.1/§9.6 treatment). Variable dividend ~95-100% of EPS, no floor; **buybacks used opportunistically in soft tape (Q3-25) — invisible to the dividend strip, same caveat as STNG.**
- **Mark-driven (k_broker 1.27)** — the dry-bulk analog of INSW. The −21% tool↔broker gap SURVIVED the §9.9 transaction-anchored recalibration almost unchanged (−21.7% → −21.1%): Cape was understated (+16%/+13% at 5/10yr post-GNK-prints), Supra-Ultra overstated (−10%/−13%), Pana roughly flat — the cross-class corrections net to ~zero on SBLK's mixed book. The gap is a methodological call (our realized-S&P marks vs Pareto's TC-momentum mark-ups), not a curve artefact.
- **GNK isolates the gap as name-specific:** identical class curves reconcile GNK at −5.2% (k 1.04). SBLK's residual is most plausibly its 46-vessel Pana book (the thinnest fit: 4 prints, one possible duplicate) and/or Pareto's richer read on SBLK's specific mix. Investigate the Pana leg at the Q3 tightening pass.
- Pareto NAV trajectory (free-text sweep): $23 → $25 (Sep-25) → $33 (Jun-26) — our implied broker NAV $33.17 matches their stated $33 exactly. Market paid 0.66-0.84× NAV throughout; the market sides with the tool's level, not the broker's.
- Tool TRIM/SHORT (EV −5.7% at txn marks) vs broker BUY. v1 dry-bulk calibration-lock outcome recorded as 1/2 (50%) FAIL-with-explanation — SBLK is the documented miss; no curve tuning per the back-solve rule (see the 2026-06-09 incident in decisions/sblk_log.md).

### GNK (Genco Shipping & Trading, NYSE:GNK) — second dry-bulk validator; VALIDATES the marks layer (added 2026-06-10)
- 44 vessels at Mar-31 2026 (2 Newcastlemax + 17 Capesize → 19 Cape; 15 Ultramax + 10 Supramax → 25 Supra-Ultra; **no Pana**). US domestic issuer (10-Q, CIK 1326200); per-vessel employment table in the 10-Q MD&A. Formulaic dividend: operating cash flow less voluntary reserve (modeled variable / payout 1.00 / no floor).
- **The validation datapoint: k_broker 1.04, gap −5.2%** — within the v1 ±10% bar on the same transaction-anchored curves where SBLK reads −21%. The dry-bulk marks layer recovers Pareto's NAV ($27.59 implied = their stated $27.6) almost exactly for a no-Pana, Cape-heavy fleet.
- **DEAL OVERLAY (live until ~Jun-26 2026):** Diana Shipping hostile all-cash tender $24.80 (raised from $23.50; board rejected; proxy fight at the Jun-18 AGM; SBLK conditionally buys 16 GNK vessels for $470.5M if Diana wins). Price is tender-pinned — EV/position signals are deal-arb readings, not NAV-discount signals. Pre-bid regime was 0.66-0.75× NAV; a tender lapse likely mean-reverts toward that. **No §15 haircut** — event risk is not realisation impairment.
- GNK's own disclosures are now fit inputs: 2× 2020 nmax @ $72.75M, Courageous 2020 Cape @ $63.55M, Apr-26 Imabari Cape @ $65M (issuer-confirmed), Picardy/Predator 2005 Supras @ $10.6M (old-age leg validation ~60% above scrap).
- Onboarded 2026-06-09/10; baseline gap −5.2% is the drift anchor. Q2 items: tender resolution, the $65M June-delivery Cape, and (if Diana wins) the 16-vessel SBLK purchase as a print batch.

## 7. Output Format

Each pipeline run regenerates **seven output families**: a per-company single-point FV report, a per-company scenario report, a watchlist FV roll-up, a sector-segmented scenario roll-up, a broker-NAV sensitivity sweep, a transaction-anchor comparison, and a delta / decision-log pair. All under `outputs/` (durable decision history lives in `decisions/`, machine-local snapshot state in `state/`).

### 7.1 Per-company FV report (`outputs/{ticker}_fv_report.md` + `.xlsx`)

Single-point fair value with full detail. Sections:
- Header: ticker, report date, current price, model FV, analyst target (and **valuation-basis banner** for hybrid names — INSW shows `CRUDE SLEEVE` here; the whole-company aggregation is in the scenario report)
- Data validation warnings (spot TCE spikes, constructed forward curves, etc.)
- NAV breakdown table (by vessel class + balance sheet items; reports both with and without yard discount)
- Dividend strip table (8 quarters of projected DPS, EPS, discounted DPS, terminal value, total NPV)
- Cycle weighting calculation (12M TC ÷ 10yr mean → w_nav / w_earn)
- Blended fair value
- Payout sensitivity (FV at 80% / 95% / 100% payouts for variable-policy names)
- Implied breakeven TCE (value-weighted blended + per-class detail; flagged when NAV alone covers price)
- 5×5 sensitivity heatmap (TCE shock × vessel-value shock)
- Divergence diagnosis (FV vs current vs target)
- Modeling notes

### 7.2 Per-company scenario report (`outputs/{ticker}_scenarios.md`)

The headline whole-company decision view (not the single-point detail). Sections:
- Header with sector-aware framework label ("three-phase MoU framework" for crude; "LNG glut-cycle framework" for LNG)
- Valuation-basis banner for hybrid names (INSW shows `WHOLE-CO`)
- Probability-weighted FV, EV%, position recommendation
- Scenario-invariant breakeven TCE (value-weighted blended; flagged for degraded interpretation on TC-heavy fleets)
- Per-scenario table: weight, vessel-value scale, NAV/sh (flexed), FV (base + low/high band), cycle position, w_nav, strip NPV, assumed 12M TCE, assumed/breakeven ratio
- Decision signals: upside (best scenario), downside (worst), expected value vs current
- **Hybrid sleeve breakdown** appended for INSW: per-sleeve allocated price, FV, EV%, position, plus the whole-company aggregate (METHODOLOGY §6 v2)

### 7.3 Watchlist FV roll-up (`outputs/fair_value_summary.xlsx`)

| Ticker | Basis | Current | Tool FV | Watchlist Target | Tool vs Current | Tool vs Target | Implied Breakeven TCE (blended) | Cycle Position |

`Basis` column reads `whole-company` for pure-plays and `CRUDE SLEEVE (allocated price)` for the v1 INSW single-point detail (the whole-company aggregation lives in the scenario summary).

### 7.4 Scenario summary (`outputs/scenario_summary.xlsx`)

Multi-sheet workbook with one sheet per sector + a cross-sector pair-trade sheet:
- **Sheet `Scenario summary`** (crude sector): per-name row with the four crude scenario FVs (escalation / pre_mou_baseline / mou_base / mou_bear) + probability-weighted FV + EV% + position
- **Sheet `Scenario summary (LNG)`**: per-name row with the four active LNG scenario FVs (tight_resurgence / moderate_tightening / glut_base / glut_intensifies) — the structural_reset 5th scenario is computed but inactive (Set B v2 weight 0.0)
- **Sheet `Pair trades`**: cross-name pair-implied returns (Long_EV − Short_EV), with `Comparable?` column flagging `MIXED SECTOR (lng vs crude)` pairs and `MIXED BASIS (crude sleeve vs whole-co)` pairs

`Basis` column propagates the WHOLE-COMPANY-vs-CRUDE-SLEEVE distinction; INSW row reads `WHOLE-COMPANY (hybrid aggregation)` here.

### 7.5 Broker-NAV sensitivity sweep (`outputs/broker_nav_sweep.md` + `.xlsx`)

The mark-robust vs mark-driven discrimination diagnostic (§9.9). Per-name row:

| Name | Cons. P/NAV | k_broker | EV @tool | EV @mid | EV @broker | Pos tool→broker | Breakeven tool→broker | Spread (pp) | Read |

`k_broker` is the uniform vessel-mark premium that lifts tool NAV to the consensus broker NAV (price ÷ consensus P/NAV); the EV%-spread is the headline mark-driven-ness signal. Hybrid names labeled `**(WHOLE-CO)**`; mark-robust names show ~0pp spread, mark-driven names show wide spreads (in either direction).

### 7.5b Consensus forward-EPS cross-check (`outputs/consensus_eps_xref.md` + `.xlsx`)

The **earnings-leg analog of the §7.5 broker-NAV sweep** (full methodology in §9.11). Where the sweep cross-checks the NAV leg against broker consensus, this cross-checks the forward-earnings leg that drives the dividend strip against sell-side consensus. Per-name row:

| Name | Sector | Price | Cons. fwd P/E | Cons. fwd EPS | Tool fwd EPS | Tool impl. P/E | EPS gap | Cons. earn. yld | Cycle (band) | w_earn | Read |

`consensus_fwd_eps = price ÷ consensus_fwd_pe` (Pareto 1Y FWD P/E); `tool_fwd_eps` = sum of the first four strip quarters (NTM operating EPS). The `eps_gap` paired with `w_earn` is the headline: a wide gap with a *low* `w_earn` is the cycle weighting compensating for hot near-peak FFA earnings (by design); a wide gap with a *high* `w_earn` is the actionable case (a below-mid-cycle name whose trusted strip earnings the street doesn't share).

### 7.6 Transaction-anchored recalibration comparison (`outputs/transaction_anchor_comparison.md` + `.xlsx`)

Diagnostic showing per-name NAV/EV impact of applying the transaction-anchored mid-age curves (currently Aframax + Suezmax; opt-in toggle, default off in production). Per-name row:

| Name | NAV base→txn | Δ% | EV base→txn | Δpp | Position (with `⚠️` if call flipped) |

Used for the §9.9 recalibration validation: names with no exposure to a recalibrated class show Δ ≈ 0 (clean controls); names with exposure show the curve-driven shift. Documents which calls are robust to transaction-anchored curves vs which would shift.

### 7.7 Delta report (`outputs/delta_report.md`)

The "what changed since last run" headline. Added 2026-06-01 as the first piece of the workflow-polish push (alongside §7.8 decision logs) — addresses the recurring "I ran the pipeline, what should I look at first?" question by surfacing material moves automatically.

Three sections, in order:

1. **Headline material moves** — per-ticker bullets flagging position flips, single-point or scenario PW FV moves > **10%**, broker-spread shifts > **5pp**, NAV/share moves > **5%**, plus any new/dropped tickers. If nothing crossed the thresholds and no positions flipped, the section reads "No material changes" — a clean signal that the world hasn't moved on you.
2. **Input files changed since last run** — list of YAML files under `inputs/` whose SHA-256 hash changed (modified), or which were added/removed. Drives "did I update everything I meant to?" verification — if the watchlist hash changed but no market-data hash did, you know which class of refresh happened.
3. **Full per-ticker delta table** — every name with current value + signed delta per column (price, single-point FV, scenario PW FV, NAV/sh, position, broker spread). Material rows flagged ⚑; position flips marked ⟵.

**Material-change thresholds locked** (`MATERIAL_FV_PCT=10`, `MATERIAL_SPREAD_PP=5`, `MATERIAL_NAV_PCT=5`, position flip always material) — see `src/crude_tanker_fv/delta.py`. Tunable but treated as standard sensitivity.

**First-run case:** when `state/last_run.json` is absent, the delta report renders "First run — N tickers captured; no deltas computed yet" and lists every input file as `(new)`. Subsequent runs compute against the saved snapshot.

### 7.8 Per-ticker decision logs (`decisions/{ticker}_log.md`)

The user-curated counterpart to §7.7. One markdown file per ticker. **Every pipeline run prepends a structured "model state" entry** to the top of each log; existing content below is preserved verbatim. The prepended entry captures price, single-point FV, scenario PW FV, NAV/share, position, broker spread, sector, and (after the first run) deltas vs the previous run with material flags. Each entry ends with `**Decision:** _[pending annotation]_` — the user's prompt to record what they actually did and why.

**Why every run, not just material runs:** the steady-state context surrounding a real decision is part of the decision context. Skipping no-material runs would create gaps that look like "this is when I made the call" but actually mean "nothing happened that day." Every-run prepending captures the full timeline; the `⚑` flag inside the entry distinguishes material moments from steady state. (See locked design choices at top of `delta.py` for the rate-limiting and dedup-on-no-op alternatives that were considered and rejected for v1.)

**Why git-track them:** decision logs ARE the durable record. They're how, six months from now, you remember why you didn't act on a TRIM signal in April. And they're the feedback loop for refining the framework over time — "was the model's signal actually predictive on the names where I acted on it?" requires the historical ground truth that lives in these files.

**File creation:** on first encounter with a ticker, the tool writes a brief header (purpose + format guidance) above the first entry, then the entry itself. Subsequent runs locate the header section (everything up to and including the first `---` separator) and insert the new entry between the header and the prior entries.

### 7.9 Run-state snapshot (`state/last_run.json`, gitignored)

Machine-local JSON snapshot of the most recent run — per-ticker `TickerSnapshot` (current_price, single_point_fv, scenario_pw_fv, nav_per_share, ev_pct, position, breakeven_tce, broker_spread_pp, k_broker, sector) plus SHA-256 of every input YAML. This is the comparison anchor for the next run's delta computation. **Gitignored** so each machine builds its own delta history — the durable record lives in `decisions/*.md`. Delete `state/last_run.json` to reset the delta baseline (the next run will be a "first run").

## 8. Onboarding & Refresh Workflow

The framework is past initial build. Two recurring workflows now matter: onboarding a new ticker (templated mode) and quarterly market-data refresh.

### 8.1 Onboarding a new name (templated mode)

If the ticker's sector already exists (crude / lng), no methodology or code work is required — only data files. Estimated effort: ~2 hours per name dominated by data assembly, not engineering.

1. **Source** the latest quarterly results (6-K / earnings release / press release) for:
   - Fleet roster (vessel-by-vessel build year, shipyard, propulsion if disclosed)
   - Balance sheet at quarter-end (cash, restricted cash, total debt incl. current portion, operating leases, newbuild commitments outstanding, shares outstanding)
   - Q1 income statement (vessel opex, G&A, interest, depreciation, voyage expenses)
   - Charter coverage (TC vs spot mix, weighted-avg TC duration, disclosed TC rates if any)
   - Dividend policy (fixed base, variable payout, recent declaration)
2. **Write four input YAMLs** under `inputs/`:
   - `fleet_manifests/{ticker}.yaml` (per §4.1 schema — vessels list with class, dwt/cbm, age, scrubber, eco, charter_status, charter_rate, count; plus spot_coverage_pct, fleet_summary)
   - `balance_sheets/{ticker}_{quarter}.yaml` (per §4.2)
   - `cost_structures/{ticker}.yaml` (per §4.4 — `opex_per_day` per class)
   - `dividend_policies/{ticker}.yaml` (per §4.3 — `policy_type` + parameters)
3. **Add one watchlist entry** in `inputs/watchlist.yaml`:
   ```yaml
   TICKER:
     current_price: X.XX
     analyst_target: Y.YY
     consensus_pnav: Z.ZZ
     sector: crude          # or lng — drives sector-scenario routing
     as_of: YYYY-MM-DD
   ```
4. **Run the pipeline** (`python -m crude_tanker_fv.pipeline {quarter}`). Outputs regenerate automatically (per-name FV + scenario report; sector-segmented scenario summary row; broker-NAV sweep row; transaction-anchor comparison row).
5. **Verify**: tests stay green (`pytest -q`); pipeline run produces no class-not-found errors; per-name report's NAV breakdown adds up; scenario report rendered with the correct sector framework label.

If the ticker's sector does NOT yet exist, the additional one-time steps are in §11.4 (Adding new sectors).

### 8.2 Onboarding a new vessel class (e.g. MGC sub-class)

Required when an existing-sector name has fleet outside the current class coverage. Sample: CCEC's MGC gas fleet (2026-06-01).

1. Add the class to `ALLOWED_CLASSES` in `loaders.py` (one line).
2. Add the class to `SCENARIO_CLASS_MAP` in `scenarios.py` (one line — maps model class to scenario-curve key).
3. Add the class's value curve to `inputs/market_data/vessel_value_curves.yaml`.
4. Add the class's rate entries to `spot_tce.yaml`, `twelve_month_tc.yaml`, `historical_tce_means.yaml`, `ffa_forward_curve.yaml`.
5. Add per-scenario forward blocks under the appropriate sector's `scenarios.<scenario>.<class_key>` plus a cycle anchor under `cycle_anchors.<class_key>`.
6. Update any test in `tests/test_scenarios.py` that asserts on the cycle_anchors set (the set membership changes).
7. Run pipeline + tests.

### 8.3 Quarterly market-data refresh

The refresh has a **pre-flight check** before the data assembly proper — run the refresh checklist first to see exactly what's stale and what's missing for the target quarter.

**Step 0: Pre-flight check.** Run `python -m crude_tanker_fv.refresh` to generate `outputs/refresh_checklist.md`. The checklist:
- Infers the **target quarter** (the most recently closed quarter as of today — see §7.x for the inference rule, or pass an explicit quarter as CLI arg).
- Reports which **balance sheets are missing** for the target quarter, with per-ticker IR press-release URLs, SEC EDGAR filer URLs, and fleet-page URLs sourced from `inputs/data_sources.yaml`.
- Flags **stale market data** (files older than 30 days), **stale watchlist `as_of` dates** (older than 14 days), and **APPROX consensus_pnav entries** still flagged in the watchlist YAML comments.
- Surfaces a per-ticker **file age table** (fleet / BS / cost / dividend with their respective thresholds: 90d / required for target quarter / 180d / 180d) so multi-quarter drift surfaces explicitly.
- Closes with the **full IR URL playbook** — a per-ticker table of IR home, press releases archive, SEC EDGAR filings, fleet page — for ad-hoc lookups outside the refresh cycle.

This turns refresh from a "remember what to update" half-day grind into a structured task list that takes 5 minutes to scan and explicitly tells you which IR pages to open.

**Steps 1-7 (after the checklist):**

1. Pull the latest broker valuations (Compass / VesselsValue / Clarksons) and update `vessel_value_curves.yaml` anchors per class.
2. Pull the latest spot, 12-month TC, and FFA forward strip for each class — update the four rate files.
3. **VIE Market Rates & Trends cross-check** (added 2026-06-03). Pull the VIE Live Analytics Platform Market Rates & Trends tab (URL in `inputs/data_sources.yaml` under `_market_data_sources.vie_market_rates_and_trends`). Compare against `spot_tce.yaml` (VIE Q2 Live Est ≈ QTD spot average), `twelve_month_tc.yaml` (VIE per-quarter forward columns), and `historical_tce_means.yaml` (back-compute VIE-implied 10y means from the "Vs. 10y Avg" column). Material discrepancies feed `outputs/vie_market_rates_xref.md` and the refresh checklist. **Do NOT bulk-update from VIE without an explicit methodology decision per class** — our base-period and outlier-handling choices are deliberate (see e.g. LNGC's spike-inclusive comment in `historical_tce_means.yaml`).
4. Refresh disclosed second-hand transactions in `inputs/market_data/transactions/<class>.yaml` — the transaction-anchored toggle re-fits automatically on next run.
5. Refresh the watchlist prices, analyst targets, and any APPROX consensus_pnav entries with authoritative broker NAV prints, in `watchlist.yaml`. Also pull the **VIE Coverage Universe** tab (separate gid) and update `outputs/vie_coverage_universe_xref.md` if any watchlist name's VIE stance changed materially (§6 footnotes are the durable surface for stance disagreements).
6. Per-company Q+1 inputs (balance sheets, cost structures) refreshed from each name's latest filing — use the IR URLs from the checklist's playbook section.
7. Run `python -m crude_tanker_fv.pipeline {quarter}` + scan for `validate.py` warnings (extreme spot prints, constructed curves, etc.) and tag any new ones. The pipeline now ends with a delta report (§7.7) and per-ticker decision-log entries (§7.8) — those become the post-refresh review surface.

**Staleness thresholds** (locked 2026-06-01, defined in `src/crude_tanker_fv/refresh.py`):
- Market data: 30 days
- Watchlist `as_of`: 14 days
- Fleet manifest: 90 days (vessel sales / purchases happen quarterly)
- Cost structure & dividend policy: 180 days (rarely change; revisit annually)

These thresholds are tunable but treated as the standard sensitivity. Tighten them if you want earlier warnings; loosen if false positives become noise.

## 9. Open Methodology Decisions

Decisions that should be revisited as the model matures or new data becomes available:

1. **Cycle weighting curve shape** — currently a step function across five bands. Could be replaced with a continuous logistic, but step function is more interpretable. Revisit after first quarter of use.
2. **Terminal value at quarter 9 = 1.0× NAV** — arguably should be 0.9× NAV to reflect mid-cycle discount, or 1.1× if structural undersupply persists. **Sensitivity tested 2026-06-05** (`scripts/terminal_value_sensitivity.py` → `outputs/terminal_value_sensitivity.md`): sweep across {0.85, 0.9, 1.0, 1.1, 1.15} for the full 12-name watchlist. Single-point FV % range scales cleanly with `w_earn` (w_earn 0.30 ⇒ ~5-7%; w_earn 0.60 ⇒ ~13-14%). **3 names flip position at the literal §9.2 priors:** TNK and STNG flip HOLD → TRIM/SHORT under the 0.9× mid-cycle-discount prior; FLNG flips TRIM/SHORT → HOLD under the 1.1× structural-undersupply prior. No name flips on both sides. Highest-sensitivity name (CCEC, +14.4% FV range) does NOT flip — its BUY survives the full sweep. **Resolution still pending** — the sweep quantifies the size of the decision but does not pick a multiple; that needs a methodological prior, applied uniformly. Decision logs for TNK / STNG / FLNG should name the §9.2 choice explicitly until resolved.
3. **LR2 classification for FRO** — crude or product? Affects fleet weighting and rate inputs.
4. **INSW allocation method** — *resolved (§6 v2)*: hybrid carve-out allocates by vessel **market value** (not count, not EBITDA), with vessel-secured debt assigned directly to its sleeve and corporate/unsecured debt pro-rated by sleeve vessel-value share. Dual-use LR1 split 30% crude / 70% product. **Both sleeves now run through the scenario engine and aggregate to a whole-company FV** (the v2 product strip — MR/LR1_clean/LR2_clean forward curves under the four MoU scenarios, with the product sleeve weighted MORE bearish than crude to reflect "product is leading the rate normalization" per the May-29 MR -52% / LR2 -28% w/w prints). The scenario report shows the per-sleeve breakdown plus the whole-company aggregate vs the actual tape price; the FV report (single-point detail) remains crude-sleeve.
5. **Discount rate** — 11% chosen heuristically; could justify a CAPM-derived rate but high beta + cyclical premium probably lands in the same range.
6. **Newbuild commitments treatment** — *resolved (§3.1)*: for material orderbooks, committed newbuilds are valued at delivered market value less remaining commitment (not at sunk cost), since at cost they understate NAV by the embedded value of cheaply-contracted ships in a hot market (decisive for FRO, ~$5.7/sh). Still open: whether to PV-discount the delivered value for time-to-delivery (currently undiscounted; minor).
7. **Tax rate** — modeled at 2% (tanker shipping benefits from tonnage tax regimes). Verify per-company; some structures differ.
8. **Sanctioned / dark fleet ton-mile effects** — not currently modeled explicitly, but show up implicitly through spot TCE rates. Could be made explicit as a forward demand multiplier if structural shifts (Russia, Iran) persist.
9. **Vessel-mark level (tool vs broker)** — the tool's value curves are conservative independent marks; brokers (Compass / VesselsValue / Clarksons) mark the modern and product fleet higher. Disposal data (the only ground truth) validates the **old-age leg** of the tool curve; the mid-age and product anchors are looser (thin second-hand deal flow). Handled via two complementary diagnostics:

    - **Broker-NAV sweep** (`marks.py`, `pipeline.run_broker_sweep`): each name is valued at tool marks (k=1.00), midpoint, and broker-equivalent (the uniform vessel-mark premium k that lifts tool NAV to the consensus broker NAV = price / consensus P/NAV). The **tool→broker EV spread** shows how much of a name's call is a genuine price-vs-value signal vs a NAV-mark choice — ~0 for mark-validated pure-plays (DHT/FRO/ECO, k_broker≈0.99), wide for mark-uncertain blended-fleet names (TNK k_broker≈1.18 / +10pp; INSW k_broker≈1.37 / +21pp).
    - **Transaction-anchored curve recalibration** (`transactions.py`, `pipeline.run_transaction_anchored_comparison`): opt-in toggle (`use_transaction_anchored=True`) that replaces the mid-age (5yr, 10yr) anchors of any class with a populated `inputs/market_data/transactions/<class>.yaml`. Newbuild + old-age legs are NOT touched (newbuilds publicly priced; old-age disposal-validated). The fit is a recency-weighted (~15-month half-life) WLS regression of clean prices (quality-flag uplifts: financing +5%, distressed +10%) on age, in the mid-age window [3, 17]; slope must be negative or the fit falls back. The v1 LR2-as-Aframax proxy propagates the Aframax fit to LR2 automatically.

    *Scope discipline:* recalibrate one class at a time, anchor to disclosed transactions, stop when the transaction sample is exhausted.

    **Aframax** was the first target (broker mid-age clearly above transactions: TNK Jan 2026 sale-leaseback of 3× 2016 hulls at $47.2M ea vs Compass 10yr ~$68M); fit moved 10yr −12.8%.

    **Suezmax** was the second target — *closed 2026-06-01*. Primary anchor is the TNK 2009-built (age 17) Suezmax sold at $53.5M, disclosed as a subsequent event in TNK's Q1 2026 reporting and **confirmed clean-market** by TradeWinds (6 May 2026, "eye-catching price" to a Greek buyer during the hot Middle East crisis spot environment). Mid-age sample: trade-press 2025 / Q1-2026 prints in the [6, 12]-yr range. Fit produced **5yr +9.2%** ($92M → $100.5M), **10yr +1.3%** ($80M → $81M), **slope −$3.89M/yr**, and **reproduces the TNK $53.5M anchor with a +0.6% residual**. The age-17 anchor at $53.5M geometrically constrains the mid-age curve slope; **no defensible fit produces the 15-30% 10yr lift that would be required to bring NAT's tool P/NAV into its historical 0.7-1.0× band**. **Conclusion: the Suezmax curve is validated. NAT's residual gap is not a curve calibration issue** — it is the structural framework limitation documented in §12 (high-payout pure-plays during cycle peaks).

    **VLCC** transaction sample added 2026-06-04 (PM): `vlcc.yaml` ships 5 in-window arm's-length 2026 prints (Frontline 8-vessel disposal, CMB.TECH Ingrid/Ilma, Teekay Singapore Spirit, CSSC Liaoning, Hyundai Samho chatter) + Sinokor +10-15% premium campaign as out-of-fit documentation. Fit produces **5yr −15.6%** ($138M → $116.5M) / **10yr −13.1%** ($111M → $96.4M) / **slope −$3.44M/yr** — a substantial directional move comparable in size to the original Aframax fit. **Important correction to the prior closure language:** the previous paragraph claimed VLCC was "validated separately by pure-play P/NAV reconciliation (DHT within ~1% of consensus) and the TNK Q2 2026 VLCC disposal (2013-built $84.5M ≈ curve)." That validation logic was overstated — the TNK $84.5M print actually sits 9% below the existing curve at age 13, and the full 5-print sample shows a systematic 10-15% high bias at the modern end. The DHT-pricing-close-to-broker-consensus observation validated that broker NAV and tool NAV roughly agree on DHT; it did NOT validate either against transaction reality. Impact: DHT NAV drops 11.5% under the VLCC fit; ECO/INSW crude sleeves drop proportionally. §11.5 "Crude-class transaction anchoring" subsection documents the full per-class fits and per-name impacts.

    **MR / LR2 product transaction samples** added 2026-06-04 (PM): `mr.yaml` (2 in-window STNG scrubber-MR prints + 4 out-of-window NB documentation entries) and `lr2.yaml` (1 in-window STNG STI Goal/Gallantry print). MR fit produces 10yr +10.1% / 5yr +2.2% (clamped). LR2 fit falls back (n<2) and inherits the Aframax proxy fit — the proxy-alias logic in `transactions.py` was refactored from "fire when alias has no own file" to "fire when alias has no valid own fit" so a sparse `lr2.yaml` keeps inheriting Aframax until ≥2 LR2 prints accumulate. §11.5 documents the full empirical test of the product-side hypothesis #2.

    *Current state (2026-06-04 evening):* the transaction-anchored recalibration is now populated for **VLCC + Suezmax + Aframax + MR** (each with own valid fit) plus **LR2** (own file as data documentation; inherits Aframax proxy until enough prints clear the fallback guard). **Do not** add further classes (LR1, Handysize, LNGC, MGC) to the transaction-anchored recalibration without an analogous transaction sample of comparable quality. The `apply_transaction_anchored_curves` pipeline correctly handles the proxy alias case; no additional code changes needed when LR2 graduates to its own fit.

10. **Weight-robustness diagnostic (§9.10)** — a per-name classification of probability-weight sensitivity that complements the §9.9 mark-robustness sweep and operationalises the §13 limitation framework (scenario-weight stability under infrastructure shocks). Methodology: run each name through the production scenario-routing path under multiple defensible weight sets (typically the current production lock plus 2-3 bracketing alternatives spanning the dominant axis of uncertainty); record per-set PW FV / EV% / position; classify as **weight-robust** if the position recommendation is the same across all evaluated sets, **weight-driven** if it changes. Implemented per-sector — crude in `scripts/crude_weight_robustness.py` → `outputs/weight_robustness_diagnostic.md` + `.xlsx`; LNG in `scripts/lng_weight_comparison.py` → `outputs/lng_weight_robustness.md`. Read together: §13 provides the *conceptual* limitation framing (weights are point-in-time); §9.10 provides the *operational* diagnostic that measures sensitivity to that limitation; §11.3 documents the *specific decisions* (LNG Set B → Set B-revised) the diagnostic supported.

    *Interpretation:* weight-robust calls survive across multiple defensible probability priors and carry higher conviction than weight-driven calls. **Combined with §9.9 mark robustness, every name has two independent robustness dimensions** — paired in the per-sector diagnostic output as:

    - **Mark-robust + weight-robust** = highest conviction (call survives both judgemental input axes)
    - **Mark-driven OR weight-driven** (one of two) = mixed conviction; the call's risk is concentrated in the named dimension
    - **Mark-driven AND weight-driven** = lowest conviction; treat with explicit sizing discipline

    *Frequency:* run quarterly alongside the refresh checklist, or whenever new evidence prompts weight reconsideration (the LNG Set B → Set B-revised lock 2026-06-01 surfaced via this diagnostic). The diagnostic does NOT change locked weights — it surfaces sensitivity for the position-sizing layer to consume.

    *Naming-namespace discipline:* each sector uses its own weight-family labels. The crude family uses Crude Set A/B/C/D; the LNG family uses Set B / Set B-revised (METHODOLOGY §11.3); the product family currently inherits LNG weights and has no independent set labels yet. Cross-sector conflation of set names (e.g. "Set B" without sector qualifier) is a methodology error. Diagnostic outputs always carry the sector prefix.

    *Current state (2026-06-01 lock):* on the crude side, DHT / ECO / FRO are mark-robust + weight-robust (highest-conviction TRIM); INSW is mark-driven but weight-robust (TRIM survives any reasonable crude reweighting); **TNK is the only name that is both mark-driven and weight-driven** — its HOLD signal flips to TRIM/SHORT under a bearish Set D reweighting and the +10pp broker spread adds independent mark uncertainty. NAT is mark-driven and weight-robust on direction but always carries the §12 high-payout-pure-play caveat overriding the framework signal. On the LNG side, CCEC is weight-driven (BUY only under Set B-revised; HOLD under Set A/B) and mark-validated; FLNG is weight-robust (TRIM/SHORT across all evaluated sets) and mark-driven (k_broker 0.87 tool-above-broker).

11. **Consensus forward-EPS cross-check (§9.11)** — the **earnings-leg analog of the §9.9 broker-NAV sweep**. The sweep cross-checks the *asset* leg of the blend (does our NAV agree with broker consensus?); §9.11 cross-checks the *earnings* leg that drives the dividend strip (do our modelled forward earnings agree with sell-side consensus?). The three legs are now all independently checked: NAV (§9.9 broker sweep), scenario weights (§9.10), and forward earnings (§9.11). Implemented in `consensus_eps.py` / `pipeline.run_consensus_eps_xref` → `outputs/consensus_eps_xref.md` + `.xlsx`.

    *Mechanism:* back out consensus next-twelve-months EPS = `price / consensus_fwd_pe` (Pareto Shipping Daily 1Y FWD P/E, stored per-name in `watchlist.yaml`), and compare to our own NTM forward EPS — the sum of the first four quarters of the dividend strip's `eps_by_quarter` (FFA-forward-curve-implied operating EPS, net of tax). Both are operating-EPS constructs (each excludes one-off vessel-sale gains), so the comparison is apples-to-apples. The row reports `eps_gap_pct = (tool − consensus) / consensus`, the consensus earnings yield (`1 / fwd P/E`), the name's `cycle_position` + band, and **`w_earn`** (the strip's weight in the blend).

    *Interpretation:* a large positive gap (tool ≫ consensus) means our forward-curve earnings run hotter than the street — the FFA curve holds elevated near-peak rates while consensus prices mean-reversion. **This is expected near a cycle peak, and the framework already compensates: `w_earn` is low exactly when the gap is widest.** A wide gap paired with a low `w_earn` is the cycle weighting working as designed, NOT a calibration error — and §9.11 is the diagnostic that makes this mitigation visible and auditable. The signal to *act* on is a wide gap paired with a *high* `w_earn` (a below-mid-cycle name whose strip is trusted but whose forward EPS the street doesn't share).

    *Initial run (2026-06-04, Pareto 4-Jun P/E):* **every name shows tool EPS > consensus** (+72% to +462%), confirming the FFA-strip-vs-consensus normalisation gap is universal at this cycle point. Crude names at peak (cycle ≈ 2.79×) carry the widest gaps (+160% to +208%) but the lowest `w_earn` (0.30) — heavily mitigated. **NAT +462%** is the §12 high-payout pure-play flagged from the earnings angle (consensus pays 17× for the dividend, not the earnings). The actionable exceptions are the **below-mid-cycle names with `w_earn` 0.60 — CCEC (+219%) and FLNG (+83%)** — where the hot tool EPS is *least* mitigated; CCEC's case reinforces the §9.10 / §13 "weight-driven BUY, size with discipline" caution from an independent (earnings) angle. ASC carries the smallest gap (+72%), consistent with its softer-product read.

    *Limitations:* 1-year horizon only (the strip is 8q + terminal NAV, so this checks only the front end); EPS ≠ dividends (payout policy and buybacks — STNG's buyback channel is invisible to both EPS and the strip); shipping consensus EPS is dispersed and lags spot. A **directional cross-check, not a calibration target** — no rate or weight inputs are changed by it.

    *Frequency:* run quarterly with the refresh checklist (the `consensus_fwd_pe` values refresh from each new Pareto Shipping Daily alongside `consensus_pnav`).

## 10. Caveats

- This is a methodology, not advice. Outputs are model estimates with uncertainty bands wider than the point numbers suggest, especially on vessel values without paid broker access.
- Tanker equities have heavy idiosyncratic risk that the model does not capture: M&A activity, management decisions, sanctioned-flow exposure (positive or negative), regulatory changes (IMO 2030 emissions, etc.).
- The cycle weighting framework is a heuristic, not a forecast. It does not predict turning points; it adjusts how much to trust the dividend strip in the current environment.
- Past peak dividends are not future dividends. The model assumes mean reversion in the terminal value but allows the front-loaded dividend strip to reflect current strength.
- **MEG export capacity recovery is an unmodeled supply-side constraint (§14).** Scenario TCE forwards through 2026 assume MEG export volumes ramp in step with vessel transit capacity post-MoU; the empirical picture is that volumes lag transit. Near-term Phase 2 signals on names with high MEG-route exposure (VLCC, Suezmax, Aframax-loading-MEG) should be read alongside the §14.4 qualitative overlay.
- **The framework's 10-year mean TCEs are TC-anchored, not spot-anchored.** `historical_tce_means.yaml` reflects what a one-year time charter would have locked in over a 10-year window — smoothed by the TC contract structure, which **structurally excludes negative spot prints** (owners don't sign multi-month charters at a loss; the floor is at operating cost). This is the methodologically correct denominator for our cycle-position ratio (METHODOLOGY §2.3) because the numerator is also a TC (12M Compass TC). External commentary (VIE, raw Baltic publications) often cites spot-anchored 10-year means, which include deep-negative periods (e.g. VLCC TD3C spot TCE clearing around −$34,845/day in 2020-2022 per SpotMarketCap). Spot-anchored means are structurally lower than TC-anchored means — the gap is a known methodology difference, not a calibration error. Both are internally consistent; they answer different questions ("what would I have locked in?" vs "what did the average day historically pay, loss-making days included?"). **VIE-style cycle multipliers (e.g. "+482% vs 10y avg") are useful for directional commentary but do not numerically compose with our cycle-position ratios**; a name showing "+482%" on VIE is not interchangeable with "2.79× our cycle position." Direct cross-reference at the magnitude level requires unit alignment that we don't have. See `outputs/vie_market_rates_xref.md` for the worked example and LIMITATIONS.md for the credibility-level callout.

#### VIE methodology comparison — within-window structural adjustments (added 2026-06-04 PM)

A refinement to the TC-vs-spot caveat above: VIE's published "Vs. 10y Avg" multipliers incorporate **class-specific, constant structural-adjustment factors** on the denominator — 1.0 for dry bulk (no adjustment), **0.9 for tankers (VLCC / Suezmax / Aframax / LR2 / MR2) and VLGC** (−10% adjustment), and **0.7 for LNG TFDE** (−30% adjustment). The factors compensate for structural changes within the 10-year lookback window that affect different classes differently — notably the post-2018 TFDE → MEGI / X-DF / X-DF2.1 propulsion transition (driving the LNG factor) and the more modest tanker structural shifts (eco-design adoption, IMO 2020 fuel transition, sanctioned-fleet evolution). Applying these factors and back-computing collapses the apparent VLCC gap from +58% to **+42%**, Suezmax from +14% to **+3%**, Aframax from +15% to **+4%**, MR2 from +18% to **+6%**, and LNG TFDE from +53% to **+7%** vs our values. The collapse to within ~7% for Suezmax / Aframax / MR / LNG is **meaningful cross-methodology corroboration** that those anchors are in the right neighborhood. VLCC and LR2 retain larger residuals (+42% / +24%) warranting separate investigation if calibration discipline ever calls for it. **The two methodologies differ in whether structural adjustment is implicit (our TC anchor, which captures it via contemporaneous market-clearing prices at each historical point) or explicit (VIE's class-specific factor application).** Both are methodologically defensible. See `outputs/vie_market_rates_xref.md` for the worked corrected back-computations and discussion.

**Self-check item (recurring discipline):** verify our 10-year means in `historical_tce_means.yaml` are TC-anchored throughout, not spot-anchored. If any spot-anchored components are inadvertently mixed in, consider whether an explicit within-window structural adjustment (analogous to VIE's 0.9 / 0.7 factors) would be appropriate. Currently not flagged as a concern; included as a refresh-time discipline check.

## 11. Sector portability — the scenario layer

The valuation skeleton (NAV + dividend strip blended via a cycle-position weight, scenario-weighted across a small set of probability-weighted forward curves) is sector-agnostic; what varies between crude tankers, LNG carriers, product tankers, dry bulk etc. is the **scenario set** and the **10-year mean** anchoring the cycle ratio. The v1 build collapsed both into a single top-level `scenarios:` block in `inputs/scenario_inputs.yaml` named for the three-phase MoU framework (escalation / pre-MoU baseline / MoU base / MoU bear). Adding FLNG required reusing those crude scenario names on an LNG-interpreted forward curve — workable for one test name, but a name collision that does not extend.

The sector layer factors this out.

### 11.1 File shape

`inputs/scenario_inputs.yaml` is keyed by sector:

```yaml
sectors:
  crude:
    scenarios:
      escalation:        {weight: 0.10, vlcc: …, suezmax: …, aframax_dirty: …, lr2_clean: …}
      pre_mou_baseline:  {weight: 0.15, …}
      mou_base:          {weight: 0.50, …}
      mou_bear:          {weight: 0.25, …}
    cycle_anchors:       {vlcc: …, suezmax: …, aframax_dirty: …, lr2_clean: …}
  lng:
    scenarios:
      tight_resurgence:    {weight: 0.10, lng: …, mgc: …}
      moderate_tightening: {weight: 0.15, …}
      glut_base:           {weight: 0.50, …}
      glut_intensifies:    {weight: 0.25, …}
      structural_reset:    {weight: 0.00, vessel_scale_multiplier: 0.90, …}
    cycle_anchors:       {lng: {ten_year_mean: 85000, …}, mgc: {ten_year_mean: 20000, …}}
  product:
    scenarios:
      refinery_squeeze:    {weight: 0.10, mr: …, lr1_clean: …, lr2_clean: …}
      moderate_correction: {weight: 0.15, …}
      glut_base:           {weight: 0.50, …}
      demand_softening:    {weight: 0.25, …}
      structural_decline:  {weight: 0.00, vessel_scale_multiplier: 0.90, …}
    cycle_anchors:       {mr: {ten_year_mean: 16000, …}, lr1_clean: …, lr2_clean: …}
```

`load_scenarios(sector=...)` returns one sector's `{scenarios, cycle_anchors, sector}` sub-doc; `run_scenarios(...)` consumes that sub-doc unchanged (the engine itself stays sector-agnostic). The sector name is stamped onto the returned `ScenarioReport.sector` so the markdown title flexes per sector ("three-phase MoU framework" vs "LNG glut-cycle framework") and the roll-up writes one Excel sheet per sector with that sector's scenario columns.

### 11.2 Per-ticker resolution

`inputs/watchlist.yaml` carries a `sector:` field per ticker; default `crude` if absent. `pipeline._resolve_sector` reads it and `_load_all_sectors` pre-loads all sector sub-docs ({crude, lng, product}) once per pipeline run. The hybrid INSW carve-out (METHODOLOGY §6 v2) routes its **crude sleeve through `sectors.crude`** and its **product sleeve through `sectors.product`** — see §11.5 for the product sector that closed the v2 INSW shortcut.

### 11.3 LNG sector weight history — v1 → v2 (Set B) → v3 (Set B-revised)

The LNG scenario weights have transitioned through three locks. The current production lock is **Set B-revised (v3, 2026-06-01)** — see the v3 sub-section below for the rationale tied to the 2026 supply environment. Earlier locks are preserved here as history.

#### v1 (placeholder, ~2026-04) → v2 (Set B, 2026-06-01)

The crude sector keeps its v1 weights `{escalation 0.10, pre_mou_baseline 0.15, mou_base 0.50, mou_bear 0.25}` unchanged. The LNG sector launched in v1 with the same `{0.10, 0.15, 0.50, 0.25}` weights as a placeholder so FLNG's headline FV was preserved through the sector refactor. **v2 transition completed 2026-06-01 with Set B locked**:

| LNG scenario | v1 placeholder | **v2 (Set B)** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.10 | **0.10** | unchanged |
| moderate_tightening | 0.15 | **0.15** | unchanged |
| glut_base | 0.50 | **0.55** | +0.05 |
| glut_intensifies | 0.25 | **0.20** | −0.05 |
| structural_reset | — | **0.00** | newly curated, weight 0 |

Set B headline impact: FLNG PW FV $25.90 → $26.17 (EV −14.3% → −13.4%, position TRIM/SHORT unchanged). Set B reflects historical LNG cycle behaviour — US Gulf Coast capacity ramp through 2027 + LNG cyclical bears historically shallower than crude's MoU-bear analogue.

#### v2 (Set B) → v3 (Set B-revised, 2026-06-01)

**Set B-revised replaces Set B as the production lock the same day it was applied, reflecting the 2026 supply environment as observed:**

| LNG scenario | v2 (Set B) | **v3 (Set B-revised)** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.10 | **0.15** | +0.05 |
| moderate_tightening | 0.15 | **0.25** | +0.10 |
| glut_base | 0.55 | **0.45** | −0.10 |
| glut_intensifies | 0.20 | **0.15** | −0.05 |
| structural_reset | 0.00 | **0.00** | unchanged |

**Constructive total (tight + moderate + glut_base):** Set B 0.80 → Set B-revised **0.85**.

**Set B-revised headline impact:**

| Ticker | Set B PW FV | Set B-revised PW FV | Δ | Position change |
|---|--:|--:|--:|---|
| FLNG | $26.17 (EV −13.4%) | $28.04 (EV −7.2%) | +$1.87 (+7.1%) | TRIM/SHORT → TRIM/SHORT (closer to HOLD threshold) |
| CCEC | $22.94 (EV −1.0%) | $26.45 (EV +14.1%) | +$3.51 (+15.3%) | **HOLD → BUY (flip)** |

Pinned by `test_flng_v3_set_b_revised_fv_band` and `test_ccec_v3_set_b_revised_fv_band_and_buy_flip`.

##### Rationale (Set B-revised)

The empirical 2026 LNG environment is **tight-market-pricing, not glut-pricing** — Set B's 55% on `glut_base` implicitly asserted glut as the dominant 2026 condition, which the observable evidence contradicts:

- **Ras Laffan Trains 4 & 6 (12.8 mtpa / ~17% of Qatar LNG) offline through end-summer 2026 at earliest** per QatarEnergy disclosure (June 2026 macro briefing + VIE/Seeking Alpha analysis from Catlin, May 25 2026). Restart risk extends beyond end-summer due to subsurface/mechanical complications of prolonged shut-in. This partially offsets the Cheniere Stage 3 ramp (Train 5 substantially complete, Train 6 first LNG imminent) through at least H2 2026.
- **Empirical pricing:** LNG spot at **$67,500** (+391% YoY per Pareto Shipping Daily), TFDE rates at **$98,500**. These are unambiguously tight-market levels, not glut levels. The 12-month TC at $98.5k is the cycle position the model reads — Set B's bearish base case is inconsistent with the rates being observed.
- **Glut timing shifts to 2027, not Q3 2026.** Glut consensus still arrives once Ras Laffan restarts and Cheniere Stage 3 finishes ramping — but the timing of that transition is late-2026 / early-2027, not mid-2026. Set B-revised reflects that 2026 is mid-tight (moderate_tightening band) and the glut weight (still 0.45 — the plurality) captures the 2027+ regime.
- **Glut_intensifies trimmed from 0.20 → 0.15.** The 2026 supply environment with both Ras Laffan offline and current rates at multi-year highs doesn't justify extreme cyclical-bear weight; the 5pp moves into the constructive band.

##### Relationship to §13 (the meta-process limitation) and §9.10 (the diagnostic methodology)

The Set B → Set B-revised transition documented in this subsection is the **worked example** referenced from §13 (scenario-weight stability under infrastructure shocks). §13's general framing — "weights are point-in-time best estimate, not stable parametric calibration; methodology owner re-evaluates after material infrastructure shocks" — was operationalised here as the response to the Ras Laffan disclosure landing within weeks of the v2 (Set B) lock. The mechanics of running the comparison are documented in §9.10 (weight-robustness diagnostic): `scripts/lng_weight_comparison.py` produces the per-name FV / EV / position table under both weight sets and surfaces the CCEC position flip as a weight-driven signal. Read together: §13 says *why* re-evaluate; §9.10 says *how* to evaluate; §11.3 v3 documents the *specific decision* that resulted.

##### Relationship to the §14 infrastructure constraint

Set B-revised reflects a **balance** between two opposing structural factors: (a) the US Gulf Coast capacity ramp (Cheniere Stage 3) which would normally tilt 2026 toward `glut_base`, and (b) the Ras Laffan + broader MEG export infrastructure constraint (§14) which slows that ramp's effective supply impact through at least H2 2026. Set B-revised's `glut_base: 0.45` is the resulting central weight — neither pure-glut (which would be Set B's 0.55) nor pure-tight (which would push to 0.60+). The §14 limitation remains a **separate, qualitative overlay** on top of Set B-revised: weights capture the probability of each scenario unfolding; §14 notes that even within the `glut_base` and `moderate_tightening` scenarios the Q3-Q4 2026 TCE forwards may be conservative on rate level if MEG capacity recovery lags vessel transit. The framework discipline is to keep these two layers explicit rather than fold §14 into the weights.

##### Anti-hindsight discipline

The reweighting was **specified based on the supply-environment evidence before per-name FV impact was computed**. CCEC's flip from HOLD to BUY is a *finding*, not the target. The candidate weights came from the news cycle (Ras Laffan + Cheniere + observable rates); the per-name computation showed FLNG improves but doesn't flip, and CCEC flips firmly. The asymmetry is structurally driven by CCEC's $2.25B newbuild orderbook providing 2× the scenario torque of FLNG's mature TC-heavy book — see the per-scenario FV tables in `outputs/lng_weight_robustness.md`.

##### What the CCEC BUY flip means (and what it doesn't)

CCEC's BUY signal under Set B-revised is a **leveraged expression of the LNG-tight thesis, not a NAV-anchored value play**. CCEC's per-scenario FV ranges from $48.52 (tight_resurgence) to $1.05 (structural_reset) — extreme dispersion driven by the NB-option leverage. Position sizing for CCEC should reflect that the call's robustness depends heavily on LNG market direction. Contrast with FLNG, whose per-scenario FV ranges $39.76 to $14.58 — much narrower dispersion, more NAV-anchored. The same weight shift moves the two names differently because their structures are different — Set B-revised's case is qualitatively stronger for CCEC.

##### What `structural_reset` retains

The energy-transition tail remains curated at weight 0.00, same treatment as in Set B. The recommended **−5 to −15% qualitative overlay** for energy-transition timing is unchanged. See the §11.3 v2 rationale subsection above.

##### What this lock does NOT do

Does NOT modify any LNG scenario forward curves (TCE assumptions stay where they are). Does NOT touch crude or product scenario weights — they remain at v1 / v3 respectively. Does NOT change `structural_reset` parametrisation. Does NOT extend to MGC scenario weights (MGC weights stay at the LNG-inherited Set B-revised values; MGC-specific weights are a future v4 work block).

#### v3 (Set B-revised) → Jun-9-2026 POINT-IN-TIME (v4)

**This is NOT a permanent lock.** The Jun-9 set is dated, conditional, and explicitly tagged in `scenario_inputs.yaml` headers as point-in-time. It exists because the April/May MoU/ceasefire path failed to physically reopen Hormuz, and as of Jun-8 a US helicopter was downed near the strait with ceasefire faltering. The standalone analysis brief (Appendix A panel) backtests show the May-29 set (which leaned mou_base 0.50 the day after an unsigned deal) was disconfirmed within ~10 days — that lesson is now codified as the **confirmation-gated, not announcement-gated** discipline (see also §13).

| LNG scenario | v3 (Set B-revised) | **Jun-9 v4 point-in-time** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.15 | **0.25** | +0.10 |
| moderate_tightening | 0.25 | **0.25** | unchanged |
| glut_base | 0.45 | **0.38** | −0.07 |
| glut_intensifies | 0.15 | **0.12** | −0.03 |
| structural_reset | 0.00 | **0.00** | unchanged |

**Rationale.** Qatari LNG transits Hormuz; a contested strait is a direct `tight_resurgence` trigger. Weight migrates from glut-side scenarios (cyclical glut consensus weakens when a major supply source is at infrastructure risk) to the tight upside.

**Headline impact (regenerated 2026-06-09):**

| Ticker | v3 PW FV | Jun-9 v4 PW FV | Δ | Position change |
|---|--:|--:|--:|---|
| FLNG | $28.04 | $29.73 | +$1.69 | TRIM/SHORT → HOLD |
| CCEC | $26.45 | $29.63 | +$3.18 | BUY → BUY (firmer, +14.5pp EV) |

**Companion fix landing with Jun-9 weights — `structural_reset` shoulder quarters.** Pulled below `glut_intensifies` in q3_2026 / q2_2027 / q3_2027 for both `lng` and `mgc` sub-classes. The prior values had `structural_reset` printing 25% above `glut_intensifies` in q3_2026 — defensible as "flatter, lower-mean" but reading as a bug. Weight remains 0.00 so no parametric impact; the override-friendly tail now monotonically dominates the cyclical bear in shoulder quarters too.

**Companion fix — `mgc` weight family inherits v4 alongside `lng`.** Same weights apply across both sub-classes (the MGC-specific weights deferred in the v3 doc are deferred again at v4 — same `mgc` weights as `lng` is the simplest tractable choice).

**Revisit trigger.** Re-evaluate when the US response to the Jun-8 helicopter downing resolves. Master state variable is **physical Hormuz transit** (verified at pre-war volumes, mines cleared), NOT a fresh deal announcement. See Appendix A for the full Feb-27 → Jun-9 weight-history panel + the locked benchmark `{0.10/0.15/0.50/0.25}` retained for future backtest scoring (§Task 3 backlog).

##### What this lock does NOT do

Does NOT modify any LNG scenario forward curves (TCE assumptions stay where they are; only `structural_reset` shoulders moved). Crude and product weights ALSO moved on the same Jun-9 reset — see §11.x for those parallel transitions. The `vessel_scale_multiplier` calibration is unchanged.

#### The `vessel_scale_multiplier` mechanism

The `structural_reset` scenario introduced a small extension to `scenarios.py`: optional per-scenario field `vessel_scale_multiplier` that applies after the elasticity-derived `vessel_scale` (with reclamping). For `structural_reset` the field is `0.90` — a −10% accelerated-retirement haircut on top of the elasticity flex.

**The mechanism is preserved in code even with structural_reset's weight at 0.00.** It remains available for future use if (a) better data emerges on energy-transition timing or magnitude, (b) other sectors (product, dry bulk) need analogous structural-tail treatment, or (c) a specific LNG name has fleet characteristics — older steam-turbine vessels, single-yard concentration — that justify a fleet-specific structural haircut applied via a custom scenario.

#### What this lock closes

- `data_gaps.lng.lng_scenario_weights` is resolved (Set B).
- `data_gaps.lng.structural_reset_tail` is reclassified — the scenario is curated and available, but explicitly NOT used as a parametric weighted input; documented as a sensitivity/override tool.
- The crude-inheritance compromise is removed; LNG is now fully LNG-specific (curves + weights + cycle anchor).

The sector portability claim is therefore fully defensible: architecture (sector layer + class map), data (LNGC curves + LNG forwards + LNG 10yr mean), and probability calibration (Set B weights) are all LNG-specific. Onboarding additional LNG names (CCEC, GLNG, etc.) requires only data files (fleet manifest + BS + cost + dividend + watchlist `sector: lng` field) — no further scenario/methodology work.

### 11.4 Adding new sectors

To onboard dry bulk (SBLK / GOGL), chemical tankers, or another sector:

1. Add a new top-level `sectors.<name>` block in `inputs/scenario_inputs.yaml` with its own `scenarios` map and `cycle_anchors`.
2. Add the sector's vessel classes to `SCENARIO_CLASS_MAP_BY_SECTOR` in `scenarios.py` (mapping model class → scenario key) and append pretty labels to `_PRETTY` / `_SECTOR_FRAMEWORK_LABEL` for the markdown title.
3. Add the same classes to the module-level `SCENARIO_CLASS_MAP` if the routing is unambiguous across sectors (i.e. no class collision with another sector's mapping); otherwise pass the per-sector map explicitly via `run_scenarios(..., scenario_class_map=...)`.
4. Stamp `sector: <name>` on the relevant tickers in `inputs/watchlist.yaml`.
5. Populate the cost / balance-sheet / fleet manifests as for any pure-play name.
6. Update `pipeline._load_all_sectors` to include the new sector key.

No engine changes are required for additional sectors — `run_scenarios` already takes the sub-doc as an opaque set of scenarios and anchors. The pre-existing v1 simplification (LNG curves carried under crude scenario names) is removed.

### 11.5 Product sector — formalised 2026-06-01

The product sector was the third sector formalised, closing the v2 INSW shortcut: MR / LR1_clean / LR2_clean forwards previously lived under `sectors.crude.scenarios.<scenario>.mr` (and the LR2_clean entry was shared between crude dual-use LR2 and product LR2). After the refactor, all product-class forwards live cleanly under `sectors.product` and the INSW carve-out routes its **product sleeve through `sectors.product`** while keeping its **crude sleeve through `sectors.crude`**.

The five product scenarios (v2 / Set B weights shown — see v1 → v2 transition below):

| Scenario | Set A (v1) | **Set B (v2 lock)** | Description |
|---|--:|--:|---|
| `refinery_squeeze` | 0.10 | **0.15** | Refinery outages + jet/marine demand surge + ME tightening; the product upside tail |
| `moderate_correction` | 0.15 | **0.25** | May-2026 product correction stabilises at current levels |
| `glut_base` | 0.50 | **0.45** | MR/LR2 NB orderbook delivers; refining margins compress — the product central case |
| `demand_softening` | 0.25 | **0.15** | Refinery margin collapse + warm winter + EV gasoline + accelerated NB delivery |
| `structural_decline` | 0.00 | **0.00** | Energy-transition secular tail (EV peak / jet substitution / refinery rationalisation) — curated but inactive |

#### v1 product weights — Product Set A (placeholder, 2026-06-01 → 2026-06-03)

The v1 lock used Product Set A = {refinery_squeeze 0.10, moderate_correction 0.15, glut_base 0.50, demand_softening 0.25, structural_decline 0.00} — the same weights INSW's product sleeve was already using via the v2 shortcut. This preserved the INSW whole-company FV exactly through the sector refactor (only a tiny shift of ~$0.05/sh from `LR1_clean`'s cycle anchor moving from `lr2_clean`'s $27k 10yr mean to its own $25k). Set A was retained as a defensible placeholder pending empirical evidence to support a sector-specific calibration — same posture LNG took at its v1 → v2 transition (§11.3).

#### v1 → v2 transition — Product Set A → Set B (locked 2026-06-03)

**Set A overrun by empirical 2026 product environment.** Catlin's VIE product tanker macro update (2026-06-03) plus the Baltic Clean Tanker Index at multi-decade highs, cargo-mile demand gains (LR2 +6.62% YTD, MR2 +3.17% YTD per VV), and critical regional inventory shortages document a product market in which clean tanker earnings are running **>2× their historic average**. Set A's 50% on `glut_base` mis-centres 2026 — same diagnostic logic that motivated the LNG Set B → Set B-revised lock (§11.3 v3).

**Product Set B v2 weights:**

| Scenario | Set A (v1) | **Set B (v2 lock)** | Δ |
|---|--:|--:|--:|
| refinery_squeeze | 0.10 | **0.15** | +0.05 |
| moderate_correction | 0.15 | **0.25** | +0.10 |
| glut_base | 0.50 | **0.45** | −0.05 |
| demand_softening | 0.25 | **0.15** | −0.10 |
| structural_decline | 0.00 | **0.00** | unchanged |

**Constructive total (refinery_squeeze + moderate_correction + glut_base):** Set A 0.75 → Set B **0.85**.

**Headline impact:**

| Ticker | Set A PW FV | Set B PW FV | Δ | Position change |
|---|--:|--:|--:|---|
| ASC | $13.59 (EV −26.5%) | $14.24 (EV −23.0%) | +$0.65 (+4.8%) | TRIM/SHORT → TRIM/SHORT (still deep TRIM) |
| STNG | $68.75 (EV −13.0%) | $73.58 (EV −6.9%) | +$4.83 (+7.0%) | TRIM/SHORT → TRIM/SHORT (closer to HOLD: just −1.9pp below boundary) |
| INSW (whole-co) | $52.08 (EV −32.2%) | **$52.08 (EV −32.2%)** | **$0.00** | unchanged — see hybrid-aggregation property below |

Pinned by `test_asc_whole_company_fv_in_expected_band`, `test_stng_whole_company_fv_in_expected_band`, and `test_insw_whole_company_fv_preserved_through_product_sector_refactor`.

##### Rationale (Set B)

Mirrors LNG Set B → Set B-revised's shift direction exactly: +5pp upside tail, +10pp moderate constructive, −5pp central glut, −10pp cyclical bear, structural tail unchanged. The empirical case for product is **stronger** than for LNG because product rate spike is at multi-decade highs (LNG was at $98k 12M TC — tight but not historically extreme; clean product earnings are >2× historic average — historically extreme).

##### Same-day LNG / product label coincidence

Product Set B's destination weights {0.15, 0.25, 0.45, 0.15, 0.00} are **numerically identical** to LNG Set B-revised. This is not accident: both sectors face the same 2026 Iran-crisis empirical case. **The labels are NOT interchangeable** (per §9.10 naming-namespace discipline) — "LNG Set B" and "Product Set B" refer to different scenario sets with different forwards. The numerical coincidence is documentary, not structural.

##### Anti-hindsight discipline

The Set A → Set B candidate weights were specified BEFORE per-name FV impact was computed — same pattern as the LNG Set B → Set B-revised lock. Set B's shift direction was derived from Catlin's empirical evidence (rate spike, cargo-mile gains, regional shortages); the per-name impacts (ASC +$0.65, STNG +$4.83, INSW $0.00) are *findings*, not targets.

##### A notable property — INSW whole-co preservation through Set B

INSW whole-co PW FV is **unchanged** ($52.08 under both Set A and Set B). This is a property of `_aggregate_hybrid_report` (METHODOLOGY §6 v2): the hybrid carve-out builds the whole-co probability-weighted FV by pairing crude scenario *i* with product scenario *i* and using **crude scenario weights** as the aggregation probability. The per-scenario sum `c.fv + p.fv` is weight-independent, and the aggregation weights come from the crude doc. Therefore product weight changes affect pure-product names (ASC, STNG) but **do not affect INSW whole-co FV** under the current hybrid carve-out methodology. The preservation test now spans **both** the sector refactor (2026-06-01) AND the Product Set A → Set B v2 transition (2026-06-03); the test's `expected_headline` invariant uses the methodology equation directly rather than the simpler `sleeve_sum` approximation that only holds when product weights match crude weights numerically.

##### §14.6 cross-references

Product Set B reflects the **probability-weighted** constructive tilt for 2026. The **scenario TCE forwards** themselves still don't parametrically include the MEG export capacity recovery lag (§14.1), the LR2 cargo-switching optionality (§14.6.1 — particularly relevant for STNG given its 32-vessel coated-LR2 fleet, see §6 STNG entry), the sanction-waiver June 17 expiry (§14.6.2), or the post-reopen stockpile replenishment phase (§14.6.3). Set B weights + §14.4/§14.6 qualitative overlay together capture the framework's current view; either alone is incomplete.

#### v2 (Set B) → Jun-9-2026 POINT-IN-TIME (v3)

**Same Jun-9 reset event as LNG §11.3 v4 and crude.** The product sector sees the parallel weight migration plus a discrete bug fix on Q3-2026 LR1/LR2 forward curves (see "Companion fix" below).

| Product scenario | v2 (Set B) | **Jun-9 v3 point-in-time** | Δ |
|---|--:|--:|--:|
| refinery_squeeze | 0.15 | **0.25** | +0.10 |
| moderate_correction | 0.25 | **0.30** | +0.05 |
| glut_base | 0.45 | **0.30** | −0.15 |
| demand_softening | 0.15 | **0.15** | unchanged |
| structural_decline | 0.00 | **0.00** | unchanged |

**Rationale.** MEG product flows transit Hormuz alongside crude; refinery_squeeze gets the largest mass migration from glut_base. The base case widens (moderate_correction +5pp) reflecting reduced consensus on the glut. demand_softening is unchanged — the bearish demand-side story doesn't change under a supply-side shock; structural_decline stays curated at 0 weight as the qualitative-overlay tail.

**Companion fix landing with Jun-9 weights — Q3-2026 LR1/LR2 spike removal (Issue #1 from the standalone analysis brief).** The PRODUCT sector's `glut_base / demand_softening / structural_decline` LR1/LR2 forwards inherited the q3_2026 Phase-1 MoU spike from `sectors.crude.scenarios.{mou_base,mou_bear}.lr2_clean` when the v2 sector refactor copied those curves over. Crude scenarios have a legitimate Phase-1 spike (Hormuz disruption); product scenarios do not, so the spike was meaningless in the product context. Fix lands q3_2026 mids as: `glut_base 95k → 37k`, `demand_softening 48k → 32k`, `structural_decline 38k → 26k` (lr1_clean == lr2_clean invariant preserved). q4_2026 unchanged. **This deliberately breaks the prior "INSW whole-company FV preserved exactly through the v2 refactor" invariant** — the invariant was preserving a copy bug. INSW Q3-2026 LR2 weighted moves $114.5k → $109.4k under the full Jun-9 reset (weights + curves); isolated curve-only effect on the same weights would be $114.5k → $86.0k.

**Headline impact (regenerated 2026-06-09):**

| Ticker | v2 PW FV | Jun-9 v3 PW FV | Δ | Position change |
|---|--:|--:|--:|---|
| ASC | $14.50 | $15.07 | +$0.57 | TRIM/SHORT → TRIM/SHORT (narrower) |
| STNG | $73.40 | $76.37 | +$2.97 | HOLD → HOLD (firmer) |
| HAFN | $5.41 | $5.87 | +$0.46 | TRIM/SHORT → TRIM/SHORT (narrower) |
| TRMD | $25.59 | $27.83 | +$2.24 | TRIM/SHORT → HOLD |
| INSW | $52.08 | $64.59 | +$12.51 | TRIM/SHORT → TRIM/SHORT (much narrower) |

INSW moves are dominated by the crude-sleeve weight reset (mou_base 0.50 → 0.18 makes the biggest difference); the product-sleeve Q3-2026 LR2 correction contributes ~$3-4 of the move.

**Revisit trigger.** Same as LNG: re-evaluate when the US response to the Jun-8 helicopter downing resolves. Master state variable is physical Hormuz transit.

##### What this lock does NOT do

Does NOT modify any product scenario forward curves except the Q3-2026 LR1/LR2 fix described above. Does NOT touch product class routing (`SCENARIO_CLASS_MAP_BY_SECTOR["product"]` unchanged). Does NOT change `structural_decline.vessel_scale_multiplier` (still 0.90). Does NOT extend a Product `mgc` equivalent — product sector has no MGC class.

#### `structural_decline` and `vessel_scale_multiplier`

Analogous to LNG's `structural_reset`: the product structural-tail scenario carries a `vessel_scale_multiplier: 0.90` (−10% accelerated-retirement haircut). Captures EV gasoline demand peak, jet-fuel substitution via SAF, OECD refinery rationalisation (2-3 mb/d 2026-2030), and marine ammonia/methanol bunkering displacing some marine gasoil. Weight 0 because the timing/magnitude within 2028-2035 is too judgmental for parametric weighting; applied as a qualitative −5 to −15% overlay on the product FV per individual transition-timing view.

#### Class routing — the LR1 / LR2 sleeve split

The product sector unlocks the architecturally-correct treatment of dual-use vessels. In `SCENARIO_CLASS_MAP_BY_SECTOR`:

| Class | Crude context | Product context |
|---|---|---|
| LR2 | `lr2_clean` (sectors.crude — FRO dual-use LR2) | `lr2_clean` (sectors.product — pure-product LR2) |
| LR1 | `aframax_dirty` (dirty leg of dual-use LR1) | `lr1_clean` (clean leg, has its own forwards as of 2026-06-01 — v1 proxy = LR2_clean values) |
| MR | n/a | `mr` |

For pure-product tickers (`sector: product` in watchlist), `pipeline._run_scenarios_for_ticker` routes through `sectors.product` and uses the product class map. For hybrid INSW: crude sleeve → `sectors.crude` + crude map; product sleeve → `sectors.product` + product map.

#### What this unlocks

- **STNG / TORM / Hafnia / Ardmore** — pure-product tanker names valued directly via `sectors.product`; templated-mode onboarding per §8.1.
- **Clean INSW architecture** — the v2 shortcut where MR forwards lived under `sectors.crude` is retired. The hybrid carve-out is now structurally clean: each sleeve has its own sector doc with its own scenario set and cycle anchors.
- **Future product-v2 weight lock** — when product cycle data supports a product-specific weight distribution different from the inherited {0.10/0.15/0.50/0.25}, the lock procedure mirrors LNG §11.3.

#### Cross-methodology comparison — product-sector tool TRIM vs VIE Bullish (added 2026-06-04)

As of mid-2026, the framework's product sector calls (ASC TRIM, TRMD TRIM, HAFN TRIM) diverge from VIE's Bullish stance on the same names. STNG is TRIM in our framework and Watch (HOLD-equivalent) in VIE — both methodologies converge on the cautious side, but VIE doesn't go bullish on STNG the way it does on ASC / TRMD / HAFN. **This is a sector-level pattern, not name-specific noise.**

Possible explanations:

1. **VIE forward curves on product reflect more constructive cyclical assumptions** than our scenario forwards capture. Product Set B v2 (locked 2026-06-03) already incorporates Catlin VIE's Iran-crisis-tightness reweighting (+10pp constructive vs Set A); VIE's stance implies their forward-curve assumptions go further than even Set B's reweighted distribution captures.
2. **Our MR / LR1 / LR2 vessel curves are conservative vs current second-hand transaction prices.** Unlike the Aframax and Suezmax curves (which have been transaction-anchored per §9.9 against TNK / NAT disposal prints), no product-class transaction-anchored recalibration has been applied. The tool-vs-broker spreads on product names (ASC +40pp, HAFN +29pp, INSW +22pp on the product sleeve) are likely driven in meaningful part by this absent recalibration.
3. **The product sector is in a transitional phase** where both methodologies may be partially right — we're too bearish on the strength of current cycle tightness; VIE may be too bullish on the durability of the post-Iran-crisis rate environment; the true path lies between.

**Implication for usage:** product sector TRIM signals carry less conviction than crude sector TRIM signals where transaction validation exists. Position sizing on product names should reflect this **structural mark uncertainty**. A product short basket should be smaller and more diversified than the equivalent crude short basket would be. The combined-conviction matrix in §9.10 already classifies the affected product names as mark-driven (ASC +40pp, HAFN +29pp, INSW +22pp) or VIE-opposed (ASC, TRMD, HAFN); pairing both signals across a single sector — as here — is a sector-level conviction softener distinct from any name's individual classification.

**This is not a calibration error to fix** — it's a known methodology divergence to document. The §10 baseline-methodology caveat already establishes that our framework and external commentary can produce internally-consistent but numerically-non-composable readings on the same underlying environment; this product-sector pattern is one specific instance.

**Re-evaluate after Q2 2026 product tanker prints (mid-to-late July)** when actual rate path provides empirical anchor for which methodology is closer to reality. If Q2 product TCEs land closer to VIE's implied path → our scenario forwards under-state the empirical environment and Product Set B should be revisited (Set C-leaning constructive). If Q2 lands closer to our scenario forwards → VIE's stance was overstated and our TRIM signals get retroactive validation. Either outcome is information; both are within the §13 weight-stability re-evaluation discipline.

#### Empirical test of hypothesis #2 — product-class transaction anchoring (added 2026-06-04 PM)

A 12-row 2026 product tanker transactions worksheet (Scorpio Tankers fleet-renewal disposals + d'Amico newbuild orders + Compass broker prints; archived at `inputs/market_data/transactions/raw/product_tanker_transactions_2026.xlsx`) was filed into the §9.9 transaction-anchor infrastructure as `mr.yaml` (2 in-window + 4 out-of-window documentation prints) and `lr2.yaml` (1 in-window print). The recalibration solver was re-run with `use_transaction_anchored=True` and the result tested against hypothesis #2 above ("our product vessel curves are too conservative vs current secondhand transactions").

**Solver fits:**

| Class | n in-window | 5yr Δ | 10yr Δ | Notes |
|---|--:|--:|--:|---|
| MR | 2 | +2.2% ($46.0M→$47.0M) | **+10.1%** ($34.5M→$38.0M) | clamped at 5yr; raw fit implied $53M, clamp band [scrap×1.5, NB×0.95] capped at $47.0M |
| LR2 (own fit) | 1 | — | — | **Fallback** (n<2 minimum); inherits Aframax proxy fit per §9.9 v1 proxy |
| LR2 (via Aframax) | 6 | −2.8% | **−12.8%** ($68.0M→$59.3M) | active fit — propagated from Aframax sample |
| Aframax | 6 | −2.8% | −12.8% | unchanged from prior |
| Suezmax | 5 | +9.2% | +1.3% | unchanged from prior |

**Per-name NAV impact (full curve-vs-transaction comparison at `outputs/transaction_anchor_comparison.md`):**

| Name | NAV Δ% | Driver |
|---|--:|---|
| ASC | **+8.6%** | pure-MR fleet — fully captures MR 10yr lift |
| HAFN | +2.6% | MR + LR1 lift dominates LR2-via-Aframax drop on whole-co NAV |
| INSW (whole-co) | +1.6% | MR fit applies to product carve-out sleeve |
| TRMD | +0.7% | MR / LR1 / LR2 exposure roughly offsets |
| STNG | −3.0% | LR2-dominated — Aframax-proxy drop outweighs MR lift |

**Reading the test:**

1. **MR side of hypothesis #2 is PARTIALLY VALIDATED.** The MR 10yr anchor lifts ~10% under transaction anchoring (extrapolation from the two age-11/12 STNG scrubber-MR prints sitting modestly above the existing curve). NAV impact on MR-heavy names is positive (ASC +8.6%, INSW +1.6%) — direction predicted by hypothesis #2.

2. **LR2 side of hypothesis #2 is FALSIFIED IN THE WRONG DIRECTION.** The one available age-10 LR2 print (STNG STI Goal/Gallantry @ $52.3M, closing Q1 2026) sits ~27% BELOW the active Aframax-proxy curve. With n=1 in-window the solver falls back and LR2 continues to inherit the Aframax fit, but the print itself empirically confirms the §3.1 v1 limitation ("LR2 modeled as Aframax-equivalent (crude/dirty proxy); v2: distinguish clean-LR2 product economics"). If/when LR2 transitions to a clean-product sub-curve, the move on LR2-heavy product names will run in the OPPOSITE direction to hypothesis #2.

3. **Net effect on the §11.5 divergence is real but modest.** ASC's tool→VIE gap closes by ~6.4pp on the EV axis; INSW, HAFN, TRMD by 1-3pp. STNG's gap WIDENS by 2.7pp (LR2 exposure outweighs MR). **The cross-methodology divergence is not closed by transaction anchoring**; it just shuffles per-name positions within the same TRIM cluster (no position-call flips).

**Updated implication:** the §11.5 divergence has now been formally tested. Hypothesis #2 is partially validated for MR but partially falsified for LR2, and the two effects offset on mixed-fleet names. Recalibration narrows the methodology gap on the order of ~2-9pp depending on class mix; it does not close it. Hypothesis #1 (VIE forward-curve TCE assumptions more constructive than even Set B v2) remains the dominant unexplained residual and is the likely structural driver. The Q2 2026 re-evaluation gate (above) becomes the next decision point — empirical rate path, not curve recalibration, will settle which methodology is closer to reality.

**Pending:** a clean-LR2 sub-curve (separate from the dirty-Aframax LR2 proxy) requires at least 2 in-window LR2 prints. The 2026 worksheet documents the first one; the second is the data dependency that gates an LR2 v2 curve change. Until then, LR2 continues to be valued via the Aframax-proxy fit and the methodology gap on LR2-heavy product names remains within the §11.5 documented divergence band.

#### Crude-class transaction anchoring — expanded sample (added 2026-06-04 evening)

The 2026 transactions worksheet was extended with a "Crude Tanker Deals" sheet (14 rows: VLCC + Suezmax + Aframax). The §9.9 infrastructure was expanded with a new **`vlcc.yaml`** (5 in-window single-vessel prints + Sinokor campaign and FRO related-party NB as out-of-fit documentation), and the existing **`suezmax.yaml`** + **`aframax.yaml`** were extended with new named-vessel prints. The fit was re-run and produces a separate and structurally different read from the product side above:

| Class | n in-window | 5yr Δ | 10yr Δ | Note |
|---|--:|--:|--:|---|
| **VLCC** (NEW) | 5 | **−15.6%** ($138M→$117M) | **−13.1%** ($111M→$96M) | Cooler-than-Aframax 2026 transaction reality; curve substantially HIGH at modern end. Sinokor +10-15% premium campaign documented but out-of-fit |
| Suezmax (extended) | 6 | +8.3% | +0.1% | FRO Front Ull/Idun (age 11.5, $70M, FRO Q2 ER) named-deal CONFIRMS the prior chatter-only mid-age level |
| Aframax (extended) | 7 | +1.4% | −9.1% (was −12.8%) | STI Condotti (age 11, $70M, eco scrubber, Aframax-trading-mode LR2) lifts the right-edge slightly |
| LR2 (via Aframax) | 7 | +1.4% | −9.1% (was −12.8%) | propagated — mid-age drop softens to −9.1% |
| MR | 2 | +2.2% | +10.1% | unchanged from PM run |

**Per-name NAV impact (vs the prior PM run):**

| Name | NAV Δ% | vs PM | Driver |
|---|--:|--:|---|
| ASC | +8.6% | unchanged | pure-MR — no crude exposure |
| TRMD | +2.7% | +2.0pp | **POSITION FLIPS TRIM → HOLD ⚠️** |
| HAFN | +3.5% | +0.9pp | MR + LR1 + softened LR2 drop |
| NAT | +0.4% | −1.7pp | Suezmax fit unchanged; tiny adjustment |
| TNK | −3.0% | unchanged | Aframax + Suezmax exposure |
| STNG | −1.0% | +2.0pp | softened LR2-via-Aframax drop |
| INSW (whole-co) | **−2.0%** | **−3.6pp** | VLCC drop on crude sleeve now dominates MR lift on product sleeve |
| FRO | **−8.9%** | −8.6pp | Suezmax + Aframax + LR2-proxy drop, no VLCC offset (FRO exited VLCC in Q1 disposal) |
| ECO | **−8.6%** | **−10.3pp** | VLCC + Suezmax — VLCC drop now dominates Suezmax lift |
| DHT | **−11.5%** | **−11.5pp** | pure-VLCC — fully captures the VLCC fit |

**Reading the crude expansion:**

1. **The VLCC curve was materially overstated at the modern end.** 5yr −15.6% / 10yr −13.1% is a substantial directional move — comparable to the Aframax fit's original size. The transaction sample is anchored on five named arm's-length 2026 deals (Frontline 8-vessel disposal + CMB.TECH 2-vessel + Teekay VLCC exit + CSSC Liaoning + Hyundai Samho chatter). All five prints sit below the existing broker-resale curve at their respective ages. The Sinokor +10-15% premium buying campaign (~$2.5bn aggregate, ~35 vessels) is documented as out-of-fit because a single weighted aggregate point would dominate the regression and overstate the opportunistic premium as a universal market level. **The §9.9 item-9 paragraph claim that "VLCC is validated separately by pure-play P/NAV reconciliation (DHT within ~1% of consensus) and the TNK Q2 2026 VLCC disposal (2013-built $84.5M ≈ curve)" was overstated** — the TNK $84.5M print actually sits 9% below the existing curve at age 13, and the broader sample confirms a systematic 10-15% high bias at the modern end. The DHT-pricing-≈-broker-consensus argument validated that BROKER NAV and TOOL NAV roughly agree on DHT — not that either is correct vs transaction reality.

2. **The Suezmax curve is reconfirmed.** The FRO Front Ull/Idun named print at age 11.5 / $70M lands ~$3M below the prior age-12 chatter ($73M) — well within noise. Suezmax fit unchanged at +0.1% at 10yr.

3. **The Aframax curve fit softens slightly.** The STI Condotti age-11 print at $70M (eco scrubber LR2 trading dirty) lifts the right-edge of the Aframax window enough to take the 10yr drop from −12.8% to −9.1%. This propagates to LR2-via-Aframax. The empirical observation is also interesting: STI Condotti at $70M (dirty-mode LR2) vs STI Goal/Gallantry at $52.3M (clean-mode LR2) is a 33% spread between same-class same-vintage same-spec hulls sold by the same seller within 4 months — direct evidence for the §14.6.1 LR2 cargo-switching value bifurcation.

4. **One position flip: TRMD TRIM → HOLD.** TRMD's pre-transaction EV was −6.1% (right at the TRIM/HOLD threshold). The post-transaction EV of −3.7% crosses into the HOLD band. The flip is genuinely informative — it moves TRMD CLOSER to VIE Bullish (one more step in the directional narrowing on product names per the PM §11.5 hypothesis-#2 test) — but it sits on a thin margin and could revert with a single TCE-deck update. **Position-sizing implication for TRMD specifically: the TRIM signal was always low-conviction (Δ vs HOLD threshold = 1.1pp pre-tx; 1.3pp post-tx in the OPPOSITE direction); decisions on TRMD should treat the tool call as agnostic on the TRIM/HOLD axis and rely on §9.10 weight robustness + §11.5 cross-methodology framing.**

5. **Crude-side TRIM signals on DHT / ECO / FRO get DEEPER, not narrower.** This is the inverse of the product-side narrowing observed in the PM test. The crude TRIM cluster widens its EV gap by 5-11pp under transaction anchoring (DHT EV −18.7% → −26.9%; ECO −32.4% → −37.7%; FRO −30.8% → −37.0%). **The framework's existing crude TRIMs get retroactive validation from transaction data — the curves were running too generous, and correcting that strengthens the existing call.** This is the OPPOSITE of the product-side §11.5 picture (where transaction anchoring narrows but doesn't close the divergence with VIE Bullish). The two sectors are moving in opposite directions under empirical anchoring.

**Cross-sector pattern (added discipline):** transaction anchoring on crude classes (VLCC + Suezmax + Aframax) MOSTLY DEEPENS existing TRIM signals (curves were generous); transaction anchoring on product classes (MR + LR2-via-Aframax) MOSTLY NARROWS existing TRIM signals on mixed-fleet names (curves had a mix of conservative and generous regions). This sector-asymmetric response is itself a useful read on the cycle position — the crude market's modern second-hand mid-age values have softened more than our resale-anchor curves capture, while the product mid-age MR market has held up better than our curve assumed. Consistent with the broader "crude leading the rate normalization; product holding firmer" narrative across §11.5 and §6.

**Open methodology decision (deferred):** whether to ship the transaction-anchored fit as the production default rather than an opt-in toggle. The PM test framing left this as "opt-in diagnostic" because the LR2 falsification meant the fit was directionally mixed for product names. With the crude expansion the fit is now directionally consistent on crude (deeper TRIM) and consistent-but-modest on product (slight narrowing). **Deferred decision** until at least one more LR2 print clears the fallback guard and a clean-LR2 sub-curve can be considered. Until then, transaction-anchored remains opt-in; reports rendered under the toggle are diagnostic, not production.

#### VIE NAV cross-reference — hypothesis #2 confirmed by two agreeing sources (added 2026-06-04 PM)

A NAV-layer cross-reference of all 12 watchlist names against VIE's published
NAV/sh, bridged by broker-consensus NAV (price ÷ Pareto P/NAV), was built at
`outputs/vie_nav_xref.md`. It bears directly on hypothesis #2 ("our product
vessel curves are conservative vs current market").

**First, a data correction.** The exercise surfaced two stale APPROX
`consensus_pnav` inputs: STNG (0.87) and TRMD (1.00). The Pareto Shipping Daily
of 4 Jun 2026 publishes real P/NAVs of **STNG 0.70** and **TRMD 0.83**.
Correcting them raised broker NAV (STNG $90.80 → $108.00; TRMD $27.25 → $33.98)
and widened the tool→broker EV spread (STNG +8pp → **+27pp**; TRMD +2pp →
**+22pp**). **STNG and TRMD reclassify mark-validated → mark-driven.** STNG had
been a cited mark-validated validator; that framing is retired (LIMITATIONS §1,
§4 corrected; `vie_coverage_universe_xref.md` STNG row updated). Pareto publishes
no P/NAV for NAT / ASC / CCEC — those stay unanchored APPROX.

**The finding.** With corrected P/NAVs, **VIE NAV ≈ broker-consensus NAV across
all 12 names** (VIE/broker in a 0.86–1.07 band, VIE running at-or-slightly-below
broker). VIE is not an independent third mark — it is a second read on broker
consensus. So the tool-vs-VIE NAV gap is **entirely the §9.9 mark-driven spread
re-expressed.** (An earlier draft claimed "VIE marks product above even broker";
that was the artifact of the stale APPROX P/NAVs and has been withdrawn.)

**Why this strengthens hypothesis #2.** On product, **two independent sources now
agree** that asset values sit well above our curves — Pareto broker and VIE,
which agree with each other:

| Name | Tool NAV | Broker NAV (Pareto) | VIE NAV | Tool below both by |
|---|--:|--:|--:|--:|
| STNG | $83.76 | $108.00 | $103.62 | ~24–29% |
| TRMD | $26.74 | $33.98 | $30.83 | ~15–27% |
| HAFN | $5.30 | $8.11 | $8.55 | ~53–61% |

Two converging independent marks above our curve is materially stronger evidence
than a single source. **The product curve level is conservative** — confirmed.

**Reconciliation with the LR2 transaction print (unchanged).** The clean-LR2
print (STI Goal/Gallantry $52.3M) sits 27% *below* our Aframax-proxy — the
opposite direction. The full STNG LR2 mark stack is `transaction $52.3M < tool
$71.4M < broker/VIE ~$78–88M`. This is the **§14.6.1 LR2 cargo-switching
option**: broker + VIE mark the coated LR2 at its dirty-Aframax-optionality
value; the clean-only buyer paid only the clean-product value (directly
evidenced by STI Condotti dirty-mode $70M vs STI Goal/Gallantry clean-mode
$52.3M). Both are right conditional on whether the marginal buyer values the
switch option. **The product NAV gap = VIE and broker price the LR2 option; our
curve (and a clean-only buyer) do not.** No curve recalibration is implied.

**Net for §11.5.** The product divergence decomposes across three diagnostic
layers: position (`vie_coverage_universe_xref.md`), forward-rate
(`vie_market_rates_xref.md`, hypothesis #1), and now NAV (this finding,
hypothesis #2 = the §14.6.1 LR2 option). Hypothesis #2 is **confirmed and
bounded** (it is the cargo-switching option value, ~25-50% on LR2-heavy names);
hypothesis #1 (VIE forward TCEs more constructive) remains the larger
unresolved residual, to be tested at the Q2 2026 product-print re-evaluation gate.

#### Clean-product Handysize class added (2026-06-05) — partial retirement of the off-curve gap

A **Handysize class** (~37-40k DWT clean-product) was added to
`vessel_value_curves.yaml` (NB $40M / 5yr $34M / 10yr $26M / scrap $4.5M;
eco-inclusive, premiums 0 — same convention as MR/LR1). Going deep into the
hulls showed the old blanket "no Handysize class" gap was really **three
distinct problems wearing one label**, and the build addresses only the first:

1. **Clean-product Handysize (~37-40k)** — *now on-curve.* HAFN's 22 (winding-
   down cohort, modelled age 18 ⇒ ~$14.5M/vessel via the curve) and ASC's 2
   Korea-built 37k product Handies (Defender/Dauntless, age 11 ⇒ ~$24.6M)
   moved from `working_capital_net` onto their fleet manifests. NAV effect is
   small and as-forecast: HAFN +$0.04/sh (the move drops the prior 10% wind-down
   liquidity haircut — the framework has no on-curve liquidity-discount
   mechanism, documented), ASC +$0.18/sh. **No position flips** (both stay
   TRIM/SHORT). 38 hulls total were eligible; HAFN 22 + ASC 2 = 24 moved.
2. **Chemical Handymax (38k IMO-II coated) — now on-curve (2026-06-05 PM).**
   STNG's 14 IMO-II chemical Handymax (~38k DWT Hyundai Mipo 2008-2014 builds)
   migrated to a dedicated **Handymax class** anchored on STNG's own disclosed
   marks ($14.3M/vessel at avg-age 15). Curve: NB $45M / 5yr $32M / 10yr $20M /
   scrap_25 $4M — distinct from clean-product Handysize ($40 / $34 / $26 / $4.5),
   reflecting the chemical discount that lives **on the value side**, not rates.
   Rate side empirically validated: STNG's Q1+Q2 2026 disclosed Handymax pool/
   spot rates ($34k Q1, $32k Q2) ran ≈ MR rates ($32k Q1, $36.5k Q2) — so the
   Handymax class routes to the `mr` rate key in `PRODUCT_SCENARIO_CLASS_MAP`
   (same proxy pattern as Handysize → mr). On-curve total $205M reproduces the
   prior `working_capital_net` $200M within $5M; net NAV +$0.10/sh on STNG.
   Subsection below documents the full curve construction. ASC's 4 × 25k
   stainless chemical hulls remain OFF-curve (different sub-class — see below).
3. **Sub-25k stainless chemical Handy — deliberately left OFF-curve.** ASC's
   4 × 25k stainless chemical hulls (Chippewa/Chinook/Cheyenne/Cherokee, Japan-
   built 2015) trade in a structurally smaller specialty-chemical pool than the
   38k IMO-II coated curve covers. Valuing them on the new Handymax curve at
   age 11 (~$28M) would overvalue them vs the ASC-disclosed ~$13M/vessel
   estimate (a ~$60M aggregate overvaluation). They remain in
   `working_capital_net`, now re-scoped as the narrower **"sub-25k stainless
   chemical Handy"** residual tied to the chemical-sector gap (LIMITATIONS §2).
4. **Wind-down/liquidity discounting** — HAFN's sleeve carried a deliberate 10%
   wind-down haircut the framework can't represent on-curve. Moving HAFN's Handies
   on-curve drops it (+$0.04/sh, flagged). A general on-curve liquidity-overlay
   mechanism remains unbuilt (minor; bounded).

**Earnings routing (v1):** Handysize and Handymax earnings both proxy to the
MR scenario key and MR-level rate inputs (ffa / spot / 12M TC / 10y mean) —
their cycle positions therefore equal MR's. For Handysize, the per-day earnings
are mildly overstated vs a true ~0.8× Handysize rate, but the sleeve is small
and down-weighted at peak (immaterial, ~$0.04/sh on HAFN). For Handymax, the
proxy is **empirically validated** by STNG's Q1+Q2 2026 disclosed Handymax
pool/spot rates running ≈ MR (slight Handymax premium in Q1, slight discount
in Q2). In both cases the **NAV value curve is the real differentiator** and is
done properly. Mirrors the LR1→lr2_clean proxy precedent. A dedicated
`handysize` scenario block at ~0.8× MR is the v2 refinement if that sleeve
grows; Handymax can stay on the validated MR proxy until evidence of rate
divergence emerges.

#### Chemical Handymax (38k IMO-II coated) class added (2026-06-05 PM) — narrowed off-curve gap

A **Handymax class** (38k DWT IMO-II coated chemical-capable) was added to
`vessel_value_curves.yaml` (NB $45M / 5yr $32M / 10yr $20M / scrap_25 $4M;
eco-inclusive, premiums 0). Distinct from the clean-product Handysize curve
($40 / $34 / $26 / $4.5) — steeper depreciation reflects the narrower second-
hand market for IMO-II coated hulls. **STNG's 14 Handymax (Hyundai Mipo 2008-
2014, ages 12-18) migrated on-curve**; STNG `working_capital_net` $802.8M →
$602.8M, on-curve fleet +$205M (vs prior $200M estimate), net NAV +$0.10/sh.

**Anchoring logic.** The curve is anchored on STNG's disclosed $14.3M/vessel
mark at the cohort's average age 15. With the piecewise-linear interpolation
between 10yr ($20M) and scrap_25 ($4M), age 15 reproduces $14.67M (within $0.4M
of the disclosed anchor) — a single hard anchor at the cohort's centroid plus
a defensible NB and 5yr inferred from rate-parity-with-MR ($45M, $32M) and
scrap conventions. APPROX-flagged in the curve YAML: mid-age 5yr and 10yr
anchors derived from a single class-average; refresh when a disclosed chemical
Handymax transaction print clears the transaction-anchored fallback guard.

**Rate routing — empirically validated MR proxy.** Chemical Handymax routes
to the `mr` rate key in `PRODUCT_SCENARIO_CLASS_MAP`. STNG IR 25-Mar-2026
disclosed Q1+Q2 2026 Handymax pool/spot rates of $34k / $32k vs MR's $32k /
$36.5k — slight Handymax premium in Q1, slight discount in Q2; rate parity
within 7%. The "chemical discount" lives on the value side, not the rate side,
so MR forwards × 1.0 is a defensible proxy. A dedicated chemical-Handymax FFA
block becomes the v2 refinement only if rate divergence emerges in later
quarterly prints.

**What this does NOT cover.** Three sub-classes deliberately excluded from
the Handymax curve scope:
- **Stainless steel chemical Handymax (~40k)** — Odfjell's 2027-29 NB order
  at ~$72.5M/vessel (Kitanihon Japan; $290M total for 4 hulls) and NYK-Stolt's
  6 × 38k stainless at Nantong Xiangyu anchor a structurally higher curve.
  No watchlist name has this exposure; deferred until one does.
- **Sub-25k stainless chemical Handy** — ASC's 4 × 25k Japan-built 2015 hulls
  (Chippewa/Chinook/Cheyenne/Cherokee). Specialty-chemical trade pool;
  remains in `working_capital_net` per the §11.5 sub-25k stainless residual.
- **Pure-chemical parcel operators** (Stolt-Nielsen / Odfjell) — un-onboardable
  until a stainless-Handymax curve + chemical-specific rate economics land.

### 11.6 DP2 shuttle / contract-anchored sleeve convention (added 2026-06-05 PM)

**Motivating case: TEN (Tsakos).** TEN's NAV is dominated by ~14 DP2 shuttle
tankers (4 in-water + 10 NBs on order through 2028) that operate on long-
dated contracts with offshore charterers (Petrobras, etc.). These vessels:
- Have no observable spot market — they earn contracted bareboat / TC rates
  for 5-15 year terms, not BDTI-comparable day rates.
- Have no public second-hand transaction flow — no anchor to fit a value
  curve. The closest comparable would be a same-DWT Suezmax, but DP2
  carries a large specialised-equipment premium that varies by trade route
  and charterer demand.
- Have no orderbook FFA — no forward curve to drive a dividend-strip
  scenario.

Building a full `Shuttle` vessel class with its own value curve, scenario
forwards, and rate-key plumbing would require methodology calls in three
places where we have no defensible empirical anchor. **The framework instead
adopts an off-curve-at-contracted-book convention** that uses the disclosed
contracted cash flows as the empirical anchor and leaves the §3.1 value
curve / §3.2 dividend strip machinery out of the shuttle sleeve entirely.

#### In-water shuttle sleeve — NPV of contracted cash flows

For each in-water shuttle vessel, compute the present value of contracted
cash flows over the disclosed charter term, plus a residual at expiry:

> **value_per_vessel** = Σ<sub>t=1..T</sub> [day_rate(t) × 365 × utilization × (1 − offhire) − opex(t)] / (1 + WACC)<sup>t/4</sup>
> &nbsp;&nbsp; + **residual at expiry / (1 + WACC)<sup>T/4</sup>**
>
> where **residual at expiry** = Suezmax value curve at *age-at-expiry* —
> the conventional-Suezmax disposal value the vessel would command if
> repurposed at TC expiry. **Mid-conservative** — ignores DP2-spec premium
> but doesn't zero the vessel out.

Inputs per vessel: disclosed TC rate (with escalation clauses), charter
expiry date, vessel age at expiry, utilization (fleet-wide proxy; TEN runs
~98%), offhire rate (default 1%). WACC = the framework's 11% discount rate
(§3.2), consistent with the dividend strip.

The per-vessel NPVs sum into the **`shuttle_contracted_book`** line on the
balance sheet (METHODOLOGY §4.2). NAV adds the figure to balance-sheet net
(like working_capital_net) — it is an asset, not a claim.

#### Newbuild shuttle sleeve — delivered-at-contract-price

For NB shuttle vessels (TEN: Anfield + 9 HN2733-2741 hulls, 15-year bareboat
upon delivery), the §3.1 newbuild-at-market convention does NOT apply — the
"delivered market value" of a DP2 shuttle has no observable benchmark, so
the "delivered market less remaining commitment" formula would lean on a
fabricated mark. **Instead, treat NB shuttle as delivered-at-contract-
price:** the delivered value = the contract price, and the embedded value
of the bareboat charter is reflected only at delivery (when the vessel
enters service and the contracted cash flow stream begins).

In schema terms, this means the contract price flows through the existing
`newbuild_capex_commitments` line at face — no §3.1 hot-market markup, no
embedded delivered-NB-value-less-commitments premium. Conservative; mirrors
the working_capital_net-at-agreed-price convention for HFS vessels (DHT
Bauhinia, STNG's 9 HFS hulls).

#### Three-sleeve architecture

A name like TEN combines four asset types:
- Crude tankers (VLCC + Suezmax + Aframax)
- Product tankers (Aframax LR + Panamax LR1 + MR + Handysize)
- LNG carriers (Tenergy + Maria Energy)
- DP2 shuttle tankers (off-curve via `shuttle_contracted_book`)

The 3-sleeve carve-out (`carveout.py`: `crude_carve_out` +
`product_carve_out` + `lng_carve_out`) handles the first three; the shuttle
sleeve sits at the corporate level via `shuttle_contracted_book`. Sleeve
shares sum across the WHOLE-COMPANY denominator (crude_value + product_value
+ lng_value); pipeline `_aggregate_three_sleeve_report` pairs scenarios by
index across the three sectors.

For pipeline dispatch, names with this shape go in `THREE_SLEEVE_TICKERS`
(parallel to `HYBRID_TICKERS` for 2-sleeve names like INSW).

#### What this convention does NOT cover

- **FPSOs, drilling rigs, offshore platform support vessels** — different
  asset class entirely; out of scope.
- **Spot-traded shuttle tankers** (if any emerge) — would need a Shuttle
  value curve, which this convention deliberately avoids building.
- **Contracted-rate vessels in conventional fleets** (e.g. a Suezmax on a
  5-year TC) — these stay on-curve via the standard NAV machinery. The
  off-curve convention applies only when (a) the vessel class has no
  defensible curve, AND (b) the cash flows are contractually visible.

#### Refresh discipline

The `shuttle_contracted_book` figure is **point-in-time at the quarterly
balance sheet date**. Each quarter:
1. Re-confirm charter expiry dates and rate escalation clauses.
2. Recompute per-vessel NPVs with the new horizon (one quarter shorter).
3. If a new contract or extension is announced, update the underlying
   per-vessel basis; the figure should track contracted-book reality, not
   stale estimates.

A future v2 could refine: charter renewal probability at expiry (treat as a
discount on the Suezmax residual rather than full step-down), DP2-spec
premium amortisation curve, or a full Shuttle value class once enough
disposal data emerges. For v1 the simple convention is the honest call.

### 11.7 Dry bulk sector — formalised 2026-06-09

First fully greenfield sector after the v1 crude / LNG / product builds.
Dry bulk shipping moves the largest cargoes by tonne-mile — iron ore, coal,
grain, and the catch-all "minor bulks" (bauxite, fertilisers, scrap metal,
cement clinker). The freight cycle is China-dominated on the demand side
(China imports ~70% of seaborne iron ore and ~30% of coal) and orderbook-
sensitive on the supply side. The methodology lifts cleanly into the
NAV + dividend-strip + cycle-blend skeleton; this section locks the
sector-specific decisions for v1.

#### 11.7.1 Vessel classes

| Class | DWT range | Primary cargo | Pareto rate published? |
|---|---|---|---|
| Capesize | ~180k+ | Iron ore (60%+), coal | ✓ as "Capesize USD/day" |
| Panamax | ~75-85k | Coal, grain, minor bulk | ✓ as "Panamax" |
| Supra-Ultra (combined) | ~55-65k | Minor bulk, cabotage | ✓ as "Ultramax" (was "Supramax" pre-Sep-2025) |

**Supra-Ultra is a deliberate v1 collapse.** Pareto's Shipping Daily
reclassified the smaller-bulker benchmark from Supramax to Ultramax in
September 2025 — the same chartering desk continues to quote a single
sub-Panamax rate, just under a more modern label. We treat them as one
class in v1 (`bulk_supra_ultra`); the source label is preserved per-report
as a transparency tag for downstream analysis. The Pareto class evolution
independently validates the methodology decision.

**Omitted from v1:**
- **Handysize bulk (~38k DWT)** — Pareto does not separately rate it
  (thin liquidity, less-traded second-hand market). Mirrors VIE's class
  scope.
- **Newcastlemax (~200k+ DWT)** — collapsed into Capesize. Real chartering
  treats them as one segment for spot rates with a modest premium.

#### 11.7.2 External NAV anchor — Pareto coverage

Pareto Shipping Daily publishes P/NAV and 1Y FWD P/E for **three dry-bulk
pure-plays**: SBLK (Star Bulk), GNK (Genco Shipping), HSHP (Himalaya
Shipping). The watchlist tickers without Pareto coverage (CMDB, PANL, SB,
DSX, EDRY, SHIP) carry `APPROX` consensus_pnav values per the existing
APPROX convention (METHODOLOGY §6 NAT/ASC/CCEC/TEN precedent;
`/reconcile` treats them as `n/a` for SANITY rather than failing against
a placeholder anchor).

**Complementary cycle indicator:** the `baltic_indexes_daily.csv` feed
(per `inputs/rocketchat_sources.yaml`) carries published Baltic Exchange
index values — BDI composite, BCI / BPI / BSI sub-indices, capesize_index
— at index units rather than $/day. These are NOT used as cycle anchors
(anchor methodology is $/day-denominated per §10) but feed cycle-position
diagnostics and serve as a primary-source cross-check on Pareto's reported
bulk rates.

#### 11.7.3 Validator pool (v1)

Three names, mirroring the existing-sector pattern (single methodology
validator + a peer for v1 calibration):

- **SBLK** (Star Bulk) — Pareto P/NAV-anchored, multi-class fleet
  (Capesize + Ultramax), largest pure-play with deep analyst coverage.
  Stress-tests the multi-class machinery.
- **GNK** (Genco Shipping) — Pareto P/NAV-anchored, also Cape + Ultra,
  clean structure. The two-Pareto-anchored sample lets the v1 calibration
  lock test (§11.7.6) report against a real bar.
- **CMDB** (Costamare Bulkers) — APPROX-anchored (no Pareto), the
  originally-stated interest. CMRE spinoff with potential intercompany
  contract structure to monitor; reconciles via the APPROX path.

#### 11.7.4 Scenarios — Bulk Set A (locked 2026-06-09)

Four scenarios, weights mirror the four-scenario crude structure. Macro
drivers are China-iron-ore-dominated for Cape, more diversified for
Pana/Supra-Ultra:

| Scenario | Probability | Cape | Pana | Supra-Ultra | Macro driver |
|---|:---:|:---:|:---:|:---:|---|
| `china_acceleration` | **0.20** | tight | tight | firm | China steel demand re-accelerates; iron ore imports >110 mt/mo |
| `moderate_growth` (base) | **0.40** | base | base | base | Current trajectory: ~100 mt/mo iron ore, modest grain growth |
| `china_property_drag` | **0.25** | weak | base | base | China property/steel weakness; Pana/Supra insulated by grain + minor bulk |
| `coordinated_slowdown` | **0.15** | weak | weak | weak | Global recession; broad freight demand contraction |

**Weight rationale.** `moderate_growth` as base reflects the current
firm-but-not-extreme rate environment (Cape ~$44k, Pana ~$20k, Supra-Ultra
~$20k as of Jun 2026). `china_property_drag` gets the largest downside
weight (25%) because it is bulk-specific, observable through China iron
ore import data, and the most documented soft spot in 2025-26 commentary.
`coordinated_slowdown` is the global tail. `china_acceleration` is
meaningful upside given the orderbook is low (post-2015 trauma) plus iron
ore inventory dynamics.

**Per-class rate paths** (8-quarter strip horizons) are wired in Week 2
when `inputs/scenario_inputs.yaml` gets the `sectors.dry_bulk` block.
The v1 forward-curve approach inherits the synthesised-from-spot
convention used in tanker sectors; OCR'd FFA grids from Joeri's
`inputs/joeri_clipboard/` PNGs are deferred to §11.7 v2 (see task #3 in
this session's task log).

#### 11.7.5 Cycle anchors — v1 empirical from Pareto archive

Cycle anchors per METHODOLOGY §10 are TC-anchored 10-year means. For dry
bulk v1 we have a **22-month Pareto archive** (Aug 2024 → Jun 2026), not
a 10-year series. The v1 anchors are the **median** of daily Pareto-
reported $/day rates over the archive — median rather than mean for
robustness to PDF parse-error tails (a handful of dates have rate
extractions that survive plausibility filtering but inflate the right
tail; medians are unaffected). Refine in Q3 when longer history or a
paid Clarksons/Howe Robinson series is available.

| Class | v1 cycle anchor (USD/day) | n obs | Date range |
|---|---:|---:|---|
| Capesize | **$23,650** | 349 | 2024-08-22 → 2026-06-08 |
| Panamax | **$11,900** | 349 | same |
| Supra-Ultra | **$13,930** | 349 | same |

Per-quarter empirical means (cycle shape, for §11.7.4 scenario tuning):

| Period | Cape | Pana | Supra-Ultra | n |
|---|---:|---:|---:|---:|
| 2024-Q3 | $26,254 | $11,378 | $14,241 | 23 |
| 2024-Q4 | $24,154 | $9,351 | $11,958 | 48 |
| 2025-Q1 | $30,779 | $13,685 | $9,490 | 57 |
| 2025-Q2 | $35,305 | $10,513 | $12,155 | 49 |
| 2025-Q3 | $25,960 | $14,450 | $17,636 | 35 |
| 2025-Q4 | $42,885 | $14,995 | $17,639 | 47 |
| 2026-Q1 | $35,980 | $13,824 | $14,433 | 55 |
| 2026-Q2 (PD) | $37,230 | $18,277 | $18,716 | 37 |

Cycle position at archive end (2026-06-08): Cape 1.73× anchor, Pana
1.69×, Supra-Ultra 1.44× — the dry bulk market is in a structurally firm
environment, comparable to the post-MoU crude tanker setup but anchored
on Chinese steel demand rather than ton-mile redirection.

**Methodology caveat (locked in writing here):** the empirical anchor is
biased ELEVATED by the 22-month sample (which sits in a relatively strong
dry bulk environment vs the 2015-2020 trough). A true 10-year TC-anchored
mean is likely lower — perhaps $18-20k for Cape, $9-11k for Pana,
$10-12k for Supra-Ultra. The current anchors will read as biased toward
"current is cycle position 1.0×" rather than "current is peak". Acceptable
for v1; flag during Q3 refresh if positioning calls feel off.

##### FFA cross-check discipline (added 2026-06-09)

Dry bulk has a **liquid FFA forward curve** (Cape / Pmax / Smax quoted out
to Cal+3) that crude / product / LNG do not. This is a meaningful gift —
the FFA represents the market's probability-weighted expectation of forward
TCEs, which is exactly the quantity our scenario set is supposed to
produce (PW = `weight × forward` summed across scenarios). Use FFA as the
v1 calibration check on scenario mids.

**Calibration check applied 2026-06-09 (initial Bulk Set A mids):**
- Joeri's FFA grid (Jun 9 2026) revealed my initial Cape mids ran ~+20%
  above the FFA forward; Pana was effectively perfect; Supra-Ultra was
  close on front quarters but ~+20% high in Cal27.
- v2 mids (this section's locked values) bring PW vs FFA gaps to:
  Cape Q3-2026 +6.3%, Q4-2026 +1%, Cal27 +5%;
  Pana effectively exact at Cal27 (+2%);
  Supra-Ultra Q3-2026 −4%, Q4-2026 +2%, Cal27 within band.

**Refresh discipline:** at each quarterly refresh, re-compute the PW
forward implied by `sectors.dry_bulk.scenarios` and compare against the
current FFA grid. Material drift (>10% on Cape front-quarter, >15% on
Cal27, or Pana Cal27 outside ±5%) triggers a scenarios-block update.

**Source for forward FFA going forward:** Joeri's daily Cape/Pmax/Smax
clipboard PNGs (`inputs/joeri_clipboard/`) — captured most weekdays via
the Rocket.Chat ingest. OCR pipeline is task #3 in the session log
(deferred to §11.7 v2); until then, eyeball-check at refresh time.

#### 11.7.6 v1 calibration lock target

Per the new-sector bar (CLAUDE.md "Reconciliation has three jobs"):
**≥70% of Pareto-anchored validators within ±10% of broker NAV at v1
ship**. With SBLK + GNK as the two Pareto-anchored names, the bar is
2/2 (100%) or 1/2 (50%) — a binary outcome at this sample size. The
calibration-lock test runs once at sector ship:

```
PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.reconcile \
    --calibration-lock dry_bulk
```

A FAIL signals methodology calibration is off — likely the cycle anchors
(too high, biasing tool NAVs above broker consensus) or the class map
(if Pana is being routed through Cape rates by accident).

#### 11.7.7 What is NOT in v1

- **Handysize bulk class** — added if a Pareto-covered Handy pure-play
  appears on the watchlist, or if Joeri OCR yields a Handy FFA series.
- **Newcastlemax sub-class** — collapsed into Cape; could split later
  with disposal evidence.
- **Transaction-anchored recalibration** (METHODOLOGY §9.9 scope
  discipline) — no comparable transaction sample for bulk classes.
  Do NOT add without an analogous disclosed-deals dataset.
- **Per-class scrubber premium** — Pareto's bulk table does not separate
  scrubber from non-scrubber rates the way the tanker table does.
- **OCR-derived FFA forward curve** — Joeri's clipboard PNGs include
  clean Cape/Pmax/Smax FFA grids (~12-25% of his images) but require
  classifier + OCR work to harvest. Deferred to §11.7 v2; trigger is
  §9.11 EPS-xref signalling that the synthesised-curve bulk strip is
  unreliable vs consensus.

#### 11.7.8 Onboarding sequence

| Step | When | Owner |
|---|---|---|
| §11.7 methodology decision doc (this section) | DONE 2026-06-09 | methodology |
| `inputs/scenario_inputs.yaml` sectors.dry_bulk block + class map + cycle anchors YAML | Week 2 Day 1 | code |
| `pipeline._load_all_sectors` includes dry_bulk; `SCENARIO_CLASS_MAP_BY_SECTOR` updates | Week 2 Day 1 | code |
| CMDB + SBLK + GNK YAMLs scaffolded via `/add-ticker` | Week 2 Day 2 | data |
| Data assembly from Q1 2026 results | Week 2 Day 2-4 | data |
| `/reconcile --calibration-lock dry_bulk` test | Week 2 end | gate |
| §11.7 v2 (OCR FFA, longer history): | Q3 if triggered | — |

## 12. Framework limitation — high-payout pure-plays at cycle peak

The NAV + dividend-strip framework **systematically undervalues high-payout single-asset-class equities during cycle peaks**. This is a structural feature of the model, not a calibration error. It is documented here as a named constraint so that outputs for the affected names are read correctly.

### 12.1 Mechanism

- At ~100% payout and peak-cycle conditions the model returns **FV ≈ NAV** (the peak `w_nav` weighting times NAV, plus a small contribution from the dividend strip which itself ≈ NAV + near-term DPS PV).
- Each quarter of dividend payment is treated by the model as **value extraction** — the terminal NAV at quarter 9 is depleted by the dividends paid out — rather than as the investment thesis.
- Market participants in these names are pricing the **near-term dividend stream as the dominant value driver**: a high-payout pure-play at cycle peak is held for the next ~6-12 quarters of large dividends, not for terminal NAV.
- The result is market P/NAV multiples well above 1.0× during peak conditions, with the model reading those as "rich" and producing TRIM signals that are mathematically internally consistent but commercially misaligned.

The model does not model **finite-duration dividend extraction as a discrete value claim** — only as a periodic decrement of terminal NAV. Closing that gap would require a separate cycle-aware dividend-window model layered on top of the current strip, which is out of scope for v1.

### 12.2 Names exhibiting this pattern

- **NAT** (Suezmax tankers) — current peak; tool P/NAV ≈ 2.0× during 2026-Q2 spot strength
- **SBLK** (peak dry bulk)
- **DLNG** (peak VLGC)
- **HSHP**
- Any single-asset-class structure with sustained payout ratio > 90% during a cycle peak

### 12.3 Recommended usage for affected names

- Treat the model's FV as a **NAV floor**, not a market-fair-value estimate.
- Apply a **qualitative dividend-stream overlay separately** — e.g. 4-8 quarters of projected DPS at the current rate environment, discounted, vs current price — and form the call from the two views together.
- **Do not act on the model's TRIM signal** for these names without explicitly framing the dividend extraction window.
- For NAT specifically: the Suezmax curve has been transaction-anchored and validated against the TNK $53.5M disposal with a +0.6% residual (§9.9). The residual gap between tool FV and market price is **not** closeable by further curve work and should not be presented as a calibration weakness.

### 12.4 What this is not

This is not a "we'll fix it later" caveat. The NAV + cycle-blended strip framework's interpretability across the wider 6-name crude-tanker watchlist + FLNG depends on **not** fitting around the NAT-style edge case (adding a "dividend window" term would silently change every name's FV). Documenting the limitation here, and excluding affected names from the framework's TRIM/HOLD/BUY signal, preserves the model's integrity for the names it is designed to value.

## 13. Framework limitation — scenario-weight stability under infrastructure shocks

The scenario weights locked in any sector (§11.3 for LNG; the crude weights inherited from v1; the product weights inherited from LNG-like for `sectors.product`) are **conditional on the observable supply regime at the time of the lock**. A major infrastructure event — a multi-train LNG facility coming back online, sustained Hormuz disruption, a sanctioned-flow re-routing, a new LNG basin entering meaningful operations — can change the supply picture enough that the locked weights no longer reflect the empirical regime. **The weights do not auto-update; methodology owner must re-evaluate after material infrastructure shocks.**

This section names that constraint explicitly so the production weight set is read as **point-in-time best estimate**, not a stable parametric calibration.

### 13.1 Mechanism

The scenario engine treats weights as probability inputs at the time of valuation. Per-scenario forward curves are anchored to "this is what rates look like in scenario X"; the weight is "this is how likely scenario X is in the current environment." When the environment shifts — particularly when **a structural supply imbalance reverses or compounds** — the weight assignment can become stale faster than the per-scenario forwards do, because forwards are observable (broker FFA strip, transaction prints) while weights are judgmental.

The Set B → Set B-revised transition is the worked example: Set B's `glut_base: 0.55` was defensible against the 2027 baseline US Gulf Coast ramp picture but was overrun by the Ras Laffan Trains 4 & 6 disclosure landing within weeks of the lock. The 10pp shift to `glut_base: 0.45` (Set B-revised) is the methodology-owner response to that empirical update. If Ras Laffan restarts cleanly by end-summer 2026 and US Gulf Coast Stage 3 finishes ramping on schedule, the supply picture flips back toward glut and Set B-revised may itself become stale.

### 13.2 What this means for tool outputs

- **Treat locked weights as a snapshot.** A weight lock dated 2026-06-01 reflects evidence available 2026-06-01. The weights are not a stable calibration like the cycle anchors or the discount rate.
- **The position recommendation is more weight-sensitive than the NAV.** Mark-driven names already carry a vessel-mark sensitivity flag (§9.9). Now also flag **weight-driven** names — those whose call would flip under a reasonable alternative weight set. CCEC under Set B-revised flips HOLD → BUY; the same name flips back to HOLD under Set B. That sensitivity is real and should be priced into position sizing. The weight-robustness diagnostic at §9.10 is the systematic methodology for this classification — every name on the watchlist is run under multiple defensible weight sets, with the per-sector outputs (`outputs/weight_robustness_diagnostic.md` for crude, `outputs/lng_weight_robustness.md` for LNG) feeding the mark-robust × weight-robust matrix.
- **The recurring quarterly diagnostic (per §9.10) addresses this.** Per-name comparison of the locked weight set against bracketing alternatives; per-sector outputs at `outputs/weight_robustness_diagnostic.md` (crude — Sets A/B/C/D) and `outputs/lng_weight_robustness.md` (LNG — Set B vs Set B-revised). Names with small EV%-spread are weight-robust within the evaluated range (FLNG: +6.2pp EV between Set B and Set B-revised); names with large spread or position flip are weight-driven (CCEC: +15.1pp EV, HOLD → BUY) and the call should be sized accordingly. The §13 limitation provides the conceptual *why*; §9.10 provides the operational *how*.

### 13.3 When to re-evaluate

A weight lock should be revisited when **at least one** of the following lands:

- A multi-train LNG facility comes back online (Ras Laffan restart, Plaquemines Phase 2, Arctic LNG 2 resumption) materially changes capacity assumptions.
- The MoU signs (or definitively fails to sign) — this changes the crude weight set, not LNG, but the methodology owner discipline is the same.
- Sustained spot deviation from the central scenario's forward-curve range over a full quarter — e.g., LNG spot persisting above the `tight_resurgence` Q4 2026 forward range ($170-260k) or below the `glut_intensifies` range ($45-68k) for the entire winter.
- A material new LNG basin enters operations (Mozambique LNG, Coral Norte, Rovuma).
- Sanctioned-flow regime change (new sanctions or sanctions relief on a major exporter) changes the trade routing assumption embedded in the cycle-position calculation.

### 13.4 What this is NOT

This is **not** an admission that weights are arbitrary or that the model is over-fit. The framework's interpretability depends on the weight set being a *defensible point-in-time estimate*, periodically refreshed against empirical reality — same discipline as transaction-anchoring the vessel curves (§9.9). The §13 discipline preserves model integrity by making the weight-update protocol explicit rather than implicit.

The Set B → Set B-revised transition was a 10pp shift in a single weight, taking ~30 minutes of evidence review plus a programmatic comparison via `scripts/lng_weight_comparison.py` to generate the diagnostic. The cost of doing it is low. The cost of *not* doing it — running locked Set B weights against a tight 2026 market for another quarter — would be a structurally biased call across the LNG sector.

## 14. Framework limitation — MEG export capacity recovery (infrastructure constraint)

A structural supply-side factor **not currently parametrically modeled** in the scenario forwards: Middle East Gulf export infrastructure damage from the 2026 Iran crisis persists as a binding constraint on actual export volumes even after Strait of Hormuz transit normalises. The framework's Phase 2 rate-normalisation scenarios implicitly assume MEG export capacity recovers in step with vessel transit capacity — which the empirical picture contradicts. Documented as a labelled boundary so it is tracked alongside §12 (high-payout pure-plays at peak) and §13 (scenario-weight stability), not silently embedded in scenario TCE assumptions. (§13 is about *how the framework responds to* infrastructure events; §14 is about *which specific supply-side dynamics are unmodeled*.)

### 14.1 Mechanism

- **MEG export infrastructure damage** from the 2026 Iran crisis affected ~80+ energy facilities across the region (Clarksons / industry reporting, Catlin / VIE analysis 2026-05-25).
- **Ras Laffan Trains 4 & 6** (12.8 mtpa / ~17% of Qatar LNG) confirmed offline through at least end-summer 2026 per QatarEnergy disclosure; restart timeline at material risk of slippage from subsurface / mechanical complications that scale non-linearly with shut-in duration.
- **Some critical repair components require seaborne transit through SoH itself** (specialised turbines, cryogenic exchangers, instrumentation from European / Japanese / Korean OEMs) — a chicken-and-egg constraint that compounds the recovery timeline.
- **Net result:** MEG export volumes recover **slower than vessel transit capacity**, even after the strait reopens. Vessels can move; cargo cannot be loaded in full pre-crisis volumes from the affected facilities.

### 14.2 Why this is not modeled parametrically

- **Non-linear cross-class impact.** VLCC/Suezmax loading from Ras Tanura/Basra is coupled to crude facility recovery; LNG carriers to specific train status; clean-product to refinery throughput. Parametric embedding would require per-scenario, per-class haircuts that compound judgement on top of judgement.
- **Magnitude uncertainty.** Which facilities are damaged, repair timelines, sanctions enforcement on Iranian flows, insurance/finance restoration pace — none have point estimates that survive a 6-month horizon.
- **No historical analog.** Modern LNG / VLCC trade has not absorbed war-scale damage to a single basin's export infrastructure. The 1990 Iraq invasion of Kuwait is the closest precedent and the structural mechanics differ (Kuwait was a smaller share of global oil; LNG trade was nascent).

### 14.3 How this affects current scenario outputs

- **Phase 2 normalisation arrives faster in the framework than reality is likely to deliver.** All sectors' "post-MoU baseline" / "moderate" / "glut_base" Q3 2026 rate-decline curves implicitly assume MEG export volumes are back near pre-crisis levels by then.
- **Q3 2026 TCEs probably conservative on rate level; Q4 2026 TCEs may overshoot to the downside.** Actual Q3 rates may stay elevated above the modelled Phase 2 range (supply side cannot ramp as fast as the framework assumes); the pre_mou_baseline / mou_base / moderate-tightening Q4 forwards are anchored to a "rates have settled" assumption that may not hold.
- **LNG sector specifically:** 2026 glut-scenario near-term intensity overstates actual glut depth. Partly addressed via the v3 Set B-revised weight shift (§11.3) — but the underlying issue is in scenario TCE forwards, not just weights.
- **Crude sector specifically:** MoU base / pre-MoU baseline Q3-Q4 VLCC and Suezmax forwards do not parametrically reflect that MEG crude loading lags VLCC transit capacity. A modest MEG-capacity-drag overlay would tilt these rate forwards 5-15% higher near-term.

### 14.4 Recommended usage

- **Treat near-term (Q3-Q4 2026) Phase 2 TCEs as conservative on rate level.** Mental adjustment: +10-15% on Q3 pre_mou_baseline / moderate forwards; +5-10% on Q4. Phase 1 (escalation / tight) may extend through Q4 2026 rather than resolving in Q3.
- **High-spot crude names (ECO, FRO, DHT VLCC):** the framework's near-term bearishness may be premature. Expect actual rates to lag the framework's normalisation assumption by **1-2 quarters**. For position decisions where the call rests primarily on the Q3-Q4 2026 forward decline, weight the qualitative MEG-drag overlay alongside the model's TRIM signal.
- **LNG specifically:** Ras Laffan is the dominant 2026 narrative — more important than the US Gulf Coast capacity ramp through at least H2 2026. The LNG scenario forwards' winter / Q4 2026 spike numbers are central, not optimistic.
- **For decision-log entries:** when annotating a TRIM signal on a name with high MEG-rate sensitivity in 2026, note §14 is in scope and the actual signal may resolve in the opposite direction over 1-2 quarters if the supply-side ramp lag is real.

### 14.5 What would close this limitation

- **Empirical post-MoU MEG export volume recovery pace.** Two-three quarters of post-MoU data would let the framework either (a) close §14 as historical, (b) parametrise the supply-side lag with an empirical anchor, or (c) curate a "delayed normalisation" scenario.
- **Updated supply-side modelling** that decomposes "rate scenario" into a vessel-side component (FFA-anchored, modelled) and a supply-side component (currently judgemental). Out of scope for v1 because supply-side data is sparse; a natural v2 extension once empirical observation is in hand.
- **Cross-validation against actual Phase 2 spot behaviour in late 2026.** If framework Q3-Q4 forwards are systematically below realised rates, that's quantitative evidence of MEG drag and the magnitude can be inferred from the residual.
- **Until those data points exist, §14 remains qualitative.** The framework's outputs are not silently re-calibrated for it; the discipline is the explicit overlay in §14.4. This preserves model integrity (no opaque adjustments) at the cost of accepting that near-term Phase 2 signals are imperfect.

### 14.6 Related 2026 Iran-crisis dynamics (added 2026-06-03)

Three further structural factors surfaced by Catlin's VIE product tanker macro update (June 3 2026) that are mechanistically adjacent to §14.1-§14.5 but distinct enough to warrant their own bullets. Grouped here rather than as standalone §15 / §16 / §17 sections because they share the 2026-Iran-crisis root cause and the same recommended-overlay discipline; expand into separate labelled sections if any of them grow material enough to need their own subsection structure.

#### 14.6.1 LR2 cargo-switching optionality (vessel-level, not basin-level)

LR2 product tankers with coated tanks carry an **embedded option to switch between clean and dirty trades** based on relative earnings. Per Kpler / Catlin, between early March and mid-April 2026 clean LR2 earnings traded at an **average discount of $87,000/day to dirty equivalents** — clean LR2 demand collapsed (MEG accounted for 44% of LR2 ton-miles in 2025) while West-of-Suez Aframax demand surged. Coated tonnage redeployed rapidly into crude and fuel-oil trades. **The framework values LR2 vessels at the LR2 (Aframax-equivalent) curve for marks (correct) but routes earnings exclusively through `lr2_clean` rate forwards via the product class map (incomplete).** The cargo-switching optionality is unmodeled — it would show up as Q2-Q3 2026 earnings upside vs the framework's blended TCE assumption for LR2-heavy names, particularly STNG (see §6 STNG entry). Distinct from §14.1's basin-level MEG supply constraint: §14.1 is *fewer cargoes available at the port*; §14.6.1 is *the coated vessel can carry a different cargo than the framework assumes*. Both effects compound for LR2-heavy product names.

#### 14.6.2 Sanction-waiver expiry (date-specific binary event)

OFAC General License 134C extends Russian crude / refined-product sanctions relief through **2026-06-17** (the current iteration; loaded-by cutoff 2026-04-17, deliver-by 2026-06-17). On expiry, **~11% of the global product tanker fleet (DWT) currently flagged as sanctioned** loses the temporary waiver. Catlin notes enforcement post-waiver is now physical (naval interventions, territorial seizures, Ukrainian asymmetric operations) plus a deepening blacklist of supporting networks (financial services, shipbrokers, flag registries, cargo inspection), so the post-waiver capacity withdrawal is likely effective rather than paper. **This is a discrete, date-specific event that materially changes the effective product tanker supply count** in a way the framework's scenario forwards (which are smooth continuous curves) do not parametrically reflect. Recommended overlay: when the waiver expires (or is extended), refresh the watchlist with a §14.6.2 annotation in the relevant decision logs; if expiry holds, treat near-term product TCEs as *more* conservative than the §14.4 overlay alone suggests.

#### 14.6.3 Post-reopen stockpile replenishment phase (demand-side recovery lag)

When the Strait of Hormuz reopens, the framework's Phase 2 normalisation scenarios assume Q3-Q4 2026 rates ease back toward forward-curve levels. Catlin's central scenario is a **multi-quarter elevated-demand period** as: (a) regional repositioning of stranded tonnage commands rate premiums, then (b) chronically depleted refined-product stockpiles (US distillates at two-decade low ~100M bbl; Myanmar / Vietnam / Philippines at ~30 days; Australia at sub-critical diesel / jet fuel; European middle-distillate hubs contracted) require a prolonged replenishment effort alongside organic demand. **This is the demand-side analog of §14.1's supply-side recovery lag** — and like §14.1, it's not parametrically modeled in scenario TCE forwards. Both effects compound: scenario forwards under-state Q3 supply (§14.1) AND under-state Q3-Q4 demand (§14.6.3). Recommended overlay: in addition to §14.4's "+10-15% Q3 / +5-10% Q4" rate-level adjustment, extend the elevated-rate horizon a further 1-2 quarters past the framework's normalisation point.

#### 14.6.4 Bunker MGO-spread blowout (fuel-cost transmission channel)

The Iran/MEG crisis transmits to vessel economics via a **bunker cost channel** that is distinct from the §14.1 supply / §14.6.3 demand effects above. Refinery throughput disruption in the MEG region tightens global middle-distillate supply (jet fuel, diesel, MGO are all distillate products sharing refinery capacity), which drives a **structural premium on Marine Gas Oil (MGO) vs High-Sulphur Fuel Oil (HSFO)**. The Global 4 HSFO-MGO bunker spread (per VIE's Bunker Fuel Spreads sheet, sourced from Ship & Bunker) widened from a baseline ~$300/MT in Aug-Feb 2026 to a peak ~$950/MT in mid-March 2026, easing to ~$550 by early June — the largest absolute spread blowout in the past year and roughly **2-3× the baseline distillate premium**.

**Vessel-economic transmission:**

- **MGO-burning vessels** (vessels operating in Emission Control Areas — North Sea, Baltic, US/Canadian coastal, parts of the Med — and vessels with high port-time / coastal-trade exposure) face a direct net-TCE compression equal to (spread Δ) × (MGO burn rate). For a product tanker burning ~25 MT/day of MGO on ECA routes, the spread Δ from $300→$950 = $16,250/day of incremental fuel cost vs the baseline. Net-TCE drag is real and material.
- **Scrubber-equipped vessels** burning HSFO see the inverse effect: the HSFO-VLSFO spread (currently ~$50-90/MT, recently +$150) widened a similar ~$50 ($80→$130) on the same March 2026 spike, increasing the scrubber economic advantage and validating retroactive scrubber-fitting decisions.

**Framework capture (already implicit):** observed spot TCE inputs to `inputs/market_data/historical_tce_means.yaml` and `scenario_inputs.yaml` are net-of-bunkers (TCE is a freight-rate-minus-bunkers construct), so charterer-side spread pass-through into TCE is implicit. The risk is **staleness**: if our forward TCE deck (scenario rate forwards through Q3-Q4 2026) was set before the MGO spike crystallised and hasn't been refreshed, we'd be carrying stale net-TCE assumptions for MGO-heavy routes.

**Directional read for the watchlist (Q2 2026):**

- **Product tankers running ECA / port-heavy routes** (STNG, HAFN, TRMD product fleets in ARA-Med-USEC corridors; ASC US Atlantic basin; INSW product sleeve): net-TCE more compressed than our forwards capture. **Reinforces the existing TRIM signals on product names** and pushes the same direction as the §11.5 hypothesis #1 (VIE may be too constructive on forward product TCEs). One of the few signals that directionally STRENGTHENS the tool-vs-VIE-Bullish divergence rather than narrowing it.
- **Scrubber-heavy crude fleets** (FRO scrubber-fitted Suezmax/VLCC; ECO modern fleet; STNG/TRMD/ASC scrubber-fitted product hulls): relative scrubber economic value increased ~$50/MT × ~55 MT/day = $2,750/day for a VLCC. Over ~340 sailing days × remaining 10yr life × 0.7 utilization NPV ≈ $3-4M additional per-vessel value not currently marked in `vessel_value_curves.scrubber_premium` (flat $2.5M for VLCC, $1M for Aframax/LR2). NAV understatement on scrubber-heavy fleets ~2-4% — within model noise but worth flagging as a directional bias.

**Cross-reference to §14.6 family:** §14.6.1 is the LR2 cargo-switching vessel-level optionality; §14.6.2 is the OFAC sanction-waiver date-binary event; §14.6.3 is the post-reopen demand-side replenishment lag; **§14.6.4 is the bunker-cost transmission channel from the upstream refinery disruption**. All four are 2026-Iran-crisis-rooted but route through different mechanisms; together they form a more complete picture of how the MEG closure translates into per-name P&L beyond the headline supply-side ton-mile effects.

**Recommended overlay:** as part of the quarterly refresh discipline, cross-check the HSFO-MGO and HSFO-VLSFO spreads (VIE Bunker Fuel Spreads sheet or Ship & Bunker direct) against the bunker-state assumed in current scenario TCE forwards. If spreads have moved >$100/MT since the last forward-deck refresh, treat downstream product TCE assumptions as having ~5-10% upward bias and adjust position-sizing on MGO-exposed product names accordingly. **Not currently modeled parametrically** — adding an explicit bunker-spread layer (dynamic `scrubber_premium` + bunker pass-through coefficient on TCE forwards) is a candidate future framework extension but not warranted at current precision level (2-4% NAV effect, within scenario-weight noise).

## 15. Framework limitation — governance / structural-NAV-trap discount (added 2026-06-06)

The framework's NAV machinery answers **"what are the assets worth?"** It
does not answer **"what will the market pay for those assets given how the
controlling shareholders are going to allocate them?"** For most names the
two questions converge — assets get monetised via dividends, sales, or
buybacks within a reasonable horizon. For a class of **controlled-FPI /
low-payout / related-party** structures the two questions diverge
persistently, and the framework's headline FV becomes a structurally
unreliable signal for actionable position-sizing on those names.

This is the **inverse symmetric case of §12** (high-payout pure-plays at
peak, where the framework UNDERvalues because the dividend stream is the
investment thesis). Here the framework OVERvalues because the asset NAV
will never be realised for common shareholders at full face value.

### 15.1 Mechanism

For an affected name:
- **Asset NAV** computes normally: vessels at market, balance sheet net, no
  governance penalty in `compute_nav`. Broker NAV consensus (k_broker)
  typically agrees with tool NAV on the asset-side question — both lenses
  see the same vessels and balance sheet.
- **Market price** clears at a persistent fraction of asset NAV (typical
  range 0.40-0.60 across multiple cycles) — not the temporary mark-driven
  discount the `consensus_pnav` spread captures for a single quarter.
- **Sources of the persistent discount** (typically multiple in combination):
  1. **Controlled-shareholder structures.** Founding-family or single-block
     control limits hostile takeover, suppresses M&A premium, and concentrates
     capital-allocation discretion in management whose interests are not
     1:1 with common shareholders.
  2. **Related-party transactions.** Management fees paid to founder-
     controlled service entities (Tsakos Columbia for TEN; analogues at
     other FPI structures), charter counterparties with founder-related
     interests, sourcing arrangements with related yards.
  3. **Capital-allocation alignment.** Low common dividend (often <25% of
     EPS) with retained capital deployed into newbuild programs whose
     returns to common are uncertain; no buyback programs even when stock
     trades far below tool NAV. Implicit message to the market: "we will
     reinvest, not return."
  4. **Preferred-share structure.** Multiple series with rates / call
     dates / liquidation preferences that may not align with common; held
     in part by affiliated entities; preferred dividends mandatory while
     common is discretionary.
  5. **Free-float / governance discount.** Combined effect of all of the
     above on the equity-risk premium common shareholders demand.

None of these are illegal or improper — they are well-disclosed
structural choices. The framework's silence on them is the limitation.

### 15.2 The mechanism we DO have (and why it isn't enough)

The §9.9 broker-NAV sweep (`k_broker`) captures *vessel-mark uncertainty*:
the wedge between tool NAV and broker NAV under different vessel-value
assumptions. For affected §15 names, **both tool and broker NAV agree on
the asset-side question** (k_broker close to 1.0 or modestly above), yet
the market price sits ~50% below both. The k_broker mechanism therefore
DOES NOT flag §15 cases — it correctly reports the assets agree, while
the unrelated market discount goes unmodelled.

### 15.3 Names exhibiting the pattern

Currently on the watchlist:
- **TEN (Tsakos Energy Navigation)** — first §15 case, onboarded 2026-06-06
  with a 30% governance discount. All five sources above apply; market
  consistently clears at ~40-50% of tool NAV across cycles. VIE Bullish
  $51.50 ≈ tool PW FV $49.37 (post-30%-haircut); VIE itself implicitly
  applies ~47% discount vs the unconstrained NAV. The framework's pre-
  haircut BUY signal at +55% EV would mislead a reader without explicit
  governance overlay. With the 30% haircut, the signal moderates to a
  +12% EV BUY consistent with VIE.

Other archetypes that would exhibit the pattern if onboarded:
- DSX (Diana Shipping) — controlled-shareholder structure; dry-bulk
  retention/payout pattern
- SBLK, CMRE — controlled FPI with management-related entities
- Multiple smaller US-listed FPI tankers/dry-bulk where Greek founding
  families retain majority control

### 15.4 The schema knob

`BalanceSheet.governance_discount_pct` (float in [0, 1], defaults to 0.0):
when set, applies a multiplicative haircut to:
- The NAV term in `blend_fair_value` (the blended FV becomes
  `w_nav × NAV × (1 - gov_disc) + w_earn × strip`)
- The strip's terminal value in `compute_dividend_strip` (the terminal
  is a NAV-realisation; interim DPS are NOT haircut — those are
  realised cash to common already)

Calibration:
- `0.0` (default) — no discount; framework treats asset NAV as realisable.
- `0.10-0.20` — modest governance overhang (e.g. controlled-shareholder
  structure without related-party drag).
- `0.30-0.40` — full §15 pattern (controlled + related-party + low payout
  + preferred misalignment). TEN sits here at 0.30.
- `0.50+` — extreme value-trap; consider whether the framework's BUY
  signal is meaningful at all, or whether the name should be marked
  "do not act on tool output" in the decision log.

Judgmental, set per-name based on observed multi-year median P/NAV vs
peer group. Revisit at any material governance signal change (capital-
return policy update, management transition, M&A activity, related-party
unwind, preferred refinancing).

### 15.5 Recommended usage for §15 names

1. **Treat the post-haircut PW FV as the actionable headline**, not the
   pre-haircut.
2. **Cross-reference against external signals** — VIE coverage,
   sell-side consensus, the name's own multi-year median P/NAV. The
   tool's role is to keep the discount **named and auditable**, not
   to claim it solved governance.
3. **In the decision log, name the §15 overlay explicitly** when
   discussing the position. "Tool BUY +12% post-§15 30% haircut;
   VIE Bullish $51.50 agrees; pre-haircut tool would have been
   +55% misleading" beats "tool BUY +55%, market wrong" — the former
   is what scoreable decisions look like in this class of name.
4. **Diagnostic divergence between pre-haircut and post-haircut FV is
   itself information.** A name where the 30% governance haircut moves
   the position from BUY to HOLD is in the danger zone — the call is
   contingent on a judgmental discount many readers would set
   differently. A name where the haircut moves BUY → milder BUY (TEN)
   is less fragile.

### 15.6 What §15 is NOT

- **Not a parametric solution.** The framework will never encode "the
  right governance haircut"; the haircut is a judgemental input.
- **Not a substitute for fundamental governance analysis.** Setting
  the haircut requires reading the name's history of capital allocation,
  related-party disclosures, and shareholder treatment; the schema
  knob is the storage mechanism, not the analysis.
- **Not applied to broker-NAV sweep or k_broker** — those operate on
  asset-side NAV (the question they answer). The §15 discount applies
  only at the realisation-of-NAV layers (blend NAV term + strip terminal).
- **Not retroactive** — historical decision-log entries are not re-scored
  with §15 haircuts. Going forward, §15 names should be tagged at the
  decision-log layer and discount applied per-quarter as relevant.

## Appendix A. Changelog

Dated record of material framework changes. Lock dates use UTC.

### 2026-06-09 (late evening, Part 4) — Transaction-anchored marks become the pipeline DEFAULT (owner decision)

- **`use_transaction_anchored` flipped to `True` by default** across
  `value_company`, `run_scenarios_watchlist`, and `run_broker_sweep`
  (which now also applies the recalibrated marks to its "tool" endpoint,
  so `k_broker` measures the broker premium over TRANSACTION-VALIDATED
  levels). The §9.9 comparison report still values both ways. This closes
  the question left open in the Part 3 entry below.
- **Owner rationale (verbatim intent):** Sinokor's VLCC buying campaign is
  not a distortion to be filtered out — Sinokor is the dominant buyer in
  the VLCC S&P market and **its bid IS the market**. The "tool produces
  independent NAV from transaction-validated marks" doctrine now holds at
  the default code path, not just on a toggle. The Sinokor 35-vessel
  aggregate remains out of the regression on DATA-QUALITY grounds only
  (no per-vessel disclosure; synthetic splits would violate the
  no-back-solve rule) — vlcc.yaml notes updated accordingly; promote
  individual campaign vessels when itemized prints surface.
- **Headline re-base (2026-Q1, price-unchanged):** DHT FV $16.49 → $14.31
  (BUY → TRIM/SHORT), ECO $42.56 → $36.66 (HOLD → TRIM/SHORT), FRO
  $31.37 → $27.09 (HOLD → TRIM/SHORT), TNK $79.13 → $73.96 (BUY → HOLD),
  TRMD $27.27 → $26.09 (HOLD → TRIM/SHORT), NAT NAV $2.63 → $2.08,
  INSW NAV $57.91 → $52.43, TEN NAV $88.56 → $80.78 (BUY intact),
  STNG NAV $83.87 → $80.35 (HOLD intact), SBLK $25.52 → $25.66.
  FLNG / CCEC unchanged (no class exposure). Decision logs annotated
  (9 names) — the drift flags on this run are the methodology re-base,
  not market moves.
- **New k_broker semantics:** validated crude pure-plays now show a tight,
  UNIFORM broker premium (DHT 1.14 / ECO 1.12 / FRO 1.12) — brokers run
  ~12-14% above arm's-length transaction levels on crude as of Jun-2026.
  INSW (1.52), HAFN (1.43), STNG (1.37), NAT (1.98) discriminate above
  that band. `test_broker_sweep_discriminates_hybrid` re-written to
  assert uniformity-of-premium across pure-plays rather than k≈1.0;
  DHT FV-band tests re-based 16.0-17.0 → 14.0-15.0.
- The un-anchored broker-resale curve remains available as the diagnostic
  alternative (`use_transaction_anchored=False`) and as the baseline
  column of `outputs/transaction_anchor_comparison.md`.

### 2026-06-09 (late evening, Part 3) — Pareto-archive S&P sweep: tanker transaction samples expanded, LR2 own-fit, incremental scanner

- **Pareto Shipping Daily archive systematically mined for tanker S&P prints**
  (280 reports, 2025-01 → 2026-06; same sweep methodology as the Part 2
  dry-bulk pass). In-window samples expanded: VLCC 5 → 10, Suezmax 6 → 18,
  Aframax 7 → 12, **LR2 1 → 11**, MR 2 → 21. LNGC scanned but yielded only
  demolition prints — per §9.9 scope discipline, NO lngc.yaml created (no
  comparable sample exists; LNG S&P for modern tonnage is structurally thin).
- **LR2 graduates from Aframax-proxy to own-class fit.** The §3.1 v1
  limitation ("LR2 modeled as Aframax-equivalent") is retired — 11 in-window
  prints (mostly STNG's own disclosed fleet-renewal sales) clear the n≥2
  gate, and the `_PROXY_ALIASES` propagation becomes a no-op for LR2. The
  clean-LR2 fit lands −1.6%/−9.2% at 5/10yr vs the crude-Aframax proxy.
- **Headline finding: tanker 10yr anchors were running HOT vs arm's-length
  prints.** New fits: VLCC −18.3%/−18.1% at 5/10yr, Suezmax −6.6%/−12.9%,
  Aframax +3.3%/−10.4%, MR ~flat (+0.1%/−0.2%). Under
  `use_transaction_anchored=True` five names flip: DHT BUY→TRIM/SHORT,
  ECO HOLD→TRIM/SHORT, FRO HOLD→TRIM/SHORT, TNK BUY→HOLD,
  TRMD HOLD→TRIM/SHORT. Headline (baseline) calls unchanged — the toggle
  remains opt-in. **OPEN DECISION (owner): make transaction-anchored marks
  the pipeline default now that every covered class has a real sample?**
  The "what this tool is" doctrine (independent NAV from transaction-
  validated marks) argues yes; the counter is that several fits lean on
  broker-reported (non-issuer-confirmed) prints and the Sinokor-distorted
  VLCC market. Deliberately NOT flipped unilaterally.
- **§6 mark-driven retest:** INSW, STNG, HAFN, ASC classifications all
  SURVIVE the expanded anchors (spreads widen, not close — the marks gap
  is real, and for STNG the curve is now anchored largely to STNG's own
  realised prints with NAV moving <4.5%). One locked test expectation
  reversed with documentation: `test_suezmax_recalibration_lifts_nat_nav`
  → `..._lowers_nat_nav` (thin-sample artifact corrected by 18-print fit).
- **Incremental scan infrastructure** (`sp_scan.py`, 6 tests): cursor at
  `inputs/market_data/transactions/_scan_state.json` (currently 2026-06-08),
  review queue at `outputs/sp_print_candidates.md` (191 candidates archived).
  Weekly Pareto ingest now only scans new PDFs:
  `python -m crude_tanker_fv.sp_scan`. Candidates are human-classified
  before entering a transactions YAML — auto-parsing prose into fit inputs
  is deliberately out of scope. 2024-H2 archive files (71 PDFs) deliberately
  NOT mined: pre-2025 market regime, recency weight < 0.4 at current as_of.
- **Backlog registered — exogenous-recession demand-destruction overlay**
  (depends on the Task-3 news-driven weight adjuster above): dated
  `demand_destruction_overlay` field (0.00–0.25, default 0.00) on the
  weights ledger, applied as FINAL multiplier on probability-weighted FV,
  crude + product only. Parameterizes ONLY the war-INDEPENDENT demand
  channel (credit cycle, China structural, equity drawdown) — the
  war-LINKED channel (high oil → demand destruction) lives in the scenario
  curves and must NOT be double-counted. Guardrail first: verify
  `pre_mou_baseline`'s back half bends down enough to carry the linked
  erosion before sizing any overlay. Sensitivity report at {0, 10%, 20%};
  trigger rules tied to macro signals (PMIs, credit spreads, equity tape),
  explicitly NOT oil price or Hormuz status. Sizing of the 25% cap needs
  an empirical peg (2008-09 precedent) before implementation.
- **Backlog registered — issuer-report S&P sweep at refresh time:** fold a
  "scan the quarter's 6-K/10-Q/PRs for disclosed vessel sales" step into
  the quarterly refresh checklist per ticker (marginal yield ~1-3 prints
  per name per quarter with better vessel detail than Pareto prose).
- **Backlog registered (2026-06-10, owner spec vetted) — periodic news
  pull.** Two halves: (a) a weekly scheduled runner (wrapper + launchd
  plist, RC-ingest pattern) chaining the existing scanners — `sp_scan` →
  `--links` → `--fetch-links` → `pareto_archive --build-manifest` —
  logging to `state/`; (b) a `/news-pull` slash command for the
  agent-judgment half: web-sweep all watchlist names weighted to the
  APPROX set (NAT/ASC/CCEC/TEN) + live-event names (detected from
  decision logs, not hardcoded), hunting disclosed S&P prints, dividend/
  policy changes, stance changes, NB orders, deal milestones; output a
  dated review digest at `outputs/news_digest_YYYY-MM-DD.md` with
  promotable-candidate, stance-change, live-deal, stale-price, and
  no-action sections; ends with the post-promotion drift-loop reminder.
  Digest is a review queue — the pipeline never reads it; promotion is
  human-only. **Amendments from the vetting pass (apply at build time):**
  (1) restate the automation-write constraint as "never write
  pipeline-loaded YAMLs" — the raw-archive trees under `inputs/`
  (`research_pareto*`, `ffa_drybulk`) + the scan cursor are designated
  automation-writable, otherwise `--fetch-links` violates the rule as
  drafted; (2) sequence the runner AFTER (or chaining) the Rocket.Chat
  incremental ingest — dailies arrive via RC, so a Friday-evening runner
  can fire before Friday's daily exists; (3) APPROX names are
  permanently stale-priced by construction — flag them only when the
  sweep finds a FRESHER price, else one standing known-stale line, to
  keep the digest signal-dense; (4) promotable-candidate format must
  carry built-year/age and an explicit en-bloc/per-vessel-split field —
  en-bloc without disclosed split is documented-not-promoted per the
  no-back-solve rule. Cross-links: complementary to the issuer-report
  sweep above (weekly web-side vs quarterly filings-side); the digest is
  a natural future signal feed for the Task-3 news-driven weight
  adjuster that the demand-destruction overlay depends on (out of v1
  scope). One session, v1 time-boxed.
- **Backlog carried forward:** GNK onboarding (second dry-bulk validator —
  decides the §11.7.6 v1 lock outcome), §6 SBLK entry promotion (drafted in
  decisions/sblk_log.md), Pana 2016-kamsarmax duplicate-print
  disambiguation (2025-09-19 vs 2025-10-06 Pareto mentions).

### 2026-06-09 (evening) — Jun-9 scenario recalibration (crude / LNG / product weights + LR fix + VLCC re-anchor)

- **Crude weights reset, Jun-9 point-in-time** (`{escalation 0.25, pre_mou_baseline 0.45, mou_base 0.18, mou_bear 0.12}`, from `{0.10/0.15/0.50/0.25}` v1). `pre_mou_baseline` becomes the base case — the April/May MoU/ceasefire path failed to physically reopen Hormuz; Jun-8 US helicopter downed near the strait; ceasefire faltering. Revisit when US response resolves. NOT a permanent lock.
- **LNG weights reset, Jun-9 v4** (`{0.25/0.25/0.38/0.12/0.00}`, from v3 Set B-revised `{0.15/0.25/0.45/0.15/0.00}`). Qatari LNG transits Hormuz; tight_resurgence gains mass. See §11.3 v4.
- **Product weights reset, Jun-9 v3** (`{0.25/0.30/0.30/0.15/0.00}`, from Set B v2 `{0.15/0.25/0.45/0.15/0.00}`). MEG product flows transit Hormuz; refinery_squeeze gains mass. See §11.5 v3.
- **Dry bulk weights UNCHANGED.** Iron-ore flows are stable; only channel is global-recession risk; expressed via existing `coordinated_slowdown` weight (0.15).
- **Issue #1 fix — product LR Q3-2026 Phase-1 spike removal.** `sectors.product.scenarios.{glut_base,demand_softening,structural_decline}.{lr1_clean,lr2_clean}.q3_2026` corrected (95k/48k/38k → 37k/32k/26k mids). Deliberately breaks the prior "INSW whole-company FV preserved exactly through the v2 refactor" invariant — the invariant was preserving a copy bug from the v2 INSW shortcut. INSW Q3-2026 LR2 weighted moves $114.5k → $86.0k under isolated curve fix (or → $109.4k under the full Jun-9 weights+curve reset).
- **Issue #2 fix — dry-bulk supra_ultra crossover.** `sectors.dry_bulk.scenarios.china_property_drag.supra_ultra` back-half (q3_2027 → q2_2028) lowered so the bear stays below the base. "Insulated by minor bulk" was over-credited; insulated ≠ unaffected.
- **Issue #3 fix — LNG `structural_reset` shoulders.** q3_2026 / q2_2027 / q3_2027 pulled below `glut_intensifies` for both `lng` and `mgc` sub-classes. Weight 0.00 so no parametric impact; cosmetic-but-honest fix.
- **VLCC Q3-2026 timing re-anchor (Task 2b).** `pre_mou_baseline.vlcc.q3_2026` 200k → 233k mid; `mou_bear.vlcc.q3_2026` 80k → 119k mid. q4 troughs unchanged — at current $388k spot, the prior Q3 band would have required a physically impossible near-instant crash into the first month of Q3. Lift Q3 only; the crash now lands inside Q3. Timing view, not a settled level.
- **Confirmation-gated, NOT announcement-gated weight discipline.** The May-29 set (which leaned `mou_base 0.50` the day after an unsigned deal) was disconfirmed within ~10 days — that lesson is codified as the rule going forward. `mou_base` earns mass on PHYSICAL Hormuz reopening (verified transit + mine-clearing), NEVER on a deal announcement alone. Master state variable for the crude/Iran tree is the physical status of Hormuz, not a headline. The May-29 → Jun-9 backtest panel + the locked benchmark `{0.10/0.15/0.50/0.25}` are retained for future Task-3-backlog backtest scoring.
- **Headline FV moves** (regenerated 2026-06-09 evening, pipeline `2026-Q1`):
  - DHT $13.34 → $17.32 (TRIM/SHORT → **BUY**); ECO $32.53 → $45.41 (→ HOLD); FRO $23.87 → $33.77 (→ HOLD)
  - INSW $52.08 → $64.59 (TRIM/SHORT narrows); TNK $69.31 → $78.90 (HOLD → BUY); NAT $2.28 → $3.37 (TRIM/SHORT, §12 floor unchanged)
  - FLNG $28.04 → $29.73 (→ HOLD); CCEC $26.45 → $29.63 (BUY firmer, +14.5pp EV)
  - STNG $73.40 → $76.37; HAFN $5.41 → $5.87; TRMD $25.59 → $27.83 (→ HOLD); ASC $14.50 → $15.07
  - TEN $49.37 → $62.79 (3-sleeve hybrid; benefits from both crude and product reweights)
- **Test surgery.** 10 FV-band / position / "INSW preserved" tests marked `@pytest.mark.skip` with rationale "Jun-9 weight reset is point-in-time; unskip when weights settle post-Hormuz physical-state resolution." Weight-load tests (LNG, product) updated to Jun-9 v4 / v3 values. Suite: 189 pass / 10 skip.
- **Task 3 backlog registered.** News-driven scenario-weight adjuster — dated `weights_history.yaml` ledger, trigger→shift rules formalising the confirmation-gated discipline, backtest mode with `--as-of <date>` flag, optional HITL pipeline for proposed deltas. Scope deferred; the Jun-9 weights themselves are the first dated entry going forward.

### 2026-06-09 — §11.7 Dry bulk sector formalised (first fully greenfield sector)

- **§11.7 added.** Dry bulk methodology decision doc locked: three classes
  (Cape / Pana / Supra-Ultra collapsed), four-scenario Bulk Set A weight family
  (china_acceleration 0.20 / moderate_growth 0.40 / china_property_drag 0.25 /
  coordinated_slowdown 0.15), three-name validator pool (SBLK + GNK Pareto-
  anchored, CMDB APPROX-anchored). Cycle anchors derived empirically from a
  22-month Pareto Shipping Daily archive (351 reports, 2024-08 → 2026-06):
  Capesize $23,650 / Panamax $11,900 / Supra-Ultra $13,930 USD/day, all median
  (robust to PDF parse-error tails). Calibration-lock target ≥70%/±10% per
  CLAUDE.md new-sector tier. **Methodology-only this week**; code wire-up
  (`sectors.dry_bulk` block + class map + cycle anchors YAML + name onboarding)
  in Week 2.
- **Independent validation of the Supra/Ultra collapse decision:** Pareto's
  own Shipping Daily reclassified the smaller-bulker benchmark from "Supramax"
  to "Ultramax" in September 2025 — a chartering-desk-level confirmation that
  the two are commonly treated as one cycle class.
- **Pareto archive infrastructure shipped:** new module
  `src/crude_tanker_fv/pareto_archive.py` walks 481 PDFs in
  `inputs/research_pareto/`, classifies as shipping_daily (351) /
  container_weekly (42) / company_report (83) / other (5), refolders non-
  dailies under `inputs/research_pareto_other/<type>/YYYY/MM/`. Extracts ~45
  right-column scalars per shipping_daily into `inputs/market_data/
  pareto_daily.csv` (wide) and per-ticker share-price + P/NAV + P/E rows into
  `inputs/market_data/pareto_share_prices.csv` (long, 3,834 rows × 25 tickers).
  Handles four documented schema epochs (tanker route labels added Apr 2025,
  Supramax→Ultramax Sep 2025, MR West/East split May 2026, comma vs space
  thousands separator). Designed for re-use by Phase F daily-extraction hook.
- **Joeri PNG sampling outcome:** 837 PNGs from Rocket.Chat clipboard ingest
  evaluated; ~12-25% are clean Cape/Pmax/Smax FFA grids — high-quality
  structured data when present. Decision: defer OCR to §11.7 v2 (post-§9.11-
  signal); v1 ships with synthesised forward curve per tanker-sector default.

### 2026-06-04 (late-evening — §14.6.4 bunker-spread channel)

- **§14.6.4 Bunker MGO-spread blowout (fuel-cost transmission channel) added** to the §14.6 family, completing the four-channel decomposition of how the 2026 Iran/MEG crisis transmits to vessel economics. §14.6.1 = LR2 cargo-switching vessel-level optionality; §14.6.2 = OFAC sanction-waiver date-binary event; §14.6.3 = post-reopen demand-side replenishment lag; §14.6.4 = bunker-cost transmission via distillate tightness (HSFO-MGO spread blew out from baseline ~$300/MT to peak ~$950/MT in mid-March 2026, easing to ~$550 by early June per VIE Bunker Fuel Spreads sheet sourced from Ship & Bunker). **Net transmission:** MGO-burning vessels (ECA traders, port-heavy product fleets in ARA-Med-USEC) face direct net-TCE compression on order of $16k/day at peak spread; scrubber-equipped vessels (FRO/ECO/STNG/TRMD/ASC scrubber-heavy fleets) get an inverse benefit from the parallel HSFO-VLSFO scrubber-spread widening. **Framework capture is implicit** via observed-TCE inputs (TCE is net-of-bunkers by construction); the risk is staleness — if forward TCE deck was set before the spike crystallised, MGO-heavy product TCE assumptions carry 5-10% upward bias. **Directional implication:** REINFORCES existing product TRIMs and pushes the same direction as §11.5 hypothesis #1 (VIE may be too constructive on forward product TCEs) — one of the few transmission channels that STRENGTHENS rather than narrows the tool-vs-VIE divergence. **Not formally modeled** — adding dynamic `scrubber_premium` + bunker-cost pass-through coefficients is a candidate future extension, not warranted at current 2-4% NAV precision level. Quarterly refresh discipline: cross-check bunker spreads against bunker state assumed in current TCE forwards.

### 2026-06-05 — Clean-product Handysize class added

- **Handysize class (~37-40k DWT clean-product) added to `vessel_value_curves.yaml`** (NB $40M / 5yr $34M / 10yr $26M / scrap $4.5M; eco-inclusive). Retires the §11.5 off-curve gap for CLEAN-PRODUCT Handies: HAFN's 22 (winding-down, modelled age 18 ⇒ ~$14.5M/ea) and ASC's 2 product Handies (age 11 ⇒ ~$24.6M) moved from `working_capital_net` onto their fleet manifests; HAFN working_capital_net $775M→$475M, ASC $172.6M→$131.0M. **NAV impact as-forecast and small: HAFN +$0.04/sh (drops the prior 10% wind-down liquidity haircut — no on-curve liquidity mechanism), ASC +$0.18/sh. No position flips** (both stay TRIM/SHORT). Going deep showed "Handysize" is really 3 problems: (1) clean-product — now on-curve; (2) **chemical Handy/Handymax** (STNG's 14 IMO-II + ASC's 4×25k stainless) — left OFF-curve deliberately, a product curve would overvalue them (~+$60-100M on STNG); (3) wind-down liquidity discounting — unbuilt. Earnings v1-proxied to MR (rate files + scenario key; Handysize cycle = MR's); NAV curve is the real differentiator. Wired: `loaders.ALLOWED_CLASSES`, `scenarios.PRODUCT_SCENARIO_CLASS_MAP` (Handysize→mr), 4 rate files. STNG fleet/balance-sheet unchanged (chemical Handymax stay off-curve, gap re-labelled). 3 tests updated/added (167 total). Residual "chemical Handy" gap re-scoped under LIMITATIONS §2.

### 2026-06-04 (late-evening — TEN assessed + deferred)

- **TEN (Tsakos Energy Navigation) assessed as the next VIE-Bullish candidate and DEFERRED.** Status verified (still public, no take-private; Q1 2026 strong — rev $253M, NI $89M, EPS $2.72). But TEN is a **four-asset-type hybrid** (crude + product + LNG + DP2 shuttle tankers), and ~15-20% of its value is **DP2 shuttle tankers** (6 in-water + 9 of 18 newbuilds) — offshore contract-backed assets with no spot rate, no FFA curve, and no value curve in our system, anchoring most of TEN's $3.6B backlog. Plus ~$287M preferred equity (no schema line) and a $2.0B newbuild book (> market cap). Onboarding without a shuttle-tanker module would produce a confident-looking BUY (TEN trades at a deep discount to NAV) resting on the framework's weakest, un-curveable foundation. **Deferred rather than hand-wave the dominant sleeve.** New `decisions/ten_log.md` captures blockers + gathered research + revisit criteria; `DP2 shuttle tankers` added to LIMITATIONS §2 as the binding coverage gap; §1 + `vie_coverage_universe_xref.md` candidate lines updated. No inputs built; no test/code changes.

### 2026-06-04 (late-evening — consensus forward-EPS cross-check, §9.11)

- **New §9.11 consensus forward-EPS cross-check — the earnings-leg analog of the §9.9 broker-NAV sweep.** Completes the three-legged validation suite: NAV (§9.9), scenario weights (§9.10), forward earnings (§9.11). New `consensus_eps.py` / `pipeline.run_consensus_eps_xref` → `outputs/consensus_eps_xref.md` + `.xlsx`; `consensus_fwd_pe` added to all 12 watchlist entries (Pareto Shipping Daily 4-Jun 1Y FWD P/E) + loader passthrough; wired into `pipeline.main`; documented §9.11 + §7.5b + LIMITATIONS; 8 new tests (158→166). **Mechanism:** back out consensus NTM EPS = price ÷ fwd P/E, compare to our strip's first-4-quarter EPS. **Initial run:** every name shows tool EPS > consensus (+72% to +462%) — the FFA strip holds near-peak rates while consensus prices normalisation. The widest gaps (crude at peak, +160-208%) carry the lowest `w_earn` (0.30) — **the cycle weighting is the designed compensation, and §9.11 makes it auditable.** NAT +462% flags the §12 high-payout name from the earnings angle. Actionable exceptions: below-mid-cycle CCEC (+219%) and FLNG (+83%) at `w_earn` 0.60, where the hot tool EPS is least mitigated — CCEC reinforces the §9.10/§13 weight-driven-BUY caution from an independent angle. Directional cross-check only; no rate/weight inputs changed.

### 2026-06-04 (late-evening — Pareto P/NAV check + VIE NAV cross-reference)

- **Pareto Shipping Daily 4-Jun P/NAV check corrected two stale APPROX inputs and reclassified STNG + TRMD as mark-driven.** Our `consensus_pnav` for STNG (0.87) and TRMD (1.00) were APPROX guesses; the real Pareto 4-Jun P/NAVs are **0.70** and **0.83**. Correcting them (and refreshing all 12 prices + P/NAVs to the 4-Jun report as a matched set) raised broker NAV (STNG $90.80→$108.00; TRMD $27.25→$33.98) and widened the tool→broker spread (STNG +8pp→**+27pp**; TRMD +2pp→**+22pp**). **STNG is no longer mark-validated** — the "mark-validated bucket" reduces to DHT/ECO/FRO. The 5 well-covered names (DHT/ECO/FRO/TNK/INSW) validated to ±0.01. Pareto publishes **no P/NAV for NAT/ASC/CCEC** (stay APPROX/unanchored). LIMITATIONS §1/§3/§4 + `vie_coverage_universe_xref.md` STNG row corrected.
- **New `outputs/vie_nav_xref.md` NAV-layer diagnostic + §11.5 subsection.** Cross-references all 12 names' tool NAV vs broker NAV (price÷Pareto-P/NAV) vs VIE NAV. **Finding: VIE NAV ≈ broker-consensus NAV across the board** (VIE/broker 0.86–1.07; VIE at-or-below broker, never the bullish outlier) — VIE is a second read on broker consensus, not an independent third mark, so the tool-vs-VIE gap is the §9.9 mark spread re-expressed. An earlier draft's "VIE marks product above even broker" was an artifact of the stale STNG/TRMD P/NAVs and was withdrawn. **§11.5 hypothesis #2 (product curves conservative) confirmed by two agreeing sources** (Pareto broker + VIE, both ~25-50% above tool on STNG/TRMD/HAFN); the gap reconciles to the §14.6.1 LR2 cargo-switching option (broker+VIE price it; the clean-LR2 transaction print and our curve do not). No curve recalibration implied. Two conservative-side reads (TNK, FLNG) where VIE validates our lower mark over a broker premium.

### 2026-06-04 (post-HAFN, evening — crude-class transaction anchor expansion)

- **§9.9 item-9 closure language updated + new §11.5 "Crude-class transaction anchoring — expanded sample" subsection added.** The 2026 transactions worksheet was extended with a "Crude Tanker Deals" sheet (14 rows), driving a new `vlcc.yaml` (5 in-window single-vessel prints + Sinokor campaign + FRO related-party NB as out-of-fit documentation) and extending `suezmax.yaml` (FRO Front Ull/Idun named-deal age 11.5 $70M + NB resales) and `aframax.yaml` (STI Condotti age 11 $70M, eco scrubber, Aframax-trading-mode LR2). **Solver fits:** VLCC 5yr **−15.6%** ($138→$117M), 10yr **−13.1%** ($111→$96M); Suezmax unchanged (FRO named-deal confirms prior chatter); Aframax 10yr softens from −12.8% to **−9.1%** (STI Condotti at $70M lifts right-edge). **§9.9 item-9 correction:** prior closure language ("VLCC validated separately by pure-play P/NAV reconciliation and TNK $84.5M ≈ curve") was overstated — TNK $84.5M actually sits 9% below the existing curve at age 13, and the full 5-print sample shows systematic 10-15% high bias at modern end; DHT-price-≈-broker-consensus validates only that tool and broker agree on DHT, not either vs transaction reality. **Per-name NAV impact:** DHT −11.5%, ECO −8.6%, FRO −8.9%, INSW −2.0%, TNK −3.0%, NAT +0.4%, STNG −1.0%, HAFN +3.5%, **TRMD +2.7% → POSITION FLIPS TRIM → HOLD** (TRMD was on TRIM/HOLD margin; flip is on a thin 1.3pp basis and direction-narrows the §11.5 tool-vs-VIE-Bullish gap). **Cross-sector asymmetry observed:** transaction anchoring DEEPENS crude TRIMs (curves were generous) and modestly NARROWS product TRIMs on mixed-fleet names (curves had mixed conservative/generous regions) — sector-asymmetric response consistent with "crude leading rate normalization; product holding firmer" narrative. Three new tests added (`test_vlcc_yaml_loads_and_fit_lowers_anchors`, `test_vlcc_recalibration_lowers_dht_nav`, plus extended `test_toggle_on_changes_exposed_names_only` and `test_comparison_report_writes_outputs` for the new VLCC exposure — DHT/ECO no longer no-exposure controls, FLNG/CCEC remain). **Open methodology decision (deferred):** whether to ship transaction-anchored fit as production default rather than opt-in toggle — held until ≥2 LR2 prints clear the fallback guard for a clean-LR2 sub-curve.

### 2026-06-04 (post-HAFN, PM — product-class transaction anchor)

- **§11.5 empirical test of hypothesis #2 — product-class transaction anchoring added.** A 12-row 2026 product tanker transactions worksheet (Scorpio Tankers fleet disposals + d'Amico newbuild orders + Compass broker prints) was filed into the §9.9 transaction-anchor infrastructure as `mr.yaml` (2 in-window, 4 out-of-window documentation prints) and `lr2.yaml` (1 in-window). The §9.9 proxy-alias logic in `transactions.py` was refactored from "fire when alias has no own file" to "fire when alias has no valid own fit", so a sparse `lr2.yaml` continues to inherit the Aframax fit until enough LR2 prints accumulate for a clean-LR2 sub-curve. **Solver fits:** MR 10yr +10.1% ($34.5M→$38.0M), MR 5yr +2.2% (clamped from +15% raw fit), LR2-via-Aframax 10yr −12.8% (unchanged from prior). **NAV impact:** ASC +8.6%, HAFN +2.6%, INSW +1.6%, TRMD +0.7%, STNG −3.0% (LR2-dominated). **Conclusion:** hypothesis #2 partially validated for MR but falsified-in-wrong-direction for LR2 — the single LR2 print sits ~27% BELOW the active Aframax-proxy curve, empirically confirming the §3.1 v1 limitation. Methodology divergence narrows by 1-9pp on mixed-fleet names but is NOT closed; hypothesis #1 (VIE forward TCEs more constructive than even Product Set B v2) remains the dominant unexplained residual. **No position-call flips.** Two new tests added (`test_lr2_yaml_loads_and_documents_clean_lr2_gap`, `test_mr_yaml_round_trip_and_fit`); the existing `test_lr2_propagation_from_aframax` updated for the new sparse-file-still-proxies behaviour. **Pending:** ≥2 in-window LR2 prints to gate a clean-LR2 v2 sub-curve.

### 2026-06-04 (post-HAFN)

- **§11.5 cross-methodology comparison subsection added** documenting the product-sector pattern of tool TRIM vs VIE Bullish across ASC / TRMD / HAFN (STNG concurrent at TRIM/Watch). This is a sector-level structural divergence, not name-specific noise. Three candidate explanations documented: (1) VIE forward curves more constructive than even Product Set B v2 captures; (2) MR/LR1/LR2 vessel curves conservative vs current second-hand transactions (no product-class transaction-anchored recalibration applied yet, unlike Aframax/Suezmax); (3) transitional phase where both methodologies may be partially right. **Implication:** product sector TRIM signals carry less conviction than crude sector TRIMs where transaction validation exists; product short basket sizing should reflect this structural mark uncertainty. **Not a calibration error to fix** — known methodology divergence to document. Q2 2026 product tanker prints (mid-to-late July) will provide empirical anchor for which methodology is closer to reality and trigger a §13-aligned re-evaluation.

### 2026-06-04 (evening)

- **HAFN (Hafnia Limited) onboarded** as the watchlist's first IFRS-reporting name (Bermuda-incorporated + Singapore-headquartered, dual-listed NYSE + Oslo), first pool-operator (world's largest product-tanker pool), and largest product fleet on the watchlist (109 owned vessels: 10 LR2 + 25 LR1 + 49 MR on-curve + 22 Handysize off-curve, plus 12 chartered-in + 8 firm + 2 option MR newbuilds at Hyundai). Tool: single-point FV $5.54 / scenario PW FV $5.27 (EV −34.6%, TRIM/SHORT). **Mark-driven** (k_broker 1.45, +29pp tool→broker spread — joins ASC/INSW in mark-driven bucket). VIE Bullish ($9.00, +12% upside vs price $8.05) = **third product name after ASC and TRMD where VIE Bullish overrules tool TRIM** — cross-product pattern firmly established (VIE structurally more bullish on product than our framework + broker consensus). **Three-way ordering** tool $5.27 < broker ~$7.66 < VIE $9.00. **Schema notes:** IFRS 16 vessel lease liability ($35.9M) kept separate from bank_debt; TORM equity stake ($395M / $0.79/sh) rolled into working_capital_net pending a future `marketable_equity_investments` schema line; Handysize off-curve sleeve at 10% liquidity discount reflecting strategic wind-down; newbuild commitments $405M (8 firm × ~$50.6M, options excluded). Inputs: 4 YAMLs; watchlist + data_sources updated; 2 new tests (`test_hafn_full_three_class_product_loads_and_routes` validates LR2+LR1+MR routing; `test_hafn_whole_company_fv_in_expected_band_set_b` pins FV in $5.0–$5.8 band + sector assertion per workflow verifier).
- **Workflow-driven verification ran on HAFN onboarding** — 4 parallel adversarial verifiers (inputs / tests / docs / pipeline outputs) caught 3 blockers (newbuild_capex_commitments off by $45M; README ticker count stale; mark-spread classification error in §6 HAFN entry — wrote "mark-validated" when actual k_broker 1.45 / +29pp is mark-driven) plus several nits (fleet manifest comment math; cost structure G&A comparison direction; band test missing sector assertion). All blockers fixed inline; selected nits addressed; pipeline + tests re-verified clean.

### 2026-06-04 (PM)

- **VIE methodology documentation refined based on observed adjustment factor structure.** VIE applies class-specific factors (**0.7 LNG TFDE**, **0.9 tankers / VLGC**, **1.0 dry bulk**) to the 10y-mean comparison denominator; the factors compensate for within-window structural changes (notably the TFDE → MEGI / X-DF / X-DF2.1 propulsion transition that drives the 0.7 LNG factor). Our framework's TC-anchored approach handles structural shifts implicitly via market-clearing historical prices at each historical point; VIE's spot-anchored approach handles them explicitly via factor application. Applying the factors and back-computing collapses the apparent gaps from yesterday's analysis: **VLCC +58% → +42%, Suezmax +14% → +3%, Aframax +15% → +4%, MR2 +18% → +6%, LNG TFDE +53% → +7%**. The collapse to within ~7% for Suezmax / Aframax / MR / LNG is meaningful cross-methodology corroboration. VLCC (+42%) and LR2 (+24%) retain residual gaps warranting separate investigation if/when calibration discipline calls for it. **No rate inputs changed.** New METHODOLOGY §10 subsection added documenting the within-window-structural-adjustment refinement; LIMITATIONS.md framework-level callout extended; `outputs/vie_market_rates_xref.md` updated with corrected back-computations. New self-check item added (verify our 10y means TC-anchored throughout; consider explicit structural adjustment if any spot-anchored components are mixed in). The B-1 work block remains closed by reframe rather than recalibration; the refinement strengthens the cross-methodology corroboration argument.

### 2026-06-04

- **VIE cross-reference reframed from calibration gap to methodology difference.** Public-source research dig (16 sources, 2026-06-04) confirmed VIE's 10-year-mean methodology is not publicly disclosed. The +14% to +58% gaps across vessel classes between our `historical_tce_means.yaml` values and VIE-implied values are the **expected structural signature of a TC-anchored vs spot-anchored baseline difference, not calibration errors.** Our framework uses TC anchoring in both the numerator and denominator of the cycle-position ratio (METHODOLOGY §2.3), which is internally consistent. Switching to VIE's spot-anchored denominator would create a unit mismatch (TC numerator / spot-mean denominator) with no physical interpretation. **No rate inputs changed.** The VIE diagnostic (`outputs/vie_market_rates_xref.md`) reframed accordingly with original numbers preserved as Historical Context. New §10 caveat documents the TC-vs-spot baseline distinction; LIMITATIONS.md §3 Framework-level adds the equivalent credibility-level callout. The B-1 work block (originally framed as "VLCC 10y mean revisit") is closed by this reframe rather than by recalibration. The Suezmax / Aframax / LR2 / MR class gaps are likely the same structural pattern but empirical confirmation deferred — not blocking. The LNG +53% gap is separately and explicitly a deliberate spike-inclusive choice and orthogonal to TC-vs-spot framing.

### 2026-06-03 (late evening)

- **VIE Market Rates & Trends added as a refresh-cycle rate-input cross-check** (`outputs/vie_market_rates_xref.md`). Wired into `inputs/data_sources.yaml` under a new `_market_data_sources` key (non-ticker; refresh.py code paths ignore underscore-prefixed entries). §8.3 refresh workflow updated from 6 to 7 steps — new Step 3 documents VIE cross-check between `spot_tce.yaml` / `twelve_month_tc.yaml` / `historical_tce_means.yaml` and VIE's "Vs. 10y Avg" column.
- **Cross-check findings (documented, NOT actioned):** our `historical_tce_means.yaml` 10-year means run systematically above VIE-implied across every class — Suezmax +14%, Aframax +15%, MR2 +18%, LR2 +37%, LNG +53% (deliberate spike-inclusive), VLCC +58%. The VLCC and LR2 gaps are the cleanest cases for a methodology revisit. **No rate inputs changed** — base-period and outlier-handling choices are deliberate; bulk-replacing from VIE would require explicit methodology decisions per class. Diagnostic captured for the next quarterly refresh review.
- **Spot vs QTD-average framing distinction surfaced:** our `spot_tce.yaml` is a 29-May point-in-time snapshot (capturing the post-correction print); VIE Q2-26 Live Est is a quarter-to-date fixture average (capturing sustained Q2 strength). VIE values are 21-188% higher across classes. This is a structural input-source choice worth a future decision — switching to QTD-average would systematically raise tool FVs across the crude watchlist.

### 2026-06-03 (evening)

- **TRMD (Torm Plc) onboarded** as the first full-3-class product name on the watchlist (22 LR2 + 10 LR1 + 63 MR). Exercises every branch of `PRODUCT_SCENARIO_CLASS_MAP` end-to-end — first time `lr1_clean` rate forwards drive a pure-product name directly (previously only INSW's 30/70 product sleeve touched them). Tool: single-point FV $27.27 ≈ price $27.25; scenario PW FV $25.59 (EV −6.1%, TRIM/SHORT — just below the −5% HOLD threshold). **Mark-validated, narrowest spread on watchlist** (k_broker 1.01, +2pp). VIE Bullish ($34.00 / +20%) is the third product-name opposite-direction counter-signal after ASC and CCEC. Inputs: 4 YAMLs (fleet/BS/cost/dividend); watchlist + data_sources updated; 2 new tests (`test_trmd_full_three_class_product_loads_and_routes` validates MR + LR1 + LR2 routing; `test_trmd_whole_company_fv_in_expected_band_set_b` pins FV in $24-$27 band). Refresh tests rebased to be ticker-count-flexible. 152/152 tests green.
- **VIE Coverage Universe cross-reference added** (`outputs/vie_coverage_universe_xref.md`). Independent-analyst external counter-signal layer alongside §9.9 mark robustness and §9.10 weight robustness. **Full 10-of-10 overlap** with our watchlist; **6 in directional agreement** (DHT/ECO/FRO/TNK/NAT/FLNG/STNG), **2 OPPOSITE** (CCEC: VIE Avoid vs our BUY; ASC: VIE Bullish vs our TRIM), **1 mark-driven gap** (INSW: VIE $79.50 ≈ broker, tool $52.08). **§6 footnotes** added for CCEC (VIE Avoid sharpens §13 — sizing reduced from "smaller than weight-robust BUY" to "neutral pending Q2"), ASC (VIE Bullish softens TRIM to "qualified TRIM"; flags §11.5 Handysize-sleeve gap as partial explanation), INSW (VIE Watch corroborates broker — three-way ordering tool < broker ≈ VIE confirms mark-driven classification), and FLNG (VIE Avoid extends tool > broker > VIE three-way ordering; flags FLNG-specific structural_reset weight as candidate methodology extension). Three onboarding candidates surfaced: TRMD (Torm), HAFN (Hafnia), TEN (Tsakos) — all VIE Bullish. Cross-reference is recurring quarterly (refresh checklist + on VIE coverage updates).

### 2026-06-03 (afternoon)

- **Product weights transitioned from Set A to Set B (v1 → v2 lock).** LNG-analog constructive reweighting following Catlin VIE June 2026 product tanker macro update. Shift: +5pp `refinery_squeeze` (0.10 → 0.15), +10pp `moderate_correction` (0.15 → 0.25), −5pp `glut_base` (0.50 → 0.45), −10pp `demand_softening` (0.25 → 0.15), `structural_decline` unchanged at 0.00. Same shift direction as LNG Set B → Set B-revised (§11.3 v3); Product Set B's destination weights {0.15, 0.25, 0.45, 0.15, 0.00} are numerically identical to LNG Set B-revised by empirical coincidence (both sectors face the same Iran-crisis case), but the labels are sector-scoped and not interchangeable (§9.10). **Impact:** ASC $13.59 → $14.24 (EV −26.5% → −23.0%, TRIM/SHORT unchanged); STNG $68.75 → $73.58 (EV −13.0% → −6.9%, TRIM/SHORT unchanged but just −1.9pp below HOLD); INSW whole-co $52.08 → $52.08 (unchanged, a property of the hybrid carve-out aggregation using crude weights — see §11.5 v2 transition section and test_insw_whole_company_fv_preserved_through_product_sector_refactor rationale). Crude weights, LNG weights, and all scenario forward curves unchanged. Tests rebased (ASC band, STNG band, product weights sum); INSW preservation test now spans both refactor + Set B transition with the methodology equation as the invariant.

### 2026-06-03

- **§14.6 added — three further 2026-Iran-crisis dynamics** grouped under §14 because they share the same root-cause and recommended-overlay discipline as the existing MEG export capacity limitation: (a) **§14.6.1 LR2 cargo-switching optionality** — coated LR2 hulls' embedded option to switch between clean and dirty trades, unmodeled in the current `lr2_clean`-only earnings path; Kpler / Catlin documented an $87k/day average clean-vs-dirty discount Mar-Apr 2026; cross-referenced from §6 STNG entry; (b) **§14.6.2 sanction-waiver expiry** — OFAC GL 134C ends 2026-06-17, potentially re-removing ~11% of fleet (DWT) from active supply; binary date-specific event the smooth scenario forwards don't capture; (c) **§14.6.3 post-reopen stockpile replenishment** — demand-side analog of §14.1's supply-side recovery lag; extends elevated-rate horizon 1-2 quarters past framework normalisation point. Source: Catlin's VIE product tanker macro update (2026-06-03).
- **§6 STNG entry expanded** with "STNG LR2 cargo-switching option value" subsection — analogous to CCEC NB option value scoping but mechanistically distinct (operating-mode optionality vs contract-vs-market optionality). Documents the framework gap, sizes the magnitude (~$0.95/sh of additional Q2 EPS if optimally captured), explains why parametric modelling is out of scope for v1, recommends treating STNG's TRIM signal as "mildly TRIM, with framework-known upside bias" rather than "decisively TRIM." Cross-references §14.6.1 for the framework-gap rationale.
- **No code, test, scenario-weight, or scenario-forward-curve changes** — pure documentation work block extending §14 and §6 in response to authorised user direction (2026-06-03). The cargo-switching mechanism is a flagged framework gap for future v2 consideration; product weights remain locked at the inherited v1 values.

### 2026-06-01

- **§9.10 added — weight-robustness diagnostic** as the probability-weight analog to §9.9 mark robustness. Crude sector diagnostic at `outputs/weight_robustness_diagnostic.md` + `.xlsx` (generated via `scripts/crude_weight_robustness.py`); LNG sector analog at `outputs/lng_weight_robustness.md`. Pairs with §9.9 to give every name two independent robustness dimensions; combined classification framework documented inline. Locked crude weights unchanged — diagnostic only. Initial run found DHT / ECO / FRO are mark-robust + weight-robust (highest conviction TRIM); TNK is the only crude name that is both mark-driven and weight-driven (lowest conviction); CCEC (LNG) is weight-driven BUY + mark-validated. **Cross-reference fixes (audit pass, same day):** §13 (added earlier in WB1) and §11.3 (Set B-revised rationale) were updated to point to §9.10 — §13 now reads "§13 provides the conceptual *why*; §9.10 provides the operational *how*"; §11.3 gains a "Relationship to §13 and §9.10" subsection. The §6 CCEC torque subsection's "§13 framework" tag broadened to "§13 limitation + §9.10 diagnostic". `report.py` gained generic sidecar-diagnostic discovery so `outputs/ccec_buy_diagnostic.md` now surfaces as a hyperlink in `outputs/ccec_fv_report.md` under a new "Additional diagnostics" section.
- **§14 added — infrastructure constraint limitation documented as framework boundary** following VIE / Catlin analysis (2026-05-25) and June 1 macro briefing identifying MEG export capacity recovery as a structural factor not currently parametrically modeled in scenario TCE forwards. Cross-referenced from §3.2 (forward dividend strip), §10 (caveats), and §11.3 (LNG weight history — relationship to Set B-revised). No code, test, scenario-weight, or scenario-forward-curve changes — pure documentation work block codifying what was previously an undocumented assumption embedded in scenario TCE choices.
- **LNG weights transitioned from Set B to Set B-revised (v2 → v3 lock).** Rationale: empirical 2026 LNG supply environment (Ras Laffan Trains 4 & 6 offline through end-summer 2026 at earliest, US Gulf Coast Stage 3 ramp partially absorbed) is more tight-pricing than glut-pricing. Empirical confirmation: LNG spot $67,500 (+391% YoY), TFDE $98,500. Set B's 55% on `glut_base` implicitly asserted glut was the dominant 2026 condition — contradicted by observable market pricing. Set B-revised shifts 10pp constructively: tight 0.10 → 0.15, moderate 0.15 → 0.25, glut_base 0.55 → 0.45, glut_intensifies 0.20 → 0.15, structural_reset 0.00 unchanged. **Impact:** FLNG TRIM/SHORT unchanged but EV improves +6.2pp (−13.4% → −7.2%); CCEC flips HOLD → BUY (EV −1.0% → +14.1%) with weight-driven flag (METHODOLOGY §6 CCEC entry; `outputs/ccec_buy_diagnostic.md`). Crude weights, product weights, and all scenario forward curves unchanged.
- **New §13 framework limitation: scenario-weight stability under infrastructure shocks.** Documents weights as point-in-time best estimate (not stable parametric calibration); methodology owner re-evaluates after material infrastructure shocks (multi-train LNG facility offline/online, sanctioned-flow re-routing, sustained spot deviation from central scenario, new LNG basin operations). Recurring quarterly diagnostic at `outputs/lng_weight_robustness.md`.
- **New scenario torque diagnostic** on the LNG sheet of `scenario_summary.xlsx` (`FV_range` + `torque_5pp` columns). Surfaces TC-heavy (low-torque, FLNG-style) vs NB-heavy (high-torque, CCEC-style) for future LNG name onboardings.
- **CCEC §6 entry expanded** with scenario torque table + weight-driven signal framing + position-sizing recommendation reflecting NB-orderbook leverage.

### 2026-06-01 (earlier same day)

- **Product sector formalised** (`sectors.product`) with five scenarios (refinery_squeeze / moderate_correction / glut_base / demand_softening / structural_decline). Closes the v2 INSW shortcut where MR forwards lived under `sectors.crude` (METHODOLOGY §11.5). INSW whole-company FV preserved to within $0.05/sh ($52.03 → $52.08); pinned by `test_insw_whole_company_fv_preserved_through_product_sector_refactor`.
- **ASC (Ardmore Shipping) onboarded** as the product-sector methodology validator. 19 active MRs + 6 off-curve Handysize/chem + 1 MR HFS + 2 Handy NBs. Single-class pure-product analog to DHT (crude) and FLNG (LNG).
- **STNG (Scorpio Tankers) onboarded** as the first multi-class product name. 32 LR2 + 41 MR on-curve + 14 Handymax off-curve + 9 HFS + 10 NBs (incl. 2 VLCC NBs — first crude exposure). Exercises both LR2 and MR through the product class map simultaneously.
- **Delta report + decision log infrastructure** added. Per-run `outputs/delta_report.md` flags material moves (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, |ΔNAV%| > 5%) and which input YAMLs changed. Per-ticker `decisions/{ticker}_log.md` auto-prepended with structured model-state entries each run, user annotates with calls. Documented in §7.7-7.9.
- **Refresh checklist** (`python -m crude_tanker_fv.refresh`) added as the pre-flight step at quarter start. Flags missing balance sheets with IR URLs from `inputs/data_sources.yaml`, stale market data (>30 days), stale watchlist as_of (>14 days), APPROX consensus_pnav entries. Documented in §8.3.
- **README + LIMITATIONS.md** rewritten as external-reader entry points. Methodology PDF build script at `scripts/build_methodology_pdf.sh` (requires pandoc + xelatex; install docs included).

### Earlier (pre-changelog backfill, approximate ordering)

- **CCEC onboarded** as the second LNG name. Introduced the MGC gas-carrier sub-class (§3.1) for the 22k cbm LCO2 / multi-gas / dual-fuel MGC fleet. LNGC X-DF2.1 propulsion-premium recalibration (5% NB premium, narrowing with age). All committed newbuilds valued newbuild-at-market per §3.1.
- **LNG sector launched + v1 → v2 (Set B) weight transition**: crude-inheritance `{0.10, 0.15, 0.50, 0.25, 0.0}` placeholder replaced with LNG-specific Set B `{0.10, 0.15, 0.55, 0.20, 0.00}`. `structural_reset` scenario curated as the energy-transition tail with `vessel_scale_multiplier: 0.90` mechanism; weight 0.0 (sensitivity tool only, not parametric). FLNG headline FV moved $25.90 → $26.17.
- **Hybrid INSW carve-out (v2)** — both crude and product sleeves now run through the scenario engine and aggregate to a whole-company FV against the actual tape price (§6 v2). Position pairing by per-scenario index in the aggregation step.
- **Transaction-anchored curve recalibration** (§9.9): Aframax + Suezmax curves recalibrated against disclosed second-hand transactions (TNK sale-leasebacks, NAT Suezmax disposal). Opt-in toggle in the pipeline; default off in production to preserve broker-marked baseline as the primary lens.
- **Broker-NAV sweep diagnostic** (§9.9): per-name `k_broker` premium that lifts tool NAV to consensus broker NAV; classification as mark-validated (≤10pp EV spread) vs mark-driven (>10pp).
- **NAT (Nordic American Tankers) onboarded** as the framework-limitation §12 archetype (high-payout pure-play at cycle peak). Suezmax curve transaction-anchored via the TNK $53.5M disposal (residual +0.6%).
- **Cycle-position weighting heuristic** (§2.3): five-band step function on 12M TC / 10yr mean ratio, driving NAV-vs-strip blend weight. Acknowledged as a heuristic, not a forecast; revisit after first quarter of live use.
- **Initial DHT / ECO / FRO crude builds**: NAV path (vessel value curves + balance sheet), dividend strip (8-quarter EPS → DPS → discounted), blended fair value, breakeven TCE, 5×5 sensitivity heatmap. Templated mode established with DHT as the methodology validator.

For older milestones, consult git history.

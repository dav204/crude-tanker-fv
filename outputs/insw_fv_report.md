# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (65.0% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $71.85 (= whole-company $110.60 × crude_share). Product sleeve (~35%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q2
- **Current price (crude-allocated):** $71.85
- **Model fair value:** $37.95
- **Analyst target (crude-allocated):** $51.64

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 689.9 |
| Fleet value — Suezmax | 776.3 |
| Fleet value — Aframax | 175.5 |
| Fleet value — LR1 | 102.2 |
| + Cash & equivalents | 265.9 |
| + Working capital (net) | 183.6 |
| − Total debt | 365.4 |
| − Lease liabilities | 4.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,823.5** |
| Diluted shares | 49,857,565 |
| **NAV / share** | **$36.57** |
| NAV / share (ex yard discount) | $37.44 |
| Yard-discount impact / share | $-0.86 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 117,600 | 117,600 | 4.903 | 3.552 | 3.460 |
| Q2 | 117,600 | 117,600 | 4.903 | 3.552 | 3.371 |
| Q3 | 74,500 | 74,500 | 3.013 | 2.229 | 2.062 |
| Q4 | 74,500 | 74,500 | 3.013 | 2.229 | 2.008 |
| Q5 | 30,400 | 30,400 | 1.184 | 0.949 | 0.833 |
| Q6 | 30,400 | 30,400 | 1.184 | 0.949 | 0.811 |
| Q7 | 30,400 | 30,400 | 1.184 | 0.949 | 0.790 |
| Q8 | 30,400 | 30,400 | 1.184 | 0.949 | 0.770 |
| Σ discounted DPS | | | | | 14.11 |
| Terminal value (NAV, q9) | | | | 34.19 | 27.04 |
| **DivStrip implied price** | | | | | **$41.14** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$96,050/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$74,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $74,500 / 10-yr mean $27,747 = **2.51×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $36.57 (NAV) + 0.30 × $41.14 (strip) = **$37.95**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 24.49 | 65% |
| Balance-sheet net | 1.12 | 3% |
| Discounted DPS (strip, 8-10q) | 4.23 | 11% |
| Discounted terminal (aged NAV) | 8.11 | 21% |
| **Blend FV** | **37.95** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.66 = **90%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $38.03 |
| 95% | $38.15 |
| 100% | $38.19 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.99× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **629,961** | — |
| 10-year mean | 33,465 | 18.82× |
| 12-month FFA | 105,192 | 5.99× |
| Current spot | 235,542 | 2.67× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (45% of fleet value) | 575,212 | 20.73× |
| VLCC (40% of fleet value) | 780,025 | 19.50× |
| Aframax (10% of fleet value) | 410,224 | 11.24× |
| LR1 (6% of fleet value) | 410,224 | 14.86× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $29.71 | $32.81 | $35.91 | $39.01 | $42.10 |
| **-15%** | $30.73 | $33.83 | $36.93 | $40.02 | $43.12 |
| **+0%** | $31.75 | $34.85 | $37.95 | $41.04 | $44.14 |
| **+15%** | $32.77 | $35.87 | $38.96 | $42.06 | $45.16 |
| **+30%** | $33.79 | $36.89 | $39.98 | $43.08 | $46.18 |

_Current price $71.85. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$37.95** is -47.2% vs the current price ($71.85) and -26.5% vs the analyst target ($51.64). The current price implies the fleet earning a value-weighted blended **$629,961/day** (5.99× the current forward) — 18.8× the value-weighted 10-yr mean ($33,465, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 65.0% of vessel value ($1,744M crude vs $941M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -47% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~35% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.

# BRUT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $4.94
- **Model fair value:** $4.70
- **Analyst target:** $4.56

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 691.7 |
| + Cash & equivalents | 11.8 |
| + Working capital (net) | -0.7 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 398.1 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **304.7** |
| Diluted shares | 61,923,808 |
| **NAV / share** | **$4.92** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 179,650 | 0.187 | 0.000 | 0.000 |
| Q2 | 179,650 | 179,650 | 0.435 | 0.000 | 0.000 |
| Q3 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q4 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q5 | 48,850 | 48,850 | 0.116 | 0.000 | 0.000 |
| Q6 | 48,850 | 48,850 | 0.174 | 0.000 | 0.000 |
| Q7 | 48,850 | 48,850 | 0.174 | 0.000 | 0.000 |
| Q8 | 48,850 | 48,850 | 0.174 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 5.29 | 4.18 |
| **DivStrip implied price** | | | | | **$4.18** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.64×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $4.92 (NAV) + 0.30 × $4.18 (strip) = **$4.70**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 7.82 | 166% |
| Balance-sheet net | -4.37 | -93% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 1.25 | 27% |
| **Blend FV** | **4.70** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $4.74 |
| 95% | $4.75 |
| 100% | $4.76 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.42× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **203,062** | — |
| 10-year mean | 40,000 | 5.08× |
| 12-month FFA | 142,675 | 1.42× |
| Current spot | 488,900 | 0.42× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.49 | $3.51 | $4.52 | $5.54 | $6.55 |
| **-15%** | $2.58 | $3.60 | $4.61 | $5.63 | $6.64 |
| **+0%** | $2.67 | $3.68 | $4.70 | $5.71 | $6.73 |
| **+15%** | $2.76 | $3.77 | $4.79 | $5.80 | $6.82 |
| **+30%** | $2.84 | $3.86 | $4.87 | $5.89 | $6.90 |

_Current price $4.94. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$4.70** is -5.0% vs the current price ($4.94) and +3.0% vs the analyst target ($4.56). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$203,062/day** (1.42× the current forward) — 5.1× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

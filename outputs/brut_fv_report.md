# BRUT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $5.00
- **Model fair value:** $4.71
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
| Q1 | 154,800 | 154,800 | 0.151 | 0.000 | 0.000 |
| Q2 | 154,800 | 154,800 | 0.363 | 0.000 | 0.000 |
| Q3 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q4 | 105,700 | 105,700 | 0.221 | 0.000 | 0.000 |
| Q5 | 55,050 | 55,050 | 0.143 | 0.000 | 0.000 |
| Q6 | 55,050 | 55,050 | 0.210 | 0.000 | 0.000 |
| Q7 | 55,050 | 55,050 | 0.210 | 0.000 | 0.000 |
| Q8 | 55,050 | 55,050 | 0.210 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 5.31 | 4.20 |
| **DivStrip implied price** | | | | | **$4.20** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$130,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.64×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $4.92 (NAV) + 0.30 × $4.20 (strip) = **$4.71**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 7.82 | 166% |
| Balance-sheet net | -4.37 | -93% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 1.26 | 27% |
| **Blend FV** | **4.71** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $4.75 |
| 95% | $4.76 |
| 100% | $4.76 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.51× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **196,633** | — |
| 10-year mean | 40,000 | 4.92× |
| 12-month FFA | 130,250 | 1.51× |
| Current spot | 488,900 | 0.40× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.50 | $3.51 | $4.53 | $5.54 | $6.56 |
| **-15%** | $2.59 | $3.60 | $4.62 | $5.63 | $6.65 |
| **+0%** | $2.68 | $3.69 | $4.71 | $5.72 | $6.74 |
| **+15%** | $2.76 | $3.78 | $4.79 | $5.81 | $6.82 |
| **+30%** | $2.85 | $3.87 | $4.88 | $5.90 | $6.91 |

_Current price $5.00. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$4.71** is -6.0% vs the current price ($5.00) and +3.2% vs the analyst target ($4.56). The current price implies the fleet earning a value-weighted blended **$196,633/day** (1.51× the current forward) — 4.9× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

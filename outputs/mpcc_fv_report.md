# MPCC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $2.85
- **Model fair value:** $2.29
- **Analyst target:** $2.63

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Intermediate | 1,060.7 |
| Fleet value — Ctr-Feeder | 408.3 |
| + Cash & equivalents | 314.1 |
| + Working capital (net) | 100.8 |
| − Total debt | 436.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 631.7 |
| + Newbuild advances | 118.1 |
| **= NAV total** | **933.5** |
| Diluted shares | 443,700,279 |
| **NAV / share** | **$2.10** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Intermediate, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 46,350 | 26,532 | 0.130 | 0.065 | 0.063 |
| Q2 | 45,325 | 26,532 | 0.127 | 0.063 | 0.060 |
| Q3 | 44,325 | 27,137 | 0.137 | 0.069 | 0.063 |
| Q4 | 43,300 | 28,846 | 0.155 | 0.078 | 0.070 |
| Q5 | 42,275 | 29,161 | 0.166 | 0.083 | 0.073 |
| Q6 | 41,275 | 29,864 | 0.179 | 0.089 | 0.076 |
| Q7 | 40,250 | 29,852 | 0.187 | 0.093 | 0.078 |
| Q8 | 39,225 | 30,517 | 0.199 | 0.100 | 0.081 |
| Q9 | 38,225 | 30,636 | 0.199 | 0.099 | 0.079 |
| Q10 | 37,200 | 32,549 | 0.212 | 0.106 | 0.082 |
| Σ discounted DPS | | | | | 0.72 |
| Terminal value (NAV, q9) | | | | 2.45 | 1.84 |
| **DivStrip implied price** | | | | | **$2.56** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$44,825/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$46,350/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $46,350 / 10-yr mean $33,700 = **1.32×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.10 (NAV) + 0.40 × $2.56 (strip) = **$2.29**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 1.99 | 87% |
| Balance-sheet net | -0.72 | -32% |
| Discounted DPS (strip, 8-10q) | 0.29 | 13% |
| Discounted terminal (aged NAV) | 0.73 | 32% |
| **Blend FV** | **2.29** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.24 |
| 95% | $2.25 |
| 100% | $2.25 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.95× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **192,190** | — |
| 10-year mean | 30,129 | 6.38× |
| 12-month FFA | 38,863 | 4.95× |
| Current spot | 40,208 | 4.78× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (72% of fleet value) | 221,671 | 6.58× |
| Ctr-Feeder (28% of fleet value) | 115,595 | 5.54× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.60 | $1.89 | $2.18 | $2.47 | $2.76 |
| **-15%** | $1.62 | $1.91 | $2.20 | $2.49 | $2.78 |
| **+0%** | $1.65 | $1.94 | $2.23 | $2.52 | $2.81 |
| **+15%** | $1.67 | $1.96 | $2.25 | $2.54 | $2.83 |
| **+30%** | $1.69 | $1.98 | $2.27 | $2.56 | $2.86 |

_Current price $2.85. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.29** is -19.9% vs the current price ($2.85) and -13.0% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$192,190/day** (4.95× the current forward) — 6.4× the value-weighted 10-yr mean ($30,129, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

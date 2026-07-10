# MPCC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $2.49
- **Model fair value:** $2.21
- **Analyst target:** $2.63

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Feeder | 440.8 |
| Fleet value — Ctr-Intermediate | 1,093.3 |
| + Cash & equivalents | 269.3 |
| + Working capital (net) | 85.9 |
| − Total debt | 462.9 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 633.7 |
| + Newbuild advances | 112.9 |
| **= NAV total** | **905.6** |
| Diluted shares | 443,700,279 |
| **NAV / share** | **$2.04** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Intermediate, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 46,350 | 26,404 | 0.129 | 0.064 | 0.063 |
| Q2 | 45,325 | 26,404 | 0.131 | 0.066 | 0.062 |
| Q3 | 44,325 | 27,014 | 0.135 | 0.068 | 0.063 |
| Q4 | 43,300 | 28,736 | 0.146 | 0.073 | 0.066 |
| Q5 | 42,275 | 29,055 | 0.155 | 0.077 | 0.068 |
| Q6 | 41,275 | 29,765 | 0.166 | 0.083 | 0.071 |
| Q7 | 40,250 | 29,755 | 0.174 | 0.087 | 0.072 |
| Q8 | 39,225 | 30,430 | 0.186 | 0.093 | 0.075 |
| Q9 | 38,225 | 30,553 | 0.194 | 0.097 | 0.077 |
| Q10 | 37,200 | 32,493 | 0.217 | 0.108 | 0.084 |
| Σ discounted DPS | | | | | 0.70 |
| Terminal value (NAV, q9) | | | | 2.35 | 1.76 |
| **DivStrip implied price** | | | | | **$2.46** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$44,825/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$46,350/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $46,350 / 10-yr mean $33,700 = **1.31×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.04 (NAV) + 0.40 × $2.46 (strip) = **$2.21**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.16 |
| 95% | $2.17 |
| 100% | $2.17 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.24× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **124,928** | — |
| 10-year mean | 30,008 | 4.16× |
| 12-month FFA | 38,554 | 3.24× |
| Current spot | 39,856 | 3.13× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (71% of fleet value) | 145,249 | 4.31× |
| Ctr-Feeder (29% of fleet value) | 74,528 | 3.57× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.50 | $1.80 | $2.10 | $2.41 | $2.71 |
| **-15%** | $1.52 | $1.82 | $2.13 | $2.43 | $2.73 |
| **+0%** | $1.54 | $1.85 | $2.15 | $2.45 | $2.76 |
| **+15%** | $1.56 | $1.87 | $2.17 | $2.48 | $2.78 |
| **+30%** | $1.59 | $1.89 | $2.20 | $2.50 | $2.80 |

_Current price $2.49. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.21** is -11.3% vs the current price ($2.49) and -16.0% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$124,928/day** (3.24× the current forward) — 4.2× the value-weighted 10-yr mean ($30,008, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

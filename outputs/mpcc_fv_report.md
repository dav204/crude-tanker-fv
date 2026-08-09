# MPCC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $2.56
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
| Q5 | 42,275 | 29,055 | 0.155 | 0.078 | 0.068 |
| Q6 | 41,275 | 29,765 | 0.166 | 0.083 | 0.071 |
| Q7 | 40,250 | 29,755 | 0.174 | 0.087 | 0.073 |
| Q8 | 39,225 | 30,430 | 0.186 | 0.093 | 0.076 |
| Q9 | 38,225 | 30,553 | 0.194 | 0.097 | 0.077 |
| Q10 | 37,200 | 32,493 | 0.217 | 0.108 | 0.084 |
| Σ discounted DPS | | | | | 0.70 |
| Terminal value (NAV, q9) | | | | 2.35 | 1.76 |
| **DivStrip implied price** | | | | | **$2.46** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$44,825/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$46,350/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $46,350 / 10-yr mean $33,700 = **1.32×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.04 (NAV) + 0.40 × $2.46 (strip) = **$2.21**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.07 | 94% |
| Balance-sheet net | -0.85 | -38% |
| Discounted DPS (strip, 8-10q) | 0.28 | 13% |
| Discounted terminal (aged NAV) | 0.71 | 32% |
| **Blend FV** | **2.21** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.16 |
| 95% | $2.17 |
| 100% | $2.17 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.66× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **141,591** | — |
| 10-year mean | 30,008 | 4.72× |
| 12-month FFA | 38,662 | 3.66× |
| Current spot | 40,000 | 3.54× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (71% of fleet value) | 164,163 | 4.87× |
| Ctr-Feeder (29% of fleet value) | 85,606 | 4.11× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.50 | $1.80 | $2.10 | $2.41 | $2.71 |
| **-15%** | $1.52 | $1.82 | $2.13 | $2.43 | $2.74 |
| **+0%** | $1.54 | $1.85 | $2.15 | $2.45 | $2.76 |
| **+15%** | $1.57 | $1.87 | $2.17 | $2.48 | $2.78 |
| **+30%** | $1.59 | $1.89 | $2.20 | $2.50 | $2.80 |

_Current price $2.56. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.21** is -13.5% vs the current price ($2.56) and -16.0% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$141,591/day** (3.66× the current forward) — 4.7× the value-weighted 10-yr mean ($30,008, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

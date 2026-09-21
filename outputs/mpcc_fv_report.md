# MPCC — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $3.03
- **Model fair value:** $2.33
- **Analyst target:** $2.63

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Intermediate | 1,067.0 |
| Fleet value — Ctr-Feeder | 423.3 |
| + Cash & equivalents | 314.1 |
| + Working capital (net) | 100.8 |
| − Total debt | 436.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 631.7 |
| + Newbuild advances | 118.1 |
| **= NAV total** | **954.8** |
| Diluted shares | 443,700,279 |
| **NAV / share** | **$2.15** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Intermediate, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 47,567 | 26,532 | 0.130 | 0.065 | 0.063 |
| Q2 | 46,425 | 26,532 | 0.127 | 0.063 | 0.060 |
| Q3 | 45,275 | 27,169 | 0.138 | 0.069 | 0.064 |
| Q4 | 44,100 | 28,956 | 0.156 | 0.078 | 0.070 |
| Q5 | 42,950 | 29,274 | 0.167 | 0.084 | 0.073 |
| Q6 | 41,800 | 29,982 | 0.180 | 0.090 | 0.077 |
| Q7 | 40,650 | 29,948 | 0.188 | 0.094 | 0.078 |
| Q8 | 39,500 | 30,604 | 0.201 | 0.100 | 0.081 |
| Q9 | 38,350 | 30,680 | 0.200 | 0.100 | 0.079 |
| Q10 | 37,200 | 32,549 | 0.212 | 0.106 | 0.082 |
| Σ discounted DPS | | | | | 0.73 |
| Terminal value (NAV, q9) | | | | 2.49 | 1.87 |
| **DivStrip implied price** | | | | | **$2.60** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$45,842/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$47,567/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $47,567 / 10-yr mean $33,700 = **1.36×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.15 (NAV) + 0.40 × $2.60 (strip) = **$2.33**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.02 | 87% |
| Balance-sheet net | -0.72 | -31% |
| Discounted DPS (strip, 8-10q) | 0.29 | 13% |
| Discounted terminal (aged NAV) | 0.75 | 32% |
| **Blend FV** | **2.33** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.28 |
| 95% | $2.29 |
| 100% | $2.29 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.71× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **226,840** | — |
| 10-year mean | 30,050 | 7.55× |
| 12-month FFA | 39,744 | 5.71× |
| Current spot | 41,299 | 5.49× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (72% of fleet value) | 261,640 | 7.76× |
| Ctr-Feeder (28% of fleet value) | 139,120 | 6.67× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.63 | $1.93 | $2.22 | $2.52 | $2.81 |
| **-15%** | $1.66 | $1.95 | $2.25 | $2.54 | $2.84 |
| **+0%** | $1.68 | $1.98 | $2.27 | $2.56 | $2.86 |
| **+15%** | $1.71 | $2.00 | $2.29 | $2.59 | $2.88 |
| **+30%** | $1.73 | $2.02 | $2.32 | $2.61 | $2.91 |

_Current price $3.03. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.33** is -23.1% vs the current price ($3.03) and -11.4% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$226,840/day** (5.71× the current forward) — 7.5× the value-weighted 10-yr mean ($30,050, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

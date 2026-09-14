# NAT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $7.46
- **Model fair value:** $2.95
- **Analyst target:** $6.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 787.8 |
| + Cash & equivalents | 133.3 |
| + Working capital (net) | 44.9 |
| − Total debt | 406.6 |
| − Lease liabilities | 0.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **585.1** |
| Diluted shares | 211,750,663 |
| **NAV / share** | **$2.76** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 117,600 | 94,600 | 0.511 | 0.511 | 0.498 |
| Q2 | 117,600 | 94,600 | 0.511 | 0.511 | 0.485 |
| Q3 | 74,500 | 64,969 | 0.315 | 0.315 | 0.291 |
| Q4 | 74,500 | 64,969 | 0.315 | 0.315 | 0.284 |
| Q5 | 30,400 | 34,650 | 0.114 | 0.114 | 0.100 |
| Q6 | 30,400 | 34,650 | 0.114 | 0.114 | 0.098 |
| Q7 | 30,400 | 34,650 | 0.114 | 0.114 | 0.095 |
| Q8 | 30,400 | 34,650 | 0.114 | 0.114 | 0.093 |
| Σ discounted DPS | | | | | 1.94 |
| Terminal value (NAV, q9) | | | | 1.80 | 1.43 |
| **DivStrip implied price** | | | | | **$3.37** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$96,050/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$74,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $74,500 / 10-yr mean $27,747 = **2.68×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.76 (NAV) + 0.30 × $3.37 (strip) = **$2.95**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.60 | 88% |
| Balance-sheet net | -0.67 | -23% |
| Discounted DPS (strip, 8-10q) | 0.58 | 20% |
| Discounted terminal (aged NAV) | 0.43 | 15% |
| **Blend FV** | **2.95** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.42 = **83%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.93 |
| 95% | $2.94 |
| 100% | $2.95 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **8.11× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **778,983** | — |
| 10-year mean | 27,747 | 28.07× |
| 12-month FFA | 96,050 | 8.11× |
| Current spot | 77,600 | 10.04× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.10 | $2.43 | $2.76 | $3.08 | $3.41 |
| **-15%** | $2.20 | $2.52 | $2.85 | $3.18 | $3.50 |
| **+0%** | $2.29 | $2.62 | $2.95 | $3.27 | $3.60 |
| **+15%** | $2.39 | $2.72 | $3.04 | $3.37 | $3.69 |
| **+30%** | $2.48 | $2.81 | $3.14 | $3.46 | $3.79 |

_Current price $7.46. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.95** is -60.5% vs the current price ($7.46) and -50.9% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$778,983/day** (8.11× the current forward) — 28.1× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

# NAT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $6.77
- **Model fair value:** $2.89
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
| Q1 | 118,900 | 95,494 | 0.517 | 0.517 | 0.504 |
| Q2 | 118,900 | 95,494 | 0.517 | 0.517 | 0.491 |
| Q3 | 58,050 | 53,659 | 0.240 | 0.240 | 0.222 |
| Q4 | 58,050 | 53,659 | 0.240 | 0.240 | 0.216 |
| Q5 | 26,950 | 32,278 | 0.099 | 0.099 | 0.087 |
| Q6 | 26,950 | 32,278 | 0.099 | 0.099 | 0.084 |
| Q7 | 26,950 | 32,278 | 0.099 | 0.099 | 0.082 |
| Q8 | 26,950 | 32,278 | 0.099 | 0.099 | 0.080 |
| Σ discounted DPS | | | | | 1.77 |
| Terminal value (NAV, q9) | | | | 1.80 | 1.43 |
| **DivStrip implied price** | | | | | **$3.19** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$88,475/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$58,050/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $58,050 / 10-yr mean $27,747 = **2.09×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $2.76 (NAV) + 0.30 × $3.19 (strip) = **$2.89**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 2.60 | 90% |
| Balance-sheet net | -0.67 | -23% |
| Discounted DPS (strip, 8-10q) | 0.53 | 18% |
| Discounted terminal (aged NAV) | 0.43 | 15% |
| **Blend FV** | **2.89** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.45 = **83%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.88 |
| 95% | $2.89 |
| 100% | $2.89 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **7.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **678,594** | — |
| 10-year mean | 27,747 | 24.46× |
| 12-month FFA | 88,475 | 7.67× |
| Current spot | 77,600 | 8.74× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $2.07 | $2.39 | $2.72 | $3.04 | $3.37 |
| **-15%** | $2.15 | $2.48 | $2.80 | $3.13 | $3.46 |
| **+0%** | $2.24 | $2.57 | $2.89 | $3.22 | $3.54 |
| **+15%** | $2.33 | $2.65 | $2.98 | $3.31 | $3.63 |
| **+30%** | $2.41 | $2.74 | $3.07 | $3.39 | $3.72 |

_Current price $6.77. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.89** is -57.3% vs the current price ($6.77) and -51.8% vs the analyst target ($6.00). The current price implies the fleet earning a value-weighted blended **$678,594/day** (7.67× the current forward) — 24.5× the value-weighted 10-yr mean ($27,747, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

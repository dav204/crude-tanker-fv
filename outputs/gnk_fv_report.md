# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $25.33
- **Model fair value:** $24.83
- **Analyst target:** $24.80

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 915.1 |
| Fleet value — Supra-Ultra | 518.7 |
| + Cash & equivalents | 73.6 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.7 |
| − Newbuild commitments | 57.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,131.1** |
| Diluted shares | 44,572,591 |
| **NAV / share** | **$25.38** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 38,800 | 38,685 | 1.509 | 1.509 | 1.470 |
| Q2 | 37,250 | 37,212 | 1.449 | 1.449 | 1.375 |
| Q3 | 25,875 | 26,406 | 0.921 | 0.921 | 0.852 |
| Q4 | 31,225 | 31,489 | 1.111 | 1.111 | 1.001 |
| Q5 | 31,250 | 31,512 | 1.098 | 1.098 | 0.964 |
| Q6 | 31,250 | 31,512 | 1.084 | 1.084 | 0.927 |
| Q7 | 30,750 | 31,038 | 1.058 | 1.058 | 0.881 |
| Q8 | 30,250 | 30,562 | 1.032 | 1.032 | 0.838 |
| Σ discounted DPS | | | | | 8.31 |
| Terminal value (NAV, q9) | | | | 19.86 | 15.71 |
| **DivStrip implied price** | | | | | **$24.01** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$33,288/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$31,550/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $31,550 / 10-yr mean $23,650 = **1.29×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.38 (NAV) + 0.40 × $24.01 (strip) = **$24.83**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.30 | 78% |
| Balance-sheet net | -4.08 | -16% |
| Discounted DPS (strip, 8-10q) | 3.32 | 13% |
| Discounted terminal (aged NAV) | 6.28 | 25% |
| **Blend FV** | **24.83** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.65 = **86%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.75 |
| 95% | $24.81 |
| 100% | $24.83 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.11× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **30,423** | — |
| 10-year mean | 20,134 | 1.51× |
| 12-month FFA | 27,387 | 1.11× |
| Current spot | 32,160 | 0.95× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 36,978 | 1.56× |
| Supra-Ultra (36% of fleet value) | 18,859 | 1.35× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.93 | $20.71 | $23.48 | $26.25 | $29.03 |
| **-15%** | $18.61 | $21.38 | $24.16 | $26.93 | $29.70 |
| **+0%** | $19.28 | $22.06 | $24.83 | $27.60 | $30.38 |
| **+15%** | $19.96 | $22.73 | $25.51 | $28.28 | $31.05 |
| **+30%** | $20.64 | $23.41 | $26.18 | $28.95 | $31.73 |

_Current price $25.33. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$24.83** is -2.0% vs the current price ($25.33) and +0.1% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$30,423/day** (1.11× the current forward) — 1.5× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

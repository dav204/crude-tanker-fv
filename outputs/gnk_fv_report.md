# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $25.33
- **Model fair value:** $24.62
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
| Q1 | 34,900 | 34,980 | 1.358 | 1.358 | 1.323 |
| Q2 | 35,725 | 35,764 | 1.374 | 1.374 | 1.304 |
| Q3 | 30,675 | 30,966 | 1.104 | 1.104 | 1.021 |
| Q4 | 29,675 | 30,016 | 1.052 | 1.052 | 0.948 |
| Q5 | 28,675 | 29,066 | 1.000 | 1.000 | 0.878 |
| Q6 | 27,675 | 28,116 | 0.948 | 0.948 | 0.810 |
| Q7 | 27,175 | 27,641 | 0.922 | 0.922 | 0.768 |
| Q8 | 26,675 | 27,166 | 0.896 | 0.896 | 0.727 |
| Σ discounted DPS | | | | | 7.78 |
| Terminal value (NAV, q9) | | | | 19.86 | 15.71 |
| **DivStrip implied price** | | | | | **$23.48** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.44×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.38 (NAV) + 0.40 × $23.48 (strip) = **$24.62**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.30 | 78% |
| Balance-sheet net | -4.08 | -17% |
| Discounted DPS (strip, 8-10q) | 3.11 | 13% |
| Discounted terminal (aged NAV) | 6.28 | 26% |
| **Blend FV** | **24.62** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.67 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.54 |
| 95% | $24.60 |
| 100% | $24.62 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.17× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **31,433** | — |
| 10-year mean | 20,134 | 1.56× |
| 12-month FFA | 26,967 | 1.17× |
| Current spot | 29,486 | 1.07× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 38,166 | 1.61× |
| Supra-Ultra (36% of fleet value) | 19,553 | 1.40× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $17.79 | $20.56 | $23.33 | $26.11 | $28.88 |
| **-15%** | $18.43 | $21.20 | $23.98 | $26.75 | $29.52 |
| **+0%** | $19.07 | $21.85 | $24.62 | $27.39 | $30.17 |
| **+15%** | $19.72 | $22.49 | $25.26 | $28.04 | $30.81 |
| **+30%** | $20.36 | $23.13 | $25.91 | $28.68 | $31.45 |

_Current price $25.33. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$24.62** is -2.8% vs the current price ($25.33) and -0.7% vs the analyst target ($24.80). Tool, market, and analyst are in broad agreement (all within ~5%). The current price implies the fleet earning a value-weighted blended **$31,433/day** (1.17× the current forward) — 1.6× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

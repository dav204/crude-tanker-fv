# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $25.88
- **Model fair value:** $25.42
- **Analyst target:** $27.20

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 915.1 |
| Fleet value — Supra-Ultra | 518.6 |
| + Cash & equivalents | 73.6 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.7 |
| − Newbuild commitments | 57.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,131.0** |
| Diluted shares | 44,572,591 |
| **NAV / share** | **$25.37** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 45,250 | 44,812 | 1.770 | 1.770 | 1.725 |
| Q2 | 44,475 | 44,076 | 1.765 | 1.765 | 1.675 |
| Q3 | 30,125 | 30,444 | 1.104 | 1.104 | 1.021 |
| Q4 | 34,359 | 34,466 | 1.269 | 1.269 | 1.144 |
| Q5 | 34,358 | 34,465 | 1.269 | 1.269 | 1.114 |
| Q6 | 34,358 | 34,465 | 1.269 | 1.269 | 1.085 |
| Q7 | 33,858 | 33,990 | 1.243 | 1.243 | 1.036 |
| Q8 | 33,358 | 33,515 | 1.217 | 1.217 | 0.988 |
| Σ discounted DPS | | | | | 9.79 |
| Terminal value (NAV, q9) | | | | 19.86 | 15.71 |
| **DivStrip implied price** | | | | | **$25.49** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$38,552/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$37,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $37,300 / 10-yr mean $23,650 = **1.49×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.37 (NAV) + 0.40 × $25.49 (strip) = **$25.42**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.30 | 76% |
| Balance-sheet net | -4.08 | -16% |
| Discounted DPS (strip, 8-10q) | 3.92 | 15% |
| Discounted terminal (aged NAV) | 6.28 | 25% |
| **Blend FV** | **25.42** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.62 = **85%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.33 |
| 95% | $25.40 |
| 100% | $25.42 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.09× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **34,013** | — |
| 10-year mean | 20,134 | 1.69× |
| 12-month FFA | 31,206 | 1.09× |
| Current spot | 34,360 | 0.99× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 42,020 | 1.78× |
| Supra-Ultra (36% of fleet value) | 19,885 | 1.43× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.35 | $21.12 | $23.89 | $26.67 | $29.44 |
| **-15%** | $19.11 | $21.88 | $24.66 | $27.43 | $30.20 |
| **+0%** | $19.88 | $22.65 | $25.42 | $28.19 | $30.97 |
| **+15%** | $20.64 | $23.41 | $26.19 | $28.96 | $31.73 |
| **+30%** | $21.40 | $24.18 | $26.95 | $29.72 | $32.50 |

_Current price $25.88. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.42** is -1.8% vs the current price ($25.88) and -6.5% vs the analyst target ($27.20). The current price implies the fleet earning a value-weighted blended **$34,013/day** (1.09× the current forward) — 1.7× the value-weighted 10-yr mean ($20,134, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

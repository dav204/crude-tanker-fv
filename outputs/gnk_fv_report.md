# GNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $25.88
- **Model fair value:** $25.02
- **Analyst target:** $27.20

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 915.1 |
| Fleet value — Supra-Ultra | 507.2 |
| + Cash & equivalents | 73.6 |
| + Working capital (net) | 16.8 |
| − Total debt | 330.0 |
| − Lease liabilities | 5.7 |
| − Newbuild commitments | 57.5 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,119.6** |
| Diluted shares | 44,572,591 |
| **NAV / share** | **$25.12** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 41,313 | 41,072 | 1.610 | 1.610 | 1.569 |
| Q2 | 42,125 | 41,844 | 1.660 | 1.660 | 1.576 |
| Q3 | 28,725 | 29,114 | 1.031 | 1.031 | 0.954 |
| Q4 | 33,625 | 33,769 | 1.235 | 1.235 | 1.113 |
| Q5 | 33,625 | 33,769 | 1.235 | 1.235 | 1.084 |
| Q6 | 33,625 | 33,769 | 1.235 | 1.235 | 1.056 |
| Q7 | 33,125 | 33,294 | 1.209 | 1.209 | 1.007 |
| Q8 | 32,625 | 32,819 | 1.183 | 1.183 | 0.960 |
| Σ discounted DPS | | | | | 9.32 |
| Terminal value (NAV, q9) | | | | 19.66 | 15.55 |
| **DivStrip implied price** | | | | | **$24.87** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$36,447/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,425/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,425 / 10-yr mean $23,650 = **1.42×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $25.12 (NAV) + 0.40 × $24.87 (strip) = **$25.02**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 19.15 | 77% |
| Balance-sheet net | -4.08 | -16% |
| Discounted DPS (strip, 8-10q) | 3.73 | 15% |
| Discounted terminal (aged NAV) | 6.22 | 25% |
| **Blend FV** | **25.02** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.63 = **85%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $24.93 |
| 95% | $25.00 |
| 100% | $25.02 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.18× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **34,989** | — |
| 10-year mean | 20,184 | 1.73× |
| 12-month FFA | 29,758 | 1.18× |
| Current spot | 34,472 | 1.01× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (64% of fleet value) | 42,854 | 1.81× |
| Supra-Ultra (36% of fleet value) | 20,799 | 1.49× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.04 | $20.79 | $23.55 | $26.30 | $29.05 |
| **-15%** | $18.78 | $21.53 | $24.28 | $27.03 | $29.78 |
| **+0%** | $19.51 | $22.27 | $25.02 | $27.77 | $30.52 |
| **+15%** | $20.25 | $23.00 | $25.75 | $28.50 | $31.26 |
| **+30%** | $20.99 | $23.74 | $26.49 | $29.24 | $31.99 |

_Current price $25.88. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.02** is -3.3% vs the current price ($25.88) and -8.0% vs the analyst target ($27.20). The current price implies the fleet earning a value-weighted blended **$34,989/day** (1.18× the current forward) — 1.7× the value-weighted 10-yr mean ($20,184, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $28.90
- **Model fair value:** $31.84
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.8 |
| Fleet value — Pana | 1,389.0 |
| Fleet value — Supra-Ultra | 1,391.3 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,686.6** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$33.04** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 34,900 | 34,900 | 1.655 | 1.572 | 1.531 |
| Q2 | 35,725 | 35,725 | 1.643 | 1.561 | 1.481 |
| Q3 | 30,675 | 30,675 | 1.289 | 1.225 | 1.133 |
| Q4 | 29,675 | 29,675 | 1.213 | 1.152 | 1.038 |
| Q5 | 28,675 | 28,675 | 1.136 | 1.079 | 0.947 |
| Q6 | 27,675 | 27,675 | 1.059 | 1.006 | 0.860 |
| Q7 | 27,175 | 27,175 | 1.017 | 0.966 | 0.805 |
| Q8 | 26,675 | 26,675 | 0.978 | 0.929 | 0.754 |
| Σ discounted DPS | | | | | 8.55 |
| Terminal value (NAV, q9) | | | | 27.17 | 21.49 |
| **DivStrip implied price** | | | | | **$30.03** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.48×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $33.04 (NAV) + 0.40 × $30.03 (strip) = **$31.84**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 23.33 | 73% |
| Balance-sheet net | -3.50 | -11% |
| Discounted DPS (strip, 8-10q) | 3.42 | 11% |
| Discounted terminal (aged NAV) | 8.59 | 27% |
| **Blend FV** | **31.84** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.72 = **89%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $31.77 |
| 95% | $31.84 |
| 100% | $31.86 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.51× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **11,773** | — |
| 10-year mean | 16,771 | 0.70× |
| 12-month FFA | 22,926 | 0.51× |
| Current spot | 25,145 | 0.47× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 16,815 | 0.71× |
| Supra-Ultra (32% of fleet value) | 8,614 | 0.62× |
| Pana (32% of fleet value) | 9,282 | 0.78× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $23.30 | $26.66 | $30.03 | $33.39 | $36.75 |
| **-15%** | $24.21 | $27.57 | $30.93 | $34.29 | $37.65 |
| **+0%** | $25.12 | $28.48 | $31.84 | $35.20 | $38.56 |
| **+15%** | $26.02 | $29.38 | $32.74 | $36.10 | $39.46 |
| **+30%** | $26.93 | $30.29 | $33.65 | $37.01 | $40.37 |

_Current price $28.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$31.84** is +10.2% vs the current price ($28.90) and -7.7% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$11,773/day** (0.51× the current forward) — 0.7× the value-weighted 10-yr mean ($16,771, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

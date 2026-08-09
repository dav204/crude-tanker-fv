# SBLK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $28.90
- **Model fair value:** $31.28
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,548.8 |
| Fleet value — Pana | 1,328.1 |
| Fleet value — Supra-Ultra | 1,389.1 |
| + Cash & equivalents | 565.3 |
| + Working capital (net) | 84.2 |
| − Total debt | 1,036.6 |
| − Lease liabilities | 142.4 |
| − Newbuild commitments | 122.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,614.5** |
| Diluted shares | 111,585,370 |
| **NAV / share** | **$32.39** |

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
| Terminal value (NAV, q9) | | | | 26.63 | 21.05 |
| **DivStrip implied price** | | | | | **$29.60** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,744/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.48×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $32.39 (NAV) + 0.40 × $29.60 (strip) = **$31.28**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.94 | 73% |
| Balance-sheet net | -3.50 | -11% |
| Discounted DPS (strip, 8-10q) | 3.42 | 11% |
| Discounted terminal (aged NAV) | 8.42 | 27% |
| **Blend FV** | **31.28** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.71 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $31.21 |
| 95% | $31.28 |
| 100% | $31.30 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.61× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **13,931** | — |
| 10-year mean | 16,827 | 0.83× |
| 12-month FFA | 22,977 | 0.61× |
| Current spot | 25,206 | 0.55× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 19,852 | 0.84× |
| Supra-Ultra (33% of fleet value) | 10,170 | 0.73× |
| Pana (31% of fleet value) | 10,959 | 0.92× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $22.86 | $26.16 | $29.47 | $32.77 | $36.08 |
| **-15%** | $23.76 | $27.07 | $30.37 | $33.68 | $36.98 |
| **+0%** | $24.67 | $27.97 | $31.28 | $34.58 | $37.89 |
| **+15%** | $25.57 | $28.88 | $32.18 | $35.49 | $38.79 |
| **+30%** | $26.48 | $29.78 | $33.09 | $36.39 | $39.70 |

_Current price $28.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$31.28** is +8.2% vs the current price ($28.90) and -9.3% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$13,931/day** (0.61× the current forward) — 0.8× the value-weighted 10-yr mean ($16,827, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

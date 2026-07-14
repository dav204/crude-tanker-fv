# ASC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $15.83
- **Model fair value:** $16.75
- **Analyst target:** $17.95

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 580.6 |
| Fleet value — Handysize | 49.1 |
| + Cash & equivalents | 47.2 |
| + Working capital (net) | 119.7 |
| − Total debt | 103.4 |
| − Lease liabilities | 1.7 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **727.1** |
| Diluted shares | 40,857,533 |
| **NAV / share** | **$17.80** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.435 | 0.290 | 0.283 |
| Q2 | 30,000 | 30,000 | 0.784 | 0.523 | 0.497 |
| Q3 | 28,000 | 28,000 | 0.697 | 0.465 | 0.430 |
| Q4 | 19,000 | 19,000 | 0.304 | 0.203 | 0.183 |
| Q5 | 18,000 | 18,000 | 0.261 | 0.174 | 0.153 |
| Q6 | 23,000 | 23,000 | 0.479 | 0.319 | 0.273 |
| Q7 | 26,000 | 26,000 | 0.610 | 0.407 | 0.339 |
| Q8 | 18,000 | 18,000 | 0.261 | 0.174 | 0.141 |
| Σ discounted DPS | | | | | 2.30 |
| Terminal value (NAV, q9) | | | | 16.30 | 12.89 |
| **DivStrip implied price** | | | | | **$15.19** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.38×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $17.80 (NAV) + 0.40 × $15.19 (strip) = **$16.75**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 9.25 | 55% |
| Balance-sheet net | 1.43 | 9% |
| Discounted DPS (strip, 8-10q) | 0.92 | 5% |
| Discounted terminal (aged NAV) | 5.16 | 31% |
| **Blend FV** | **16.75** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.85 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.77 |
| 95% | $16.80 |
| 100% | $16.81 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **16,487** | — |
| 10-year mean | 16,000 | 1.03× |
| 12-month FFA | 24,750 | 0.67× |
| Current spot | 35,600 | 0.46× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (92% of fleet value) | 16,487 | 1.03× |
| Handysize (8% of fleet value) | 16,487 | 1.03× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $13.27 | $14.60 | $15.92 | $17.25 | $18.57 |
| **-15%** | $13.69 | $15.01 | $16.34 | $17.66 | $18.99 |
| **+0%** | $14.10 | $15.43 | $16.75 | $18.08 | $19.40 |
| **+15%** | $14.52 | $15.84 | $17.17 | $18.49 | $19.82 |
| **+30%** | $14.93 | $16.26 | $17.58 | $18.91 | $20.23 |

_Current price $15.83. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$16.75** is +5.8% vs the current price ($15.83) and -6.7% vs the analyst target ($17.95). The current price implies the fleet earning a value-weighted blended **$16,487/day** (0.67× the current forward) — 1.0× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

# ASC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $15.40
- **Model fair value:** $16.77
- **Analyst target:** $17.95

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — MR | 581.5 |
| Fleet value — Handysize | 49.1 |
| + Cash & equivalents | 47.2 |
| + Working capital (net) | 119.7 |
| − Total debt | 103.4 |
| − Lease liabilities | 1.7 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **727.9** |
| Diluted shares | 40,857,533 |
| **NAV / share** | **$17.82** |

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
| Terminal value (NAV, q9) | | | | 16.32 | 12.91 |
| **DivStrip implied price** | | | | | **$15.20** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.38×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $17.82 (NAV) + 0.40 × $15.20 (strip) = **$16.77**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 9.26 | 55% |
| Balance-sheet net | 1.43 | 9% |
| Discounted DPS (strip, 8-10q) | 0.92 | 5% |
| Discounted terminal (aged NAV) | 5.16 | 31% |
| **Blend FV** | **16.77** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.85 = **94%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.79 |
| 95% | $16.82 |
| 100% | $16.83 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.50× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **12,385** | — |
| 10-year mean | 16,000 | 0.77× |
| 12-month FFA | 24,750 | 0.50× |
| Current spot | 35,600 | 0.35× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (92% of fleet value) | 12,385 | 0.77× |
| Handysize (8% of fleet value) | 12,385 | 0.77× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $13.29 | $14.62 | $15.94 | $17.27 | $18.60 |
| **-15%** | $13.70 | $15.03 | $16.36 | $17.68 | $19.01 |
| **+0%** | $14.12 | $15.44 | $16.77 | $18.10 | $19.42 |
| **+15%** | $14.53 | $15.86 | $17.19 | $18.51 | $19.84 |
| **+30%** | $14.95 | $16.27 | $17.60 | $18.93 | $20.25 |

_Current price $15.40. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$16.77** is +8.9% vs the current price ($15.40) and -6.6% vs the analyst target ($17.95). The current price implies the fleet earning a value-weighted blended **$12,385/day** (0.50× the current forward) — 0.8× the value-weighted 10-yr mean ($16,000, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

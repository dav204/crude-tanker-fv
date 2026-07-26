# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.84
- **Model fair value:** $21.01
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 218.9 |
| Fleet value — Pana | 141.4 |
| Fleet value — Supra-Ultra | 315.7 |
| + Cash & equivalents | 258.5 |
| + Working capital (net) | 3.8 |
| − Total debt | 141.4 |
| − Lease liabilities | 20.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **776.3** |
| Diluted shares | 24,180,472 |
| **NAV / share** | **$32.10** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 19,100 | 19,100 | 1.270 | 0.000 | 0.000 |
| Q2 | 18,450 | 18,450 | 1.248 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.890 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.817 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.744 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.671 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.632 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.595 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 23.81 | 18.83 |
| **DivStrip implied price** | | | | | **$18.83** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,775/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,800/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,800 / 10-yr mean $13,930 = **1.45×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $22.47 (NAV) + 0.40 × $18.83 (strip) = **$21.01**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 16.77 | 80% |
| Balance-sheet net | 2.49 | 12% |
| §15 governance haircut | -5.78 | -27% |
| Discounted DPS (strip, 8-10q) | 0.00 | 0% |
| Discounted terminal (aged NAV) | 7.53 | 36% |
| **Blend FV** | **21.01** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 1.00 = **100%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.79 |
| 95% | $21.93 |
| 100% | $21.98 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.38× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **8,510** | — |
| 10-year mean | 16,653 | 0.51× |
| 12-month FFA | 22,218 | 0.38× |
| Current spot | 24,574 | 0.35× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (47% of fleet value) | 6,425 | 0.46× |
| Cape (32% of fleet value) | 12,542 | 0.53× |
| Pana (21% of fleet value) | 6,923 | 0.58× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.59 | $18.27 | $19.96 | $21.64 | $23.32 |
| **-15%** | $17.12 | $18.80 | $20.49 | $22.17 | $23.85 |
| **+0%** | $17.65 | $19.33 | $21.01 | $22.70 | $24.38 |
| **+15%** | $18.18 | $19.86 | $21.54 | $23.23 | $24.91 |
| **+30%** | $18.70 | $20.39 | $22.07 | $23.75 | $25.44 |

_Current price $18.84. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$21.01** is +11.5% vs the current price ($18.84) and -24.9% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$8,510/day** (0.38× the current forward) — 0.5× the value-weighted 10-yr mean ($16,653, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

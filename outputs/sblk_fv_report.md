# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.90
- **Model fair value:** $29.16
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,584.0 |
| Fleet value — Pana | 1,416.0 |
| Fleet value — Supra-Ultra | 1,388.0 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,537.8** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$30.13** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 35,400 | 35,400 | 1.636 | 1.555 | 1.515 |
| Q2 | 35,200 | 35,200 | 1.572 | 1.494 | 1.418 |
| Q3 | 30,100 | 30,100 | 1.240 | 1.178 | 1.089 |
| Q4 | 29,100 | 29,100 | 1.165 | 1.107 | 0.997 |
| Q5 | 28,100 | 28,100 | 1.090 | 1.036 | 0.909 |
| Q6 | 27,100 | 27,100 | 1.016 | 0.965 | 0.825 |
| Q7 | 26,600 | 26,600 | 0.974 | 0.925 | 0.771 |
| Q8 | 26,100 | 26,100 | 0.937 | 0.890 | 0.722 |
| Σ discounted DPS | | | | | 8.25 |
| Terminal value (NAV, q9) | | | | 24.63 | 19.47 |
| **DivStrip implied price** | | | | | **$27.72** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$32,450/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$35,300/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $35,300 / 10-yr mean $23,650 = **1.48×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $30.13 (NAV) + 0.40 × $27.72 (strip) = **$29.16**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.42 | 77% |
| Balance-sheet net | -4.34 | -15% |
| Discounted DPS (strip, 8-10q) | 3.30 | 11% |
| Discounted terminal (aged NAV) | 7.79 | 27% |
| **Blend FV** | **29.16** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.60 + 0.40 × 0.70 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $29.10 |
| 95% | $29.16 |
| 100% | $29.19 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.25× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **5,782** | — |
| 10-year mean | 16,784 | 0.34× |
| 12-month FFA | 22,804 | 0.25× |
| Current spot | 25,475 | 0.23× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 8,227 | 0.35× |
| Pana (32% of fleet value) | 4,599 | 0.39× |
| Supra-Ultra (32% of fleet value) | 4,198 | 0.30× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $20.95 | $24.18 | $27.42 | $30.65 | $33.88 |
| **-15%** | $21.82 | $25.06 | $28.29 | $31.52 | $34.76 |
| **+0%** | $22.69 | $25.93 | $29.16 | $32.40 | $35.63 |
| **+15%** | $23.57 | $26.80 | $30.04 | $33.27 | $36.51 |
| **+30%** | $24.44 | $27.68 | $30.91 | $34.15 | $37.38 |

_Current price $24.90. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$29.16** is +17.1% vs the current price ($24.90) and -15.5% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$5,782/day** (0.25× the current forward) — 0.3× the value-weighted 10-yr mean ($16,784, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $64.1M (+3%) / 10yr $46.9M (+4%) [n=29], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.1M (+10%) / 10yr $26.1M (+9%) [n=6], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.2M (-9%) / 10yr $23.6M (-6%) [n=27], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

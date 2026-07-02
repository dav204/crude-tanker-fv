# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $24.81
- **Model fair value:** $28.34
- **Analyst target:** $34.50

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 1,557.5 |
| Fleet value — Pana | 1,407.8 |
| Fleet value — Supra-Ultra | 1,330.4 |
| + Cash & equivalents | 397.0 |
| + Working capital (net) | 44.6 |
| − Total debt | 946.3 |
| − Lease liabilities | 149.8 |
| − Newbuild commitments | 195.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **3,445.6** |
| Diluted shares | 117,431,435 |
| **NAV / share** | **$29.34** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 31,200 | 31,200 | 1.594 | 1.514 | 1.475 |
| Q2 | 31,450 | 31,450 | 1.480 | 1.406 | 1.334 |
| Q3 | 28,500 | 28,500 | 1.186 | 1.127 | 1.042 |
| Q4 | 27,000 | 27,000 | 1.103 | 1.048 | 0.944 |
| Q5 | 25,500 | 25,500 | 1.022 | 0.970 | 0.852 |
| Q6 | 25,000 | 25,000 | 0.980 | 0.931 | 0.796 |
| Q7 | 24,500 | 24,500 | 0.930 | 0.884 | 0.736 |
| Q8 | 24,000 | 24,000 | 0.897 | 0.852 | 0.692 |
| Σ discounted DPS | | | | | 7.87 |
| Terminal value (NAV, q9) | | | | 23.99 | 18.97 |
| **DivStrip implied price** | | | | | **$26.84** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$29,538/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$27,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $27,000 / 10-yr mean $23,650 = **1.25×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $29.34 (NAV) + 0.40 × $26.84 (strip) = **$28.34**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $28.28 |
| 95% | $28.34 |
| 100% | $28.36 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.37× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **8,164** | — |
| 10-year mean | 16,789 | 0.49× |
| 12-month FFA | 21,835 | 0.37× |
| Current spot | 26,535 | 0.31× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 11,045 | 0.47× |
| Pana (33% of fleet value) | 6,896 | 0.58× |
| Supra-Ultra (31% of fleet value) | 6,135 | 0.44× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $20.30 | $23.47 | $26.64 | $29.81 | $32.97 |
| **-15%** | $21.15 | $24.32 | $27.49 | $30.66 | $33.83 |
| **+0%** | $22.00 | $25.17 | $28.34 | $31.51 | $34.68 |
| **+15%** | $22.86 | $26.02 | $29.19 | $32.36 | $35.53 |
| **+30%** | $23.71 | $26.87 | $30.04 | $33.21 | $36.38 |

_Current price $24.81. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$28.34** is +14.2% vs the current price ($24.81) and -17.9% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$8,164/day** (0.37× the current forward) — 0.5× the value-weighted 10-yr mean ($16,789, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.

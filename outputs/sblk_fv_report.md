# SBLK — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $26.35
- **Model fair value:** $28.32
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
| Q1 | 32,500 | 32,500 | 1.528 | 1.452 | 1.414 |
| Q2 | 33,650 | 33,650 | 1.464 | 1.391 | 1.320 |
| Q3 | 29,500 | 29,500 | 1.193 | 1.133 | 1.048 |
| Q4 | 28,500 | 28,500 | 1.118 | 1.062 | 0.957 |
| Q5 | 27,500 | 27,500 | 1.043 | 0.991 | 0.870 |
| Q6 | 26,500 | 26,500 | 0.969 | 0.920 | 0.787 |
| Q7 | 26,000 | 26,000 | 0.927 | 0.881 | 0.734 |
| Q8 | 25,500 | 25,500 | 0.890 | 0.845 | 0.686 |
| Σ discounted DPS | | | | | 7.82 |
| Terminal value (NAV, q9) | | | | 23.99 | 18.97 |
| **DivStrip implied price** | | | | | **$26.78** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$31,038/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$33,100/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $33,100 / 10-yr mean $23,650 = **1.42×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $29.34 (NAV) + 0.40 × $26.78 (strip) = **$28.32**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $28.26 |
| 95% | $28.32 |
| 100% | $28.34 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.65× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **14,332** | — |
| 10-year mean | 16,789 | 0.85× |
| 12-month FFA | 21,987 | 0.65× |
| Current spot | 23,020 | 0.62× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (36% of fleet value) | 20,231 | 0.86× |
| Pana (33% of fleet value) | 11,362 | 0.95× |
| Supra-Ultra (31% of fleet value) | 10,568 | 0.76× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $20.29 | $23.45 | $26.62 | $29.79 | $32.96 |
| **-15%** | $21.13 | $24.30 | $27.47 | $30.64 | $33.81 |
| **+0%** | $21.98 | $25.15 | $28.32 | $31.49 | $34.65 |
| **+15%** | $22.83 | $26.00 | $29.17 | $32.33 | $35.50 |
| **+30%** | $23.68 | $26.84 | $30.01 | $33.18 | $36.35 |

_Current price $26.35. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$28.32** is +7.5% vs the current price ($26.35) and -17.9% vs the analyst target ($34.50). The current price implies the fleet earning a value-weighted blended **$14,332/day** (0.65× the current forward) — 0.9× the value-weighted 10-yr mean ($16,789, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

# LPG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $40.14
- **Model fair value:** $32.76
- **Analyst target:** $54.00

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLGC | 1,745.6 |
| + Cash & equivalents | 327.4 |
| + Working capital (net) | 100.8 |
| − Total debt | 565.8 |
| − Lease liabilities | 148.7 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,459.3** |
| Diluted shares | 42,782,681 |
| **NAV / share** | **$34.11** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLGC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 62,000 | 62,000 | 1.875 | 1.125 | 1.096 |
| Q2 | 55,000 | 55,000 | 1.553 | 0.932 | 0.885 |
| Q3 | 48,000 | 48,000 | 1.231 | 0.739 | 0.683 |
| Q4 | 45,000 | 45,000 | 1.093 | 0.656 | 0.591 |
| Q5 | 43,000 | 43,000 | 1.001 | 0.601 | 0.527 |
| Q6 | 42,000 | 42,000 | 0.955 | 0.573 | 0.490 |
| Q7 | 41,000 | 41,000 | 0.909 | 0.546 | 0.455 |
| Q8 | 40,000 | 40,000 | 0.863 | 0.518 | 0.420 |
| Σ discounted DPS | | | | | 5.15 |
| Terminal value (NAV, q9) | | | | 30.95 | 24.48 |
| **DivStrip implied price** | | | | | **$29.62** |

_FFA spot is the VLGC forward curve that drives the strip cash flows; its 12-month average is **$52,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$63,615/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $63,615 / 10-yr mean $40,000 = **1.59×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $34.11 (NAV) + 0.30 × $29.62 (strip) = **$32.76**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $32.83 |
| 95% | $32.88 |
| 100% | $32.89 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.66× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **139,786** | — |
| 10-year mean | 40,000 | 3.49× |
| 12-month FFA | 52,500 | 2.66× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $24.11 | $27.77 | $31.43 | $35.09 | $38.75 |
| **-15%** | $24.78 | $28.44 | $32.10 | $35.76 | $39.42 |
| **+0%** | $25.45 | $29.10 | $32.76 | $36.42 | $40.08 |
| **+15%** | $26.11 | $29.77 | $33.43 | $37.09 | $40.75 |
| **+30%** | $26.78 | $30.44 | $34.09 | $37.75 | $41.41 |

_Current price $40.14. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$32.76** is -18.4% vs the current price ($40.14) and -39.3% vs the analyst target ($54.00). The current price implies the fleet earning a value-weighted blended **$139,786/day** (2.66× the current forward) — 3.5× the value-weighted 10-yr mean ($40,000, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

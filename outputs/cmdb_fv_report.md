# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $19.56
- **Model fair value:** $20.52
- **Analyst target:** $27.98

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Cape | 215.2 |
| Fleet value — Pana | 140.0 |
| Fleet value — Supra-Ultra | 302.2 |
| + Cash & equivalents | 258.5 |
| + Working capital (net) | 3.8 |
| − Total debt | 141.4 |
| − Lease liabilities | 20.6 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **757.6** |
| Diluted shares | 24,180,472 |
| **NAV / share** | **$31.33** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Supra-Ultra, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 18,800 | 18,800 | 1.277 | 0.000 | 0.000 |
| Q2 | 17,875 | 17,875 | 1.206 | 0.000 | 0.000 |
| Q3 | 15,075 | 15,075 | 0.872 | 0.000 | 0.000 |
| Q4 | 14,475 | 14,475 | 0.799 | 0.000 | 0.000 |
| Q5 | 13,875 | 13,875 | 0.725 | 0.000 | 0.000 |
| Q6 | 13,275 | 13,275 | 0.652 | 0.000 | 0.000 |
| Q7 | 12,975 | 12,975 | 0.613 | 0.000 | 0.000 |
| Q8 | 12,675 | 12,675 | 0.576 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 23.29 | 18.41 |
| **DivStrip implied price** | | | | | **$18.41** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,556/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$18,350/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $18,350 / 10-yr mean $13,930 = **1.44×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $21.93 (NAV) + 0.40 × $18.41 (strip) = **$20.52**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.28 |
| 95% | $21.42 |
| 100% | $21.47 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.72× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **15,989** | — |
| 10-year mean | 16,680 | 0.96× |
| 12-month FFA | 22,096 | 0.72× |
| Current spot | 22,491 | 0.71× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (46% of fleet value) | 11,981 | 0.86× |
| Cape (33% of fleet value) | 23,482 | 0.99× |
| Pana (21% of fleet value) | 13,125 | 1.10× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.20 | $17.84 | $19.48 | $21.12 | $22.75 |
| **-15%** | $16.73 | $18.36 | $20.00 | $21.64 | $23.28 |
| **+0%** | $17.25 | $18.89 | $20.52 | $22.16 | $23.80 |
| **+15%** | $17.77 | $19.41 | $21.05 | $22.69 | $24.32 |
| **+30%** | $18.30 | $19.93 | $21.57 | $23.21 | $24.85 |

_Current price $19.56. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$20.52** is +4.9% vs the current price ($19.56) and -26.6% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$15,989/day** (0.72× the current forward) — 1.0× the value-weighted 10-yr mean ($16,680, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.

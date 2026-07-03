# CMDB — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $18.18
- **Model fair value:** $20.43
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
| Q1 | 18,550 | 18,550 | 1.180 | 0.000 | 0.000 |
| Q2 | 17,300 | 17,300 | 1.109 | 0.000 | 0.000 |
| Q3 | 14,800 | 14,800 | 0.829 | 0.000 | 0.000 |
| Q4 | 14,200 | 14,200 | 0.756 | 0.000 | 0.000 |
| Q5 | 13,600 | 13,600 | 0.683 | 0.000 | 0.000 |
| Q6 | 13,000 | 13,000 | 0.610 | 0.000 | 0.000 |
| Q7 | 12,700 | 12,700 | 0.570 | 0.000 | 0.000 |
| Q8 | 12,400 | 12,400 | 0.534 | 0.000 | 0.000 |
| Σ discounted DPS | | | | | 0.00 |
| Terminal value (NAV, q9) | | | | 22.97 | 18.17 |
| **DivStrip implied price** | | | | | **$18.17** |

_FFA spot is the Supra-Ultra forward curve that drives the strip cash flows; its 12-month average is **$16,212/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$17,900/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $17,900 / 10-yr mean $13,930 = **1.38×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $21.93 (NAV) + 0.40 × $18.17 (strip) = **$20.43**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $21.13 |
| 95% | $21.26 |
| 100% | $21.31 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.34× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **7,207** | — |
| 10-year mean | 16,680 | 0.43× |
| 12-month FFA | 21,325 | 0.34× |
| Current spot | 22,491 | 0.32× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Supra-Ultra (46% of fleet value) | 5,479 | 0.39× |
| Cape (33% of fleet value) | 10,489 | 0.44× |
| Pana (21% of fleet value) | 5,891 | 0.50× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $16.13 | $17.77 | $19.41 | $21.05 | $22.68 |
| **-15%** | $16.64 | $18.28 | $19.92 | $21.55 | $23.19 |
| **+0%** | $17.15 | $18.79 | $20.43 | $22.06 | $23.70 |
| **+15%** | $17.66 | $19.30 | $20.93 | $22.57 | $24.21 |
| **+30%** | $18.17 | $19.80 | $21.44 | $23.08 | $24.72 |

_Current price $18.18. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$20.43** is +12.3% vs the current price ($18.18) and -27.0% vs the analyst target ($27.98). The current price implies the fleet earning a value-weighted blended **$7,207/day** (0.34× the current forward) — 0.4× the value-weighted 10-yr mean ($16,680, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.

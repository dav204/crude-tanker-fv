# CMBT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $14.05
- **Model fair value:** $15.19
- **Analyst target:** $16.59

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 624.4 |
| Fleet value — Suezmax | 1,266.2 |
| Fleet value — Cape | 4,746.2 |
| Fleet value — Pana | 980.4 |
| Fleet value — Ctr-Large | 257.2 |
| + Cash & equivalents | 202.9 |
| + Working capital (net) | 912.1 |
| − Total debt | 5,238.2 |
| − Lease liabilities | 6.2 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 759.8 |
| **= NAV total** | **4,604.9** |
| Diluted shares | 290,169,769 |
| **NAV / share** | **$15.87** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Cape, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 32,500 | 32,500 | 0.967 | 0.484 | 0.471 |
| Q2 | 33,650 | 33,650 | 1.112 | 0.556 | 0.528 |
| Q3 | 29,500 | 29,500 | 0.947 | 0.473 | 0.438 |
| Q4 | 28,500 | 28,500 | 0.748 | 0.374 | 0.337 |
| Q5 | 27,500 | 27,500 | 0.667 | 0.334 | 0.293 |
| Q6 | 26,500 | 26,500 | 0.753 | 0.377 | 0.322 |
| Q7 | 26,000 | 26,000 | 0.768 | 0.384 | 0.320 |
| Q8 | 25,500 | 25,500 | 0.580 | 0.290 | 0.235 |
| Σ discounted DPS | | | | | 2.94 |
| Terminal value (NAV, q9) | | | | 13.48 | 10.66 |
| **DivStrip implied price** | | | | | **$13.60** |

_FFA spot is the Cape forward curve that drives the strip cash flows; its 12-month average is **$31,038/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$33,100/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $33,100 / 10-yr mean $23,650 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.87 (NAV) + 0.30 × $13.60 (strip) = **$15.19**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $15.25 |
| 95% | $15.29 |
| 100% | $15.30 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.60× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **29,270** | — |
| 10-year mean | 24,709 | 1.18× |
| 12-month FFA | 48,817 | 0.60× |
| Current spot | 65,259 | 0.45× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Cape (60% of fleet value) | 18,610 | 0.79× |
| Suezmax (16% of fleet value) | 50,965 | 1.84× |
| Pana (12% of fleet value) | 10,452 | 0.88× |
| VLCC (8% of fleet value) | 92,937 | 2.32× |
| Ctr-Large (3% of fleet value) | 36,350 | 0.89× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.52 | $11.93 | $14.34 | $16.74 | $19.15 |
| **-15%** | $9.94 | $12.35 | $14.76 | $17.17 | $19.58 |
| **+0%** | $10.37 | $12.78 | $15.19 | $17.60 | $20.01 |
| **+15%** | $10.80 | $13.21 | $15.62 | $18.03 | $20.44 |
| **+30%** | $11.23 | $13.63 | $16.04 | $18.45 | $20.86 |

_Current price $14.05. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.19** is +8.1% vs the current price ($14.05) and -8.4% vs the analyst target ($16.59). The current price implies the fleet earning a value-weighted blended **$29,270/day** (0.60× the current forward) — 1.2× the value-weighted 10-yr mean ($24,709, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.

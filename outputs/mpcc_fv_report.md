# MPCC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $2.62
- **Model fair value:** $2.19
- **Analyst target:** $2.63

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Feeder | 432.6 |
| Fleet value — Ctr-Intermediate | 1,093.3 |
| + Cash & equivalents | 269.3 |
| + Working capital (net) | 85.9 |
| − Total debt | 462.9 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 633.7 |
| + Newbuild advances | 112.9 |
| **= NAV total** | **897.4** |
| Diluted shares | 443,700,279 |
| **NAV / share** | **$2.02** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Ctr-Intermediate, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 43,375 | 26,404 | 0.129 | 0.064 | 0.063 |
| Q2 | 42,875 | 26,404 | 0.131 | 0.066 | 0.062 |
| Q3 | 42,350 | 26,946 | 0.134 | 0.067 | 0.062 |
| Q4 | 41,325 | 28,463 | 0.143 | 0.071 | 0.064 |
| Q5 | 40,800 | 28,808 | 0.152 | 0.076 | 0.067 |
| Q6 | 39,775 | 29,426 | 0.162 | 0.081 | 0.069 |
| Q7 | 39,250 | 29,513 | 0.170 | 0.085 | 0.071 |
| Q8 | 38,750 | 30,281 | 0.183 | 0.092 | 0.074 |
| Q9 | 37,700 | 30,369 | 0.192 | 0.096 | 0.076 |
| Q10 | 37,200 | 32,493 | 0.217 | 0.108 | 0.084 |
| Σ discounted DPS | | | | | 0.69 |
| Terminal value (NAV, q9) | | | | 2.33 | 1.75 |
| **DivStrip implied price** | | | | | **$2.44** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$42,481/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$43,400/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $43,400 / 10-yr mean $33,700 = **1.21×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.02 (NAV) + 0.40 × $2.44 (strip) = **$2.19**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.14 |
| 95% | $2.15 |
| 100% | $2.15 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **4.36× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **157,594** | — |
| 10-year mean | 30,057 | 5.24× |
| 12-month FFA | 36,179 | 4.36× |
| Current spot | 36,908 | 4.27× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (72% of fleet value) | 185,047 | 5.49× |
| Ctr-Feeder (28% of fleet value) | 88,208 | 4.23× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.48 | $1.78 | $2.09 | $2.39 | $2.69 |
| **-15%** | $1.50 | $1.80 | $2.11 | $2.41 | $2.71 |
| **+0%** | $1.52 | $1.83 | $2.13 | $2.43 | $2.73 |
| **+15%** | $1.55 | $1.85 | $2.15 | $2.45 | $2.76 |
| **+30%** | $1.57 | $1.87 | $2.17 | $2.48 | $2.78 |

_Current price $2.62. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.19** is -16.4% vs the current price ($2.62) and -16.8% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$157,594/day** (4.36× the current forward) — 5.2× the value-weighted 10-yr mean ($30,057, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

# MPCC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $2.54
- **Model fair value:** $1.99
- **Analyst target:** $2.63

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

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
| Terminal value (NAV, q9) | | | | 1.68 | 1.26 |
| **DivStrip implied price** | | | | | **$1.95** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$42,481/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$43,400/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $43,400 / 10-yr mean $33,700 = **1.21×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.02 (NAV) + 0.40 × $1.95 (strip) = **$1.99**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.12 |
| 95% | $2.18 |
| 100% | $2.20 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **8.28× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **299,648** | — |
| 10-year mean | 30,057 | 9.97× |
| 12-month FFA | 36,179 | 8.28× |
| Current spot | 36,908 | 8.12× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (72% of fleet value) | 351,846 | 10.44× |
| Ctr-Feeder (28% of fleet value) | 167,718 | 8.04× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.35 | $1.66 | $1.97 | $2.27 | $2.58 |
| **-15%** | $1.36 | $1.67 | $1.98 | $2.29 | $2.59 |
| **+0%** | $1.37 | $1.68 | $1.99 | $2.30 | $2.60 |
| **+15%** | $1.39 | $1.69 | $2.00 | $2.31 | $2.62 |
| **+30%** | $1.40 | $1.70 | $2.01 | $2.32 | $2.63 |

_Current price $2.54. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$1.99** is -21.5% vs the current price ($2.54) and -24.2% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$299,648/day** (8.28× the current forward) — 10.0× the value-weighted 10-yr mean ($30,057, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

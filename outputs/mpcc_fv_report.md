# MPCC — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $2.78
- **Model fair value:** $2.13
- **Analyst target:** $2.63

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Ctr-Feeder | 440.9 |
| Fleet value — Ctr-Intermediate | 1,194.8 |
| + Cash & equivalents | 269.3 |
| + Working capital (net) | 85.9 |
| − Total debt | 462.9 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 633.7 |
| + Newbuild advances | 112.9 |
| **= NAV total** | **1,007.2** |
| Diluted shares | 443,700,279 |
| **NAV / share** | **$2.27** |

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
| Terminal value (NAV, q9) | | | | 1.64 | 1.23 |
| **DivStrip implied price** | | | | | **$1.92** |

_FFA spot is the Ctr-Intermediate forward curve that drives the strip cash flows; its 12-month average is **$42,481/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$43,400/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $43,400 / 10-yr mean $33,700 = **1.21×** → **elevated**
- Weights: w_nav = 0.60, w_earn = 0.40

## Blended fair value

0.60 × $2.27 (NAV) + 0.40 × $1.92 (strip) = **$2.13**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $2.26 |
| 95% | $2.32 |
| 100% | $2.34 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **9.61× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **350,590** | — |
| 10-year mean | 30,236 | 11.59× |
| 12-month FFA | 36,489 | 9.61× |
| Current spot | 37,228 | 9.42× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Ctr-Intermediate (73% of fleet value) | 408,164 | 12.11× |
| Ctr-Feeder (27% of fleet value) | 194,564 | 9.33× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $1.46 | $1.79 | $2.11 | $2.43 | $2.75 |
| **-15%** | $1.48 | $1.80 | $2.12 | $2.44 | $2.76 |
| **+0%** | $1.49 | $1.81 | $2.13 | $2.45 | $2.77 |
| **+15%** | $1.50 | $1.82 | $2.14 | $2.46 | $2.78 |
| **+30%** | $1.51 | $1.83 | $2.15 | $2.47 | $2.79 |

_Current price $2.78. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$2.13** is -23.4% vs the current price ($2.78) and -19.0% vs the analyst target ($2.63). The current price implies the fleet earning a value-weighted blended **$350,590/day** (9.61× the current forward) — 11.6× the value-weighted 10-yr mean ($30,236, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $30.2M (-8%) / 10yr $22.1M (-12%) [n=20], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.

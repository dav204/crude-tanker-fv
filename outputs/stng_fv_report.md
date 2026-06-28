# STNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $72.58
- **Model fair value:** $78.93
- **Analyst target:** $94.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 2,099.5 |
| Fleet value — MR | 1,400.1 |
| Fleet value — Handymax | 205.3 |
| + Cash & equivalents | 984.3 |
| + Working capital (net) | 602.8 |
| − Total debt | 789.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 572.8 |
| + Newbuild advances | 90.0 |
| **= NAV total** | **4,020.1** |
| Diluted shares | 50,030,000 |
| **NAV / share** | **$80.35** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 69,375 | 3.958 | 0.450 | 0.438 |
| Q2 | 88,000 | 80,750 | 5.395 | 0.450 | 0.427 |
| Q3 | 82,000 | 75,500 | 4.898 | 0.450 | 0.416 |
| Q4 | 64,000 | 59,750 | 3.112 | 0.450 | 0.405 |
| Q5 | 59,000 | 55,375 | 2.764 | 0.450 | 0.395 |
| Q6 | 70,000 | 65,000 | 3.806 | 0.450 | 0.385 |
| Q7 | 74,000 | 68,500 | 4.301 | 0.450 | 0.375 |
| Q8 | 56,000 | 52,750 | 2.614 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 91.57 | 72.41 |
| **DivStrip implied price** | | | | | **$75.62** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.75×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $80.35 (NAV) + 0.30 × $75.62 (strip) = **$78.93**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $79.72 |
| 95% | $79.87 |
| 100% | $79.92 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.42× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **23,127** | — |
| 10-year mean | 22,573 | 1.02× |
| 12-month FFA | 54,500 | 0.42× |
| Current spot | 37,284 | 0.62× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (57% of fleet value) | 32,781 | 1.19× |
| MR (38% of fleet value) | 10,503 | 0.66× |
| Handymax (6% of fleet value) | 10,503 | 0.66× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $62.50 | $69.06 | $75.62 | $82.18 | $88.74 |
| **-15%** | $64.16 | $70.72 | $77.28 | $83.84 | $90.40 |
| **+0%** | $65.81 | $72.37 | $78.93 | $85.49 | $92.05 |
| **+15%** | $67.47 | $74.03 | $80.59 | $87.15 | $93.71 |
| **+30%** | $69.12 | $75.68 | $82.24 | $88.80 | $95.36 |

_Current price $72.58. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$78.93** is +8.8% vs the current price ($72.58) and -16.0% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$23,127/day** (0.42× the current forward) — 1.0× the value-weighted 10-yr mean ($22,573, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

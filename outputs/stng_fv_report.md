# STNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $76.17
- **Model fair value:** $74.00
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
| Terminal value (NAV, q9) | | | | 70.77 | 55.96 |
| **DivStrip implied price** | | | | | **$59.17** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.75×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $80.35 (NAV) + 0.30 × $59.17 (strip) = **$74.00**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $80.64 |
| 95% | $81.89 |
| 100% | $82.31 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **50.00× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **2,725,019** | — |
| 10-year mean | 22,573 | 120.72× |
| 12-month FFA | 54,500 | 50.00× |
| Current spot | 37,284 | 73.09× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (57% of fleet value) | 3,862,500 | 139.95× |
| MR (38% of fleet value) | 1,237,500 | 77.34× |
| Handymax (6% of fleet value) | 1,237,500 | 77.34× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $60.57 | $67.28 | $74.00 | $80.71 | $87.42 |
| **-15%** | $60.57 | $67.28 | $74.00 | $80.71 | $87.42 |
| **+0%** | $60.57 | $67.28 | $74.00 | $80.71 | $87.42 |
| **+15%** | $60.57 | $67.28 | $74.00 | $80.71 | $87.42 |
| **+30%** | $60.57 | $67.28 | $74.00 | $80.71 | $87.42 |

_Current price $76.17. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$74.00** is -2.9% vs the current price ($76.17) and -21.3% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$2,725,019/day** (50.00× the current forward) — 120.7× the value-weighted 10-yr mean ($22,573, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

# STNG — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $69.53
- **Model fair value:** $76.13
- **Analyst target:** $94.00

## Data validation warnings

- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 2,099.5 |
| Fleet value — MR | 1,210.7 |
| Fleet value — Handymax | 205.3 |
| + Cash & equivalents | 984.3 |
| + Working capital (net) | 163.3 |
| − Total debt | 589.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 572.8 |
| + Newbuild advances | 69.1 |
| **= NAV total** | **3,875.3** |
| Diluted shares | 50,025,865 |
| **NAV / share** | **$77.47** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (LR2, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 69,375 | 3.812 | 0.450 | 0.438 |
| Q2 | 88,000 | 80,750 | 5.163 | 0.450 | 0.427 |
| Q3 | 82,000 | 75,500 | 4.688 | 0.450 | 0.416 |
| Q4 | 64,000 | 59,750 | 2.999 | 0.450 | 0.405 |
| Q5 | 59,000 | 55,375 | 2.661 | 0.450 | 0.395 |
| Q6 | 70,000 | 65,000 | 3.649 | 0.450 | 0.385 |
| Q7 | 74,000 | 68,500 | 4.112 | 0.450 | 0.375 |
| Q8 | 56,000 | 52,750 | 2.511 | 0.450 | 0.365 |
| Σ discounted DPS | | | | | 3.21 |
| Terminal value (NAV, q9) | | | | 88.27 | 69.80 |
| **DivStrip implied price** | | | | | **$73.01** |

_FFA spot is the LR2 forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $27,600 = **1.77×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $77.47 (NAV) + 0.30 × $73.01 (strip) = **$76.13**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $76.89 |
| 95% | $77.03 |
| 100% | $77.08 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.38× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **21,075** | — |
| 10-year mean | 22,928 | 0.92× |
| 12-month FFA | 56,103 | 0.38× |
| Current spot | 39,661 | 0.53× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| LR2 (60% of fleet value) | 29,018 | 1.05× |
| MR (34% of fleet value) | 9,297 | 0.58× |
| Handymax (6% of fleet value) | 9,297 | 0.58× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $60.51 | $66.73 | $72.96 | $79.18 | $85.41 |
| **-15%** | $62.09 | $68.32 | $74.54 | $80.77 | $86.99 |
| **+0%** | $63.68 | $69.90 | $76.13 | $82.35 | $88.58 |
| **+15%** | $65.26 | $71.49 | $77.71 | $83.94 | $90.16 |
| **+30%** | $66.85 | $73.07 | $79.30 | $85.52 | $91.75 |

_Current price $69.53. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$76.13** is +9.5% vs the current price ($69.53) and -19.0% vs the analyst target ($94.00). The current price implies the fleet earning a value-weighted blended **$21,075/day** (0.38× the current forward) — 0.9× the value-weighted 10-yr mean ($22,928, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

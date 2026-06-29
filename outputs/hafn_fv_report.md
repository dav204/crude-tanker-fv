# HAFN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $6.86
- **Model fair value:** $5.66
- **Analyst target:** $10.00

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — LR2 | 577.3 |
| Fleet value — LR1 | 848.8 |
| Fleet value — MR | 1,585.9 |
| Fleet value — Handysize | 319.7 |
| + Cash & equivalents | 146.5 |
| + Working capital (net) | 475.0 |
| − Total debt | 943.5 |
| − Lease liabilities | 35.9 |
| − Newbuild commitments | 405.0 |
| + Newbuild advances | 40.0 |
| **= NAV total** | **2,608.8** |
| Diluted shares | 500,000,000 |
| **NAV / share** | **$5.22** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (MR, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 22,000 | 22,000 | 0.556 | 0.445 | 0.434 |
| Q2 | 30,000 | 30,000 | 0.738 | 0.591 | 0.561 |
| Q3 | 28,000 | 28,000 | 0.676 | 0.541 | 0.500 |
| Q4 | 19,000 | 19,000 | 0.450 | 0.360 | 0.324 |
| Q5 | 18,000 | 18,000 | 0.406 | 0.325 | 0.285 |
| Q6 | 23,000 | 23,000 | 0.538 | 0.430 | 0.368 |
| Q7 | 26,000 | 26,000 | 0.601 | 0.480 | 0.400 |
| Q8 | 18,000 | 18,000 | 0.387 | 0.310 | 0.252 |
| Σ discounted DPS | | | | | 3.12 |
| Terminal value (NAV, q9) | | | | 4.53 | 3.58 |
| **DivStrip implied price** | | | | | **$6.70** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $5.22 (NAV) + 0.30 × $6.70 (strip) = **$5.66**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.66 |
| 95% | $5.68 |
| 100% | $5.69 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.78× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **83,976** | — |
| 10-year mean | 20,965 | 4.01× |
| 12-month FFA | 47,221 | 1.78× |
| Current spot | 20,190 | 4.16× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (48% of fleet value) | 44,014 | 2.75× |
| LR1 (25% of fleet value) | 137,378 | 4.98× |
| LR2 (17% of fleet value) | 137,378 | 4.98× |
| Handysize (10% of fleet value) | 44,014 | 2.75× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $4.03 | $4.61 | $5.20 | $5.79 | $6.38 |
| **-15%** | $4.26 | $4.84 | $5.43 | $6.02 | $6.61 |
| **+0%** | $4.49 | $5.08 | $5.66 | $6.25 | $6.84 |
| **+15%** | $4.72 | $5.31 | $5.89 | $6.48 | $7.07 |
| **+30%** | $4.95 | $5.54 | $6.12 | $6.71 | $7.30 |

_Current price $6.86. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.66** is -17.5% vs the current price ($6.86) and -43.4% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$83,976/day** (1.78× the current forward) — 4.0× the value-weighted 10-yr mean ($20,965, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

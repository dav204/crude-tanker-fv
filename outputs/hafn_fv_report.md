# HAFN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $7.70
- **Model fair value:** $5.59
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
| Terminal value (NAV, q9) | | | | 4.22 | 3.34 |
| **DivStrip implied price** | | | | | **$6.46** |

_FFA spot is the MR forward curve that drives the strip cash flows; its 12-month average is **$24,750/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$22,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $22,000 / 10-yr mean $16,000 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $5.22 (NAV) + 0.30 × $6.46 (strip) = **$5.59**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $5.59 |
| 95% | $5.77 |
| 100% | $5.83 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **126,273** | — |
| 10-year mean | 20,965 | 6.02× |
| 12-month FFA | 47,221 | 2.67× |
| Current spot | 20,190 | 6.25× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| MR (48% of fleet value) | 66,183 | 4.14× |
| LR1 (25% of fleet value) | 206,573 | 7.48× |
| LR2 (17% of fleet value) | 206,573 | 7.48× |
| Handysize (10% of fleet value) | 66,183 | 4.14× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $4.01 | $4.61 | $5.21 | $5.81 | $6.41 |
| **-15%** | $4.20 | $4.80 | $5.40 | $6.00 | $6.60 |
| **+0%** | $4.39 | $4.99 | $5.59 | $6.19 | $6.79 |
| **+15%** | $4.58 | $5.18 | $5.78 | $6.38 | $6.98 |
| **+30%** | $4.77 | $5.37 | $5.97 | $6.57 | $7.17 |

_Current price $7.70. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$5.59** is -27.4% vs the current price ($7.70) and -44.1% vs the analyst target ($10.00). The current price implies the fleet earning a value-weighted blended **$126,273/day** (2.67× the current forward) — 6.0× the value-weighted 10-yr mean ($20,965, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.9M (+16%) / 10yr $50.7M (+13%) [n=25], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $85.9M (-7%) / 10yr $69.7M (-13%) [n=18], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

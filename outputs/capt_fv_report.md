# CAPT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $12.79
- **Model fair value:** $12.59
- **Analyst target:** $18.90

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,607.9 |
| Fleet value — Suezmax | 957.4 |
| Fleet value — Aframax | 289.4 |
| Fleet value — LR2 | 372.7 |
| + Cash & equivalents | 405.0 |
| + Working capital (net) | 13.0 |
| − Total debt | 217.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,880.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,548.3** |
| Diluted shares | 133,700,000 |
| **NAV / share** | **$11.58** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 147,500 | 0.547 | 0.246 | 0.240 |
| Q2 | 183,500 | 183,500 | 1.043 | 0.470 | 0.446 |
| Q3 | 165,500 | 165,500 | 1.109 | 0.499 | 0.461 |
| Q4 | 123,500 | 123,500 | 0.903 | 0.406 | 0.366 |
| Q5 | 111,500 | 111,500 | 0.831 | 0.374 | 0.328 |
| Q6 | 135,500 | 135,500 | 1.210 | 0.545 | 0.466 |
| Q7 | 147,500 | 147,500 | 1.489 | 0.670 | 0.558 |
| Q8 | 105,500 | 105,500 | 1.131 | 0.509 | 0.413 |
| Σ discounted DPS | | | | | 3.28 |
| Terminal value (NAV, q9) | | | | 14.75 | 11.66 |
| **DivStrip implied price** | | | | | **$14.94** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.44×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $11.58 (NAV) + 0.30 × $14.94 (strip) = **$12.59**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $12.67 |
| 95% | $12.70 |
| 100% | $12.71 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.08× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **127,839** | — |
| 10-year mean | 34,618 | 3.69× |
| 12-month FFA | 118,285 | 1.08× |
| Current spot | 224,196 | 0.57× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (50% of fleet value) | 167,519 | 4.19× |
| Suezmax (30% of fleet value) | 91,865 | 3.31× |
| LR2 (12% of fleet value) | 83,489 | 3.02× |
| Aframax (9% of fleet value) | 83,489 | 2.29× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $7.38 | $9.61 | $11.84 | $14.07 | $16.30 |
| **-15%** | $7.76 | $9.99 | $12.22 | $14.45 | $16.67 |
| **+0%** | $8.13 | $10.36 | $12.59 | $14.82 | $17.05 |
| **+15%** | $8.50 | $10.73 | $12.96 | $15.19 | $17.42 |
| **+30%** | $8.88 | $11.11 | $13.34 | $15.57 | $17.80 |

_Current price $12.79. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$12.59** is -1.6% vs the current price ($12.79) and -33.4% vs the analyst target ($18.90). The current price implies the fleet earning a value-weighted blended **$127,839/day** (1.08× the current forward) — 3.7× the value-weighted 10-yr mean ($34,618, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

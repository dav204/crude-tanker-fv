# CAPT — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $13.24
- **Model fair value:** $15.24
- **Analyst target:** $18.90

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 1,947.9 |
| Fleet value — Suezmax | 1,075.4 |
| Fleet value — Aframax | 290.5 |
| Fleet value — LR2 | 376.9 |
| + Cash & equivalents | 405.0 |
| + Working capital (net) | 13.0 |
| − Total debt | 217.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,880.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,011.7** |
| Diluted shares | 133,700,000 |
| **NAV / share** | **$15.05** |

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
| Terminal value (NAV, q9) | | | | 15.72 | 12.43 |
| **DivStrip implied price** | | | | | **$15.71** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.50×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $15.05 (NAV) + 0.30 × $15.71 (strip) = **$15.24**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $16.01 |
| 95% | $16.34 |
| 100% | $16.45 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$15.05** ≥ price **$13.24** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 34,187 | 0.00× |
| 12-month FFA | 120,544 | 0.00× |
| Current spot | 234,091 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (53% of fleet value) | 0 | 0.00× |
| Suezmax (29% of fleet value) | 0 | 0.00× |
| LR2 (10% of fleet value) | 0 | 0.00× |
| Aframax (8% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $9.68 | $12.29 | $14.89 | $17.49 | $20.09 |
| **-15%** | $9.86 | $12.46 | $15.07 | $17.67 | $20.27 |
| **+0%** | $10.04 | $12.64 | $15.24 | $17.85 | $20.45 |
| **+15%** | $10.22 | $12.82 | $15.42 | $18.03 | $20.63 |
| **+30%** | $10.40 | $13.00 | $15.60 | $18.20 | $20.81 |

_Current price $13.24. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$15.24** is +15.1% vs the current price ($13.24) and -19.3% vs the analyst target ($18.90). NAV alone covers the price (NAV/sh $15.05 ≥ $13.24); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

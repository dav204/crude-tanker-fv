# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $40.93
- **Model fair value:** $26.40
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,363.4 |
| Fleet value — Suezmax | 1,607.0 |
| Fleet value — LR2 | 1,179.3 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,360.9** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$24.08** |
| NAV / share (ex yard discount) | $25.38 |
| Yard-discount impact / share | $-1.29 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 147,500 | 128,750 | 2.592 | 2.462 | 2.399 |
| Q2 | 183,500 | 153,950 | 3.297 | 3.132 | 2.973 |
| Q3 | 165,500 | 141,350 | 3.087 | 2.932 | 2.712 |
| Q4 | 123,500 | 111,950 | 2.332 | 2.216 | 1.996 |
| Q5 | 111,500 | 103,550 | 2.107 | 2.002 | 1.757 |
| Q6 | 135,500 | 120,350 | 2.585 | 2.456 | 2.100 |
| Q7 | 147,500 | 128,750 | 2.777 | 2.638 | 2.197 |
| Q8 | 105,500 | 99,350 | 1.993 | 1.893 | 1.536 |
| Σ discounted DPS | | | | | 17.67 |
| Terminal value (NAV, q9) | | | | 17.88 | 14.13 |
| **DivStrip implied price** | | | | | **$31.80** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $24.08 (NAV) + 0.30 × $31.80 (strip) = **$26.40**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.30 |
| 95% | $26.40 |
| 100% | $26.43 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.61× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **469,143** | — |
| 10-year mean | 35,790 | 13.11× |
| 12-month FFA | 129,946 | 3.61× |
| Current spot | 276,399 | 1.70× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (66% of fleet value) | 559,593 | 13.99× |
| Suezmax (20% of fleet value) | 306,874 | 11.06× |
| LR2 (14% of fleet value) | 278,894 | 10.10× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.21 | $21.47 | $24.73 | $27.99 | $31.25 |
| **-15%** | $19.04 | $22.30 | $25.56 | $28.82 | $32.08 |
| **+0%** | $19.88 | $23.14 | $26.40 | $29.66 | $32.92 |
| **+15%** | $20.71 | $23.97 | $27.23 | $30.49 | $33.75 |
| **+30%** | $21.55 | $24.81 | $28.07 | $31.33 | $34.59 |

_Current price $40.93. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.40** is -35.5% vs the current price ($40.93) and -13.4% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$469,143/day** (3.61× the current forward) — 13.1× the value-weighted 10-yr mean ($35,790, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $71.8M (+16%) / 10yr $50.6M (+12%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.7M (+11%) / 10yr $25.8M (+7%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.9M (-9%) / 10yr $22.2M (-11%) [n=22], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

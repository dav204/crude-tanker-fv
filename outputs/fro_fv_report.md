# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $34.50
- **Model fair value:** $27.09
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,433.8 |
| Fleet value — Suezmax | 1,607.0 |
| Fleet value — LR2 | 1,179.3 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,431.2** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$24.40** |
| NAV / share (ex yard discount) | $25.71 |
| Yard-discount impact / share | $-1.31 |

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
| Terminal value (NAV, q9) | | | | 19.88 | 15.72 |
| **DivStrip implied price** | | | | | **$33.39** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $24.40 (NAV) + 0.30 × $33.39 (strip) = **$27.09**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.26 |
| 95% | $27.09 |
| 100% | $27.37 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **2.39× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **311,332** | — |
| 10-year mean | 35,826 | 8.69× |
| 12-month FFA | 130,161 | 2.39× |
| Current spot | 277,356 | 1.12× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (66% of fleet value) | 370,745 | 9.27× |
| Suezmax (20% of fleet value) | 203,312 | 7.33× |
| LR2 (14% of fleet value) | 184,774 | 6.69× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.79 | $22.15 | $25.50 | $28.85 | $32.21 |
| **-15%** | $19.59 | $22.94 | $26.30 | $29.65 | $33.00 |
| **+0%** | $20.39 | $23.74 | $27.09 | $30.45 | $33.80 |
| **+15%** | $21.19 | $24.54 | $27.89 | $31.25 | $34.60 |
| **+30%** | $21.98 | $25.34 | $28.69 | $32.04 | $35.40 |

_Current price $34.50. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$27.09** is -21.5% vs the current price ($34.50) and -11.2% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$311,332/day** (2.39× the current forward) — 8.7× the value-weighted 10-yr mean ($35,826, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $81.6M (+3%) / 10yr $60.9M (-10%) [n=12], Cape 5yr $71.9M (+16%) / 10yr $50.7M (+13%) [n=25], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $34.2M (+7%) / 10yr $24.7M (+3%) [n=4], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.7M (-10%) / 10yr $21.8M (-13%) [n=17], VLCC 5yr $112.7M (-18%) / 10yr $90.9M (-18%) [n=11]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

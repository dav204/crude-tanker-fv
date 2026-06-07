# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $34.50
- **Model fair value:** $31.37
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $388,300/day is 9.7x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 6,161.0 |
| Fleet value — Suezmax | 1,784.3 |
| Fleet value — LR2 | 1,252.1 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **6,408.6** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$28.79** |
| NAV / share (ex yard discount) | $30.20 |
| Yard-discount impact / share | $-1.41 |

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
| Terminal value (NAV, q9) | | | | 24.93 | 19.71 |
| **DivStrip implied price** | | | | | **$37.38** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $28.79 (NAV) + 0.30 × $37.38 (strip) = **$31.37**

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $30.53 |
| 95% | $31.37 |
| 100% | $31.64 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.59× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **207,932** | — |
| 10-year mean | 35,935 | 5.79× |
| 12-month FFA | 130,836 | 1.59× |
| Current spot | 280,312 | 0.74× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (67% of fleet value) | 246,335 | 6.16× |
| Suezmax (19% of fleet value) | 135,087 | 4.87× |
| LR2 (14% of fleet value) | 122,770 | 4.45× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $22.21 | $25.99 | $29.77 | $33.55 | $37.33 |
| **-15%** | $23.01 | $26.79 | $30.57 | $34.35 | $38.13 |
| **+0%** | $23.80 | $27.58 | $31.37 | $35.15 | $38.93 |
| **+15%** | $24.60 | $28.38 | $32.16 | $35.94 | $39.72 |
| **+30%** | $25.40 | $29.18 | $32.96 | $36.74 | $40.52 |

_Current price $34.50. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$31.37** is -9.1% vs the current price ($34.50) and +2.8% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$207,932/day** (1.59× the current forward) — 5.8× the value-weighted 10-yr mean ($35,935, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

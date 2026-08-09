# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $39.74
- **Model fair value:** $27.60
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,647.8 |
| Fleet value — Suezmax | 1,633.7 |
| Fleet value — LR2 | 1,147.9 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,640.6** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$25.34** |
| NAV / share (ex yard discount) | $26.63 |
| Yard-discount impact / share | $-1.30 |

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
| Terminal value (NAV, q9) | | | | 19.24 | 15.21 |
| **DivStrip implied price** | | | | | **$32.88** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $25.34 (NAV) + 0.30 × $32.88 (strip) = **$27.60**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 26.50 | 96% |
| Balance-sheet net | -8.77 | -32% |
| Discounted DPS (strip, 8-10q) | 5.30 | 19% |
| Discounted terminal (aged NAV) | 4.56 | 17% |
| **Blend FV** | **27.60** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.46 = **84%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $27.50 |
| 95% | $27.60 |
| 100% | $27.63 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.18× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **416,150** | — |
| 10-year mean | 35,937 | 11.58× |
| 12-month FFA | 130,845 | 3.18× |
| Current spot | 221,249 | 1.88× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (67% of fleet value) | 492,974 | 12.32× |
| Suezmax (19% of fleet value) | 270,340 | 9.74× |
| LR2 (14% of fleet value) | 245,692 | 8.90× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $19.17 | $22.55 | $25.93 | $29.31 | $32.69 |
| **-15%** | $20.01 | $23.39 | $26.77 | $30.14 | $33.52 |
| **+0%** | $20.84 | $24.22 | $27.60 | $30.98 | $34.36 |
| **+15%** | $21.68 | $25.06 | $28.44 | $31.82 | $35.19 |
| **+30%** | $22.51 | $25.89 | $29.27 | $32.65 | $36.03 |

_Current price $39.74. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$27.60** is -30.5% vs the current price ($39.74) and -9.5% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$416,150/day** (3.18× the current forward) — 11.6× the value-weighted 10-yr mean ($35,937, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

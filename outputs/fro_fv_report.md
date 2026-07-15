# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $38.38
- **Model fair value:** $26.54
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,394.4 |
| Fleet value — Suezmax | 1,607.0 |
| Fleet value — LR2 | 1,179.3 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,391.8** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$24.22** |
| NAV / share (ex yard discount) | $25.52 |
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
| Terminal value (NAV, q9) | | | | 18.05 | 14.27 |
| **DivStrip implied price** | | | | | **$31.94** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$155,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$111,500/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $111,500 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $24.22 (NAV) + 0.30 × $31.94 (strip) = **$26.54**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.72 | 97% |
| Balance-sheet net | -8.77 | -33% |
| Discounted DPS (strip, 8-10q) | 5.30 | 20% |
| Discounted terminal (aged NAV) | 4.28 | 16% |
| **Blend FV** | **26.54** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.45 = **83%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.44 |
| 95% | $26.54 |
| 100% | $26.57 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.13× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **406,711** | — |
| 10-year mean | 35,805 | 11.36× |
| 12-month FFA | 130,041 | 3.13× |
| Current spot | 218,887 | 1.86× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (66% of fleet value) | 484,772 | 12.12× |
| Suezmax (20% of fleet value) | 265,843 | 9.58× |
| LR2 (14% of fleet value) | 241,604 | 8.75× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.32 | $21.59 | $24.86 | $28.14 | $31.41 |
| **-15%** | $19.15 | $22.43 | $25.70 | $28.97 | $32.25 |
| **+0%** | $19.99 | $23.26 | $26.54 | $29.81 | $33.08 |
| **+15%** | $20.82 | $24.10 | $27.37 | $30.64 | $33.92 |
| **+30%** | $21.66 | $24.93 | $28.21 | $31.48 | $34.75 |

_Current price $38.38. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.54** is -30.9% vs the current price ($38.38) and -13.0% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$406,711/day** (3.13× the current forward) — 11.4× the value-weighted 10-yr mean ($35,805, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

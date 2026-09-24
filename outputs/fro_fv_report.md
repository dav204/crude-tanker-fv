# FRO — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $47.56
- **Model fair value:** $26.71
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $790,800/day is 19.8x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,542.0 |
| Fleet value — Suezmax | 1,478.7 |
| Fleet value — LR2 | 1,122.8 |
| + Cash & equivalents | 322.3 |
| + Working capital (net) | 368.0 |
| − Total debt | 2,434.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 601.1 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,797.9** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$26.04** |
| NAV / share (ex yard discount) | $27.25 |
| Yard-discount impact / share | $-1.21 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 154,800 | 129,899 | 2.877 | 2.734 | 2.663 |
| Q2 | 154,800 | 129,899 | 2.998 | 2.848 | 2.703 |
| Q3 | 105,700 | 100,439 | 2.067 | 1.964 | 1.816 |
| Q4 | 105,700 | 100,439 | 2.067 | 1.964 | 1.769 |
| Q5 | 55,050 | 70,049 | 1.152 | 1.094 | 0.960 |
| Q6 | 55,050 | 70,049 | 1.152 | 1.094 | 0.935 |
| Q7 | 55,050 | 70,049 | 1.152 | 1.094 | 0.911 |
| Q8 | 55,050 | 70,049 | 1.152 | 1.094 | 0.888 |
| Σ discounted DPS | | | | | 12.65 |
| Terminal value (NAV, q9) | | | | 19.75 | 15.62 |
| **DivStrip implied price** | | | | | **$28.26** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$130,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.57×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $26.04 (NAV) + 0.30 × $28.26 (strip) = **$26.71**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.61 | 96% |
| Balance-sheet net | -7.38 | -28% |
| Discounted DPS (strip, 8-10q) | 3.79 | 14% |
| Discounted terminal (aged NAV) | 4.68 | 18% |
| **Blend FV** | **26.71** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.55 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.63 |
| 95% | $26.71 |
| 100% | $26.74 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **6.63× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **766,008** | — |
| 10-year mean | 36,065 | 21.24× |
| 12-month FFA | 115,526 | 6.63× |
| Current spot | 572,684 | 1.34× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (68% of fleet value) | 863,636 | 21.59× |
| Suezmax (18% of fleet value) | 636,870 | 22.95× |
| LR2 (14% of fleet value) | 454,196 | 16.46× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $19.08 | $22.34 | $25.60 | $28.86 | $32.12 |
| **-15%** | $19.63 | $22.89 | $26.15 | $29.42 | $32.68 |
| **+0%** | $20.19 | $23.45 | $26.71 | $29.97 | $33.23 |
| **+15%** | $20.74 | $24.00 | $27.26 | $30.53 | $33.79 |
| **+30%** | $21.30 | $24.56 | $27.82 | $31.08 | $34.34 |

_Current price $47.56. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.71** is -43.8% vs the current price ($47.56) and -12.4% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$766,008/day** (6.63× the current forward) — 21.2× the value-weighted 10-yr mean ($36,065, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

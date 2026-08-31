# FRO — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $44.19
- **Model fair value:** $26.58
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
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
| Q1 | 179,650 | 144,809 | 2.965 | 2.817 | 2.744 |
| Q2 | 179,650 | 144,809 | 3.101 | 2.946 | 2.796 |
| Q3 | 105,700 | 100,439 | 1.917 | 1.821 | 1.684 |
| Q4 | 105,700 | 100,439 | 1.917 | 1.821 | 1.641 |
| Q5 | 48,850 | 66,329 | 1.053 | 1.001 | 0.878 |
| Q6 | 48,850 | 66,329 | 1.053 | 1.001 | 0.856 |
| Q7 | 48,850 | 66,329 | 1.053 | 1.001 | 0.834 |
| Q8 | 48,850 | 66,329 | 1.053 | 1.001 | 0.812 |
| Σ discounted DPS | | | | | 12.24 |
| Terminal value (NAV, q9) | | | | 19.72 | 15.60 |
| **DivStrip implied price** | | | | | **$27.84** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.44×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $26.04 (NAV) + 0.30 × $27.84 (strip) = **$26.58**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.61 | 96% |
| Balance-sheet net | -7.38 | -28% |
| Discounted DPS (strip, 8-10q) | 3.67 | 14% |
| Discounted terminal (aged NAV) | 4.68 | 18% |
| **Blend FV** | **26.58** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.56 = **87%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $26.50 |
| 95% | $26.58 |
| 100% | $26.61 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.92× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **715,733** | — |
| 10-year mean | 36,065 | 19.85× |
| 12-month FFA | 120,838 | 5.92× |
| Current spot | 357,205 | 2.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (68% of fleet value) | 845,074 | 21.13× |
| Suezmax (18% of fleet value) | 524,043 | 18.89× |
| LR2 (14% of fleet value) | 329,767 | 11.95× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.99 | $22.25 | $25.51 | $28.77 | $32.03 |
| **-15%** | $19.52 | $22.78 | $26.05 | $29.31 | $32.57 |
| **+0%** | $20.06 | $23.32 | $26.58 | $29.84 | $33.11 |
| **+15%** | $20.60 | $23.86 | $27.12 | $30.38 | $33.64 |
| **+30%** | $21.13 | $24.39 | $27.66 | $30.92 | $34.18 |

_Current price $44.19. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$26.58** is -39.8% vs the current price ($44.19) and -12.8% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$715,733/day** (5.92× the current forward) — 19.8× the value-weighted 10-yr mean ($36,065, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

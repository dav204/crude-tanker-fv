# CAPT — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $16.46
- **Model fair value:** $16.95
- **Analyst target:** $18.90

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 2,442.7 |
| Fleet value — Suezmax | 1,145.5 |
| Fleet value — Aframax | 287.3 |
| Fleet value — LR2 | 374.6 |
| + Cash & equivalents | 350.2 |
| + Working capital (net) | 42.0 |
| − Total debt | 520.8 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 1,806.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,315.0** |
| Diluted shares | 133,692,593 |
| **NAV / share** | **$17.32** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 97,076 | 0.641 | 0.288 | 0.281 |
| Q2 | 179,650 | 97,076 | 0.811 | 0.365 | 0.346 |
| Q3 | 105,700 | 97,076 | 0.500 | 0.225 | 0.208 |
| Q4 | 105,700 | 97,076 | 0.631 | 0.284 | 0.256 |
| Q5 | 48,850 | 97,076 | 0.510 | 0.229 | 0.201 |
| Q6 | 48,850 | 97,076 | 0.706 | 0.318 | 0.272 |
| Q7 | 48,850 | 97,076 | 0.854 | 0.384 | 0.320 |
| Q8 | 48,850 | 97,076 | 1.025 | 0.461 | 0.374 |
| Σ discounted DPS | | | | | 2.26 |
| Terminal value (NAV, q9) | | | | 17.49 | 13.83 |
| **DivStrip implied price** | | | | | **$16.09** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.36×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $17.32 (NAV) + 0.30 × $16.09 (strip) = **$16.95**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 22.25 | 131% |
| Balance-sheet net | -10.13 | -60% |
| Discounted DPS (strip, 8-10q) | 0.68 | 4% |
| Discounted terminal (aged NAV) | 4.15 | 24% |
| **Blend FV** | **16.95** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.86 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $17.00 |
| 95% | $17.03 |
| 100% | $17.04 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.55× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **63,532** | — |
| 10-year mean | 35,367 | 1.80× |
| 12-month FFA | 114,517 | 0.55× |
| Current spot | 313,645 | 0.20× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (57% of fleet value) | 79,154 | 1.98× |
| Suezmax (27% of fleet value) | 49,085 | 1.77× |
| LR2 (9% of fleet value) | 30,888 | 1.12× |
| Aframax (7% of fleet value) | 30,888 | 0.85× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $10.80 | $13.71 | $16.62 | $19.53 | $22.44 |
| **-15%** | $10.97 | $13.88 | $16.78 | $19.69 | $22.60 |
| **+0%** | $11.13 | $14.04 | $16.95 | $19.86 | $22.77 |
| **+15%** | $11.29 | $14.20 | $17.11 | $20.02 | $22.93 |
| **+30%** | $11.46 | $14.36 | $17.27 | $20.18 | $23.09 |

_Current price $16.46. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$16.95** is +2.9% vs the current price ($16.46) and -10.3% vs the analyst target ($18.90). The current price implies the fleet earning a value-weighted blended **$63,532/day** (0.55× the current forward) — 1.8× the value-weighted 10-yr mean ($35,367, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

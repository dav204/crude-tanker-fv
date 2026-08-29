# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $42.27
- **Model fair value:** $59.21
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 233.5 |
| Fleet value — Suezmax | 1,015.0 |
| Fleet value — Aframax | 1,425.6 |
| Fleet value — LR2 | 229.0 |
| Fleet value — LR1 | 250.6 |
| Fleet value — MR | 109.5 |
| Fleet value — Handysize | 26.9 |
| Fleet value — LNGC | 443.2 |
| + Cash & equivalents | 321.4 |
| + Working capital (net) | 174.7 |
| − Total debt | 2,136.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 442.7 |
| **= NAV total** | **2,655.9** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$88.16** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 59,900 | 32,640 | 4.238 | 1.180 | 1.150 |
| Q2 | 59,900 | 32,640 | 4.238 | 1.180 | 1.120 |
| Q3 | 51,450 | 31,432 | 3.700 | 1.078 | 0.997 |
| Q4 | 51,450 | 31,432 | 3.700 | 1.078 | 0.971 |
| Q5 | 38,000 | 29,508 | 3.218 | 0.986 | 0.866 |
| Q6 | 38,000 | 29,508 | 3.218 | 0.986 | 0.844 |
| Q7 | 38,000 | 29,508 | 3.218 | 0.986 | 0.822 |
| Q8 | 38,000 | 29,508 | 3.218 | 0.986 | 0.801 |
| Σ discounted DPS | | | | | 7.57 |
| Terminal value (NAV, q9) | | | | 57.94 | 45.81 |
| **DivStrip implied price** | | | | | **$53.38** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$55,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$51,450/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $51,450 / 10-yr mean $36,483 = **1.66×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $61.71 (NAV) + 0.30 × $53.38 (strip) = **$59.21**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 86.74 | 146% |
| Balance-sheet net | -25.03 | -42% |
| §15 governance haircut | -18.51 | -31% |
| Discounted DPS (strip, 8-10q) | 2.27 | 4% |
| Discounted terminal (aged NAV) | 13.74 | 23% |
| **Blend FV** | **59.21** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.86 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $61.02 |
| 95% | $61.46 |
| 100% | $61.61 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$88.16** ≥ price **$42.27** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,198 | 0.00× |
| 12-month FFA | 69,908 | 0.00× |
| Current spot | 93,961 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (38% of fleet value) | 0 | 0.00× |
| Suezmax (27% of fleet value) | 0 | 0.00× |
| LNGC (12% of fleet value) | 0 | 0.00× |
| LR1 (7% of fleet value) | 0 | 0.00× |
| VLCC (6% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $43.17 | $50.87 | $58.57 | $66.28 | $73.98 |
| **-15%** | $43.48 | $51.19 | $58.89 | $66.60 | $74.30 |
| **+0%** | $43.80 | $51.51 | $59.21 | $66.91 | $74.62 |
| **+15%** | $44.12 | $51.83 | $59.53 | $67.23 | $74.94 |
| **+30%** | $44.44 | $52.15 | $59.85 | $67.55 | $75.26 |

_Current price $42.27. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$59.21** is +40.1% vs the current price ($42.27) and +15.0% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $88.16 ≥ $42.27); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

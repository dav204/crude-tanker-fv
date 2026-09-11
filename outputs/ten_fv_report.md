# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $44.71
- **Model fair value:** $59.49
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
| Q1 | 81,000 | 35,657 | 4.669 | 1.262 | 1.230 |
| Q2 | 81,000 | 35,657 | 4.669 | 1.262 | 1.198 |
| Q3 | 56,000 | 32,082 | 3.895 | 1.115 | 1.031 |
| Q4 | 56,000 | 32,082 | 3.895 | 1.115 | 1.004 |
| Q5 | 40,000 | 29,794 | 3.280 | 0.998 | 0.876 |
| Q6 | 40,000 | 29,794 | 3.280 | 0.998 | 0.854 |
| Q7 | 40,000 | 29,794 | 3.280 | 0.998 | 0.832 |
| Q8 | 40,000 | 29,794 | 3.280 | 0.998 | 0.810 |
| Σ discounted DPS | | | | | 7.83 |
| Terminal value (NAV, q9) | | | | 58.79 | 46.49 |
| **DivStrip implied price** | | | | | **$54.32** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$68,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,000 / 10-yr mean $36,483 = **1.89×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $61.71 (NAV) + 0.30 × $54.32 (strip) = **$59.49**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 86.74 | 146% |
| Balance-sheet net | -25.03 | -42% |
| §15 governance haircut | -18.51 | -31% |
| Discounted DPS (strip, 8-10q) | 2.35 | 4% |
| Discounted terminal (aged NAV) | 13.95 | 23% |
| **Blend FV** | **59.49** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.86 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $61.40 |
| 95% | $61.87 |
| 100% | $62.03 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$88.16** ≥ price **$44.71** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,198 | 0.00× |
| 12-month FFA | 77,752 | 0.00× |
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
| **-30%** | $43.36 | $51.07 | $58.77 | $66.47 | $74.18 |
| **-15%** | $43.72 | $51.43 | $59.13 | $66.83 | $74.54 |
| **+0%** | $44.09 | $51.79 | $59.49 | $67.20 | $74.90 |
| **+15%** | $44.45 | $52.15 | $59.85 | $67.56 | $75.26 |
| **+30%** | $44.81 | $52.51 | $60.22 | $67.92 | $75.62 |

_Current price $44.71. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$59.49** is +33.1% vs the current price ($44.71) and +15.5% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $88.16 ≥ $44.71); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

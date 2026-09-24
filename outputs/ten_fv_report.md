# TEN — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $46.97
- **Model fair value:** $62.06
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $790,800/day is 19.8x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 231.3 |
| Fleet value — Suezmax | 1,069.9 |
| Fleet value — Aframax | 1,407.1 |
| Fleet value — LR2 | 225.4 |
| Fleet value — LR1 | 245.5 |
| Fleet value — MR | 108.6 |
| Fleet value — Handysize | 26.2 |
| Fleet value — LNGC | 440.2 |
| + Cash & equivalents | 466.1 |
| + Working capital (net) | 65.4 |
| − Total debt | 2,102.2 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 470.1 |
| **= NAV total** | **2,769.2** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$91.91** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,000 | 35,657 | 4.806 | 1.288 | 1.255 |
| Q2 | 81,000 | 35,657 | 4.806 | 1.288 | 1.223 |
| Q3 | 56,000 | 32,082 | 4.032 | 1.141 | 1.055 |
| Q4 | 56,000 | 32,082 | 4.032 | 1.141 | 1.028 |
| Q5 | 40,000 | 29,794 | 3.418 | 1.024 | 0.899 |
| Q6 | 40,000 | 29,794 | 3.418 | 1.024 | 0.876 |
| Q7 | 40,000 | 29,794 | 3.418 | 1.024 | 0.853 |
| Q8 | 40,000 | 29,794 | 3.418 | 1.024 | 0.831 |
| Σ discounted DPS | | | | | 8.02 |
| Terminal value (NAV, q9) | | | | 61.62 | 48.72 |
| **DivStrip implied price** | | | | | **$56.75** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$68,500/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,000/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,000 / 10-yr mean $36,483 = **1.90×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $64.34 (NAV) + 0.30 × $56.75 (strip) = **$62.06**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 87.23 | 141% |
| Balance-sheet net | -22.89 | -37% |
| §15 governance haircut | -19.30 | -31% |
| Discounted DPS (strip, 8-10q) | 2.41 | 4% |
| Discounted terminal (aged NAV) | 14.62 | 24% |
| **Blend FV** | **62.06** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.86 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $64.04 |
| 95% | $64.52 |
| 100% | $64.69 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$91.91** ≥ price **$46.97** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,050 | 0.00× |
| 12-month FFA | 78,089 | 0.00× |
| Current spot | 128,320 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (37% of fleet value) | 0 | 0.00× |
| Suezmax (28% of fleet value) | 0 | 0.00× |
| LNGC (12% of fleet value) | 0 | 0.00× |
| LR1 (7% of fleet value) | 0 | 0.00× |
| VLCC (6% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $45.86 | $53.60 | $61.34 | $69.08 | $76.82 |
| **-15%** | $46.22 | $53.96 | $61.70 | $69.44 | $77.18 |
| **+0%** | $46.58 | $54.32 | $62.06 | $69.80 | $77.54 |
| **+15%** | $46.95 | $54.68 | $62.42 | $70.16 | $77.90 |
| **+30%** | $47.31 | $55.05 | $62.78 | $70.52 | $78.26 |

_Current price $46.97. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$62.06** is +32.1% vs the current price ($46.97) and +20.5% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $91.91 ≥ $46.97); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.4M (+20%) / 10yr $29.4M (+23%) [n=17], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.7M (-7%) / 10yr $24.5M (-2%) [n=48], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

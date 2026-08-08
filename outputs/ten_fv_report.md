# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $39.14
- **Model fair value:** $59.78
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 213.5 |
| Fleet value — Suezmax | 1,015.0 |
| Fleet value — Aframax | 1,425.6 |
| Fleet value — LR2 | 231.3 |
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
| **= NAV total** | **2,638.2** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$87.57** |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Aframax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 75,000 | 34,799 | 4.336 | 1.199 | 1.168 |
| Q2 | 88,000 | 36,658 | 4.758 | 1.279 | 1.214 |
| Q3 | 82,000 | 35,800 | 4.580 | 1.245 | 1.151 |
| Q4 | 64,000 | 33,226 | 4.007 | 1.136 | 1.024 |
| Q5 | 59,000 | 32,511 | 3.852 | 1.107 | 0.972 |
| Q6 | 70,000 | 34,084 | 4.218 | 1.176 | 1.006 |
| Q7 | 74,000 | 34,656 | 4.339 | 1.199 | 0.999 |
| Q8 | 56,000 | 32,082 | 3.769 | 1.091 | 0.886 |
| Σ discounted DPS | | | | | 8.42 |
| Terminal value (NAV, q9) | | | | 60.48 | 47.83 |
| **DivStrip implied price** | | | | | **$56.25** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $36,483 = **1.75×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $61.30 (NAV) + 0.30 × $56.25 (strip) = **$59.78**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 86.33 | 144% |
| Balance-sheet net | -25.03 | -42% |
| §15 governance haircut | -18.39 | -31% |
| Discounted DPS (strip, 8-10q) | 2.53 | 4% |
| Discounted terminal (aged NAV) | 14.35 | 24% |
| **Blend FV** | **59.78** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.85 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $61.89 |
| 95% | $62.41 |
| 100% | $62.58 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$87.57** ≥ price **$39.14** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,182 | 0.00× |
| 12-month FFA | 80,238 | 0.00× |
| Current spot | 75,483 | 0.00× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Aframax (38% of fleet value) | 0 | 0.00× |
| Suezmax (27% of fleet value) | 0 | 0.00× |
| LNGC (12% of fleet value) | 0 | 0.00× |
| LR1 (7% of fleet value) | 0 | 0.00× |
| LR2 (6% of fleet value) | 0 | 0.00× |
| VLCC (6% of fleet value) | 0 | 0.00× |
| MR (3% of fleet value) | 0 | 0.00× |
| Handysize (1% of fleet value) | 0 | 0.00× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $43.53 | $51.19 | $58.86 | $66.53 | $74.19 |
| **-15%** | $43.99 | $51.65 | $59.32 | $66.99 | $74.65 |
| **+0%** | $44.45 | $52.12 | $59.78 | $67.45 | $75.11 |
| **+15%** | $44.91 | $52.58 | $60.24 | $67.91 | $75.58 |
| **+30%** | $45.37 | $53.04 | $60.70 | $68.37 | $76.04 |

_Current price $39.14. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$59.78** is +52.7% vs the current price ($39.14) and +16.1% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $87.57 ≥ $39.14); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

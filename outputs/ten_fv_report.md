# TEN — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $39.75
- **Model fair value:** $59.66
- **Analyst target:** $51.50

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax/LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 216.7 |
| Fleet value — Suezmax | 1,002.9 |
| Fleet value — Aframax | 1,425.6 |
| Fleet value — LR2 | 233.5 |
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
| **= NAV total** | **2,631.5** |
| Diluted shares | 30,127,603 |
| **NAV / share** | **$87.35** |

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
| Terminal value (NAV, q9) | | | | 60.42 | 47.78 |
| **DivStrip implied price** | | | | | **$56.20** |

_FFA spot is the Aframax forward curve that drives the strip cash flows; its 12-month average is **$77,250/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$56,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $56,250 / 10-yr mean $36,483 = **1.75×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $61.14 (NAV) + 0.30 × $56.20 (strip) = **$59.66**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 86.18 | 144% |
| Balance-sheet net | -25.03 | -42% |
| §15 governance haircut | -18.34 | -31% |
| Discounted DPS (strip, 8-10q) | 2.53 | 4% |
| Discounted terminal (aged NAV) | 14.33 | 24% |
| **Blend FV** | **59.66** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.85 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $61.76 |
| 95% | $62.28 |
| 100% | $62.45 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

**NAV alone covers the price.** NAV/share **$87.35** ≥ price **$39.75** at base cycle weighting, so the strip provides no extra hurdle — the implied breakeven floor is effectively zero (rates could fall to ~0 and the price would still be justified by vessel value alone). The market is pricing the fleet at a discount to NAV.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **0** | — |
| 10-year mean | 38,211 | 0.00× |
| 12-month FFA | 80,286 | 0.00× |
| Current spot | 75,485 | 0.00× |

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
| **-30%** | $43.43 | $51.08 | $58.74 | $66.39 | $74.04 |
| **-15%** | $43.89 | $51.54 | $59.20 | $66.85 | $74.50 |
| **+0%** | $44.35 | $52.00 | $59.66 | $67.31 | $74.97 |
| **+15%** | $44.81 | $52.46 | $60.12 | $67.77 | $75.43 |
| **+30%** | $45.27 | $52.93 | $60.58 | $68.23 | $75.89 |

_Current price $39.75. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$59.66** is +50.1% vs the current price ($39.75) and +15.8% vs the analyst target ($51.50). NAV alone covers the price (NAV/sh $87.35 ≥ $39.75); the dividend strip provides no extra hurdle, so the implied breakeven floor is effectively zero — the market is pricing the fleet at a discount to vessel value.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.1M (+2%) / 10yr $46.0M (+2%) [n=26], LR2 5yr $77.8M (-2%) / 10yr $61.7M (-9%) [n=11], MR 5yr $46.1M (+0%) / 10yr $34.4M (-0%) [n=21], Pana 5yr $35.5M (+11%) / 10yr $25.8M (+8%) [n=5], Suezmax 5yr $86.3M (-6%) / 10yr $69.6M (-13%) [n=19], Supra-Ultra 5yr $29.3M (-11%) / 10yr $22.4M (-10%) [n=22], VLCC 5yr $113.2M (-18%) / 10yr $92.5M (-17%) [n=10], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

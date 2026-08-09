# INSW — Fair Value Report

> **Valuation basis:** CRUDE SLEEVE only (66.2% of vessel value). FV and price are the CRUDE sleeve / CRUDE-ALLOCATED price $61.20 (= whole-company $92.41 × crude_share). Product sleeve (~34%) is EXCLUDED from the model FV — covered qualitatively only (v2 product strip pending). Do not compare directly to whole-company P/NAV without re-aggregating.

- **Report date:** 2026-Q1
- **Current price (crude-allocated):** $61.20
- **Model fair value:** $39.76
- **Analyst target (crude-allocated):** $52.65

## Data validation warnings

- spot TCE VLCC: $285,500/day is 7.1x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 707.0 |
| Fleet value — Suezmax | 800.7 |
| Fleet value — Aframax | 182.2 |
| Fleet value — LR1 | 86.4 |
| + Cash & equivalents | 249.6 |
| + Working capital (net) | 151.8 |
| − Total debt | 370.3 |
| − Lease liabilities | 5.3 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **1,802.1** |
| Diluted shares | 49,700,000 |
| **NAV / share** | **$36.26** |
| NAV / share (ex yard discount) | $37.15 |
| Yard-discount impact / share | $-0.89 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 81,500 | 3.882 | 2.838 | 2.765 |
| Q2 | 99,000 | 99,000 | 4.878 | 3.534 | 3.355 |
| Q3 | 92,000 | 92,000 | 4.426 | 3.218 | 2.976 |
| Q4 | 67,500 | 67,500 | 3.139 | 2.318 | 2.088 |
| Q5 | 60,000 | 60,000 | 2.762 | 2.053 | 1.802 |
| Q6 | 78,000 | 78,000 | 3.597 | 2.638 | 2.256 |
| Q7 | 81,500 | 81,500 | 3.872 | 2.830 | 2.358 |
| Q8 | 56,500 | 56,500 | 2.573 | 1.921 | 1.559 |
| Σ discounted DPS | | | | | 19.16 |
| Terminal value (NAV, q9) | | | | 36.38 | 28.76 |
| **DivStrip implied price** | | | | | **$47.92** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **2.36×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $36.26 (NAV) + 0.30 × $47.92 (strip) = **$39.76**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 25.02 | 63% |
| Balance-sheet net | 0.36 | 1% |
| Discounted DPS (strip, 8-10q) | 5.75 | 14% |
| Discounted terminal (aged NAV) | 8.63 | 22% |
| **Blend FV** | **39.76** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.60 = **88%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $39.85 |
| 95% | $39.99 |
| 100% | $40.04 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **3.40× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **380,065** | — |
| 10-year mean | 33,513 | 11.34× |
| 12-month FFA | 111,691 | 3.40× |
| Current spot | 174,245 | 2.18× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (45% of fleet value) | 289,241 | 10.42× |
| VLCC (40% of fleet value) | 527,439 | 13.19× |
| Aframax (10% of fleet value) | 262,869 | 7.21× |
| LR1 (5% of fleet value) | 262,869 | 9.52× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $30.75 | $33.91 | $37.08 | $40.25 | $43.42 |
| **-15%** | $32.08 | $35.25 | $38.42 | $41.59 | $44.76 |
| **+0%** | $33.42 | $36.59 | $39.76 | $42.93 | $46.09 |
| **+15%** | $34.76 | $37.93 | $41.10 | $44.27 | $47.43 |
| **+30%** | $36.10 | $39.27 | $42.44 | $45.60 | $48.77 |

_Current price $61.20. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$39.76** is -35.0% vs the current price ($61.20) and -24.5% vs the analyst target ($52.65). The current price implies the fleet earning a value-weighted blended **$380,065/day** (3.40× the current forward) — 11.3× the value-weighted 10-yr mean ($33,513, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.8M (-7%) / 10yr $24.5M (-2%) [n=44], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- HYBRID crude carve-out (METHODOLOGY 6): crude sleeve = 66.2% of vessel value ($1,776M crude vs $906M product). Price/target shown are crude-ALLOCATED (whole-company x crude_share); balance sheet, G&A and corporate debt pro-rated, LR1-secured ECA debt held with the product sleeve.
- Crude sleeve (this model): -35% vs the crude-allocated price. Product sleeve (qualitative, awaiting v2): ~34% of vessel value, held at current Compass values. Product rates have corrected MORE than crude week-over-week (MR -52%, LR2 -28% vs Aframax/Suezmax/VLCC -7 to -8%), so product is LEADING the MoU normalization — a static-Compass product NAV likely OVERSTATES fair value once a v2 product strip is incorporated. Whole-company decision deferred to v2.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.

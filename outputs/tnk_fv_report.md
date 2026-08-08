# TNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $77.25
- **Model fair value:** $86.17
- **Analyst target:** $75.00

## Data validation warnings

- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 934.9 |
| Fleet value — Aframax | 794.4 |
| + Cash & equivalents | 1,211.6 |
| + Working capital (net) | 149.8 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 156.6 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,934.0** |
| Diluted shares | 34,680,112 |
| **NAV / share** | **$84.60** |
| NAV / share (ex yard discount) | $85.82 |
| Yard-discount impact / share | $-1.22 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 76,517 | 5.138 | 1.534 | 1.495 |
| Q2 | 99,000 | 90,342 | 6.182 | 1.796 | 1.704 |
| Q3 | 92,000 | 84,812 | 5.734 | 1.684 | 1.557 |
| Q4 | 67,500 | 65,457 | 4.280 | 1.320 | 1.189 |
| Q5 | 60,000 | 59,532 | 3.854 | 1.213 | 1.065 |
| Q6 | 78,000 | 73,752 | 4.839 | 1.460 | 1.248 |
| Q7 | 81,500 | 76,517 | 5.100 | 1.525 | 1.271 |
| Q8 | 56,500 | 56,767 | 3.630 | 1.157 | 0.939 |
| Σ discounted DPS | | | | | 10.47 |
| Terminal value (NAV, q9) | | | | 100.38 | 79.37 |
| **DivStrip implied price** | | | | | **$89.84** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **1.91×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $84.60 (NAV) + 0.30 × $89.84 (strip) = **$86.17**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 34.90 | 41% |
| Balance-sheet net | 24.32 | 28% |
| Discounted DPS (strip, 8-10q) | 3.14 | 4% |
| Discounted terminal (aged NAV) | 23.81 | 28% |
| **Blend FV** | **86.17** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $86.85 |
| 95% | $87.04 |
| 100% | $87.10 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.11× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **8,968** | — |
| 10-year mean | 31,760 | 0.28× |
| 12-month FFA | 81,440 | 0.11× |
| Current spot | 86,947 | 0.10× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (54% of fleet value) | 9,360 | 0.34× |
| Aframax (46% of fleet value) | 8,507 | 0.23× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $74.35 | $78.76 | $83.17 | $87.57 | $91.98 |
| **-15%** | $75.86 | $80.26 | $84.67 | $89.08 | $93.48 |
| **+0%** | $77.36 | $81.77 | $86.17 | $90.58 | $94.98 |
| **+15%** | $78.87 | $83.27 | $87.68 | $92.08 | $96.49 |
| **+30%** | $80.37 | $84.78 | $89.18 | $93.59 | $97.99 |

_Current price $77.25. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$86.17** is +11.6% vs the current price ($77.25) and +14.9% vs the analyst target ($75.00). The current price implies the fleet earning a value-weighted blended **$8,968/day** (0.11× the current forward) — 0.3× the value-weighted 10-yr mean ($31,760, i.e. the market is pricing distress), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.

# TNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $79.95
- **Model fair value:** $83.25
- **Analyst target:** $75.00

## Data validation warnings

- Aframax FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — Suezmax | 934.9 |
| Fleet value — Aframax | 794.4 |
| + Cash & equivalents | 996.2 |
| + Working capital (net) | 97.3 |
| − Total debt | 0.0 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 0.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **2,822.7** |
| Diluted shares | 34,643,858 |
| **NAV / share** | **$81.48** |
| NAV / share (ex yard discount) | $82.70 |
| Yard-discount impact / share | $-1.22 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (Suezmax, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 81,500 | 76,517 | 5.143 | 1.536 | 1.496 |
| Q2 | 99,000 | 90,342 | 6.189 | 1.797 | 1.706 |
| Q3 | 92,000 | 84,812 | 5.740 | 1.685 | 1.558 |
| Q4 | 67,500 | 65,457 | 4.284 | 1.321 | 1.190 |
| Q5 | 60,000 | 59,532 | 3.858 | 1.214 | 1.066 |
| Q6 | 78,000 | 73,752 | 4.844 | 1.461 | 1.249 |
| Q7 | 81,500 | 76,517 | 5.106 | 1.526 | 1.272 |
| Q8 | 56,500 | 56,767 | 3.634 | 1.158 | 0.940 |
| Σ discounted DPS | | | | | 10.48 |
| Terminal value (NAV, q9) | | | | 97.27 | 76.92 |
| **DivStrip implied price** | | | | | **$87.39** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$85,000/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$61,250/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $61,250 / 10-yr mean $27,747 = **1.91×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $81.48 (NAV) + 0.30 × $87.39 (strip) = **$83.25**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 34.94 | 42% |
| Balance-sheet net | 22.09 | 27% |
| Discounted DPS (strip, 8-10q) | 3.14 | 4% |
| Discounted terminal (aged NAV) | 23.07 | 28% |
| **Blend FV** | **83.25** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.88 = **96%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $83.93 |
| 95% | $84.11 |
| 100% | $84.18 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **0.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **54,688** | — |
| 10-year mean | 31,760 | 1.72× |
| 12-month FFA | 81,440 | 0.67× |
| Current spot | 86,947 | 0.63× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (54% of fleet value) | 57,078 | 2.06× |
| Aframax (46% of fleet value) | 51,874 | 1.42× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $71.42 | $75.83 | $80.24 | $84.65 | $89.06 |
| **-15%** | $72.93 | $77.34 | $81.75 | $86.16 | $90.57 |
| **+0%** | $74.43 | $78.84 | $83.25 | $87.66 | $92.07 |
| **+15%** | $75.94 | $80.35 | $84.76 | $89.17 | $93.58 |
| **+30%** | $77.44 | $81.85 | $86.26 | $90.67 | $95.08 |

_Current price $79.95. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$83.25** is +4.1% vs the current price ($79.95) and +11.0% vs the analyst target ($75.00). The current price implies the fleet earning a value-weighted blended **$54,688/day** (0.67× the current forward) — 1.7× the value-weighted 10-yr mean ($31,760, i.e. the market is pricing extended peak rates), and the market is below the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.4M (+5%) [n=31], LR2 5yr $76.1M (-4%) / 10yr $61.4M (-10%) [n=12], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $35.5M (+11%) / 10yr $26.3M (+9%) [n=8], Post-Panamax 5yr $33.6M (-1%) / 10yr $24.3M (-6%) [n=5], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $30.9M (-6%) / 10yr $24.4M (-2%) [n=33], VLCC 5yr $113.5M (-18%) / 10yr $89.4M (-19%) [n=11], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.

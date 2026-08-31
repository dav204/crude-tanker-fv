# TNK — Fair Value Report

- **Report date:** 2026-Q2
- **Current price:** $88.70
- **Model fair value:** $83.23
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
| Q1 | 118,900 | 106,063 | 5.759 | 1.690 | 1.646 |
| Q2 | 118,900 | 106,063 | 5.759 | 1.690 | 1.604 |
| Q3 | 58,050 | 57,992 | 3.508 | 1.127 | 1.042 |
| Q4 | 58,050 | 57,992 | 3.508 | 1.127 | 1.015 |
| Q5 | 26,950 | 33,423 | 2.015 | 0.754 | 0.661 |
| Q6 | 26,950 | 33,423 | 2.015 | 0.754 | 0.644 |
| Q7 | 26,950 | 33,423 | 2.015 | 0.754 | 0.628 |
| Q8 | 26,950 | 33,423 | 2.015 | 0.754 | 0.612 |
| Σ discounted DPS | | | | | 7.85 |
| Terminal value (NAV, q9) | | | | 91.26 | 72.16 |
| **DivStrip implied price** | | | | | **$80.01** |

_FFA spot is the Suezmax forward curve that drives the strip cash flows; its 12-month average is **$88,475/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$58,050/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $58,050 / 10-yr mean $27,747 = **1.78×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $84.60 (NAV) + 0.30 × $80.01 (strip) = **$83.23**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 34.90 | 42% |
| Balance-sheet net | 24.32 | 29% |
| Discounted DPS (strip, 8-10q) | 2.36 | 3% |
| Discounted terminal (aged NAV) | 21.65 | 26% |
| **Blend FV** | **83.23** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.90 = **97%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $83.76 |
| 95% | $83.91 |
| 100% | $83.96 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **1.77× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **130,174** | — |
| 10-year mean | 31,760 | 4.10× |
| 12-month FFA | 73,407 | 1.77× |
| Current spot | 76,589 | 1.70× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| Suezmax (54% of fleet value) | 156,894 | 5.65× |
| Aframax (46% of fleet value) | 98,729 | 2.71× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $72.29 | $76.70 | $81.10 | $85.51 | $89.91 |
| **-15%** | $73.35 | $77.76 | $82.16 | $86.57 | $90.97 |
| **+0%** | $74.41 | $78.82 | $83.23 | $87.63 | $92.04 |
| **+15%** | $75.48 | $79.88 | $84.29 | $88.69 | $93.10 |
| **+30%** | $76.54 | $80.94 | $85.35 | $89.75 | $94.16 |

_Current price $88.70. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$83.23** is -6.2% vs the current price ($88.70) and +11.0% vs the analyst target ($75.00). The current price implies the fleet earning a value-weighted blended **$130,174/day** (1.77× the current forward) — 4.1× the value-weighted 10-yr mean ($31,760, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $38.1M (+19%) / 10yr $28.9M (+20%) [n=14], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.

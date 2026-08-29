# FRO — Fair Value Report

- **Report date:** 2026-Q1
- **Current price:** $44.19
- **Model fair value:** $25.94
- **Analyst target:** $30.50

## Data validation warnings

- spot TCE VLCC: $488,900/day is 12.2x the 10-yr mean ($40,000) — unsustainable as a level. Confirm it is a genuine cycle spike (not a unit/source error) and do not anchor valuation to it.
- LR2 FFA forward curve is CONSTRUCTED (no market anchor) — built from the 12M TC + spot, not a Baltic / $MT / Worldscale series. Treat its dividend-strip contribution as indicative.

## NAV breakdown

| Item | $M |
|---|---:|
| Fleet value — VLCC | 5,647.8 |
| Fleet value — Suezmax | 1,633.7 |
| Fleet value — LR2 | 1,147.9 |
| + Cash & equivalents | 471.7 |
| + Working capital (net) | 295.6 |
| − Total debt | 2,631.1 |
| − Lease liabilities | 0.0 |
| − Newbuild commitments | 925.0 |
| + Newbuild advances | 0.0 |
| **= NAV total** | **5,640.6** |
| Diluted shares | 222,622,889 |
| **NAV / share** | **$25.34** |
| NAV / share (ex yard discount) | $26.63 |
| Yard-discount impact / share | $-1.30 |

## Dividend strip (r = 11%)

| Quarter | FFA spot (VLCC, $/day) | Blended TCE ($/day) | EPS | DPS | Disc. DPS |
|---|---:|---:|---:|---:|---:|
| Q1 | 179,650 | 151,255 | 3.094 | 2.939 | 2.863 |
| Q2 | 179,650 | 151,255 | 3.207 | 3.047 | 2.892 |
| Q3 | 105,700 | 99,490 | 1.958 | 1.860 | 1.720 |
| Q4 | 105,700 | 99,490 | 1.976 | 1.877 | 1.691 |
| Q5 | 48,850 | 59,695 | 1.004 | 0.954 | 0.837 |
| Q6 | 48,850 | 59,695 | 1.004 | 0.954 | 0.816 |
| Q7 | 48,850 | 59,695 | 1.004 | 0.954 | 0.795 |
| Q8 | 48,850 | 59,695 | 1.004 | 0.954 | 0.774 |
| Σ discounted DPS | | | | | 12.39 |
| Terminal value (NAV, q9) | | | | 18.91 | 14.95 |
| **DivStrip implied price** | | | | | **$27.34** |

_FFA spot is the VLCC forward curve that drives the strip cash flows; its 12-month average is **$142,675/day**. Blended TCE is that spot dampened by charter coverage. Cycle weighting (below) uses a different, more conservative input — the 12-month TC of **$105,700/day** — not this FFA average._

## Cycle weighting

- Cycle position = 12M TC (Compass) $105,700 / 10-yr mean $40,000 = **2.43×** → **late-cycle/peak**
- Weights: w_nav = 0.70, w_earn = 0.30

## Blended fair value

0.70 × $25.34 (NAV) + 0.30 × $27.34 (strip) = **$25.94**

### FV attribution

| Term | $/sh | share of FV |
|---|---:|---:|
| Vessel marks | 26.50 | 102% |
| Balance-sheet net | -8.77 | -34% |
| Discounted DPS (strip, 8-10q) | 3.72 | 14% |
| Discounted terminal (aged NAV) | 4.49 | 17% |
| **Blend FV** | **25.94** | 100% |

_Effective asset-value share = w_nav + w_earn × (terminal/strip) = 0.70 + 0.30 × 0.55 = **86%** — the strip contributes timing information (near-quarter contracted/forward cash) layered on an asset-value chassis (§2.1). Marks/curve provenance work carries proportionally more FV leverage than strip-side rate refreshes._

## Payout sensitivity

| Dividend payout | Fair value |
|---|---:|
| 80% | $25.86 |
| 95% | $25.94 |
| 100% | $25.97 |

_80% = stated-floor / discipline-reasserts; ~95% = base (recent peak behaviour with some conservatism); 100% = peak persists._

## Implied breakeven TCE

The current price requires the fleet to run at **5.67× the current forward curve** (inter-class rate ratios preserved). Headline is the value-weighted blended TCE across the fleet; per-class detail below.

| Benchmark (value-weighted blended) | $/day | vs breakeven |
|---|---:|---:|
| **Implied breakeven (blended)** | **682,553** | — |
| 10-year mean | 35,937 | 18.99× |
| 12-month FFA | 120,323 | 5.67× |
| Current spot | 352,875 | 1.93× |

| Per-class implied breakeven | $/day | × its 10-yr mean |
|---|---:|---:|
| VLCC (67% of fleet value) | 809,351 | 20.23× |
| Suezmax (19% of fleet value) | 501,891 | 18.09× |
| LR2 (14% of fleet value) | 315,827 | 11.44× |

## Sensitivity — fair value (rows: TCE shock, cols: vessel-value shock)

| TCE \ Vessel | -20% | -10% | +0% | +10% | +20% |
|---|---:|---:|---:|---:|---:|
| **-30%** | $18.01 | $21.39 | $24.77 | $28.15 | $31.53 |
| **-15%** | $18.59 | $21.97 | $25.35 | $28.73 | $32.11 |
| **+0%** | $19.18 | $22.56 | $25.94 | $29.32 | $32.70 |
| **+15%** | $19.77 | $23.15 | $26.53 | $29.90 | $33.28 |
| **+30%** | $20.35 | $23.73 | $27.11 | $30.49 | $33.87 |

_Current price $44.19. Cycle weights held at base across the grid._

## Divergence diagnosis

Tool fair value **$25.94** is -41.3% vs the current price ($44.19) and -15.0% vs the analyst target ($30.50). The current price implies the fleet earning a value-weighted blended **$682,553/day** (5.67× the current forward) — 19.0× the value-weighted 10-yr mean ($35,937, i.e. the market is pricing extended peak rates), and the market is above the forward curve.

## Modeling notes

- Mid-age value anchors **transaction-recalibrated** (METHODOLOGY 9.9): Aframax 5yr $78.7M (-0%) / 10yr $61.0M (-10%) [n=13], Cape 5yr $63.9M (+3%) / 10yr $47.7M (+6%) [n=34], LR2 5yr $74.3M (-6%) / 10yr $61.0M (-10%) [n=13], MR 5yr $46.0M (-0%) / 10yr $34.5M (-0%) [n=22], Pana 5yr $37.4M (+17%) / 10yr $28.5M (+19%) [n=13], Post-Panamax 5yr $36.0M (+6%) / 10yr $26.3M (+1%) [n=10], Suezmax 5yr $87.9M (-4%) / 10yr $70.6M (-12%) [n=20], Supra-Ultra 5yr $29.7M (-10%) / 10yr $23.9M (-4%) [n=43], VLCC 5yr $121.5M (-12%) / 10yr $100.2M (-10%) [n=14], VLGC 5yr $91.9M (-0%) / 10yr $80.0M (-0%) [n=7]. Newbuild + old-age anchors unchanged.
- Earning fleet varies over the strip per the manifest fleet_schedule (e.g. newbuild deliveries / sales); NAV is anchored at the report date.
- Vessel values carry a yard-quality discount (Chinese / ex-Hanjin-Subic yards); NAV is shown with and without it.
- LR2/Aframax vessels modeled as Aframax-equivalent (crude/dirty proxy) for v1; true clean-LR2 product rates would differ (v2: max of Aframax-crude and LR2-product).

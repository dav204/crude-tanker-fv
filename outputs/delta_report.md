# Pipeline Delta Report

- **This run:** 2026-06-22T16:04:37+00:00
- **Previous run:** 2026-06-22T15:33:40+00:00

## Headline changes (material moves)

- **CAPT:** broker spread +20.4pp; NAV/sh -15.2%
- **MPCC:** broker spread +8.1pp; NAV/sh -11.0%

## Input files changed since last run

- `inputs/data_sources.yaml` (modified)
- `inputs/fleet_manifests/capt.yaml` (modified)
- `inputs/fleet_manifests/fro.yaml` (modified)
- `inputs/fleet_manifests/mpcc.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $18.89 (no change) | $14.31 (no change) | $15.08 (no change) | $12.93 (no change) | TRIM/SHORT (overvalued) | +21.8pp (no change) |
| ECO | $52.48 (no change) | $36.67 (no change) | $39.33 (no change) | $33.71 (no change) | TRIM/SHORT (overvalued) | +17.4pp (no change) |
| FRO | $40.93 (no change) | $26.93 (-0.6%) | $29.18 (-0.6%) | $24.08 (-1.3%) | TRIM/SHORT (overvalued) | +23.1pp (+0.8pp) |
| INSW | $84.49 (no change) | $37.31 (no change) | $59.47 (no change) | $52.39 (no change) | TRIM/SHORT (overvalued) | +38.4pp (no change) |
| TNK | $74.45 (no change) | $73.94 (no change) | $73.72 (no change) | $77.47 (no change) | HOLD (fairly valued) | +24.6pp (no change) |
| NAT | $5.85 (no change) | $2.59 (no change) | $2.86 (no change) | $2.07 (no change) | TRIM/SHORT (overvalued) | +76.2pp (no change) |
| FLNG | $29.74 (no change) | $26.27 (no change) | $29.73 (no change) | $28.45 (no change) | HOLD (fairly valued) | -21.0pp (no change) |
| CCEC | $20.03 (no change) | $22.88 (no change) | $29.63 (no change) | $28.10 (no change) | BUY (undervalued) | -27.3pp (no change) |
| STNG | $80.58 (no change) | $74.00 (no change) | $73.13 (no change) | $80.35 (no change) | TRIM/SHORT (overvalued) | +38.5pp (no change) |
| HAFN | $7.23 (no change) | $5.59 (no change) | $5.77 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +29.5pp (no change) |
| TRMD | $29.41 (no change) | $26.09 (no change) | $26.68 (no change) | $25.43 (no change) | TRIM/SHORT (overvalued) | +30.4pp (no change) |
| ASC | $17.07 (no change) | $14.88 (no change) | $15.05 (no change) | $15.93 (no change) | TRIM/SHORT (overvalued) | +35.7pp (no change) |
| TEN | $38.29 (no change) | $57.74 (no change) | $62.23 (no change) | $87.56 (no change) | BUY (undervalued) | +42.5pp (no change) |
| CMDB | $16.90 (no change) | $20.00 (no change) | $19.98 (no change) | $32.49 (no change) | BUY (undervalued) | -18.9pp (no change) |
| SBLK | $25.81 (no change) | $26.00 (no change) | $25.98 (no change) | $26.57 (no change) | HOLD (fairly valued) | +16.6pp (no change) |
| GNK | $23.68 (no change) | $25.30 (no change) | $25.76 (no change) | $26.27 (no change) | BUY (undervalued) | +3.5pp (no change) |
| CAPT ⚑ | $13.24 (no change) | $15.24 (-8.8%) | $16.20 (-8.4%) | $15.05 (-15.2%) | BUY (undervalued) | +34.6pp (+20.4pp) |
| MPCC ⚑ | $2.54 (no change) | $1.99 (-6.6%) | $1.85 (-5.6%) | $2.02 (-11.0%) | TRIM/SHORT (overvalued) | +13.4pp (+8.1pp) |
| GSL | $37.89 (no change) | $33.61 (no change) | $31.76 (no change) | $38.59 (no change) | TRIM/SHORT (overvalued) | +25.0pp (no change) |
| BRUT | $5.40 (no change) | $9.79 (no change) | $10.65 (no change) | $9.40 (no change) | BUY (undervalued) | -40.7pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
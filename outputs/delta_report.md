# Pipeline Delta Report

- **This run:** 2026-06-30T13:13:01+00:00
- **Previous run:** 2026-06-29T23:45:25+00:00

## Headline changes (material moves)

- **SBLK:** broker spread -8.5pp; NAV/sh +9.0%

## Input files changed since last run

- `inputs/market_data/newbuild_convention.yaml` (new)
- `inputs/balance_sheets/sb_2026-Q1.yaml` (modified)
- `inputs/balance_sheets/sblk_2026-Q1.yaml` (modified)
- `inputs/fleet_manifests/mpcc.yaml` (modified)
- `inputs/fleet_manifests/sb.yaml` (modified)
- `inputs/fleet_manifests/sblk.yaml` (modified)
- `inputs/market_data/basis_status.yaml` (modified)
- `inputs/market_data/newbuild_contract_prices.yaml` (modified)
- `inputs/market_data/vessel_value_curves.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $17.08 (no change) | $14.15 (no change) | $14.92 (no change) | $13.10 (no change) | TRIM/SHORT (overvalued) | +13.8pp (no change) |
| ECO | $49.60 (no change) | $37.33 (no change) | $40.17 (no change) | $34.56 (no change) | TRIM/SHORT (overvalued) | +11.9pp (no change) |
| FRO | $35.44 (no change) | $26.54 (no change) | $28.82 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +13.8pp (no change) |
| INSW | $77.81 (no change) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +32.3pp (no change) |
| TNK | $65.99 (no change) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +12.4pp (no change) |
| NAT | $5.78 (no change) | $2.51 (no change) | $2.78 (no change) | $2.07 (no change) | TRIM/SHORT (overvalued) | +74.2pp (no change) |
| FLNG | $29.29 (no change) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -22.4pp (no change) |
| CCEC | $20.87 (no change) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -22.1pp (no change) |
| STNG | $70.09 (no change) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +24.7pp (no change) |
| HAFN | $6.86 (no change) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +25.5pp (no change) |
| TRMD | $26.31 (no change) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +20.9pp (no change) |
| ASC | $16.00 (no change) | $15.09 (no change) | $15.15 (no change) | $15.93 (no change) | TRIM/SHORT (overvalued) | +29.6pp (no change) |
| TEN | $35.76 (no change) | $61.29 (no change) | $65.49 (no change) | $88.70 (no change) | BUY (undervalued) | +29.3pp (no change) |
| CMDB | $17.99 (no change) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -7.8pp (no change) |
| SBLK ⚑ | $24.64 (no change) | $28.34 (+9.0%) | $28.37 (+8.8%) | $29.34 (+9.0%) | BUY (undervalued) | +2.5pp (-8.5pp) |
| GNK | $24.39 (no change) | $23.99 (no change) | $24.05 (no change) | $24.69 (no change) | HOLD (fairly valued) | +11.9pp (no change) |
| CAPT | $12.73 (no change) | $16.13 (no change) | $17.26 (no change) | $15.59 (no change) | BUY (undervalued) | +25.3pp (no change) |
| MPCC | $2.62 (no change) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +15.3pp (no change) |
| GSL | $37.74 (no change) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.4pp (no change) |
| BRUT | $5.21 (no change) | $9.84 (no change) | $10.81 (no change) | $9.40 (no change) | BUY (undervalued) | -45.8pp (no change) |
| CMBT | $14.08 (no change) | $15.26 (no change) | $16.07 (no change) | $15.87 (no change) | BUY (undervalued) | +20.1pp (no change) |
| SB | $6.36 (no change) | $10.30 (+5.1%) | $10.10 (+4.4%) | $10.61 (+2.9%) | BUY (undervalued) | -46.1pp (-4.5pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
# Pipeline Delta Report

- **This run:** 2026-07-01T21:16:11+00:00
- **Previous run:** 2026-07-01T19:50:47+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## Input files changed since last run

- `inputs/fleet_manifests/eco.yaml` (modified)
- `inputs/market_data/newbuild_specs.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $16.40 (no change) | $14.95 (no change) | $15.77 (no change) | $13.88 (no change) | HOLD (fairly valued) | +6.5pp (no change) |
| ECO | $50.12 (no change) | $37.18 (-0.4%) | $40.02 (-0.4%) | $34.35 (-0.6%) | TRIM/SHORT (overvalued) | +13.0pp (+0.4pp) |
| FRO | $34.50 (no change) | $26.54 (no change) | $28.82 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +12.1pp (no change) |
| INSW | $76.59 (no change) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +31.3pp (no change) |
| TNK | $70.80 (no change) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +19.3pp (no change) |
| NAT | $5.54 (no change) | $3.09 (no change) | $3.33 (no change) | $2.79 (no change) | TRIM/SHORT (overvalued) | +61.1pp (no change) |
| FLNG | $28.06 (no change) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | BUY (undervalued) | -26.4pp (no change) |
| CCEC | $21.35 (no change) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -19.2pp (no change) |
| STNG | $75.60 (no change) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +32.0pp (no change) |
| HAFN | $6.64 (no change) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +23.3pp (no change) |
| TRMD | $26.06 (no change) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +20.1pp (no change) |
| ASC | $16.00 (no change) | $16.75 (no change) | $16.83 (no change) | $17.80 (no change) | BUY (undervalued) | +19.4pp (no change) |
| TEN | $35.37 (no change) | $61.29 (no change) | $65.49 (no change) | $88.70 (no change) | BUY (undervalued) | +27.6pp (no change) |
| CMDB | $17.56 (no change) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -10.3pp (no change) |
| SBLK | $24.97 (no change) | $28.34 (no change) | $28.37 (no change) | $29.34 (no change) | BUY (undervalued) | +3.9pp (no change) |
| GNK | $24.78 (no change) | $23.99 (no change) | $24.05 (no change) | $24.69 (no change) | HOLD (fairly valued) | +13.3pp (no change) |
| CAPT | $12.58 (no change) | $16.03 (no change) | $17.16 (no change) | $15.49 (no change) | BUY (undervalued) | +24.7pp (no change) |
| MPCC | $2.55 (no change) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +13.6pp (no change) |
| GSL | $37.60 (no change) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.1pp (no change) |
| BRUT | $5.21 (no change) | $9.27 (no change) | $10.24 (no change) | $8.80 (no change) | BUY (undervalued) | -34.5pp (no change) |
| CMBT | $13.99 (no change) | $15.26 (no change) | $16.07 (no change) | $15.87 (no change) | BUY (undervalued) | +19.5pp (no change) |
| SB | $6.31 (no change) | $9.87 (no change) | $9.68 (no change) | $10.12 (no change) | BUY (undervalued) | -40.5pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
# Pipeline Delta Report

- **This run:** 2026-07-01T02:12:47+00:00
- **Previous run:** 2026-07-01T01:56:33+00:00

## Headline changes (material moves)

- **DHT:** position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- **TNK:** broker spread +6.9pp
- **FLNG:** position HOLD (fairly valued) → BUY (undervalued)
- **STNG:** broker spread +7.3pp

## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT ⚑ | $16.40 (-0.68) | $14.95 (no change) | $15.77 (no change) | $13.88 (no change) | HOLD (fairly valued) ⟵ | +6.5pp (-3.1pp) |
| ECO | $50.12 (+0.52) | $37.33 (no change) | $40.17 (no change) | $34.56 (no change) | TRIM/SHORT (overvalued) | +12.6pp (+0.7pp) |
| FRO | $34.50 (-0.94) | $26.54 (no change) | $28.82 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +12.1pp (-1.7pp) |
| INSW | $76.59 (-1.22) | $38.63 (no change) | $61.34 (no change) | $52.59 (no change) | TRIM/SHORT (overvalued) | +31.3pp (-1.0pp) |
| TNK ⚑ | $70.80 (+4.81) | $79.42 (no change) | $79.59 (no change) | $77.51 (no change) | BUY (undervalued) | +19.3pp (+6.9pp) |
| NAT | $5.54 (-0.24) | $3.09 (no change) | $3.33 (no change) | $2.79 (no change) | TRIM/SHORT (overvalued) | +61.1pp (-1.9pp) |
| FLNG ⚑ | $28.06 (-1.23) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | BUY (undervalued) ⟵ | -26.4pp (-4.0pp) |
| CCEC | $21.35 (+0.48) | $32.08 (no change) | $35.91 (no change) | $28.10 (no change) | BUY (undervalued) | -19.2pp (+2.9pp) |
| STNG ⚑ | $75.60 (+5.51) | $78.93 (no change) | $79.99 (no change) | $80.35 (no change) | BUY (undervalued) | +32.0pp (+7.3pp) |
| HAFN | $6.64 (-0.22) | $5.66 (no change) | $5.91 (no change) | $5.22 (no change) | TRIM/SHORT (overvalued) | +23.3pp (-2.2pp) |
| TRMD | $26.06 (-0.25) | $26.35 (no change) | $27.32 (no change) | $25.43 (no change) | HOLD (fairly valued) | +20.1pp (-0.8pp) |
| ASC | $16.00 (no change) | $15.09 (no change) | $15.15 (no change) | $15.93 (no change) | TRIM/SHORT (overvalued) | +29.6pp (no change) |
| TEN | $35.37 (-0.39) | $61.29 (no change) | $65.49 (no change) | $88.70 (no change) | BUY (undervalued) | +27.6pp (-1.7pp) |
| CMDB | $17.56 (-0.43) | $20.43 (no change) | $20.43 (no change) | $31.33 (no change) | BUY (undervalued) | -10.3pp (-2.5pp) |
| SBLK | $24.97 (+0.33) | $28.34 (no change) | $28.37 (no change) | $29.34 (no change) | BUY (undervalued) | +3.9pp (+1.4pp) |
| GNK | $24.78 (+0.39) | $23.99 (no change) | $24.05 (no change) | $24.69 (no change) | HOLD (fairly valued) | +13.3pp (+1.4pp) |
| CAPT | $12.58 (-0.15) | $16.03 (no change) | $17.16 (no change) | $15.49 (no change) | BUY (undervalued) | +24.7pp (-1.3pp) |
| MPCC | $2.55 (-0.07) | $2.19 (no change) | $2.11 (no change) | $2.02 (no change) | TRIM/SHORT (overvalued) | +13.6pp (-1.7pp) |
| GSL | $37.60 (-0.14) | $43.00 (no change) | $40.59 (no change) | $38.59 (no change) | BUY (undervalued) | +24.1pp (-0.3pp) |
| BRUT | $5.21 (no change) | $9.84 (no change) | $10.81 (no change) | $9.40 (no change) | BUY (undervalued) | -45.8pp (no change) |
| CMBT | $13.99 (-0.09) | $15.26 (no change) | $16.07 (no change) | $15.87 (no change) | BUY (undervalued) | +19.5pp (-0.6pp) |
| SB | $6.31 (-0.05) | $10.17 (no change) | $9.97 (no change) | $10.47 (no change) | BUY (undervalued) | -45.3pp (-1.1pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 3 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
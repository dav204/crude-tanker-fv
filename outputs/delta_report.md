# Pipeline Delta Report

- **This run:** 2026-07-15T14:33:38+00:00
- **Previous run:** 2026-07-14T21:24:16+00:00

## Headline changes (material moves)

- **STNG:** position TRIM/SHORT (overvalued) → HOLD (fairly valued)
- **HAFN:** scenario PW FV +11.1%
- **TRMD:** position HOLD (fairly valued) → BUY (undervalued); scenario PW FV +11.3%

## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)
- `inputs/reweight_triggers.yaml` (modified)
- `inputs/scenario_inputs.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $18.18 (+0.87) | $14.95 (no change) | $13.34 (no change) | $13.88 (no change) | TRIM/SHORT (overvalued) | +9.1pp (+3.1pp) |
| ECO | $56.73 (+2.53) | $37.18 (no change) | $32.09 (no change) | $34.35 (no change) | TRIM/SHORT (overvalued) | +10.9pp (+2.3pp) |
| FRO | $38.38 (+1.46) | $26.54 (no change) | $22.91 (no change) | $24.22 (no change) | TRIM/SHORT (overvalued) | +7.9pp (+2.0pp) |
| INSW | $88.12 (+1.95) | $38.63 (no change) | $54.21 (+2.4%) | $52.59 (no change) | TRIM/SHORT (overvalued) | +25.8pp (+1.6pp) |
| TNK | $72.27 (+1.55) | $79.42 (no change) | $73.18 (no change) | $77.51 (no change) | HOLD (fairly valued) | +23.2pp (+1.8pp) |
| NAT | $6.29 (+0.20) | $3.09 (no change) | $2.72 (no change) | $2.79 (no change) | TRIM/SHORT (overvalued) | +58.4pp (+1.1pp) |
| FLNG | $30.81 (+0.67) | $28.16 (no change) | $30.67 (+5.1%) | $28.45 (no change) | HOLD (fairly valued) | -17.0pp (+1.2pp) |
| CCEC | $22.68 (+0.30) | $32.08 (no change) | $35.91 (+7.2%) | $28.10 (no change) | BUY (undervalued) | -12.0pp (+1.1pp) |
| STNG ⚑ | $77.87 (+0.59) | $76.13 (no change) | $77.13 (+8.8%) | $77.47 (no change) | HOLD (fairly valued) ⟵ | +39.8pp (+3.5pp) |
| HAFN ⚑ | $7.48 (+0.16) | $5.99 (no change) | $6.23 (+11.1%) | $5.57 (no change) | TRIM/SHORT (overvalued) | +36.5pp (+3.8pp) |
| TRMD ⚑ | $29.43 (+0.57) | $30.97 (no change) | $31.90 (+11.3%) | $30.34 (no change) | BUY (undervalued) ⟵ | +16.5pp (+2.8pp) |
| ASC | $16.18 (+0.35) | $16.75 (no change) | $16.83 (+3.4%) | $17.80 (no change) | HOLD (fairly valued) | +20.5pp (+2.8pp) |
| TEN | $39.75 (+0.92) | $61.29 (no change) | $57.60 (+2.2%) | $88.70 (no change) | BUY (undervalued) | +41.1pp (+3.6pp) |
| CMDB | $19.94 (+0.38) | $20.52 (no change) | $20.10 (no change) | $31.33 (no change) | HOLD (fairly valued) | +2.5pp (+1.8pp) |
| SBLK | $26.56 (+0.02) | $28.50 (no change) | $27.69 (no change) | $29.34 (no change) | HOLD (fairly valued) | +15.0pp (no change) |
| GNK | $25.45 (+0.10) | $23.98 (no change) | $23.15 (no change) | $24.69 (no change) | TRIM/SHORT (overvalued) | +12.9pp (+0.3pp) |
| CAPT | $13.40 (+0.12) | $16.03 (no change) | $13.14 (no change) | $15.49 (no change) | HOLD (fairly valued) | +24.2pp (+0.9pp) |
| MPCC | $2.54 (+0.03) | $2.21 (no change) | $2.06 (no change) | $2.04 (no change) | TRIM/SHORT (overvalued) | +12.4pp (+0.7pp) |
| GSL | $41.24 (+0.43) | $43.06 (no change) | $40.54 (no change) | $38.59 (no change) | HOLD (fairly valued) | +31.1pp (+0.8pp) |
| BRUT | $5.57 (+0.03) | $9.27 (no change) | $6.20 (no change) | $8.80 (no change) | BUY (undervalued) | -16.1pp (+0.8pp) |
| CMBT | $15.78 (+0.34) | $15.25 (no change) | $13.87 (no change) | $15.87 (no change) | TRIM/SHORT (overvalued) | +30.2pp (+1.8pp) |
| SB | $7.13 (+0.17) | $9.78 (no change) | $9.56 (no change) | $10.12 (no change) | BUY (undervalued) | -24.3pp (+3.0pp) |
| LPG | $41.63 (+1.49) | $32.76 (no change) | $30.55 (no change) | $34.11 (no change) | TRIM/SHORT (overvalued) | +30.9pp (+2.6pp) |
| BWLP | $21.16 (+1.06) | $15.43 (no change) | $14.46 (no change) | $15.80 (no change) | TRIM/SHORT (overvalued) | +23.6pp (+3.3pp) |
| 2343 | $0.39 (no change) | $0.38 (no change) | $0.38 (no change) | $0.39 (no change) | HOLD (fairly valued) | +3.0pp (+0.2pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
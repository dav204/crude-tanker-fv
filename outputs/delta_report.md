# Pipeline Delta Report

- **This run:** 2026-08-16T20:06:34+00:00
- **Previous run:** 2026-08-16T15:23:15+00:00

## Headline changes (material moves)

- **BRUT:** broker spread +7.8pp

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: GNK (+1.71%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $18.23 | $19.76 | hist · fair\|rich | -7.76% | +6.68% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $26.34 | $25.90 | parity · cheap\|fair | **+1.71%** | -3.08% (@ $25.10) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $29.05 | $27.72 | hist · cheap\|fair | +4.81% | +3.18% (@ $28.60) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- `inputs/market_data/prices_daily.yaml` (modified)

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $19.52 (+0.32) | $15.32 (no change) | $15.97 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +14.1pp (+1.1pp) |
| ECO | $60.29 (-3.63) | $39.73 (no change) | $41.71 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +8.1pp (-3.4pp) |
| FRO | $41.21 (+0.69) | $25.94 (no change) | $27.79 (no change) | $25.34 (no change) | TRIM/SHORT (overvalued) | +13.4pp (+0.9pp) |
| INSW | $97.05 (+1.90) | $37.59 (no change) | $59.59 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +26.5pp (+1.1pp) |
| TNK | $85.13 (+1.59) | $83.23 (no change) | $83.93 (no change) | $84.60 (no change) | HOLD (fairly valued) | +22.4pp (+1.6pp) |
| NAT | $6.71 (+0.10) | $2.97 (no change) | $3.07 (no change) | $2.85 (no change) | TRIM/SHORT (overvalued) | +65.8pp (+0.6pp) |
| FLNG | $30.80 (+0.49) | $28.16 (no change) | $30.67 (no change) | $28.45 (no change) | HOLD (fairly valued) | -20.8pp (+1.4pp) |
| CCEC | $22.61 (+0.13) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -2.4pp (+0.6pp) |
| STNG | $79.41 (+0.87) | $72.23 (no change) | $76.73 (no change) | $76.22 (no change) | HOLD (fairly valued) | +41.7pp (+1.0pp) |
| HAFN | $7.74 (+0.13) | $5.71 (no change) | $6.56 (no change) | $5.56 (no change) | TRIM/SHORT (overvalued) | +34.0pp (+1.1pp) |
| TRMD | $30.08 (+0.71) | $29.98 (no change) | $33.58 (no change) | $30.22 (no change) | BUY (undervalued) | +14.6pp (+2.2pp) |
| ASC | $17.61 (+0.30) | $17.22 (no change) | $16.38 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +29.7pp (+1.5pp) |
| TEN | $41.45 (+0.64) | $59.21 (no change) | $62.66 (no change) | $88.16 (no change) | BUY (undervalued) | +51.1pp (+2.1pp) |
| CMDB | $18.23 (+0.15) | $21.13 (no change) | $20.11 (no change) | $32.13 (no change) | BUY (undervalued) | -8.6pp (+0.9pp) |
| SBLK | $29.05 (+0.31) | $31.88 (no change) | $29.79 (no change) | $32.78 (no change) | HOLD (fairly valued) | -0.4pp (+1.0pp) |
| GNK | $26.34 (+0.35) | $24.61 (no change) | $22.67 (no change) | $25.12 (no change) | TRIM/SHORT (overvalued) | +10.9pp (+1.1pp) |
| CAPT | $14.68 (+0.16) | $15.10 (no change) | $16.02 (no change) | $15.48 (no change) | BUY (undervalued) | +32.8pp (+1.1pp) |
| MPCC | $2.72 (+0.08) | $2.22 (no change) | $2.07 (no change) | $2.05 (no change) | TRIM/SHORT (overvalued) | +16.3pp (+1.6pp) |
| GSL | $42.17 (+0.69) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | HOLD (fairly valued) | +27.8pp (+1.3pp) |
| BRUT ⚑ | $6.74 (+0.36) | $9.63 (no change) | $10.28 (no change) | $9.62 (no change) | BUY (undervalued) | -25.2pp (+7.8pp) |
| CMBT | $17.24 (+0.28) | $15.65 (no change) | $14.41 (no change) | $16.46 (no change) | TRIM/SHORT (overvalued) | +18.4pp (+1.3pp) |
| SB | $7.75 (+0.08) | $10.24 (no change) | $9.53 (no change) | $10.58 (no change) | BUY (undervalued) | -19.2pp (+1.2pp) |
| LPG | $47.37 (+1.74) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +24.0pp (+2.4pp) |
| BWLP | $22.75 (+0.34) | $15.43 (no change) | $14.46 (no change) | $15.80 (no change) | TRIM/SHORT (overvalued) | +15.8pp (+0.9pp) |
| 2343 | $0.50 (+0.01) | $0.40 (no change) | $0.40 (no change) | $0.41 (no change) | TRIM/SHORT (overvalued) | +24.1pp (+0.2pp) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
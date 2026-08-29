# Pipeline Delta Report

- **This run:** 2026-08-29T20:49:33+00:00
- **Previous run:** 2026-08-29T20:44:37+00:00

## Headline changes (material moves)

- **No material changes.** All tickers within thresholds (|ΔFV%|≤10%, |Δspread|≤5pp, |ΔNAV%|≤5%) and no position flips.

## §17 read-flip strobe — tape vs the flip boundary

> ⚡ **STROBE ZONE — 1 name(s) inside the ±2.0% deadband at the tape: GNK (-0.07%).** The governed `read_flag` holds its state on the watchlist vintage, but at today's close the read sits close enough to its settling boundary that the next vintage rebase could restate it — and `read_flag` caps position size. This is the hazard the deadband exists for: surfaced, not acted on.

| Ticker | read_flag | Tape | Flip boundary | Edge | Tape margin | Row margin (vintage) | |
|---|---|---|---|---|---|---|---|
| CMDB | flips (cheap/fair) | $20.52 | $19.95 | parity · cheap\|fair | +2.87% | +6.68% (@ $17.25) | clear of the deadband |
| GNK | flips (cheap/fair) | $25.88 | $25.90 | parity · cheap\|fair | **-0.07%** | -3.08% (@ $25.10) | ⚡ inside ±2.0% deadband |
| SBLK | flips (cheap/fair) | $30.48 | $33.26 | parity · cheap\|fair | -8.36% | +3.18% (@ $28.60) | clear of the deadband |

_MONITOR layer, forward-looking. `Tape margin` is the signed distance from the price this run values at to the nearest band edge whose crossing would settle the flip — i.e. where the read would sit once the watchlist rebases to today's tape. It is NOT a scorecard number and never governs: `read_flag` and the deadband are measured on the watchlist vintage (`Row margin`), the same price the read itself is computed on (Addendum B2, 2026-08-14). The two differ by exactly the drift between the two vintages._
## Input files changed since last run

- _(no input file changes detected — hashes match)_

## Full per-ticker deltas

| Ticker | Price | Single-point FV | Scenario PW FV | NAV/sh | Position | Broker spread |
|---|---|---|---|---|---|---|
| DHT | $19.66 (no change) | $15.32 (no change) | $15.97 (no change) | $15.01 (no change) | TRIM/SHORT (overvalued) | +14.6pp (no change) |
| ECO | $66.86 (no change) | $39.73 (no change) | $41.71 (no change) | $39.54 (no change) | TRIM/SHORT (overvalued) | +13.9pp (no change) |
| FRO | $44.19 (no change) | $25.94 (no change) | $27.79 (no change) | $25.34 (no change) | TRIM/SHORT (overvalued) | +17.2pp (no change) |
| INSW | $98.81 (no change) | $37.59 (no change) | $59.59 (no change) | $54.64 (no change) | TRIM/SHORT (overvalued) | +27.4pp (no change) |
| TNK | $88.70 (no change) | $83.23 (no change) | $83.93 (no change) | $84.60 (no change) | TRIM/SHORT (overvalued) | +25.9pp (no change) |
| NAT | $6.77 (no change) | $2.97 (no change) | $3.07 (no change) | $2.85 (no change) | TRIM/SHORT (overvalued) | +66.1pp (no change) |
| FLNG | $31.48 (no change) | $27.01 (no change) | $29.47 (no change) | $27.22 (no change) | TRIM/SHORT (overvalued) | -15.3pp (no change) |
| CCEC | $22.72 (no change) | $29.97 (no change) | $33.70 (no change) | $25.70 (no change) | BUY (undervalued) | -1.9pp (no change) |
| STNG | $78.03 (no change) | $72.23 (no change) | $76.73 (no change) | $76.22 (no change) | HOLD (fairly valued) | +40.1pp (no change) |
| HAFN | $8.47 (no change) | $5.71 (no change) | $6.56 (no change) | $5.56 (no change) | TRIM/SHORT (overvalued) | +39.8pp (no change) |
| TRMD | $32.62 (no change) | $32.14 (no change) | $35.79 (no change) | $32.30 (no change) | BUY (undervalued) | +16.0pp (no change) |
| ASC | $17.36 (no change) | $17.22 (no change) | $16.38 (no change) | $17.37 (no change) | TRIM/SHORT (overvalued) | +28.4pp (no change) |
| TEN | $42.52 (no change) | $59.21 (no change) | $62.66 (no change) | $88.16 (no change) | BUY (undervalued) | +54.5pp (no change) |
| CMDB | $20.52 (no change) | $21.13 (no change) | $20.11 (no change) | $32.13 (no change) | HOLD (fairly valued) | +2.7pp (no change) |
| SBLK | $30.48 (no change) | $31.88 (no change) | $29.79 (no change) | $32.78 (no change) | HOLD (fairly valued) | +4.0pp (no change) |
| GNK | $25.88 (no change) | $24.61 (no change) | $22.67 (no change) | $25.12 (no change) | TRIM/SHORT (overvalued) | +9.5pp (no change) |
| CAPT | $16.46 (no change) | $15.10 (no change) | $16.02 (no change) | $15.48 (no change) | HOLD (fairly valued) | +43.4pp (no change) |
| MPCC | $2.85 (no change) | $2.22 (no change) | $2.07 (no change) | $2.05 (no change) | TRIM/SHORT (overvalued) | +19.2pp (no change) |
| GSL | $44.52 (no change) | $44.02 (no change) | $42.88 (no change) | $41.20 (no change) | HOLD (fairly valued) | +31.8pp (no change) |
| BRUT | $4.94 (no change) | $9.63 (no change) | $10.28 (no change) | $9.62 (no change) | BUY (undervalued) | -74.7pp (no change) |
| CMBT | $18.35 (no change) | $15.65 (no change) | $14.41 (no change) | $16.46 (no change) | TRIM/SHORT (overvalued) | +23.2pp (no change) |
| SB | $6.39 (no change) | $10.24 (no change) | $9.53 (no change) | $10.58 (no change) | BUY (undervalued) | -43.5pp (no change) |
| LPG | $49.78 (no change) | $33.93 (no change) | $31.82 (no change) | $35.69 (no change) | TRIM/SHORT (overvalued) | +27.0pp (no change) |
| BWLP | $24.05 (no change) | $15.43 (no change) | $14.46 (no change) | $15.80 (no change) | TRIM/SHORT (overvalued) | +18.9pp (no change) |
| 2343 | $0.39 (no change) | $0.40 (no change) | $0.40 (no change) | $0.41 (no change) | HOLD (fairly valued) | +4.8pp (no change) |

_⚑ flags a material change (position flip, |ΔFV%| > 10%, |Δspread| > 5pp, or |ΔNAV%| > 5%). ⟵ marks a position flip._

_⚠ MIXED-ANCHOR-BASIS: this table spans 4 incompatible cycle-anchor bases — cycle-position ratios are NOT comparable across them (METHODOLOGY §10): `archive_22mo_median` (22-month archive median: dry_bulk); `fy_calendar_avg` (FY2021-2025 calendar average: containerships); `realized_tce_10yr_mean` (realized-TCE 10-year through-cycle mean: lpg); `tc_10yr_mean` (TC-anchored 10-year mean: crude, lng, product)._
# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| SB | ✓ robust | position BUY across all 3 weight sets |
| 2343 | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Weight sets compared

| Scenario | Set A | Set B | Set C |
|---|--:|--:|--:|
| china_acceleration | 0.20 | 0.30 | 0.12 |
| moderate_growth | 0.40 | 0.40 | 0.33 |
| china_property_drag | 0.25 | 0.18 | 0.35 |
| coordinated_slowdown | 0.15 | 0.12 | 0.20 |

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Robustness | Notes |
|---|--:|--:|--:|---|---|
| SBLK | -6.7% (TRIM/SHORT) | -3.5% (HOLD) | -10.3% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| GNK | -20.4% (TRIM/SHORT) | -17.2% (TRIM/SHORT) | -23.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -18.8% (TRIM/SHORT) | -16.5% (TRIM/SHORT) | -21.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| SB | +11.5% (BUY) | +15.9% (BUY) | +6.8% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -28.9% (TRIM/SHORT) | -27.4% (TRIM/SHORT) | -30.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $30.79, target $34.50

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.71 | -6.7% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.71 | -3.5% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.62 | -10.3% | TRIM/SHORT |

### GNK — price $27.00, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $21.50 | -20.4% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $22.35 | -17.2% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $20.56 | -23.9% | TRIM/SHORT |

### CMDB — price $24.10, target $27.98

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $19.56 | -18.8% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.11 | -16.5% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $18.95 | -21.4% | TRIM/SHORT |

### SB — price $8.27, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.22 | +11.5% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.58 | +15.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $8.83 | +6.8% | BUY |

### 2343 — price $0.53, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -28.9% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.38 | -27.4% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.37 | -30.5% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

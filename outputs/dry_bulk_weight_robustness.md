# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
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
| SBLK | -2.3% (HOLD) | +1.2% (HOLD) | -6.1% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| GNK | -12.4% (TRIM/SHORT) | -8.8% (TRIM/SHORT) | -16.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | -2.0% (HOLD) | +0.9% (HOLD) | -5.2% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| SB | +11.9% (BUY) | +16.4% (BUY) | +7.1% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -25.8% (TRIM/SHORT) | -24.1% (TRIM/SHORT) | -27.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $30.48, target $34.50

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $29.79 | -2.3% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $30.86 | +1.2% | HOLD |
| Bulk Set C (China-property-drag bracket) | $28.61 | -6.1% | TRIM/SHORT |

### GNK — price $25.88, target $27.20

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $22.67 | -12.4% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $23.60 | -8.8% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $21.63 | -16.4% | TRIM/SHORT |

### CMDB — price $20.52, target $27.98

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.11 | -2.0% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +0.9% | HOLD |
| Bulk Set C (China-property-drag bracket) | $19.45 | -5.2% | TRIM/SHORT |

### SB — price $8.52, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.53 | +11.9% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.92 | +16.4% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +7.1% | BUY |

### 2343 — price $0.53, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.40 | -25.8% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.40 | -24.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.39 | -27.6% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

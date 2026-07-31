# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position HOLD across all 3 weight sets |
| GNK | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
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
| SBLK | -0.5% (HOLD) | +3.3% (HOLD) | -4.6% (HOLD) | ✓ robust | position HOLD across all 3 weight sets |
| GNK | -6.5% (TRIM/SHORT) | -2.8% (HOLD) | -10.7% (TRIM/SHORT) | ⚑ driven | TRIM/SHORT under Set A/Set C; HOLD under Set B |
| CMDB | +7.7% (BUY) | +10.9% (BUY) | +4.1% (HOLD) | ⚑ driven | BUY under Set A/Set B; HOLD under Set C |
| SB | +21.3% (BUY) | +26.6% (BUY) | +15.6% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -7.2% (TRIM/SHORT) | -5.1% (TRIM/SHORT) | -9.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $28.77, target $34.50

**Classification:** WEIGHT-ROBUST. position HOLD across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.62 | -0.5% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.71 | +3.3% | HOLD |
| Bulk Set C (China-property-drag bracket) | $27.44 | -4.6% | HOLD |

### GNK — price $25.76, target $24.80

**Classification:** WEIGHT-DRIVEN. TRIM/SHORT under Set A/Set C; HOLD under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $24.08 | -6.5% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $25.04 | -2.8% | HOLD |
| Bulk Set C (China-property-drag bracket) | $23.00 | -10.7% | TRIM/SHORT |

### CMDB — price $19.30, target $27.98

**Classification:** WEIGHT-DRIVEN. BUY under Set A/Set B; HOLD under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.79 | +7.7% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $21.40 | +10.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $20.11 | +4.1% | HOLD |

### SB — price $7.81, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.47 | +21.3% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.88 | +26.6% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.03 | +15.6% | BUY |

### 2343 — price $0.42, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.39 | -7.2% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.40 | -5.1% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.38 | -9.5% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| GNK | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | ✓ robust | position HOLD across all 3 weight sets |
| SB | ✓ robust | position BUY across all 3 weight sets |
| 2343 | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

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
| SBLK | +4.3% (HOLD) | +8.3% (BUY) | -0.1% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| GNK | -9.0% (TRIM/SHORT) | -5.3% (TRIM/SHORT) | -13.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | +0.8% (HOLD) | +3.8% (HOLD) | -2.5% (HOLD) | ✓ robust | position HOLD across all 3 weight sets |
| SB | +34.1% (BUY) | +40.0% (BUY) | +27.9% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -3.3% (HOLD) | -1.1% (HOLD) | -5.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

## Per-name detail

### SBLK — price $26.56, target $34.50

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $27.69 | +4.3% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $28.75 | +8.3% | BUY |
| Bulk Set C (China-property-drag bracket) | $26.53 | -0.1% | HOLD |

### GNK — price $25.45, target $24.80

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.15 | -9.0% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.09 | -5.3% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $22.11 | -13.1% | TRIM/SHORT |

### CMDB — price $19.94, target $27.98

**Classification:** WEIGHT-ROBUST. position HOLD across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.10 | +0.8% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +3.8% | HOLD |
| Bulk Set C (China-property-drag bracket) | $19.44 | -2.5% | HOLD |

### SB — price $7.13, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.56 | +34.1% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.98 | +40.0% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +27.9% | BUY |

### 2343 — price $0.39, target $0.44

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -3.3% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -1.1% | HOLD |
| Bulk Set C (China-property-drag bracket) | $0.37 | -5.7% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

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
| CMDB | ✓ robust | position BUY across all 3 weight sets |
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
| SBLK | +2.5% (HOLD) | +6.2% (BUY) | -1.5% (HOLD) | ⚑ driven | HOLD under Set A/Set C; BUY under Set B |
| GNK | -13.9% (TRIM/SHORT) | -10.4% (TRIM/SHORT) | -17.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |
| CMDB | +10.3% (BUY) | +13.5% (BUY) | +6.7% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +23.0% (BUY) | +28.0% (BUY) | +17.7% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -20.2% (TRIM/SHORT) | -18.4% (TRIM/SHORT) | -22.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 3 weight sets |

## Per-name detail

### SBLK — price $29.05, target $34.50

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set C; BUY under Set B.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $29.79 | +2.5% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $30.86 | +6.2% | BUY |
| Bulk Set C (China-property-drag bracket) | $28.61 | -1.5% | HOLD |

### GNK — price $26.34, target $28.40

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $22.67 | -13.9% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $23.60 | -10.4% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $21.63 | -17.9% | TRIM/SHORT |

### CMDB — price $18.23, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.11 | +10.3% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $20.70 | +13.5% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.45 | +6.7% | BUY |

### SB — price $7.75, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.53 | +23.0% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $9.92 | +28.0% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.12 | +17.7% | BUY |

### 2343 — price $0.50, target $0.44

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.40 | -20.2% | TRIM/SHORT |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.40 | -18.4% | TRIM/SHORT |
| Bulk Set C (China-property-drag bracket) | $0.39 | -22.1% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

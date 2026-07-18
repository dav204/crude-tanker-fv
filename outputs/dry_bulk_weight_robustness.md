# Dry-Bulk Weight-Robustness Diagnostic (§9.10 — WO4)

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Bulk Set A weights. Surfaces which dry-bulk calls survive a defensible reweighting (**weight-robust**) vs which depend on a specific prior (**weight-driven**). Unblocks the consumer's Gate E (`weight_sign_stable`).

**Axis:** China dry-bulk demand tension — the four scenarios' own parameter (china_acceleration ↔ china_property_drag / coordinated_slowdown) and the charter thesis's load-bearing variable (Simandou ton-mile + supply discipline vs China property/steel drag). Bulk Set B brackets the China-bull / super-cycle case; Bulk Set C the property-drag case; both are ±~10pp shifts.

**Naming namespace:** labels are DRY-BULK families ("Bulk Set …"); crude and LNG both use "Set B" for their own — a bare unprefixed label would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| SBLK | ✓ robust | position BUY across all 3 weight sets |
| GNK | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | ✓ robust | position BUY across all 3 weight sets |
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
| SBLK | +13.8% (BUY) | +18.2% (BUY) | +9.1% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| GNK | -1.2% (HOLD) | +2.7% (HOLD) | -5.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |
| CMDB | +9.2% (BUY) | +12.5% (BUY) | +5.7% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| SB | +40.8% (BUY) | +46.9% (BUY) | +34.2% (BUY) | ✓ robust | position BUY across all 3 weight sets |
| 2343 | -2.8% (HOLD) | -0.6% (HOLD) | -5.2% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B; TRIM/SHORT under Set C |

## Per-name detail

### SBLK — price $24.90, target $34.50

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $28.35 | +13.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $29.43 | +18.2% | BUY |
| Bulk Set C (China-property-drag bracket) | $27.16 | +9.1% | BUY |

### GNK — price $24.12, target $24.80

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $23.82 | -1.2% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $24.78 | +2.7% | HOLD |
| Bulk Set C (China-property-drag bracket) | $22.75 | -5.7% | TRIM/SHORT |

### CMDB — price $18.81, target $27.98

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $20.55 | +9.2% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $21.16 | +12.5% | BUY |
| Bulk Set C (China-property-drag bracket) | $19.87 | +5.7% | BUY |

### SB — price $6.82, target $7.10

**Classification:** WEIGHT-ROBUST. position BUY across all 3 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $9.60 | +40.8% | BUY |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $10.02 | +46.9% | BUY |
| Bulk Set C (China-property-drag bracket) | $9.15 | +34.2% | BUY |

### 2343 — price $0.40, target $0.44

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B; TRIM/SHORT under Set C.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Bulk Set A (locked 2026-06-09, FFA-calibrated prior) | $0.38 | -2.8% | HOLD |
| Bulk Set B (China-bull / Simandou super-cycle bracket) | $0.39 | -0.6% | HOLD |
| Bulk Set C (China-property-drag bracket) | $0.37 | -5.2% | TRIM/SHORT |

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness). This is the §9.10 output for the dry-bulk sector; crude/LNG analogues live in `outputs/weight_robustness_diagnostic.md` / `outputs/lng_weight_robustness.md`.

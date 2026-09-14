# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | ✓ robust | position BUY across all 8 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | ⚑ driven | BUY under Set A'''; HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Weight sets compared

| Scenario | Set A''' | Set A'' | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| escalation | 0.28 | 0.25 | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.59 | 0.62 | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.00 | 0.00 | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.13 | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A''' EV | Set A'' EV | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -25.8% (TRIM/SHORT) | -26.7% (TRIM/SHORT) | -27.1% (TRIM/SHORT) | -28.1% (TRIM/SHORT) | -36.1% (TRIM/SHORT) | -33.4% (TRIM/SHORT) | -39.8% (TRIM/SHORT) | -36.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -44.6% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | -45.9% (TRIM/SHORT) | -46.6% (TRIM/SHORT) | -54.2% (TRIM/SHORT) | -51.7% (TRIM/SHORT) | -57.6% (TRIM/SHORT) | -54.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -41.5% (TRIM/SHORT) | -42.5% (TRIM/SHORT) | -42.9% (TRIM/SHORT) | -43.8% (TRIM/SHORT) | -52.1% (TRIM/SHORT) | -49.3% (TRIM/SHORT) | -55.9% (TRIM/SHORT) | -52.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -42.2% (TRIM/SHORT) | -42.8% (TRIM/SHORT) | -43.0% (TRIM/SHORT) | -43.4% (TRIM/SHORT) | -47.7% (TRIM/SHORT) | -46.3% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | -48.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -17.4% (TRIM/SHORT) | -18.2% (TRIM/SHORT) | -18.4% (TRIM/SHORT) | -18.8% (TRIM/SHORT) | -24.1% (TRIM/SHORT) | -22.3% (TRIM/SHORT) | -26.4% (TRIM/SHORT) | -24.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -60.2% (TRIM/SHORT) | -61.0% (TRIM/SHORT) | -61.2% (TRIM/SHORT) | -61.7% (TRIM/SHORT) | -67.3% (TRIM/SHORT) | -65.5% (TRIM/SHORT) | -69.7% (TRIM/SHORT) | -67.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +29.0% (BUY) | +27.7% (BUY) | +27.4% (BUY) | +26.6% (BUY) | +17.2% (BUY) | +20.3% (BUY) | +13.2% (BUY) | +16.6% (BUY) | ✓ robust | position BUY across all 8 weight sets |
| CMBT | -31.7% (TRIM/SHORT) | -32.2% (TRIM/SHORT) | -32.4% (TRIM/SHORT) | -32.7% (TRIM/SHORT) | -36.5% (TRIM/SHORT) | -35.2% (TRIM/SHORT) | -38.2% (TRIM/SHORT) | -36.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +7.0% (BUY) | +4.5% (HOLD) | +3.3% (HOLD) | +0.4% (HOLD) | -21.9% (TRIM/SHORT) | -14.5% (TRIM/SHORT) | -32.6% (TRIM/SHORT) | -23.9% (TRIM/SHORT) | ⚑ driven | BUY under Set A'''; HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -5.9% (TRIM/SHORT) | -7.6% (TRIM/SHORT) | -8.4% (TRIM/SHORT) | -10.2% (TRIM/SHORT) | -24.9% (TRIM/SHORT) | -20.0% (TRIM/SHORT) | -31.9% (TRIM/SHORT) | -26.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Per-name detail

### DHT — price $22.00, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.32 | -25.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.12 | -26.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.03 | -27.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.82 | -28.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.07 | -36.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.65 | -33.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.24 | -39.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.91 | -36.8% | TRIM/SHORT |

### ECO — price $76.15, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $42.22 | -44.6% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $41.50 | -45.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.23 | -45.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.63 | -46.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $34.88 | -54.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $36.79 | -51.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.27 | -57.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.45 | -54.8% | TRIM/SHORT |

### FRO — price $49.21, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $28.79 | -41.5% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.30 | -42.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.10 | -42.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.64 | -43.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.59 | -52.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.93 | -49.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.70 | -55.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.25 | -52.8% | TRIM/SHORT |

### INSW — price $103.65, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $59.91 | -42.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $59.32 | -42.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.13 | -43.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.70 | -43.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.21 | -47.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.70 | -46.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.23 | -49.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $53.90 | -48.0% | TRIM/SHORT |

### TNK — price $100.83, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $83.24 | -17.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $82.48 | -18.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $82.29 | -18.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $81.86 | -18.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $76.51 | -24.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $78.30 | -22.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $74.21 | -26.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $76.19 | -24.4% | TRIM/SHORT |

### NAT — price $7.46, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $2.97 | -60.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $2.91 | -61.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.89 | -61.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.85 | -61.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.44 | -67.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.57 | -65.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.26 | -69.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.41 | -67.7% | TRIM/SHORT |

### TEN — price $47.90, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.80 | +29.0% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.17 | +27.7% | BUY |
| Crude Set A' (B' reweight, history bracket) | $61.00 | +27.4% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.62 | +26.6% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $56.13 | +17.2% | BUY |
| Crude Set C (bullish, extended Phase 1) | $57.61 | +20.3% | BUY |
| Crude Set D (bearish, deep normalization) | $54.21 | +13.2% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $55.87 | +16.6% | BUY |

### CMBT — price $19.48, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $13.30 | -31.7% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $13.21 | -32.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $13.18 | -32.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $13.10 | -32.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.38 | -36.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $12.62 | -35.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.05 | -38.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.32 | -36.7% | TRIM/SHORT |

### BRUT — price $5.00, target $4.56

**Classification:** WEIGHT-DRIVEN. BUY under Set A'''; HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.35 | +7.0% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.23 | +4.5% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.17 | +3.3% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.02 | +0.4% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.91 | -21.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.28 | -14.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.37 | -32.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.81 | -23.9% | TRIM/SHORT |

### CAPT — price $18.89, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $17.77 | -5.9% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $17.46 | -7.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $17.31 | -8.4% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.97 | -10.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.19 | -24.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.12 | -20.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.87 | -31.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.94 | -26.2% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (weight robustness, this run)

Mark-spread robustness is the OTHER dimension — cross-read with `outputs/broker_nav_sweep.md` before acting on any call.

| Ticker | Weight robustness | What drives the call |
|---|---|---|
| DHT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| NAT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | ✓ robust | position BUY across all 7 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | ⚑ driven | BUY under Set A''/Set A'/Set A/Set C; HOLD under Set B/Set E; TRIM/SHORT under Set D |
| CAPT | ⚑ driven | BUY under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Weight sets compared

| Scenario | Set A'' | Set A' | Set A | Set B | Set C | Set D | Set E |
|---|--:|--:|--:|--:|--:|--:|--:|
| escalation | 0.25 | 0.25 | 0.25 | 0.10 | 0.15 | 0.05 | 0.10 |
| pre_mou_baseline | 0.62 | 0.57 | 0.45 | 0.25 | 0.30 | 0.10 | 0.20 |
| mou_base | 0.00 | 0.05 | 0.18 | 0.45 | 0.40 | 0.55 | 0.45 |
| mou_bear | 0.13 | 0.13 | 0.12 | 0.20 | 0.15 | 0.30 | 0.25 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A'' EV | Set A' EV | Set A EV | Set B EV | Set C EV | Set D EV | Set E EV | Robustness | Notes |
|---|--:|--:|--:|--:|--:|--:|--:|---|---|
| DHT | -18.2% (TRIM/SHORT) | -18.7% (TRIM/SHORT) | -19.7% (TRIM/SHORT) | -28.8% (TRIM/SHORT) | -25.8% (TRIM/SHORT) | -33.0% (TRIM/SHORT) | -29.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -30.8% (TRIM/SHORT) | -31.3% (TRIM/SHORT) | -32.3% (TRIM/SHORT) | -41.8% (TRIM/SHORT) | -38.6% (TRIM/SHORT) | -46.1% (TRIM/SHORT) | -42.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -32.6% (TRIM/SHORT) | -33.1% (TRIM/SHORT) | -34.2% (TRIM/SHORT) | -44.6% (TRIM/SHORT) | -41.2% (TRIM/SHORT) | -49.5% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -38.6% (TRIM/SHORT) | -38.8% (TRIM/SHORT) | -39.3% (TRIM/SHORT) | -43.9% (TRIM/SHORT) | -42.3% (TRIM/SHORT) | -45.9% (TRIM/SHORT) | -44.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -1.4% (HOLD) | -1.7% (HOLD) | -2.2% (HOLD) | -8.3% (TRIM/SHORT) | -6.3% (TRIM/SHORT) | -11.0% (TRIM/SHORT) | -8.7% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| NAT | -54.3% (TRIM/SHORT) | -54.5% (TRIM/SHORT) | -55.1% (TRIM/SHORT) | -61.4% (TRIM/SHORT) | -59.3% (TRIM/SHORT) | -64.1% (TRIM/SHORT) | -61.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +51.2% (BUY) | +50.7% (BUY) | +49.7% (BUY) | +39.3% (BUY) | +42.7% (BUY) | +34.6% (BUY) | +38.5% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -16.4% (TRIM/SHORT) | -16.6% (TRIM/SHORT) | -17.0% (TRIM/SHORT) | -21.2% (TRIM/SHORT) | -19.8% (TRIM/SHORT) | -23.1% (TRIM/SHORT) | -21.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +52.5% (BUY) | +50.2% (BUY) | +44.9% (BUY) | +4.9% (HOLD) | +18.1% (BUY) | -14.5% (TRIM/SHORT) | +1.1% (HOLD) | ⚑ driven | BUY under Set A''/Set A'/Set A/Set C; HOLD under Set B/Set E; TRIM/SHORT under Set D |
| CAPT | +9.1% (BUY) | +8.1% (BUY) | +6.0% (BUY) | -12.3% (TRIM/SHORT) | -6.3% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | -13.9% (TRIM/SHORT) | ⚑ driven | BUY under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $19.52, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $15.97 | -18.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -18.7% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -19.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -28.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -25.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -33.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -29.5% | TRIM/SHORT |

### ECO — price $60.29, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.71 | -30.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.44 | -31.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -32.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -41.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -38.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -46.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -42.5% | TRIM/SHORT |

### FRO — price $41.21, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $27.79 | -32.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $27.57 | -33.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.10 | -34.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $22.81 | -44.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.24 | -41.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $20.82 | -49.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $22.46 | -45.5% | TRIM/SHORT |

### INSW — price $97.05, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.59 | -38.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.39 | -38.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -39.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -43.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -42.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -45.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -44.2% | TRIM/SHORT |

### TNK — price $85.13, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $83.93 | -1.4% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $83.72 | -1.7% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | -2.2% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -8.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -6.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $75.77 | -11.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -8.7% | TRIM/SHORT |

### NAT — price $6.71, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $3.07 | -54.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.05 | -54.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.01 | -55.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.59 | -61.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.73 | -59.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.41 | -64.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.57 | -61.8% | TRIM/SHORT |

### TEN — price $41.45, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $62.66 | +51.2% | BUY |
| Crude Set A' (B' reweight, history bracket) | $62.47 | +50.7% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +49.7% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +39.3% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +42.7% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +34.6% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +38.5% | BUY |

### CMBT — price $17.24, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $14.41 | -16.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $14.38 | -16.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.30 | -17.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.58 | -21.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.82 | -19.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.25 | -23.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.52 | -21.6% | TRIM/SHORT |

### BRUT — price $6.74, target $7.13

**Classification:** WEIGHT-DRIVEN. BUY under Set A''/Set A'/Set A/Set C; HOLD under Set B/Set E; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $10.28 | +52.5% | BUY |
| Crude Set A' (B' reweight, history bracket) | $10.13 | +50.2% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $9.77 | +44.9% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $7.07 | +4.9% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $7.97 | +18.1% | BUY |
| Crude Set D (bearish, deep normalization) | $5.77 | -14.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $6.82 | +1.1% | HOLD |

### CAPT — price $14.68, target $18.90

**Classification:** WEIGHT-DRIVEN. BUY under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $16.02 | +9.1% | BUY |
| Crude Set A' (B' reweight, history bracket) | $15.88 | +8.1% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.56 | +6.0% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $12.87 | -12.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.76 | -6.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $11.62 | -20.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.65 | -13.9% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

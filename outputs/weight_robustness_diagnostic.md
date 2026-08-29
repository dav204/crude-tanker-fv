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
| TNK | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | ✓ robust | position BUY across all 7 weight sets |
| CMBT | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | ⚑ driven | HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

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
| DHT | -18.8% (TRIM/SHORT) | -19.2% (TRIM/SHORT) | -20.3% (TRIM/SHORT) | -29.3% (TRIM/SHORT) | -26.3% (TRIM/SHORT) | -33.5% (TRIM/SHORT) | -30.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| ECO | -37.6% (TRIM/SHORT) | -38.0% (TRIM/SHORT) | -38.9% (TRIM/SHORT) | -47.5% (TRIM/SHORT) | -44.7% (TRIM/SHORT) | -51.4% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| FRO | -37.1% (TRIM/SHORT) | -37.6% (TRIM/SHORT) | -38.7% (TRIM/SHORT) | -48.4% (TRIM/SHORT) | -45.2% (TRIM/SHORT) | -52.9% (TRIM/SHORT) | -49.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| INSW | -39.7% (TRIM/SHORT) | -39.9% (TRIM/SHORT) | -40.3% (TRIM/SHORT) | -44.9% (TRIM/SHORT) | -43.4% (TRIM/SHORT) | -46.9% (TRIM/SHORT) | -45.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TNK | -5.4% (TRIM/SHORT) | -5.6% (TRIM/SHORT) | -6.1% (TRIM/SHORT) | -12.0% (TRIM/SHORT) | -10.0% (TRIM/SHORT) | -14.6% (TRIM/SHORT) | -12.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| NAT | -54.7% (TRIM/SHORT) | -54.9% (TRIM/SHORT) | -55.5% (TRIM/SHORT) | -61.7% (TRIM/SHORT) | -59.7% (TRIM/SHORT) | -64.4% (TRIM/SHORT) | -62.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| TEN | +47.4% (BUY) | +46.9% (BUY) | +45.9% (BUY) | +35.7% (BUY) | +39.1% (BUY) | +31.2% (BUY) | +35.1% (BUY) | ✓ robust | position BUY across all 7 weight sets |
| CMBT | -21.5% (TRIM/SHORT) | -21.7% (TRIM/SHORT) | -22.1% (TRIM/SHORT) | -26.0% (TRIM/SHORT) | -24.7% (TRIM/SHORT) | -27.8% (TRIM/SHORT) | -26.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 7 weight sets |
| BRUT | +3.6% (HOLD) | +2.3% (HOLD) | -0.5% (HOLD) | -23.2% (TRIM/SHORT) | -15.7% (TRIM/SHORT) | -34.0% (TRIM/SHORT) | -25.3% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -2.7% (HOLD) | -3.5% (HOLD) | -5.5% (TRIM/SHORT) | -21.8% (TRIM/SHORT) | -16.4% (TRIM/SHORT) | -29.4% (TRIM/SHORT) | -23.2% (TRIM/SHORT) | ⚑ driven | HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E |

## Per-name detail

### DHT — price $19.66, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $15.97 | -18.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -19.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.67 | -20.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.91 | -29.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.49 | -26.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.08 | -33.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.76 | -30.0% | TRIM/SHORT |

### ECO — price $66.86, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $41.71 | -37.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.44 | -38.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.83 | -38.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $35.10 | -47.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $37.00 | -44.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.49 | -51.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.66 | -48.2% | TRIM/SHORT |

### FRO — price $44.19, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $27.79 | -37.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $27.57 | -37.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.10 | -38.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $22.81 | -48.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.24 | -45.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $20.82 | -52.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $22.46 | -49.2% | TRIM/SHORT |

### INSW — price $98.81, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $59.59 | -39.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.39 | -39.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.96 | -40.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.49 | -44.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.97 | -43.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.51 | -46.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $54.18 | -45.2% | TRIM/SHORT |

### TNK — price $88.70, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $83.93 | -5.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $83.72 | -5.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $83.25 | -6.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $78.07 | -12.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $79.79 | -10.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $75.77 | -14.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $77.71 | -12.4% | TRIM/SHORT |

### NAT — price $6.77, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $3.07 | -54.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.05 | -54.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.01 | -55.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.59 | -61.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.73 | -59.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.41 | -64.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.57 | -62.1% | TRIM/SHORT |

### TEN — price $42.52, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $62.66 | +47.4% | BUY |
| Crude Set A' (B' reweight, history bracket) | $62.47 | +46.9% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $62.05 | +45.9% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $57.72 | +35.7% | BUY |
| Crude Set C (bullish, extended Phase 1) | $59.15 | +39.1% | BUY |
| Crude Set D (bearish, deep normalization) | $55.81 | +31.2% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $57.42 | +35.1% | BUY |

### CMBT — price $18.35, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 7 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $14.41 | -21.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $14.38 | -21.7% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $14.30 | -22.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $13.58 | -26.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.82 | -24.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.25 | -27.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.52 | -26.3% | TRIM/SHORT |

### BRUT — price $4.94, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $5.12 | +3.6% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.06 | +2.3% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $4.92 | -0.5% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.80 | -23.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.17 | -15.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.26 | -34.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.70 | -25.3% | TRIM/SHORT |

### CAPT — price $16.46, target $18.90

**Classification:** WEIGHT-DRIVEN. HOLD under Set A''/Set A'; TRIM/SHORT under Set A/Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A'' (C2 toll-cliff, production 2026-08-16) | $16.02 | -2.7% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $15.88 | -3.5% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.56 | -5.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $12.87 | -21.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $13.76 | -16.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $11.62 | -29.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $12.65 | -23.2% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

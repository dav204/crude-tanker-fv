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
| TEN | ⚑ driven | BUY under Set A'''/Set A''/Set A'/Set A/Set B/Set C/Set E; HOLD under Set D |
| CMBT | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
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
| DHT | -28.7% (TRIM/SHORT) | -29.6% (TRIM/SHORT) | -30.0% (TRIM/SHORT) | -30.9% (TRIM/SHORT) | -38.5% (TRIM/SHORT) | -36.0% (TRIM/SHORT) | -42.2% (TRIM/SHORT) | -39.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -50.7% (TRIM/SHORT) | -51.6% (TRIM/SHORT) | -51.9% (TRIM/SHORT) | -52.6% (TRIM/SHORT) | -59.3% (TRIM/SHORT) | -57.1% (TRIM/SHORT) | -62.3% (TRIM/SHORT) | -59.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -46.6% (TRIM/SHORT) | -47.5% (TRIM/SHORT) | -47.9% (TRIM/SHORT) | -48.7% (TRIM/SHORT) | -56.3% (TRIM/SHORT) | -53.8% (TRIM/SHORT) | -59.8% (TRIM/SHORT) | -56.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -45.8% (TRIM/SHORT) | -46.4% (TRIM/SHORT) | -46.5% (TRIM/SHORT) | -46.9% (TRIM/SHORT) | -51.0% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | -52.8% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -18.1% (TRIM/SHORT) | -18.8% (TRIM/SHORT) | -19.0% (TRIM/SHORT) | -19.4% (TRIM/SHORT) | -24.7% (TRIM/SHORT) | -22.9% (TRIM/SHORT) | -26.9% (TRIM/SHORT) | -25.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -63.3% (TRIM/SHORT) | -64.0% (TRIM/SHORT) | -64.2% (TRIM/SHORT) | -64.7% (TRIM/SHORT) | -69.9% (TRIM/SHORT) | -68.2% (TRIM/SHORT) | -72.0% (TRIM/SHORT) | -70.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +18.2% (BUY) | +17.0% (BUY) | +16.7% (BUY) | +16.0% (BUY) | +7.4% (BUY) | +10.2% (BUY) | +3.7% (HOLD) | +6.9% (BUY) | ⚑ driven | BUY under Set A'''/Set A''/Set A'/Set A/Set B/Set C/Set E; HOLD under Set D |
| CMBT | -47.6% (TRIM/SHORT) | -48.1% (TRIM/SHORT) | -48.2% (TRIM/SHORT) | -48.6% (TRIM/SHORT) | -52.1% (TRIM/SHORT) | -51.0% (TRIM/SHORT) | -53.7% (TRIM/SHORT) | -52.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +1.4% (HOLD) | -0.9% (HOLD) | -2.1% (HOLD) | -4.8% (HOLD) | -25.9% (TRIM/SHORT) | -19.0% (TRIM/SHORT) | -36.1% (TRIM/SHORT) | -27.9% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -10.3% (TRIM/SHORT) | -11.9% (TRIM/SHORT) | -12.6% (TRIM/SHORT) | -14.3% (TRIM/SHORT) | -28.3% (TRIM/SHORT) | -23.7% (TRIM/SHORT) | -35.0% (TRIM/SHORT) | -29.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Per-name detail

### DHT — price $22.89, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.32 | -28.7% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.12 | -29.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.03 | -30.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.82 | -30.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.07 | -38.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.65 | -36.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.24 | -42.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.91 | -39.2% | TRIM/SHORT |

### ECO — price $85.66, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $42.22 | -50.7% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $41.50 | -51.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.23 | -51.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.63 | -52.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $34.88 | -59.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $36.79 | -57.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.27 | -62.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.45 | -59.8% | TRIM/SHORT |

### FRO — price $53.93, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $28.79 | -46.6% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.30 | -47.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.10 | -47.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.64 | -48.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.59 | -56.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.93 | -53.8% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.70 | -59.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.25 | -56.9% | TRIM/SHORT |

### INSW — price $110.61, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $59.91 | -45.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $59.32 | -46.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.13 | -46.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.70 | -46.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.21 | -51.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.70 | -49.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.23 | -52.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $53.90 | -51.3% | TRIM/SHORT |

### TNK — price $101.59, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $83.24 | -18.1% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $82.48 | -18.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $82.29 | -19.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $81.86 | -19.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $76.51 | -24.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $78.30 | -22.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $74.21 | -26.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $76.19 | -25.0% | TRIM/SHORT |

### NAT — price $8.09, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $2.97 | -63.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $2.91 | -64.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.89 | -64.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.85 | -64.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.44 | -69.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.57 | -68.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.26 | -72.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.41 | -70.2% | TRIM/SHORT |

### TEN — price $52.28, target $51.50

**Classification:** WEIGHT-DRIVEN. BUY under Set A'''/Set A''/Set A'/Set A/Set B/Set C/Set E; HOLD under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.80 | +18.2% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.17 | +17.0% | BUY |
| Crude Set A' (B' reweight, history bracket) | $61.00 | +16.7% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.62 | +16.0% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $56.13 | +7.4% | BUY |
| Crude Set C (bullish, extended Phase 1) | $57.61 | +10.2% | BUY |
| Crude Set D (bearish, deep normalization) | $54.21 | +3.7% | HOLD |
| Crude Set E (Jul-2 stand-down vintage) | $55.87 | +6.9% | BUY |

### CMBT — price $20.49, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $10.73 | -47.6% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $10.64 | -48.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $10.61 | -48.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $10.53 | -48.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $9.81 | -52.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $10.05 | -51.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.48 | -53.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $9.75 | -52.4% | TRIM/SHORT |

### BRUT — price $5.28, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.35 | +1.4% | HOLD |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.23 | -0.9% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.17 | -2.1% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.02 | -4.8% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.91 | -25.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.28 | -19.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.37 | -36.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.81 | -27.9% | TRIM/SHORT |

### CAPT — price $19.81, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $17.77 | -10.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $17.46 | -11.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $17.31 | -12.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.97 | -14.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.19 | -28.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.12 | -23.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.87 | -35.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.94 | -29.6% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

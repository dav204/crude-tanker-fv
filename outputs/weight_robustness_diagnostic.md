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
| DHT | -29.3% (TRIM/SHORT) | -30.2% (TRIM/SHORT) | -30.6% (TRIM/SHORT) | -31.5% (TRIM/SHORT) | -39.1% (TRIM/SHORT) | -36.6% (TRIM/SHORT) | -42.7% (TRIM/SHORT) | -39.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -50.1% (TRIM/SHORT) | -51.0% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | -52.0% (TRIM/SHORT) | -58.8% (TRIM/SHORT) | -56.5% (TRIM/SHORT) | -61.9% (TRIM/SHORT) | -59.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -43.5% (TRIM/SHORT) | -44.5% (TRIM/SHORT) | -44.9% (TRIM/SHORT) | -45.8% (TRIM/SHORT) | -53.7% (TRIM/SHORT) | -51.1% (TRIM/SHORT) | -57.4% (TRIM/SHORT) | -54.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -46.1% (TRIM/SHORT) | -46.7% (TRIM/SHORT) | -46.8% (TRIM/SHORT) | -47.2% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | -49.9% (TRIM/SHORT) | -53.0% (TRIM/SHORT) | -51.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -17.2% (TRIM/SHORT) | -18.0% (TRIM/SHORT) | -18.2% (TRIM/SHORT) | -18.6% (TRIM/SHORT) | -23.9% (TRIM/SHORT) | -22.1% (TRIM/SHORT) | -26.2% (TRIM/SHORT) | -24.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -63.7% (TRIM/SHORT) | -64.4% (TRIM/SHORT) | -64.6% (TRIM/SHORT) | -65.0% (TRIM/SHORT) | -70.1% (TRIM/SHORT) | -68.5% (TRIM/SHORT) | -72.3% (TRIM/SHORT) | -70.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +17.6% (BUY) | +16.4% (BUY) | +16.1% (BUY) | +15.4% (BUY) | +6.8% (BUY) | +9.6% (BUY) | +3.2% (HOLD) | +6.3% (BUY) | ⚑ driven | BUY under Set A'''/Set A''/Set A'/Set A/Set B/Set C/Set E; HOLD under Set D |
| CMBT | -47.9% (TRIM/SHORT) | -48.4% (TRIM/SHORT) | -48.5% (TRIM/SHORT) | -48.9% (TRIM/SHORT) | -52.5% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | -54.1% (TRIM/SHORT) | -52.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +2.1% (HOLD) | -0.2% (HOLD) | -1.4% (HOLD) | -4.1% (HOLD) | -25.4% (TRIM/SHORT) | -18.4% (TRIM/SHORT) | -35.6% (TRIM/SHORT) | -27.4% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -10.0% (TRIM/SHORT) | -11.6% (TRIM/SHORT) | -12.3% (TRIM/SHORT) | -14.1% (TRIM/SHORT) | -28.1% (TRIM/SHORT) | -23.4% (TRIM/SHORT) | -34.8% (TRIM/SHORT) | -29.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Per-name detail

### DHT — price $23.09, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.32 | -29.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.12 | -30.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.03 | -30.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $15.82 | -31.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.07 | -39.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.65 | -36.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.24 | -42.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.91 | -39.7% | TRIM/SHORT |

### ECO — price $84.61, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $42.22 | -50.1% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $41.50 | -51.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $41.23 | -51.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $40.63 | -52.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $34.88 | -58.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $36.79 | -56.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $32.27 | -61.9% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $34.45 | -59.3% | TRIM/SHORT |

### FRO — price $50.96, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $28.79 | -43.5% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.30 | -44.5% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.10 | -44.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $27.64 | -45.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $23.59 | -53.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $24.93 | -51.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.70 | -57.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.25 | -54.4% | TRIM/SHORT |

### INSW — price $111.21, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $59.91 | -46.1% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $59.32 | -46.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $59.13 | -46.8% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $58.70 | -47.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.21 | -51.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $55.70 | -49.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $52.23 | -53.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $53.90 | -51.5% | TRIM/SHORT |

### TNK — price $100.54, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $83.24 | -17.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $82.48 | -18.0% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $82.29 | -18.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $81.86 | -18.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $76.51 | -23.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $78.30 | -22.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $74.21 | -26.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $76.19 | -24.2% | TRIM/SHORT |

### NAT — price $8.16, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $2.97 | -63.7% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $2.91 | -64.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $2.89 | -64.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $2.85 | -65.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.44 | -70.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.57 | -68.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.26 | -72.3% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.41 | -70.4% | TRIM/SHORT |

### TEN — price $52.55, target $51.50

**Classification:** WEIGHT-DRIVEN. BUY under Set A'''/Set A''/Set A'/Set A/Set B/Set C/Set E; HOLD under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.80 | +17.6% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.17 | +16.4% | BUY |
| Crude Set A' (B' reweight, history bracket) | $61.00 | +16.1% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.62 | +15.4% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $56.13 | +6.8% | BUY |
| Crude Set C (bullish, extended Phase 1) | $57.61 | +9.6% | BUY |
| Crude Set D (bearish, deep normalization) | $54.21 | +3.2% | HOLD |
| Crude Set E (Jul-2 stand-down vintage) | $55.87 | +6.3% | BUY |

### CMBT — price $20.15, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $10.50 | -47.9% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $10.40 | -48.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $10.37 | -48.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $10.30 | -48.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $9.57 | -52.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $9.81 | -51.3% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.24 | -54.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $9.51 | -52.8% | TRIM/SHORT |

### BRUT — price $5.24, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.35 | +2.1% | HOLD |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.23 | -0.2% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.17 | -1.4% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.02 | -4.1% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $3.91 | -25.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.28 | -18.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.37 | -35.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $3.81 | -27.4% | TRIM/SHORT |

### CAPT — price $19.75, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $17.77 | -10.0% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $17.46 | -11.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $17.31 | -12.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.97 | -14.1% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.19 | -28.1% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.12 | -23.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.87 | -34.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $13.94 | -29.4% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

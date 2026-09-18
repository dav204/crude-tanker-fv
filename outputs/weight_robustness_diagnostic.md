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
| DHT | -28.3% (TRIM/SHORT) | -29.1% (TRIM/SHORT) | -29.5% (TRIM/SHORT) | -30.3% (TRIM/SHORT) | -37.5% (TRIM/SHORT) | -35.1% (TRIM/SHORT) | -41.1% (TRIM/SHORT) | -38.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -47.8% (TRIM/SHORT) | -48.6% (TRIM/SHORT) | -48.9% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | -56.2% (TRIM/SHORT) | -54.0% (TRIM/SHORT) | -59.5% (TRIM/SHORT) | -56.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -42.4% (TRIM/SHORT) | -43.2% (TRIM/SHORT) | -43.6% (TRIM/SHORT) | -44.5% (TRIM/SHORT) | -52.2% (TRIM/SHORT) | -49.6% (TRIM/SHORT) | -56.0% (TRIM/SHORT) | -53.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -44.4% (TRIM/SHORT) | -44.9% (TRIM/SHORT) | -45.1% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | -49.5% (TRIM/SHORT) | -48.1% (TRIM/SHORT) | -51.4% (TRIM/SHORT) | -49.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -12.9% (TRIM/SHORT) | -13.4% (TRIM/SHORT) | -13.7% (TRIM/SHORT) | -14.4% (TRIM/SHORT) | -19.7% (TRIM/SHORT) | -17.9% (TRIM/SHORT) | -22.4% (TRIM/SHORT) | -20.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -60.4% (TRIM/SHORT) | -60.9% (TRIM/SHORT) | -61.2% (TRIM/SHORT) | -61.8% (TRIM/SHORT) | -66.9% (TRIM/SHORT) | -65.2% (TRIM/SHORT) | -69.5% (TRIM/SHORT) | -67.5% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +24.8% (BUY) | +24.0% (BUY) | +23.4% (BUY) | +22.2% (BUY) | +13.3% (BUY) | +16.3% (BUY) | +8.6% (BUY) | +12.2% (BUY) | ✓ robust | position BUY across all 8 weight sets |
| CMBT | -46.4% (TRIM/SHORT) | -46.7% (TRIM/SHORT) | -46.9% (TRIM/SHORT) | -47.3% (TRIM/SHORT) | -50.9% (TRIM/SHORT) | -49.7% (TRIM/SHORT) | -52.6% (TRIM/SHORT) | -51.3% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +5.2% (BUY) | +3.0% (HOLD) | +1.9% (HOLD) | -0.6% (HOLD) | -20.9% (TRIM/SHORT) | -14.0% (TRIM/SHORT) | -31.2% (TRIM/SHORT) | -23.1% (TRIM/SHORT) | ⚑ driven | BUY under Set A'''; HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -6.0% (TRIM/SHORT) | -7.3% (TRIM/SHORT) | -8.1% (TRIM/SHORT) | -9.9% (TRIM/SHORT) | -23.5% (TRIM/SHORT) | -18.9% (TRIM/SHORT) | -30.5% (TRIM/SHORT) | -25.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Per-name detail

### DHT — price $23.09, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.56 | -28.3% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.37 | -29.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.29 | -29.5% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.10 | -30.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.42 | -37.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.99 | -35.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.59 | -41.1% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.25 | -38.3% | TRIM/SHORT |

### ECO — price $84.61, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $44.15 | -47.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $43.53 | -48.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $43.24 | -48.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $42.61 | -49.6% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $37.02 | -56.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $38.92 | -54.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $34.26 | -59.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $36.44 | -56.9% | TRIM/SHORT |

### FRO — price $50.96, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $29.38 | -42.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.92 | -43.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.73 | -43.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $28.30 | -44.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $24.36 | -52.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $25.70 | -49.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $22.43 | -56.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.97 | -53.0% | TRIM/SHORT |

### INSW — price $111.21, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.81 | -44.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.31 | -44.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $61.09 | -45.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.60 | -45.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $56.17 | -49.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $57.68 | -48.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $54.00 | -51.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $55.73 | -49.9% | TRIM/SHORT |

### TNK — price $100.54, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $87.59 | -12.9% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $87.05 | -13.4% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $86.75 | -13.7% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $86.09 | -14.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $80.76 | -19.7% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $82.58 | -17.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $78.02 | -22.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $80.14 | -20.3% | TRIM/SHORT |

### NAT — price $8.16, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $3.24 | -60.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $3.19 | -60.9% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.17 | -61.2% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.12 | -61.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.70 | -66.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.84 | -65.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.49 | -69.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.66 | -67.5% | TRIM/SHORT |

### TEN — price $52.55, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $65.59 | +24.8% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $65.15 | +24.0% | BUY |
| Crude Set A' (B' reweight, history bracket) | $64.86 | +23.4% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $64.22 | +22.2% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $59.53 | +13.3% | BUY |
| Crude Set C (bullish, extended Phase 1) | $61.12 | +16.3% | BUY |
| Crude Set D (bearish, deep normalization) | $57.09 | +8.6% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $58.97 | +12.2% | BUY |

### CMBT — price $20.15, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $10.81 | -46.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $10.73 | -46.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $10.69 | -46.9% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $10.61 | -47.3% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $9.90 | -50.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $10.14 | -49.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.54 | -52.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $9.82 | -51.3% | TRIM/SHORT |

### BRUT — price $5.24, target $4.56

**Classification:** WEIGHT-DRIVEN. BUY under Set A'''; HOLD under Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.51 | +5.2% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.40 | +3.0% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.34 | +1.9% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.21 | -0.6% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $4.14 | -20.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.51 | -14.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.61 | -31.2% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $4.03 | -23.1% | TRIM/SHORT |

### CAPT — price $19.75, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $18.57 | -6.0% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $18.30 | -7.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $18.14 | -8.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $17.80 | -9.9% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $15.10 | -23.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $16.02 | -18.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.72 | -30.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.79 | -25.1% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

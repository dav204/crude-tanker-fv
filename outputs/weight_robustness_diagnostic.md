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
| DHT | -28.8% (TRIM/SHORT) | -29.6% (TRIM/SHORT) | -30.0% (TRIM/SHORT) | -30.8% (TRIM/SHORT) | -38.0% (TRIM/SHORT) | -35.6% (TRIM/SHORT) | -41.6% (TRIM/SHORT) | -38.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| ECO | -48.0% (TRIM/SHORT) | -48.8% (TRIM/SHORT) | -49.1% (TRIM/SHORT) | -49.8% (TRIM/SHORT) | -56.4% (TRIM/SHORT) | -54.2% (TRIM/SHORT) | -59.7% (TRIM/SHORT) | -57.1% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| FRO | -42.9% (TRIM/SHORT) | -43.8% (TRIM/SHORT) | -44.1% (TRIM/SHORT) | -45.0% (TRIM/SHORT) | -52.6% (TRIM/SHORT) | -50.0% (TRIM/SHORT) | -56.4% (TRIM/SHORT) | -53.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| INSW | -44.4% (TRIM/SHORT) | -44.8% (TRIM/SHORT) | -45.0% (TRIM/SHORT) | -45.5% (TRIM/SHORT) | -49.5% (TRIM/SHORT) | -48.1% (TRIM/SHORT) | -51.4% (TRIM/SHORT) | -49.9% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TNK | -13.2% (TRIM/SHORT) | -13.7% (TRIM/SHORT) | -14.0% (TRIM/SHORT) | -14.7% (TRIM/SHORT) | -20.0% (TRIM/SHORT) | -18.2% (TRIM/SHORT) | -22.7% (TRIM/SHORT) | -20.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| NAT | -60.8% (TRIM/SHORT) | -61.3% (TRIM/SHORT) | -61.6% (TRIM/SHORT) | -62.2% (TRIM/SHORT) | -67.3% (TRIM/SHORT) | -65.5% (TRIM/SHORT) | -69.8% (TRIM/SHORT) | -67.8% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| TEN | +25.9% (BUY) | +25.1% (BUY) | +24.5% (BUY) | +23.3% (BUY) | +14.3% (BUY) | +17.3% (BUY) | +9.6% (BUY) | +13.2% (BUY) | ✓ robust | position BUY across all 8 weight sets |
| CMBT | -46.7% (TRIM/SHORT) | -47.1% (TRIM/SHORT) | -47.3% (TRIM/SHORT) | -47.7% (TRIM/SHORT) | -51.2% (TRIM/SHORT) | -50.0% (TRIM/SHORT) | -53.0% (TRIM/SHORT) | -51.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |
| BRUT | +4.6% (HOLD) | +2.4% (HOLD) | +1.3% (HOLD) | -1.1% (HOLD) | -21.4% (TRIM/SHORT) | -14.5% (TRIM/SHORT) | -31.5% (TRIM/SHORT) | -23.6% (TRIM/SHORT) | ⚑ driven | HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E |
| CAPT | -5.8% (TRIM/SHORT) | -7.2% (TRIM/SHORT) | -8.0% (TRIM/SHORT) | -9.7% (TRIM/SHORT) | -23.4% (TRIM/SHORT) | -18.7% (TRIM/SHORT) | -30.4% (TRIM/SHORT) | -25.0% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all 8 weight sets |

## Per-name detail

### DHT — price $23.27, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $16.56 | -28.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $16.37 | -29.6% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $16.29 | -30.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $16.10 | -30.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.42 | -38.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $14.99 | -35.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.59 | -41.6% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.25 | -38.8% | TRIM/SHORT |

### ECO — price $84.95, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $44.15 | -48.0% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $43.53 | -48.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $43.24 | -49.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $42.61 | -49.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $37.02 | -56.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $38.92 | -54.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $34.26 | -59.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $36.44 | -57.1% | TRIM/SHORT |

### FRO — price $51.42, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $29.38 | -42.9% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $28.92 | -43.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $28.73 | -44.1% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $28.30 | -45.0% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $24.36 | -52.6% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $25.70 | -50.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $22.43 | -56.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $23.97 | -53.4% | TRIM/SHORT |

### INSW — price $111.15, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $61.81 | -44.4% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $61.31 | -44.8% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $61.09 | -45.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $60.60 | -45.5% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $56.17 | -49.5% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $57.68 | -48.1% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $54.00 | -51.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $55.73 | -49.9% | TRIM/SHORT |

### TNK — price $100.92, target $75.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $87.59 | -13.2% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $87.05 | -13.7% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $86.75 | -14.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $86.09 | -14.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $80.76 | -20.0% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $82.58 | -18.2% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $78.02 | -22.7% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $80.14 | -20.6% | TRIM/SHORT |

### NAT — price $8.25, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $3.24 | -60.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $3.19 | -61.3% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $3.17 | -61.6% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $3.12 | -62.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.70 | -67.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.84 | -65.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.49 | -69.8% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $2.66 | -67.8% | TRIM/SHORT |

### TEN — price $52.09, target $51.50

**Classification:** WEIGHT-ROBUST. position BUY across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $65.59 | +25.9% | BUY |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $65.15 | +25.1% | BUY |
| Crude Set A' (B' reweight, history bracket) | $64.86 | +24.5% | BUY |
| Crude Set A (Jun-9 war tilt, history bracket) | $64.22 | +23.3% | BUY |
| Crude Set B (Catlin-leaning, slow normalization) | $59.53 | +14.3% | BUY |
| Crude Set C (bullish, extended Phase 1) | $61.12 | +17.3% | BUY |
| Crude Set D (bearish, deep normalization) | $57.09 | +9.6% | BUY |
| Crude Set E (Jul-2 stand-down vintage) | $58.97 | +13.2% | BUY |

### CMBT — price $20.29, target $16.59

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $10.81 | -46.7% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $10.73 | -47.1% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $10.69 | -47.3% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $10.61 | -47.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $9.90 | -51.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $10.14 | -50.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $9.54 | -53.0% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $9.82 | -51.6% | TRIM/SHORT |

### BRUT — price $5.27, target $4.56

**Classification:** WEIGHT-DRIVEN. HOLD under Set A'''/Set A''/Set A'/Set A; TRIM/SHORT under Set B/Set C/Set D/Set E.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $5.51 | +4.6% | HOLD |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $5.40 | +2.4% | HOLD |
| Crude Set A' (B' reweight, history bracket) | $5.34 | +1.3% | HOLD |
| Crude Set A (Jun-9 war tilt, history bracket) | $5.21 | -1.1% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $4.14 | -21.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $4.51 | -14.5% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $3.61 | -31.5% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $4.03 | -23.6% | TRIM/SHORT |

### CAPT — price $19.71, target $18.90

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all 8 weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A''' (C3 re-armed, production 2026-09-10) | $18.57 | -5.8% | TRIM/SHORT |
| Crude Set A'' (C2 toll-cliff, production 2026-08-16 to 09-10, history bracket) | $18.30 | -7.2% | TRIM/SHORT |
| Crude Set A' (B' reweight, history bracket) | $18.14 | -8.0% | TRIM/SHORT |
| Crude Set A (Jun-9 war tilt, history bracket) | $17.80 | -9.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $15.10 | -23.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $16.02 | -18.7% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $13.72 | -30.4% | TRIM/SHORT |
| Crude Set E (Jul-2 stand-down vintage) | $14.79 | -25.0% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

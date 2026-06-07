# Crude Weight-Robustness Diagnostic

Diagnostic (METHODOLOGY §9.10) — does NOT change the locked Crude Set A weights. Surfaces which crude tanker calls survive defensible reweighting (call is **weight-robust**) vs which depend on a specific weight prior (**weight-driven**).

**Driver:** Catlin / VIE analysis (2026-05-25) plus the June 1 macro briefing suggest current Set A weights may put too much weight on "deep normalisation" relative to "slow normalisation with extended Phase 1." Sets B/C/D bracket the normalisation-speed axis.

**Naming namespace:** the labels below are CRUDE-sector weight families. The LNG sector uses its own "Set B" / "Set B-revised" naming (METHODOLOGY §11.3). Cross-sector conflation would be a methodology error.

## Key findings (combined mark + weight robustness)

Cross-referencing with the broker-NAV sweep (`outputs/broker_nav_sweep.md`):

| Ticker | Mark spread | Weight robustness | Combined conviction |
|---|---:|---|---|
| DHT  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |
| ECO  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |
| FRO  | −1pp  (mark-robust)  | ✓ robust | **HIGHEST** — TRIM survives both dimensions |
| INSW | +22pp (mark-driven)  | ✓ robust | MIXED — TRIM survives weights but depends on marks |
| TNK  | +10pp (mark-driven)  | ⚑ driven | **LOWEST** — call sensitive to BOTH dimensions |
| NAT  | +53pp (mark-driven)  | ✓ robust | **§12 archetype** — tool TRIM is structural (read NAV as floor, not call) |

**Takeaway:** the three pure-VLCC / VLCC+Suezmax names (DHT/ECO/FRO) are the highest-conviction TRIM calls in the current crude watchlist — their TRIM signal survives both a reasonable mark perturbation AND a defensible reweighting toward Catlin's slow-normalisation view. **TNK is the only name where both judgemental dimensions matter** — and specifically, TNK flips to TRIM/SHORT only under the bearish Set D weighting; under the Catlin-leaning Set B TNK's EV is mildly positive (+0.8%). For TNK position decisions, the weight prior is the dominant uncertainty.

## Weight sets compared

| Scenario | Set A (current) | Set B (Catlin) | Set C (bullish) | Set D (bearish) |
|---|--:|--:|--:|--:|
| escalation | 0.10 | 0.10 | 0.15 | 0.05 |
| pre_mou_baseline | 0.15 | 0.25 | 0.30 | 0.10 |
| mou_base | 0.50 | 0.45 | 0.40 | 0.55 |
| mou_bear | 0.25 | 0.20 | 0.15 | 0.30 |

Set B (Catlin-leaning) shifts 10pp from `mou_base` and 5pp from `mou_bear` into `pre_mou_baseline` — i.e. Phase 1 extends, Phase 2 normalisation arrives later. Set C is more bullish (15pp into Phase 1). Set D is more bearish (15pp deeper into MoU phase).

## Summary — per-name robustness

| Ticker | Set A EV | Set B EV | Set C EV | Set D EV | Robustness | Notes |
|---|--:|--:|--:|--:|---|---|
| DHT | -18.7% (TRIM/SHORT) | -14.2% (TRIM/SHORT) | -8.4% (TRIM/SHORT) | -24.4% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all four weight sets |
| ECO | -32.4% (TRIM/SHORT) | -27.3% (TRIM/SHORT) | -20.9% (TRIM/SHORT) | -38.7% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all four weight sets |
| FRO | -30.8% (TRIM/SHORT) | -25.4% (TRIM/SHORT) | -18.6% (TRIM/SHORT) | -37.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all four weight sets |
| INSW | -32.2% (TRIM/SHORT) | -28.9% (TRIM/SHORT) | -24.9% (TRIM/SHORT) | -36.2% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all four weight sets |
| TNK | -1.7% (HOLD) | +0.8% (HOLD) | +4.2% (HOLD) | -5.0% (TRIM/SHORT) | ⚑ driven | HOLD under Set A/Set B/Set C; TRIM/SHORT under Set D |
| NAT | -57.8% (TRIM/SHORT) | -53.8% (TRIM/SHORT) | -49.0% (TRIM/SHORT) | -62.6% (TRIM/SHORT) | ✓ robust | position TRIM/SHORT across all four weight sets |

## Per-name detail

### DHT — price $16.40, target $16.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all four weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $13.34 | -18.7% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $14.08 | -14.2% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $15.02 | -8.4% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $12.39 | -24.4% | TRIM/SHORT |

### ECO — price $48.10, target $45.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all four weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $32.53 | -32.4% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $34.97 | -27.3% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $38.03 | -20.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $29.47 | -38.7% | TRIM/SHORT |

### FRO — price $34.50, target $30.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all four weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $23.87 | -30.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $25.75 | -25.4% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $28.10 | -18.6% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $21.52 | -37.6% | TRIM/SHORT |

### INSW — price $76.80, target $79.50

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all four weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $52.08 | -32.2% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $54.59 | -28.9% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $57.66 | -24.9% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $49.01 | -36.2% | TRIM/SHORT |

### TNK — price $70.50, target $75.00

**Classification:** WEIGHT-DRIVEN. HOLD under Set A/Set B/Set C; TRIM/SHORT under Set D.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $69.31 | -1.7% | HOLD |
| Crude Set B (Catlin-leaning, slow normalization) | $71.10 | +0.8% | HOLD |
| Crude Set C (bullish, extended Phase 1) | $73.44 | +4.2% | HOLD |
| Crude Set D (bearish, deep normalization) | $66.97 | -5.0% | TRIM/SHORT |

### NAT — price $5.40, target $6.00

**Classification:** WEIGHT-ROBUST. position TRIM/SHORT across all four weight sets.

| Weight set | PW FV | EV % | Position |
|---|--:|--:|---|
| Crude Set A (current locked) | $2.28 | -57.8% | TRIM/SHORT |
| Crude Set B (Catlin-leaning, slow normalization) | $2.49 | -53.8% | TRIM/SHORT |
| Crude Set C (bullish, extended Phase 1) | $2.76 | -49.0% | TRIM/SHORT |
| Crude Set D (bearish, deep normalization) | $2.02 | -62.6% | TRIM/SHORT |

## Combined mark + weight robustness framework

Pairing this diagnostic with the broker-NAV sweep (METHODOLOGY §9.9) gives every name two robustness dimensions:

- **Mark-robust + weight-robust** = highest-conviction signals (call survives both vessel-mark uncertainty and probability-weight reshuffling)
- **Mark-driven OR weight-driven** (one of the two) = moderate conviction; the call depends on one specific judgemental input
- **Mark-driven AND weight-driven** = lowest conviction; two compounding judgemental dependencies. Treat with explicit sizing discipline.

See METHODOLOGY §9.9 (mark robustness) and §9.10 (weight robustness) for the methodology. This diagnostic is the §9.10 output for the crude sector; the LNG analogue lives in `outputs/lng_weight_robustness.md`.

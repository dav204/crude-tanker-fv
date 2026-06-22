# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.3% of vessel value) + product sleeve (34.7%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Per-sleeve FVs flow through the same scenario set (METHODOLOGY 6 v2).

- **Current price:** $84.49
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.39 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $61.16 (-27.6% vs price)
- **Breakeven TCE (scenario-invariant):** $316,872/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $65.51 | $77.65 | $73.75–$82.16 | 6.12× | 0.70 | $105.97 | $166,758 | 0.53× |
| Pre-MoU baseline | 45% | 1.09× | $60.15 | $65.66 | $63.24–$68.40 | 3.78× | 0.70 | $78.53 | $102,045 | 0.32× |
| MoU base case | 18% | 0.75× | $42.39 | $42.17 | $40.59–$43.83 | 1.77× | 0.70 | $42.07 | $48,111 | 0.15× |
| MoU bear | 12% | 0.71× | $39.42 | $38.41 | $36.76–$40.15 | 1.45× | 0.60 | $37.39 | $38,839 | 0.12× |
| **Probability-weighted** | | | | **$61.16** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-6.84
- **Downside (worst scenario − price):** $-46.08
- **Expected value vs current** (weighted FV − price): $-23.33 (-27.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.3% | $55.17 | $40.23 | -27.1% | TRIM/SHORT |
| Product | 34.7% | $29.32 | $19.78 | -32.5% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$84.49** | **$61.16** | **-27.6%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._

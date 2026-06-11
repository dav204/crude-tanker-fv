# INSW [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY = crude sleeve (65.3% of vessel value) + product sleeve (34.7%) AGGREGATED. Compared to the WHOLE-COMPANY tape price (not the crude-allocated proxy). Per-sleeve FVs flow through the same scenario set (METHODOLOGY 6 v2).

- **Current price:** $82.61
- **Analyst target:** $79.50
- **NAV / share (reference, unflexed):** $52.40 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $59.47 (-28.0% vs price)
- **Breakeven TCE (scenario-invariant):** $393,378/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $65.52 | $74.11 | $71.27–$77.38 | 6.12× | 0.70 | $94.15 | $166,747 | 0.42× |
| Pre-MoU baseline | 45% | 1.09× | $60.16 | $63.97 | $62.22–$65.96 | 3.78× | 0.70 | $72.87 | $102,039 | 0.26× |
| MoU base case | 18% | 0.75× | $42.40 | $42.10 | $40.95–$43.31 | 1.77× | 0.70 | $41.81 | $48,109 | 0.12× |
| MoU bear | 12% | 0.71× | $39.42 | $38.16 | $36.96–$39.42 | 1.45× | 0.60 | $36.75 | $38,838 | 0.10× |
| **Probability-weighted** | | | | **$59.47** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-8.50
- **Downside (worst scenario − price):** $-44.45
- **Expected value vs current** (weighted FV − price): $-23.14 (-28.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

## Hybrid sleeve breakdown (v2 whole-company aggregation)

| Sleeve | Share | Allocated price | Weighted FV | EV% | Position |
|---|--:|--:|--:|--:|---|
| Crude | 65.3% | $53.95 | $38.81 | -28.1% | TRIM/SHORT |
| Product | 34.7% | $28.66 | $19.54 | -31.8% | TRIM/SHORT |
| **WHOLE-COMPANY** | 100% | **$82.61** | **$59.47** | **-28.0%** | **TRIM/SHORT** |

_Whole-company FV = crude FV + product FV (both per shares-outstanding); compared against the whole-company tape price, not the carved proxy. The product sleeve uses CLEAN trading rates (LR1/LR2 via clean curves, MR via its own scenario forwards). The product sleeve carries MORE downside than crude because product is leading the MoU rate normalisation (MR -52% w/w, LR2 -28% w/w as of 2026-05-29) — flagged in METHODOLOGY 6 v2._

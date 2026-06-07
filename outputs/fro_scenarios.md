# FRO — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $34.50
- **Analyst target:** $30.50
- **NAV / share (reference, unflexed):** $28.79 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.87 (-30.8% vs price)
- **Breakeven TCE (scenario-invariant):** $207,932/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $39.12 | $46.11 | $44.29–$48.22 | 7.66× | 0.70 | $62.44 | $280,973 | 1.35× |
| Pre-MoU baseline | 15% | 1.11× | $33.19 | $36.64 | $35.60–$37.82 | 4.29× | 0.70 | $44.70 | $155,763 | 0.75× |
| MoU base case | 50% | 0.75× | $18.43 | $19.29 | $18.67–$19.87 | 2.00× | 0.70 | $21.29 | $72,711 | 0.35× |
| MoU bear | 25% | 0.69× | $15.91 | $16.48 | $15.91–$17.06 | 1.38× | 0.60 | $17.34 | $49,590 | 0.24× |
| **Probability-weighted** | | | | **$23.87** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.61
- **Downside (worst scenario − price):** $-18.02
- **Expected value vs current** (weighted FV − price): $-10.63 (-30.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

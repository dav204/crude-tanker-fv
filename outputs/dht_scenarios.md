# DHT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $17.18
- **Analyst target:** $16.00
- **NAV / share (reference, unflexed):** $13.88 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $11.35 (-33.9% vs price)
- **Breakeven TCE (scenario-invariant):** $318,149/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $17.85 | $20.59 | $19.87–$21.42 | 8.44× | 0.70 | $26.97 | $337,500 | 1.06× |
| Pre-MoU baseline | 20% | 0.82× | $10.95 | $11.59 | $11.33–$11.87 | 2.65× | 0.70 | $13.08 | $106,100 | 0.33× |
| MoU base case | 45% | 0.74× | $9.80 | $10.27 | $10.02–$10.50 | 2.12× | 0.70 | $11.36 | $84,875 | 0.27× |
| MoU bear | 25% | 0.70× | $9.06 | $9.41 | $9.22–$9.59 | 1.63× | 0.70 | $10.21 | $65,250 | 0.21× |
| **Probability-weighted** | | | | **$11.35** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.41
- **Downside (worst scenario − price):** $-7.77
- **Expected value vs current** (weighted FV − price): $-5.83 (-33.9%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

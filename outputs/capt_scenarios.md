# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.94
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.38 (-4.0% vs price)
- **Breakeven TCE (scenario-invariant):** $19,107/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.50 | $24.41 | $23.64–$25.30 | 7.00× | 0.70 | $28.88 | $246,248 | 12.89× |
| Pre-MoU baseline | 57% | 0.82× | $10.40 | $10.39 | $10.10–$10.69 | 2.32× | 0.70 | $10.36 | $81,128 | 4.25× |
| MoU base case | 5% | 0.75× | $8.51 | $8.33 | $8.08–$8.57 | 1.90× | 0.70 | $7.90 | $66,145 | 3.46× |
| MoU bear | 13% | 0.71× | $7.24 | $7.21 | $6.94–$7.47 | 1.50× | 0.60 | $7.15 | $51,979 | 2.72× |
| **Probability-weighted** | | | | **$13.38** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+10.47
- **Downside (worst scenario − price):** $-6.73
- **Expected value vs current** (weighted FV − price): $-0.56 (-4.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

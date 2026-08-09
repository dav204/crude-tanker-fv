# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.94
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.39 (-3.9% vs price)
- **Breakeven TCE (scenario-invariant):** $18,274/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $22.49 | $24.43 | $23.66–$25.32 | 7.00× | 0.70 | $28.97 | $246,259 | 13.48× |
| Pre-MoU baseline | 57% | 0.82× | $10.39 | $10.40 | $10.11–$10.70 | 2.32× | 0.70 | $10.42 | $81,132 | 4.44× |
| MoU base case | 5% | 0.75× | $8.50 | $8.34 | $8.09–$8.58 | 1.90× | 0.70 | $7.95 | $66,149 | 3.62× |
| MoU bear | 13% | 0.71× | $7.24 | $7.22 | $6.96–$7.49 | 1.50× | 0.60 | $7.20 | $51,983 | 2.84× |
| **Probability-weighted** | | | | **$13.39** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+10.50
- **Downside (worst scenario − price):** $-6.72
- **Expected value vs current** (weighted FV − price): $-0.55 (-3.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.33
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.38 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.53 (-7.1% vs price)
- **Breakeven TCE (scenario-invariant):** $31,433/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $30.23 | $29.75 | $29.12–$30.38 | 1.77× | 0.70 | $28.63 | $36,270 | 1.15× |
| Moderate growth (base) | 40% | 0.99× | $24.98 | $24.18 | $23.55–$24.81 | 1.32× | 0.60 | $22.98 | $26,893 | 0.86× |
| China property drag | 25% | 0.89× | $21.81 | $20.80 | $20.17–$21.43 | 1.06× | 0.50 | $19.79 | $21,015 | 0.67× |
| Coordinated slowdown | 15% | 0.82× | $19.44 | $18.02 | $17.50–$18.53 | 0.90× | 0.50 | $16.59 | $18,175 | 0.58× |
| **Probability-weighted** | | | | **$23.53** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.42
- **Downside (worst scenario − price):** $-7.31
- **Expected value vs current** (weighted FV − price): $-1.80 (-7.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

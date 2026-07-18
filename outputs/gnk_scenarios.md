# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.12
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.82 (-1.2% vs price)
- **Breakeven TCE (scenario-invariant):** $23,026/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.16× | $30.48 | $29.95 | $29.33–$30.56 | 1.76× | 0.70 | $28.70 | $35,902 | 1.56× |
| Moderate growth (base) | 40% | 0.99× | $25.31 | $24.46 | $23.85–$25.07 | 1.32× | 0.60 | $23.19 | $26,642 | 1.16× |
| China property drag | 25% | 0.90× | $22.20 | $21.16 | $20.53–$21.78 | 1.06× | 0.50 | $20.11 | $20,882 | 0.91× |
| Coordinated slowdown | 15% | 0.82× | $19.84 | $18.39 | $17.89–$18.89 | 0.90× | 0.50 | $16.95 | $18,038 | 0.78× |
| **Probability-weighted** | | | | **$23.82** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.83
- **Downside (worst scenario − price):** $-5.73
- **Expected value vs current** (weighted FV − price): $-0.30 (-1.2%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

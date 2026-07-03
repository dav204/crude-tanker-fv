# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.50
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $24.69 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.56 (-3.9% vs price)
- **Breakeven TCE (scenario-invariant):** $29,692/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $30.20 | $29.71 | $29.10–$30.32 | 1.76× | 0.70 | $28.55 | $36,034 | 1.21× |
| Moderate growth (base) | 40% | 1.01× | $25.00 | $24.20 | $23.59–$24.81 | 1.32× | 0.60 | $23.00 | $26,732 | 0.90× |
| China property drag | 25% | 0.91× | $21.86 | $20.87 | $20.25–$21.50 | 1.06× | 0.50 | $19.89 | $20,930 | 0.70× |
| Coordinated slowdown | 15% | 0.83× | $19.49 | $18.11 | $17.60–$18.61 | 0.90× | 0.50 | $16.72 | $18,087 | 0.61× |
| **Probability-weighted** | | | | **$23.56** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+5.21
- **Downside (worst scenario − price):** $-6.39
- **Expected value vs current** (weighted FV − price): $-0.94 (-3.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

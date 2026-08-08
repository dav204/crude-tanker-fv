# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.33
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.98 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $24.08 (-4.9% vs price)
- **Breakeven TCE (scenario-invariant):** $27,848/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $30.78 | $30.22 | $29.60–$30.83 | 1.76× | 0.70 | $28.90 | $35,770 | 1.28× |
| Moderate growth (base) | 40% | 0.99× | $25.60 | $24.72 | $24.10–$25.33 | 1.32× | 0.60 | $23.39 | $26,552 | 0.95× |
| China property drag | 25% | 0.89× | $22.50 | $21.41 | $20.79–$22.03 | 1.06× | 0.50 | $20.32 | $20,834 | 0.75× |
| Coordinated slowdown | 15% | 0.82× | $20.13 | $18.64 | $18.14–$19.14 | 0.90× | 0.50 | $17.15 | $17,988 | 0.65× |
| **Probability-weighted** | | | | **$24.08** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.89
- **Downside (worst scenario − price):** $-6.69
- **Expected value vs current** (weighted FV − price): $-1.25 (-4.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

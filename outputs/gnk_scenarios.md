# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.57
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $24.64 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $24.02 (+1.9% vs price)
- **Breakeven TCE (scenario-invariant):** $22,647/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $30.94 | $30.38 | $29.76–$30.99 | 1.76× | 0.70 | $29.05 | $36,057 | 1.59× |
| Moderate growth (base) | 40% | 1.03× | $25.54 | $24.68 | $24.07–$25.30 | 1.32× | 0.60 | $23.40 | $26,747 | 1.18× |
| China property drag | 25% | 0.92× | $22.29 | $21.25 | $20.63–$21.88 | 1.06× | 0.50 | $20.22 | $20,938 | 0.92× |
| Coordinated slowdown | 15% | 0.84× | $19.83 | $18.41 | $17.91–$18.91 | 0.90× | 0.50 | $16.99 | $18,095 | 0.80× |
| **Probability-weighted** | | | | **$24.02** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.81
- **Downside (worst scenario − price):** $-5.16
- **Expected value vs current** (weighted FV − price): $+0.45 (+1.9%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

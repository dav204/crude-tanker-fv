# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.57
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $24.69 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $24.05 (+2.0% vs price)
- **Breakeven TCE (scenario-invariant):** $22,511/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** HOLD (fairly valued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $31.00 | $30.41 | $29.80–$31.03 | 1.76× | 0.70 | $29.05 | $36,034 | 1.60× |
| Moderate growth (base) | 40% | 1.03× | $25.59 | $24.71 | $24.10–$25.33 | 1.32× | 0.60 | $23.40 | $26,732 | 1.19× |
| China property drag | 25% | 0.92× | $22.34 | $21.28 | $20.66–$21.90 | 1.06× | 0.50 | $20.22 | $20,930 | 0.93× |
| Coordinated slowdown | 15% | 0.84× | $19.88 | $18.43 | $17.93–$18.93 | 0.90× | 0.50 | $16.99 | $18,087 | 0.80× |
| **Probability-weighted** | | | | **$24.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.84
- **Downside (worst scenario − price):** $-5.14
- **Expected value vs current** (weighted FV − price): $+0.48 (+2.0%)
- **Position:** HOLD (fairly valued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

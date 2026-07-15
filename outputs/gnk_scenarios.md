# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.45
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $24.69 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.15 (-9.0% vs price)
- **Breakeven TCE (scenario-invariant):** $36,008/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.16× | $29.56 | $29.14 | $28.53–$29.75 | 1.76× | 0.70 | $28.15 | $36,034 | 1.00× |
| Moderate growth (base) | 40% | 0.99× | $24.51 | $23.78 | $23.17–$24.40 | 1.32× | 0.60 | $22.69 | $26,732 | 0.74× |
| China property drag | 25% | 0.90× | $21.47 | $20.55 | $19.93–$21.17 | 1.06× | 0.50 | $19.62 | $20,930 | 0.58× |
| Coordinated slowdown | 15% | 0.82× | $19.18 | $17.84 | $17.34–$18.34 | 0.90× | 0.50 | $16.50 | $18,087 | 0.50× |
| **Probability-weighted** | | | | **$23.15** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.69
- **Downside (worst scenario − price):** $-7.61
- **Expected value vs current** (weighted FV − price): $-2.30 (-9.0%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

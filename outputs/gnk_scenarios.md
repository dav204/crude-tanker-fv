# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $26.77
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.48 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.66 (-11.6% vs price)
- **Breakeven TCE (scenario-invariant):** $39,889/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $30.21 | $29.71 | $29.10–$30.32 | 1.76× | 0.70 | $28.54 | $35,902 | 0.90× |
| Moderate growth (base) | 40% | 0.99× | $25.11 | $24.29 | $23.68–$24.90 | 1.32× | 0.60 | $23.06 | $26,642 | 0.67× |
| China property drag | 25% | 0.89× | $22.04 | $21.02 | $20.40–$21.64 | 1.06× | 0.50 | $20.00 | $20,882 | 0.52× |
| Coordinated slowdown | 15% | 0.82× | $19.71 | $18.29 | $17.78–$18.79 | 0.90× | 0.50 | $16.86 | $18,038 | 0.45× |
| **Probability-weighted** | | | | **$23.66** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+2.94
- **Downside (worst scenario − price):** $-8.48
- **Expected value vs current** (weighted FV − price): $-3.11 (-11.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

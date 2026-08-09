# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.33
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.38 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $22.89 (-9.6% vs price)
- **Breakeven TCE (scenario-invariant):** $30,423/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $29.20 | $28.84 | $28.21–$29.47 | 1.77× | 0.70 | $28.00 | $36,270 | 1.19× |
| Moderate growth (base) | 40% | 0.96× | $24.21 | $23.52 | $22.89–$24.15 | 1.32× | 0.60 | $22.48 | $26,893 | 0.88× |
| China property drag | 25% | 0.87× | $21.20 | $20.28 | $19.65–$20.92 | 1.06× | 0.50 | $19.37 | $21,015 | 0.69× |
| Coordinated slowdown | 15% | 0.80× | $18.94 | $17.60 | $17.08–$18.11 | 0.90× | 0.50 | $16.25 | $18,175 | 0.60× |
| **Probability-weighted** | | | | **$22.89** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.51
- **Downside (worst scenario − price):** $-7.73
- **Expected value vs current** (weighted FV − price): $-2.44 (-9.6%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

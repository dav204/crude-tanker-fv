# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.33
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $22.67 (-10.5% vs price)
- **Breakeven TCE (scenario-invariant):** $31,845/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.12× | $28.92 | $28.59 | $27.96–$29.22 | 1.77× | 0.70 | $27.83 | $36,387 | 1.14× |
| Moderate growth (base) | 40% | 0.96× | $23.96 | $23.31 | $22.68–$23.93 | 1.32× | 0.60 | $22.32 | $26,972 | 0.85× |
| China property drag | 25% | 0.87× | $20.96 | $20.08 | $19.45–$20.72 | 1.06× | 0.50 | $19.21 | $21,058 | 0.66× |
| Coordinated slowdown | 15% | 0.80× | $18.72 | $17.42 | $16.90–$17.93 | 0.90× | 0.50 | $16.11 | $18,219 | 0.57× |
| **Probability-weighted** | | | | **$22.67** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+3.26
- **Downside (worst scenario − price):** $-7.91
- **Expected value vs current** (weighted FV − price): $-2.66 (-10.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

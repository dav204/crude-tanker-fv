# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.00
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.50 (-20.4% vs price)
- **Breakeven TCE (scenario-invariant):** $41,274/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $26.99 | $26.88 | $26.25–$27.50 | 1.77× | 0.70 | $26.62 | $36,271 | 0.88× |
| Moderate growth (base) | 40% | 0.91× | $22.55 | $22.09 | $21.46–$22.72 | 1.32× | 0.60 | $21.39 | $26,893 | 0.65× |
| China property drag | 25% | 0.83× | $19.87 | $19.16 | $18.53–$19.79 | 1.06× | 0.50 | $18.45 | $21,016 | 0.51× |
| Coordinated slowdown | 15% | 0.77× | $17.86 | $16.69 | $16.18–$17.20 | 0.90× | 0.50 | $15.51 | $18,175 | 0.44× |
| **Probability-weighted** | | | | **$21.50** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.12
- **Downside (worst scenario − price):** $-10.31
- **Expected value vs current** (weighted FV − price): $-5.50 (-20.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

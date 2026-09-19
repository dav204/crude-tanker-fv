# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.96
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.14 (-24.4% vs price)
- **Breakeven TCE (scenario-invariant):** $55,727/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.03× | $26.41 | $26.36 | $25.73–$26.99 | 1.77× | 0.70 | $26.26 | $36,271 | 0.65× |
| Moderate growth (base) | 40% | 0.90× | $22.12 | $21.71 | $21.08–$22.34 | 1.32× | 0.60 | $21.11 | $26,893 | 0.48× |
| China property drag | 25% | 0.82× | $19.52 | $18.87 | $18.23–$19.50 | 1.06× | 0.50 | $18.21 | $21,016 | 0.38× |
| Coordinated slowdown | 15% | 0.76× | $17.58 | $16.45 | $15.94–$16.96 | 0.90× | 0.50 | $15.32 | $18,175 | 0.33× |
| **Probability-weighted** | | | | **$21.14** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.60
- **Downside (worst scenario − price):** $-11.51
- **Expected value vs current** (weighted FV − price): $-6.82 (-24.4%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.96
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.05 (-24.7% vs price)
- **Breakeven TCE (scenario-invariant):** $55,689/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.03× | $26.26 | $26.23 | $25.60–$26.86 | 1.77× | 0.70 | $26.17 | $36,271 | 0.65× |
| Moderate growth (base) | 40% | 0.90× | $22.01 | $21.62 | $20.99–$22.25 | 1.32× | 0.60 | $21.03 | $26,893 | 0.48× |
| China property drag | 25% | 0.82× | $19.44 | $18.79 | $18.16–$19.43 | 1.06× | 0.50 | $18.15 | $21,016 | 0.38× |
| Coordinated slowdown | 15% | 0.76× | $17.51 | $16.39 | $15.88–$16.90 | 0.90× | 0.50 | $15.27 | $18,175 | 0.33× |
| **Probability-weighted** | | | | **$21.05** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-1.73
- **Downside (worst scenario − price):** $-11.57
- **Expected value vs current** (weighted FV − price): $-6.91 (-24.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

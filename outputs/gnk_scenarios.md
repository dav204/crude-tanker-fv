# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $27.65
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.48 (-22.3% vs price)
- **Breakeven TCE (scenario-invariant):** $44,779/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $26.94 | $26.84 | $26.21–$27.47 | 1.77× | 0.70 | $26.59 | $36,271 | 0.81× |
| Moderate growth (base) | 40% | 0.91× | $22.52 | $22.06 | $21.43–$22.69 | 1.32× | 0.60 | $21.37 | $26,893 | 0.60× |
| China property drag | 25% | 0.83× | $19.84 | $19.14 | $18.50–$19.77 | 1.06× | 0.50 | $18.43 | $21,016 | 0.47× |
| Coordinated slowdown | 15% | 0.77× | $17.84 | $16.67 | $16.16–$17.18 | 0.90× | 0.50 | $15.49 | $18,175 | 0.41× |
| **Probability-weighted** | | | | **$21.48** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.81
- **Downside (worst scenario − price):** $-10.98
- **Expected value vs current** (weighted FV − price): $-6.17 (-22.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

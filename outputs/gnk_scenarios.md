# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.88
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.12 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.66 (-16.3% vs price)
- **Breakeven TCE (scenario-invariant):** $34,989/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.07× | $27.28 | $27.14 | $26.51–$27.77 | 1.77× | 0.70 | $26.81 | $36,387 | 1.04× |
| Moderate growth (base) | 40% | 0.93× | $22.74 | $22.25 | $21.62–$22.88 | 1.32× | 0.60 | $21.52 | $26,972 | 0.77× |
| China property drag | 25% | 0.84× | $19.98 | $19.26 | $18.63–$19.89 | 1.06× | 0.50 | $18.54 | $21,058 | 0.60× |
| Coordinated slowdown | 15% | 0.77× | $17.93 | $16.75 | $16.24–$17.26 | 0.90× | 0.50 | $15.56 | $18,219 | 0.52× |
| **Probability-weighted** | | | | **$21.66** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+1.26
- **Downside (worst scenario − price):** $-9.13
- **Expected value vs current** (weighted FV − price): $-4.22 (-16.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

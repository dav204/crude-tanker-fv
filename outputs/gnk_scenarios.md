# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.80
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $26.24 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.73 (+8.1% vs price)
- **Breakeven TCE (scenario-invariant):** $17,309/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $32.93 | $32.91 | $32.29–$33.52 | 1.77× | 0.70 | $32.86 | $36,454 | 2.11× |
| Moderate growth (base) | 40% | 1.03× | $27.21 | $26.54 | $25.93–$27.15 | 1.32× | 0.60 | $25.54 | $27,018 | 1.56× |
| China property drag | 25% | 0.92× | $23.74 | $22.44 | $21.81–$23.06 | 1.06× | 0.50 | $21.13 | $21,082 | 1.22× |
| Coordinated slowdown | 15% | 0.84× | $21.17 | $19.50 | $19.00–$20.00 | 0.90× | 0.50 | $17.83 | $18,244 | 1.05× |
| **Probability-weighted** | | | | **$25.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.10
- **Downside (worst scenario − price):** $-4.31
- **Expected value vs current** (weighted FV − price): $+1.93 (+8.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

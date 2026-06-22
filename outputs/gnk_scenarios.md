# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.68
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $26.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.41 (+7.3% vs price)
- **Breakeven TCE (scenario-invariant):** $16,540/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $32.96 | $32.13 | $31.52–$32.74 | 1.77× | 0.70 | $30.20 | $36,441 | 2.20× |
| Moderate growth (base) | 40% | 1.03× | $27.23 | $26.11 | $25.49–$26.72 | 1.32× | 0.60 | $24.42 | $27,010 | 1.63× |
| China property drag | 25% | 0.92× | $23.76 | $22.46 | $21.84–$23.08 | 1.06× | 0.50 | $21.15 | $21,078 | 1.27× |
| Coordinated slowdown | 15% | 0.84× | $21.19 | $19.52 | $19.02–$20.02 | 0.90× | 0.50 | $17.85 | $18,239 | 1.10× |
| **Probability-weighted** | | | | **$25.41** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.45
- **Downside (worst scenario − price):** $-4.16
- **Expected value vs current** (weighted FV − price): $+1.73 (+7.3%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $24.00
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $26.16 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.65 (+6.9% vs price)
- **Breakeven TCE (scenario-invariant):** $18,726/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $32.83 | $32.82 | $32.20–$33.43 | 1.77× | 0.70 | $32.79 | $36,519 | 1.95× |
| Moderate growth (base) | 40% | 1.03× | $27.12 | $26.46 | $25.85–$27.08 | 1.32× | 0.60 | $25.48 | $27,062 | 1.45× |
| China property drag | 25% | 0.92× | $23.65 | $22.36 | $21.74–$22.99 | 1.06× | 0.50 | $21.07 | $21,106 | 1.13× |
| Coordinated slowdown | 15% | 0.84× | $21.09 | $19.43 | $18.93–$19.93 | 0.90× | 0.50 | $17.78 | $18,268 | 0.98× |
| **Probability-weighted** | | | | **$25.65** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.82
- **Downside (worst scenario − price):** $-4.57
- **Expected value vs current** (weighted FV − price): $+1.65 (+6.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

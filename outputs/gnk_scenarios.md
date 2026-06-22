# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $23.68
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $26.27 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $25.76 (+8.8% vs price)
- **Breakeven TCE (scenario-invariant):** $16,540/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.21× | $32.96 | $32.94 | $32.32–$33.55 | 1.77× | 0.70 | $32.88 | $36,441 | 2.20× |
| Moderate growth (base) | 40% | 1.03× | $27.23 | $26.57 | $25.95–$27.18 | 1.32× | 0.60 | $25.56 | $27,010 | 1.63× |
| China property drag | 25% | 0.92× | $23.76 | $22.46 | $21.84–$23.08 | 1.06× | 0.50 | $21.15 | $21,078 | 1.27× |
| Coordinated slowdown | 15% | 0.84× | $21.19 | $19.52 | $19.02–$20.02 | 0.90× | 0.50 | $17.85 | $18,239 | 1.10× |
| **Probability-weighted** | | | | **$25.76** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.26
- **Downside (worst scenario − price):** $-4.16
- **Expected value vs current** (weighted FV − price): $+2.08 (+8.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

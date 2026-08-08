# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.33
- **Analyst target:** $24.80
- **NAV / share (reference, unflexed):** $25.26 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $23.42 (-7.5% vs price)
- **Breakeven TCE (scenario-invariant):** $32,091/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.15× | $30.09 | $29.63 | $29.00–$30.25 | 1.77× | 0.70 | $28.54 | $36,250 | 1.13× |
| Moderate growth (base) | 40% | 0.99× | $24.86 | $24.08 | $23.45–$24.71 | 1.32× | 0.60 | $22.90 | $26,879 | 0.84× |
| China property drag | 25% | 0.89× | $21.71 | $20.71 | $20.07–$21.34 | 1.06× | 0.50 | $19.71 | $21,008 | 0.65× |
| Coordinated slowdown | 15% | 0.82× | $19.34 | $17.93 | $17.42–$18.44 | 0.90× | 0.50 | $16.52 | $18,168 | 0.57× |
| **Probability-weighted** | | | | **$23.42** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+4.30
- **Downside (worst scenario − price):** $-7.40
- **Expected value vs current** (weighted FV − price): $-1.91 (-7.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

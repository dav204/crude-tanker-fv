# MPCC — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $2.54
- **Analyst target:** $2.63
- **NAV / share (reference, unflexed):** $2.02 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $1.85 (-27.3% vs price)
- **Breakeven TCE (scenario-invariant):** $299,648/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.02× | $2.09 | $2.05 | $2.03–$2.08 | 1.20× | 0.60 | $2.01 | $36,801 | 0.12× |
| Gradual normalization (base) | 40% | 0.97× | $1.93 | $1.90 | $1.88–$1.92 | 1.16× | 0.50 | $1.87 | $35,588 | 0.12× |
| Normalization + orderbook overhang | 20% | 0.93× | $1.79 | $1.76 | $1.74–$1.78 | 1.13× | 0.50 | $1.73 | $34,407 | 0.11× |
| Demand recession | 15% | 0.85× | $1.49 | $1.48 | $1.46–$1.49 | 0.99× | 0.50 | $1.46 | $30,187 | 0.10× |
| **Probability-weighted** | | | | **$1.85** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-0.49
- **Downside (worst scenario − price):** $-1.06
- **Expected value vs current** (weighted FV − price): $-0.69 (-27.3%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

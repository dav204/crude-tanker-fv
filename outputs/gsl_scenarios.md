# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $37.60
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $38.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $40.59 (+8.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.03× | $39.95 | $44.45 | $43.74–$45.16 | 1.44× | 0.60 | $51.21 | $56,335 | 51801957064189316926900535296.00× |
| Gradual normalization (base) | 40% | 0.97× | $36.97 | $41.26 | $40.66–$41.86 | 1.38× | 0.60 | $47.70 | $53,862 | 49528139210122705962977460224.00× |
| Normalization + orderbook overhang | 20% | 0.90× | $33.60 | $37.75 | $37.26–$38.24 | 1.30× | 0.60 | $43.98 | $50,777 | 46691076855841564974064336896.00× |
| Demand recession | 15% | 0.87× | $32.48 | $36.18 | $35.79–$36.57 | 1.21× | 0.60 | $41.74 | $47,465 | 43645305107350125429825470464.00× |
| **Probability-weighted** | | | | **$40.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.85
- **Downside (worst scenario − price):** $-1.42
- **Expected value vs current** (weighted FV − price): $+2.99 (+8.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

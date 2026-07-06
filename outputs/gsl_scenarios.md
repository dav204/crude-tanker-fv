# GSL — Scenario Fair Value (Container Set A (disruption-led))

- **Current price:** $38.11
- **Analyst target:** $52.04
- **NAV / share (reference, unflexed):** $38.59 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $40.54 (+6.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Disruption persists | 25% | 1.03× | $39.87 | $44.39 | $43.68–$45.10 | 1.44× | 0.60 | $51.16 | $56,335 | n/a |
| Gradual normalization (base) | 40% | 0.97× | $36.90 | $41.20 | $40.60–$41.80 | 1.38× | 0.60 | $47.66 | $53,862 | n/a |
| Normalization + orderbook overhang | 20% | 0.90× | $33.54 | $37.70 | $37.21–$38.19 | 1.30× | 0.60 | $43.95 | $50,777 | n/a |
| Demand recession | 15% | 0.87× | $32.42 | $36.14 | $35.75–$36.53 | 1.21× | 0.60 | $41.71 | $47,465 | n/a |
| **Probability-weighted** | | | | **$40.54** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+6.28
- **Downside (worst scenario − price):** $-1.97
- **Expected value vs current** (weighted FV − price): $+2.43 (+6.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

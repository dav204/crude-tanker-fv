# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $64.33
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.51 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $67.61 (+5.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — **price justified by NAV alone** (blended FV clears the price even at zero rates; the entire earnings leg is optionality on top of asset coverage).
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 10% | 1.25× | $89.00 | $94.77 | $92.14–$97.79 | 4.23× | 0.70 | $108.24 | $134,591 | n/a |
| Pre-MoU baseline | 20% | 0.80× | $68.43 | $67.54 | $66.43–$68.70 | 1.66× | 0.70 | $65.45 | $52,704 | n/a |
| MoU base case | 45% | 0.75× | $66.19 | $64.57 | $63.24–$65.89 | 1.41× | 0.60 | $62.14 | $44,921 | n/a |
| MoU bear | 25% | 0.72× | $64.58 | $62.29 | $61.18–$63.40 | 1.20× | 0.60 | $58.86 | $38,261 | n/a |
| **Probability-weighted** | | | | **$67.61** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven is n/a — the price clears at any rate, so every scenario's rates trivially justify it._

## Decision signals

- **Upside (best scenario − price):** $+30.44
- **Downside (worst scenario − price):** $-2.04
- **Expected value vs current** (weighted FV − price): $+3.28 (+5.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

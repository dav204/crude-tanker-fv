# TNK — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $67.99
- **Analyst target:** $75.00
- **NAV / share (reference, unflexed):** $77.51 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $79.59 (+17.1% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $89.00 | $94.77 | $92.14–$97.79 | 4.23× | 0.70 | $108.24 | $134,591 | 80858046044821863068032040960.00× |
| Pre-MoU baseline | 45% | 1.04× | $79.41 | $81.78 | $80.08–$83.66 | 2.82× | 0.70 | $87.31 | $89,284 | 53639048382680915531947573248.00× |
| MoU base case | 18% | 0.75× | $66.19 | $64.57 | $63.24–$65.89 | 1.41× | 0.60 | $62.14 | $44,921 | 26986928893864612635414102016.00× |
| MoU bear | 12% | 0.72× | $64.58 | $62.29 | $61.18–$63.40 | 1.20× | 0.60 | $58.86 | $38,261 | 22986171401949855936409501696.00× |
| **Probability-weighted** | | | | **$79.59** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+26.78
- **Downside (worst scenario − price):** $-5.70
- **Expected value vs current** (weighted FV − price): $+11.60 (+17.1%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

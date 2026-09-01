# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $25.88
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.45 (-17.1% vs price)
- **Breakeven TCE (scenario-invariant):** $34,013/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.05× | $26.90 | $26.80 | $26.17–$27.43 | 1.77× | 0.70 | $26.56 | $36,271 | 1.07× |
| Moderate growth (base) | 40% | 0.91× | $22.48 | $22.03 | $21.40–$22.66 | 1.32× | 0.60 | $21.35 | $26,893 | 0.79× |
| China property drag | 25% | 0.83× | $19.82 | $19.12 | $18.48–$19.75 | 1.06× | 0.50 | $18.41 | $21,016 | 0.62× |
| Coordinated slowdown | 15% | 0.77× | $17.82 | $16.65 | $16.14–$17.16 | 0.90× | 0.50 | $15.48 | $18,175 | 0.53× |
| **Probability-weighted** | | | | **$21.45** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.92
- **Downside (worst scenario − price):** $-9.23
- **Expected value vs current** (weighted FV − price): $-4.43 (-17.1%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

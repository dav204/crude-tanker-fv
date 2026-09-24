# GNK — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $26.43
- **Analyst target:** $27.20
- **NAV / share (reference, unflexed):** $25.37 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.20 (-19.8% vs price)
- **Breakeven TCE (scenario-invariant):** $42,937/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.04× | $26.51 | $26.45 | $25.82–$27.08 | 1.77× | 0.70 | $26.32 | $36,271 | 0.84× |
| Moderate growth (base) | 40% | 0.90× | $22.19 | $21.78 | $21.15–$22.41 | 1.32× | 0.60 | $21.16 | $26,893 | 0.63× |
| China property drag | 25% | 0.82× | $19.58 | $18.92 | $18.28–$19.55 | 1.06× | 0.50 | $18.25 | $21,016 | 0.49× |
| Coordinated slowdown | 15% | 0.76× | $17.63 | $16.49 | $15.98–$17.00 | 0.90× | 0.50 | $15.35 | $18,175 | 0.42× |
| **Probability-weighted** | | | | **$21.20** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.02
- **Downside (worst scenario − price):** $-9.94
- **Expected value vs current** (weighted FV − price): $-5.23 (-19.8%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

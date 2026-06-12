# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $12.79
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $17.74 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $17.68 (+38.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $25.32 | $24.52 | $24.15–$24.95 | 7.04× | 0.70 | $22.66 | $253,538 | 105081806100573053007544975360.00× |
| Pre-MoU baseline | 45% | 1.11× | $21.05 | $19.94 | $19.71–$20.20 | 4.15× | 0.70 | $17.36 | $148,217 | 61430252296970960952774098944.00× |
| MoU base case | 18% | 0.75× | $10.18 | $9.23 | $9.11–$9.35 | 1.90× | 0.70 | $7.02 | $67,650 | 28038539058563514832124903424.00× |
| MoU bear | 12% | 0.71× | $8.81 | $7.59 | $7.46–$7.72 | 1.50× | 0.60 | $5.76 | $53,056 | 21989511265210968837923536896.00× |
| **Probability-weighted** | | | | **$17.68** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+11.73
- **Downside (worst scenario − price):** $-5.20
- **Expected value vs current** (weighted FV − price): $+4.89 (+38.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

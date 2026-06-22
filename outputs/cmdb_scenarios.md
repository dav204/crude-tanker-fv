# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $16.90
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.49 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $21.13 (+25.0% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $37.59 | $25.32 | $24.81–$25.82 | 1.76× | 0.70 | $22.99 | $30,002 | 71155750367676698812112437248.00× |
| Moderate growth (base) | 40% | 1.02× | $32.96 | $21.48 | $20.96–$22.00 | 1.33× | 0.60 | $19.09 | $22,583 | 53559783992108033772777111552.00× |
| China property drag | 25% | 0.94× | $30.68 | $19.54 | $18.96–$20.12 | 1.13× | 0.50 | $17.60 | $18,664 | 44264740414943849342241341440.00× |
| Coordinated slowdown | 15% | 0.85× | $28.16 | $17.25 | $16.80–$17.70 | 0.95× | 0.50 | $14.79 | $15,802 | 37476784044445940478111645696.00× |
| **Probability-weighted** | | | | **$21.13** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+8.42
- **Downside (worst scenario − price):** $+0.35
- **Expected value vs current** (weighted FV − price): $+4.23 (+25.0%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

# SB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $6.36
- **Analyst target:** $7.10
- **NAV / share (reference, unflexed):** $10.61 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.10 (+58.8% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.16× | $13.40 | $12.99 | $12.82–$13.16 | 1.96× | 0.70 | $12.03 | $26,770 | 67294320169601436402013175808.00× |
| Moderate growth (base) | 40% | 0.99× | $10.49 | $10.20 | $10.04–$10.37 | 1.49× | 0.60 | $9.77 | $20,258 | 50924041097455624040002617344.00× |
| China property drag | 25% | 0.93× | $9.45 | $9.12 | $8.98–$9.26 | 1.29× | 0.60 | $8.62 | $17,246 | 43351890134188060484692869120.00× |
| Coordinated slowdown | 15% | 0.83× | $7.75 | $7.60 | $7.46–$7.74 | 1.08× | 0.50 | $7.45 | $14,496 | 36439075191497998426471137280.00× |
| **Probability-weighted** | | | | **$10.10** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+6.63
- **Downside (worst scenario − price):** $+1.24
- **Expected value vs current** (weighted FV − price): $+3.74 (+58.8%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

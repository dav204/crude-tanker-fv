# CMDB — Scenario Fair Value (Bulk Set A (China-driven))

- **Current price:** $17.25
- **Analyst target:** $27.98
- **NAV / share (reference, unflexed):** $32.23 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $28.32 (+64.2% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| China acceleration | 20% | 1.18× | $37.30 | $33.91 | $33.91–$33.91 | 1.76× | 0.70 | $26.00 | $30,065 | 71203225994892651934099963904.00× |
| Moderate growth (base) | 40% | 1.02× | $32.71 | $28.77 | $28.77–$28.77 | 1.33× | 0.60 | $22.86 | $22,627 | 53587455522980071137624457216.00× |
| China property drag | 25% | 0.94× | $30.44 | $25.87 | $25.87–$25.87 | 1.13× | 0.50 | $21.30 | $18,689 | 44260785426764470078375198720.00× |
| Coordinated slowdown | 15% | 0.85× | $27.94 | $23.76 | $23.76–$23.76 | 0.95× | 0.50 | $19.59 | $15,826 | 37481059250700178535913357312.00× |
| **Probability-weighted** | | | | **$28.32** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+16.66
- **Downside (worst scenario − price):** $+6.51
- **Expected value vs current** (weighted FV − price): $+11.07 (+64.2%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

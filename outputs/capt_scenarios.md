# CAPT — Scenario Fair Value (three-phase MoU framework)

- **Current price:** $13.24
- **Analyst target:** $18.90
- **NAV / share (reference, unflexed):** $15.05 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $16.20 (+22.4% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $21.95 | $22.69 | $22.32–$23.11 | 7.04× | 0.70 | $24.42 | $249,089 | 104777747274634899083715674112.00× |
| Pre-MoU baseline | 45% | 1.11× | $18.05 | $18.31 | $18.08–$18.57 | 4.15× | 0.70 | $18.91 | $145,948 | 61392229393490692051006652416.00× |
| MoU base case | 18% | 0.75× | $8.17 | $8.14 | $8.02–$8.26 | 1.90× | 0.70 | $8.08 | $66,704 | 28058422362914500415936528384.00× |
| MoU bear | 12% | 0.71× | $6.92 | $6.86 | $6.73–$6.98 | 1.50× | 0.60 | $6.76 | $52,346 | 22019189455093547262082547712.00× |
| **Probability-weighted** | | | | **$16.20** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+9.45
- **Downside (worst scenario − price):** $-6.38
- **Expected value vs current** (weighted FV − price): $+2.96 (+22.4%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

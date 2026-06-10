# TEN [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY 3-SLEEVE = crude (71.3%) + product (16.6%) + lng (12.1%) AGGREGATED (METHODOLOGY §11.6). Off-curve shuttle-contracted-book sleeve sits at the corporate level (`shuttle_contracted_book`) and flows through NAV uniformly across scenarios. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $44.00
- **Analyst target:** $51.50
- **NAV / share (reference, unflexed):** $80.78 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $57.61 (+30.9% vs price)
- **Breakeven TCE (scenario-invariant):** $0/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** BUY (undervalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 25% | 1.25× | $111.20 | $74.99 | $74.70–$75.33 | 4.30× | 0.70 | $68.35 | $147,876 | 84290095368744422308564697088.00× |
| Pre-MoU baseline | 45% | 1.04× | $90.98 | $61.65 | $61.47–$61.85 | 2.79× | 0.70 | $56.61 | $91,637 | 52233579222435689212011347968.00× |
| MoU base case | 18% | 0.75× | $55.91 | $38.67 | $38.54–$38.80 | 1.40× | 0.60 | $37.51 | $45,719 | 26060029499496638979252420608.00× |
| MoU bear | 12% | 0.71× | $49.77 | $34.68 | $34.55–$34.81 | 1.18× | 0.50 | $34.26 | $37,765 | 21526402725020195002874068992.00× |
| **Probability-weighted** | | | | **$57.61** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+30.99
- **Downside (worst scenario − price):** $-9.32
- **Expected value vs current** (weighted FV − price): $+13.61 (+30.9%)
- **Position:** BUY (undervalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

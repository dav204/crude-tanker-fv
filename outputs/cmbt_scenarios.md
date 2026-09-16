# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.1%) + containerships (3.1%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $19.33
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $16.46 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $13.58 (-29.7% vs price)
- **Breakeven TCE (scenario-invariant):** $203,487/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $19.29 | $19.71 | $19.01–$20.45 | 6.47× | 0.70 | $20.66 | $83,364 | 0.41× |
| Pre-MoU baseline | 59% | 0.93× | $14.08 | $13.27 | $12.78–$13.77 | 2.27× | 0.70 | $11.96 | $41,550 | 0.20× |
| MoU base case | 0% | 0.85× | $11.51 | $10.44 | $9.98–$10.90 | 1.87× | 0.70 | $9.15 | $32,817 | 0.16× |
| MoU bear | 13% | 0.79× | $9.90 | $8.56 | $8.18–$8.94 | 1.53× | 0.70 | $6.94 | $27,996 | 0.14× |
| **Probability-weighted** | | | | **$13.58** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $+0.38
- **Downside (worst scenario − price):** $-10.77
- **Expected value vs current** (weighted FV − price): $-5.75 (-29.7%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

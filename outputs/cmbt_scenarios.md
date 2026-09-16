# CMBT [WHOLE-CO] — Scenario Fair Value (three-phase MoU framework)

> **Valuation basis:** WHOLE-COMPANY MULTI-SLEEVE = crude (23.8%) + dry_bulk (73.1%) + containerships (3.1%) AGGREGATED (METHODOLOGY §11.9). Off-curve segments (chemical / offshore / FSO / held-for-sale / newbuild book) sit at the corporate level and flow through NAV uniformly across sleeves. Compared to the WHOLE-COMPANY tape price.

- **Current price:** $19.33
- **Analyst target:** $16.59
- **NAV / share (reference, unflexed):** $13.36 _(flexes per scenario via vessel-value elasticity — see table)_
- **Probability-weighted fair value:** $10.73 (-44.5% vs price)
- **Breakeven TCE (scenario-invariant):** $295,440/day — the value-weighted blended rate (fleet-mix-adjusted) that justifies the current price. The scenario sets the *probability* of clearing it, not the level.
- **Position (tool view):** TRIM/SHORT (overvalued)

## Per-scenario fair value

| Scenario | Weight | Vessel× | NAV/sh | FV (base) | FV [low–high] | Cycle | w_nav | Strip NPV | Assumed TCE (12M) | Assumed / Breakeven |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Escalation | 28% | 1.25× | $16.19 | $16.80 | $16.10–$17.54 | 6.47× | 0.70 | $18.21 | $83,364 | 0.28× |
| Pre-MoU baseline | 59% | 0.93× | $10.98 | $10.41 | $9.92–$10.91 | 2.27× | 0.70 | $9.51 | $41,550 | 0.14× |
| MoU base case | 0% | 0.85× | $8.40 | $7.63 | $7.17–$8.09 | 1.87× | 0.70 | $6.70 | $32,817 | 0.11× |
| MoU bear | 13% | 0.79× | $6.79 | $5.75 | $5.37–$6.13 | 1.53× | 0.70 | $4.49 | $27,996 | 0.09× |
| **Probability-weighted** | | | | **$10.73** | | | | | | |

_Assumed TCE = the scenario's value-weighted 12-month forward (the model's rate assumption, NOT a breakeven). Assumed/Breakeven < 1 ⇒ that scenario's rates fall short of justifying the price; > 1 ⇒ they clear it._

## Decision signals

- **Upside (best scenario − price):** $-2.53
- **Downside (worst scenario − price):** $-13.58
- **Expected value vs current** (weighted FV − price): $-8.60 (-44.5%)
- **Position:** TRIM/SHORT (overvalued)

_Convention: FV above price = undervalued = BUY; FV below = overvalued = TRIM/SHORT. (This is the inverse of the literal buy/trim labels in scenario_inputs.yaml output_requirements.highlight — flagged for confirmation.)_

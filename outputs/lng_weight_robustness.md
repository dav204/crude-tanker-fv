# LNG Weight Robustness Diagnostic — Set B vs Set B-revised

**Purpose** (METHODOLOGY §13): the recurring per-LNG-name weight-
sensitivity diagnostic. Identifies which calls are weight-robust
(small EV% spread across plausible weight sets) vs weight-driven
(call would flip under reasonable alternative weights). Refresh at
the start of each quarterly cycle alongside the refresh checklist.

**Current production lock:** Set B-revised (v3, 2026-06-01).
Comparison reference: Set B (v2, prior lock, same day).

**Lock driver:** Ras Laffan Trains 4 & 6 (12.8 mtpa / ~17% of Qatar LNG) offline through end-summer 2026 at earliest; restart risk from subsurface complications. Partially offsets Cheniere Stage 3 ramp through H2 2026. Empirical pricing: spot $67.5k (+391% YoY), TFDE $98.5k — tight-market levels, not glut levels.

**Weights:**

| Scenario | Set B (v2, prior) | **Set B-revised (v3, current)** | Δ |
|---|--:|--:|--:|
| tight_resurgence | 0.10 | 0.15 | +0.05 |
| moderate_tightening | 0.15 | 0.25 | +0.10 |
| glut_base | 0.55 | 0.45 | -0.10 |
| glut_intensifies | 0.20 | 0.15 | -0.05 |
| structural_reset | 0.00 | 0.00 | +0.00 |

## FLNG — at price $30.23, target $25.00

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $41.93 | $39.76 | $34.70 | $147,500 |
| moderate_tightening | 1.13× | $35.59 | $32.82 | $30.04 | $78,750 |
| glut_base | 0.96× | $26.34 | $24.49 | $23.25 | $58,000 |
| glut_intensifies | 0.84× | $19.84 | $19.03 | $18.48 | $43,250 |
| structural_reset | 0.74× | $14.55 | $14.58 | $14.60 | $44,250 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $26.17 | $28.04 | $+1.87 (+7.1%) |
| EV% | -13.4% | -7.2% | +6.2pp |
| Position | TRIM/SHORT | TRIM/SHORT | unchanged |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $28.72, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $31.74, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

**Set B → Set B-revised is NOT sufficient to flip FLNG to HOLD.** Extrapolating along the same direction (more aggressive constructive reweighting):

- alpha for HOLD = **1.36** (must extrapolate 36% beyond Set B-revised)
- alpha for BUY = **2.98**

**Extrapolated weights that would flip FLNG to HOLD (alpha = 1.36):**

| Scenario | Weight at HOLD threshold | vs Set B | vs Set B-revised |
|---|--:|--:|--:|
| tight_resurgence | 0.168 | +0.068 | +0.018 |
| moderate_tightening | 0.286 | +0.136 | +0.036 |
| glut_base | 0.414 | -0.136 | -0.036 |
| glut_intensifies | 0.132 | -0.068 | -0.018 |
| structural_reset | 0.000 | +0.000 | +0.000 |

**Constructive total (tight + moderate + glut_base) at the flip point: 87%**
  (vs Set B: 80%; Set B-revised: 85%). Whether this is defensible depends on whether the Ras Laffan + winter view warrants a constructive environment lasting deep into 2027 with only 13% on the bear cases.

---

## CCEC — at price $23.18, target $25.17

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $52.98 | $48.52 | $38.10 | $137,383 |
| moderate_tightening | 1.13× | $41.36 | $35.36 | $29.36 | $74,327 |
| glut_base | 0.96× | $24.44 | $19.76 | $16.64 | $54,921 |
| glut_intensifies | 0.84× | $12.48 | $9.59 | $7.66 | $41,075 |
| structural_reset | 0.74× | $2.45 | $1.05 | $0.12 | $41,611 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $22.94 | $26.45 | $+3.51 (+15.3%) |
| EV% | -1.0% | +14.1% | +15.1pp |
| Position | HOLD | BUY | **FLIP** |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $22.02, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $24.34, EV ≥ +5%): alpha ≥ **0.40**

---

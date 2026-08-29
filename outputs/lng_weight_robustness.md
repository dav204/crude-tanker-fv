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

## FLNG — at price $31.93, target $25.00

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $40.48 | $38.00 | $32.22 | $147,500 |
| moderate_tightening | 1.13× | $34.24 | $32.41 | $30.59 | $78,750 |
| glut_base | 0.96× | $25.14 | $25.13 | $25.12 | $58,000 |
| glut_intensifies | 0.84× | $18.74 | $19.34 | $19.73 | $43,250 |
| structural_reset | 0.72× | $12.60 | $15.18 | $16.28 | $40,500 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $26.35 | $28.01 | $+1.66 (+6.3%) |
| EV% | -17.5% | -12.3% | +5.2pp |
| Position | TRIM/SHORT | TRIM/SHORT | unchanged |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $30.33, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $33.53, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

**Set B → Set B-revised is NOT sufficient to flip FLNG to HOLD.** Extrapolating along the same direction (more aggressive constructive reweighting):

- alpha for HOLD = **2.40** (must extrapolate 140% beyond Set B-revised)
- alpha for BUY = **4.32**

**Extrapolated weights that would flip FLNG to HOLD (alpha = 2.40):**

| Scenario | Weight at HOLD threshold | vs Set B | vs Set B-revised |
|---|--:|--:|--:|
| tight_resurgence | 0.220 | +0.120 | +0.070 |
| moderate_tightening | 0.390 | +0.240 | +0.140 |
| glut_base | 0.310 | -0.240 | -0.140 |
| glut_intensifies | 0.080 | -0.120 | -0.070 |
| structural_reset | 0.000 | +0.000 | +0.000 |

**Constructive total (tight + moderate + glut_base) at the flip point: 92%**
  (vs Set B: 80%; Set B-revised: 85%). Whether this is defensible depends on whether the Ras Laffan + winter view warrants a constructive environment lasting deep into 2027 with only 8% on the bear cases.

---

## CCEC — at price $22.62, target $25.17

**Per-scenario FV (identical under both weight sets — only weights change, scenario forwards unchanged):**

| Scenario | Vessel× | NAV/sh | FV (base) | Strip NPV | Assumed 12M TCE |
|---|--:|--:|--:|--:|--:|
| tight_resurgence | 1.25× | $50.28 | $47.20 | $40.03 | $136,327 |
| moderate_tightening | 1.13× | $38.81 | $39.08 | $39.35 | $73,865 |
| glut_base | 0.96× | $22.11 | $26.78 | $29.89 | $54,599 |
| glut_intensifies | 0.84× | $10.31 | $16.27 | $20.24 | $40,848 |
| structural_reset | 0.72× | $-1.37 | $6.00 | $10.90 | $37,815 |

**Headline:**

| Metric | Set B | Set B-revised | Δ |
|---|--:|--:|--:|
| PW FV | $28.57 | $31.34 | $+2.78 (+9.7%) |
| EV% | +26.3% | +38.6% | +12.3pp |
| Position | BUY | BUY | unchanged |

**Threshold analysis** (alpha = 0: Set B; alpha = 1: Set B-revised; FV is linear in weights so the convex combination is exact):

- HOLD threshold (FV ≥ $21.49, EV ≥ -5%): _not reachable on the [Set B → Set B-revised] line_
- BUY threshold (FV ≥ $23.75, EV ≥ +5%): _not reachable on the [Set B → Set B-revised] line_

---

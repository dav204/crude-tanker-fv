# Container determinant ingest — 2026-07-06 (§11.8 event; trigger container_mb_refresh)

First MB monthly re-capture, closing the Apr-01 freeze. Source: **MB Container
Weekly 27** (assessments dated **2026-07-03**), harvested this session via the
Gmail step (`session:mb-batch` in the run ledger) — W27 superseded the W26
dry-run prep (decisions/container_ingest_prep_2026-07-03.md) in exactly one
cell: the 1,700-TEU 12M assessment ticked 29,000 → 30,000. The trigger fired
due 2026-07-04 and was worked 2 days late (the Saturday session didn't happen
— the flag held; the human was away). Re-armed monthly, next due 2026-08-07.

## What moved (all cited to W27 p.2 TC table + p.3 assessment tables)

| Determinant | Was (Apr-01 freeze) | Now (W27 Jul-3) | Δ |
|---|---:|---:|---:|
| Ctr-Feeder 12M TC / spot ref | 20,500 | **23,750** | **+15.9%** |
| Ctr-Intermediate 12M TC (A3) | 43,400 | **46,350** | +6.8% |
| Ctr-Large 12M TC | 62,500 | **63,000** | +0.8% |
| Feeder 10-yr value (MB 1,700) | $28.0M | **$29.0M** | +3.6% |
| All other 2nd-hand + NB assessments | — | unchanged | — |
| Ctr forward strips | Apr-01 starts | re-synthesized: W27 starts → SAME wire-up terminals (19,000/37,200/48,000), linear | — |

**A3 re-derivation (fork 1 of the prep, resolved):** TEU-weighted on the live
combined validator intermediate fleets — MPCC 44 vessels/151,246 TEU (IR fleet
page) + GSL 28/104,988 (Q1-2026 PR fleet table, SEC exhibit) = 72 vessels,
256,234 TEU; bucket shares 2,500: 11.5% / 2,700: 21.8% / 3,500: 25.3% /
4,250: 41.4% (5,470-5,500 boundary ships → 4,250 per §11.8.1). Cross-foot vs
the as-of manifests: 72 vs 72 count-weighted intermediate rows (MPCC 44/42,
GSL 28/30 — ±2 compositional differences between live pages and as-of
manifests; <1% A3 sensitivity). The prep's placeholder (44,550, uplift-ratio
method) UNDERSHOT — the fleets skew to the 4,250 bucket.

## Model impact (gate-annotated)

- **MPCC:** NAV $2.02 → $2.04 (+1.0%, matching the prep's +0.92% prediction);
  scenario EV −13.7% → **−18.1%** (−4.4pp) — the rate lift RICHENS the cycle
  position (feeder 0.98x → 1.14x) while ~99% 2026 coverage keeps the strip
  contracted, so the cycle-conditional terminal/blend mechanics dominate.
  TRIM/SHORT unchanged. Annotated in decisions/mpcc_log.md.
- **GSL:** stable (−0.1pp) — larger-class mix (+0.8% rate) and heavy backlog.
- **CAPT −2.2pp rode the same regen but is PRICE drift** (first regen since
  the drift-guard fix picked up the Jul-3 close) — separately annotated in
  decisions/capt_log.md per the isolate-commit discipline.
- Suite: green except the designed `-dirty` stamp guard (clears on the
  owner's commit + clean regen). Drift gate: **0 UNEXPLAINED, 2 explained.**
- METHODOLOGY §11.8.5 table revised (dated); cycle positions now
  1.14x / 1.38x / 1.54x.

## Residual forks / notes

1. **Strip re-synthesis shape:** staged = new start → SAME wire-up terminal
   (the anchored end is the documented convention). Alternative
   (shape-preserving scaling, lifts terminals above the FY21-25 anchors)
   rejected as un-anchored; revisit only with a §11.8.6.4 revision.
2. **ctr_large remains the softest-validated leg** (§11.8.5) — W27 quotes
   still WB-only above 5,400; the derived 10-yr (56.0) stands unchanged.
3. The cycle positions richened across the board — the §13.3 lens applies at
   the next weight review, not silently here.

**Owner action to close:** review this diff, commit, then
`./scripts/ratify_baseline.sh "container W27 ingest (MPCC) + Jul-3 price drift (CAPT)"`
and regenerate for the clean source_commit stamp.

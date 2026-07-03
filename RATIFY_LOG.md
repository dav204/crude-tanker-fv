# Ratify log — one row per drift-gate baseline re-anchor (WO1 Task 4, 2026-07-02)

Appended by `drift_gate --ratify`; read by the governance repo's weekly monitor to
learn the valuation surface re-based since its last run — the producer's page to
the consumer. The hash is HEAD at ratify time (the ratify commit lands one ahead).

| date | commit | cause |
|---|---|---|
| 2026-07-02T13:44:45Z | 6749362 | TRMD P0 reconciliation (clears the queue) — seeded from git history |
| 2026-07-02T16:45:57Z | aabbe5f | July-1 price-vintage recovery (audit F-1 follow-up; dNAV 0.0% all names, pure price drift; STNG flip annotated) — seeded |
| 2026-07-02T16:48:15Z | afc7270 | C-3 multi-sleeve aggregation fix — per-sleeve sector weights replace rank-1 index pairing; CMBT -3.6pp / TEN -3.2pp / INSW -1.5pp EV, dNAV 0.0% — seeded |
| 2026-07-02T22:30:00Z | d1544b4 | post-stand-down vintage (owner-approved, option (i)) — crude + leg recalibration + product v2-restore + LNG v3-restore + F-5 rates; six band flips annotated — seeded |
| 2026-07-02T23:40:00Z | 39ccfa6 | F-13 rendering fix — verdict/JSON fv re-based to the scenario-weighted FV; dNAV/dEV 0.0, printed-FV changes large — seeded |
| 2026-07-03T00:13:19Z | 3281827 | July-2 close price drift (isolated layer) — TNK and TRMD band-edge BUYs compress to HOLD; dNAV 0.0% — seeded |

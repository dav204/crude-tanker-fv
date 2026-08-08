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
| 2026-07-06T18:40:24Z | 031d65a | container W27 ingest (MPCC) + Jul-3 price drift (CAPT) |
| 2026-07-06T19:23:20Z | 6314357 | consensus-pair recapture (Pareto 3-Jul daily): 18 pairs rebased; 5 k_broker moves accepted (INSW/FRO/ECO/HAFN/TNK), SANITY OK |
| 2026-07-10T21:57:05Z | c530714 | WO3 Phase-4 LPG+BWLP added; Jul-10 price-vintage EV drift accepted (dNAV 0.0 all names); GSL BUY-HOLD + STNG HOLD-TRIM flips eyeballed + accepted by owner 2026-07-10 |
| 2026-07-13T17:30:52Z | 1f6f2f2 | Jul-12 war-tilt regen (owner-executed) + Jul-10-13 price vintage + 13-Jul dry-bulk FFA promotion; 4 flips eyeballed individually - BRUT void-tier, CAPT pre-approved 7/12, ASC shallow price-crossing, GNK tender-pinned; owner accept-all 2026-07-13 |
| 2026-07-14T16:41:26Z | 0aa4fba | 2343 onboarding + 2026-07-14 price vintage |
| 2026-07-15T14:35:08Z | 893002d | hormuz re-tilt RESTORE BOTH (owner ruling 2026-07-14 EVE) + same-evening price vintage |
| 2026-07-15T19:54:12Z | c6877ee | TEN reconciliation ruled: four §6 forks 'proceed as recommended' (NCI preferred_equity / Ulysses carrying-in-WC / SLB steel excluded / WC composite) — headline 88.76->87.35 in band, TEN the sole drifted row |
| 2026-07-18T19:46:16Z | d1403e0 | batch absorb, two causes (owner: 'batch baseline ratify' 2026-07-18): (1) the 7/17-close price vintage — EV-only x16, dNAV 0.0 every row; (2) the ratified 13-Jul spot-reproxy §3 applied at the Week-close audit — dry-bulk band-mech flips SBLK HOLD->BUY, CMDB HOLD->BUY, GNK TRIM/SHORT->HOLD, all price-inside-interval per D-M5 |
| 2026-07-18T20:15:50Z | 84232cc | post-promotion absorb (owner: 'Ratify' 2026-07-18): the 13-print marks-trail promotion — 5 movers annotated (NAT +2.1 NAV / DHT -2.2 / CMDB +2.5 / GNK +3.2 / SBLK +2.7), zero band flips |
| 2026-07-26T21:24:12Z | a46eda7 | week-close batch absorb 2026-07-26: 7/21+7/24-close price vintages EV-only (dNAV 0.0 every row; SB -1.5% = 7/18 marks-snapshot residual) + container W28/W29 promote (sub-display) + 7/24 FFA promote (sub-2pp); five flips eyeballed INDIVIDUALLY: SBLK BUY->HOLD price-at-FV (coherent w/ governance take-profit), GNK tender-pinned recross (outcome PR pending Mon 7/28), ASC pre-warned oscillation, GSL recross, 2343 rally crossing - all band-mech |
| 2026-07-31T18:04:54Z | b9aa18a | B' reweight executed at owner go 2026-07-31 (7/22 frozen conditional; mediation-check third-state ruled: letter governs) + the 7/31 live price-vintage absorb (earnings-week tape; the 7/24->stale-fallback incident's artifact outputs discarded). One flip eyeballed individually: TNK HOLD->T/S price-led (+18% wk, Q2 refresh queued). CAPT no-flip recorded per the halt rider. dNAV 0.0 every row |
| 2026-08-08T17:51:36Z | b2799a6 | price-vintage absorb 7/31->8/07 (earnings-week tape; dNAV/dFV 0.0 all 25 rows; flips TNK/GNK/GSL/BRUT eyeballed price-mechanical — owner go 2026-08-08) |
| 2026-08-08T18:03:30Z | 4e9bd11 | Q2 cluster transition block 1 — SB/TNK/ASC paired refresh on the frozen 8/07 tape; all three pre-registered bands HIT (TNK +8.8% center-band, ASC -2.5% sign-opposite-confirmed, SB -0.4%); forward invariance verified (22 lagging names delta 0.0 everywhere); logs annotated (owner-authorized sequence 2026-08-08) |
| 2026-08-08T20:35:04Z | f0203b7 | Q2 backlog drain names 1-2: ECO NAV +9.4% and CCEC NAV -8.5%, both INSIDE pre-registered bands, both-halves verified, forward invariance held, logs annotated (ECO eco_log + CCEC ccec_log 2026-08-08); no position flips |
| 2026-08-08T21:24:39Z | ccaa216 | Q2 backlog drain #3: STNG NAV -0.9% INSIDE prereg band; census corrections (74-hull list, Handymax ages fixed, -7 LR2), scrubbers VERIFIED 54 (queue 8->7), debt 855.0 gross w/ OOM converts, both-halves verified, invariance held, stng_log annotated; no flip (HOLD stands) |

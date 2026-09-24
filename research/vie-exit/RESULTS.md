# VIE exit trial: retain temporarily

The shadow infrastructure is implemented. Feed procurement, contract matching and the 20-day live comparison remain blocked. VIE remains active; no purchase, source switch or cancellation has been made.

## Full-book broker diagnostic ablation

All 25 names reproduced the frozen baseline. Removing P/NAV in isolated copies changed none of the checked economic fields, scenario intervals, cycle readings, sleeve values, sign stability or position labels. Governor events were identical.

Available-input publication validation passed. The unavailable-input run was correctly held by existing unexplained diagnostic drift gates; it was never published. Broker checks in the trial are explicitly UNAVAILABLE. Legacy snapshot fallbacks need repair before production removal.

| Ticker | NAV/share | Weighted FV | Blended FV | Economic change without P/NAV |
|---|---:|---:|---:|---|
| 2343 | 0.41 | 0.37 | 0.41 | none |
| ASC | 17.37 | 16.28 | 17.26 | none |
| BRUT | 4.92 | 5.51 | 4.71 | none |
| BWLP | 15.83 | 14.52 | 15.48 | none |
| CAPT | 17.32 | 18.57 | 17.09 | none |
| CCEC | 25.7 | 33.7 | 29.97 | none |
| CMBT | 13.36 | 10.75 | 13.04 | none |
| CMDB | 32.6 | 19.3 | 21.97 | none |
| DHT | 15.01 | 16.56 | 15.26 | none |
| ECO | 39.54 | 44.15 | 39.87 | none |
| FLNG | 27.22 | 29.47 | 27.01 | none |
| FRO | 26.04 | 29.38 | 26.71 | none |
| GNK | 25.37 | 21.05 | 25.23 | none |
| GSL | 41.37 | 42.94 | 44.17 | none |
| HAFN | 4.64 | 5.47 | 4.92 | none |
| INSW | 54.64 | 61.81 | 37.95 | none |
| LPG | 35.69 | 31.82 | 33.93 | none |
| MPCC | 2.15 | 2.16 | 2.33 | none |
| NAT | 2.76 | 3.24 | 2.95 | none |
| SB | 10.72 | 9.01 | 10.42 | none |
| SBLK | 33.27 | 28.2 | 32.81 | none |
| STNG | 76.22 | 75.97 | 72.66 | none |
| TEN | 91.91 | 68.15 | 62.06 | none |
| TNK | 84.6 | 87.59 | 84.12 | none |
| TRMD | 32.3 | 35.14 | 32.62 | none |

## Independent report backfill

94 PDFs indexed: 51 MB, 9 Advanced, 9 Banchero, 8 Fearnleys, 8 Intermodal and 9 Xclusiv. Oldest pending issue: June 26, 2026.
Candidate rows: {'assessment': 150, 'tanker-ffa': 45, 'transaction_table': 101, 'fixture_table': 24}. Extraction failures: 0; warnings: 1. All documents remain pending visual/table triage. Counts are candidate appearances, not unique verified transactions.

## Decisions and next steps

- Retain VIE temporarily: daily matching feed, licensed access and observed 20-day coverage are not established.
- Do not buy standalone P/NAV yet: the reviewed evidence does not demonstrate enough unique benefit; preserve current bug gates pending the explicit unavailable-state review.
- Review vendor-inquiries.md, starting with Baltic. No inquiry has been sent. Exact source contracts and account cancellation terms still need confirmation.
- A real scheduled local scan and a real MB connector run must be evidenced separately. A manual smoke run does not close either blocker.
- Provider-specific live retrieval remains blocked on the contracted sample; the normalized import interface is not a substitute for a live transport.

## Validation

Initial full producer suite: 1,021 passed, four skipped, 12 expected failures; the only failure was the isolated archive symlinks confusing the graph ignore check. Archives were copied into isolation and the graph check rerun successfully. Follow-up targeted suite: 80 passed, including source validation, calendar replay, durable queue, acknowledgments, registry, scoped commits and deterministic DNS guards.

Reproduce the economic comparison with scripts/vie_shadow_compare.py --governor /Users/dan_personal/Projects/portfolio-governance using the project interpreter. It creates disposable clones, regenerates all five scenario families, values both configurations and invokes the publication validator and governor evaluator without notification/healthcheck transports. Full results and workspace identities are in broker_ablation.json.

Rollback: disable only research/vie-exit/trial.json enabled. Preserve receipts and accepted-publication history. Production source switching and governor baseline changes require separate owner review.

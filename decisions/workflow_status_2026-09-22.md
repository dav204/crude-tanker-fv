# Workflow report preview — 2026-09-22 rollout

Read-only preview of the repaired weekly report. This is not a scheduled run receipt,
SMTP acceptance or proof that historical executions occurred. Existing owner decisions,
missing run evidence and the full filing backlog remain open. The inbox permission
request is pending; no permission grant was applied by the rejected action.

# Weekly report — 2026-09-22

**21 need your word · 37 in the agent's queue · 0 longs · 20 moves · HEALTH ATTENTION**

Window: 2026-09-15 → 2026-09-22. Book compared against the scorecard committed 2026-09-15 (3807e9f).

## 1. The book

**Actionable long set: empty** — `` (the scorecard's own four-conjunct read: construction-validated, read-robust, cheap on parity, and a BUY).

| Name | What | Detail |
|---|---|---|
| BRUT | EV | +2.0% → +4.6% (+2.6pp) |
| CAPT | BAND | unreliable read (not actionable) → TRIM/SHORT (overvalued) |
| CAPT | EV | -8.4% → -5.7% (+2.7pp) |
| CCEC | EV | +52.3% → +55.6% (+3.3pp) |
| CMBT | NAV | 16.46 → 13.36 (-18.8%) |
| CMBT | EV | -29.7% → -47.0% (-17.3pp) |
| DHT | EV | -26.8% → -28.8% (-2.0pp) |
| FLNG | EV | -6.3% → -9.1% (-2.8pp) |
| GNK | EV | -20.4% → -24.7% (-4.3pp) |
| HAFN | EV | -41.8% → -46.0% (-4.2pp) |
| LPG | EV | -42.1% → -45.3% (-3.2pp) |
| SB | BAND | BUY (undervalued) → HOLD (fairly valued) |
| SB | EV | +11.5% → -1.9% (-13.4pp) |
| SBLK | EV | -6.7% → -13.2% (-6.5pp) |
| TEN | NAV | 88.16 → 91.91 (+4.3%) |
| TEN | EV | +26.5% → +30.8% (+4.3pp) |
| TNK | BAND | unreliable read (not actionable) → rich · cycle position (not a short) |
| TNK | EV | -17.0% → -13.2% (+3.8pp) |
| TRMD | BAND | BUY (undervalued) → TRIM/SHORT (overvalued) |
| TRMD | EV | +6.6% → -8.1% (-14.7pp) |

## 2. Needs your word

- carry:04 [waiting; resolver owner] — **FRO** whether the associate stake belongs in NAV is a methodology question for the owner.
- governor:CCEC:BASELINE_UNKNOWN_weight_sign_stable [blocked; resolver owner] — review baseline not documented for weight_sign_stable; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:CCEC:BASELINE_UNKNOWN_weight_sign_stable
- governor:CCEC:WIDE_CAP [blocked; resolver owner] — valuation-supported sizing is capped; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:CCEC:WIDE_CAP
- governor:SB:BASELINE_UNKNOWN_weight_sign_stable [blocked; resolver owner] — review baseline not documented for weight_sign_stable; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:SB:BASELINE_UNKNOWN_weight_sign_stable
- governor:SB:VALUATION_CONVICTION_ZERO [blocked; resolver owner] — weight-family sign unstable; valuation cannot support sizing; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:SB:VALUATION_CONVICTION_ZERO
- governor:SBLK:BASELINE_UNKNOWN_weight_sign_stable [blocked; resolver owner] — review baseline not documented for weight_sign_stable; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:SBLK:BASELINE_UNKNOWN_weight_sign_stable
- governor:SBLK:READ_CAP [blocked; resolver owner] — size to the weaker-basis read: flips (cheap/fair); OWNER — open a valuation mini-review; no order is authorized; blockers: governor:SBLK:READ_CAP
- governor:TEN:GATES_PENDING [blocked; resolver owner] — gates: {"buy": true, "current_balance_sheet": true, "family_min": false, "sign_stable": true, "stage_a": "unknown", "war_falsifier": true}; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:TEN:GATES_PENDING
- governor:TEN:GATE_current_balance_sheet [blocked; resolver owner] — gate current_balance_sheet: False → True; OWNER — re-present TEN as a fresh TRADE_PREREG; remaining gates still apply; blockers: governor:TEN:GATE_current_balance_sheet
- governor:TEN:WIDE_CAP [blocked; resolver owner] — valuation-supported sizing is capped; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:TEN:WIDE_CAP
- governor:TRMD:GATES_PENDING [blocked; resolver owner] — gates: {"buy": false, "compressed_curve_anchor": "unknown", "current_balance_sheet": true, "sign_stable": true, "tier": false}; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:TRMD:GATES_PENDING
- governor:TRMD:GATE_sign_stable [blocked; resolver owner] — gate sign_stable: False → True; OWNER — re-present TRMD as a fresh TRADE_PREREG; remaining gates still apply; blockers: governor:TRMD:GATE_sign_stable
- governor:TRMD:WIDE_CAP [blocked; resolver owner] — valuation-supported sizing is capped; OWNER — open a valuation mini-review; no order is authorized; blockers: governor:TRMD:WIDE_CAP
- quarterly:G-2 [blocked; resolver owner] — Decide Hynix armed-prereg disposition; deep-value gate remains armed; blockers: G-2
- quarterly:inbox-permission [blocked; resolver owner] — Approve the narrowly scoped monitor/inbox/** Write grant requested in the task; automatic approval review rejected installation without explicit approval
- roadmap:a1-horizon [blocked; resolver owner] — **The A1 horizon.** Wired at 10 and unratified since 2026-06-11 — ratify it or drop it.; blockers: a1-horizon
- roadmap:b1 [blocked; resolver owner] — **B1** — re-armed 2026-09-18 when TNK's void retired, never ruled. Trigger: the day a registry name reads robust-cheap (none does). `decisions/forks_registered_2026-09-10.md` item 7.; blockers: b1
- roadmap:crude-weights [blocked; resolver owner] — **The crude weight question.** After the 2026-09-18 deck re-expression, 59% of the crude mass sits on a base-tracking leg and 13% carries the only real downside. The deck is now coherent; its de-escalation CONTENT is a weight question, which WO5's kill-switch fences out of agent scope. Not a registered fork. `decisions/r4_deck_reexpression_method_2026-09-18.md` §8.; blockers: crude-weights
- roadmap:product-reexpression [blocked; resolver owner] — **The product deck's own re-expression.** Same absolute-curve construction against the same moving base; WO5 was crude-scoped by design. Not a registered fork.; blockers: product-reexpression
- roadmap:ten-anchor [blocked; resolver owner] — **TEN's alternative anchor.** TEN is structurally APPROX — no broker anchor exists. VIE? company-implied? none? Resolving it moves TEN out of `tests/test_approx_roster.py`'s guard.; blockers: ten-anchor
- FORK-OPENED — ten_commitments_convention: executes after 2026-09-24 unless you object — HOLD advances-only on TEN (newbuild_capex_commitments stays 0) and carry the now-CITED 2,233,409k remainin
Status evidence is incomplete. The agent repair queue below remains open.

**Agent/external tasks and workflow repairs:**

- carry:01 [waiting; resolver agent] — **SBLK** share count 111,671,386 → 116,071,386. Corroborated a third time 2026-09-18 (0000950157-26-001031, holdings-notification denominators); still no treasury figure stated, so the net-of-treasury caveat stands for the owner-present sheet build.
- carry:02 [waiting; resolver agent] — **HAFN** Q3 cash-for-investment swap: ΔNAV ≈ 0 only if both legs move together. The TORM leg is now a SHARE COUNT, not a percentage — **18,656,061** TRMD A-shares, issuer-stated by TORM 2026-09-18 (0000919574-26-006391 ex-99.2); the 18.22% / 18.19% gap is TORM's denominator moving on its own RSU issue, not a disagreement.
- carry:03 [waiting; resolver agent] — **TRMD** next vintage carries the exact count **102,553,688** A-shares (104,000,000 is rounded; two RSU increases, +31,483 on 9/11 and +132,421 on 9/18, both below any gate).
- carry:05 [waiting; resolver agent] — **Front Vefsna** $135.0M (FRO P1 leg) stays unpromoted, blocked on issuer vessel-name disclosure.
- carry:06 [waiting; resolver agent] — **CMBT** §9.4 yard-quality discount and Dec-2025 segment vintages — revisit at the November Bermuda appeal.
- carry:07 [waiting; resolver agent] — **SB** `analyst_target` 7.10 has been STALE-flagged since 8/29. **GNK** dividend guidance wants a cross-check against `dividend_policies/gnk.yaml`.
- carry:08 [waiting; resolver agent] — **PANL** onboarding deferred; the B3 IR query went out 2026-08-12 and is still waiting. Scaffolded in `data_sources.yaml`, not watchlisted.
- defect:01 [ready; resolver agent] — `drift_gate` has no from-inputs recompute mode, so a clean clone cannot run the gate.
- defect:02 [ready; resolver agent] — `decision_log_annotated_since` string-matches `**Decision:**` exactly (`drift_gate.py`); a dated prefix is invisible to it and untested.
- defect:03 [ready; resolver agent] — `_fetch` catches only `HTTPError` in `hkex_poll.py` and `newsweb_poll.py` — a `URLError` escapes both pollers. One module-level fix.
- defect:05 [ready; resolver agent] — CLAUDE.md's APPROX list names five tickers; `reconcile.APPROX_PNAV_TICKERS` holds nine (adds CMDB, GSL, SB, 2343).
- defect:06 [ready; resolver agent] — The eight-item news-pull limitations backlog has never been triaged (GlobeNewswire timeout, sec.gov/efts 403, hellenic/splash 403, PDF primaries via `fetch_pdf`, JS-shell IR pages, Glob/Grep restore-or-bless, the missing 8/14 daily).
- filings:pending [ready; resolver agent] — Drain all pending accessions; commit dispositions before acknowledging
- fork:ten_commitments_convention [waiting; resolver agent] — HOLD advances-only on TEN (newbuild_capex_commitments stays 0) and carry the now-CITED 2,233,409k remaining commitment as provenance on the line — the CMBT Branch-A shape. The §9.6 gate is procedurally open (TEN is out of NAV_FIGURE_ESTIMATE_QUEUE) but the ASSET half cannot be built: 10 of the 20 hulls are DP2 shuttles, 62% of the $2,413M priced program, and there is no shuttle class in vessel_value_curves.yaml, so every netting variant books the obligation without its asset. Sized, all four: naive commitment-net -$74.13/sh (NAV -> 17.78, -86.0% vs broker = SANITY FAIL); on-curve markable-only -$53.18/sh (-69.5% = SANITY FAIL); on-curve at contract price PV'd -$22.82/sh; the same undiscounted -$9.64/sh, which is exactly the unpriced-20th-hull residual — i.e. at a zero discount rate advances-only IS contract-value-net, so holding is not ignoring the obligation, it is netting it 1:1 against the asset it buys. ALL FOUR cross the governance sizing gate: ev_pct_family_min falls below the +5 BUY edge at -$3.60/sh and sign-flips to conviction-zero at -$7.51/sh. TEN stays in OFF_CONVENTION_QUEUE and takes NO structural_exempt line (the BWLP verifier's ruling, and it would be factually false here since 10 of 20 hulls ARE markable). Predicted impact: ZERO on all 25 names — comment and provenance text only; commitments, advances, the manifest, the curve registry and the convention registry are FROZEN; any nonzero NAV = HALT. Exit condition, explicitly NOT this fork: a §11.6 newbuild-shuttle contracted-book leg, a TEN newbuild_specs.yaml entry with cited scrubber/eco flags, and a disclosed price for the 20th hull.
- housekeeping:01 [ready; resolver agent] — **F13** — merge `TICKER_NOTES.md` into the per-ticker log headers and delete it; CLAUDE.md's router still points at it.
- housekeeping:02 [ready; resolver agent] — **F16** — four worktrees live under `.claude/worktrees/`; confirm `goldstine` is merged, then remove them.
- housekeeping:03 [ready; resolver agent] — **F19 remainder** — the `sp_scan` tanker-period-signal internals are dead data.
- housekeeping:04 [ready; resolver agent] — **Autopilot Stage A is 3 of 5**: `promote check`/`land`, the weekly report and the "Needs your word" queue ship; the **Saturday stager** and the **pin migration** (`tests/fixtures/pins.yaml`) do not. Gate 0→A has no owner attestation on file — write it or delete the gate.
- housekeeping:05 [ready; resolver agent] — **Standing rule that belongs elsewhere:** source sweeps run single-threaded, no parallel fleets of web-fetch-heavy agents. Graduate it to WORKFLOWS.md and drop it from here.
- quarterly:G-3 [ready; resolver agent] — Reconcile USDNOK basis in monitor; preserve portfolio rulings
- quarterly:scheduler-proof [blocked; resolver agent] — Run fresh scheduled smoke using scoped inbox Write and --probe-file; verify application log contains no approval request; blockers: quarterly:inbox-permission
- roadmap:dm2-dm3-dm4 [ready; resolver agent] — **D-M2 / D-M3 / D-M4** (per-sector asset r_a and relever · cycle-parity denominator A/B · piecewise-linear cycle) are RULED and UNEXECUTED; their post-Stage-A gate expired 2026-08-10.
- roadmap:gsl-commitment [ready; resolver agent] — **GSL containers commitment-net prereg** — the shape CMBT took on 2026-09-16. `OFF_CONVENTION_QUEUE` is {GSL, STNG, TEN} and GSL leaves by this route.
- roadmap:image-filings [ready; resolver agent] — **Auto-fetch page images for image-only filings.** Detection ships (`arrivals.validate_html`); recovery is still done by hand, 86 images last time.
- roadmap:lr1-anchor [ready; resolver agent] — **LR1 contract-floor anchor round.** The only overdue valuation work. Frozen prereg (`PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md`), its post-Stage-A gate cleared 2026-08-10 and Stage B landed 2026-09-09. Predicts INSW +$7.80M, TEN +$1.17M, TRMD and HAFN exactly 0, and takes TRMD to VALIDATED-TIGHT.
- roadmap:q3-calendar [ready; resolver agent] — **Q3 calendar re-seed** — CMBT 11/26, BRUT 11/19, OMC AR 2027-02-25. Dispositions are parked in `state/filings_triaged.json`; `inputs/earnings_calendar.yaml` still carries Q2 dates.
- roadmap:stng-newbuild [ready; resolver agent] — **STNG 10-hull §9.6 wiring** — un-gated since thread (d) signed 2026-07-15, ~+$9.6/sh, its own pre-registered step.
- trigger:container_mb_refresh [waiting; resolver agent] — Same §11.8 ingest procedure: newest weekly, class-collapse per §11.8.1 (A3 re-weight if the validator fleets changed), machine as_of, decisions/ note, gate annotation for MPCC/GSL moves. Re-arm monthly on completion.

- trigger:crude_geopolitics_weekly [waiting; resolver agent] — LEG 1 fires: revisit the pre_mou_baseline -> mou_bear mass (a functioning fee regime is mou_bear's registered premise — "framework holds, tolls imposed post-day-60" — which the 8/16 observed state contradicted and which systematic collection would restore). Rerun §9.10, reweight, annotate, ratify. LEG 2: any change of state is correction-annotated on the prior record FIRST, then the escalation question is re-run against the corrected record — never on an uncorrected premise. A reweight proposal is pre-registered (predicted impact per crude name, band, flip tripwires), verified, then registered in inputs/forks.yaml under the silence rule (owner policy 2026-09-10) — it executes by silence or word.

- trigger:handy_bulk_txn_refit [waiting; resolver agent] — Owner-run promotion: classify prints (eco/gear/TC-attached/survey adjustments) into transactions/handy_bulk.yaml, run the §9.9 dwt-normalized fit (38k baseline), predict bands AHEAD, re-run the drift-gate loop; the class leaves un-anchored (LNGC-regime) k_broker semantics and basis_status/handoff tiers upgrade accordingly. Expected fit direction: 5yr/10yr DOWN toward prints (prereg Band 3) — do not "fix" the interim high-side reads toward Pareto meanwhile.

- trigger:lpg_anchor_annual_review [waiting; resolver agent] — Re-derive the trailing-10yr VLGC realized-TCE mean off Dorian's + BW LPG's latest 10-K/20-F year-by-year TCE series (the FY2016-26 series is in the methodology doc); update the anchor value + as_of; re-run the LPG cycle layer; gate-annotate; re-arm +1yr. Realized-TCE basis is correct for the 85-99%-spot validator pair — do NOT switch to 1-yr TC (that stays a documented cross-check only).

- trigger:lpg_v1_lock_rerun [waiting; resolver agent] — When the splits land: promote the per-vessel prints to transactions/ vlgc.yaml, re-fit (prints->rerun->drift loop, annotate moves), then re-run `/reconcile --calibration-lock lpg` and put the readout to the OWNER — the 2026-07-10 ruling (option (a), PLAN decision #1b) holds the sector at PROVISIONAL·v1-lock-miss (SECTOR_V1_UNLOCKED) until that re-run; if the re-fit still misses on the residual broker premium, the GOVERNED-WIDE question returns to the owner WITH evidence (logged amendment, not blind loosening). If the splits have not been filed by the due date, record the check and re-arm toward the FQ3 10-Q (~Feb-2027) — NOTE R-5: the charter expires 2026-12-26; work past it needs a new charter.

- trigger:ppmx_txn_refit [waiting; resolver agent] — Re-fit the PPMX anchors + re-derive the MARK_WIDE_NODES band; take the old-age-overhang methodology fork to the owner (the scrap-anchored [10,25] segment reads ~+28% above the seed's print cloud — steeper terminal vs accept-as-documented). decisions/ppmx_fit_seed_prereg_2026-07-18.md.

- trigger:product_glut_arrival_timing [waiting; resolver agent] — Tightness persisting into Q4-2026 at glut_base weights: shift mass back toward refinery_squeeze/moderate_correction with a dated non-war rationale. Glut arriving early: shift toward demand_softening. Either way §11.5 revision + lock-test re-pin.

- trigger:tce_means_semiannual_review [waiting; resolver agent] — Re-derive the trailing 10-yr mean for EVERY class off its documented route benchmark / basis (VLCC TD3C, Suezmax TD20, etc. — the per-class basis and its caveats are commented in the file itself). TC-ANCHORED throughout, not spot — re-run METHODOLOGY §8.3's self-check that no spot-anchored component has crept in. Do NOT bulk-update from VIE: the ~14-58% VIE gaps are deliberate base-period / outlier-handling differences and switching base shifts FVs across the whole watchlist (per-class methodology decision required, §8.3 Step 3). Update values + as_of, re-run the cycle layer, check the drift gate, gate-annotate every class whose EV moves >2pp, and re-arm +6mo. LPG DEFERS to lpg_anchor_annual_review, whose realized-TCE basis is tied to the Dorian 10-K / BW LPG 20-F filing cadence — this sweep records LPG as "covered by the annual trigger", it does not re-derive it.

- Operational receipt evidence UNKNOWN [resolver agent] — establish the missing execution/landing receipts; do not infer historic success
- FILING-QUEUE-STALLED 0000950157-26-000799: 100 pending; oldest 2026-07-14T14:20:05+00:00; repair daily triage [resolver agent]

## 3. What the machine did

- **Standing drift is AUTO-ABSORBABLE** (25 gate rows): price-vintage only, no NAV move, no band exit, no BUY-ward flip. This is the shape a one-word ratify takes.
- Legacy SMTP acceptance ledger in the window: 8 page(s), 8 digest(s); last send 2026-09-22T15:15:07+00:00
- Baseline re-anchors:
    - 2026-09-16 — auto-land 2026-09-16: The 2026-09-15 dry FFA promote (decisions/ffa_promotion_2026-09-15.md, the ruled straddling construction) moved the Supra-Ultra 
    - 2026-09-18 — 2026-09-18 dry FFA promote plus the spot promote and the 9/17-9/18 tape: 12 rows annotated, NAV unchanged on every name
    - 2026-09-18 — WO5/R4 the crude deck re-expression and its three Phase-4 void dispositions (decisions/r4_deck_reexpression_method_2026-09-18.md). Deck: the three de-
    - 2026-09-21 — TEN 2026-Q2 pair landed: NAV/sh 88.16 -> 91.91 (+4.2%), EV +6.0pp, band BUY unchanged. Both blockers ruled — shuttle extension rate cited at 55,000/da
    - 2026-09-22 — auto-land 2026-09-22: BWLP broker reference repaired from $20.40 to $19.04 using its matched source price/P-NAV pair; this is a diagnostic correction,
- Uncommitted files: 0 · unpushed commits: 26
- producer execution: UNKNOWN — missing receipts
- publication attempt: accepted; state/publications/status.json; stages {}
- governor landing: UNKNOWN — missing receipts
- accepted publication: 402b3fc5d56691b112824b24acac4c9970220f35cc01d7e141ff94efe92dc700
- consumption: 402b3fc5d56691b112824b24acac4c9970220f35cc01d7e141ff94efe92dc700
- producer delivery: 0 unresolved exact-message receipt(s); SMTP accepted is not proof of inbox delivery
- governor delivery: 0 unresolved exact-message receipt(s); SMTP accepted is not proof of inbox delivery
- Automation authority: graph.yaml and recorded rulings; authority is separate from observed execution/landing evidence.
- Complete filing backlog: 100; oldest arrival: 2026-07-14T14:20:05+00:00; invalid records: 0

## 4. Health

| Job | Outcome | Age (h) | Late? | Last heartbeat |
|---|---|--:|:--|---|
| delivery-worker | ok | 0 | ok | 2026-09-22T19:56:32Z |
| edgar-poll | ok | 1 | ok | 2026-09-22T19:20:25Z |
| harvester | ok | 76 | ok | 2026-09-19T16:00:26Z |
| news-pull | ok | 77 | ok | 2026-09-19T15:01:24Z |
| price-refresh | skipped-dirty | 18 | ok | 2026-09-22T01:30:05Z |
| rocketchat-ingest | ok | 6 | ok | 2026-09-22T14:00:21Z |
| sentinel | ok | 5 | ok | 2026-09-22T15:15:09Z |

- Credentials: no surface has reported an auth failure.
- Dead-man ping: SENT at 2026-09-22T15:15:08

## 5. Next 14 days

- **2026-09-24** — trigger crude_geopolitics_weekly due
- **2026-10-02** — trigger container_mb_refresh due
- **2026-10-02** — trigger product_glut_arrival_timing due

## 6. Flag counts (what the daily digest would have mailed)

- FILING-LANDED: 100
- UNINGESTED-PRINTS: 2
- FILING-QUEUE-STALLED: 1
- FLEET-TRANSACTION: 1
- FORK-OPENED: 1
- NOTIFY-UNCONFIGURED: 1
- STALE-INPUT: 1

_Generated by `crude_tanker_fv.weekly_report` at 2026-09-22T19:56:53+00:00. Every figure is derived from a committed surface or machine state; nothing here is hand-maintained._


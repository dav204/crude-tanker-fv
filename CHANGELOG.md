# Changelog — Tanker FV tool

Split out of CLAUDE.md (2026-06-22) to keep the operating rulebook short.
Append new dated entries at the TOP. This is the running history of
methodology decisions, onboardings, and fixes; CLAUDE.md carries only the
live rules distilled from it.

- **2026-09-02 — THE AUTOMATION RULING + STAGE 0 LANDED.** *Owner words (on
  `decisions/autopilot_authority_2026-09-02.md` — a code promoter with bounded authority inside
  guard-tested predicates, rolled out A→D behind clean-season gates — and
  `decisions/prune_ledger_2026-09-02.md`, the 82-row prune ledger):* "adopt Stage 0 · accept all
  Q recs · accept all F recs except F7 no (keep), F18 no (keep)". Both documents were produced by
  multi-agent design/audit workflows (4 readers → 3 designs → 9 adversarial verifications → critic;
  5 auditors → 5 refuters) and re-verified read-only at HEAD 4bb3237. *Stage 0, executed this
  sitting:* (1) the 8/31 archive-gap entry re-shaped into the `accepted[]` schema — appended at
  root level it had broken the YAML parse and CRASHED the 9/01 sentinel (no digest, no page, no
  ping) while the heartbeat recorded a normal `flags` day; `tests/test_live_yaml_parse.py` now
  loads every live input YAML. (2) CI unblocked: two unused imports had failed `ruff` on every
  Action run since 7/24, so the clean-clone suite had not executed for six weeks (one import is a
  re-export the shared-state guard test reads — kept with `noqa`). (3) Sentinel exit codes
  0/2/1; the wrapper records a traceback as `error`. (4) Routing re-cut (owner Q-9): `page` /
  `page_once` / `digest` / `record_only`; only `FETCH-FAILED` escalates (F10); `EARNINGS-UNCONFIRMED`
  and `EARNINGS-SWEEP-STALE` routed explicitly — they had paged ~50× in August through the
  unknown-tag rule because the routing test's hand-typed tag set omitted them (it now derives the
  live set from `sentinel.py`); `FILING-LANDED` keyed per accession (94 page instances for 52
  filings); the sweep-stale trailing colon dropped. (5) `REAUTH-NEEDED`: `reauth.py` +
  `state/reauth/` (Rocket.Chat 401/403, SMTP auth, two healthchecks 4xx), paged once;
  `state/ping_status.json` records every ping outcome (it was stdout-only). (6) The daily ingest
  chain indexes BEFORE it scans (`pareto_archive --build-manifest --incremental`, new PDFs only)
  and the Saturday chain's full rebuild now precedes the scan — the 9/01 "nothing to scan" was a
  stale index; `sp_scan` keys on a scanned-path set so a late-arriving older issue is scanned.
  (7) FFA OCR accepts the ratified month-end 4-tenor grid and sorts Q tenors from the print
  quarter (the 8/31 column-transposition trap). (8) `price_refresh` writes atomically and a bare
  run ledgers itself `manual:` (the seven 8/17-24 salvages were invisible to the no-human-fetches
  instrument). (9) HKEX governance notices (terms of reference, corporate governance,
  Circulars-[Other]) no longer page. (10) `agent_duties.yaml` gains `artifact_path:`; the
  governance repo's Friday monitor is a registered duty. (11) The expired summer `silence_days`
  override dropped. (12) The README test-count guard is a floor check (adding tests no longer
  reds it). *Owner acts still owed — an agent cannot do them:* `launchctl unload` the two zombie
  ctxprobe plists; set `SENTINEL_LITE_HC_URL` or record the Action unmonitored; name the two days
  for the healthchecks ping-gap drill (Q-10); `git push`. *The F-list prune executes in the
  commits that follow; Stage A (shadow promoter, weekly report, decision queue) is the next build.*

- **2026-09-02 — THE PRUNE ROUND EXECUTED (owner F1-F20 at their recommendations; F7/F18 = keep).**
  *Why:* the 2026-09-01 audit traced every job, flag, output, trigger and guard to a named consumer
  (a loader that reads it into a number, a `book_scorecard.json` field the governance repo reads, a
  ruling that cites it, or a guard with a recorded catch); five refuters then tried to rescue each
  candidate. What survived the refutation is deleted here, one commit per item, all git-reversible.
  **Stopped:** the WO2 acceptance ritual (`close_acceptance.py`, its null receipts, the ping-gap
  drill doc) and the ctxprobe scripts/tests — never run, never measured (F6; the two installed
  plists are an owner `launchctl` act) · `draft_queue.py`, which shelled to a `claude` CLI this
  machine does not have and served 0 of 17 preregs · the Baltic index text lane, its parser and the
  capesize PNG lane — `normal_rates` refuses index points BY CONTRACT (§18.5a) and the README itself
  said "deliberately unconsumed"; the 769-row CSV is frozen in git, not deleted (F14) · the §16
  overlay ledger, `inputs/overlays.yaml` and its renderer — no reader anywhere, rows keyed to the
  Jun-9 weights (F4; the §12.6 dividend-window control survives in `dividend_window.build_rows`) ·
  the linked-Pareto-report weekly harvest — one basis citation ever against 192 MB of unread PDFs
  (both modules stay for on-demand onboarding) · `ffa_vs_strip`, the 20 `pareto_mentions_*` sweeps,
  `state/fdprobe` · **every `.xlsx`**: 35 committed workbooks, 4,074 blob versions, zero readers
  outside tmp-dir tests — `fair_value_summary` and `scenario_summary` existed ONLY as workbooks and
  are gone (the roll-up is `outputs/book_scorecard.md`, which is what the consumer repo reads) ·
  the consensus-EPS xref and the §12 dividend-window render leave the per-regen path; the
  transaction-anchor comparison becomes the S&P ROUND's artifact (`pipeline <Q> --txn-comparison`) ·
  the harvester CI job (F1 — its N-5 rationale died when the 8/31 and 9/01 rounds cited harvester
  output 0×; the Saturday crawl STAYS, F2, because it parses the xclusiv row that IS the age-0 NAV
  anchor) · `spot_tce` leaves the UNINGESTED lane (F17 — diagnostic-only, and no spot parser exists
  to promote from) · the Test-2 per-quarter re-run duty (F15 — nobody owned it) · three stale
  worktrees (F16 — `git cherry` confirmed every commit is in main; the branches are kept).
  **Simplified:** a pipeline run now writes a decision-log entry ONLY for names that moved
  (material / new / gate-breaching) — 5,042 machine headers against 163 human ones had buried the
  annotations the entries exist to prompt (F12) · the trigger register keeps ARMED cards only,
  23 → 10 and 539 → 270 lines, with eight done cards moved verbatim to
  `decisions/reweight_trigger_archive.md` and five retired with their reasons (F20, F8) · the
  `sentinel-lite` issue is re-edited only when the flag set changes, and the clean-clone job is
  push-only (F9). **Deferred by design:** F3 (fold the two Hormuz cards) and F19 (retire
  `tanker_forward_print_lands` + the TRIGGER-EVIDENCE lane) wait for WO5 / Stage B on 9/04-05.
  **Kept against a prune recommendation, on the owner's word:** the 2017-2024 FFA image archive
  (F7) and `shipping_harvester/data/` (F18) — both irreversible deletions of gitignored disk with
  no recurring cost. *Full reasoning, per item, with consumer / last-mattered / cost / removal
  steps:* `decisions/prune_ledger_2026-09-02.md`.
- **2026-08-16 — THE OSLO/EURONEXT ISSUER CHANNEL EXISTS: `newsweb_poll.py`, the third venue
  adapter, closes the last venue with no filing lane.** *Why:* BRUT/MPCC/CAPT carry
  `sec_edgar: null` and no HKEX id, so nothing mechanical could see their corporate actions —
  `edgar_poll.covered_ciks` said as much in its own docstring ("their net is the calendar +
  FILING-OVERDUE **until the Oslo poller follow-up**"). This is that follow-up, and the bill for
  its absence is now four items long: BRUT 7/07 (demerger + delivery + SLB + CEO, unread 5 weeks),
  MPCC 6/25 ($340m of ships + $375m loan, unread 7 weeks), MPCC 6/30–7/02 (a COMPLETED placement of
  44,370,027 shares = **exactly +10.0%** of the share count `mpcc_2026-Q1.yaml` still carries — a
  denominator change no scanner in the repo could see), and CAPT 8/06 + 8/13 (two §9.6 deliveries
  plus $117.5m of financing, missed by the agent sweep built to catch them). *Mechanism:* MFN's
  JSON Feed 1.1 at `mfn.se/all/a/<slug>.json`, slugs from new `mfn_slug:` keys in
  `data_sources.yaml`; staging-only; rides the hourly edgar-poll launchd row exactly as `hkex_poll`
  does; bodies + PDF attachments to `inputs/filings/<ticker>/`, arrivals to
  `state/edgar_manifest.jsonl` with `source: "newsweb"`. *Two design traps, both found by
  simulating the spec against the LIVE feeds before writing the filter:* (1) the obvious relevance
  allow-list (`:regulatory` + `inside-information`) **drops CAPT's vessel deliveries**, which carry
  `ext:ob:non-regulatory` — the same tag as the noise bucket — i.e. the natural filter would have
  missed the exact releases motivating the module; so relevance is a DENY-list of one tag
  (`sub:ci:insider`), affordable because post-dedup volume is ~2–4 releases/issuer/month. (2) each
  release can arrive TWICE, `source: "ob"` (Oslo Børs mirror) and `source: "mfn"` (issuer), seconds
  apart under different `news_id` **and** different `group_id` — so identity keys on (date,
  normalized title). A whitespace-only normalization still leaked CAPT's 2026-06-04 ex-dividend
  twin because the mirror renders the issuer's en-dash as whitespace; punctuation is not identity,
  words are. Audited every collapse on live data: 21 collapsed, all true twins (19 ob/mfn pairs +
  2 same-day duplicate "Financial calendar" filings), zero false collapses. *Guard, not prose:*
  `tests/test_newsweb_poll.py::test_known_historical_misses_survive_the_filter` pins all four
  historical misses as fixtures with their verbatim live tags, so any future tightening of
  `NOISE_TAGS` into an allow-list reds the suite instead of silently re-opening the hole.
  CLAUDE.md deliberately **not** touched — it sits 20 chars under its cap and the rule is
  guard-enforced, which is exactly the case the compounding-knowledge habit says to carry as a test
  and not a sentence.
  **ADVERSARIAL REVIEW, SAME DAY — and it caught a SAFETY-NET REGRESSION the build itself
  introduced.** A four-lens review (correctness / conventions / integration / operational) with
  per-finding refutation agents was run over the new module. Six defects were confirmed — by the
  review with live reproduction, or by me reading the code — and all six are fixed with guards:
  (1) **FILING-OVERDUE was being silenced.** `sentinel._filing_event_flags` clears that flag on ANY
  manifest arrival with `filed >= window_start`, and its own text calls it "the Oslo trio's net."
  Before this poller those four names had NO manifest lines at all, so the net always held; after
  it, a routine ex-dividend or financial-calendar notice would clear it for a report that never
  landed. **Adding the channel would have removed the net.** Fixed by putting `report: bool` on the
  manifest line (MFN's `sub:report*` namespace — verified more precise than title keywords: it
  excludes "Results of Annual General Meeting" and "Q2 Financial Report Release ... on 28 August")
  and gating `arrived` on it; edgar/hkex lines carry no such key and default True, so their
  behaviour is byte-for-byte unchanged. Guarded by
  `test_non_report_newsweb_arrival_does_not_silence_filing_overdue`, verified to RED against the
  pre-fix sentinel and green after — the guard is not vacuous.
  (2) **The noise deny-list was defeated by the untagged twin.** Filtering per-copy *before* the
  collapse makes the filter only as strong as the weaker-tagged copy: BRUT's real 2026-06-19 PDMR
  notice carries `sub:ci:insider` on the mfn copy and a bare `:regulatory` on the ob copy, so
  filter-then-collapse dropped the tagged one and emitted the untagged one. Reproduced on the live
  feed (shipped order emitted 1, corrected order emits 0) — and it was already latent in the
  bootstrapped state file. Now collapse-then-filter.
  (3) **`seen_ids[:200]` kept the OLDEST ids** — `dedupe()` returns ascending where both sibling
  pollers' upstream indexes are newest-first, inverting the property that makes the cap safe.
  (4) **A 200 response with an empty item list wiped `seen_ids`**, so the next good poll would
  re-emit and re-download everything above the watermark. (5) The remote `publish_date` was
  interpolated into a staged filename unsanitized. (6) Attachments were downloaded but never
  referenced on the manifest line, and a cap-dropped attachment left no trace; both now recorded.
  Also: `form` carried raw tag soup that the FILING-LANDED pager rendered verbatim — it now carries
  a human label ("interim report", "inside information", "corporate action") and the pager appends
  the headline. **Caveat on the review:** 13 of its 29 agents died on connection errors, so its
  own `rejected_count: 18` is NOT evidence of refutation — the surviving findings were re-verified
  by hand against the live feeds rather than taken on the workflow's arithmetic.
  A seventh followed from the same review and is also fixed: the collapse elected a winner by tag
  richness but persisted only the WINNER's `news_id`, so if the two copies were indexed in
  different polls (ob first, mfn second) the flip re-emitted the release; every id in a collapsed
  group is now marked seen. 27 new poller tests + 1 sentinel guard; full suite **694 passed /
  3 skipped / 14 xfailed**, ruff clean, drift gate unaffected (no NAV surface touched).
- **2026-08-16 — WEEK-CLOSE (the 8/10 week): Stage A lands → the tier learns what it certifies → the toll cliff resolves into the observed state.** The week's arc: (1) **STAGE A LANDED 8/10** (d510311; frozen 7/15 prereg + four owner rulings): the Jun-7 war-vintage tanker curves RETIRED, INSW band-HIT $54.64; the halt fired and was disposed (B) — the BRUT/CAPT/TNK BUY-ward flips VOIDed as deck-incoherence artifacts pending the 8/16 re-derivation. (2) **BRUT H1 8/13**: prereg band HIT ($9.62 in [8.50, 10.00]), the cash flag resolved, and the tier moved PROVISIONAL→GOVERNED-WIDE **mechanically** (subreason cash-pending → going-concern-unfinanced); ratified @ 54276ea. (3) **The 8/07 consensus-pair rebase PROMOTED 8/13** (bffdbfe → ratified a2d46ca): 20 names one vintage, 2343 issuer-NAV pnav 0.98→0.91, GNK anchor re-pointed to Pareto NAV $28.40; the k-vintage-skew allowance RETIRED — and the rebase's SBLK demotion surfaced the flaw that became (4). (4) **TIER SEMANTICS AMENDMENT ruled + landed 8/13–14** (entry of 2026-08-13 above): tier = construction only, TIGHT gates on evaluability, governed `read_flag` (HYST 2.0), schema 2.7→2.8, migrations exactly {SBLK, CMDB, GNK}→VALIDATED-TIGHT, edge-cleared long set **{SB}** unchanged; Addendum B2's tape-basis flip strobe landed on the **delta/monitor layer only** (6f6648a — SBLK's +0.62% tape margin finally reaches a surface; the settling edge is the NEAREST state-changing boundary, not always the weaker basis: GNK settles on PARITY cheap|fair at $25.90). (5) **TOLL CLIFF 8/16 — C2 EXECUTED** (decisions/crude_day60_toll_cliff_2026-08-16.md): neither pre-registered branch fired (fee INTENT documented — PGSA "service fees", the UNCLOS-safe framing — collection NOT evidenced; no extension; Oman framework not convened; the window expired into interdiction, traffic 17% of pre-conflict); crude **0.25/0.57/0.05/0.13 → 0.25/0.62/0.00/0.13**, `mou_base` retired AT ZERO (series continuity — deleting a leg silently narrows fv_low/fv_high); R2 product revisit a recorded NO-OP (IEA stockpile observation routed to `product_glut_arrival_timing`, 10/02); **R4: the Stage-A voids STAND** — deck re-expression docketed as its own work order (corrected framing per the adversarial review: CAPT the one BUY-ward void at tape, TNK reads HOLD); R5: C3 escalation tilt DECLINED; successors `hormuz_fee_collection_watch` (label-agnostic, standing; due date owed to owner) + `escalation_pause_corroboration` (8/23, primary sources only, correction-annotate-first). The record's own adversarial review (wf_8b0d1184) caught and fixed three errors before ratify — the sim priced at watchlist STATICS not the tape (deltas survive, levels didn't), the TNK BUY-ward read was that artifact, and the planned BRUT annotation was mooted by a −11.6pp price leg netting −9.3pp. (6) **Venue + cadence hardening, all 8/16:** `newsweb_poll` third venue adapter (entry above — the four-miss bill: BRUT 7/07, MPCC 6/25 + the +10.0% placement, CAPT 8/06+8/13) · `cron_lane` per-lane outcomes on the edgar-poll row (`note=edgar=ok,hkex=ok,newsweb=rc1` — the 2026-07-18 camouflage rule inverted: red-on-a-sibling was hiding two live lanes; wrapper still exits 1, a down poller stays loud) · `historical_tce_means` moved OFF the 30d mtime clock onto **`tce_means_semiannual_review`** (due 12/07; every entry is a TRAILING 10-yr mean and the two largest distortions — war tape entering, 2020-22 trough leaving — are live in the roll now; guard `test_tce_means_cadence_has_an_owner`) · the weekday-dependent sentinel test fixed (entry above) · the healthcheck pager RE-ARMED (PING-SENT — the 7/13-drill comment-out finally restored). (7) **Week-close two-cause ratify @ e92fa8a** (RATIFY_LOG 2026-08-16T20:09Z): C2 weight leg (+0.20…+2.47pp, EV-positive all ten crude names) + the 8/12→8/14 price vintage, adversarially verified TWO-cause exact (max residual 0.05pp); dNAV 0.0% all 25 rows; **three flips eyeballed individually** — **2343 HOLD→T/S band-EXIT = static-fallback RELEASE** (the stale 7/14 static 0.39 stopped tripping the ±30% guard; a genuine month-long HKG rally absorbed in one +26.9% step — **watchlist rebase OWED, urgent**), ASC HOLD→T/S band-mech (pre-warned oscillator), SBLK BUY→HOLD band-mech (FV-line whipsaw; three-thread sitting stands, GTC untouched); k_broker breaches (INSW/LPG/STNG/TNK) price-mechanical. Suite **700 green with the gate AWAKE** — the C2 commit's earlier green was green-with-the-gate-ASLEEP (stale `state/` had SKIPPED the three freshness tests; they armed one minute after the regen), a pattern worth naming. Gate 25 rows, 0 UNEXPLAINED; pushed at 4029e09. **Open into next week:** the earnings train 8/26–28 + Stage B 8/26–9/04 (bands BEFORE prints), the R4 deck re-expression WO, the 2343 rebase, the MPCC prereg share-count amendment, the NAT date sweep, June 1–3 archive gap, and the 8-item news-pull limitations handoff (NewsWeb item closed same day).
- **2026-08-16 — WEEKDAY-DEPENDENT TEST FIX: `test_archive_gap_sees_hole_behind_a_live_head` staged
  on BUSINESS days but asserted on CALENDAR offsets.** The test reds whenever the suite runs on a
  **Friday or Saturday** — pre-existing at `fc7fee3` (reproduced in a clean detached worktree),
  unrelated to the tier work it surfaced beside. *Mechanism:* the fixture stages `i` in 0..39
  skipping weekends and skipping `i` in [14,21] to punch the hole, then accepted the gap with the
  raw window `today−21 .. today−14`. But `_archive_gaps` reports the hole in **calendar** terms —
  first missing business day `..` the day *before* the feed resumes (`d − 1` where `d` is the next
  staged business day) — so a hole that resumes on a Monday drags the reported end across the
  weekend. On Fri 2026-08-14 the detector reported `2026-07-24..2026-08-02` while acceptance
  reached only `2026-07-31`, so `_accepted_gap`'s `end <= to` leg failed, the flag survived, and
  the final assertion red. *Fix:* derive the accepted window from the staged calendar itself —
  last staged date before the hole `+1` .. first staged date after the hole `−1` — which is
  **exactly** what the detector reports on every weekday, not a widened one; the assertion is
  untouched, so "acceptance silences it, and nothing else does" still binds, and a blanket window
  would still be wrong. *Verified:* seven-weekday sweep with a faked `date.today()` (patched on
  `datetime`, the test module, and `sentinel`), Mon 2026-08-10 → Sun 2026-08-16, all PASS; the same
  sweep run against the **pre-fix** test from HEAD fails on exactly Fri + Sat and passes the other
  five, which bounds the bug and proves the harness wasn't agreeing with itself. Full suite green
  (657 passed / 4 skipped / 14 xfailed). No engine change — `sentinel.py` is correct as written;
  the test was measuring the wrong thing. Field-general lesson, guard-carried rather than
  prose-carried: **a fixture that stages on business days must assert on the calendar the detector
  reports, never on the day offsets that punched the hole.**
- **2026-08-13 — TIER SEMANTICS AMENDMENT: read-corroboration OUT of the confidence tier
  (owner-ratified ruling + Addendum A).** The tier now certifies ONE thing — **how the NAV is
  BUILT** (traced resale-uniform basis, sourced NAV-driving figures, on-convention, known-gap
  surfaces immaterial). **A price movement may never change a tier**, which extends the ECO
  2026-07-01 doctrine ("VALIDATED-TIGHT means the NAV is SOLID, NOT that ECO is cheap") from prose
  into the gate. *Why the 6/30 wiring was wrong:* it accepted two-basis read-AGREEMENT as internal
  corroboration "of comparable force" to a broker cross-foot — but a broker cross-foot is
  **estimate-level** (their NAV vs ours) while read-agreement is **call-level**, a function of
  where the price sits. The two coincide only at deep discounts, which is why the flaw stayed
  invisible until SBLK drifted into the seam. *The reductio:* SBLK's 8/13 demotion was driven by
  the watchlist PRICE leg (25.20→28.60) crossing the hist-basis cheap|fair boundary at **$27.72**
  with tool NAV byte-identical at $32.78 — and with the tape at $27.89, **0.62% above the
  boundary, a 62 bp red open would have UPGRADED the grade** hours after a data repair degraded it.
  `robust` therefore LEAVES the tier and ships beside `weight_sign_stable` as the
  read-corroboration line (the TNK precedent: the tier does not double-count it). The 2026-06-29
  sizing seam is amended — construction failures cap via tier, read-flips caps independently, and
  **where both bind the SMALLER authorization applies; the two never stack** as a repeated discount
  penalty. **ADDENDUM A (owner ruling, raised by the implementing agent before any code changed):**
  simulating the drafted §1 showed it promoted FIVE names, not three — BRUT and CAPT ride on
  `robust = "n/a"`, which is not read-agreement at all but the §17 multiple being *blocked* by the
  newbuild-heavy guard. Ruled: **TIGHT gates on EVALUABILITY, never on agreement.**
  `confidence_tier` takes `read_blocked` (the blocker's label, else None); a name whose multiple
  cannot be produced is a CONSTRUCTION defect and stays GOVERNED-WIDE, so BRUT's same-day
  going-concern ruling and CAPT's `newbuild-heavy` subreason both stand. Supporting finding:
  **every blocking guard in `evaluate()` is price-INDEPENDENT** — only the cheap/fair/rich read is
  price-dependent — which is what lets `read_blocked` stay in the tier without reopening the hole.
  Shipped with it: the **§17 margin block** finally reaching paper (`J_par`/`J_hist`, per-basis
  boundary PRICE, signed `flip_margin_pct` — the table previously printed the verdict of the
  comparison but never the numbers compared), and a **governed `read_flag`** with a
  `READ_FLAG_HYST_PCT = 2.0` deadband so a name parked on a boundary reports one stable sizing
  input instead of strobing (governance consumes `read_flag`; `robust` is display). Guards:
  `test_tier_is_price_invariant` (regression **SBLK-2026-08-13**; ±20% price-only perturbation,
  every tier byte-identical) — which is ALSO the standing guard on future blockers, since any
  price-dependent guard later added to `evaluate()` reds it — plus a companion asserting the
  perturbation actually MOVES the reads so the invariance test can't pass vacuously, and a guard
  that `read-flips` can never re-enter `TIER_SUBREASON`. Regen: **{SBLK, CMDB, GNK} → VALIDATED-
  TIGHT** each carrying `read_flag = flips`, 22 of 25 rows unchanged, **edge-cleared long set {SB}
  before and after**, **drift gate 0 UNEXPLAINED / +0.0pp / +0.0% on all 25 rows** — the amendment
  relocates a label without moving a number. Handoff JSON 2.7→**2.8** (additive). Record:
  `decisions/tier_semantics_amendment_2026-08-13.md`; governance TRADE_PREREG #4 rewrite routed
  SEPARATELY (§6) and `read_flag` must not enter any prereg gate until the RATIFY_LOG entry exists.
  Two items carried to the owner: the edge-cleared filter gates on `read_flag == "robust"` rather
  than §4's literal wording (which would have admitted TNK — robust, raw-BUY, but rich/rich and
  `POSITION_UNRELIABLE` — enlarging the actionable surface against §7); and the §17 margin measures
  the **watchlist vintage** price the read is computed on (SBLK +3.18%), not the tape (+0.62%), so
  **the live surface does not currently flag the strobe zone the deadband was written for.**
  **ADDENDUM B (owner, 2026-08-14) ruled both.** *B1:* the edge-cleared filter is RATIFIED —
  §4's literal wording was defective because **`robust` is agreement and agreement is symmetric,
  while actionability is directional**; operative definition is TIGHT ∧ `read_flag == "robust"` ∧
  `read == "cheap"` ∧ BUY. That named the **parity/headline** basis, which corrected the landed
  code: it had shipped on `read_hist`. Moot under an *instantaneous* robust (the bases agree), but
  `read_flag` is **governed** — inside the deadband it holds "robust" while the reads have already
  separated, and there the two conjuncts return opposite answers. Now pinned by a test built from
  SBLK's real J's. Whether `POSITION_UNRELIABLE` becomes an explicit conjunct is DOCKETED, not
  ruled — moot while the read excludes TNK, live the day a name is robust-cheap and weight-fragile.
  *B2:* margin vintage RATIFIED as built and **no second scorecard column** — the scorecard is a
  single-vintage surface and a tape-basis margin beside a watchlist-basis read would re-create the
  k-vintage mismatch the 8/07 rebase retired; the tape view routes to the **delta/monitor layer**
  as its own chip. *B3:* RATIFY_LOG correctly withheld. *B4:* the state-write fix is elevated to
  **doctrine** — governed state is writable only from the production entry, never a library call a
  test can reach. Recorded in CLAUDE.md by GENERALIZING the 2026-07-18 "read-only agents must not
  run pytest in the shared tree" line into one field-general rule ("a run must never write SHARED
  state") rather than appending a fourth instance — router held at 15,980 of its 16,000-char
  budget, cap not raised.
- **2026-08-13 — JULY ARCHIVE-HOLE AUDIT (owner-directed backfill): NOTHING TO BACKFILL —
  attribution corrected + full-window name sweep.** The 7/03→7/14 Pareto gap that hid the BRUT
  7/07 chain is SOURCE-QUIET (Pareto's Jul/Aug cadence; the owner's 7/12 seasonal note in
  `rocketchat_sources.yaml` covered it, recorded during the window), NOT an un-backfilled ingest
  outage: a full RC history walk (uncapped, since 7/01, 2,379 msgs) shows zero Pareto-lane posts
  7/04–7/13 while the sibling FFA lane ingested daily (7/06 arrivals on disk); the archive equals
  the channel exactly for 7/01→8/13. The "harvester outage" was the weekly broker-marks lane (one
  missed Saturday, revived 8/11 with W32/W33) — and a deep 40-page HSN+CapitalLink recrawl (1,449
  raw issues) recovered NO July-window weeklies either: per-broker scatter (advanced W29, banchero
  W28, fearnleys W27+W29, intermodal W28) against healthy July crons = mirror-side non-publication;
  allied confirmed dead in 2026; W33 banchero+fearnleys were the only pickups. Remediation
  therefore shifts to the surviving causes — untriaged name-text and NO ISSUER-RELEASE CHANNEL
  (Oslo NewsWeb) for non-EDGAR names. Executed: manifest rebuilt (→8/13), `--names all` sweep over
  issues 7/14→8/13 (mention files kept OUT of the tree, scratchpad-only), 15 decision logs given
  dated triage entries; two OPEN PRINT FLAGS recorded, not promoted (FRO 2×2017 VLCCs — priceless
  as yet; CMBT 'Bristol' suezmax — beyond the 8/07 print cursor, expected in the 8/15 queue); the
  7/20 unnamed prints verified already dispositioned (8/09 round). No regen run; `prices_daily.yaml`
  untouched. WORKFLOWS §Report-day clause + PLAN 8/13 AM block corrected; brut_log carries the
  audit record.
- **2026-08-09 — THE PROMOTION MEGA-ROUND (owner-authorized) + STAGE A RULED.** Three
  data events in one session, each with its own record/gate cycle: **marks-trail**
  (28 in-window S&P prints incl. three war-tape VLCCs $120-130M @ 9-13y; 4 unnamed-print
  DUPLICATES caught by the suezmax round-trip guard + dedupe review — Jag Lokesh /
  WF Artemis / Wooyang Belos / TNK Singapore Spirit were all re-reports; new WORKFLOWS
  rule: sweep the class file before promoting any unnamed print; k_broker pure-play
  premium collapsed to ~1.00-1.04 → TXN_PURE_PLAY_K_BAND re-pinned (0.95, 1.15));
  **dry-bulk FFA 8/06** (tenor set ROLLED → 12M proxies stepped down on window
  composition, the Q1-27 trough entering — like-for-like Q4 firmed +4.3%; SBLK
  BUY→HOLD band-mech was purely 12M-composition → FROZEN-FOR-OWNER-REVIEW);
  **containers MB W32** (Ctr-Large 64,000 + feeder 10yr 29.5 — TC+value joint,
  NAV-halt verified, MPCC +0.5% only). Vintage-coherence guard forced the same-round
  multi-promotion as_of restructure (newest event = default, older = explicit holds);
  the hygiene guard forced the family-diagnostics re-run (weight_sign_stable nulls).
  **Stage A computed to the frozen prereg's letter** with the §5 breaches investigated
  (both trace to ECO's verified $206.6k QTD print; the bands pre-date the 7/20
  blockade escalation) and **FOUR OWNER RULINGS recorded**: wait-for-INSW (wires
  8/10) · breaches accepted · VLCC 12M = Mount Horizon $105,700 single-print ·
  LR2_clean term = §4-letter 28,000 flagged. INSW pre-registered ($56.30 point,
  [51.50, 61.00]); the watchlist consensus-pair rebase transcribed from the 8/7
  daily and STAGED as a draft. Records: marks_trail_triage_2026-08-09.md ·
  ffa_promotion_2026-08-09.md · container_mb_refresh_packet_2026-08-09.md ·
  stage_a_computation_draft_2026-08-09.md · insw_q2_prereg_2026-08-09.md.
- **2026-08-08 — THE Q2 TRANSITION EXECUTED (block 1: SB/TNK/ASC) — the 7/31 half-application
  arc CLOSES on paired inputs.** Sequence per the owner-ruled split: guards commit → price-absorb
  ratify (8/07 tape, ΔNAV 0.0 all rows, 4 flips eyeballed) → transition on the frozen tape.
  Manifests restored from 3cd0f46^ WITH pins (SB scrubber 20→19, provenance), SB `report_date`
  bumped WITH its sheet this time. Preflight CLEAN at 2026-Q2 → run → **forward invariance HELD:
  all 22 lagging names printed delta 0.0 in every column** (the laundering signature is absent).
  All three pre-registered bands HIT: TNK $77.73→$84.60 (+8.8%, predicted +8-9% — the VOIDed
  artifact said $81.48) · ASC $17.82→$17.37 (−2.5% vs predicted −2.9%, SIGN-OPPOSITE to the
  +16.9% artifact, the $183.6M commitment now visible in the breakdown) · SB $10.07→$10.03
  (−0.4%; **the 7/31 band miss VANISHES on paired inputs** — cause re-classified to the
  half-application, NOT the young-Pana anchor; the curve question stays in the ladder review on
  its own merits). Both-halves consumption verified in each fv_report. Baseline ratified.
  **TNK tier correction:** the 7/31 GOVERNED-WIDE·read-flips entry was computed ON the artifact
  (family 2×HOLD/4×T/S at FV $76.95); on paired inputs the family reads 5/6 HOLD, §17 robust —
  **TNK stays VALIDATED-TIGHT** (6th TIGHT), fragility carried by weight_sign_stable=False.
  Tests learned to roll with the book: tests/conftest.py BOOK_QUARTER (committed-scorecard
  quarter) replaces hardcoded run-quarter constants across 15 test files — the pair guard fired
  at collection on the first roll, proving the class the vet's advisory predicted.

- **2026-08-08 — Q2 TRANSITION MECHANISM RULED + LANDED (closes the 7/31 blocker; full record =
  the Decision block in `decisions/q2_cluster_transition_2026-07-31.md`).** Owner ruled BOTH fixes,
  then vetted and adopted the "Vintage Coherence v2" proposal as amended (5-agent adversarial vet,
  `wf_56a55a2a-f74`). Landed in one guards+tests commit, deliberately SPLIT from the transition
  itself (sequencing: this commit → price-absorb Q1 regen → Q2 block on a frozen tape, with the
  forward-invariance check: lagging names must print delta exactly 0.0 at the roll). The pieces:
  loader-vintage fallback (`resolve_balance_sheet_path`, newest-at-or-before, self-reporting, never
  forward) · pair guard in `load_company_inputs` (manifest label must equal the RESOLVED vintage) ·
  all-names preflight in `pipeline.main()` (fail-before-writes, F-6 pattern) · mislabel hard-fail +
  repo-wide sweep test · scorecard Balance-sheet-basis header + `balance_sheet_basis` +
  `names[].balance_sheet_vintage` (schema 2.6→2.7, consumer wired governance-side same day) ·
  provenance-at-ingest trio (`source_url`/`retrieved_at`/`filing_period_end`) required on sheets
  keyed ≥2026-Q2 · `add_ticker --quarter` REQUIRED as the FILING's vintage (the run-state default
  manufactured coherent-but-false labels) · `pipeline`/`overlay_ledger` no-arg quarters derive from
  state (the hardcoded `2026-Q1` was a post-transition crash in waiting) · overlay_ledger §15/§12.6
  routed through the same resolver (its newest-wins glob was a SECOND instance of the
  half-application shape — staged future sheets leaked into the dividend-window computation; also
  fixed its `[a-z]+` regex silently skipping 2343) · `scripts/check_snapshot_advance.py` as a
  WARNING for the one pattern the pair guard can't see (snapshot advanced, label not bumped —
  fitted on the single observed instance f8809d0, so no enforcement authority; the report-day
  checklist line is the higher-confidence half). Mechanism C as proposed (any content change ⇒
  report_date bump) REJECTED on evidence: 22/23 content-only manifest commits in history were
  legitimate within-quarter work. Staleness ceiling DEFERRED with a recorded shape (cadence-aware,
  never a loader crash — 2343 semi-annual false-fire + the loud-over-refuse precedent). A post-vet
  adversarial diff review caught 3 defects pre-commit (add_ticker's template substitution born-
  mislabeled regression → whole-line regex + stub parse test; the `missing` disclosure lane dead on
  arrival → summary computed over the WATCHLIST, not surviving rows; the snapshot-advance detector
  blind to flow-style manifests → mid-line age regex, smoke-verified on a synthetic TNK shift) and
  the diagnostic scripts' hardcoded `2026-Q1` (now `current_book_quarter()`). Suite 611→627 green +
  15 xfailed; the preflight test pins the real staged state (exactly {ASC, SB, TNK} flagged at
  2026-Q2).

- **2026-07-31 — STALE-RUN GUARD SHIPPED (closes the GUARD OWED in the entry below).** Freshness-gate
  fallbacks are now counted per run (`loaders.stale_price_fallbacks`, the `stale quote` subset only —
  flagged and never-fetched names are other disclosure lanes); at >= `STALE_PRICE_ALERT_MIN_NAMES` (3,
  `price_refresh.py`) the run goes LOUD instead of silent: a banner LEADS `outputs/delta_report.md`
  (above any flip line), the scorecard price_basis header screams above its quiet STATIC-FALLBACK
  disclosure ("flips are presumptively PHANTOM"), and the pipeline prints the alert to stderr at the
  delta step. Chose loud-banner over refuse-to-run so a deliberate offline regen stays possible —
  escalate to a hard refusal only if the banner ever gets ignored. Handoff schema 2.5 → 2.6
  (additive: `price_basis.stale_fallback`). Guards: 4 in test_price_refresh (synthetic 7-day-old
  vintage end-to-end into `price_basis_summary`), 2 in test_delta, 2 in test_scorecard. Suite green;
  fresh-price runs render byte-identical.

- **2026-07-31 — STALE-PRICE SILENT FALLBACK (caught same hour; artifact outputs discarded
  uncommitted).** The B' regen ran while the committed `prices_daily` vintage was 7 days old
  (the laptop-shut week: daily refreshes wrote the file but nothing committed it, and the
  revert-before-regen rule discarded them) — the loader's overlay freshness gate silently fell
  back to `watchlist.current_price` values dated Jun-26/Jul-3, producing phantom BUY flips
  (TNK/STNG/ASC) on month-old prices. Caught because the flips contradicted the live IBKR
  tape (SB $6.39 vs $7.81). Fix-of-the-day: fresh 7/31 vintage fetched + deliberately
  committed FIRST, regen re-run, artifacts discarded. GUARD OWED (task-flagged): a regen
  where >N names fall back past the freshness gate should refuse or go loud in the delta
  header — a silent basis swap during an FV-moving event is exactly the §10 mixed-basis
  class of error. Also of note: B' executed same day (see the reweight commits) after the
  7/29 mediation watch surfaced a THIRD state (pause-without-talks) the pre-registration's
  binary didn't name — successor trigger now carries three explicit branches.

- **2026-07-28 — DECISION-LOG AUTO-PREPEND ANCHOR FIXED (the 2343 mid-file quirk flagged at
  71e7020).** `delta.prepend_decision_log_entries` anchored on the first `---\n`, which is the
  preamble separator only in AUTO-founded logs; a manually-founded log (2343 at its 7/14
  onboarding) has its top entry above any `---`, so every auto entry landed mid-file, breaking
  the newest-first contract `drift_gate.decision_log_annotated_since` reads by (it consults only
  the first dated header — 2343_log had to be hand-reordered 7/28). Now the prepend inserts
  immediately before the first dated `## YYYY-MM-DD` header (preamble stays above; entry-less
  files get the entry appended). The header regex moved to `delta.DECISION_LOG_HEADER_RE` and
  drift_gate imports it — writer and reader share one definition per the incidental-identity
  rule. Guard: `test_decision_log_prepend_lands_above_manual_top_entry`; auto-founded logs
  verified byte-identical old-vs-new. Suite 603 green.

- **2026-07-27 — SCHEDULED RC INGEST WEDGED 3 DAYS BY THE NEW LANE'S BOOTSTRAP (fixed; sentinel
  FETCH-FAILED caught it).** The 7/24 `baltic_capesize_table` bootstrap walked unbounded — TWO
  stacked bugs: main()'s cursor precedence put `None in cursors` ahead of `--since` (a cursor-less
  source silently discarded the bound), and the RC API silently ignores an `oldest` it can't parse
  (hand-typed second-precision ISO), so nothing bound the walk server-side either. It hit the WO2
  1.1 sanity cap, exited 3 WITHOUT persisting the cursor, and every scheduled run after (Sat
  news-pull, Mon daily) refused at the CURSOR-RESET guard. Fixed both layers (`_decide_oldest`
  precedence + client-side bound enforcement in `iter_history`), seeded the cursor via a bounded
  walk (55 msgs), caught the weekend backlog (3 FFA images, Baltic rows through 7/24), 3 regression
  tests (`tests/test_rocketchat_api.py`). Suite 602 green. The guard chain WORKED as designed —
  fail-loud, no cursor corruption, no silent re-crawl; the cost was 3 days of staging lag, all
  recovered.

- **2026-07-26 — WEEK-CLOSE (the 7/20 week): collapse-recorded + two promotions + sender
  reshuffle + batch ratify.** The week's arc: (1) **Doha round-3 COLLAPSE recorded** 7/22
  (MoU declared dead by both principals; no reweight — pre-registered branch;
  `crude_ceasefire_mediation_watch` armed 7/29) and the **MoU-scenario reweight RULED same
  evening** (owner: "Rule A - conditional B′" — no reweight now, B′ 0.25/0.57/0.05/0.13
  FROZEN + pre-registered on the 7/29 watch's collapse branch; Aug-16 stays the full
  re-derivation venue). (2) **Container W28/W29 promote** 7/22 (Ctr-Feeder 24,250, NAV
  frozen verified). (3) **RC sender reshuffle** absorbed 7/24 (entry below). (4) **First
  Palun-vintage FFA promotion** 7/24 (entry: ffa_promotion_2026-07-24.md — 100% of OCR
  misreads inside flagged rows; Supra Cal27 held-node bracket). (5) **Hynix print re-dated
  7/29** (issuer 6-K) + GOOG capex-raise logged as G4 1-of-4 (governance side). (6) **GNK
  tender census**: offer expired 7/24, outcome PR pending Mon 7/28. (7) **Week-close batch
  ratify** @ a46eda7 (RATIFY_LOG 2026-07-26T21:24Z): 7/21+7/24 price vintages + both
  promotes; FIVE flips eyeballed individually — SBLK BUY→HOLD **price-at-FV** (the model
  and the governance $28 take-profit agreeing: the discount leg is spent; SB back to the
  lone TIGHT BUY), GNK tender-pinned recross, ASC/GSL/2343 shallow crossings. Suite 599 +
  15 xfailed; gate 0/0. Lesson added to CLAUDE.md: revert prices_daily before promote
  regens (bit twice this week).

- **2026-07-24 — RC CHANNEL SENDER RESHUFFLE ABSORBED (three lanes; the 7/22 STALE-INPUT was
  a sender change, not a quiet channel).** Owner intel + channel inspect: the dry-bulk FFA
  widget screenshots moved Joeri.van.der.Sman → **Chris.Palun** (~7/19-20, phone captures);
  the full Baltic-5 panel returned under NEW sender **Big_P** (7/20 →, diff-fenced fixed-width
  format); **CPLazos** posts a daily official Baltic Capesize panel (BCI + routes $/day +
  C5TC-182 $/day). Wired: (1) ffa_drybulk accepts both senders, `single_sender` retired;
  (2) baltic parser extended for Big_P's format ("Shipping Indices" header, colon-less
  panel lines gated on change+percent columns, explicit textual date) + ingest now reads
  upload-caption text from attachment descriptions (Palun's capesize lines ride his image
  posts — invisible before); silence_days 10→3, dormancy-override premise retired;
  (3) NEW staging-only lane `baltic_capesize_table` (CPLazos, no consumer — the C5TC $/day
  average is the §18.5a-blocked series; determinant wiring = owner ruling; bootstrap pulled
  his archive to early May); (4) **ffa_ocr layout detection**: Palun's phone captures STACK
  the three panels vertically — header y-band assignment added (x-third fallback unchanged,
  ≥2 anchors required); the pre-fix mis-bucketed 7/20-24 db entries dropped + re-parsed
  (bucketing verified against the source image; residual digit-misreads honestly flagged,
  promotion stays owner-run). Backfilled via `--since 2026-07-18`: 10 FFA images, Baltic
  rows 7/20-24 (Big_P panels + Palun capesize). Suite 596 green (+3 parser/layout tests).

- **2026-07-20 — EDGAR POLLER STAGES EX-99 EXHIBITS (the BWLP cover-only gap).** The poller
  staged only each filing's PRIMARY document, but a 6-K/8-K's substance lives in exhibit 99.x:
  BWLP 0001213900-26-078478 (filed 2026-07-16) staged the 9KB 6-K cover while ex-99.1 carried
  the Product Services Q2 pre-announcement (net −$31M) — fetched by hand 2026-07-18. Now: for
  each new accession the poller also fetches the accession's `-index.htm`, stages every row
  whose Type matches EX-99* under the same `{accession}_{form}_{filename}` convention, and
  records them on the manifest line (`exhibits: [{doc, type, staged_path}]` — additive key;
  sentinel reads via .get, unaffected). Politeness preserved: same UA/spacing seam, exhibit
  downloads count against MAX_DOCS_PER_RUN; exhibit DETECTION is never capped (cap-exhausted
  rows land manifest-only, the primary-doc convention). Primary-registered-as-exhibit rows
  skipped (no double-stage); iXBRL `/ix?doc=` hrefs handled. Row shape verified against the
  live BWLP index page. Guards: test_ex99_exhibits_staged_and_manifested,
  test_exhibit_detection_never_capped_staging_is, test_dry_run_fetches_no_archives.
- **2026-07-15 — TEN FULL BALANCE-SHEET RECONCILIATION (ninth of the pattern; pre-registered @
  ce65da4, both bands HIT).** Requested by the governance sizing analysis (TEN card gate ii).
  The 6-K's OWN condensed Mar-31 balance sheet — which the 2026-06-05 onboarding log had already
  extracted — had never been wired into the YAML (estimates shipped instead): advances
  $400M[EST]→$442.740M (6-K BS line; the $128M 20-F-to-data-kit range resolved $42.7M ABOVE book) ·
  WC $28M→$174.654M composite (basis validated at Dec-31: 27.9≈28.2 — the +$146.7M Q1 swing is real:
  Ulysses HFS reclass, $36M securities, EUA/receivables) · debt $2,148.2M→$2,136.109M (BS net of
  deferred finance costs). NEW: Mare Success NCI $45.954M netted via preferred_equity (49% Polaris/
  Flopec, 20-F Note 11 — the manifest's dangling "49% FLOPEC JV counted at full" note finally
  resolved; BWLP convention). MANIFEST: 4 not-owned hulls removed — Ulysses (sale MOA Jan-22-2026,
  20-F Note 17(c); HFS at carrying inside the WC composite; $83M free cash lands H1),
  Arctic/Antarctic/Sakura Princess (ASC-842 TRUE-SALE SLBs — RoU-not-vessel on the audited BS;
  the prior YAML note "Antarctic expired during Q1" was wrong [term to ~Jun-2026]; Arctic+Antarctic
  repurchase agreed Apr-7 → re-add OWNED at H1). Net: headline NAV $88.76→$87.35 (−1.6%), base
  $97.01→$94.58, PW FV −2.0%, BUY intact — the STNG plausible-but-wrong pattern again (±$244M of
  opposing errors netting small). ten LEAVES the figure queue; STAYS OFF_CONVENTION (19-hull NB
  program on delivered=contract; §9.6 wiring = owner decision) + OPERATING_SCRUBBER (no issuer
  aggregate to cross-foot — data-kit callouts only). Owner forks in the prereg §6 (NCI basis /
  Ulysses value / SLB convention / WC composite). Deliberate re-pins: test_scenarios preferred
  333,282; test_manifest_provenance + provenance.py queue sync. Baseline re-ratify OWNER-GATED,
  not executed. Record: decisions/ten_reconciliation_prereg_2026-07-15.md + ten_log 2026-07-15.
- **2026-07-15 — §9.10 FAMILY-RANGE CONTAINMENT GUARD (TEN ev_pct +45.0 printed against its own
  family max +44.9).** The handoff printed a point EV OUTSIDE its weight-family range: the WO1-F4
  basis stamp scopes only scenario_inputs.yaml, but the MR age-0 re-anchor (5ed418f) moved TEN's
  PW FV $57.60 → $57.64 (+0.1pp EV) with the sidecar held at the prior marks. The family DOES
  include the adopted set (Set A again since the 7/14 Hormuz restore), so containment is the
  intended invariant and the out-of-range print was a vintage artifact, not rounding. Guards
  (over prose): (1) the scorecard emit now WITHHOLDS a name's family fields when its live point
  EV (1-dp, as printed) exits the sidecar range — null + `weight_family_basis.ev_lagging` +
  banner, never silently out-of-range (schema 2.4 → 2.5, additive); the S-2 coverage guard then
  reds until the family script re-runs at the current tape. (2) `handoff_coherence_flags` gains
  the containment check — EXACT, no tolerance (both sides share the 1-dp rounding) — so the
  committed-surface test AND the sentinel enforce it on every shipped artifact. (3)
  `crude_weight_robustness.py` asserts the adopted scenario_inputs weights ARE a family member
  before running (the containment premise), and Set E's stale "current locked" label is
  corrected (production prior = Set A). Crude sidecar re-run at the current marks: TEN
  26.5/44.9 → 26.6/45.0, every other name byte-identical. (The same-day TEN balance-sheet
  reconciliation recompute then moved the point EV to +42.0 — INTERIOR to the range, so
  containment holds; the guard fires on range exit, not interior drift. Fold a family-script
  re-run into the post-reconciliation clean-HEAD regen so the recorded range re-anchors.)
  Consumer note (TRADE_PREREG #4 reads these fields fresh): null family fields + `ev_lagging` =
  "re-run the family diagnostics before sizing". Also caught in passing: the committed surface
  at 5ed418f stamps `9869336-dirty` —
  it already reds the WO1-F1 guard (pre-existing; the `_vintage_stamp` docstring still blessed
  committed '-dirty' stamps and is now corrected); regenerate from clean HEAD at the next
  chore(outputs) round.
- **2026-07-18 — WEEK CLOSE (Jul-13 → Jul-18).** The 5-step checklist run end-to-end (owner
  "Yes"): **(1) doc audit** — 5-agent read-only fan-out; fixes applied: METHODOLOGY (TEN §6
  restated to the reconciled figures; §15.3/§15.7 vintage-flagged; §11.5 Handysize 44.9
  restatements ×3; §9 decision-1 marked resolved-by-D-M4; schema pin → 2.5; Handy-Bulk alias
  note; §18.2 LR1 no-parity split; §1 coverage → 25/6; §17.7 APPROX list synced; **Appendix A
  Week entry added**), CLAUDE.md (Handy-Bulk dwt baseline added; two rotting counters dropped),
  TICKER_NOTES (13 patches: TEN/GNK/TRMD restated, CAPT/CMDB/GSL/BRUT/MPCC/SB/CCEC/STNG/INSW
  dated lines, 4 missing entries added [CMBT/2343/LPG/BWLP]), README (schema 2.5, tables +6 rows
  + LPG table, B4 semantics, dead counters), LIMITATIONS (APPROX seven→nine, TEN vintage-flag,
  MB-container (a) CLOSED, §4 restated post-P1c). **The audit's material catch: the RATIFIED
  13-Jul spot re-proxy §3 was never wired** — applied (Cape 36,000 / Pana+PPMX 20,000 / Supra
  19,050); dry-bulk band-mech flips CMDB HOLD→BUY · GNK TRIM/SHORT→HOLD · SBLK HOLD→BUY (all
  price-inside-interval per D-M5, logs annotated with BOTH causes). **(2) verification gate** —
  suite 587+3skip+15xf green · backtest 13 · pipeline clean · reconcile 25×SANITY-OK · drift
  gate **0 UNEXPLAINED / 17 explained** (the 7/17 price vintage ×16 annotated EV-only ΔNAV 0.0;
  batch baseline ratify = the owner's next deliberate step, now carrying both causes).
  **(3) PLAN rewritten** (2026-07-18 state + the Week-of-7/20 theme: Q2 intake + Stage-A basis
  accumulation). **(4) clean git** with this entry. Also: baltic_indexes staleness probed →
  **SOURCE-QUIET + a text→image format drift** on the capesize lane (silence_days 3→10 dated
  override, the pareto summer-override pattern; owner eyeballs the three images); the sentinel's
  other 7/18 flags all dispositioned same-day (MoU check recorded; 3 filings triaged).
  **Process catch for the rulebook: a "read-only" audit agent ran the suite in the shared tree
  and stashed collateral, sweeping the session's annotations — recovered deterministically;
  audit agents get worktree isolation or no state-mutating commands next time.**
- **2026-07-15 (close) — THREAD (d) SIGNED (owner verbatim: "sign thread (d) as confirmed") —
  CLOSED.** §4 consequences executed: STNG's 2-VLCC §9.6 gate formally lifted (wiring = its own
  prereg, post-Stage-A; stng_log annotated); the live "level-provisional" VLCC language retired
  (provenance.py BRUT rationale now reads two remaining legs — cash-pending-H1 + going-concern;
  historical records left as written); PLAN P1(d) marked signed. Zero numbers moved. With the
  same-evening LR1 ruling this closes the day's arc: every P1c/thread-(d) decision is now either
  EXECUTED (MR), SIGNED (thread d), or FROZEN-scheduled (LR1 + extract refresh, post-Stage-A).
- **2026-07-15 (late evening) — LR1 FORK RULED (owner verbatim: "rule the LR1 fork — taxonomy
  (b) + contract-floor, post-Stage-A"); execution prereg FROZEN — TRMD → VALIDATED-TIGHT is now
  scheduled work.** Fork (i): LR1 age-0 → the dated xclusiv Panamax-tanker NB contract floor
  (~\$61.0M; the lower of the two current contract prints, MB \$64M the cross-check) + 5yr →
  the dated intermodal mark (~\$60.0M) — marks re-dated at execution (freshness rule), method
  frozen. Taxonomy (b): NEW scoped status **`resale-corroborated`** — class-level
  qualification (no broker Resale line exists + dated contract floor + dated second-house 5yr,
  both current) with a per-name honesty rule (uniform-equivalent iff every hull the name holds
  in the class is age ≥10 — the wired nodes only touch ages <10; guard-tested so a young hull
  arriving auto-degrades the name). LR1 is TODAY the only qualifying class (Handysize/Handymax/
  VLGC all fail the two-mark requirement — the status self-limits). Predicted movers verified
  through compute_nav AND hand interpolation (agree to the cent): INSW +\$7.80M (+0.27%, its 3
  young hulls; nav_basis stays honestly pending), TEN +\$1.17M (+0.04%, the age-9.5/9.6 pair),
  TRMD + HAFN **exact zero = the controls**. At the round: TIER_SUBREASON TRMD basis-pending
  removed → **VALIDATED-TIGHT (the 7th)**, with two registered boundary checkpoints (LR1 sleeve
  = 8.7% of fleet value vs 2343's 51% cap comparator — sub-material; the W-frag sign-instability
  eyeball). `newbuild_contract` LR1 stays OMITTED (contract-vs-contract parity is degenerate;
  not worth weakening the resale-invariant HALT — reverses the earlier PLAN note). Execution:
  post-Stage-A anchor round, folded with the extract-refresh rider (one attributable step).
  PRE_REGISTRATION_LR1_CONTRACT_FLOOR.md; ruling annotated in lr1_level_evidence_2026-07-15.md.
- **2026-07-15 (evening) — THREAD (d) CONFIRMED-CURRENT + P1c MR CLEARED TO RESALE-UNIFORM;
  LR1 fork staged (three frozen packets, one NAV-neutral-scale wiring).** The 2026-07-13
  xclusiv weekly (in-repo via the harvester) confirms every wired crude Resale anchor within
  the Thread-1B ±2% (VLCC 175.0 EXACT — passes the BRUT ±0.5% carve-out; Suezmax +1.49%;
  Aframax/LR2 0.0%), label-verified ("prompt delivery ex yard"), independently corroborated
  by advanced W28 — thread (d) has NO remaining open question
  (decisions/thread_d_crude_level_confirmation_2026-07-15.md, owner sign-off pending);
  STNG's 2-VLCC §9.6 portion un-gates in principle, wiring queued post-Stage-A. Same issue
  RESUMED the MR2 secondhand line (dropped since 2023Q4): the \$54M exception confirmed −1.8%,
  age-0 re-anchored to the resumed Resale \$55.0M, **MR → resale-uniform** (XCLUSIV_WIRED +=
  MR; exception retired). Prereg predicted TEN as the SOLE mover (+\$1.94M = +0.07%, 2 young
  MRs) — landed to the cent, drift gate 25/0 UNEXPLAINED, suite 588+16x, no re-ratify
  (decisions/mr_secondhand_resumption_2026-07-15.md). Consequence: **LR1 is now TRMD's (and
  INSW's) LAST basis blocker**; the current intermodal W29 5yr (\$60.0M) exposes the wired LR1
  curve's inversion (age-0 59 < dated 5yr 60 < dated NB 61) — owner fork (contract-floor /
  uplift / hold) + the resale-uniform taxonomy question (whether TRMD can EVER reach
  VALIDATED-TIGHT on current broker coverage) staged FV-moving post-Stage-A
  (decisions/lr1_level_evidence_2026-07-15.md). Advanced W28 MR Resale \$60 (+9% house spread
  vs xclusiv, 5yrs agree) recorded as a divergence footnote, not blended. Handymax: the 07-15
  five-broker sweep re-confirms NO product-Handy/Handymax secondhand line exists anywhere.
- **2026-07-15 (later) — THREAD-1A PRODUCT-HANDYSIZE CONTAMINATION CORRECTED (owner:
  "Execute"; zero-impact window beaten — ASC reports Jul-28).** The Thread-1A \$36M product
  age-0 was the xclusiv BULK row (section-mislabel; cache-proven). Source hunt exhausted:
  NO broker tabulates product-Handy secondhand (xclusiv/MB/Intermodal all stop at MR) →
  age-0 re-sourced to the only real dated product-Handy mark: ASC's issuer-filed April-2026
  contract \$44.9M/hull (acc 0001104659-26-056715). basis_status pending-sourceable;
  AGE0_BASIS dated exception; product Handysize OUT of XCLUSIV_WIRED (the guard had been
  enforcing the contamination); the xclusiv extract row RENAMED Handy-Bulk and read
  directly by the dry class (alias retired — the mislabel is now impossible by
  construction). Bands registered ahead + VERIFIED: zero live NAV movement (drift 25/0/
  stable); forward: the ASC Q2 NB entry corrects ~+\$14M (~+1.9% ASC NAV) vs the
  contaminated basis. Record: decisions/product_handysize_resource_2026-07-15.md.
- **2026-07-15 — ALL FOUR METHODOLOGY DECISIONS RULED (owner: "Proceed as recommended") —
  D-M5 built same day; the rest sequenced behind Stage A.** D-M5 (the governance-load one):
  `fv_low`/`fv_high` = scenario min/max over weight>0 scenarios (0-mass tails excluded) in
  the Verdict table + book_scorecard.json **schema 2.4** + TickerSnapshot; the INTERVAL
  FLIP-TRIAGE RULE live in drift_gate.evaluate — a band flip with price inside the interval
  auto-classifies band-mech (no eyeball owed, gate green, absorbed at next ratify); an
  interval-EXIT keeps the full eyeball; pre-2.4 state falls back to always-eyeball.
  Guard-tested 3-branch. D-M2: Option B (leverage-adjusted r_e) ruled — sweep memo +
  adoption post-Stage-A; B′ deferred to the container refresh. D-M3: parity-denominator
  A/B pre-registration FROZEN (runs post-Stage-A; kill condition may legitimately scope it
  to txn-anchored sectors). D-M4: open decision 9.1 CLOSED — piecewise-linear ramp ruled;
  cycle.py stays frozen until the shared D1 adoption round with D-M3 (~late Aug). One
  FV-moving event in flight at a time: Stage A → D-M2 sweep → D1 round.
- **2026-07-14 (evening, second memo) — METHODOLOGY REVIEW (companion to the ops audit;
  `outputs/METHODOLOGY_REVIEW_2026-07-14.md`): M-1 + M-3-interim EXECUTED, four decisions
  STAGED to the owner.** The memo's core finding (arithmetic verified against the committed
  DHT report before acting): the blend's EFFECTIVE asset-value content is ~0.65-0.85, not
  w_nav — the strip terminal IS aged NAV — so marks/provenance work carries ~5x the FV
  leverage of strip-side rate refreshes. Executed (the memo's own no-ruling class): the
  standing **FV attribution** block in every fv_report (foots to blend FV, lock-tested,
  DHT effective-asset-share 0.84 reproduces) + §2.1 effective-structure paragraph +
  §2.3 cycle-denominator provenance table (the M-3 incomparability made visible at the
  point of use). RESERVED to the owner (PLAN decision block −1): D-M2 leverage-adjusted
  discount rate · D-M3 parity-denominator A/B (D1) · D-M4 continuous-ramp bands (D1,
  open decision 9.1) · D-M5 verdict FV interval + interval-exit flip rule (the one that
  retires shallow-flip eyeball load). M-6a/b registered for the next anchor refresh
  (M-6a is value-touching — bands-ahead discipline, not a same-day edit).
- **2026-07-14 (evening) — EXTERNAL AUDIT (clean-clone re-review @ 1d3db14): CLEAN, nothing
  above P2; all seven findings dispositioned same-day.** The audit verified from a cold clone
  on Python 3.12/pandas 3.0: 580 green, byte-identical pipeline regen, drift 0 UNEXPLAINED,
  the 2343 reconcile reproducing −2.0%, secret hygiene clean across all 297 commits, and all
  five prior P0/P1 fixes holding. Dispositions (`outputs/EXTERNAL_AUDIT_2026-07-14.md`
  addendum): N-1 pyproject deps rewritten to the REAL five + CI installs `-e .[dev]` (single
  source); N-4 push-trigger CI (sentinel job stays cron-only); N-5 harvester suite now a CI
  job; N-2 converted quotes 4dp (the sub-$1 2343 quantization); N-3 stale PLAN
  pending-ratify marker cleared + ratify_baseline.sh now greps for the marker (last-mile
  guard); N-6 ruff: 37 auto-fixes applied, 20 legacy cosmetics config-accepted dated, CI
  holds the line; N-7 README test count guarded by a census-band test (the F-9 class fully
  covered). Residual: governance consumer asserts schema major==2 — confirmed as-designed.
- **2026-07-14 (later) — 2343 (Pacific Basin) ONBOARDED — 25th name, first HKEX listing, first
  Handy-Bulk carrier (Stage-3 intake, owner-scheduled "before q2").** Four-YAML sourcing off the
  AR2025 audited 31-Dec-2025 snapshot (subsequent-events note FIRST — Note 27: Caravel agreement
  only) + the fleet page's per-vessel list RECONCILED to the AR class table exactly (58/48/1;
  zero 2026 owned-fleet movements; the AR's rounded class dwt includes NBs — resolved, manifest
  header). PRE-REGISTERED bands all passed first-run (2343_log): NAV $0.39 (band 0.36-0.44),
  SANITY −2.0% vs the ISSUER-COMPOSITE APPROX anchor (AR-published per-class broker values —
  the strongest APPROX basis in the book), k_broker 1.03, HOLD. Tier GOVERNED-WIDE·pending-anchor
  via the NEW `UNANCHORED_VALUE_CLASS_CAP` (a resale-uniform age-0 rollup must not over-grade an
  un-anchored mid-age class to TIGHT — registry empties at the class re-fit). Scrubber: AR
  aggregate "35 core Supramax" with no public per-vessel identification → all flags FALSE, a
  documented conservative omission (~2.5% NAV; deliberately NOT the untraced-true queue —
  XPASS-strict taught the distinction). Onboarding was provably inert on the book: every
  existing name's FV/NAV printed "no change"; the CMDB/SBLK BUY→HOLD flips were 7/14 tape
  boundary-crossings, eyeballed individually. Baseline ratify (2343 new + 10 EV%-only price
  rows) STAGED for the owner — Phase-4 designed-reds pattern. PANL deferred (owner; B3 email
  first, possibly post-Q2-block).
- **2026-07-14 — STAGE-3 INTAKE PREP + Handy-Bulk class (§11.7.11, Option B, owner-ratified).**
  Two blocks, same day. (1) **HKEX light-adapter DELIVERED (governance F-3 → met):** `hkex_poll.py`
  mirrors edgar_poll's invariants against the HKEXnews JSON index (stockId 7703 pinned; arrivals →
  `edgar_manifest.jsonl` `source: hkexnews`, so sentinel/draft-queue/commit_drift work unchanged);
  rides the hourly edgar-poll launchd row; live bootstrap 56 filings. 2343's conditional Gate-D
  PASS is now unconditional. Scaffolds: data_sources "2343"(quoted key)+PANL (CIK 0001606909
  verified vs company_tickers.json), calendar seeds (sentinel-inert), PANL B3 IR-query draft
  (governance-side, owner sends). (2) **Handy-Bulk wired gate-neutral** (2343 40.7% / PANL 23.5%
  Handy dwt): owner ruled Option B — static broker curve, un-anchored — after the print hunt found
  the Pareto archive holds ZERO dry-Handy prints (the sp_scan "one print" was a PRODUCT-tanker
  pair, corrected same day; the keyword matched tanker-section prose). Nodes = xclusiv 2026-06-22
  committed vintage (36/29.5/23.3/4.5 @38k dwt-scaled), 5-broker corroboration ±4%, 2343's own JNS
  contract $29.8M ≈ the NB node; **bands registered AHEAD and PASSED** (Dec-2025-vintage
  construction = 2343's issuer-published Handy composite +3.1%, Supra sleeve −5.8% — prereg
  `handy_curve_sourcing_prereg_2026-07-14.md`). Deck + ffa row + 12M TC: three derived/own-cadence
  surfaces, identity guard-tested (= supra × 0.90 locked; MB weekly TC 14.5k own vintage — the
  vintage-agreement guards caught BOTH integration gaps on the first run, working as designed).
  Re-fit trigger `handy_bulk_txn_refit` armed: the MB Dry Bulk weekly reports ~3 sub-45k prints/wk
  (22-print candidate table in the prereg) — Option A may arm by Q3; promotion owner-run.
  **FLAGGED, not acted:** Thread-1A wired this same xclusiv BULK row to the PRODUCT Handysize
  age-0 ($36M vs ASC's actual product-Handy NB $44.9M) — owner queue item, basis flags left in
  place, live NAV impact ≈ 0. Suite 583 green / 16 xfailed; drift 0 UNEXPLAINED.
- **2026-07-12 — HORMUZ RE-ESCALATION: pre-registered crude war-tilt RESTORED (trigger fired
  Jul-7/8, executed at owner go).** The sentinel's FIRST live run surfaced `crude_doha_talks_resumption`
  as overdue; the check found the strike leg had fired five days earlier — Iran hit 3 vessels near
  Hormuz Jul-7/8 (incl. the Qatari LNG carrier Al Rekayat), the US RE-IMPOSED the Islamabad-MoU-lifted
  oil sanctions + CENTCOM retaliation, transit threat 'severe' (decisions/doha_check_2026-07-12.md,
  sourced). Crude weights restored to the Jun-9 shape {escalation .25, pre_mou .45, mou_base .18,
  mou_bear .12} per the trigger's letter ("restore ... the SAME DAY" — 5 days late, the watch-layer
  install gap; the layer's first catch was its own blind week). Test re-pins: crude weights dict;
  INSW whole-co ~$57.15; TEN 3-sleeve ~$61.09; the DHT wnav-direction pin did NOT flip back (the
  Jul-2 semantic recalibration keeps PW NAV below base even war-tilted — direction depends on paths
  AND weights, documented). LNG/product deliberately NOT re-tilted (crude-only pre-registration; the
  LNG-Hormuz question flagged to the owner). Follow-up trigger `crude_doha_round2_outcome` armed
  (Jul-15). Same session: pareto_research silence identified as SEASONAL (silence_days 14 override,
  owner RC intel); WO2 install items 1-4 completed (D-2 closed) with NBSP/var-name/BWLPG.OL fixes.
- **2026-07-10 (later still) — owner decision #1b RESOLVED: v1 lock ruling = option (a), WO3 Phase 5
  CLOSED.** The 0/2 lock miss accepted as documented; lpg holds PROVISIONAL·v1-lock-miss
  (`SECTOR_V1_UNLOCKED`) until an owner-reviewed lock RE-RUN off the Dorian trio per-vessel splits —
  registered as sentinel-paged trigger `lpg_v1_lock_rerun` (due 2026-11-13; R-5 charter expiry
  2026-12-26 noted in its action). Precedent context recorded: dry bulk's v1 lock was 1/2
  FAIL-with-explanation (pre-WO3-letter, no cap); containers N/A-by-construction (GOVERNED-WIDE
  cap). WO3's definition-of-done is met on the "miss documented + sector held PROVISIONAL" branch —
  the charter's LPG half is delivered as an HONEST validation surface (charter B-4: a PROVISIONAL
  read is a legitimate outcome). Still open from the onboarding: the BWLP NCI convention review.
- **2026-07-10 (later) — owner decision #1 RESOLVED: baseline re-ratified ("accept both").** The
  Jul-6→Jul-10 price-vintage drift (12 names, ΔNAV 0.0% everywhere) accepted; LPG/BWLP added to the
  baseline (the last red test clears). Both band flips eyeballed individually per the
  don't-batch-accept rule (the DHT/FLNG 2026-07-01 precedent): GSL BUY→HOLD accepted as a shallow
  price crossing (unheld; Q2 FV rebuild due ~Aug-5 with the $917M NB order); STNG HOLD→TRIM/SHORT
  accepted as a price-position ARTIFACT, not a short thesis (PROVISIONAL·off-curve, handoff NO,
  weight-fragile −12.5…+1.2, +$9.6/sh un-wired §9.6 leg — full rationale in stng_log). Also fixed
  the stale provenance.py comment ("not one is a name-specific short" — CAPT/CMBT/STNG have printed
  as name-specific since the 2026-07-02 rework). Ratify row in RATIFY_LOG.md; human commit.
- **2026-07-10 — WO3 Phase 4 LANDED: Dorian LPG (`LPG`) + BW LPG (`BWLP`) onboarded; v1 lock MISSED
  0/2 → sector held PROVISIONAL (`SECTOR_V1_UNLOCKED`, a NEW tier cap).** Full four-YAML sourcing:
  Dorian off the FY2026 10-K (acc 0001596993-26-000025; fiscal 3/31 year-end = the 2026-Q1 snapshot,
  22 owned/bareboat hulls incl Cobra [sold 5/6 post-quarter, filed $81.9M net REPLACED the broker
  $83.5M print — the pre-registered vlgc.yaml watch item; the Jun-23 8-K trio (Corsair+2×2015,
  $256M en bloc, no split → no back-solve) corrected the old "Cobra inside the trio" note]; Japanese
  SLB financings INSIDE Note-10 debt $565.8M; the $148.7M chartered-in operating-lease book carried
  per the CMDB/SBLK convention — largest in the model, flagged); BWLP off the Q1-2026 6-K (acc
  0001213900-26-064314) + FY2025 20-F (39 hulls = 28 parent + 3 lease-financed [borrowings' "Lease
  financing arrangement" line — the Dorian-JP pattern] + 8 BW LPG India; the 30-May 8×Panamax-VLGC
  ~$940M order EXCLUDED as a subsequent event — the ASC/HAFN/TRMD pattern's 4TH instance; **NCI
  handled via preferred_equity $199.0M on a NAV-basis derivation** [India 48% at curve marks + PS
  19% at book] — no schema field existed; owner-review item, marks-dependent). Both reconciled
  **SANITY=OK** (−20.4% / −17.2% vs broker, k_broker ~1.2) but the **v1 calibration lock read 0/2
  within ±10% → per the WO3 letter the sector HOLDS at PROVISIONAL·v1-lock-miss**: new
  `SECTOR_V1_UNLOCKED` registry caps an unlocked sector's names at PROVISIONAL in
  `confidence_tier` (guard `test_sector_v1_lock_caps_tier_at_provisional`); both names also joined
  `POSITION_CYCLE_RELABEL` (1.59× war-elevated cycle → "rich · cycle position (not a short)") and
  `OPERATING_SCRUBBER_VERIFIED` ({LPG:16, BWLP:12} — per-vessel issuer columns at onboarding, the
  work-the-queue-at-onboarding rule). §9.10 family populated (both WEIGHT-ROBUST). §15 on the BW
  Group bloc (31.99%, Sohmen): N/A-gated at ~1.0x P/NAV, drop-down tripwires recorded, no haircut.
  Same-vintage Jul-3 Pareto pairs (LPG $36.00/0.84/9.3 + TP $54 BUY; BWLP kr181.9→$18.52/0.97/9.9)
  — the Jul-3 LPG rows were MISSING from `pareto_share_prices.csv` (parser gap, re-extracted from
  the PDF; fix at the next harvest pass). EDGAR poller pins +LPG/BWLP (CIKs re-confirmed against
  SEC submissions JSONs). 12 names' EV%-only price-vintage drift annotated explain-not-accept
  (owner decision #1; STNG's price-driven HOLD→TRIM/SHORT band flip joins GSL's for owner eyeball).
  At HEAD two DESIGNED reds: baseline-covers-live-state (LPG/BWLP await the owner ratify) +
  committed-scorecard vintage (clears at the ratify commit). Phase 5 = the owner's lock ruling.
- **2026-07-09 — pre-Phase-4 hardening: the four owner-review findings closed (documented → ENFORCED).**
  (F-1) The age-5 WIDE flag is machine-readable: `provenance.MARK_WIDE_NODES` registry (VLGC
  five_year, band $89.7-95.9M, ≥50%-sensitivity age window 2.5-7.5) → `scorecard._mark_wide_exposure`
  → per-name `mark_wide_nodes` in `book_scorecard.json` (**schema 2.2→2.3**, additive) + a
  wide-node block in the markdown — BW LPG's 2019-21 hulls can no longer print age-5-dependent NAV
  unmarked. (F-2) The synthetic pure-VLGC end-to-end is a COMMITTED artifact:
  `tests/test_lpg_sector.py::test_synthetic_pure_vlgc_end_to_end` (cycle 1.59× realized-vs-realized,
  w_nav 0.70, FV ordering, PW identity, absorption_base vessel_scale 1.00) plus the two-surfaces
  identity `test_ffa_base_forward_equals_absorption_base_path` (the Phase-3 derivation rule is now an
  asserted identity, per the 2026-07-02 rule). (F-3) The realized-basis numerator is machine-pinned:
  `twelve_month_tc.yaml` gains a `rate_basis` block (default tc_assessment; VLGC realized_tce) and
  `test_cycle_numerator_basis_agrees_with_anchor_basis` asserts set-equality between realized_tce
  stamps and the classes of realized-anchored sectors — pasting a 1-yr-TC print into VLGC now has to
  falsify a diffed stamp to stay green. (F-4) **METHODOLOGY §11.10 written** (scope / LPG Set A /
  realized anchor / marks incl. the wide node / rates plumbing / v1 lock target) — the lock tests'
  §11.10.x remediation pointer is live; "prospective §11.10" comments de-staled. Suite 550→558.

- **2026-07-09 — WO3 Phase 3 LANDED: VLGC rates plumbing (realized basis, war-spike NOT promoted).**
  `twelve_month_tc.VLGC = 63,615` — Dorian Q1-2026 REALIZED fleet TCE (disclosure-cluster vintage
  2026-06-02, held), the DELIBERATE basis: the ratified LPG cycle multiple is realized-vs-realized
  (63,615 ÷ 40,000 = **1.59×**, the late-cycle/peak war-elevated read; a 1-yr-TC numerator was the
  VOIDED mixed-basis read — the BW Pampero ~$60k TC stays a cross-check, 0.94× coherent).
  `ffa_forward_curve.VLGC` = the absorption_base scenario base path under a DOCUMENTED derivation
  rule (starts at current realized ~$62k, decays along the observed backwardation [1-yr $60k →
  3-5yr low-$40ks] to the $40k anchor by q8) — the war-spiked `vlgc_*` spot dailies (usgom ~$155k)
  are NOT promoted, per the Phase-0 convention. This row doubles as the scenario engine's
  vessel-elasticity reference, so absorption_base carries vessel_scale 1.00 (marks struck at
  today's market, where the §9.9 prints are). New standing trigger `vlgc_realized_tce_refresh`
  (due null — each validator quarterly disclosure; the held-VALUE-invisible-to-mtime lesson).
  END-TO-END VERIFIED: a synthetic pure-VLGC 4-hull name runs the full NAV+cycle+strip+scenario
  stack (fleet $343M off the fitted curve; cycle 1.59× → w_nav 0.70; scenario FVs $20.00-32.80) —
  Phase 4 onboarding has no engine gaps left. Gate-neutral (zero LPG names; suite 550 green;
  drift gate 0 UNEXPLAINED).

- **2026-07-09 — WO3 Phase 2 LANDED: VLGC marks — §9.9 transaction-anchored, the 9th fitted class.**
  `transactions/vlgc.yaml` (7 in-window prints from the sec99 hunt sample, ages 9-17 under the
  repo's sale_year−build_year convention, + 3 documentation rows incl. the BW Yushi OPTION strike —
  never fit) + a VLGC curve block (flat, 54k dwt/84k cbm ref): **NB $117.5M (NB-parity age-0,
  registered AGE0_BASIS exception — no broker gas resale line exists; basis_status
  pending-sourceable) · 5yr $92M · 10yr $80M · age-25 VALUE anchor $42M** (LNGC convention, NOT
  demo ~$12M — the old leg reproduces Hampshire 18yr/$57M and Lycaste Peace 23yr/$48M within $2-3M;
  the no-scrappage-lever cell priced). Fit: n=7, slope −$2.40M/yr, **age-10 $80.3M stable under
  every exclusion cut (the strong node); age-5 $92.3M EXTRAPOLATED, flagged WIDE $89.7-95.9M**
  (zero 5-yr prints; cross-checks: age-5/NB 0.79 = the VLCC ratio; option strike $70M below it);
  ex-ALL-BW degenerates and the solver correctly falls back (slope guard). Related-party downweight
  (BW Chinook/Pampero) delivered via recency weights (~0.45), not a guessed quality uplift. Broker
  cross-read recorded: fitted age-10 sits ~+11% over Pareto's $72M generic-2016 quote (their own
  "10%+ beat" comment on Sinogas) — LPG now reads on txn-anchored k_broker semantics. Record:
  `decisions/vlgc_marks_2026-07-09.md`. Gate-neutral (zero LPG names; suite 550 green; drift gate
  0 UNEXPLAINED). Watch: Dorian trio per-vessel splits (Q4-26 filings), Advanced full-year
  re-harvest (highest-value sample upgrade).

- **2026-07-08 — WO3 Phase 1 LANDED: `sectors.lpg` scenario family live (LPG Set A, US-export-arb).**
  Per the ratified Phase-0 doc (decisions/lpg_methodology_2026-07-07.md): 4 scenarios
  arb_wide/absorption_base/overhang/arb_collapse at **0.15/0.35/0.35/0.15**, VLGC 8-quarter curves
  (±15% bands) grounded in the Phase-0 evidence cells — PW front-4 ≈ $48.6k (1.22× anchor), PW
  end-strip $34.3k (the overhang tilt priced, below the mean). Cycle anchor **$40,000/day 10-yr
  through-cycle REALIZED TCE, `as_of: 2026-07-07`**, under a NEW anchor-basis token
  `realized_tce_10yr_mean` — a FOURTH basis that trips MIXED-ANCHOR-BASIS vs the TC-anchored sectors
  (test-pinned) instead of silently composing. Routing wired (scenarios/pipeline/loaders/add_ticker
  already knew lpg; VLGC → `vlgc`, VLGC-only per Fork 1). **§9.10 weight family shipped from birth:**
  `scripts/lpg_weight_comparison.py` (LPG Set A locked + Set B arb-bull / Set C deep-overhang ±~10pp
  brackets, sets live in the script) — family registered in the sidecar now; per-name entries populate
  when the Phase-4 validators (Dorian LPG CIK 1596993 / BW LPG CIK 1649313) onboard.
  `test_lpg_locked_weights_and_anchor` pins weights + anchor + as_of. Gate-neutral: zero LPG names,
  delta report 0 material, drift gate 0 UNEXPLAINED, suite 547+ green.
  **BUG found & fixed in the sidecar seam** (scorecard.py `update_weight_fragility_sidecar`): the
  pre-namespacing guard was a hardcoded `{crude, product, lng}` whitelist, so the FIRST merge after
  WO4's `dry_bulk` block landed would have WIPED every other family's `weight_sets` — and silently
  narrowed `weight_family_basis`'s staleness scope to the caller. Replaced with key-shape detection
  (set-label keys vs lowercase family tokens); `test_sidecar_merge_preserves_all_other_families` pins
  N-family preservation. All four legacy families re-run to re-stamp against the new
  scenario_inputs.yaml hash (required by WO1-F4): entries numerically stable, **no `ev_sign_stable`
  flips, no position changes** — only ±0.1-0.9pp EV wobble from the stale-feed static-price fallback.
  **Drift-gate note (explain, not accept):** the verification pipeline run surfaced the KNOWN
  committed-price drift (PLAN pending owner decision #1) as 4 UNEXPLAINED EV%-only rows
  (CAPT/CMDB/GSL/MPCC, ΔNAV 0.0%) — annotated in their decision logs as price-vintage artifacts
  (stale daily feed since Jul-2/3 → static-price fallback); the re-ratify AND the GSL BUY→HOLD band
  call remain the owner's.

- **2026-07-07 — WO4: dry-bulk weight-robustness family (§9.10) shipped (charter dry-bulk half; unblocks
  consumer Gate E).** `scripts/dry_bulk_weight_comparison.py` (mirrors crude) runs SBLK/GNK/CMDB/SB under
  locked Bulk Set A + two defensible ±~10pp China-demand brackets (Bulk Set B China-bull / Set C
  property-drag; sets live in the SCRIPT, production untouched). Findings: **SB & CMDB weight-robust BUY;
  SBLK sign-stable-positive but LABEL position-driven (BUY→HOLD at the drag bracket); GNK
  sign-stable-negative.** The sidecar (`outputs/weight_robustness.yaml`) now carries a current-SHA
  dry_bulk block with `ev_sign_stable`/min/max for all four — the field the consumer's Gate E reads;
  the schema-2.2 seam emits them into `book_scorecard.json` on regen (proven by
  `test_weight_fragility_flag_renders_and_reaches_the_json`). `test_dry_bulk_locked_weights_position`
  pins Bulk Set A + SBLK's BUY so a future reweight surfaces deliberately. DIAGNOSTIC ONLY — Bulk Set A
  byte-unchanged, gate-neutral (no NAV/EV/mark/weight move). **Separate finding surfaced (NOT WO4):**
  regen exposed pre-existing committed-price drift — FVs byte-identical but EV% denominators moved vs the
  Jul-6 book snapshot (CMDB EV +6.0pp, GSL band BUY→HOLD) — the overdue daily-price-refresh re-ratify
  thread; deliberately not bundled into WO4, teed up for its own owner-aware re-ratify.

- **2026-07-07 — WO3 LPG Phase 0 ratified + a known-failure-mode flag.** LPG/VLGC sector methodology
  doc ratified (decisions/lpg_methodology_2026-07-07.md): VLGC-only; §11.8.6 coverage reuse; §15
  BW-bloc screen; scenario weights **0.15/0.35/0.35/0.15** (overhang co-weighted with base — LPG is
  the supply-heavy/demand-soft mirror of dry bulk, not its shape). Cycle anchor = **~$40,000/day
  10-yr through-cycle VLGC realized TCE** (as_of 2026-07-07, annual-review trigger
  `lpg_anchor_annual_review`) — realized-TCE basis is CORRECT for an 85-99%-spot validator pair, not
  a compromise; 1-yr TC ~$60k is a documented cross-check; cycle multiple is realized-vs-realized
  ~1.5-1.6× (war-elevated), never mixed-basis. Triangulated from Dorian's complete FY2016-26 10-K
  TCE series + BW LPG + Clarksons "in line with long-run averages" + Dorian's own trailing-10yr
  impairment concept. **KNOWN FAILURE MODE flagged (owner, 3× now):** web-heavy source-agent fleets
  keep stalling the stream watchdog; each salvage worked (the Dorian series was recovered straight
  from a frozen agent's jsonl) but cost a manual synthesis pass. On the WO2 board as its own line
  (PLAN.md, task #32); interim rule: source sweeps run single-threaded until web-research agents get
  the fetchers' watchdog-and-restart. "Salvageable by hand each time" is the manual step the
  automation exists to retire.

- **2026-07-03 — Xclusiv geometry confirmed on a live issue (WO2 1.3 landing condition):**
  `cli inspect` on `data/pdfs/xclusiv/2026W26_0670764b.pdf` — pdfplumber detects the ruled
  grids (newbuilding orders table 11×8; BC/tanker S&P sales tables 8-col with clean rows),
  and the poppler text layer carries the production parser's section keys (`DRY SECONDHAND`
  ×1, `TANKER SECONDHAND` ×1, `Resale` ×10, `5 Year` ×16 — parse/xclusiv.py:119 keys off
  exactly these; WET SECONDHAND is the alternate label, correctly absent). The documented
  parser caveat (xclusiv.py:18-20) is closed for the current issue format. Harvester UA
  placeholder also fixed to a real contact (config.py:26, the fetch_pdf.py:54 precedent).

- **2026-07-03 — RECORD NOTE (WO1-F3):** commit `afaa43c`'s message says "schema v3" — an
  integer dev-iteration label that never shipped as a contract version. The handoff schema
  went 2 (int) → "2.1" → "2.2" (strings, major-2 asserted by the consumer); the transient
  int 3/4 states exist only inside the 2026-07-02 dev sequence. There is no phantom v3 to
  hunt for. (History not rewritten post-push; this line is the correction of record.)

- **2026-07-02 — F-13 (P0, same-day): verdict rows MIXED VALUATION BASES — blend FV next to scenario position; handoff re-based + coherence-guarded.**
  Post-vintage review caught `d1544b4` shipping self-contradictory rows ("CAPT +28% upside · TRIM/SHORT"):
  `valuation_index` took fv from the single-point BLEND while position came from the SCENARIO-weighted EV.
  The two bases agreed incidentally under the Jun-9 war weights; the vintage separated them — the THIRD
  same-day instance of an incidental identity treated as an invariant (after C-3's rank-1 pairing and the
  "identical weights at each index" comment). Fix: headline fv/ev_pct in the scorecard + JSON are now the
  SCENARIO-weighted FV (one basis with position, the proposal tables, and the C-2 decomposition); the blend
  survives as the labeled secondary `blend_fv` (a large Blend-vs-Model gap IS the scenario-dependence
  signal — BRUT $9.27 vs $3.12); **schema_version 2** (ingesting side must assert). Guards close the class:
  hard identity (`test_f13_fv_and_position_share_one_basis`) + committed-surface sign/label coherence under
  the one canonical ±5% band (`test_committed_handoff_sign_label_coherence`). Gate: 0 UNEXPLAINED (dNAV/dEV
  0.0 — snapshot EVs were always scenario-based; the defect was rendering-only), re-ratified with cause for
  the record. The tanker rows' blend staleness is partly the DISCLOSED option-(i) rate hold — the disclosure
  was working; the column basis was the defect. Field-general rule added to CLAUDE.md: two surfaces assumed
  to agree need a test asserting they agree.

- **2026-07-02 — REVIEW ARC: reweight proposal approved through 3 rounds; C-3 MULTI-SLEEVE AGGREGATION BUG fixed; §13.3 triggers operationalized; W-frag on the verdict row.**
  The post-stand-down reweight proposal (`decisions/crude_reweight_proposal_2026-07-02.md`, v3) went through
  review → addendum → C-4 sign-off same day. Landed: (1) **C-3 — all three hybrid aggregators applied the
  LEAD sleeve's (crude's) probability weights to every sleeve** (rank-1 index pairing; the 2-sleeve
  aggregator's own comment recorded the "currently-identical weights" assumption that the Jun-9 reweight
  silently broke — CMBT's dry-bulk sleeve, 72.7% of vessel value, was probability-weighted by the Hormuz
  state). Fixed to per-sleeve sector weights in one aggregation core; regression test (a worthless crude
  sleeve is invariant under a crude-only reweight); the old INSW identity test asserted the bug's math and
  was inverted. Own gate layer ratified: CMBT −3.6pp / TEN −3.2pp / INSW −1.5pp, ΔNAV 0.0%. Narrative
  corrected: the reweight's false-BUY list is BRUT + CAPT; CMBT's downgrade was majority artifact.
  (2) **§13.3 triggers → `inputs/reweight_triggers.yaml`** (7 dated/statused triggers incl. the Jul-17 MoU
  implementation checkpoint, the Aug-16 toll cliff scoped crude+product, product glut-arrival-timing),
  surfaced red by the refresh preflight — the prose trigger that fired Jun-17 and sat 15 days can't recur.
  (3) **W-1 W-frag** — EV-sign stability across the §9.10 family on the verdict row + `weight_sign_stable`
  in the JSON handoff (flags BRUT/CAPT/CMBT under the CURRENT weights). (4) The §9.10 diagnostic had run on
  un-anchored marks + static prices since Jun-9 with a stale "Set A" (look-back: no decision affected — the
  only citation predates the break); fixed, extended to all 10 crude-exposed names, machine-readable sidecar.
  (5) Sizing language struck from valuation outputs (reviewer correction: worth + trust only; sizing is the
  governance repo's field). **THE VINTAGE EXECUTED same day (owner "Approved, option (i)" after the
  Rider-3 diff review):** crude 0.10/0.20/0.45/0.25 + MoU-ineffective leg recalibrated (0.15-flare mixture;
  `semantics_changed: 2026-07-02` machine marker) + product v2-restore + LNG v3-restore (§11.3/§11.5
  revision notes; lock tests re-pinned per their own instructions) + F-5 refresh (spot_tce fully re-cited to
  the 2-Jul Pareto — TD3C $285.5k, Brent $70.8; dry-bulk FFA/12M-TC promoted from the 2-Jul OCR; TANKER
  forwards HELD at Jun-7, owner option (i) — no market print exists; trigger `tanker_forward_print_lands`
  armed, scorecard Rate-basis header discloses). Gate: 18 UNEXPLAINED re-ratified with cause; six band flips
  eyeballed + annotated (DHT HOLD→TRIM [cycle-relabeled], STNG BUY→HOLD [retracts the morning's
  price-driven flip], FLNG BUY→HOLD [back to v3 history], CMBT BUY→TRIM [BOUNDARY-CROSS at −5.05% — the
  −$0.39 dry-bulk rates nudge carried it over; read as HOLD-straddle], BRUT +98%→−40% and CAPT +37%→−19%
  [the two genuine war-premium false-BUYs]). C-2 decomposition complete per-sector in the proposal §10;
  tanker rate-effect exactly $0.00 (held forwards — understated as caveated). W-5 registered in brut_log
  with the corrected epistemology: the governance layer (PROVISIONAL ⛔ + POSITION_UNRELIABLE) succeeded by
  preventing the model from fighting a correct tape — BRUT fell 7.5% on Jun-30 vs the crude five's 15–22%;
  the market never carried the model's war premium.

- **2026-07-02 — EXTERNAL AUDIT RESPONSE: 12 findings verified (10 confirmed / 2 partial), 9 fixed same-day; the price band was WORSE than the audit said.**
  An independent clone-and-run audit of `6749362` landed 12 findings (`outputs/EXTERNAL_AUDIT_2026-07-02.md` —
  register + disposition). Every finding re-verified locally by an 18-agent workflow (adversarial re-checks on all
  P0/P1s; all upheld). Three things the audit couldn't see from a clone: (1) **the ±15% "day move" band was actually
  a ~5-session trailing move** — `chartPreviousClose` on a `range=5d` request is the close before the WINDOW (proven:
  June-30 prev_close values sat 12-21% above the June-26 committed closes mid-slide), so the June-30 repricing would
  have held ASC/TNK on statics ~5 trading days, not 1; (2) **the July-1 price cron fired and its output was
  discarded** — reverted ~1h later by the HAFN session's price-drift isolation, and the deferred re-ratify never
  happened (vintage survives only in `state/price_refresh.log`); the discipline is amended: revert → **drift commit
  in the SAME session**; (3) F-5's plumbing is inverted — `spot_tce` never feeds the strip; the strip's war-vintage
  exposure is `ffa_forward_curve.yaml` (VLCC q1 3.7× mean, UNDER the 5× warning bar) + `twelve_month_tc.yaml`, both
  unrefreshed since 2026-06-07. **Fixed same-day** (six commits, each finding-attributed): F-1 (true prior-day close
  + ≥3-name market-event circuit breaker + loader fallback recording + scorecard price-basis header), F-3/F-10
  (breakeven exact-zero sentinel; SIX docs carried 1e29 ratios, not 3 — now "price justified by NAV alone" / "n/a",
  guarded by `test_outputs_hygiene`), F-4 (`outputs/book_scorecard.json` — schema_version 1, void-striking, NaN→null,
  lock-tested; the governance seam is now a contract), F-6 (quarter regex + abort-before-state-writes; an all-skip
  run used to touch `decisions/*.md`), F-7 (regen; TRMD `· basis-pending` — the staleness was intra-commit b5019cf),
  F-8 (verdict prose derived from rows, never hand-written literals), F-9 (README 22 tickers / 460+ tests, counts
  guarded vs watchlist.yaml — the audit's own 440 was miscounted), F-12 (shares ≤ 0 hard-fails at load). Gate loop
  clean: 464 passed + 16 xfailed, drift gate 0 UNEXPLAINED (regen at the committed price vintage — zero price drift
  bundled). **OPEN:** F-2 (crude reweight = §13.3 owner trigger — proposal drafted, decision Dan's), F-5 (dated rate
  refresh, pairs with F-2's re-run), July-1 price recovery (staged as its own re-ratify), F-11 (optional YAML
  migration — noting the queues are ALSO duplicated in guard-test literals, double the audit's stated surface).

- **2026-07-02 — TRMD RECONCILED: the estimate-heaviest name, the FIRST to move NAV UP, and it CLEARS the P0 queue.**
  Eighth and LAST P0 name (TORM plc) — the reconciliation queue (`NAV_FIGURE_ESTIMATE_QUEUE ∩ PROVISIONAL`) is now
  CLEARED (NAT/SB/ASC/BRUT/ECO/HAFN/STNG/TRMD). TRMD's prior balance sheet was the estimate-heaviest in the book —
  six `[ESTIMATE]` figures — and uniquely, two of them badly SUPPRESSED NAV, so this is the only reconciliation of
  the arc that moves NAV materially UP (+19%). Every figure sourced to the Q1-2026 6-K (EDGAR acc
  0000919574-26-003082, Ex-99.1) and independently confirmed by an 8-agent verification workflow (5 extractors + 3
  adversarial verifiers, ALL verdicts agree — the WC verifier even caught the segment-vs-consolidated trap).
  Pre-reg `decisions/trmd_reconciliation_prereg_2026-07-01.md`.
  1. **The subsequent-event pattern, a THIRD time (after ASC + HAFN).** `newbuild_capex_commitments` $360M →
     **$31.2M** (Note 10 "Second-hand vessels commitments: Total"). The $360M bundled the **6 MR resales TORM
     bought "after the end of the quarter"** (Business Highlights + Note 11 subsequent events — deliveries 2027-28).
     Only the 2 Q1-agreed MR resales (Dehradun/Dapitan, 2015-built, Q2-2026 delivery) are a real 31-Mar commitment.
     (+$329M NAV.) The "audit the subsequent-events note FIRST" rule caught it before it touched the number.
  2. **Operating WC was badly under-estimated.** `working_capital_net` $110M[est] → **$254.9M** (Inventories 82.5 +
     Trade receivables 249.6 + Other receivables 32.7 + Prepayments 14.3 − Trade payables 67.2 − Other liab 53.2 −
     Current tax 0.7 − Provisions 0.5 − Prepayments-from-customers 2.6; the CONSOLIDATED column). TORM carries
     $249.6M trade receivables + $82.5M bunker inventory at a record-rate quarter-end. (+$145M NAV.)
  3. **Debt + leases refined.** `total_debt` $1,089.6M → **$1,081.8M** (BS "Total borrowings"; Note 5 reconciles:
     schedule 1,084.4 − borrowing costs 12.6 + ROU lease 10.0). `lease_liabilities` $5M → **$0** (the $10M ROU is
     INSIDE borrowings — TORM bought out its sale-leasebacks in 2025, only the ROU remains). `newbuild_advances_paid`
     $50M → **$0** (on-curve: the $38.9M "Prepayments on vessels" is embodied in the delivered value). Cash $196.4M,
     shares 103.3M — all verified.
  - **Three owner forks (all "completeness"), 2026-07-02:** (1) WC on the operating-current basis $254.9M (tool
    convention; the $45.2M held-over-gains tax flagged as a book-wide omission). (2) The 2 MR resales **wired ON-CURVE
    §9.6** — UNLIKE STNG's VLCCs, these are in-sector (product MR), near-immediate (2015-built secondhand, Q2 delivery,
    no construction/PV/cross-sector issue), so wiring on-curve is clean → TRMD leaves `OFF_CONVENTION_QUEUE`. (3)
    Scrubbers corrected to the disclosed **85** (FY2025 20-F "we successfully installed scrubbers on 85 of our vessels"
    = all 22 LR2 + all 63 MR; the 10 vintage LR1s run compliant fuel) → leaves `OPERATING_SCRUBBER_QUEUE`, `{TRMD:85}`.
    The 2 resale hulls booked scrubber=FALSE (no NB-specific statement — the SB peer-trap).
  - **Net: base NAV $26.74→$31.65, headline $25.43→$30.34, HOLD→BUY (+17-22% EV).** SANITY OK; **k_broker 1.17→1.03 —
    now the TIGHTEST tool↔broker spread in the book.** A TRIPLE corroboration: the tool headline $30.34 ≈ TORM's OWN
    disclosed NAV/share $29.7 ≈ the price-consistent broker NAV $31.40. TRMD leaves `NAV_FIGURE_ESTIMATE_QUEUE` and all
    three queues → **GOVERNED-WIDE·basis-pending** (a NEW sub-reason): NOT VALIDATED-TIGHT because the product
    nav_basis is `pending-sourceable` — the product resale-curve marks are deferred (thread P1c), a book-wide product
    limitation, not TRMD-specific (ECO reached TIGHT only because it's crude/resale-uniform).
  - **The arc finding, one last time (eight-for-eight):** cleaner + still directional. TRMD is the arc's ONLY name
    to get genuinely CHEAPER after sourcing (BUY +17%, k 1.03) — but it's a product tanker near cycle peak with a
    ~10% dividend yield (§12 caveat) and it's GOVERNED-WIDE not TIGHT, so it's a directional BUY, not a tight
    actionable long. The validated-tight-actionable-long surface stays SB + SBLK.

- **2026-07-01 — STNG RECONCILED: the most TANGLED — two large errors pointing OPPOSITE ways that nearly cancelled.**
  Seventh P0 name (Scorpio Tankers), and the one where a half-fix is most dangerous: the prior state carried a
  debt double-count (NAV too LOW) and a held-for-sale double-count (NAV too HIGH) that roughly offset, so the
  model reported a plausible-but-wrong headline NAV ($80.35). Fixing either error alone would have swung NAV by
  ~$4/sh in the wrong direction. Owner-directed FULL per-vessel rebuild vs the Q1-2026 6-K (EDGAR acc
  0001483934-26-000042, Ex-99.1, as-of 3/31). Pre-reg `decisions/stng_reconciliation_prereg_2026-07-01.md`.
  1. **`total_debt` $789.1M double-counted the $200M 2030 notes.** STNG's own reconciliation gives "Gross debt
     outstanding, March 31, 2026 = **$589,056K**" (secured bank $389.1M + Unsecured Senior Notes 2030 $200M; ties
     to reported net cash $395.3M). The model took the $589.1M TOTAL as bank-only and added the $200M notes AGAIN.
     → **$589.056M** (+$200M NAV).
  2. **The $395M held-for-sale line double-counted operating hulls AND was the wrong list.** The exhibit's 87-row
     fleet table marks 8 vessels "(22)" = agreed-to-sell (the **March 8-vessel agreement**: Solidarity LR2 $60M +
     7 MRs $245M = **$305M** agreed / $215M carrying = the BS "Assets held for sale"). But 6 of those 8 (Aqua/
     Regina/Opera 2014 MRs + Osceola/Brooklyn/Black Hawk 2015 MRs) were ALSO counted on-curve in the manifest, and
     the model's HFS *list* wrongly named operating LR2s (Broadway/Condotti/Winnie/Lauren) + the Q1-CLOSED STI
     Lavender. Fixed both ways: removed the 6 from the fleet (**MR 41→35, on-curve 87→81**) and re-booked HFS via a
     new dedicated `held_for_sale: $305M` field, replacing the wrong $395M in working_capital_net (−$280M net NAV).
  3. **Operating WC omitted accrued expenses.** $207.8M → **$163.3M** (AR 225,245 + inv 10,897 + prepaid 9,188 −
     AP 37,454 − accrued **44,603**; the prior figure dropped the $44.6M accrued line). NB advances $90M[est] →
     **$69.069M** (BS "Vessels under construction"). Cash $984.321M, diluted shares 50,025,865, leases 0 — all verified.
  - **Net: NAV $83.87→$80.97 base / $80.35→$77.47 headline, position BUY→HOLD** (landed in the pre-registered halt
    band $80.5–81.5 base / $77.2–77.8 headline). SANITY OK (−28.3% to broker $108 — a wide, DOCUMENTED tool↔broker
    spread, a feature). STNG **leaves `NAV_FIGURE_ESTIMATE_QUEUE`** (advances sourced; no uncited estimate left) but
    **stays `OFF_CONVENTION_QUEUE` → PROVISIONAL·off-curve** (sub-reason `uncited-figure`→`off-curve`).
  - **FLAGGED, separate owner decision (out of scope):** the 10-vessel newbuild order book (4 MR + 4 LR2 + **2
    VLCC** — STNG's first crude exposure) is off-curve, carried as a −$504M commitment-only drag (a §9.6 violation).
    These are REAL 3/31 commitments; wiring on-curve per §9.6 would add **~+$481M NAV (~+$9.6/sh)**, flipping the
    read materially. Deferred: the 2 VLCC NBs are cross-sector (need the crude curve) and warrant their own
    methodology decision. The arc holds seven-for-seven: cleaner + still directional, no new tight actionable long.

- **2026-07-01 — HAFN RECONCILED: the most consequential — three ways "balance-sheet-literal ≠ NAV-economic," + 2 precedents.**
  Sixth P0 name (Hafnia), and the one where "just source the number" fails most completely — nearly every figure
  needed a judgment about what the number economically MEANS, not just a citation. Workflow-sourced (12 agents) +
  independent read vs the Q1-2026 6-K (EDGAR acc 0001140361-26-022910, IFRS). Pre-reg
  `decisions/hafn_reconciliation_prereg_2026-07-01.md`. Hafnia's own disclosed NAV/sh $8.09 was the sanity anchor.
  1. **The 8 MR HHI newbuild was a SUBSEQUENT EVENT (the ASC pattern again).** The ~$405M order was signed
     **3 April 2026** (Note 7), after quarter-end — so the model's −$405M commitment + $40M phantom advance was
     the same "double-anachronism" as ASC (a commitment that didn't exist + an advance that couldn't have been
     paid). Excluded from Q1 (+$365M); HAFN leaves `OFF_CONVENTION_QUEUE`; wire on-curve in Q2. The
     "audit the subsequent-events note first" rule caught it (Note 7).
  2. **`total_debt` and `lease_liabilities` both understated.** Note 2/4 give bank borrowings **$953.9M** +
     lease liabilities **$71.6M** (SLB $35.7M + IFRS-16 $35.9M) = $1,025.5M total borrowings. The model's
     total_debt $943.5M matched no primary line (~$10.4M light) and lease_liabilities $35.9M captured ONLY the
     chartered-in piece, dropping the $35.7M sale-leaseback. Corrected (−$46M NAV).
  3. **TORM 13.97% stake → $277.2M lower-of-cost, NOT $395M market — NEW PRECEDENT.** The stake is $395M market /
     $394.954M IFRS FVTPL carry / ~$277.2M lower-of-cost. Hafnia's OWN NAV method is "the lower of the market value
     or purchase price" → $277.2M. Owner rule: **a marketable equity stake inside a shipping NAV takes the ISSUER's
     own disclosed NAV-method basis (lower-of-cost) when available, not fair value** — fair value injects market
     volatility and breaks comparability to the issuer's published NAV. First cross-holding hit; sets the precedent.
  4. **Operating WC → conservative $85.7M pool floor, NOT the gross $335.9M — NEW PRECEDENT.** The balance-sheet
     operating WC is $335.9M (receivables $670M + inventory $86M − payables $420M), but Hafnia runs the world's
     largest product-tanker POOL, so the $670M receivables carry **custodial pass-through gross-up** (revenue
     collected on behalf of other pool owners — not a NAV-economic asset; Hafnia's own $8.09 NAV nets it too). The
     6-K doesn't break out pool vs own-account, so booked at a conservative floor ≈ the clean own-account inventory
     ($85.7M), rejecting the gross. HAFN STAYS PROVISIONAL on WC → new tier sub-reason **`pool-gross-up-pending`**.
     Owner rule: **for a pool operator, gross pool receivables are custodial, not NAV-economic — net the gross-up
     out, or book the conservative floor and flag it.** `sourced ≠ economic` — the same wedge as NAT's contradicted
     advance and ASC's date-wrong newbuild, here as pool gross-up.
  Also: shares → 505.3M (EPS table). NAV $5.22→$5.57 headline (newbuild +$365M · TORM −$118M · debt/lease −$46M);
  SANITY OK; gap to broker a wide, documented tool↔broker spread (txn-anchored < broker). HAFN is **NOT actionable**
  (directional, rich to the tool's conservative marks) — rich · cycle position. **An incidental daily price-refresh
  (5 names CCEC/CMDB/FLNG/MPCC/STNG, EV-only) landed mid-session and was REVERTED from the tree to isolate this
  sourcing commit** (per `feedback_isolate_commit_from_price_drift`) — handle as a separate deliberate price
  re-ratify. **Six reconciliations, still zero new tight actionable longs** — even the hardest one lands "cleaner,
  still directional." Tight-actionable surface stays SB + SBLK. 442 pass / 20 xfail; drift 0 unexplained (HAFN annotated).

- **2026-07-01 — ECO CLEARED to VALIDATED-TIGHT: the first TIGHT of the reconciliation arc, and the cleanest.**
  Fifth P0 name (Okeanis Eco Tankers). ECO was PROVISIONAL for ONE reason — `OFF_CONVENTION_QUEUE`: its 2
  Suezmax newbuilds (Tigani, Vous) sat in the manifest at delivered market with NO `years_to_delivery`, so they
  classified "commitment-net" not "on-curve". Its figures were already issuer-cited, so the §9.6 on-curve fix was
  authorized. Pre-reg `decisions/eco_reconciliation_prereg_2026-07-01.md`. All figures VERIFIED vs the Q1-2026
  6-K (EDGAR acc 0001104659-26-060273, Exhibit 99.1): debt $683.1M (incl. sale-leasebacks, no separate lease
  line), cash $176.5M, advances $39,737,420 → remaining commitment $158.86M, 2 Suezmax NBs $99.3M each (MOA
  Jan-2026, delivery May & July 2026), shares 39,044,655, fleet 8 VLCC + 8 Suezmax (avg age 5.8y — no phantoms).
  The $90M NB financing facility was signed April-30-2026 (subsequent event, correctly not in the 3/31 sheet).
  FIX: split the NB row into Tigani (`years_to_delivery: 0.12`) + Vous (`0.29`) → PV-discounted on the §9.6 curve
  → ECO leaves `OFF_CONVENTION_QUEUE`. Also verified the 16 on-water scrubbers ("eight scrubber-fitted Suezmax +
  eight scrubber-fitted VLCC", 6-K) → `OPERATING_SCRUBBER_VERIFIED{ECO:16}`, leaves `OPERATING_SCRUBBER_QUEUE`.
  **PROVENANCE CATCH (the SB trap, live):** wiring the NBs on-curve triggered the value-flag guard, which blocked
  defaulting `scrubber=true` from the existing fleet — the 6-Ks' only scrubber statements are existing-fleet-scoped,
  never newbuild-specific, and the NBs are described only as "resale newbuilding Suezmaxes". So the NBs are booked
  **scrubber=false** (conservative, registered in `newbuild_specs.yaml`, upgradeable on a delivery-6-K disclosure) —
  the guard doing exactly its job. NAV $34.56→$34.35 (−0.6%: §9.6 PV discount + conservative NB scrubber) — BELOW
  the 2pp drift threshold, so the gate stayed stable with no re-ratify required. **Tier PROVISIONAL →
  VALIDATED-TIGHT** (traced resale-uniform + robust two-basis; op-scrubber surface immaterial at 2.2% AND now
  verified). But ECO trades RICH (~1.39× NAV; price ~$50 vs NAV $34.35) → position stays **rich · cycle position
  (not a short)**: VALIDATED-TIGHT means the NAV is SOLID, NOT that ECO is cheap — it is validated-but-RICH, **NOT
  a new actionable long.** Five reconciliations (NAT/SB/ASC/BRUT/ECO), still zero new tight actionable *longs* —
  the tight-actionable surface stays SB + SBLK. 442 pass / 21 xfail; drift 0 unexplained; SANITY OK.

- **2026-07-01 — BRUT TRACED: the reconciliation VALIDATES the model, and the name still doesn't clear.**
  Fourth P0 reconciliation, and the first with a DIFFERENT shape — no ASC-style errors. BRUT (Bruton Ltd) is a
  pre-operational Euronext-Oslo VLCC-newbuild vehicle that reports HALF-YEARLY (first issuer report H1-2026, due
  2026-08-13), so its "2026-Q1" snapshot is a Dec-2025-actual-rolled-through-Q1-subsequent-events construct.
  Sourced via a 9-agent workflow + an independent read of the primary docs (FY2025 Annual Report
  `inputs/research_issuer/2025_brut_annual_report.pdf`, audited PwC US GAAP; the Euronext admission doc — the
  "prospectus" the model said was "NOT located" IS on disk; Pareto as cross-check). Pre-reg
  `decisions/brut_reconciliation_prereg_2026-07-01.md`.
  1. **The balance sheet validates.** Four of five figures now trace to the issuer and CONFIRM the prior Pareto
     estimates: remaining newbuild commitment **$1,373.1M** (Note 10 6-vessel base $661.7M + Note 15 Jan-2026
     order $236.0M + Note 15 Mar-2026 CIMC 4-vessel order $499.0M − $23.6M Q1 installments) ≈ prior $1,370M;
     interest-bearing debt **$0** (Dec-2025 total liabilities $0.161M, equity-financed, draws-on-delivery);
     shares **61,923,808** (Dec-2025 52,399,998 + Feb-2026 placement 9,523,810 @ $5.25); advances 0 (§9.6
     convention). The max-torque worry (a wrong commitment ≈ $3/sh) resolved to "the estimate was right."
  2. **Cash is the one figure that can't settle until H1-2026 — and it keeps BRUT PROVISIONAL.** Roll-forward:
     Dec-2025 $89.661M + Feb placement $50M − itemized Q1 installments $23.6M = $116M point, BUT the Mar-2026
     CIMC order's ~$50M (10%) execution deposit likely hit Q1 (a going-concern-doubtful issuer doesn't contract
     4 VLCCs without it), which would drop cash to ~$66M. Owner decision: book the **$66M conservative FLOOR**
     (not the $116M point, not Pareto's unsourced $100M midpoint) — on a max-torque name, book the conservative
     end of the OWN sourced range, flag it a floor, pre-register the Aug-13 resolution. NAV $9.40→$8.80.
  3. **NEW tier state `cash-pending-H1-report`.** BRUT stays in `NAV_FIGURE_ESTIMATE_QUEUE` (cash is a flagged
     `[ESTIMATE]` floor) → PROVISIONAL, but its sub-reason is distinct from NAT's `void` or a plain `uncited`:
     it is SOURCED except one figure with a KNOWN RESOLUTION DATE — a "waiting" state, not "broken." Encodes the
     insight that **a reconciliation can validate-and-still-not-clear.**
  4. **Fabricated governance corrected + going-concern doubt surfaced.** The YAML's "Goodwood Ship Management /
     Koch Industries ~26% / no >50% controller / dispersed" appears in NO filing — the primary docs show managers
     **2020 Bulkers Management + Himalaya** (no Goodwood), **no Koch**, a **Trøim-sponsored** vehicle (Drew Holdings
     48.15% at the Nov-2024 admission, now diluted — current % unresolved), and a **zero-fee** Magni support
     agreement. Corrected to sourced facts. The bigger §15/risk finding: the issuer states **substantial doubt
     about the ability to continue as a going concern** — the 12-VLCC program is unfinanced ($268.3M due 2026 +
     $240.1M H1-2027) — so BRUT's NAV is a levered bet on financing that doesn't yet exist. Recorded as the §15
     haircut basis (`governance_discount_pct` kept 0, a specific % is a §15 judgment deferred to H1 financing
     clarity). **BRUT is NOT actionable** — the +96% EV is upside to a going-concern-doubtful, max-torque,
     resale-level-provisional NAV; the tight-actionable surface stays SB + SBLK. **Zero new tight actionable
     longs across four reconciliations** (NAT, SB, ASC, BRUT) — the queue produces completeness, not opportunity.
  SANITY OK (+22.2% to Pareto NAV $7.20); 440 pass / 23 xfail; drift 0 unexplained (BRUT annotated). BRUT-only
  baseline re-ratify pending (owner), to be RE-RATIFIED AGAIN when cash resolves at the H1-2026 report.

- **2026-07-01 — ASC RECONCILED: a Q2 newbuild was posted against a Q1 snapshot; PROVISIONAL → GOVERNED-WIDE.**
  Third P0 reconciliation (pre-reg `decisions/asc_reconciliation_prereg_2026-07-01.md`; band $17.70-17.95
  committed, landed $17.80; NAV $15.96→$17.80). Sourced to the Q1-2026 6-K (acc 0001104659-26-056715),
  FY2025 20-F (acc 0001104659-26-024690), and the 2013 order 6-K (acc 0000919574-13-005339). **Three errors
  + a re-source:**
  1. **The newbuild was a Q2 subsequent event loaded into Q1 (the big one, +$2.15/sh).** The 2×40,500 DWT
     Handysize contracts were signed **April 2026** (6-K Note 8), AFTER the 3/31 date — so at the snapshot
     there was no commitment (no commitments note, no vessels-under-construction line), no advance (the
     $1,024k Q1 vessel capex is existing-fleet deposits, mislabelled "~$1M advances"), no asset. The YAML
     carried a −$88.8M commitment-ONLY drag — the SB date-mixing bug in pure form AND a §9.6 violation
     (commitment with no offsetting asset). EXCLUDED from Q1 (not parked like NAT — NAT's order EXISTED at
     its snapshot; ASC's did not); to be wired on-curve in Q2 (§9.6, issuer-announced $44.9M/ship, a citable
     price). ASC left `OFF_CONVENTION_QUEUE` (no 3/31 newbuild to place on-curve).
  2. **Phantom vessel (−$0.90/sh).** The 6-K's 2017 cohort is exactly 3 MRs (Gibraltar/Pursuit/Persistence);
     the manifest invented a 4th, `Ardmore_Patriot` (age-9 MR) — 0 mentions in the 6-K AND the 20-F, never
     an Ardmore vessel (the author appears to have added a hull to represent "4 product TCs"). Removed. The
     actual owned fleet is 25: 18 operating MRs + Engineer (HFS) + 2 product + 4 chemical Handies.
  3. **Chemical Handies re-marked to a cited carrying-value floor (+$0.58/sh).** The 4×25.2k stainless
     Fukuoka hulls (no clean resale curve, §11.5) carried an uncited ~$13M/hull estimate — the last figure
     gating ASC's provenance queue. Re-marked at CARRYING VALUE, cited to the 20-F "24 of 25 vessels' market
     > carrying" disclosure (a conservative floor). Reconstructed from cited inputs: cost $29.5M (2013 order,
     $118M/4) − straight-line dep (25-yr life, $400/LWT residual; 20-F) over ~10.4-11.2 yrs ≈ $18.3M/hull,
     ~$73M total. Validation: the same method on the on-curve product Handies gives ~$20.0M carrying vs their
     $24.57M market mark (carrying ~19% below market) — so $18.3M is a floor below implied market, and the old
     $13M was simply too low. NOT the product-Handy curve (wrong class = fabrication). Basis flagged
     `carrying-value-floor · §11.5 structural` → ASC lands GOVERNED-WIDE·structural-class, not TIGHT.
  Also re-sourced cash/debt/leases/WC/shares to the 3/31 face; HFS Ardmore Engineer ($35.5M agreed, June-2026
  delivery, HFS effective 3/31) relocated to the dedicated `held_for_sale` field; Series A preferred confirmed
  fully redeemed (Oct-2025) → preferred_equity 0. **Read FLIPPED:** ASC moves TRIM/SHORT → BUY +5.2% — the
  overvalued read was partly the erroneous newbuild drag. It is now mildly CHEAP on corrected NAV (price
  0.90× NAV; −16.6% to APPROX broker, SANITY n/a-OK), so it LEFT `POSITION_CYCLE_RELABEL` (no longer rich).
  The §12 product-cycle caveat still applies to the EARNINGS leg (the strip embeds near-peak product rates;
  the Q2 newbuild on-curve will trim NAV ~$0.49), but that is not a rich-NAV read. NOT a new VALIDATED-TIGHT
  actionable long (GOVERNED-WIDE · structural-class) — the tight-actionable surface stays SB/SBLK. **LESSON (owner-directed):** the CLAUDE.md date-consistency
  rule GENERALIZED beyond the fleet to any balance-sheet figure, with the tactic **audit the subsequent-events
  note FIRST** on every reconciliation (it's where post-quarter events hide). ASC drift annotated + explained;
  ASC-only baseline re-ratify pending (owner action). Guards: ASC left NAV_FIGURE_ESTIMATE_QUEUE +
  OFF_CONVENTION_QUEUE (test copies synced); 2 ASC scenario tests rebased; 440 pass / 23 xfail, drift 0 unexplained.

- **2026-07-01 — SB CORRECTED + POST-MORTEM: the audit found the CAPT bug + a date-mix on the headline name.**
  An audit of SB (the book's single most important actionable name) vs the Q1-2026 earnings deck + the
  6-K (acc 0001317861-26-000033) + FY2025 20-F (acc 0001628280-26-014408) found **two NAV-inflating
  errors**, both now fixed in one pre-registered 2026-03-31-snapshot correction (band $10.05-10.18
  committed bc33ca9; landed $10.1157; NAV $10.47→$10.12, still ~0.63× — thesis intact):
  1. **Blanket scrubber flag (the CAPT peer-borrowed-flag bug).** Manifest carried **29** operating
     scrubbers (all 16 Post-Panamax + 6 Kamsarmax) vs the 20-F's **20** ("21 vessels, all 8 Capes";
     Michalis H a scrubber-Cape now HFS). Corrected to the 20-F per-vessel set (fleet-table ftn-15):
     only **Pedhoulas Rose** among the Kamsarmax, 12 Post-Panamax. −$18M. SB CLEARED from
     `OPERATING_SCRUBBER_QUEUE` → `OPERATING_SCRUBBER_VERIFIED{SB:20}` — the number shrank but now traces.
  2. **Date-mixing.** The manifest reflected the 2026-06-12 fleet status but valued at the 3/31 balance
     sheet. Katerina (delivered Apr) was double-counted (operating + orderbook, $47.7M); Michalis H (the
     ONE 3/31 HFS, 6-K line 398) was omitted; Xenia + Pedhoulas Commander (sales agreed May) were
     mis-bucketed HFS. Rebuilt as one 3/31 snapshot: 44 operating + 1 HFS + 8 NB.
  **POST-MORTEM (why EDGAR-sourced yet backwards):** two DIFFERENT root causes. (a) The scrubbers are
  date-INDEPENDENT — the error was a pure verification miss: the onboarding verified the NEWBUILD
  scrubbers (even caught the peer-trap there, Amendment 2) but set the OPERATING scrubbers by blanket
  default and parked SB in the unverified queue, which was never worked. We READ the disclosed aggregate
  (20) but never cross-footed it against our per-vessel flags (29); the per-vessel data (20-F ftn-15) was
  never mined. (b) The composition IS date-dependent — the fleet DID change Mar→Jun (4 transactions), and
  the onboarding took the 6-K's fleet table (as-of the June-12 FILING date, not quarter-end) for a 3/31
  NAV. Both are the project's "provenance is attention-dependent" theme: attention went to the primed
  checks (newbuild scrubbers, the balance sheet), and the operating scrubbers + fleet-date-consistency got
  a close-enough pass. Two dated rules added to CLAUDE.md (fleet-snapshot-must-match-NAV-date;
  cross-foot-operating-scrubber-count-at-onboarding). Suite 439 passed / 25 xfailed; drift gate green
  (SB-only re-ratify). Record: `decisions/sb_reconciliation_prereg_2026-07-01.md`; commits bc33ca9 + f2fc0ac.

- **2026-06-30 — NAT DE-VOIDED: P0 full balance-sheet reconciliation (the first PROVISIONAL name cleared).**
  NAT's headline FV was VOID — the $17M newbuild advance was contradicted by the Q1-2026 cash flow and the
  $153M commitment traced to nothing. Pulled the **FY2025 20-F** (acc 0001140361-26-017809, filed 2026-04-29)
  + **Q1-2026 6-K** (acc 0000919574-26-003779) from EDGAR and reconciled the whole balance sheet; a 5-agent
  adversarial-verification workflow confirmed every figure before a NAV band ($2.72–2.86) was **pre-registered
  and committed (df2c616) AHEAD of the recompute** (landed $2.79, in band). Sourced (Mar-31-2026): cash
  $75M→$81.1M; working capital $25M→$53.6M; total debt $395M→$415.4M; leases $5M→$0.34M; **advances $17M→$0
  (contradicted)**; **newbuild commitment $153M→$0 PARKED** — NAT discloses the 2-Suezmax order (delivery
  H2-2028) but NOT the price (the 20-F/6-K/XBRL are silent while pricing the $25M/$40M vessel sales in the
  same note); the only figure is a Pareto 2025-11-04 LOI (~$86M/ship), which is not out of the figure-provenance
  queue, so the §9.6 on-curve mark is UNAUTHORIZED (owner decision — park both legs so NAV is independent of the
  unsourced number). Operating fleet 18→16 (2 oldest reclassified held-for-sale, booked at the **$65M contracted
  price** via a NEW `held_for_sale` model field — schema/nav/loader/test). Owner-directed tier mechanics: NAT
  leaves `NAV_DERIVED_VOID` (de-voided) and `NAV_FIGURE_ESTIMATE_QUEUE` + `OFF_CONVENTION_QUEUE` (newbuild parked
  out of the equation), gains `NEWBUILD_PRICE_PENDING` → **GOVERNED-WIDE·newbuild-indeterminate** (directional-only,
  NOT tight; newbuild price stays a tracked open item) and `POSITION_CYCLE_RELABEL` (reads "rich · cycle position
  (not a short)", §12). NAT is NOT a new actionable long — the surface stays SB+SBLK. Suite 435→438 passed /
  28→26 xfailed. Committed ISOLATED from the day's price refresh (owner: don't launder incidental market drift —
  incl. DHT/FLNG band flips — through a sourcing commit); the daily price drift is a SEPARATE deliberate re-ratify.
  Baseline re-ratified for NAT only. Record: `decisions/nat_reconciliation_prereg_2026-06-30.md`; commits
  df2c616 (pre-reg) + b44c3c4 (fix). **Reusable pattern for the queue's park-at-$0 newbuild names.**

- **2026-06-23 — POWERED multi-cycle P/B reversion test DEFLATES the one-cycle engine result → no edge.**
  Ran the Test-2 within-name reversion estimand on the deep Sharadar P/B proxy (`run_proxy_timeseries.py`,
  2008–2025, **72 quarters, 14 names, 804 name-quarters** — GFC + 2011–16 depression + COVID + 2021–22
  boom = multiple independent cycles → genuinely powered). **Result: per-name reversion IC +0.078,
  quarter-block 95% CI [−0.081, +0.236], t +0.97, p 0.166 → INCONCLUSIVE/≈null.** The engine's one-cycle
  +0.234 (t 2.30) does NOT survive multiple cycles — it was the single-cycle bootstrap optimism flagged in
  PRE_REGISTRATION_TEST2. Crude flagships ~zero/negative (DHT −0.07, INSW −0.03, TNK −0.03, NAT +0.01,
  FRO +0.00); only off-thesis LNG/container names positive (FLNG +0.40, GSL +0.24). Cross-sectional
  de-meaned +0.086 (echoes Amendment 3). Caveat: book proxy lags market NAV (the reason the engine uses
  market marks), so this kills the *book-value* reversion thesis, not provably the engine's market-NAV one
  — but the proxy is the only multi-cycle data we have and it shows no edge. **Net across all powered tests:
  no demonstrated edge, cross-sectional OR time-series.** harness + docs only; no engine/src change.
  Built `backtest/run_engine_timeseries.py` to test the on-thesis question Test 1's cross-sectional frame
  strips out: does cheap-to-its-own-NAV+strip predict a name's OWN forward return (price reverting to the
  engine's fair value). In-sample (2019Q3–2026Q1, 275 name-quarters): **per-name within-name reversion IC
  +0.234, quarter-block 95% CI [+0.015, +0.413], t 2.30, p 0.018, positive in 12/12 names**; cross-sectional
  (quarter-de-meaned) +0.008 (no name-selection beyond the cycle); cycle-timing +0.191. So the tool's
  *designed* job — cycle/asset-value timing of single positions — points the right way and clears nominal
  significance, **but it is not a clean verdict**: exploratory/post-hoc, one autocorrelated cycle (the
  quarter-block bootstrap is optimistic; 12/12 = one cycle ridden by correlated names, not 12 independent
  edges), and cycle-not-selection. `PRE_REGISTRATION_TEST2.md` locks the CONFIRMATION on data **not yet
  used** — out-of-sample forward quarters (evaluate at +8q, ~end-2028) or a multi-cycle paid vessel-value
  feed (Clarksons SIN / VesselsValue, ~2008+, 2–3 independent cycles) — with an EDGE/FAIL/INCONCLUSIVE
  rule. Honest standing: **not a name-ranker** (Test 1 null), **plausibly a cycle/value timer** (Test 2
  hypothesis); proof pending out-of-sample/multi-cycle. No engine/src change; harness + pre-reg only.
- **2026-06-23 — 2019-2020 quality: Allied TC recovered + LNG/container excluded (no-look-ahead) + precedence fix.**
  Three fixes to the 2019-2020 quarters and the value spine: **(1)** the Allied Weekly 'period market TC
  rates' table (the `12 months` row) now feeds 2019-2020 TC — those quarters are TC-anchored, no longer
  pinned to the through-cycle mean. **(2)** LNG/container names **FLNG/CCEC/GSL excluded** from all
  vintages (`build_vintage.UNCOVERED_SECTORS = {lng, containerships, …}`): no free house tabulates their
  vessel values, so their NAV fell back to LIVE 2026 curves (a multi-year look-ahead, worst in 2019-2020)
  — violating the no-look-ahead spine. Test 1 is now scoped to the tanker+dry universe it can vintage
  (3 sectors: crude/product/dry_bulk, 11-14 names/q). **(3)** Precedence bug fixed: HSN Allied is
  spotty/stale (some Weekly-format issues + a 2024W08 reused for 2024Q2+) and was overriding the Xclusiv
  value spine for 2022Q4+ via `allied`-first precedence — now **xclusiv-first for value, intermodal-first
  for TC**, with Allied the fallback (wins only the 2019-2020 quarters where Xclusiv/Intermodal are
  absent). `ingest_wayback` now also clears stale HSN Allied marks so the store matches the methodology.
  Re-ran Test 1: **Nq 23, IC −0.020 (t −0.30), CI [−0.135, +0.100]**; 2021+ clean +0.015 (t +0.22).
  **Verdict robust** — moved <0.001 across all three fixes; the result is not an artifact of the
  look-ahead or the precedence bug. Still INCONCLUSIVE, not anti-predictive, no demonstrated edge.
  +1 harvester test (Allied TC). Gate: main 315, backtest 13, harvester 60.
- **2026-06-23 — Intermodal TC enrichment: designated period-TC source feeds the forward; verdict robust.**
  Rebuilt the Intermodal parser (was an untuned keyword stub) as a poppler-text reader of its stable
  'TC Rates' table: 1yr TC per class, lowercase k = tanker / uppercase K = dry (disambiguates the 75k
  Panamax *tanker* from the 76K *bulker*), class mapped by dwt-band to the engine TC keys
  (Pana=Kamsarmax, Supra-Ultra=Ultramax per `build_vintage.HARV_TC_KEY`). **TC-only — no vessel_value**,
  so the value spine stays single-vendor (Xclusiv/Allied). Effect: (a) **fills 2025Q3–2026Q1 TC** —
  Xclusiv stopped printing its 1y-T/C prose after 2025Q2, so the forward there was pinned to the
  through-cycle mean — and (b) **cross-broker TC reconciliation** vs Xclusiv prose for 2021–2025Q2 (89
  groups, mean spread 16%, 43 disagreements, recorded as the discrimination diagnostic). Re-ran Test 1:
  **Nq 23, IC −0.021 (t −0.31), CI [−0.130, +0.096]** — moved only −0.014→−0.021 vs pre-enrichment,
  confirming TC perturbs EV% *magnitude not sign* (the verdict is not a TC-fallback artifact). Still
  INCONCLUSIVE, not anti-predictive. +1 harvester test. Gate: main 315, backtest 13, harvester 60.
  Remaining TC houses (Banchero/Advanced/Fearnleys, Weber unavailable) optional for further reconciliation.
- **2026-06-23 — Grouped-era text parser closes the 2024Q1/Q2/Q4 + 2026 gaps → Test-1 window Nq 23.**
  The Xclusiv 2024+ *transposed/grouped* secondhand layout (age-row blocks with a FLOATING class
  label, two-column S&P prose bleed) was handled by a fragile pdfplumber geometry pass that silently
  produced 0 vessel_value for 2024Q1/Q2/Q4 + 2026 (only 2024Q3/2025 worked). Replaced it with a
  poppler-text **block walk** (`xclusiv._secondhand_grouped`): segment on each "Resale", class = the
  first *line-start* PRIMARY-tier label in the block (line-start excludes the prose; primary-only
  avoids the secondary tier label — Panamax/Supramax — floating into the next block). ~40 marks/q, 8
  clean classes; geometry kept only as a fallback. Coverage is now **contiguous 2021Q3→2026Q1**.
  Re-ran Test 1: **Nq 23 (2019Q3–2026Q1), IC −0.014 (t −0.21), CI [−0.123, +0.103]**; 2021+ clean
  subset Nq 19, IC +0.019 (t +0.27). Still INCONCLUSIVE, not anti-predictive; tighter CI excludes a
  *large* effect. +1 harvester test (grouped, with the floating-label trap). Gate: main 315, backtest
  13, harvester 59. `backtest/REPORT.md` Test 1 updated.
- **2026-06-23 — Test-1 POWERED backfill: engine EV% over 15–19 quarters (was Nq 5), still INCONCLUSIVE.**
  Took the engine EV% ex-post test from Nq 5 to **Nq 15 (2021Q3–2025Q4, clean) / Nq 19 (adding
  2019–2020)**. Result: sector-neutral pooled IC **+0.040 (t +0.60)** on the clean window,
  **−0.004 (t −0.06)** including 2019–2020; both INCONCLUSIVE, **neither anti-predictive** (never
  near the FAIL threshold). Mildly positive on the actual tool signal in the recent window; ~null
  with the lower-quality COVID-era quarters. Power compounds forward. Write-up: `backtest/REPORT.md`
  Test 1. The work that bought the power:
  - **Archive reality corrected:** the free HSN broker archive effectively starts **2021** (2019–2020
    are a void; the feasibility memo's "reaches 2018" was the category total-count misread). Capital
    Link's live API is now bot-gated (HTTP 202). Memory `project_test1_archive_depth`.
  - **Xclusiv flat-row parser (2021–2023)** — new poppler-text path (pdfplumber scrambles these
    issues' glyph order); full resale/5/10/15yr curves, all 10 classes incl. VLCC/Suezmax/Aframax,
    ~42 marks/quarter. The 2024+ transposed-era geometry parser is unchanged. `base.extract_text_poppler`
    added (reusable). +1 harvester test.
  - **2019–2020 recovered via the Wayback Machine** — Allied *Weekly Market Report* (not the no-value
    SnP supplement), 4 quarters (2019Q3/Q4, 2020Q2/Q3). `allied.py` rewritten to the Weekly value-grid
    format (HSN S&P-stats issues correctly yield nothing); `wayback_allied.py` (CDX download) +
    `ingest_wayback.py` (quarter-select + store) added. Allied test updated.
  - **Bridge export** made reproducible: `cli export-marks --brokers …` writes `_factor_marks.json`
    (was ad-hoc). Single-vendor by era (Xclusiv 2021–2025, Allied 2019–2020) per the locked caveat.
  - **Known gaps (next):** 2024Q1/Q2/Q4 + 2026 lack vessel_value (the transposed geometry parser
    misses those issues; a grouped-era text parser is the cheapest +3–4 clean quarters). 2019–2020
    carry no vintaged TC (neutral forward) + a 6–7yr live-curve look-ahead on *uncovered* classes
    (LNG/container) — flagged-not-trusted, which is why 2021–2025 is the headline window.
  - Gate green: main 315, backtest 13, harvester 58 (+2). No `src/` engine change.
- **2026-06-23 — `shipping_harvester` source brought into git (was untracked everywhere).**
  The harvester had no version control anywhere (gitignored subdir, no nested repo), so the
  Test-1 parser work (xclusiv geometry secondhand extractor, spot `avg|average` markers,
  `_period_tc`) was working-tree-only and at risk. Changed `.gitignore` `shipping_harvester/` →
  `shipping_harvester/data/` (ignore only the 62M crawl cache + third-party broker PDFs) and
  committed the **~452K source** (27 files: the package + tests + requirements.txt). Reverses
  the 2026-06-21 "stays out of this repo's history" stance — which fit a passive cross-check but
  not actively-developed parser code Test 1 depends on; versioning the source is orthogonal to
  the deps concern (it still runs only on `.venv310`, not in `src/`). PLAN.md ⚠ HANDOFF box +
  CLAUDE.md two-venv note updated. Owner decision.
- **2026-06-23 — Handoff doc consolidation (clean-handoff pass).** Verification gate green
  (main 315, backtest 13, drift gate 0 unexplained). Rewrote the sprawling PLAN.md Phase 3(c)
  bullet into a scannable handoff with a prominent **⚠ HANDOFF box** flagging what is NOT in this
  repo's git (the gitignored `shipping_harvester/` + its working-tree-only parser work, `.venv310`,
  the regenerable bridge artifacts) + a reproduce-the-pipeline command list; refreshed the
  current-state line (2026-06-23), the verification-gate section (added the backtest/harvester
  suites + the gitignore note), and the README/LIMITATIONS ex-post line (engine signal now has an
  underpowered n=5 INCONCLUSIVE read, not "untested"). No code change.
- **2026-06-23 — Phase 3(c) quarterly-grain balance sheet (direct Sharadar ARQ pull).** The
  cache held only ANNUAL BS, so a mid-year vintage used a balance sheet up to ~12 months stale.
  Ran a **direct Sharadar SF1 ARQ pull** (`backtest/pull_bs_quarterly.py`, via factor-portfolio's
  fetcher + the owner's key) for the 17 names → 837 quarterly rows (cash / total debt / shares,
  point-in-time by `datekey`) → `backtest/vintages/_bs_quarterly.csv` (gitignored).
  `build_vintage.vintaged_bs_core` now **prefers the quarterly grain**, annual ARY fallback for
  the annual-only FPIs **NAT/TEN** (0 ARQ rows, as the memo warned). De-stales the BS leg: DHT
  2025-Q2 now uses the Q1'25 BS (debt 364M) vs the stale FY'24 annual (409M). Re-ran
  `run_engine_test1`: **mean IC +0.005, t 0.02, Nq 5 → INCONCLUSIVE** (fresher BS shifts
  NAV/share; still near-zero at n=5). The BS leg is now as point-in-time as Sharadar allows.
- **2026-06-23 — Phase 3(c) point-in-time balance-sheet core (Sharadar).** `build_vintage`
  now vintages **cash, total_debt** (Sharadar `LongTermDebtNoncurrent + DebtCurrent`) and
  **diluted shares** per name, point-in-time (ARY, filed-date <= quarter-end, no look-ahead),
  overwriting the slow-rolled base. (Cash was initially thought absent — it is cached under
  `CashAndCashEquivalentsAtCarryingValue`, a field-name mismatch, now included; DHT 2024Q3 cash
  $74.7M.) The shipping-specific lines (working capital, newbuild commitments, leases) stay
  slow-rolled. **Confirmed I can run a direct Sharadar SF1 pull** (key
  `NASDAQ_DATA_LINK_API_KEY` in `~/.config/factor-portfolio.env`, factor-portfolio's
  `fetch/sharadar.py`, deps in `.venv310`) — live-fetched DHT to verify — so the cache can be
  extended (quarterly ARQ grain, SG&A/interest/tax for the strip) on demand. Verified per-quarter variation
  (DHT debt 428.7M @2024Q3 → 409.4M @2025Q2; shares ~160M). Re-ran `run_engine_test1`:
  **mean IC +0.056, t 0.31, Nq 5 → INCONCLUSIVE** (shifted from +0.086 as vintaged debt/shares
  move NAV/share; still near-zero at n=5). Debt + share count were the dominant held BS drivers;
  residual held = cash, working capital, fleet ages, newbuild/lease lines.
- **2026-06-23 — Phase 3(c) 12M-TC anchoring — the scenario forward is now TC-consistent.**
  Replaced the spot anchor (which mismatched the TC-anchored cycle means, the §10 gotcha) with
  vintaged 12-month TC. Source: not Allied (its `period_tc` is one stale 2024-02-20 issue,
  mis-parsed to a constant — dropped from the panel), but **xclusiv's 1y-T/C prose**, which the
  parser ignored. Added `xclusiv._period_tc`: each `USD n/day` level is a TC mark only when
  "1y T/C" is the nearer rate-type keyword before it (vs the spot "T/CE"), class = nearest class
  word; a sanity band + change-figure guard ("…firmer…, at USD …") + a 115-char back-window
  handle the 2024 vs 2025 prose variants. Yields full tanker 12M TC (VLCC/Suezmax/Aframax/LR2/MR,
  on the TC scale ~29–49k) for **2024-Q3 / 2025-Q1 / 2025-Q2**; xclusiv dropped the 1y-T/C prose
  after 2025-Q2, so **2025-Q3/Q4 fall back to the through-cycle mean** (neutral, not spot, to
  avoid a TC-vs-spot level confound). `build_vintage.synthesize_scenarios` now anchors on
  `vintaged_tc` (mean fallback). Re-ran `run_engine_test1`: VLCC forward now on the TC scale
  (2024Q3 base 48312 ≈ TC 49.5k; 2025Q4 base = mean 40k); **mean IC +0.086, t 0.42, Nq 5 →
  INCONCLUSIVE** (unchanged near-zero at n=5, as the cross-sectional NAV signal dominates). The
  methodology mismatch is fixed; remaining fidelity gap = the held balance sheet (Sharadar BS
  vintaging). Harvester 57 tests green. Allied excluded at the export step (note in
  `build_vintage`).
- **2026-06-22 — Phase 3(c) neutral scenario-forward synthesis + vintaged spot — first
  *legitimate* Test-1 read (still small-n).** Removed the dominant contaminant (held 2026-Hormuz
  scenario levels). **(#2 vintaged rates):** found the Allied `period_tc` is a constant mis-parse
  (VLCC 5934 every quarter — signal-free) and xclusiv carries no period TC; but the 2025 xclusiv
  redesign abbreviates "average T/CE"→"avg T/CE", so a one-line marker fix
  (`(?:average|avg)`) unlocked **consistent vintaged tanker spot across all 5 quarters**
  (VLCC 38.6k→42.9k→35.1k→89.3k→95.9k). **(#1 synthesis):** `build_vintage.synthesize_scenarios`
  replaces the held curves with one neutral scenario per sector whose per-class forward glides
  the vintaged spot toward the through-cycle TC mean (±25% band) — DATA_CONTRACT_TEST1.md's
  neutral forward. Scale verified: the cycle-anchor means (VLCC 40k) are on the same $/day scale
  as xclusiv spot, so the synthesized forward yields realistic vintaged cycle positions (2024Q3
  VLCC ~0.97×, 2025Q4 ~2.4×). Re-ran `run_engine_test1`: EV%s no longer uniformly-BUY; per-quarter
  ICs vary (+0.50/+0.68/−0.32/−0.24/−0.16); **mean IC +0.092, t 0.44, Nq 5, CI [−0.155,+0.223],
  hit-rate 49% → INCONCLUSIVE** (expected at n=5). Now a legitimate vintaged read (real NAV marks
  + real vintaged spot-derived forward + real price), no longer plumbing-validation. Caveats:
  SPOT-anchored not 12M-TC (no reliable vintaged TC), BS held, n=5. Remaining for fully-faithful
  Test 1: 12M-TC anchoring, Sharadar BS vintaging, the 2018–2023 backfill for power.
- **2026-06-22 — Phase 3(c) factor→vintage glue + first end-to-end Test-1 chain run
  (plumbing-validation).** Built `backtest/build_vintage.py`: reads the harvester's resolved
  marks (`_factor_marks.json`, exported from `.venv310`), converts to engine
  `vessel_value_curves` (class-rename Capesize→Cape / Kamsarmax→Pana / Ultramax→Supra-Ultra,
  resale→newbuild proxy, musd×1e6), **merges** over the live curves (uncovered classes keep
  live marks so NAV never breaks), re-keys `scenario_inputs` to the vintage's strip quarters
  (so the Phase-3b as-of routing fires), sets `current_price` to the Sharadar raw close at the
  quarter-end, and assembles the full vintage tree (fleet/cost/dividend held; balance sheet
  quarter-renamed). Generated 5 vintages (2024Q3, 2025Q1–Q4 — the valuation-grade quarters) and
  ran `run_engine_test1`: **the whole chain executes end-to-end on real data** (PDF → harvester
  → factor → glue → as-of engine → EV% → within-sector IC) for all 16–17 names, no errors.
  Result **mean IC +0.220, t 1.70, Nq 5, CI [+0.014, +0.294] → INCONCLUSIVE**. **This is a
  PLUMBING-VALIDATION read, NOT a valid Test-1 result:** only vessel_value + price are vintaged;
  TC, scenario *levels*, and balance sheets are held from live (held 2026-peak scenario levels
  value fleets against lower 2024–25 prices → near-universal BUY), so the number is not
  interpretable as signal — it proves the chain works. For a valid result still needed: synthesise
  the neutral mean-reversion scenario forward (vs held levels), vintage the TC (fix the Allied
  parser), vintage the balance-sheet core (Sharadar), + more quarters/houses. Generated vintage
  trees + the schema JSON exports are gitignored (reproducible via `build_vintage`); the glue
  code is committed.
- **2026-06-22 — Phase 3(c) first parser extension: xclusiv geometry-based age-curve
  extractor — unlocks the tanker vessel-value curves.** Closed the highest-leverage coverage
  gap. The pre-2025 Xclusiv secondhand-values table is a **two-column text layout** (value
  table left, S&P prose right) that pdfplumber does NOT detect as a ruled grid, so the existing
  `_secondhand(tables)` extractor missed it entirely (newbuild-only output). Added a
  **word-geometry** extractor (`xclusiv.XclusivParser._secondhand_geom`, wired via a `parse()`
  override that has the pdf_path): isolates the left value column by x-coordinate, reads the age
  label (Resale/5/10/15yr at x0≈85) + the current value (first numeric to its right),
  reconstructs one class per Resale→15yr block, and applies a **monotonic-curve sanity filter**
  so mis-joins drop rather than corrupt. Result on the real 2024-Q3 issue: **36 vessel_value
  marks** (was newbuild-only), incl. the **complete tanker age curves VLCC/Suezmax/Aframax/MR
  (resale/5/10/15yr)** — the previously-absent marks the engine's age-curve NAV needs for the
  crude/product watchlist names. Dry then completed too: the dump revealed the table groups
  **Kamsarmax/Panamax and Ultramax/Supramax into single curves — the same Pana / Supra-Ultra
  tiers the engine uses** — so assigning each block its *topmost* label (not block-center) yields
  full curves for Capesize→Cape, Kamsarmax→Pana, Ultramax→Supra-Ultra, Handy, with the text
  newbuild merging in. **All 8 classes (4 tanker + 4 dry tiers) now carry full age curves**,
  verified through the factor schema (re-parsed 10 cached issues → 183 vessel_value rows, 80
  tanker age-curve rows). Harvester's own xclusiv + dispatch tests stay green (15). **The harvester is gitignored
  (vendored cross-check), so the parser code lives in the working tree, not this repo's history;
  the committed deliverable is the coverage win + (next) the assembled vintages.** Remaining:
  dry class-naming, fix intermodal/banchero/weber, per-era 2018–2023, then the factor→vintage
  glue + `run_engine_test1`.
- **2026-06-22 — Phase 3(c) MVP backfill kicked off — pipeline proven, parser coverage
  measured as the binding constraint.** Ran the harvester end-to-end: small validation crawl
  (HSN, recent quarters) then the full MVP crawl `run --since 2024Q1 --until 2026Q2
  --max-pages 70 --capitallink` (1,412 raw issues, 60 (broker,quarter) mark-sets stored; crawl
  → dedupe → download → parse → store → panel/coverage/factor all working under `.venv310`).
  **Measured coverage (2024Q1–2026Q2):** only **xclusiv + allied** parse; intermodal /
  banchero / weber / fearnleys / advanced yield 0 (parser gaps / generic fallback).
  `period_tc` = VLCC/Suezmax/Aframax (tanker 1yr); `spot_tce` = 9 tanker+dry classes (broad);
  **`vessel_value` = Capesize/Handy/Kamsarmax/Ultramax, NEWBUILD anchor ONLY** — no tanker
  vessel values and no 5yr/10yr age anchors anywhere. **This is not valuation-grade:** the
  engine's age-curve NAV needs newbuild+5yr+10yr+scrap per class, so the MVP vintage cannot be
  assembled from current parser output. The memo's estimate (per-era parser development is the
  ~2–4 wk bottleneck) is now an empirical fact. The factor→engine glue is fully specified
  (class-rename `Capesize`→`Cape` etc., dwt injection, `musd`×1e6) and ready; it is gated on
  parser coverage, not the other way round. Harvester crawl cache is gitignored
  (`shipping_harvester/data/`).
- **2026-06-22 — Phase 3(c) env gate cleared: Python 3.12 provisioned for the harvester.**
  Owner chose provisioning a 3.10+ interpreter over a 3.9 backport. Installed CPython 3.12.13
  via `uv` into a dedicated **`.venv310`** (gitignored) with the harvester's deps (requests,
  beautifulsoup4, lxml, pdfplumber, pandas, pyarrow); the engine + the 315-test suite stay on
  `.venv` (3.9.6), untouched. The vendored `shipping_harvester` now imports under 3.12, its
  **57 tests pass**, and it parses real broker-weekly PDFs (smoke-tested on
  `state/fdprobe/Allied_2025.pdf`). That smoke test also confirmed the data contract's per-era
  reality: a non-2024-tuned format (the 2025 Allied sample) parses `confident=True` but yields
  only partial TC marks and no age-anchors — i.e. the env is unblocked, but **per-era parser
  tuning remains the real backfill work** (the 2024+ era is the tuned one). CLAUDE.md "How to
  run things" documents the two-venv split. Remaining for a result: the free-broker-weekly
  backfill (crawl 2024-Q1+ → vintages) per `backtest/DATA_CONTRACT_TEST1.md`.
- **2026-06-22 — Phase 3(c) Test 1 pre-registration + data contract + harness (engine EV%
  ex-post test; method locked, data pending).** Owner committed to the **free broker-weekly**
  data path. Wrote `backtest/PRE_REGISTRATION_TEST1.md` (locked before any result, git-order
  proof): the test of the tool's OWN signal — within-sector pooled IC of engine EV%-cheapness
  vs 1q-forward total return, valued as-of via the Phase-3b plumbing; decision rule **FAILs
  only on a significant anti-predictive result** (mean IC<0, t≤−2), EDGE on significant
  positive, INCONCLUSIVE the expected MVP outcome. Wrote `backtest/DATA_CONTRACT_TEST1.md`:
  per-vintage source / no-look-ahead / slow-roll spec mapped to the free broker-weekly sources
  (vessel marks + TC + spot are the only sign-moving per-quarter legs; BS core from Sharadar;
  fleet/cost/dividend slow-rolled; FFA + scenario forward are *derived* via mean-reversion
  synthesis — the live 2026 MoU scenario set is NOT back-projected, a locked departure). Built
  `backtest/run_engine_test1.py`: reads `backtest/vintages/<q>/`, runs the as-of engine
  (`run_scenarios_watchlist(asof_quarter=q, inputs_dir=…)`), computes the pre-registered
  statistic; the load-bearing EV%-cheapness sign convention (high EV% = cheap, via `−EV%` into
  the reused `wide_quarter_ic`) and the decision rule are unit-tested; runs clean with no
  vintages. +2 backtest tests (11→13; main `tests/` unaffected at 315). **Binding execution
  gate surfaced:** the vendored `shipping_harvester` is Python 3.10+ (`@dataclass(slots=True)`
  → TypeError under this Mac's 3.9.6), so the vessel-mark/TC vintage production needs a 3.10+
  interpreter or a small 3.9 backport — everything downstream already runs in the 3.9 venv.
  Design basis: `outputs/test1_data_feasibility_memo_2026-06-22.md`.
- **2026-06-22 — Phase 3(b) engine as-of-quarter plumbing (the prerequisite for the powered
  engine EV% test).** The scenario path hard-anchored the strip/scenario timeline to "now"
  (`QUARTER_KEYS = q3_2026…`), so it could not value a name as-of a historical quarter.
  Parametrized `scenarios.quarter_keys(n, start_q=3, start_y=2026)` (no-arg/single-arg calls
  unchanged) + added `scenarios.strip_start_from_asof(asof_quarter)` (report quarter + 2 ⇒
  q3_2026 for the live 2026-Q1 vintage) and an `asof_quarter` parameter threaded
  `run_scenarios → _run_scenarios_for_ticker → run_scenarios_watchlist`. `None` (default) =
  the live q3_2026 anchor, **byte-identical** to prior behaviour (315 tests green; `pipeline
  2026-Q1` 0 material deltas; drift gate 20/20 at +0.0pp/+0.0%/+0.000). A non-default as-of
  whose scenario doc lacks the vintage's forward-quarter curves **fails fast** naming the
  missing keys (the expected 3c "no historical data" failure mode — never silent mis-routing).
  The single-point NAV/strip path needed no change: the strip is positional and already
  as-of-correct via the `quarter` arg; only the scenario quarter-key *labels* (which index
  `scenario_inputs.yaml`) were calendar-anchored. +4 tests (311→315). 3(c) — the powered
  engine EV% test — now needs only the vintage scenario-curve backfill (its own go/no-go).
- **2026-06-22 — §16 overlay ledger: §12 dividend-window is now a control, not docs
  (closes audit E-2 for this overlay type).** `overlay_ledger.py` gains
  `dividend_window_rows(quarter)`, which auto-derives a **§12.6** row per gated name
  from the COMPUTED `dividend_window.build_rows` classification (same pattern as the §15
  governance auto-rows). NAT now renders as a *neutral* row — "TRIM stands (value trap)
  — premium NOT rate-supported (Q*>strip > H=8.0); no floor, no FV change" — with a "·"
  arrow (render gained a neutral direction). The **stale hand-written NAT §12 row**
  (`direction: up`, "treat tool FV as the NAV floor") is removed from `inputs/overlays.yaml`:
  it directly contradicted the computed TRIM-stands classification — the exact
  documentation-vs-control drift E-2 named. SBLK's peak-cycle note relabelled **§12.2**
  to disambiguate it from the §12.6 dividend-window gate (SBLK is not a high-payout
  single-class pure-play). `overlay_ledger.main` takes `--quarter` (defaults to latest
  balance-sheet quarter). +3 tests (308→311).
- **2026-06-22 — Phase 3(a) value-premium proxy test (Option C; powered, on the actual
  universe).** Pre-registered **Amendment 3** to `backtest/PRE_REGISTRATION.md` and committed
  it (`db9c4f6`) *before* writing any result-producing code — the same git-order discipline as
  Amendments 0–2. Then built `backtest/loaders_sharadar.py` (point-in-time book value + prices
  from factor-portfolio's `v2-validation-first` Sharadar cache, read directly from the cache
  CSVs with `filed`-date no-look-ahead — avoids a 3.10+ cross-repo import) and
  `backtest/run_proxy_powered.py`, reusing `evaluate_wide.wide_quarter_ic`/`mean_t` and
  `loaders.bvps_at`/`price_at`/`quarter_ends`. The Amendment-2 powered null ran on a 9-name
  SEC-XBRL panel that excluded DHT/FRO/ECO and all product; Sharadar standardizes the FPI
  20-F/6-K filings, so this runs on **17 of the 20 watchlist names — all 5 crude flagships +
  full product + dry-bulk + LNG — over deep history** (NAT→1997). **Result: a powered
  near-null** — sector-neutral pooled P/B IC **+0.036, t 0.62, Nq 72** (2008–2025), quarter-block
  bootstrap 95% CI [−0.079, +0.151], split-half unstable (early +0.090 / late −0.018); the raw
  whole-panel read +0.059 (t 1.36) is not significant. Excludes a *moderate* within-sector value
  premium, blind to a small one. It is a **book proxy** (book≠market NAV), so it bounds the
  value-premium *premise*, NOT the engine's marks — the powered engine EV% test (Phase 3 b/c)
  remains the only read that can validate/refute them. +3 cache-guarded backtest tests (backtest
  suite 8→11; the main `tests/` suite is unaffected at 308 — `testpaths=["tests"]`). Updated
  `backtest/REPORT.md` (Amendment 3 + combined verdict), README, LIMITATIONS §1 ("no demonstrated
  ex-post edge" now backed by a powered test on the right universe), PLAN.md.
- **2026-06-22 — Phase 2 ongoing accuracy gate (Option B; closes audit A-2).** The
  tool had no automated accuracy gate after sector launch — the one-time calibration
  lock is manual and never auto-invoked, and the >2pp drift alert ran against a
  gitignored, self-overwriting snapshot (`state/last_reconcile.json`), so drift had no
  durable anchor and no teeth. Built a **committed, Pareto-free drift gate**:
  `src/crude_tanker_fv/drift_gate.py`, the tracked `baselines/reconcile_baseline.yaml`
  (20 names — EV% / tool NAV / position band / k_broker, plus meta: ratified_at /
  ratified_commit / quarter / cause), `tests/test_drift_gate.py` (17 tests; +291→308),
  and `scripts/ratify_baseline.sh` (deliberate re-ratify, mandatory cause, human
  commits). The gate tracks the tool's **own** EV%/NAV/band against its committed prior
  (never broker NAV) and k_broker on its **second difference** (the *change* in the
  tool↔broker spread, never its level) — so a persistently-wide documented §6 spread
  (INSW k≈1.64, NAT k≈2.16) sits green forever and the gate never asks a number to move
  toward Pareto; only an *unexplained change* fails. Thresholds (ΔEV>2pp / ΔNAV>2% /
  Δk>0.05) live in the baseline `thresholds:` block (tunable without a code change). A
  breach clears via a dated, non-placeholder `decisions/<ticker>_log.md` annotation on/
  after `ratified_at`, or by re-ratifying with a cause; APPROX names (the reconcile set,
  single-sourced) are tracked on self-consistency only (no Δk gate). Baseline ratified
  from the current 2026-Q1 outputs @ d382bfd. Wired into CLAUDE.md "How to run things" +
  the Verification loop, and PLAN.md. Reuses the reconcile drift-delta pattern
  (`reconcile.py:144-150`) and `reconcile.APPROX_PNAV_TICKERS`. Design of record:
  `outputs/epistemic_soundness_memo_2026-06-22.md` §4 Option B.
- **2026-06-22 — Phase 1 honest framing (Option A; the direct fix for the CRITICAL
  epistemic finding).** Doc-only. Added an "independence and ex-post validation status"
  note to README + LIMITATIONS §1: the NAV is independent of broker *opinion* but not
  broker *data* (~76% of anchoring prints single-vendor-sourced, ~87% in dry-bulk/product;
  six shared-source names), so "independent" is narrow, and the tool has **no demonstrated
  ex-post cross-sectional edge** (auditable opinion, not backtested forecast). Retired the
  unqualified **"transaction-validated"** doctrine phrase → **"transaction-anchored
  (single-vendor-sourced)"** (CLAUDE.md "philosophically", METHODOLOGY Appendix A). README
  test count 286→291. *(Per-name corroboration-tier tags in `delta_report.md` deferred — a
  renderer change; the tiers are stated in the README/LIMITATIONS note for now.)*
- **2026-06-22 — Phase 0b inert cheap fixes (audit BUG-4/5/6/7 + G-1; framing BUG-8).**
  No valuation change (291 tests green). **BUG-4:** the §15 report blend line printed raw
  NAV while FV used the post-haircut value → now prints `nav_per_share_effective` so it
  foots for TEN/CMDB. **BUG-5:** value-pinned the Crude Set A weights (0.25/0.45/0.18/0.12)
  — sum-to-1 alone let a silent crude weight edit pass (LNG/product were already pinned).
  **BUG-6:** `loaders._list_map` silently dropped a partially-null FFA curve → now raises
  (a partial-null is a data error, not "class not covered"). **BUG-7:** the two decoupled
  `0.11` constants (`nav.NEWBUILD_DELIVERY_DISCOUNT_RATE`, `dividend_strip.DEFAULT_DISCOUNT_RATE`)
  now both reference `nav.COST_OF_EQUITY`. **G-1:** `compute_cycle` raises on an empty fleet
  instead of silently falling to the trough band. **BUG-8:** corrected the CLAUDE.md/PLAN.md
  backtest framing to match `REPORT.md` — the powered Amendment-2 null is a clean negative on
  a P/B proxy / different universe, not "expected small-sample" (which only fits the
  underpowered real-P/NAV tests).
- **2026-06-22 — BUG-1 (Aframax dual cycle-anchor) + BUG-2 (Sinokor row in the VLCC
  fit) fixed** (methodology audit, `outputs/METHODOLOGY_AUDIT_2026-06-22.md`).
  **BUG-1:** `historical_tce_means.yaml` carried a stale Aframax 10yr-mean of **27,600**
  while `scenario_inputs.yaml` `aframax_dirty` carried the B5-curated **36,483** — so the
  per-name FV / breakeven / sensitivity path (`compute_cycle`) and the scenario path
  computed *different cycle positions* for every Aframax-exposed name (TNK/TEN/INSW/HAFN/
  STNG). Reconciled to 36,483 (VLCC/Suezmax already matched) + new guard
  `test_cycle_anchor_cross_file_consistency`. **BUG-2:** the Sinokor en-bloc VLCC row
  (`vlcc.yaml`, age 12, $71M, labeled "documentation only — excluded") was actually IN the
  regression — the loader filtered on the age window only. Added an `in_fit: bool` flag to
  `TransactionPrint` + loader + `fit_curve_anchors`; set `in_fit: false` on the Sinokor row
  and the FRO-NB doc row. VLCC fit drops the $71M age-12 drag → age-10 anchor up → VLCC NAVs
  **+0.3–1.1pp** (DHT $12.93→$13.10; DHT report FV 14.00→14.15). All **under the 2pp drift
  gate; SANITY 0 fail; no position flips.** Tests 290 → 291.
- **2026-06-22 — cycle-conditional terminal + net retained earnings (§9.2) + §12
  reframed to a falsifiable dividend-window test (R3).** Part of the
  methodology-soundness audit (`outputs/METHODOLOGY_AUDIT_2026-06-22.md`). Resolved a
  doc-vs-code contradiction the audit found: METHODOLOGY:2115/824 claimed the strip
  terminal was "depleted by the dividends paid out" + "mean-reverts," but the engine
  aged hulls at a flat price level with the balance sheet held constant. Owner chose to
  make the engine honest, not walk back the docs.
  **Terminal (`dividend_strip.py` / `cycle.py`):** (1) **cycle-conditional multiple** on
  the terminal FLEET value — peak 0.90× / elevated 0.95× / mid 1.00× / below-mid 1.05× /
  trough 1.10× via `cycle.terminal_multiple` (cash/debt not reverted); (2) **net retained
  earnings** — terminal cash += Σ(EPS−DPS)/share (flat for ~100%-payout names, RISES for
  low-payout retainers — fixes the §12 buyback/low-payout undercount — falls for over-payers).
  No double-count (strip = PV(8q earnings) + PV(terminal asset), the standard
  explicit-period-plus-terminal DCF). The literal "subtract dividends" form was rejected as
  a double-count (owner decision). **Book impact (SANITY 0 fail; NAV untouched):**
  low-payout retainers up — **CCEC +31pp; GSL TRIM→BUY; TNK HOLD→BUY; STNG TRIM→BUY**;
  MPCC/FLNG/CMDB/HAFN/TRMD/INSW up — peak crude down — **DHT FV 14.31→14.00** (0.9×),
  FRO/ECO slightly down. Re-pinned: `test_terminal_multiple_cycle_conditional` +
  `test_terminal_retains_earnings_low_payout`; CCEC/INSW/STNG FV bands; DHT report FV;
  breakeven/sensitivity helpers (aligned to pass `terminal_multiple`).
  **§12 reframe (R3):** the owner-challenged §12 line ("TRIM signals … commercially
  misaligned") — an unfalsifiable one-way bullish override (audit E-3) — was reframed after
  a 4-agent analysis (`outputs/peak_cycle_high_payout_resolution_2026-06-22.md`) found the
  **model is right**: a high-payout pure-play at peak P/NAV ~2× is overvalued through-cycle
  (the fat yield is "the liquidation rate of a melting ice cube," ~−36% on the NAT
  arithmetic; NAT is its own 2015→2018 counterexample). The 0.9× terminal is **vindicated
  and not exempted** for high-payout names (exempting = the forbidden back-solve). §12 is now
  a falsifiable, computed classification: **§12.5** trigger gate (single-class + payout>90% +
  cycle>1.5× + price/tool-NAV>1.5×), **§12.6** break-even-dividend-window test (Q* vs the
  FFA-supported horizon H), **§12.7** ex-post falsification. New `dividend_window.py`
  (diagnostic-only, no FV change, consensus_eps-style) → `outputs/dividend_window_test.md`:
  **NAT gates in (premium 2.51×) → Q*=None (DPS never bridge the $3.13 premium) → TRIM stands**
  (value-trap, no override); DHT (1.27×) / SBLK (diversified) / all others gate out. Tests 287 → 290.
- **2026-06-22 — §9.6 time-to-delivery discount ROLLED OUT to the other newbuild
  books (owner-approved, post-BRUT).** Applied per-vessel `years_to_delivery` to
  CAPT / FRO / MPCC manifests (GSL's NB order is post-snapshot; CMDB has none).
  Moves, all SANITY-OK: **CAPT NAV $17.74 → $15.05, gap −2.6% → −17.3%** (the
  material one — NB-heavy; the discount makes the tool *more conservative on NB
  timing than Pareto*, opening a documented divergence where CAPT was a tight
  validator — a call, not a bug; position held BUY); **MPCC $2.27 → $2.02**
  (−9.4pp; test_mpcc_gsl baseline re-pinned); **FRO $24.40 → $24.08** (−1.1pp,
  negligible — its NBs deliver Apr'26-Q1'27). `reconcile --all`: 20 names, 0
  SANITY FAIL, 2 drift alerts (CAPT/MPCC) annotated with the methodology cause.
  286 tests green. Cohort `years_to_delivery` are estimates (CAPT from the
  Q1-release schedule; MPCC from the deck's ~qN hints) — refine at the Q2 reports.
- **2026-06-22 — BRUT (Bruton Ltd) onboarded as the 20th name + §9.6
  time-to-delivery newbuild discount resolved (BRUT-first).** Bruton =
  pure-play VLCC newbuild vehicle (Trøim/Magni; Koch 26% / Trøim 20% / float
  54%), Oslo Growth, 12 firm VLCC NB (0 on the water), deliveries Jul-2026 →
  Q3-2029. Real per-vessel fleet from bruton-ltd.com/fleet/; financials from the
  Pareto initiation 2026-04-22 (half-yearly reporter — H1-2026 due Aug-13
  confirms). **The build first hit SANITY=FAIL +116%**: the §3.1/§9.6
  delivered-less-commitment convention credited the full delivered-today VLCC
  mark ($175M) to ships arriving up to 3 years out — on a 100%-NB balance sheet
  the ~30% mark premium over Pareto's ~$143M/VLCC levered ~2.5x ("max torque").
  **Fix (owner-directed, resolves the long-open §9 #6):** `compute_nav` now
  PV-discounts a not-yet-delivered NB's delivered value by `1.11^(−years_to_delivery)`
  per vessel (`NEWBUILD_DELIVERY_DISCOUNT_RATE`; commitment kept at face); the
  strip terminal advances `years_to_delivery`. **Backward-compatible** —
  `years_to_delivery` defaults to 0 (on the water → factor 1.0), so the other 19
  names are byte-identical (286 tests green, all pins held). BRUT lands NAV $9.40
  vs Pareto $7.20 = **+30.6%, SANITY OK**, BUY (EV +97%). New manifest field +
  loader; schemas.Vessel.years_to_delivery; data_sources + NAME_ALIASES +
  earnings-calendar (Aug-13) wired; §15 partial (provisional 0%, fee/control
  pending the prospectus). **Mistake corrected mid-task:** I began unilaterally
  reverting BRUT on the +116% FAIL — Dan stopped me; a failed gate is a finding
  to surface, not a trigger to back out (memory saved). **ROLLOUT of the §9.6
  discount to the other newbuild books (CAPT/FRO/MPCC/GSL/CMDB) is a pending
  owner decision** — it moves their NAVs and needs re-validation.
- **2026-06-21 — automation-drift policy set + `commit_drift.sh` helper added
  (owner decision).** The recurring problem: launchd jobs write to TRACKED files
  (prices_daily, baltic CSV, sp_scan cursor + candidates, `_manifest.json`,
  preflight, FFA queue), so the working tree perpetually accumulates uncommitted
  drift. Decision (vs gitignoring them or cron auto-commit): **keep them tracked,
  flush via a manual one-step helper.** `scripts/commit_drift.sh` stages +
  commits exactly those 8 files when run; COMMIT-ONLY (push stays the deliberate
  human event); decision logs + per-name pipeline outputs excluded (committed
  deliberately with their annotations / driving input change). Documented in
  "How to run things." Rationale: preserves full history + owner control of
  every commit; no cron clutter; drift cleanup is now one command.
- **2026-06-21 — daily S&P scan wired into the RC-ingest job + ingest-lag
  diagnosis (NOT an ingest failure).** Symptom: the `sp_scan` cursor sat at
  2026-06-11 while dailies through 06-19 were on disk. Diagnosis: the daily
  07:00 RC ingest (`com.crude-tanker-fv.rocketchat-ingest` →
  `scripts/ingest_rocketchat_cron.sh`) is **healthy and current** — ran Jun-21
  07:00, downloaded the 06-18/06-19 dailies, cursors at pareto_research 06-19 /
  baltic 06-20; its 14 KB `state/rocketchat_ingest.err` is ~99% a cosmetic
  urllib3 `NotOpenSSLWarning` (LibreSSL) + one transient TLS-read retry. The
  real gap was **cadence**: dailies arrive DAILY but `sp_scan` only ran in the
  WEEKLY news-pull cron, so prints lagged up to a week. **Fix:** added an
  incremental `sp_scan` (local-only, cursor-based, idempotent — verified
  "nothing to scan" on a same-day re-run) to the daily ingest wrapper after the
  ingest step; the linked-report harvest + manifest stay weekly in
  `news_pull_cron.sh`. (My first instinct — reorder `fetch_links` before
  `sp_scan` — was WRONG: `fetch_links` downloads linked detail reports, not the
  dailies, which come from `ingest_rocketchat`.) Manual catch-up this session
  advanced the cursor 06-11 → 06-19 (+4 review candidates: VLCC ~$180m via FRO;
  LR2/LR1/MR 06-16 cluster). **SEPARATE open item:** the FFA-OCR staleness alarm
  (>7 days) is NOT an ingest problem — the ingest still SEES `ffa_drybulk`
  messages (last 06-19) but `ffa_ocr` hasn't PARSED a 3-panel grid in 9 days, so
  the single-source poster likely stopped posting the parseable grid (or changed
  format). Verify the channel content.
- **2026-06-21 — B6 §9.2 terminal-value multiple LOCKED at 1.0× (owner decision).**
  Closes the last open Week-5 item. Owner ratified the memo recommendation
  (`outputs/terminal_value_options_memo.md`): keep the q9 terminal at 1.0× ×
  aged-NAV — `w_earn` + the conservative transaction-anchored marks already carry
  the cycle view, the sweep flips are immaterial band-edge wiggles, and the
  alternatives are flawed (uniform 0.9× wrong at troughs; 1.1× = forbidden
  calibrate-to-broker). Cycle-conditional recorded as the designated successor,
  revisited only on an adoption trigger. No engine change (1.0× was production);
  now PINNED by `tests/test_dividend_strip.py::test_terminal_nav_multiple_locked_at_1x`
  (locked-weights idiom — changing it needs a deliberate memo + test edit).
  §9.2 item 2 marked *resolved*; memo DECISION block filled; dividend_strip.py
  constant comment updated. tests: +1 (the pin); full suite 283 passed (the two
  reconcile state-tests un-skip now that `state/last_run.json` is fresh).
- **2026-06-21 — DEVELOPMENT FREEZE LIFTED (owner decision).** The 2026-06-14
  freeze (which gated all feature/sector/methodology work on a crude-backtest
  "edge" verdict) is removed. Rationale: this is a forward-looking valuation aid
  for picking/valuing individual shipping names, not a cross-sectional quant
  portfolio, so a cross-sectional IC backtest is not the right gate — and the
  backtest's null is an expected small-sample result, not a refutation of the
  per-name work. The freeze DECISION RECORD at the top of CLAUDE.md was replaced
  with a forward-looking project-stance note; PLAN.md was rewritten from a
  backtest-gate plan into the live forward plan (Week-5 hardening status + active
  backlog), with the backtest demoted to a reference section. The `backtest/`
  artefacts (PRE_REGISTRATION.md, REPORT.md) are retained as a recorded
  diagnostic — accurate history, no longer a gate. (Unrelated uses of "frozen"
  for stale data archives/vintages — container feed, MB anchor — are untouched;
  they mean a stale feed, not the dev freeze.)
- **2026-06-21 (Week 5) — B6 §9.2 terminal-value options memo WRITTEN (owner
  decision pending).** Re-ran the terminal-NAV-multiple sweep over the full
  19-name watchlist (`scripts/terminal_value_sensitivity.py`; was 12 names at
  the Jun-5 first run) → 7 band-edge flippers (0.9× turns peak names DHT/ECO
  more bearish; 1.1× turns ASC/SBLK→HOLD + GNK→BUY [deal-pinned, discount];
  12/19 never flip; CCEC most sensitive but holds BUY). Wrote
  `outputs/terminal_value_options_memo.md`: four options (1.0× / 0.9× / 1.1× /
  cycle-conditional), each steelmanned by an independent agent panel, with an
  empty owner DECISION block. **Recommendation: ratify 1.0× now** (auditable;
  marks already conservative; `w_earn` already down-weights the strip at peak —
  the at-stake flips are immaterial band-edge wiggles), **cycle-conditional as
  the designated successor** pending two adoption triggers (empirically-sized
  embedded-mark error, or the book gaining trough-band names); **reject uniform
  0.9×** (wrong sign at troughs — dominated by cycle-conditional) **and 1.1×**
  (its broker-gap justification is the forbidden "calibrate to broker" move,
  §6/§9). Key mechanism point: the terminal = current marks aged forward (never
  re-priced), so the multiple sets the *embedded asset-price level* — orthogonal
  to `w_earn`, which only weights the leg; §15's `governance_discount_pct` is the
  architectural precedent for a multiplier at this layer. No engine change (rec
  is status-quo); `TERMINAL_NAV_MULTIPLE` stays 1.0. §9.2 item 2 + PLAN.md B6
  updated to point at the memo. Was a parked Week-5 item; resumed at owner
  direction.
- **2026-06-21 (Week 5) — B5 anchor-basis commensurability SHIPPED** (commit
  5fc3b7d). Cycle-position anchors carry three non-composable bases (a cycle
  ratio is forward-12M-TC / anchor): `tc_10yr_mean` (crude/product/lng),
  `archive_22mo_median` (dry_bulk), `fy_calendar_avg` (containerships). Every
  `cycle_anchors` block in `scenario_inputs.yaml` now declares an `anchor_basis`
  enum (12 added; containerships' 3 prose tags normalized). Shared helpers in
  `scenarios.py` (`all_sector_anchor_bases` / `detect_mixed_anchor_basis` /
  `format_mixed_anchor_basis` / `ANCHOR_BASIS_LABELS`) drive a **MIXED-ANCHOR-
  BASIS** flag on the two cross-sector surfaces: the delta-report table
  footnote and the `reconcile --all` footer (per-name basis shown in
  `--verbose`); `--sector` / single-name runs use one basis so never flag.
  METHODOLOGY §10 gains the three-basis subsection. Metadata + diagnostics
  ONLY — the engine reads just `ten_year_mean`, ignores the new key, so the
  valuation core is untouched (FV-band + cycle/blend pins unchanged). Tests
  +5 (3 scenarios, 2 delta) → 280 passed, 2 skipped. The B5 commit was kept
  to the 7 source/doc/yaml/test files; the verification pipeline run's
  regenerated outputs + routine decision-log stubs were reverted (they
  regenerate on the next real refresh). Was a parked Week-5 item; resumed at
  owner direction with the freeze set aside.
- **2026-06-12 (Week 5) — MB Weekly 24 prints PROMOTED (owner decision,
  7 prints recategorized per owner review) + drift loop run.** Fit
  inputs: **Seamusic** (Aframax age-17 $52.5M, in-window WITH
  premium-channel note — buyer screen: undisclosed buyer + immediate
  rename to VIRTUS MARIS + no ice notation = NOT confirmed-clean;
  single-print drift GATE passed: 5yr −3.6%/10yr +0.1%/slope negative,
  no flip on the print alone; REVISIT if no second clean corroborating
  print by Q3), Vulcania (Pana n=4→5, TC-ATTACHED caveat — residual
  could be entirely the charter), Ausone + Santa Rita (Supra-Ultra,
  curve-bracketing pair). Documentation-only (owner recategorization —
  original note overstated): Proteas (age 21 — old-age-leg validation
  DEAD-ON, the Picardy/Predator pattern; NOT fit thickening), White Bay
  (age 22), Shanhaiguan (age 0 NB; Dalian print on a Korean-spec anchor
  = conservative-to-fair, not validated-exactly). Drift loop: ONE flip
  — SBLK TRIM/SHORT→HOLD (+1.1% NAV; Pana fit +6.9/+3.0 → +11.5/+7.5;
  band-edge third oscillation, leans on the TC-attached print — sblk_log
  annotated, no size action). Ethanol/corn driver re-routed from
  demand-destruction overlay to dry-bulk scenario tree
  (framework_breakers entry — sector-structural ≠ macro recession).
  Tests 277 green, no re-pins. Fit counts: Aframax 13 / Pana 5 /
  Supra-Ultra 22.
- **2026-06-12 (Week 5) — MB weeklies first direct delivery: ingest route
  built + three-sector once-over run (review-only, nothing promoted).**
  Container/Dry Bulk/Tanker Weekly 24 archived to `inputs/research_mb/`
  (LNG not delivered — verify subscription); route = Gmail link harvest →
  fetch_pdf.py (cdn.flxml.eu added to data_sources.yaml
  `mb_shipbrokers_weeklies`). Findings in
  `outputs/mb_weekly_check_2026-06-12.md`: (1) container — frozen 10
  weeks hid a feeder rally (+13.4%, position 0.98x→1.12x; MBCI +13.9%;
  intermediate/large drift normal; marks layer current; MPCC most
  exposed) → owner-gated `twelve_month_tc.yaml` container refresh queued;
  (2) tanker — MB 5yr assessments land 5/6 classes inside
  TXN_PURE_PLAY_K_BAND over our txn marks (first INDEPENDENT
  confirmation of the B4 band semantics), but crude NB anchors read
  14-35% above MB Korea NB with a 5yr>NB prompt inversion (review item);
  Hormuz trigger NOT met (draft memo, 30-day window, conditions — the
  closest signal yet); (3) dry bulk — txn marks validated by MB's own
  prints (Proteas $12.10M dead-on the age-21 Pana curve), Supra
  assessment gap = basis not error, **Pana anchor flagged structurally
  LOW** (MB 5yr tenor never below ~16k vs anchor 11.9k — Q3 refinement +
  B5 xref). 7 promotable print candidates queued (Seamusic Aframax
  $52.5M ~65% above fit; Shanhaiguan NB resale $90M; Vulcania/Proteas
  Pana; 3 Supra-Ultra) — promotion human-only, each triggers the
  prints→rerun→drift loop.
- **2026-06-12 (Week 5, Session A) — B4 shipped: mark-driven classification
  restated to post-flip k_broker semantics + fetch_links argparse fix.**
  Two-regime definition landed in METHODOLOGY §9 item 9: txn-anchored
  sectors (crude/product/dry bulk) — mark-validated = k_broker inside the
  uniform pure-play band `TXN_PURE_PLAY_K_BAND = (1.05, 1.25)` (constants
  in `marks.py`, uniformity < 0.05; DHT/ECO/FRO 1.12-1.14 at the Jun-2026
  fit, ~+13-17pp spread EXPECTED); mark-driven = outside the band either
  side. Un-anchored sectors (LNG/containerships) keep the original ≈1.0
  reading. Broker-sweep Read column relabeled MECHANICAL
  (`wide-spread`/`narrow-spread`, owner decision) — it had been printing
  the canonical validators DHT/ECO/FRO as "mark-driven" at their expected
  band premium; §6 prose is the canonical classification. Dated
  restatements appended to §6 INSW/TNK/ASC/STNG/HAFN/SBLK, §7.5, §9
  item 10, §15.2; LIMITATIONS §1 definition updated. No mark changes —
  pipeline re-run diff was text-only, delta 0 material, reconcile 19/19.
  fetch_links: zero-option argparse front door (`--help` exits 0
  pre-network, unknown flags exit 2 — closes the Week-4 §5 observation);
  no-arg cron path unchanged. tests: 274 → 277.
- **2026-06-12 (post-Week-4-close) — brokerage MCP decision REVISED:
  keep the IBKR connector attached, DENY it in Claude Code.** The
  Week 4 owner action ("detach entirely") is superseded: the connector
  feeds a weekly Cowork portfolio routine + ad-hoc Chat discussion, and
  claude.ai connectors are account-level all-or-nothing (no per-surface
  Chat/Cowork/Code scoping exists; Code's `deniedMcpServers` doesn't
  match cloud-synced connectors). DENY rules on the synced server id
  (`mcp__8de167eb-dbd9-4178-b52a-a756c1f27b24`) added to
  `~/.claude/settings.json` (machine-wide) AND the tracked
  `.claude/settings.json`. Deny, not ask — the §5 red-team proved
  autonomous sessions auto-approve ask-tier. Verified live same
  session: read-only `get_account_summary` probe refused at the
  permission layer (deny rules hot-reload mid-session). CAVEAT: if
  IBKR is disconnected/reconnected at claude.ai, the UUID may change
  and the deny goes silently stale — re-check the id in a fresh
  session's tool list. Full rationale: PERMISSIONS_PROPOSAL.md §6.4
  revision note. Same session: `settings.local.json` pruned 262 → 38
  allow entries (arbitrary-write/interpreter/credential-exposing
  allows, ffmpeg-era strays, ask-tier-bypassing curl/launchctl
  carve-outs, tracked-allowlist duplicates, stale one-offs).
- **2026-06-12 (Week 4, Step 3 — WEEK 4 CLOSED)** — Week-close checklist
  run. **§5 red-team pass (first session with the allowlist active):
  DENY rules ENFORCE** (env-file Read refused, `rm -rf` refused);
  allow-tier friction-free (pytest, reordered-flag sp_scan, outputs
  edit, sec.gov WebFetch — probes 7-10 clean); **ASK tier NOT testable
  in an autonomous session** — the autonomous permission mode
  auto-approves ask-class calls (curl with no matching rule executed;
  watchlist Edit applied + immediately reverted; fetch_links ran), so
  the prompt half of §5 carries to Week 5 as an INTERACTIVE-session
  item. Real finding, fixed: `Bash(git push *)` had accumulated in
  `.claude/settings.local.json` as a blanket allow — it defeated the
  tracked ask-on-push policy in EVERY session, not just this one —
  pruned. Two new leak observations recorded: `git -C <path> push`
  dodges the `git push` prefix matcher (the -C variant of the
  flag-reorder leak), and fetch_links ignores unknown flags (`--help`
  ran a real pass; dedupe held, 0 downloads — argparse fix queued
  Week 5). **Verification gate: 274 passed; pipeline clean (0 material,
  0 input changes); `/reconcile --all` 19/19, 0 SANITY FAIL, 0 drift
  alerts.** Documentation audit (two read-only agents, fixes applied in
  main session): README 17→19 names / 4→5 sectors / 243→274 tests +
  containerships watchlist table + METHODOLOGY line count ~720→~2,900;
  METHODOLOGY §1 coverage header 19/5, stale "Week 4 candidate" lines
  closed, **§11.8.6.4 horizon header corrected "12 quarters"→"10 strip
  quarters"** (body and Appendix A already said 10; owner ratification
  of the A1 interpretation still pending); LIMITATIONS gains the
  containerships-CLOSED sector entry, the §11.8.5 stale-vintage +
  old-age-tilt OPEN limitation, the APPROX consensus_pnav list
  completed to all SEVEN names with actual bases (audit agent's
  suggested values were wrong — re-verified against watchlist.yaml
  before applying), §15 declined list completed
  (TNK/CCEC/CAPT/MPCC/GSL), validator list extended to all 5 sectors.
  Quick-ref preamble gains the vintage-prices note (quick-ref prices
  are note-vintage, not live — stop "fixing" them). PLAN.md rewritten
  for Week 5 (B4/B5/B6 + Q2 carry-forwards per owner direction).
  OWNER ACTIONS re-flagged: brokerage MCP connector was STILL attached
  in this session (order-writing surfaces reachable); A1 horizon
  ratification.
- **2026-06-12 (Week 4, Step 2 + maintenance)** — **CONTAINERSHIPS SHIPPED:
  engine (per-sector `strip_horizon` + `coverage_schedule`, zero-drift
  verified on all 17 prior names), Container Set A wiring (A2 class
  signatures, A3 TEU-weighted intermediate $43,400/$33,700 applied at
  onboarding), MPCC + GSL onboarded (19 names, SANITY 0 FAIL, both
  n/a-APPROX), §15.7 screens both DECLINED (GSL = the dimension-6
  charter-affiliation founding pass: CMA CGM equity zero since 2022,
  13/71 vessels), calibration lock recorded N/A-by-construction
  (machine-confirmed; primary substitute = MPCC's 3 disclosed sale
  prints — tool old-age marks 0-33% BELOW realized, conservative by
  design).** Maintenance landed: B1 overlay ledger (§16, 11 active
  rows), B2 §14.4 double-count warning, B3 all 10 weight-skips
  re-pinned (DHT wnav-vs-base direction REVERSED under Jun-9 weights).
  SESSION-LOG NOTES: (a) A1 horizon — owner brief said "~12q from
  report date"; under the repo's q3_2026 strip-start convention,
  end-2028 = **10 strip quarters** — wired as 10, flagged for owner
  review; (b) MPCC cohort AGES and NB delivery quarters are ESTIMATES
  (deck discloses no built years) — refine at Q2 (2026-08-26); (c) GSL
  analyst_target/consensus_pnav are book-based placeholders (CMDB
  convention) — replace if VIE coverage surfaces; (d) PR #2 reviewed +
  worktree-verified, MERGED by owner same day (entry below); changelog
  conflict resolved additively at integration. Tests 243 → 274. Full
  detail: METHODOLOGY Appendix A 2026-06-12.
- **2026-06-11 (Week 4, Step 1)** — **§11.8 containerships methodology
  decision doc LOCKED** (time-boxed one session, doc before code, dry-bulk
  §11.7 as template). Decisions: 3-class collapse (ctr_feeder ≤2,000 /
  ctr_intermediate 2,000-5,500 / ctr_large >5,500, WB variants excluded
  from class averages); **charter-book convention = coverage-schedule
  generalization of the §3.2 blend** (strip earns disclosed contracted
  rates through expiry via per-quarter cov_q, re-fixes at scenario rates;
  NAV stays on-curve at bare marks; charter premium/discount = v1
  limitation), NOT §11.6 off-curve; Container Set A scenarios
  0.25/0.40/0.20/0.15 (disruption_persists / gradual_normalization /
  normalization_plus_overhang / demand_recession); cycle anchors from the
  weekly's FY21-25 table NOT the boom-only 19-month archive median
  (feeder $20,850 / intermediate $32,300 / large $41,000 → positions
  0.98x/1.30x/1.53x at the Apr-01 vintage); **external anchor: NONE —
  all-APPROX sector** (verified: Pareto's own liner table dashes MPCC's
  P/NAV; they value the space on EV/EBITDA) → v1 calibration lock
  recorded N/A-by-construction with VIE + marks-consistency substitutes;
  validators MPCC + **GSL** (DAC deferred — Capesize hybrid, same logic
  as CMRE). Empirical basis: mechanical extraction of all four data
  tables across the 42-issue MB archive (40-42/42 parse rate). Key
  fresh source found on disk: Pareto MPCC quarterly review 2026-05-28
  (HOLD, TP NOK 25, 99/69/41% of 26/27/28 days fixed, $2bn backlog).
- **2026-06-12 — Permission allowlist shipped (`.claude/settings.json`,
  tracked) + fetch_links module split + fetch_pdf.py wrapper.** Full
  rationale in `PERMISSIONS_PROPOSAL.md` (decision record). Narrow
  allows for the constant loop (pytest/reconcile/pipeline/refresh/
  sp_scan/price_refresh, git add/commit, WebFetch to the
  data_sources.yaml host set); ask on git push, fetch_links,
  ingest_rocketchat, curl, launchctl, and the three human-only
  promotion surfaces (watchlist vintage / transactions / FFA curve —
  the TEN-$44 and promotion rules turned mechanical); deny on
  credential-shaped reads. Two structural changes: `--fetch-links`
  moved out of sp_scan into `crude_tanker_fv.fetch_links` (Bash rules
  are prefix matchers — a network flag on an allowed module leaks when
  flags are reordered, so the boundary is now a module boundary;
  news_pull_cron.sh updated), and `scripts/fetch_pdf.py` replaces the
  ad-hoc curl pattern (host-validated against data_sources.yaml in
  code; carries the single audited Okeanis TLS exception). Brokerage
  MCP decision: detach from Claude Code entirely (owner action),
  not deny-rules. New "What NOT to do" rule on widening the allowlist.
  *(Ordering note: this entry lands between Step 1 and Step 2 of Week 4
  chronologically; merged after Step 2 completed — see the entry above.)*
- **2026-06-11 (post-close) — TEN June-5 data-kit reconcile (user-supplied
  PDF; tenn.gr blocks agent fetching).** Found + fixed a Q1 manifest
  omission: Dr Irene Tsakos + Silia T (2025-built conventional Suezmaxes)
  were never entered — the onboarding plan's "14 conventional Suezmax"
  slip; fleet_summary claimed 60 on-curve over 58 rows. NAV/sh $80.79 →
  $88.13 (+9.1%), gap to APPROX broker −26.0% → −19.3%, BUY unchanged.
  Q2-vintage kit deltas (Ulysses sale confirmed — no gross price, not
  promotable; Sola TS step-up; Dimitris P spot→TC $40k; Alaska/Archangel
  to spot-indexed TC) documented in ten_log for the September H1 refresh,
  NOT applied to the Mar-31 snapshot. New cross-foot guard test
  (test_validate.py) + gotcha rule. tests: 244 passed.
- **2026-06-11 (WEEK 3 CLOSED)** — **first Week-close checklist run
  (checklist itself codified this session, owner decision).**
  Documentation audit via two read-only agents, fixes applied:
  METHODOLOGY line-46 monster paragraph → dated scope-change log;
  coverage header 8→17 names/4 sectors; preferred_equity comment
  (TEN is the user, not "none"); STNG §6 mark-validated→mark-driven
  with date-stamps; INSW version-label footnote; §6 entries ADDED for
  CMDB + CAPT; FFA-OCR saga moved OUT of §11.7.7 "NOT in v1" into new
  §11.7.8 (onboarding table → §11.7.9); Appendix A entries added for
  2026-06-10 + 2026-06-11 (closing the §15.7 dangling promise).
  README: status 2026-06-11, 17 names/4 sectors/243 tests, dry-bulk +
  CAPT/HAFN/TRMD watchlist tables, DP2/dry-bulk scope line corrected.
  LIMITATIONS: dry-bulk greenfield marked CLOSED, §15 names updated
  (TEN+CMDB cases; TNK/CCEC screened-declined), mark-driven snapshot
  marked as vintage with pointer to the live sweep. CLAUDE.md
  quick-refs reconciled (INSW k 1.52+, SBLK HOLD); earnings-calendar
  maintenance line added; stale "(Coming end of Week 0)" removed.
  Verification gate: 243 passed/10 skipped; `/reconcile --all` 17/17
  SANITY OK, 0 drift alerts; refresh checklist regenerated 17/17.
  **PLAN.md created** (the rolling sprint-plan/handoff doc — Week 4 =
  containers; Step 0 flags the Container Weekly feed stale since
  Apr-01). Week 3 final tally: news-pull v1, daily price refresh +
  TEN fix, FFA-OCR Stage 1 + market-consistency diagnostic, earnings
  readiness, CAPT (17th name), §15.7 + full-book retro screen,
  Week-close checklist.
- **2026-06-11 (Week 3, day 2, Part 4)** — **§15.7 screening procedure
  FORMALISED + full-book retro screen run (owner-approved).** New
  METHODOLOGY §15.7: cheap gate (multi-year median P/NAV ≥0.85 → N/A),
  structured screen below it (control/share structure, related-party
  fee load %GAV/yr, distribution behaviour, natural-experiment comp,
  external anchor), the evidence-vs-mechanism doctrine (haircuts price
  EVIDENCE; mechanism → tripwires), two quantitative calibration
  anchors (capitalized fee drag; external-anchor implied discount),
  mandatory recording per name + onboarding step 4. Retro outcomes,
  all 17: 9 gated N/A (DHT ECO FRO FLNG INSW HAFN NAT-§12 ASC GNK);
  3 Step-1 declines (STNG TRMD SBLK — open payout/buyback channels, §6
  mark-driven discounts); 2 full-screen declines with tripwires —
  **TNK 0%** (dual-class 54.9%-votes-on-30.8%-economics BUT fee leakage
  internalized Dec-24, $6.00/sh specials since mid-23; TK-combination
  tripwire) and **CCEC 0%, closest call** (float ~13%, sponsor-paid
  exec comp, fiduciary waiver, ~24% payout vs CAPT-like 0.4%-of-GAV
  fees, real conflicts committee, 76-quarter dividend record;
  payout-path + CAPT↔CCEC cross-dealing tripwires; 10% alternative
  documented — owner call). **Haircut recalibrations: TEN HOLD 30%**
  (band 30-36; VIE-implied drifted to 36.3% but the payout raise argues
  down; TCM fee anchor due at Q2) and **CMDB HOLD 30%, RE-GROUNDED** —
  capitalized fee drag ($28M/yr ÷ 10-12%) = 30-36% of the $779M equity
  NAV, landing on the haircut independently of TEN-equivalence.
- **2026-06-11 (Week 3, day 2, Part 3)** — **CAPT onboarded (17th name,
  Week 3 stretch goal) — first Oslo/NOK listing.** Assembled entirely
  from the linked-report harvest (Pareto initiation Apr-19 + Q1 review
  May-27, both already on disk) — zero new fetching for data assembly;
  issuer-report confirmation deferred to the Q2 refresh. 30 firm
  vessels (12 VLCC / 10 Suez / 4 Afra / 4 LR2-crude-routed), 9 on-water
  at Mar-31, 21 NBs at delivered-market-less-$1,880M-commitment with a
  Pareto-waypoint fleet_schedule ramp (11 Apr-26 → 17 Nov-26 → 24 YE-27
  → 30 mid-28); 13 options at cost excluded. NOK handling: watchlist in
  USD (NOK 116.2 / 9.5221 = $12.20, Jun-10 vintage incl. pnav 0.67 +
  P/E 11.1 from the same daily); price_refresh gains `yahoo_symbol` +
  `quote_currency` fields (CAPT.OL + NOK=X conversion — bare "CAPT" is
  Captivision). NAME_ALIASES + data_sources + earnings calendar
  entries added; 23-mention Pareto sweep distilled. **First reconcile:
  −2.6% gap on a real Pareto print, SANITY OK, k_broker 1.04 — the
  tightest onboarding baseline on record; BUY EV +38.8%.** §15
  considered + declined (documented in the balance sheet + log).
  tests: 243 passed, 10 skipped.
- **2026-06-11 (Week 3, day 2, Part 2)** — **Q2 earnings-readiness pass.**
  `inputs/earnings_calendar.yaml` built for all 16 names (web-swept +
  cadence-verified: 5 calendar-confirmed — ECO Aug-4, SBLK Aug-5,
  TRMD Aug-26, HAFN+FLNG Aug-28; 11 expected windows; TEN is a
  SEPTEMBER H1 reporter). Preflight gains §0 earnings check
  (`refresh.check_earnings_calendar`): 🔴 REFRESH DUE when a report
  window opens with no target-quarter balance sheet, 🟡 within 14 days.
  Report-day refresh runbook added to CLAUDE.md (7 steps incl. the
  issuer-report S&P sweep — Appendix A backlog CLOSED — and the
  vintage-rebase rule). Season shape: early cluster Jul-28→Aug-6
  (STNG/ASC/TNK/CCEC/ECO/GNK/INSW/DHT/SBLK/CMDB), late cluster
  Aug-20→31 (FLNG/FRO/NAT/TRMD/HAFN), TEN mid-Sep. tests: 238 passed.
- **2026-06-11 (Week 3, day 2)** — **FFA-OCR Stage 1 SHIPPED** (the
  Week 3 centerpiece; owner-approved re-scope, no longer trigger-gated).
  `ffa_ocr.py`: classifier (Cape + Cal2\d + "Produc* Price Change"
  signature) + TSV-positional parser (x-band panel assignment, per-row
  tenor majority vote, conf≥60 gate, trailing-only punct strip) +
  sanity model + review queue (`outputs/ffa_ocr_queue.md`) + incremental
  cursor + `--staleness` alarm, wired as the new tail of the weekly
  news-pull chain. Key empirics: the widget posts EVERY business day
  (45/46 days Apr-1→Jun-11; the ~7% archive-wide rate was format-era
  dilution); recipe = grayscale → 4× LANCZOS → psm 6 (color drops the
  headers; tesseract can't read /tmp in the sandbox — scratch lives in
  `state/ffa_scratch/`); DISCOVERED tick model — months/Cal tick $12.5
  truncated, Q tenors display the unrounded 3-month average (31766 =
  95300/3 is real, not noise). 29/45 days fully clean, 16 flagged
  (incomplete grids only; the parser refuses to guess on mangled
  tokens like "(3800"). Promotion to `ffa_forward_curve.yaml` is
  human-only; strip integration is diagnostic-first pending one review
  cycle. Stage 2 (2020-2026 backfill) open. tests: 233 passed.
- **2026-06-10 (night, Week 3 opener, Part 2)** — **first `/news-pull` run
  + TEN price-input error fixed + daily price refresh BUILT.** The
  inaugural digest (`outputs/news_digest_2026-06-10.md`, 4 agents / 16
  names) caught: TEN watchlist price $44.00 was an input ERROR (6-K prose
  "~$44" typed as a live price; actual $36-37.5 all week) — fixed to
  $37.14 with `consensus_pnav` REBASED 0.40→0.34 to preserve the implied
  broker NAV anchor (~$110) and `consensus_fwd_pe` 5.5→4.6 (drift +0.5pp,
  stable; BUY strengthens, EV +30.9%→+55.1%); an unrecorded Pareto stance
  change INSW BUY→HOLD 2026-05-18 (TP raised $84→$88, valuation-driven —
  confirmed verbatim in the archived daily, annotated); GNK deal risk
  front-loaded to the Jun-18 AGM (all 3 proxy advisors back Genco, Diana
  withdrew 4/6 nominees + floated dropping the tender, 38 shares
  tendered); STNG 4×LR2 $285.8M EN-BLOC (documented-not-promoted, watch
  Q2 6-K for splits); CMDB Astros bounded ~$22.8M (inference — NOT
  promotable). **Process fix shipped same session: daily price refresh**
  — `price_refresh.py` fetches all watchlist closes (Yahoo chart API)
  into automation-writable `prices_daily.yaml` with sanity flags (>15%
  day move / >30% vs static, flagged = never applied); launchd
  `com.crude-tanker-fv.price-refresh` daily 18:30; pipeline CLI passes
  `live_prices=True` (tests keep deterministic statics by default).
  VINTAGE RULE: broker NAV (reconcile) + consensus EPS keep the
  watchlist-static `as_of_price` — Pareto ratios pair with Pareto-vintage
  prices; only EV/position reads live. SBLK TRIM/SHORT→HOLD on the
  live-price introduction (band-edge wiggle, annotated). tests: 220
  passed, 10 skipped.
- **2026-06-10 (night, Week 3 opener)** — **periodic news pull v1 BUILT**
  (registered backlog, owner spec + 4 vetting amendments, one session as
  time-boxed). Mechanical half: `scripts/news_pull_cron.sh` + launchd
  plist `com.crude-tanker-fv.news-pull` (Saturdays 08:00, after the
  07:00 daily RC ingest per amendment 2), chaining RC ingest → `sp_scan`
  → `--links` → `--fetch-links` → `pareto_archive --build-manifest`,
  PYTHONUNBUFFERED + per-step banners + exit-code echo per the silent-
  death gotcha. Agent half: `/news-pull` command — web-sweep weighted to
  APPROX (read from `reconcile.APPROX_PNAV_TICKERS`, not hardcoded) +
  live-event names (detected from decision logs), digest at
  `outputs/news_digest_YYYY-MM-DD.md` with promotable-candidate (built-
  year + en-bloc-split fields, amendment 4) / stance-change / live-deal /
  stale-price (APPROX fresher-price-only, amendment 3) / no-action
  sections + drift-loop reminder. Never writes pipeline-loaded YAMLs
  (amendment 1). Dry-run clean end-to-end (cursor Jun-08 → Jun-10).
- **2026-06-06** — file created. Verification-loop, three-jobs
  reconciliation framework, "what this tool is, philosophically" section,
  gotcha list, per-ticker quick-refs all promoted from session memory +
  decision logs.
- **2026-06-09** — added secrets-discipline rule to "What NOT to do" after
  a `rocketchat_token.rtf` was dropped at repo root during Rocket.Chat
  ingest setup. Caught untracked but not gitignored. Defensive `.gitignore`
  patterns added (`*_token*`, `*_credentials*`, `*_secret*`, `*.rtf`, `.env*`).
- **2026-06-09 (evening Part 2)** — dry-bulk classes added to the
  transaction-anchored pipeline. Cape (24 prints) / Pana (6) / Supra-Ultra
  (18) YAMLs landed at `inputs/market_data/transactions/`. Sources are
  the Pareto Shipping Daily archive 2025-01→2026-06 plus the SBLK Q1 2026
  6-K Stonington print. SBLK gap moved −21.7% → −21.1% post-fit, locking
  it in the §6 mark-driven taxonomy (k_broker 1.27). Per-ticker quick-ref
  for SBLK + the §9.9 scope-discipline line updated. tests: 192 passed.
- **2026-06-09 (late evening Part 3)** — tanker classes swept from the same
  Pareto archive: VLCC/Suezmax/Aframax/MR samples expanded, LR2 graduates
  to own-fit (proxy retired). Tanker 10yr anchors were running HOT — VLCC
  fit −18% at both legs; 5 names flip under txn-anchored marks
  (DHT/ECO/FRO→TRIM-or-HOLD-down, TNK BUY→HOLD, TRMD HOLD→TRIM). Toggle
  still opt-in; default-on is an OPEN owner decision. `sp_scan.py` +
  `_scan_state.json` added for incremental future scans (191-candidate
  review queue archived at `outputs/sp_print_candidates.md`). One locked
  test expectation reversed with rationale (Suezmax fit direction — thin-
  sample artifact). Affected decision logs annotated (9 names). tests:
  198 passed. Backlogs registered in METHODOLOGY Appendix A: exogenous
  demand-destruction overlay, issuer-report S&P sweep at refresh, GNK
  onboarding, §6 SBLK promotion, Pana print disambiguation.
- **2026-06-09 (late evening Part 4)** — **txn-anchored marks made the
  pipeline DEFAULT** (owner decision; Sinokor's bid IS the VLCC market).
  Defaults flipped in `value_company` / `run_scenarios_watchlist` /
  `run_broker_sweep` (sweep now recalibrates its "tool" endpoint too).
  Headline re-base: DHT BUY→TRIM/SHORT $14.31, ECO/FRO →TRIM/SHORT,
  TNK BUY→HOLD, TRMD →TRIM/SHORT; FLNG/CCEC untouched. k_broker semantics
  now "broker premium over transaction levels" — uniform 1.12-1.14 on
  crude pure-plays. vlcc.yaml Sinokor exclusion re-grounded on
  data-quality only (no per-vessel split). FV-band + sweep tests re-based.
  Drift flags on this run are the re-base, not market moves — 9 logs
  annotated. tests: 198 passed.
- **2026-06-10 (later still)** — **Pareto linked-report harvest: 220
  detail reports pulled from the dailies' hyperlink annotations.** User
  tip: the dailies embed links to Pareto's full research. pypdf
  `extract_text()` is blind to /Annots — every prior sweep missed them.
  240 of 351 dailies carry links → 267 unique tracked-download URLs
  (FactSet/BlueMatrix, public, long-lived tokens; 100 arrived
  Proofpoint-wrapped and are unwrapped offline). Downloaded 220 new
  reports (47 already archived), 0 failures; 217 classify as
  company_report incl. ~70 on watchlist names (full NAV breakdowns /
  estimates). `sp_scan --links` + `--fetch-links` codified with
  inventory + report_id dedupe (no re-fetching on re-runs);
  `outputs/pareto_daily_links.json` committed. The "Capital Tankers"
  reports in the set are CAPT (Oslo-listed crude newbuild player,
  initiated by Pareto Apr-2026, BUY TP NOK 180 at 0.75-0.84x NAV) — a
  DIFFERENT entity from CCEC, whose no-coverage APPROX status stands.
  CAPT noted as a future onboarding candidate (Pareto-covered pure
  crude, deepest crude NAV discount). tests: 207 passed.
- **2026-06-10 (later)** — **Pareto free-text name-sweep added to the
  process + run retroactively for all 15 names.** `sp_scan.py --names`
  mode (alias-aware: OET=ECO, HAFNI=HAFN, TORM=TRMD, Tsakos=TEN;
  share-price-table noise filtered). 15 review files at
  `outputs/pareto_mentions_<ticker>.md`; distilled entries in every
  decision log. Findings: inputs validated (NAT NB commitments + ASC
  payout-doubling already captured); 1 missed print promoted (TEN Mar-25
  Suezmax $40M — fit moved <0.5pp, under drift gate); Pareto stance
  changes recorded (FLNG→SELL 2026-05-27, OET+FRO→HOLD 2026-05-26,
  INSW→BUY 2026-01-21); consensus_pnav plumbing confirmed by exact
  matches (TRMD stated $34 vs implied $33.98; INSW $80 vs $79.59; SBLK
  $33 vs $33.17). Mention-count distribution empirically confirms the
  APPROX taxonomy (CCEC 0, NAT 4, TEN 5, ASC 6 — "We don't cover ASC"
  verbatim — vs covered names 34-96). Onboarding workflow updated with
  the sweep as step 3; quarterly-refresh habit noted. tests: 205 passed.
- **2026-06-10 (evening)** — **CMDB onboarded (16th name, third dry-bulk
  validator) — Week 2 dry-bulk sequence CLOSED.** APPROX-anchored (zero
  Pareto/VIE coverage; P/BV 0.62 proxies P/NAV on spinoff fair-value
  book). 29 owned at Mar-31 (Clara/Miracle sold Q1; Astros closed Q2);
  CBI chartered-in platform excluded as P&L-only. Tool NAV $32.23 =
  +15.8% over book; 0.54× price/NAV, EV +64% — **flagged §15 candidate
  (related-party fees / no payout / family control), haircut decision
  with owner before the signal is actionable.** CMDB added to
  `APPROX_PNAV_TICKERS` (was missing — briefly mis-entered the lock
  denominator as 1/3; corrected to 1/2 excluded-APPROX same session).
  No promotable prints (Clara+Miracle aggregate gain only — no per-vessel
  prices; no-back-solve). §11.7.8 table marked DONE throughout.
  tests: 210 passed. **Same evening: §15 haircut set at 30% (owner
  decision, TEN-equivalent) — PW FV $28.32 → $19.82, EV +64% → +14.9%
  mild BUY; asset NAV untouched; §15.3 second-case entry added.**
- **2026-06-10** — **GNK onboarded** (15th name, second dry-bulk validator)
  from the Q1 2026 10-Q. k_broker 1.04 / gap −5.2% — VALIDATES the
  transaction-anchored dry-bulk curves on a no-Pana fleet; isolates SBLK's
  −21% as name-specific. v1 dry-bulk calibration lock recorded as 1/2
  (50%) FAIL-with-explanation (SBLK = documented §6 mark-driven miss; no
  tuning per the back-solve rule); revisit at Q3 with the ≥80%/±5% bar.
  6 prints harvested at onboarding (2× GNK nmax $72.75M + Courageous
  $63.55M + Maran SWS cape $30M in-window; Picardy/Predator $10.6M
  documentation) — Cape fit n 21→25, +16.0%/+12.7%; SBLK moved −0.1%
  (under drift gate). Diana tender deal overlay documented in
  decisions/gnk_log.md + watchlist comment — GNK price is tender-pinned
  until Jun-26. tests: 201 passed.

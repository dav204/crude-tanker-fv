# Workflows — Tanker FV tool

Split out of CLAUDE.md (2026-06-22) to keep the operating rulebook short.
The step-by-step procedures for the three recurring multi-step tasks:
onboarding a ticker, the report-day refresh, and onboarding a sector.
CLAUDE.md carries the gates these run against; this file carries the steps.

## Onboarding a new ticker — the workflow

1. `/add-ticker <SYMBOL> <SECTOR>` — scaffolds YAML stubs, test file,
   decision log entry.
2. Pull the latest 6-K / 20-F / press release; fill in the fleet manifest,
   balance sheet, cost structure, dividend policy (METHODOLOGY §8.1).
3. **Sweep the Pareto free text for the name** (added 2026-06-10 after GNK):
   `python -m crude_tanker_fv.sp_scan --names <TICKER>` (add the alias to
   `NAME_ALIASES` first — Pareto uses Oslo tickers / company names). The
   dailies carry name-specific gold the structured columns miss: Pareto's
   own dated NAV statements (cross-check `consensus_pnav` plumbing),
   stance/TP changes, deal overlays, name-attributed S&P prints, dividend
   policy changes, NB orders. Distill into the decision log; promote any
   prints (then run the prints→rerun→drift loop).
4. **§15 governance screen (METHODOLOGY §15.7, mandatory since
   2026-06-11):** gate at multi-year median P/NAV ≥0.85 (recorded N/A);
   below the gate, run the structured screen (control/share structure,
   related-party fee load as % of GAV/yr, distribution behaviour,
   natural-experiment comp, external anchor). Outcome — applied X% /
   declined-with-tripwires / N/A-gated — goes in the decision log.
   Doctrine: haircuts price EVIDENCE of realisation impairment;
   mechanism generates TRIPWIRES.
5. Add the watchlist row (current_price, analyst_target, consensus_pnav,
   consensus_fwd_pe, sector, as_of).
6. Run pipeline + tests + `/reconcile <TICKER>`.
7. If SANITY=OK, close the decision log entry with the reconciliation gap
   recorded as the baseline for future drift detection. If SANITY=FAIL,
   **stop and investigate** — don't paper it over.

The same `--names` sweep is a quarterly-refresh habit: run it incrementally
over the new quarter's dailies for ALL names and skim for stance changes,
NAV statements, and missed prints. The 2026-06-10 retro-sweep (15 names,
280 dailies) found the inputs solid but surfaced one missed print (TEN's
Mar-25 Suezmax disposal), two Pareto stance changes we hadn't recorded
(FLNG→SELL May-26; OET/FRO→HOLD May-26), and exact-match confirmations of
the consensus_pnav plumbing (TRMD $34 stated vs $33.98 implied).

## Report-day refresh — the workflow (added 2026-06-11 for Q2 season)

`inputs/earnings_calendar.yaml` holds each name's next report date
(confirmed/expected + cadence basis); the preflight
(`python -m crude_tanker_fv.refresh`) flags 🔴 REFRESH DUE when a window
opens with no target-quarter balance sheet on file, and 🟡 reports-soon
within 14 days. The weekly `/news-pull` digest catches newly-announced
dates — update the calendar when it does.

**2026-08-13 — before FREEZING a report-day prereg, sweep the name's full trail
since its last decision-log entry:** `sp_scan --names <TICKER>` over the daily
archive + an archive-GAP check for the window (`ls` the period — a hole in the
PDF archive is silent) + one issuer-newsflow search for names with no filing
channel (Oslo/Euronext names have no EDGAR sentinel). A daily consumed for one
print is NOT a triaged daily. (The BRUT H1 prereg froze 8/12 blind to the
issuer's 7/07 delivery + sale-leaseback + DEMERGER + CEO release: the 7/03→7/14
archive hole is Pareto's Jul/Aug cadence — SOURCE-QUIET, audited 8/13 PM: the RC
history walk found no dailies ever existed to backfill (brut_log) — and the 8/06
daily's BRUT paragraph sat untriaged beside the FFA prints taken from the same
issue. The prereg's band survived on subsequent-events routing — the miss was
recoverable luck, not process.) Cadence quirks worth
remembering: TEN reports Q2 in SEPTEMBER (H1 reporter); FLNG's calendar
slot is Aug-28 but 2025's release came Aug-20; the early cluster
(STNG/ASC/TNK/CCEC) opens Jul-28.

Per name, on report day:

1. Pull the 6-K/10-Q + press release (curl + pypdf for PDFs that fail
   WebFetch; **trust the report counts, not the fleet page**).
2. Update `inputs/balance_sheets/<ticker>_<quarter>.yaml` (with the
   provenance trio `source_url` / `retrieved_at` / `filing_period_end` —
   required from 2026-Q2 sheets on); touch the fleet manifest only for
   entries/exits/deliveries. **A snapshot advance moves BOTH halves in one
   commit: bump the manifest `report_date` to the new quarter WITH the new
   sheet** — the pair guard reds any run whose two halves disagree, and
   `scripts/check_snapshot_advance.py` warns on the one pattern the guard
   can't see (snapshot advanced, label not bumped). Cost structure and
   dividend policy only if the policy actually changed.
3. **Issuer-report S&P sweep** (per filing, ~1-3 prints/quarter with
   better vessel detail than Pareto prose): scan the filing + PRs for
   disclosed vessel sales/purchases. Per-vessel price → promote to
   `transactions/<class>.yaml`; en-bloc without split = document, never
   back-solve. Any promotion triggers the prints→rerun→drift loop.
4. Rebase the watchlist vintage TOGETHER: `current_price` +
   `consensus_pnav` + `consensus_fwd_pe` from the same Pareto daily
   (never the price alone — see the TEN gotcha). APPROX names: refresh
   the price leg only, keep the APPROX flags.
5. `python -m crude_tanker_fv.sp_scan --names <TICKER> --since
   <quarter-start>` — skim the name's Pareto mentions for stance/NAV
   statements and missed prints.
6. Run the pipeline + `/reconcile <TICKER>` — SANITY must be OK; stop
   and investigate a FAIL, don't paper it over.
7. Drift gate: >2pp spread move or position flip → annotate
   `decisions/<ticker>_log.md` with the why (market move? new data?
   methodology?).

## Onboarding a new sector — the workflow

METHODOLOGY §11.4 has the engine-side checklist. Before any code:

1. **Methodology decision doc first** (≈§11.x equivalent) — scenarios,
   weight family name (sector-namespaced), cycle anchors, vessel classes,
   external NAV anchor (does Pareto cover this sector? if not, what?).
2. Land the YAML structure, scenario routing, class map.
3. Add the first validator name. Reconcile. Iterate.
4. Add second validator. Pin a `test_<sector>_locked_weights` so weight
   changes are intentional.
5. Run `/reconcile --calibration-lock <sector>` — the v1 lock test
   reports the hit rate against the new-sector bar (≥70%/±10%).

Methodology decisions get time-boxed to one session. v1 ships; refinements
go in Q3.

## Harvest the MB Shipbrokers weeklies — the workflow (added 2026-06-29)

Four feeds, Fridays by email from `*@mbshipbrokers.com` (Container / Tanker / Dry Bulk /
LNG). Email tables are IMAGES; the PDF behind the "Download report" link is the artifact.
MB is a **cross-check, not a calibration input** (VIE discipline) — promotion is human-only.

**Agent half (authed Gmail session — not cron):**
1. Search Gmail (read-only): `from:mbshipbrokers.com newer_than:21d` (or `subject:Weekly`).
2. For each new weekly, `get_thread` and pull the `cdn.flxml.eu/lt-...` URL that the
   "Download report" button points to (the FIRST `lt-` link in the plaintext body — the
   others are sign-up / privacy / social). If a thread body exceeds the tool limit it is
   saved to a tool-results file; extract the link from there with `grep`/`jq`.
3. Write one TSV line per report:  `<YYYY-MM-DD>\t<email subject>\t<download url>`.

**Mechanical half (scriptable):**
4. `python scripts/mb_harvest.py links.tsv` — fetches each via `fetch_pdf.py` (cdn.flxml.eu
   allowlisted), validates `%PDF`, archives under `inputs/research_mb/<feed>/<YYYY>/`
   (gitignored cache). Idempotent: skips files already archived.

**Then (review, human-gated):** read the new issues (`pypdf`); cross-check S&P prints / value
assessments against the curves; a promotable per-vessel print goes through the normal §9.9
drift-gate path; rate/anchor disagreements are logged (§6 footnote), never auto-applied. The
LNG feed feeds the FLNG/CCEC cross-check (`outputs/mb_lng_crosscheck_*.md`).

## Runbook — the command reference (migrated from CLAUDE.md 2026-07-01)

- **Regenerate the surface:** `scripts/regen.sh <QUARTER>` (2026-09-10) — refuses a dirty determinant tree, re-runs the five weight-family sidecars when `scenario_inputs.yaml` is newer than their output, runs the pipeline, runs the outputs-hygiene guard, prints the stamp + family status. Use it instead of calling the pipeline directly: three surfaces shipped with stale sidecars this quarter (9/02, 9/07, 9/10).
- **Shadow-value a draft pair:** `bash scripts/shadow_regen.sh <TICKER> <QUARTER>` (2026-09-11) — copies `inputs/balance_sheets/<t>_<Q>.yaml.draft` (+ `inputs/fleet_manifests/<t>.yaml.draft` if present) over the live files in a throwaway git worktree of HEAD, runs the pipeline there, runs the pair/provenance guards, and prints the name's shadow scorecard row vs the committed one (deltas + guard failures) as a SHADOW-JSON block. Writes nothing to the tree or to git. The unattended `crude-fv-results-shadow-build` task uses it; a hand build can too, before touching the live pair. The live loaders never see a `.draft` (`tests/test_shadow_regen.py`).
- **The declared graph:** `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.graph check` (R1-R7 over `graph.yaml`; a `GRAPH: note R7 …` line leaves the suite green — wait for the next scheduled job before touching `launchd_utc_offset_hours` — run it after adding or changing any cron job, wrapper lane or scheduled task) and `… graph render --write` (re-renders the block in OPERATING.md; `tests/test_graph.py` fails while it is stale). New node = a `graph.yaml` entry with reads / writes / triggers / `commits`. (2026-09-13)
- **Forks as a tool:** `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.forks list` (executable today) · `… forks mark <id> executed|halted --note "…"` (rewrites the status line in place, comments kept) · `… forks open --id … --kind judgment|state-tracking --doc … --recommendation "…"`. The land lane opens a `buyflip_<ticker>_<date>` fork on a flip toward BUY and lands once it is executed. (2026-09-13)
- **Watchlist pair rebase:** `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.rebase TICKER --apply` — anchor-preserving (implied broker NAV + EPS basis carried), price / pnav / fwd_pe from the prices_daily close on ONE vintage, textual edit with comments kept; without `--apply` it writes `inputs/watchlist_rebase_<date>_<t>.yaml.draft`. Refuses a stale (>5d) or review-flagged quote. (2026-09-13)
- **Dry FFA promote:** `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.ffa_promote [--apply] [--packet-out decisions/ffa_promotion_<date>.md]` — selects the newest clean 5-tenor capture newer than the committed vintage, builds the ruled straddling construction, checks every cycle band, writes the packet. Prints `FREEZE: <reason>` and exits 2 on anything unruled (flagged parse / unruled shape / stale print / band crossing) — a freeze is the correct outcome, never a reason to hand-construct. (2026-09-13)
- **Price attribution:** `PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.annotate [--apply]` — writes the dated attribution entry for gate rows that moved on PRICE alone, and refuses everything else with the reason named (a fair-value move, a flip toward BUY, a NAV or re-read breach, a changed price basis, a determinant other than the price vintage moving, or a cent-rounding budget too coarse to tell a tape move from a curve move). Runs unattended inside the sentinel's [price-leg] lane; a refusal leaves the row UNEXPLAINED and freezes auto-land on (a), which is correct. (2026-09-15)

The daily essentials (tests / pipeline / reconcile / drift gate / fetch_pdf / two-venvs) also
sit in CLAUDE.md; the full list lives here.

- **Tests:** `PYTHONPATH=src .venv/bin/python -m pytest -q` (count grows monotonically; the
  current census lives in README — do not hardcode it here, it rots). Never bare `pytest` —
  the package isn't installed.
- **Pipeline:** `python -m crude_tanker_fv.pipeline <QUARTER>` (e.g. `2026-Q1`).
- **Pre-flight (what's stale / missing):** `python -m crude_tanker_fv.refresh` — its §0 consumes
  `inputs/earnings_calendar.yaml` (hand-maintained; update on sight when the weekly digest flags a
  newly-announced date).
- **Reconcile a name:** `python -m crude_tanker_fv.reconcile <TICKER>` (or `/reconcile <TICKER>`).
- **Drift gate (committed, Pareto-free):** `python -m crude_tanker_fv.drift_gate` — compares current
  pipeline outputs vs the tracked `baselines/reconcile_baseline.yaml` (EV% / tool NAV / position band /
  k_broker on its *second difference*); exit 1 on UNEXPLAINED drift. `tests/test_drift_gate.py` runs it
  as a build gate. Re-anchor ONLY via `./scripts/ratify_baseline.sh "<cause>"` (mandatory cause) or by
  `promote land`, which runs that script behind its five preconditions and writes its own commit — the
  morning price-leg lane calls it, and since 2026-09-18 so does the fork executor at its step 0b — **never
  hand-edit the numbers.**
- **S&P print scan (incremental):** `python -m crude_tanker_fv.sp_scan` — scans Pareto dailies not
  yet scanned (a per-path set since 2026-09-02: a late-arriving older issue is scanned, not hidden
  behind the date cursor; `--since`/`--full` keep the date semantics) and writes the review queue
  to `outputs/sp_print_candidates.md`. The scan reads `_manifest.json` — both chains index before
  they scan (the 2026-09-01 "nothing to scan" was a stale index, guard-tested). Human-classified into
  `transactions/<class>.yaml`; **never auto-promote.** Every `sp_scan` mode is local-only BY
  CONSTRUCTION (network download lives in `fetch_links`).
  **Before promoting an UNNAMED broker print, sweep the class file for same-age/similar-price rows in
  the trailing ~6 weeks — unnamed prints are re-report magnets** (2026-08-09: all 4 queued unnamed
  Pareto prints resolved to already-promoted deals — Jag Lokesh, WF Artemis, Wooyang Belos, Singapore
  Spirit/TNK; marks_trail_triage_2026-08-09.md §B-dedupe).
- **Daily price refresh:** `python -m crude_tanker_fv.price_refresh` — fetches watchlist closes (Yahoo)
  into the automation-writable `prices_daily.yaml`; launchd 18:30 daily. Pipeline values at the live
  close; watchlist statics stay as the consensus_pnav/fwd_pe vintage anchors. Flagged quotes (>15% day
  move, >30% vs static) are written but never applied. Writes atomically; a bare run outside the
  wrapper ledgers itself `manual:` in `state/automation_runs.log` (2026-09-02 — the seven 8/17-24
  outage salvages had been invisible).
- **Daily ingest chain:** `scripts/ingest_rocketchat_cron.sh` — launchd 07:00, chains RC ingest →
  `pareto_archive --build-manifest --incremental` (new PDFs only; added 2026-09-02 — before it the
  weekday scans ran on Saturday's index) → `sp_scan` → `ffa_ocr`.
- **Regen sequencing (2026-08-29; bit 2× in one week — FLNG 8/25, TRMD 8/29):** COMMIT the
  pair/inputs FIRST, regen SECOND. A regen over uncommitted inputs stamps `source_commit
  -dirty` and the hygiene guard reds it AFTER the ~8-min run — the guard catches it, but a
  wasted regen each time. Corollary: an uncommitted regen also blocks the price cron's
  dirty-tree stand-down (8/25-8/29: four stale sessions from one uncommitted tree).
- **Flush automation drift:** `./scripts/commit_drift.sh` — stages + commits (one step) the 8
  automation-written files the launchd jobs churn. COMMIT-ONLY (push stays manual). Decision logs +
  per-name pipeline outputs EXCLUDED — commit those deliberately with their annotations.
- **Weekly news pull (mechanical):** `scripts/news_pull_cron.sh` — launchd Sat 08:00, chains RC ingest
  → `pareto_archive --build-manifest` (full rebuild, reordered ahead of the scan 2026-09-02) →
  `sp_scan` → `ffa_ocr`. The linked-report harvest (`sp_scan --links` → `fetch_links`) left the
  chain 2026-09-02 (one citation ever); both modules remain for on-demand onboarding, and
  `fetch_links` stays its own ask-tier module so every `sp_scan` mode is local-only.
- **Oslo issuer poller:** `python -m crude_tanker_fv.newsweb_poll [--dry-run] [--all]` — the Oslo/
  Euronext issuer-release channel for BRUT/MPCC/CAPT/BWLP (added 2026-08-16). Staging-only, rides
  the hourly edgar-poll row; mechanics + the two filter traps in §Data-sources below.
- **FFA widget OCR (incremental):** `python -m crude_tanker_fv.ffa_ocr` — parses the daily 3-panel
  Cape/Pmax/Smax screenshot into `state/ffa_ocr_curves.json` + review queue; `--staleness` exits 1 if
  the feed is >7 days quiet. Promotion to `inputs/market_data/ffa_forward_curve.yaml` is HUMAN-ONLY
  until the autopilot's lane B lands (Stage B, `decisions/autopilot_authority_2026-09-02.md`).
  From the 24th the widget drops the expiring month, so a 4-tenor panel is complete (2026-09-02 —
  the queue no longer flags month-end captures); Q tenors sort from the print's own quarter.
  Scratch under `state/ffa_scratch/` — tesseract can't read /tmp in the agent sandbox.
- **Weekly news pull (agent-judgment):** `/news-pull` — web-sweeps watchlist names (weighted to APPROX
  + live-event names) into a dated digest. Review-only; promotion is human-only.
- **Weekly trigger check (Thursday):** the scheduled task `crude-fv-trigger-check-draft`
  (`scripts/scheduled_tasks/…SKILL.md`) drafts the geopolitics card's check to
  `decisions/trigger_check_<card>_<due>.draft.md` and commits it; the 11:15 TRIGGER-DUE page names the
  draft. Recording is the owner's, in a chat: `/record-trigger-check <card> <due> [hold|fired|reweight]`
  (renames the draft to the record, re-arms or fires the card, runs the register guards, commits, pushes).
- **PDFs:** the `.venv/` has `pypdf`. `.venv/bin/python scripts/fetch_pdf.py <url>` (WebFetch fails on
  many FlateDecode PDFs). Raw `curl` works but prompts.
- **Two venvs:** the engine + all `crude_tanker_fv` code + the full suite run on `.venv` (Python
  **3.9.6**). The vendored `shipping_harvester` (broker-weekly parser for the Test 1 backfill) requires
  **3.10+**, so a dedicated `.venv310` (Python 3.12, gitignored, provisioned via `uv`) is used ONLY for
  it: `cd shipping_harvester && PYTHONPATH=. ../.venv310/bin/python -m pytest -q` (57 tests). Never run
  the engine/tests on `.venv310` or the harvester on `.venv`. Its **source is tracked** (2026-06-23 —
  Test 1 depends on its parsers); only `shipping_harvester/data/` (crawl cache + broker PDFs) is gitignored.
- **Test 1 (engine EV% ex-post) backtest:** harness `backtest/run_engine_test1.py` (runs on `.venv`)
  reads vintages from `backtest/vintages/`. Method + input spec: `backtest/PRE_REGISTRATION_TEST1.md` +
  `backtest/DATA_CONTRACT_TEST1.md`.

## Data sources — per-source fetch mechanics (migrated from CLAUDE.md 2026-07-01)

**Tanker forward-print standing rule (prune F19, 2026-09-10 — replaces the retired `tanker_forward_print_lands` card and the TRIGGER-EVIDENCE lane).** A tanker FFA or 1-year time-charter print landing in a daily or weekly promotes ON SIGHT through the promote/regen path, never through a re-armed watch: freeze the predicted-impact block first (which files move, which are frozen; ΔNAV exactly 0.0 for a rate-only leg), classify the print in the pre-registration's own vocabulary (direct / single-print / derived-ratio / spec-premium), band-check against the current anchors (Stage B, 2026-09-09), land inputs first and outputs second. The Pareto daily carries no 1-year TC table — every Stage B input was an issuer fixture disclosure, so the weekly MB harvest and the filings poll are where prints arrive. The only sentinel nag is `UNINGESTED-PRINTS twelve_month_tc.yaml` (a daily more than 7 days past `as_of.default`).

The *discipline* rules (trust the report not the fleet page; Pareto = the consensus_pnav source with
NAT/ASC/CCEC APPROX; VIE/MB are cross-checks, not calibration) live in CLAUDE.md. The per-source fetch
quirks live here:

- **WebFetch fails on many IR PDFs** (FlateDecode binary). Pattern: `.venv/bin/python scripts/fetch_pdf.py
  <url>` (downloads to /tmp, validates the host against `inputs/data_sources.yaml` — add new sources
  THERE, not to the script), then parse with pypdf.
- **A staged inline-XBRL exhibit is READABLE — de-tag it locally, never fall back to R-renderings**
  (2026-09-21, TEN). A single-file iXBRL 6-K is one ~94k-token line, so the Read tool refuses it and
  it *looks* unreadable. It is not: a dozen lines of stdlib `re`/`html` render it as plain text
  (strip `<script>`/`<style>`, drop tags, unescape entities, collapse blank lines). The TEN H1 shadow
  declared the exhibit unreadable, worked from EDGAR R-renderings that were never on disk, and
  therefore reported "the 6-K carries no per-vessel shuttle day rates" — while the Charters-out
  schedule that *derives* the rate sat five lines below the commitment figure it did cite from that
  same note. The miss cost a quarter of carrying a $453.1M leg on an APPROX. This is CLAUDE.md's
  "absence isn't evidence" in its exact shape: a parser dropped the field and the absence was scored
  as data. R-renderings are also unciteable — they are not in the repo, so no figure taken from one
  can be verified later.
- **ECO's domain TLS chain fails WebFetch entirely** — use fetch_pdf.py, which carries the one audited
  TLS-verification exception for that host.
- **EDGAR needs a contact User-Agent** — fetch_pdf.py sends an SEC-compliant contact string (was 403 on
  `Mozilla/5.0`); www.sec.gov is allowlisted. (2026-06-26.)
- **Compass Maritime weekly URL changes every week** — pattern
  `compassmar.com/wp-content/uploads/YYYY/MM/Compass-Weekly-Report-MMM-DD-YY.pdf`.
- **The Pareto dailies carry hyperlinks to Pareto's detailed research** as PDF annotations —
  `extract_text()` NEVER sees them (they live in /Annots). Harvest: `sp_scan --links` → `fetch_links`
  → `pareto_archive --build-manifest`. Full NAV breakdowns/estimates, far richer than the daily prose.
  Part of weekly/quarterly ingest.
- **MB Shipbrokers weeklies** — email tables are IMAGES; the PDF behind the "Download report" flexmail
  link is the artifact (harvest from Gmail read-only, fetch with `fetch_pdf.py`, cdn.flxml.eu
  allowlisted; archive `inputs/research_mb/<feed>/YYYY/`). Full steps in the MB workflow above.
- **HKEXnews (2343 / any future HKEX name)** — `python -m crude_tanker_fv.hkex_poll` (F-3 light
  adapter, 2026-07-14; rides the hourly edgar-poll launchd row). Per-company JSON index
  `titleSearchServlet.do?stockId=<id>` (stockIds from `hkex_stockid:` keys in data_sources.yaml,
  pinned in `tests/test_hkex_poll.py`); the servlet's `result` field is a JSON-encoded STRING;
  filings are English PDFs under `www1.hkexnews.hk/listedco/...` (fetch_pdf-allowlisted via the
  data_sources URLs). Arrivals land in `state/edgar_manifest.jsonl` with `source: "hkexnews"` —
  sentinel FILING-LANDED work unchanged (the never-runnable `draft_queue` was deleted 2026-09-02, prune row 13). HK cadence is SEMI-ANNUAL (Annual ~Mar,
  Interim ~Jul/Aug) + Monthly Returns (share count).
- **Oslo/Euronext NewsWeb (BRUT / MPCC / CAPT / BWLP)** — `python -m crude_tanker_fv.newsweb_poll`
  (added 2026-08-16; rides the same hourly edgar-poll row). Closes the LAST venue with no filing
  lane: these names have `sec_edgar: null` and no HKEX id, so before this the only thing that could
  see a demerger or a placement was the weekly agent sweep — and when that lapsed, BRUT's 7/07
  demerger sat unread five weeks, MPCC's 6/25 acquisition seven, MPCC's +10.0% share placement
  (6/30–7/02) and CAPT's 8/06 + 8/13 deliveries likewise. Feed is MFN's JSON Feed 1.1
  (`mfn.se/all/a/<slug>.json`; slugs from `mfn_slug:` keys in data_sources.yaml, pinned in
  `tests/test_newsweb_poll.py`). **Two mechanics worth knowing before you touch the filter:**
  (1) relevance is a DENY-list (only `sub:ci:insider` is dropped), because CAPT's vessel deliveries
  are tagged `ext:ob:non-regulatory` — an allow-list on `:regulatory` would drop the very releases
  the module exists for; (2) each release can arrive TWICE — `source: "ob"` (Oslo Børs mirror,
  `TICKER: ` title prefix, `<pre>` body) and `source: "mfn"` (issuer distribution, richer tags) —
  under different news_id *and* different group_id, so dedup keys on (date, punctuation-stripped
  title) and keeps the richer copy. Release bodies stage as `.txt` + any PDF attachments into
  `inputs/filings/<ticker>/`; arrivals land in `state/edgar_manifest.jsonl` with `source: "newsweb"`.
  **BWLP is dual-lane** (Oslo primary + NYSE FPI) and is polled by BOTH — dedupe at read time.

## Earnings-date sweep — the recurring verification (added 2026-07-21, owner directive)

The calendar's windows are only as good as their last verification — the SBLK case
(2026-07-21): a wrongly-"confirmed" entry looks SAFE to every mechanical check, because
date-setting PRs are newswire releases, mostly NOT EDGAR filings. So the sweep itself is
agent work; the TRIGGER is mechanical (sentinel `EARNINGS-UNCONFIRMED` — a window opening
≤10d with status=expected pages per-name; `EARNINGS-SWEEP-STALE` — any window ≤21d with
`meta.last_date_sweep` >7d old pages for the full sweep).

**The sweep (weekly during earnings season, on the sentinel page or at the Saturday session):**
1. Fan out research agents over: every `expected` name whose window opens within ~21d,
   PLUS re-verification of `confirmed` names inside 14d (the FLNG early-release pattern).
2. Per name, only an ISSUER-GRADE source upgrades to confirmed: the company's own date PR
   (GlobeNewswire/PRNewswire/Business Wire), its financial-calendar page, or an exchange
   calendar (Euronext/Oslo Newspoint, HKEXnews board-meeting notice). Aggregator dates
   (MarketBeat/stockanalysis/Nasdaq) are ESTIMATES — record them labeled, never as status.
3. Update `inputs/earnings_calendar.yaml`: status + window + a basis line carrying the
   citation, the verbatim date sentence's substance, and the sweep date. Windows the
   pattern no longer supports get honestly RE-SHAPED (SB's Q1 slip, GSL's lateness), not
   left to look precise.
4. Stamp `meta.last_date_sweep`, run the calendar guard (`pytest -k calendar`), commit.

The backstop stack, for the record: the sweep verifies dates AHEAD; EARNINGS-DUE pages
14d out; the EDGAR poller polls in-window names every run (and everything at least ~12h)
so a print is never missed outright — what the sweep protects is the PREPARATION: the
report-day refresh queued, FVs current at the event, and no false confidence from a
stale "confirmed".

## Consensus-pair recapture — the quarterly packet (added 2026-07-03, WO2 3.1)

The consensus pair (`current_price` + `consensus_pnav` + `consensus_fwd_pe`) is valid only AS A
PAIR from one vintage — the TEN $44 lesson. The 42-day watchlist-vintage lane (`STALE-INPUT`)
and the ±30% static guard page the recapture (the standalone trigger card was retired
2026-09-02, owner F20 — only the 7/06 rebase was ever card-driven); it is ONE sitting, one source:

1. Pick ONE Pareto Shipping Daily (the newest with the full share-price/P/NAV/P/E table);
   note its date — that date becomes every touched name's `as_of`.
2. For every covered name: transcribe price, P/NAV, fwd P/E from THAT daily. Never mix days,
   never keep an old pnav against a new price.
3. APPROX names — DISCOVERED per sitting, never enumerated here (rule reshaped
   2026-08-09, owner ruling: the prose roster went stale when containers onboarded —
   "when a rule can be a test, it becomes a test"): any covered name the chosen daily
   prints NO P/NAV for is handled APPROX for that sitting — price + fwd P/E from the
   daily, pnav stays flagged with its own basis note ("flag, don't fake"). Names absent
   from the table entirely keep their FULL static pair at its current vintage. The
   expected two-sense partition is PINNED in `tests/test_approx_roster.py` (against
   `reconcile.APPROX_PNAV_TICKERS`) — an onboard or Pareto coverage change must move
   the pin deliberately, so divergence is a test failure, not silence. Residual:
   k_broker = price ÷ consensus_pnav, so APPROX names carry a mixed-vintage pair BY
   DESIGN — any k-band test allowance retired at a rebase needs a scoped APPROX-name
   replacement.
4. Rebase `inputs/watchlist.yaml` in one commit; run the gate loop (pytest -> reconcile ->
   drift annotate/ratify). Band flips from the price move follow the isolate-commit
   discipline (memory: isolate commit from price drift).
   **FX rule (codified 2026-08-09):** conversion applies to the PRICE leg only — pnav and
   fwd P/E are unit-free ratios — at the DAILY's date FX, never the promote date (the
   MPCC/CAPT machinery: e.g. "kr 24.0 × 0.101838 Jul-3 FX"). Applies to every non-USD
   quote (NOK: BRUT/CAPT/BWLP/MPCC; HKD: 2343 when sourced).
   **Staging pattern (sanctioned 2026-08-09):** transcription may land first as
   `inputs/watchlist_rebase_<date>.yaml.draft` with a NOT-APPLIED marker — transcription
   and promotion are separate acts; the draft is the sanctioned artifact, and the
   promote consumes + deletes it.
5. Re-arm the trigger to the next quarter boundary; record the sitting in decisions/.

## Ops gotcha — long-running nohup jobs (migrated from CLAUDE.md 2026-07-18)

Long-running nohup jobs die silently (block-buffered stdout; 2026-06-10). Pattern:
`nohup sh -c 'PYTHONUNBUFFERED=1 … ; echo "EXIT $?"' >> log 2>&1 &`; watch log mtime, not contents.

## Week-close checklist (migrated from CLAUDE.md 2026-07-01; codified 2026-06-11, owner decision)

Work is organised in sprints ("Weeks"). At the END of each Week, before handoff, run this — docs accrete
seams during a sprint and this is where they get smoothed:

1. **Documentation audit.** METHODOLOGY.md: relocate misfiled content, fix stale counts/k_brokers/
   positions, verify cross-references, write the Week's Appendix A entry. CLAUDE.md: rules current;
   TICKER_NOTES.md reconciled against the latest delta report; README.md + LIMITATIONS.md refreshed
   (closed limitations marked closed, not deleted). Fan out read-only audit agents; apply fixes in the
   main session.
2. **Verification gate.** Full pytest green; pipeline runs clean; `/reconcile --all` SANITY column all
   OK/n-a-APPROX.
3. **PLAN.md rewritten** for the next Week (theme, steps, standing threads, definition of done).
4. **Clean git state** — everything committed with the Week-close CHANGELOG.md entry; no untracked strays
   (check for credential-shaped files).
5. **Push to GitHub** (`git push origin main`) — at Week close at minimum; mid-week pushes after
   significant commits are fine too.

## Correctness and delivery operations (2026-09-22)

The scorecard schema is 2.9: broker_reference carries the matched price, P/NAV, NAV and source date;
cycles carries explicit company/sleeve identities, ratios, labels and anchor bases. Headline valuations
and cycle methodology are unchanged. Broker comparisons must agree with reconciliation.

Filing triage uses `sh scripts/filings_task.sh list --json`, then `record` with a JSON disposition array
on stdin. The wrapper commits the accession-bearing record before acknowledging it. It owns only
`decisions/filings_triage_log.md`. The complete pending queue is durable; --all is a compatibility alias.
`filings ack` requires an already committed decisions/ record. A queue older than three business days
pages for workflow repair; arrivals themselves remain agent work. Prompt of record: automation/filings-triage.md.

After manual regeneration and deliberate surface/baseline commits, run
`PYTHONPATH=src .venv/bin/python -m crude_tanker_fv.publication publish`.
The production-only publisher checks the existing landing gates before advancing state/publications/current.json.
The five-minute delivery worker also discovers newly acceptable committed surfaces. Tests and shadow
regeneration never call the publisher. The accepted snapshot and source/output hashes identify exactly
what the governor consumed. A publication hold retains the previous snapshot and names its reason.

Run receipts live in state/operations/runs/. SMTP messages are persisted in state/delivery/ before the
first attempt; governor messages use its monitor/state/delivery/. Retry offsets: 5m, 15m, 1h, 6h.
Configuration/authentication failures block; after correction use `operations retry producer|governor <id>`.
SMTP accepted does not prove inbox delivery. Stable Message-ID plus local receipts prevent normal
repeats; an ambiguous disconnect after server acceptance can still duplicate mail.

The worker plist is scripts/com.crude-tanker-fv.delivery-worker.plist. Disable it by creating
state/operations/disabled (or unload its launchd label); receipts and accepted snapshots remain intact.
Re-enable by removing that marker. Verify state/operations/worker.json and the delivery-worker heartbeat.
A worker tick never stands in for a missing scheduled monitor run.

Scheduler permissions: install the explicit rules in automation/task_permissions.json into the user
settings and the task's working-folder settings. Do not rely on Auto mode or SKILL.md allowed-tools.
The scoped wrappers work in Manual mode. Denied/new operations require a workflow repair, not blanket
bypass mode. See automation/README.md for provenance and runtime limitations.

## Operational status and calendar policy (2026-09-22)

`work_items.yaml` is the versioned operational task view for both projects. It is not a
valuation determinant. Filing acknowledgments, fork rulings, trigger cards, candidate
registries, completed-quarter reviews and publication/delivery receipts remain authoritative.
Run `sh scripts/routine_task.sh tasks show` to read the live projection, or `tasks sync` to
persist a locked, validated, registry-only commit. Missing/conflicting evidence creates an
UNKNOWN task and a repair task. Open manual tasks need evidence refreshed after 30 days.
Owner-blocked tasks keep resolver `owner`; completing a numerical reconciliation does not
clear a candidate's remaining restrictions. The old roadmap was retained as a migration
snapshot in `decisions/workflow_migration_2026-09-22.md`.

After committing every shadow narrative `decisions/<ticker>_shadow_build_<date>.md`, run
`sh scripts/routine_task.sh tasks shadow --report <that-path>` with a JSON array on stdin.
Each blocker requires `id`, `resolver` (owner/agent/external), `next_action`, `condition`,
and `blocking_decision_ids`. Use an empty array only when no blockers remain. The command
requires committed report evidence and commits only the matching JSON sidecar. Missing
structured blockers are UNKNOWN, never inferred clear from prose.

Live calendar policy is controlled by `inputs/calendar_policy.yaml`. Before enabling it,
review the preregistered full-book comparison. Dated FFA metadata is stored beside each
class under `calendar_nodes`; schedules have explicit origins. New or refreshed schedules
must update their calendar mappings in the same commit. Monthly means include only the
remaining current-quarter months, while a direct quarterly quote takes precedence. Annual
identities preserve quoted quarters; residual rounding goes to earliest unquoted quarters.
Ruled tail steps precede flat carry-forward. Every constructed/extended node is labelled;
no scenario weights, cycle bands or within-quarter conventions change. Historical replay
keeps its explicit historical quarter and never applies live calendar alignment.

Rollback: set calendar `enabled: false` to hold October promotion and restore legacy
projection behavior; set `work_items.yaml` `integration_enabled: false` to stop task-sync
notifications while preserving task evidence. Stop the entire worker with
`state/operations/disabled` only if needed. Accepted snapshots, outboxes, and receipts are
retained. Quarterly completion remains protected by the governor's committed ledger.

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
dates — update the calendar when it does. Cadence quirks worth
remembering: TEN reports Q2 in SEPTEMBER (H1 reporter); FLNG's calendar
slot is Aug-28 but 2025's release came Aug-20; the early cluster
(STNG/ASC/TNK/CCEC) opens Jul-28.

Per name, on report day:

1. Pull the 6-K/10-Q + press release (curl + pypdf for PDFs that fail
   WebFetch; **trust the report counts, not the fleet page**).
2. Update `inputs/balance_sheets/<ticker>_<quarter>.yaml`; touch the
   fleet manifest only for entries/exits/deliveries, cost structure and
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

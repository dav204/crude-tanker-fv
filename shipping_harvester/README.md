# shipping_harvester

Pulls the free broker-weekly PDFs (Hellenic Shipping News + Capital Link mirrors)
into a **`[Q]`-keyed, tidy long-format panel** of market marks — vessel values by
age anchor, period (1-yr) TC, spot TCE, and demolition $/ldt — ready to join into
your factor build.

It does the boring-but-fiddly 80% for free: crawl → dedupe → pick each broker's
last issue on/before quarter-end → download (cached) → parse → store. The
remaining 20% (per-broker table parsing) is scaffolded with a reusable pattern and
two worked examples; you tune column keywords against real issues.

## Why it's built this way

The crawl/dedupe/quarter-keying/storage layers are fully general and tested. The
**table extraction is the only part that genuinely needs per-broker tuning** —
column order, header wording and units differ by house and drift over time, and
can't be nailed blind. So parsing is a pluggable layer: a `GenericParser` that
never fails (records the issue, extracts nothing) plus per-broker subclasses that
supply a keyword→column map.

## Install

```bash
pip install -r requirements.txt
```

Pure-Python deps (pdfplumber, requests, bs4, pandas, pyarrow). No system binaries
required. (Optional: `poppler-utils` gives you `pdftotext -layout` as a fallback
for stubborn multi-column issues.)

## Usage

```bash
# Full pipeline for a quarter range (HSN only)
python -m shipping_harvester.cli run --since 2024Q1 --until 2026Q2

# Also crawl Capital Link contributors
python -m shipping_harvester.cli run --since 2025Q1 --until 2026Q2 --capitallink

# Inspect one PDF's tables + text — use this to build/repair a parser
python -m shipping_harvester.cli inspect data/pdfs/allied/2026W24_ab12cd34.pdf

# Print marks coverage (quarter x kind) from the stored panel
python -m shipping_harvester.cli coverage

# Resolve the multi-broker panel onto your factor schema
python -m shipping_harvester.cli factor --quarter 2026Q2
python -m shipping_harvester.cli factor --mode median --spread-warn 0.08
```

Output lands under `./data/`:

```
data/
  pdfs/<broker>/<YYYY>W<WW>_<sha8>.pdf   cached raw issues (idempotent)
  marks/<broker>/<YYYY>Q<q>.json         per-(broker, quarter) marks, auditable
  manifest.jsonl                         append-only log of everything crawled
  marks_panel.parquet                    <-- the table your factor pipeline reads
  factor_marks.parquet                   <-- resolved onto your factor schema
```

`marks_panel.parquet` columns: `quarter, broker, report_date, kind,
vessel_class, age_anchor, metric, value, unit, note, parser, source_pdf,
source_post`.

## The `[Q]` rule

Your marks are "`[Q]`, dated ≤ quarter-end". So for each target quarter the
selector takes each broker's **latest issue with published date ≤ quarter-end**.
`report_date` preserves the issue's true date; if the chosen issue is more than
`--stale-days` (default 14) before quarter-end — i.e. a broker went quiet near the
cutoff and we reached back — the run flags it `STALE` so you can see thin spots
before they bite.

## Adding / repairing a broker parser

1. Run `inspect` on a downloaded issue to see the table indices and headers.
2. Copy `parse/allied.py` to `parse/<broker>.py`, set the keyword→column maps to
   match what you saw. The reusable helper does the rest:

   ```python
   marks += base.map_value_table(
       table,
       {"newbuild": ["resale"], "five_year": ["5 year"], "ten_year": ["10 year"]},
       kind=KIND_VESSEL_VALUE, metric="value", unit="musd",
   )
   ```

3. Register it in `parse/__init__.py` (`_PARSERS["<broker>"] = <Broker>Parser()`).

`map_value_table` locates columns by **header keyword, not fixed position**, so a
parser survives column reorders, and it auto-detects 1- vs 2-row headers.

Implemented: **Allied** (values, period TC, demolition), **Intermodal** (values,
period TC, spot TCE), **Xclusiv** (values, spot TCE), **Weber** (tanker spot +
1yr/3yr period TC), **GMS** (demolition $/ldt by market and type). Anything not
listed falls back to generic until you add it — the pipeline still runs and
records those issues.

## Format-version dispatch

Broker layouts drift (Weber's 2019 "Spot Market" table is nothing like its 2024
two-column "TANKER ROUTES" layout), so a parser tuned to today's format mis-reads
old issues. `parse/dispatch.py` routes each issue to the right format-version
parser: a **structural probe** on the PDF text (strongest — Weber routes on
whether "TANKER ROUTES" is present), then the **issue date** (`since`/`until`) as
fallback, else newest version flagged low-confidence.

If every version is probe-guarded and none match, it does **not** guess — it
records `parser='generic:unrecognized-format'`, so a deep backfill never silently
mis-parses an unfamiliar layout. The run log prints the chosen version per issue
and flags low-confidence matches; the version label lands in the panel's `parser`
column for provenance.

Add an era by registering a `FormatVersion(label, parser, since=…, until=…,
probe=…)` in `dispatch._VERSIONS[broker_id]`. Single-format brokers have one
open-ended version (unchanged). Weber ships with two: `weber_2024` (current) and
`weber_2017` (legacy — spot-only, since that era predates the period-TC callout).

## Factor adapter

`factor.to_factor_marks(panel)` collapses the multi-broker panel onto your schema
— `vessel_value_curves[class]` (newbuild / five_year_benchmark /
ten_year_benchmark / scrap_25yr / scrubber_premium / eco_premium_pct),
`twelve_month_tc[class]`, `spot_tce[class]` — one row per
(quarter, segment, class, field).

- **Source precedence.** When several houses report the same field, a policy
  picks the value (default: Allied for values, Weber for tanker TC and spot). The
  cross-broker spread is recorded regardless, so you keep one number but still
  see when houses disagree. `factor.disagreements(resolved)` returns the groups
  whose spread exceeds the threshold — feed that into your sanity gating. Flip
  `--mode median|mean` for a consensus instead of a single source.
- **Segment-keying.** Tanker and dry bulk share size names (Panamax, Handysize)
  but are different vessels; everything is keyed by segment (Weber sizes →
  tanker; dry-house sizes → dry) so they never reconcile together.
- **Schema dict.** `factor.to_schema_dict(resolved, panel)` emits the nested,
  named shape (`{quarter: {segment: {vessel_value_curves: {...}, ...}}}`) with
  every curve key present — `scrap_25yr` computed from the GMS demolition parser
  ($/ldt × lightweight, tanker price for tanker classes / dry price for dry
  classes), `scrubber_premium` / `eco_premium_pct` left `None` as your `[S/J]`
  judgment inputs.

Edit precedence and thresholds in `factor.DEFAULT_POLICY`. `ffa_forward_curve` and
`historical_tce_means` are out of scope here (synthesised / computed-once
elsewhere).



- The example parsers' keyword maps are a *starting point*, validated only against
  synthetic tables in the test suite — **check them against one real issue per
  broker** before trusting the numbers.
- `eco_premium` / `scrubber_premium` aren't reliably tabulated in the free
  weeklies; keep those as your `[S/J]` judgment inputs.
- Crawl/download are unit-untestable offline (live sites), so they're written
  defensively (REST-first with HTML fallback, retries, robots check). Verify on
  first real run.

## Be a good citizen

These pages are free to read, but automated pulling should be polite. Defaults in
`config.RequestPolicy`: real User-Agent, 2s/host throttle, retry+backoff, and a
`robots.txt` check (`respect_robots=True`). Set a real contact in the User-Agent.
The broker data carries the standard "obtained from market sources, no warranty"
disclaimer — treat it as marks, not gospel, and attribute the source (provenance
is preserved on every row).

## Tests

```bash
pytest -q     # 19 tests: quarters, dedupe, attribution, link extraction,
              # value cleaning, and an end-to-end parse on a synthesised PDF
```

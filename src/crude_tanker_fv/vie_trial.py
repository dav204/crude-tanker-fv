"""Local-only VIE exit evidence. Never publishes, promotes, sends, or buys."""

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
import uuid
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from .calendar import construct_panel, index, keys, normalize, quarter
from .ffa_promote import DELTAS_2028, PANELS, PANEL_TO_CLASS
from .runtime import atomic_json, locked

ROOT = Path(__file__).resolve().parents[2]
CONFIG = "research/vie-exit/trial.json"
STATE = "state/vie_exit"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(value):
    return digest(json.dumps(value, sort_keys=True, allow_nan=False).encode())


def stamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timestamp has no timezone")
    return result


def read_json(path):
    return json.loads(path.read_text())


def config(root):
    cfg = read_json(root / CONFIG)
    if cfg.get("version") != 1 or cfg.get("mode") != "shadow":
        raise ValueError("invalid shadow trial configuration")
    if cfg.get("annual_budget_usd") != 1500:
        raise ValueError("budget change requires owner review")
    return cfg


def relative(root, raw):
    p = Path(raw)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("artifact path must be project-relative")
    return root / p


def ocr_record(root, day, entry):
    source = relative(root, entry["source"])
    quotes = []
    for panel, nodes in entry["curves"].items():
        for original, rate in nodes.items():
            kind, period = normalize(original, date.fromisoformat(day))
            quotes.append(dict(panel=panel, original_label=original, kind=kind,
                               period=period, rate=rate))
    return dict(version=1, provider="vie_ocr", source_date=day,
                observed_at=None, retrieved_at=None, units=None, quote_basis=None,
                contracts={p: None for p in PANELS}, quotes=quotes,
                raw_artifact=entry["source"], raw_sha256=digest(source.read_bytes()),
                provenance={"parser": "ffa_ocr", "status": entry["status"],
                            "limitation": "capture time is not verified market observation time"})


def panel_subset(record, panel):
    """Select the existing construction horizon without inferring quote identity."""
    printed = date.fromisoformat(record["source_date"])
    nodes = {}
    for row in record["quotes"]:
        if row["panel"] != panel:
            continue
        kind, period = normalize(row["original_label"], printed)
        if (kind, period) != (row["kind"], row["period"]):
            raise ValueError("label/period mismatch")
        key = (kind, period)
        rate = row["rate"]
        if isinstance(rate, bool) or not isinstance(rate, (int, float)) or not math.isfinite(rate) or rate <= 0 or int(rate) != rate:
            raise ValueError("unsupported rate: positive integral USD/day required")
        if key in nodes and nodes[key][1] != rate:
            raise ValueError("conflicting quote: " + period)
        nodes[key] = (row["original_label"], rate)
    start = quarter(printed)
    quarters = sorted((p for k, p in nodes if k == "quarter" and index(p) >= index(start)), key=index)
    if len(quarters) < 2:
        raise ValueError("two adjacent quoted quarters required")
    years = sorted(p for k, p in nodes if k == "year" and int(p) >= printed.year)
    target_year = str(printed.year + 1)
    if target_year not in years:
        target_year = str(printed.year) if printed.month <= 3 and str(printed.year) in years else str(printed.year + 2)
    selected = [(k, p) for k, p in nodes if k == "month" and p >= printed.strftime("%Y-%m")]
    selected = sorted(selected, key=lambda pair: pair[1])[:2]
    selected += [("quarter", p) for p in quarters] + [("year", target_year)]
    if any(k not in nodes for k in selected):
        raise ValueError("required calendar year missing")
    panel_data = {nodes[k][0]: nodes[k][1] for k in selected}
    return construct_panel(record["source_date"], panel_data,
                           DELTAS_2028[PANEL_TO_CLASS[panel]], strict_widget=False)


def validate_record(record, cfg, root, now):
    if record.get("version") != 1 or not record.get("provider") or not record.get("provenance"):
        raise ValueError("invalid normalized source contract")
    raw = relative(root, record["raw_artifact"]).read_bytes()
    if digest(raw) != record["raw_sha256"]:
        raise ValueError("raw artifact hash mismatch")
    observed, retrieved = stamp(record["observed_at"]), stamp(record["retrieved_at"])
    if not observed <= retrieved <= now or (now - observed).total_seconds() > 10 * 86400:
        raise ValueError("future, stale or out-of-order timestamps")
    if date.fromisoformat(record["source_date"]) != observed.date():
        raise ValueError("source date differs from observation date")
    if record.get("units") != "USD/day" or not record.get("quote_basis"):
        raise ValueError("unknown units or quote convention")
    if not isinstance(record.get("quotes"), list) or {q["panel"] for q in record["quotes"]} != set(PANELS):
        raise ValueError("missing or unexpected panels")
    for panel in PANELS:
        expected = cfg["contracts"].get(panel)
        if not isinstance(expected, dict) or not all(expected.get(k) for k in ("identity", "vessel_spec", "evidence", "quote_basis")):
            raise ValueError("benchmark identity unconfirmed: " + panel)
        if record["contracts"].get(panel) != expected or record["quote_basis"] != expected["quote_basis"]:
            raise ValueError("contract or quote-basis mismatch: " + panel)
    return {PANEL_TO_CLASS[p]: panel_subset(record, p) for p in PANELS}


def store_record(root, record):
    name = identity(record)
    path = root / STATE / "curves" / (name + ".json")
    if not path.exists():
        atomic_json(path, record)
    return name


def compare_records(left, right, cfg, root, now):
    a, b = validate_record(left, cfg, root, now), validate_record(right, cfg, root, now)
    rows = []
    for cls in a:
        if a[cls]["periods"] != b[cls]["periods"]:
            raise ValueError("projection periods differ")
        rows.append(dict(vessel_class=cls, before=a[cls]["values"], after=b[cls]["values"],
                         delta=[y-x for x,y in zip(a[cls]["values"], b[cls]["values"])],
                         before_proxy=a[cls]["proxy"], after_proxy=b[cls]["proxy"]))
    return dict(timing="matched" if stamp(left["observed_at"]) == stamp(right["observed_at"]) else "different_observation_times",
                classes=rows, left=identity(left), right=identity(right))


def trial_window(cfg, receipts, today):
    start = cfg.get("window_start")
    if not start:
        return dict(status="not_started", complete_days=0, elapsed_days=0, missing=[])
    first = date.fromisoformat(start)
    provider = cfg.get("selected_provider")
    holidays = set(cfg.get("providers", {}).get(provider, {}).get("holidays") or [])
    days, cursor = [], first
    while len(days) < 20:
        if cursor.weekday() < 5 and cursor.isoformat() not in holidays:
            days.append(cursor)
        cursor += timedelta(days=1)
    elapsed = [d.isoformat() for d in days if d <= today]
    good = {r["source_date"] for r in receipts if r.get("status") == "complete"}
    missing = [d for d in elapsed if d not in good]
    complete = sum(d in good for d in elapsed)
    spans_month = days[0].month != days[-1].month
    return dict(status="pass" if len(elapsed) == 20 and complete >= 19 and spans_month else "incomplete",
                complete_days=complete, elapsed_days=len(elapsed), missing=missing,
                spans_month_end=spans_month, end=days[-1].isoformat())


def feed_days(records, cfg, root):
    by_day = {}
    for row in records:
        by_day.setdefault(row['source_date'], []).append(row)
    results = []
    for day, rows in sorted(by_day.items()):
        result = dict(source_date=day, status='blocked')
        try:
            latest = max(rows, key=lambda r: r['observed_at'])
            concurrent = [r for r in rows if r['observed_at'] == latest['observed_at']]
            if len({identity(r['quotes']) for r in concurrent}) != 1:
                raise ValueError('unresolved same-time revisions')
            validate_record(latest, cfg, root, stamp(latest['retrieved_at']))
            result.update(status='complete', record=identity(latest), observed_at=latest['observed_at'])
        except (ValueError, KeyError, TypeError, OSError) as exc:
            result['reason'] = str(exc)
        results.append(result)
    return results


def document_sources(root, since):
    found = []
    for path in sorted((root / "inputs/research_mb").glob("*/*/*.pdf")):
        day = date.fromisoformat(path.name[:10])
        if day >= since:
            found.append(dict(path=str(path.relative_to(root)), publisher="mb_shipbrokers",
                              feed=path.parent.parent.name, issue_date=day.isoformat(), date_basis="archive_filename"))
    manifest = root / "shipping_harvester/data/manifest.jsonl"
    if not manifest.exists():
        raise ValueError("independent broker manifest missing")
    for n, line in enumerate(manifest.read_text().splitlines(), 1):
        try:
            row = json.loads(line)
            day = date.fromisoformat(row["published"][:10])
            if day >= since and row.get("status") == "ok":
                rel = "shipping_harvester/" + row["path"]
                relative(root, rel)
                found.append(dict(path=rel, publisher=row["broker_id"], feed=row["broker_id"],
                                  issue_date=day.isoformat(), date_basis="harvester_publication_date"))
        except (ValueError, KeyError, TypeError) as exc:
            raise ValueError("invalid broker manifest line %s: %s" % (n, exc))
    return found


def extract_document(path):
    from pypdf import PdfReader
    from .sp_scan import extract_sp_candidates, extract_tanker_period_signals
    candidates, warnings = [], []
    poppler = shutil.which('pdftotext') or ('/opt/homebrew/bin/pdftotext' if Path('/opt/homebrew/bin/pdftotext').exists() else None)
    if poppler:
        output = subprocess.run([poppler, '-layout', str(path), '-'], capture_output=True, text=True, timeout=90, check=True)
        texts = output.stdout.rstrip('\f').split('\f')
        if output.stderr.strip():
            warnings.append('PDF extractor warning: ' + output.stderr.strip()[:300])
    else:
        texts = [p.extract_text() or '' for p in PdfReader(path).pages]
        warnings.append('layout extractor unavailable; table candidates require manual inspection')
    for page, text in enumerate(texts, 1):
        if len(text.strip()) < 30:
            warnings.append("page %s: image-only or empty; visual review required" % page)
        for cls, sentence, demolition in extract_sp_candidates(text):
            candidates.append(dict(page=page, kind="demolition" if demolition else "transaction",
                                   vessel_class=cls, text=sentence))
        for kind, sentence in extract_tanker_period_signals(text):
            candidates.append(dict(page=page, kind=kind, text=sentence))
        if re.search(r"assessment|indicative|second.hand values|time.charter rates", text, re.I):
            candidates.append(dict(page=page, kind="assessment", text="Broker assessment table: cross-check only; inspect original page."))
        candidates.extend(table_candidates(text, page))
    return candidates, warnings


def table_candidates(text, page):
    hits = []
    kind = None
    for line in text.splitlines():
        if re.search(r'^\s*S&P\s*$', line):
            kind = 'transaction_table'
        elif re.search(r'^\s*Period Fixtures\b', line):
            kind = 'fixture_table'
        if kind:
            match = re.match(r'^\s*([A-Za-z][A-Za-z0-9 .\'-]+?)\s{2,}([\d,]{5,})\s+(\d{4})\s+(.*)$',line)
            if match:
                vessel, dwt, built, remainder = match.groups()
                hits.append(dict(page=page,kind=kind,text=line.strip(),vessel=vessel.strip(),
                                 dwt=int(dwt.replace(',','')),built=int(built),
                                 possible_event_key=identity([kind,vessel.strip().lower(),built]),
                                 limitation='Raw candidate row, not a validated price/rate or unique transaction; inspect cited table and notes.'))
    return hits


def pending_documents(root, limit=10):
    doc = read_json(root / STATE / 'documents.json')
    pending = sorted((r for r in doc['documents'].values() if r['disposition'] is None),
                     key=lambda r: (min(s['issue_date'] for s in r['sources']),r['sha256']))
    return dict(total_pending=len(pending), oldest=min((s['issue_date'] for r in pending for s in r['sources']),default=None),
                documents=pending[:limit] if limit else pending)


def scan_documents(root, today, extractor=extract_document):
    path = root / STATE / "documents.json"
    doc = read_json(path) if path.exists() else dict(version=1, documents={})
    if doc.get("version") != 1 or not isinstance(doc.get("documents"), dict):
        raise ValueError("malformed independent document ledger")
    for source in document_sources(root, today - timedelta(days=90)):
        raw = relative(root, source["path"]).read_bytes()
        key = digest(raw)
        if key in doc["documents"]:
            if source not in doc["documents"][key]["sources"]:
                doc["documents"][key]["sources"].append(source)
            continue
        row = dict(sha256=key, sources=[source], disposition=None, candidates=[], warnings=[])
        try:
            if not raw.startswith(b"%PDF"):
                raise ValueError("not a PDF")
            candidates, warnings = extractor(relative(root, source["path"]))
            for hit in candidates:
                hit["evidence_id"] = identity([hit["kind"], re.sub(r"\s+", " ", hit["text"]).strip().lower()])
                hit["corroboration"] = "unverified; deduplicate vessel/event before use"
            row.update(candidates=candidates, warnings=warnings,
                       extraction="partial" if warnings else "candidate_scan",
                       review="pending_visual_review", next_action="Inspect cited pages, classify tables/transactions and commit a disposition; no automatic input promotion.")
        except Exception as exc:
            row.update(extraction="failed", review="pending_repair", warnings=[str(exc)],
                       next_action="Repair extraction and inspect original PDF")
        doc["documents"][key] = row
        atomic_json(path, doc)
    atomic_json(path, doc)
    return doc


def acknowledge(root, sha, evidence_path):
    relative(root, evidence_path)
    raw = subprocess.check_output(["git", "show", "HEAD:" + evidence_path], cwd=root, text=True)
    if sha not in raw:
        raise ValueError("committed disposition must contain document SHA256")
    with locked(root / STATE / "run.lock"):
        path = root / STATE / "documents.json"
        doc = read_json(path)
        row = doc["documents"][sha]
        row["disposition"] = dict(path=evidence_path, sha256=digest(raw.encode()),
                                 commit=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip())
        row["review"] = "triaged"
        atomic_json(path, doc)


def run(root=ROOT, now=None, extractor=extract_document, if_due=False):
    now = now or datetime.now(timezone.utc)
    store = root / STATE
    run_id = now.strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:10]
    receipt = dict(version=1, run_id=run_id, started_at=now.isoformat(), mode="shadow",
                   stages={}, blockers=[], status="running")
    with locked(store / "run.lock"):
        if if_due and (store / 'latest.json').exists():
            prior = read_json(store / 'latest.json')
            retry_after = 900 if prior['status'] == 'failed' else 86400
            if (now - stamp(prior['started_at'])).total_seconds() < retry_after:
                return prior
        atomic_json(store / "runs" / (run_id + ".json"), receipt)
        try:
            cfg = config(root)
            if not cfg["enabled"]:
                receipt["status"] = "disabled"
            else:
                receipt["blockers"] = list(cfg["blockers"])
                try:
                    docs = scan_documents(root, now.date(), extractor)
                    pending = [r for r in docs["documents"].values() if r["disposition"] is None]
                    receipt["stages"]["documents"] = dict(status="persisted", total=len(docs["documents"]),
                        pending=len(pending), failed=sum(r["extraction"] == "failed" for r in pending),
                        oldest=min((s["issue_date"] for r in pending for s in r["sources"]), default=None))
                except Exception as exc:
                    receipt["stages"]["documents"] = dict(status="failed", reason=str(exc))
                try:
                    db = read_json(root / "state/ffa_ocr_curves.json")
                    day = max(d for d, e in db.items() if e.get("status") == "ok")
                    record = ocr_record(root, day, db[day])
                    key = store_record(root, record)
                    receipt["stages"]["legacy_ffa"] = dict(status="captured_unverified", record=key, source_date=day)
                except Exception as exc:
                    receipt["stages"]["legacy_ffa"] = dict(status="failed", reason=str(exc))
                provider = cfg["selected_provider"]
                day_receipts = []
                if provider is None:
                    receipt["stages"]["replacement_ffa"] = dict(status="blocked", reason="No contracted, licensed replacement feed")
                else:
                    p = cfg["providers"][provider]
                    if (p["status"] != "approved" or not p["licensed_internal_automation"] or not p["evidence"] or
                        p["annual_total_usd"] is None or not 0 <= p["annual_total_usd"] <= 1500 or p["holidays"] is None):
                        raise ValueError("provider eligibility, cost, licence or calendar is unconfirmed")
                    records = []
                    for file in sorted((store / "curves").glob("*.json")):
                        record = read_json(file)
                        if record["provider"] == provider:
                            records.append(record)
                    day_receipts = feed_days(records, cfg, root)
                    atomic_json(store / 'feed_days.json', day_receipts)
                    latest = max(records, key=lambda r: r["observed_at"])
                    validate_record(latest, cfg, root, now)
                    same = [r for r in records if r["observed_at"] == latest["observed_at"]]
                    if len({identity(r["quotes"]) for r in same}) > 1:
                        raise ValueError("unresolved conflicting replacement revision")
                    receipt["stages"]["replacement_ffa"] = dict(status="validated_shadow", record=identity(latest), source_date=latest["source_date"])
                receipt["status"] = "failed" if any(s["status"] == "failed" for s in receipt["stages"].values()) else "blocked"
                receipt["window"] = trial_window(cfg, day_receipts, now.date())
        except Exception as exc:
            receipt["status"] = "failed"
            receipt["error"] = str(exc)
        receipt["finished_at"] = datetime.now(timezone.utc).isoformat()
        atomic_json(store / "runs" / (run_id + ".json"), receipt)
        atomic_json(store / "latest.json", receipt)
        return receipt


def report(root=ROOT):
    receipt = read_json(root / STATE / "latest.json")
    lines = ["VIE exit trial: retain temporarily.", "Replacement FFA coverage and unattended operation are not yet proven.", ""]
    stage = receipt["stages"].get("documents", {})
    lines.append("Independent reports: %s pending; oldest %s; extraction failures %s." % (stage.get("pending", "unknown"), stage.get("oldest", "unknown"), stage.get("failed", "unknown")))
    for block in receipt["blockers"]:
        lines.append("- %s (%s): %s" % (block["id"], block["resolver"], block["action"]))
    for name, stage in receipt["stages"].items():
        if stage["status"] in ("failed", "blocked"):
            lines.append("- %s: %s" % (name, stage.get("reason")))
    if receipt.get("error"):
        lines.append("- Execution failure: " + receipt["error"])
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    runner = sub.add_parser("run")
    runner.add_argument("--if-due", action="store_true")
    sub.add_parser("report")
    queue = sub.add_parser("queue")
    queue.add_argument("--limit", type=int, default=10)
    imp = sub.add_parser("import-record")
    imp.add_argument("path")
    ack = sub.add_parser("ack")
    ack.add_argument("sha256")
    ack.add_argument("evidence")
    args = ap.parse_args(argv)
    if args.command == "run":
        result = run(if_due=args.if_due)
        print(report() if result["status"] != "disabled" else "VIE trial disabled")
        return 1 if result["status"] == "failed" else 0
    if args.command == "report":
        print(report())
    elif args.command == 'queue':
        if args.limit < 0:
            raise ValueError('limit must be nonnegative; zero lists all')
        print(json.dumps(pending_documents(ROOT, args.limit), indent=2))
    elif args.command == "import-record":
        record = read_json(Path(args.path))
        validate_record(record, config(ROOT), ROOT, datetime.now(timezone.utc))
        with locked(ROOT / STATE / "run.lock"):
            print(store_record(ROOT, record))
    else:
        acknowledge(ROOT, args.sha256, args.evidence)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Read-only cron sentinel (orchestration WO1 V-2, 2026-07-02).

One command that answers "does anything need the owner's eyes?" without
running the pipeline or writing anything (beyond an optional dated log line):

  python -m crude_tanker_fv.sentinel [--log state/sentinel.log]

Checks, all reusing the canonical implementations (never a second copy —
the F-13 rule):
  1. Trigger register — any §13.3 trigger DUE/overdue/FIRED
     (refresh.check_reweight_triggers; upcoming-warns are the weekly digest's
     job, not a page).
  2. Input staleness — market-data files past their per-type thresholds +
     stale watchlist vintages (refresh.check_market_data / check_watchlist_freshness).
  3. Committed-surface coherence — sign/label contradictions in the shipped
     handoff (scorecard.handoff_coherence_flags) + schema presence.
  4. Price basis — prices_daily.yaml fetch age and band-flagged quote count.
  5. Notification config (WO2 0.1) — the email channel's env vars present
     (notify.smtp_status); unconfigured means pages route nowhere.
  6. Job liveness (WO2 0.2, invariant 1) — heartbeat age/outcome per committed
     plist (cadence read from the plist: Weekday key = weekly). Heartbeats
     only, never wrapper logs — a missing/stale/errored heartbeat is the
     fetch layer failing silently (the D-2/D-3 class).

With --notify, PAGE-routed flags email the owner (notify.py) and every run
sends the daily digest — on OK days too (the unconditional send is what makes
notifier death detectable); digest tags present escalate_after consecutive
runs page ONCE; the first digest after a >48h gap carries a DARK prefix.
With --ping, the healthchecks dead-man ping fires ONLY after a completed run
whose required sends succeeded (invariant 2 — notifier death pages by absence).

Dirty-tree META-MODE (WO2 0.3, invariant 3): on a dirty tree the content
checks are suspended (they'd read half-finished surgery), but heartbeat,
digest, and ping still run — a dirty reconciliation week must not look like
death. DIRTY-TOO-LONG pages at 36h (12h inside an open earnings window).

Exit 0 = quiet. Nonzero = one status line per flag on stdout. Designed for
cron via scripts/sentinel_cron.sh (which adds the dirty-tree/PAUSE guard —
V-3: no automation through live surgery).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from .loaders import INPUTS_DIR, load_watchlist
from .refresh import (
    check_market_data,
    check_reweight_triggers,
    check_watchlist_freshness,
)
from .report import OUTPUTS_DIR
from .scorecard import handoff_coherence_flags, weight_family_basis

PRICE_FETCH_STALE_DAYS = 2   # daily cron: a fetch older than this means it missed


_PW_FV_RE = None   # compiled lazily


def _scenario_doc_pw_fv(outputs_dir: Path, ticker: str):
    """Parse the committed scenario doc's headline PW FV for the fv-identity scan."""
    import re

    global _PW_FV_RE
    if _PW_FV_RE is None:
        _PW_FV_RE = re.compile(r"Probability-weighted fair value:\*\* \$([\d,]+\.\d\d)")
    doc = outputs_dir / f"{ticker.lower()}_scenarios.md"
    if not doc.exists():
        return None
    m = _PW_FV_RE.search(doc.read_text())
    return float(m.group(1).replace(",", "")) if m else None


def collect_flags(inputs_dir: Path = INPUTS_DIR, outputs_dir: Path = OUTPUTS_DIR,
                  environ=None, pure: bool = False) -> list[str]:
    """pure=True (WO2 0.4) keeps only checks answerable from REPO CONTENT —
    what a clean clone can see: dated triggers, content-dated watchlist
    vintages, committed-surface coherence, sidecar vintage, price-basis
    disclosures. Dropped as machine-local: market-data mtimes, prices
    fetched_at age (the clone lags pushes by design — the documented Action
    caveat), notify env, heartbeats. Added: HEAD-recency inside an open
    earnings window (a dark/unpushed Mac in season blinds the backstop)."""
    import os

    if environ is None:
        environ = os.environ
    flags: list[str] = []

    # 1. Trigger register — armed-and-due/overdue, or FIRED (the Jun-17 trigger
    #    sat 15 days because nothing scheduled the check; this is the schedule).
    for it in check_reweight_triggers(inputs_dir):
        if it.status == "missing":
            flags.append(f"TRIGGER-DUE {it.label}: {it.detail}")

    # 2. Input staleness — the per-type thresholds (refresh preflight logic).
    #    mtime-based, machine-local — dropped in pure mode.
    if not pure:
        for it in check_market_data(inputs_dir):
            if it.status in ("stale", "missing"):
                flags.append(f"STALE-INPUT {it.label}: {it.detail}")
    try:
        watchlist = load_watchlist(inputs_dir)
    except Exception as exc:
        watchlist = {}
        flags.append(f"STALE-INPUT watchlist unreadable: {exc}")
    for it in check_watchlist_freshness(watchlist):
        if it.status == "stale":
            flags.append(f"STALE-INPUT watchlist {it.label}: {it.detail}")

    # 3. Committed-surface coherence — the F-13 checks against what is SHIPPED:
    #    sign/label (shared implementation) + the fv-identity between the JSON
    #    and each name's committed scenario doc.
    handoff = outputs_dir / "book_scorecard.json"
    doc = None
    if not handoff.exists():
        flags.append("SURFACE-INCOHERENT handoff missing: outputs/book_scorecard.json")
    else:
        doc = json.loads(handoff.read_text())
        if "schema_version" not in doc:
            flags.append("SURFACE-INCOHERENT handoff has no schema_version")
        for f in handoff_coherence_flags(doc):
            flags.append(f"SURFACE-INCOHERENT {f}")
        for n in doc.get("names", []):
            if n.get("void") or n.get("fv") is None:
                continue
            pw = _scenario_doc_pw_fv(outputs_dir, n["ticker"])
            if pw is not None and abs(pw - n["fv"]) > 0.011:
                flags.append(f"SURFACE-INCOHERENT {n['ticker']}: JSON fv {n['fv']} != "
                             f"scenario-doc PW FV {pw}")

    # 3b. Sidecar vintage (WO1-F4) — the §9.10 fragility sidecar must be
    #     computed against the CURRENT scenario_inputs.yaml; a lagging family
    #     means the shipped W-frag/range fields are withheld and the family
    #     scripts owe a re-run.
    fb = weight_family_basis(outputs_dir, inputs_dir)
    if fb["status"] != "current":
        flags.append(f"SIDECAR-STALE weight-family sidecar {fb['status']} vs "
                     f"scenario_inputs {fb['current_sha']} (lagging: "
                     f"{', '.join(fb['lagging']) or 'all'}) — re-run the family diagnostics")

    # 4. Price basis — static fallbacks or pending market-event reviews in the
    #    shipped handoff, plus a missed daily fetch.
    if doc is not None:
        pb = doc.get("price_basis") or {}
        for t, e in (pb.get("static_fallback") or {}).items():
            flags.append(f"PRICE-BASIS {t} on static fallback (as-of {e.get('as_of')}: "
                         f"{e.get('reason')})")
        for t, reason in (pb.get("market_event_review") or {}).items():
            flags.append(f"PRICE-BASIS {t} market-event review pending: {reason}")
    prices = inputs_dir / "market_data" / "prices_daily.yaml"
    if not prices.exists():
        flags.append("PRICE-BASIS prices_daily.yaml missing")
    elif not pure:
        import yaml

        pdoc = yaml.safe_load(prices.read_text()) or {}
        fetched = pdoc.get("fetched_at")
        if fetched:
            age = datetime.now(timezone.utc) - datetime.fromisoformat(str(fetched))
            if age.days >= PRICE_FETCH_STALE_DAYS:
                flags.append(f"PRICE-BASIS fetch is {age.days}d old ({fetched}) — cron missed?")
            # Per-ticker stuck quote (WO2 1.2, D-3): a carried-over failure or a
            # Yahoo static keeps its old asof — an asof lagging the run stamp
            # past any weekend is a quote nobody is actually fetching. Date
            # arithmetic on the date parts (asof carries an exchange offset).
            fetched_d = date.fromisoformat(str(fetched)[:10])
            for t, q in sorted((pdoc.get("prices") or {}).items()):
                asof = q.get("asof") if isinstance(q, dict) else None
                if not asof:
                    continue
                lag = (fetched_d - date.fromisoformat(str(asof)[:10])).days
                if lag > 4:
                    carried = " (carried-over failure)" if q.get("carried_over") else ""
                    flags.append(f"PRICE-BASIS {t} stuck quote: asof {str(asof)[:10]} "
                                 f"lags the {fetched_d} fetch by {lag}d{carried}")
        else:
            flags.append("PRICE-BASIS prices file carries no fetched_at")

    # Filings as events (WO2 2.3) — BOTH modes; the manifest source differs
    # (state-side locally, the tracked snapshot on the Action — pushed-state
    # lag is the documented caveat).
    flags += _filing_event_flags(inputs_dir, watchlist,
                                 _edgar_manifest_entries(inputs_dir, pure))

    if pure:
        # Pure-only: HEAD recency in an open earnings window. The Action reads
        # pushed state; a Mac dark or unpushed for days IN SEASON means the
        # backstop is watching a stale world — say so on the backstop itself.
        if _in_earnings_window(inputs_dir):
            import subprocess

            out = subprocess.run(["git", "-C", str(inputs_dir.parent), "log", "-1",
                                  "--format=%ct"], capture_output=True, text=True)
            if out.returncode == 0 and out.stdout.strip():
                head_age = (datetime.now(timezone.utc) - datetime.fromtimestamp(
                    int(out.stdout.strip()), tz=timezone.utc)).days
                if head_age >= 3:
                    flags.append(f"STALE-INPUT repo HEAD {head_age}d old inside an "
                                 "open earnings window — Mac dark or unpushed; this "
                                 "backstop only sees pushed state")
        return flags

    # 5. Notification config (WO2 0.1) — a page that routes nowhere is the
    #    watcher being inaudible; nags daily until the env file carries creds.
    from .notify import smtp_status

    st = smtp_status(environ)
    if not st["configured"]:
        flags.append("NOTIFY-UNCONFIGURED email channel missing env: "
                     f"{', '.join(st['missing'])} (~/.config/crude-tanker-fv.env; "
                     "run notify --doctor)")

    # 6. Job liveness (WO2 0.2) — every committed plist's job must have a
    #    fresh, non-errored heartbeat. Cadence from the plist itself (one
    #    source of truth); daily jobs get 2d, weekly 9d (coalesced-wake slack).
    import plistlib

    hb_dir = inputs_dir.parent / "state" / "heartbeat"
    now = datetime.now(timezone.utc)
    for plist in sorted((inputs_dir.parent / "scripts").glob("com.crude-tanker-fv.*.plist")):
        pdoc = plistlib.loads(plist.read_bytes())
        job = pdoc["Label"].replace("com.crude-tanker-fv.", "")
        limit = 9 if "Weekday" in (pdoc.get("StartCalendarInterval") or {}) else 2
        hb = hb_dir / job
        if not hb.exists():
            flags.append(f"FETCH-FAILED {job}: no heartbeat — job has never run "
                         "(launchd job not installed, or heartbeats just landed)")
            continue
        age = (now - datetime.fromtimestamp(hb.stat().st_mtime, tz=timezone.utc)).days
        if age >= limit:
            flags.append(f"FETCH-FAILED {job}: heartbeat {age}d old "
                         f"(cadence limit {limit}d) — launchd stopped firing?")
        elif "outcome=error" in hb.read_text():
            flags.append(f"FETCH-FAILED {job}: last run errored "
                         f"({hb.read_text().strip()})")

    # 7. UNINGESTED-PRINTS (WO2 1.2) — staged material more than 7d newer than
    #    a determinant's last deliberate refresh EVENT (as_of.default). Held
    #    classes are excluded by construction: they live in as_of overrides
    #    and are tracked by their own named trigger, not this lane.
    pareto_newest = _newest_dated_file(inputs_dir / "research_pareto")
    if pareto_newest:
        for fname in ("spot_tce.yaml", "twelve_month_tc.yaml"):
            a = _as_of_default(inputs_dir, fname)
            if a and (pareto_newest - a).days > 7:
                flags.append(f"UNINGESTED-PRINTS {fname}: Pareto dailies staged through "
                             f"{pareto_newest} vs as_of {a} ({(pareto_newest - a).days}d) "
                             "— promote from the newest daily or annotate the hold")
    curves = inputs_dir.parent / "state" / "ffa_ocr_curves.json"
    if curves.exists():
        import re as _re

        dates = [k for k in json.loads(curves.read_text() or "{}")
                 if _re.match(r"\d{4}-\d{2}-\d{2}$", str(k))]
        a = _as_of_default(inputs_dir, "ffa_forward_curve.yaml")
        if dates and a:
            ocr_newest = date.fromisoformat(max(dates))
            if (ocr_newest - a).days > 7:
                flags.append(f"UNINGESTED-PRINTS ffa_forward_curve.yaml: OCR widget "
                             f"parsed {ocr_newest} vs as_of {a} "
                             f"({(ocr_newest - a).days}d) — review outputs/ffa_ocr_queue.md")

    # 8. Source-silence (WO2 1.2) — per-source cadence from rocketchat_sources
    #    (the mtime file check can't see WHICH feed went quiet; this reads the
    #    staged artifacts themselves).
    rc_cfg = inputs_dir / "rocketchat_sources.yaml"
    if rc_cfg.exists():
        import yaml

        today = date.today()
        for s in (yaml.safe_load(rc_cfg.read_text()) or {}).get("sources", []):
            if "expect_cadence" not in s:
                continue
            if s.get("dest_dir"):
                newest = _newest_dated_file(inputs_dir.parent / s["dest_dir"])
            else:
                newest = _newest_csv_date(inputs_dir.parent / s["dest_file"])
            who = " — single-sender feed, check the channel" if s.get("single_sender") else ""
            if newest is None:
                flags.append(f"STALE-INPUT {s['name']}: no staged artifacts at all{who}")
                continue
            silence = s.get("silence_days")
            if silence is not None:
                if (today - newest).days > silence:
                    flags.append(f"STALE-INPUT {s['name']}: newest artifact {newest}, "
                                 f"{(today - newest).days}d silent (limit {silence}d){who}")
            elif s["expect_cadence"] == "business-daily":
                bd = _business_days_between(newest, today)
                if bd > 2:
                    flags.append(f"STALE-INPUT {s['name']}: newest artifact {newest}, "
                                 f"{bd} business days silent (limit 2){who}")
            elif (today - newest).days > (10 if s["expect_cadence"] == "weekly" else 3):
                flags.append(f"STALE-INPUT {s['name']}: newest artifact {newest} "
                             f"({(today - newest).days}d, cadence {s['expect_cadence']}){who}")

    # Harvester lanes (WO2 1.3) — mirror silence (10d incl mirror latency) +
    # the marks trail: broker weeklies staged newer than the newest PROMOTED
    # transaction print by >7d means S&P sections are sitting untriaged.
    manifest = inputs_dir.parent / "shipping_harvester" / "data" / "manifest.jsonl"
    if manifest.exists():
        pubs = []
        for line in manifest.read_text().splitlines():
            try:
                p = json.loads(line).get("published")
            except Exception:
                continue
            if p:
                pubs.append(date.fromisoformat(str(p)[:10]))
        if pubs:
            newest_issue = max(pubs)
            silent = (date.today() - newest_issue).days
            if silent > 10:
                flags.append(f"STALE-INPUT harvester: newest broker issue {newest_issue} "
                             f"({silent}d; limit 10d incl mirror latency) — crawl "
                             "missing or mirrors dry")
            tx_newest = None
            tx_dir = inputs_dir / "market_data" / "transactions"
            if tx_dir.exists():
                import yaml

                for f in sorted(tx_dir.glob("[a-z]*.yaml")):
                    if f.name == "_template.yaml":
                        continue
                    for val in (yaml.safe_load(f.read_text()) or {}).values():
                        if isinstance(val, list):
                            for p in val:
                                if isinstance(p, dict) and p.get("date"):
                                    d = date.fromisoformat(str(p["date"])[:10])
                                    if tx_newest is None or d > tx_newest:
                                        tx_newest = d
            if tx_newest and (newest_issue - tx_newest).days > 7:
                flags.append(f"UNINGESTED-PRINTS marks-trail: broker issues staged "
                             f"through {newest_issue} vs newest promoted print "
                             f"{tx_newest} ({(newest_issue - tx_newest).days}d) — "
                             "triage the weeklies or record why nothing promotes")

    # 9. TRIGGER-EVIDENCE (WO2 1.4) — tanker period-market signals scanned
    #    from the dailies while a tanker forward hold is in place: evidence
    #    FOR the armed tanker_forward_print_lands trigger. Flag-only; the
    #    owner works the register (automation never writes it). Auto-clears
    #    when the hold resolves (no tanker as_of overrides left).
    TANKER_CLASSES = {"VLCC", "Suezmax", "Aframax", "LR1", "LR2", "MR",
                      "Handysize", "Handymax", "LR1_clean", "LR2_clean"}
    scan_state = inputs_dir / "market_data" / "transactions" / "_scan_state.json"
    ffa_file = inputs_dir / "market_data" / "ffa_forward_curve.yaml"
    if scan_state.exists() and ffa_file.exists():
        import yaml

        a = (yaml.safe_load(ffa_file.read_text()) or {}).get("as_of") or {}
        tanker_holds = [v for k, v in a.items() if k in TANKER_CLASSES]
        hits = ((json.loads(scan_state.read_text()).get("tanker_period_signals")
                 or {}).get("hits") or [])
        if tanker_holds and hits:
            hold = min(tanker_holds)
            fresh = [h for h in hits if h.get("date")
                     and date.fromisoformat(str(h["date"])[:10]) > hold]
            if fresh:
                newest_hit = max(str(h["date"])[:10] for h in fresh)
                flags.append(f"TRIGGER-EVIDENCE tanker_forward_print_lands: "
                             f"{len(fresh)} period-market signal(s) in the dailies "
                             f"since the {hold} hold (newest {newest_hit}) — review "
                             "outputs/sp_print_candidates.md §Tanker period-market signals")

    # 10. FLEET-TRANSACTION (WO2 3.2) — S&P candidates scanned since the last
    #     --mark-reviewed ack; the review queue must not silently accumulate.
    if scan_state.exists():
        sdoc = json.loads(scan_state.read_text())
        total = sdoc.get("candidates_cumulative")
        if total is not None:
            unreviewed = total - sdoc.get("candidates_reviewed", 0)
            if unreviewed > 0:
                flags.append(f"FLEET-TRANSACTION {unreviewed} unreviewed S&P print "
                             "candidate(s) — review outputs/sp_print_candidates.md, "
                             "promote/dismiss, then sp_scan --mark-reviewed")

    # 11. MB weekly lanes (WO2 1.6 — landed AFTER the Apr-01 instance was
    #     fixed, per R-6: these exist to make the NEXT freeze impossible).
    #     Per-feed source silence + the container UNINGESTED lane: containers
    #     are the one class whose SOURCE OF RECORD is the MB weekly (§11.8).
    mb_root = inputs_dir / "research_mb"
    if mb_root.exists():
        today = date.today()
        for feed in ("container_weekly", "tanker_weekly",
                     "dry_bulk_weekly", "lng_weekly"):
            newest = _newest_dated_file(mb_root / feed)
            if newest is None:
                flags.append(f"STALE-INPUT mb:{feed}: no staged weeklies at all "
                             "— run the Saturday Gmail step (session:mb-batch)")
            elif (today - newest).days > 10:
                flags.append(f"STALE-INPUT mb:{feed}: newest {newest} "
                             f"({(today - newest).days}d; weekly cadence, 10d "
                             "grace incl the Gmail session step)")
        cw_newest = _newest_dated_file(mb_root / "container_weekly")
        tc_file = inputs_dir / "market_data" / "twelve_month_tc.yaml"
        if cw_newest and tc_file.exists():
            import yaml

            a = (yaml.safe_load(tc_file.read_text()) or {}).get("as_of") or {}
            if isinstance(a, dict) and a.get("default"):
                ctr_vintage = min(a.get(c, a["default"]) for c in
                                  ("Ctr-Feeder", "Ctr-Intermediate", "Ctr-Large"))
                if (cw_newest - ctr_vintage).days > 7:
                    flags.append(f"UNINGESTED-PRINTS containers: MB weekly staged "
                                 f"{cw_newest} vs Ctr vintage {ctr_vintage} "
                                 f"({(cw_newest - ctr_vintage).days}d) — the §11.8 "
                                 "source of record has a fresher assessment set; "
                                 "work trigger container_mb_refresh")
    return flags


def _tree_dirty(root: Path) -> bool:
    """git-porcelain dirtiness of the project tree, IGNORING dirt confined to
    the automation-drift list (scripts/drift_files.txt — the daily RC ingest
    writes tracked files every morning; drift-only dirt is routine, not
    surgery, and must not put the sentinel in META-MODE all week — live
    lesson 2026-07-04/05). Not-a-repo reads as clean; no drift list means
    ALL dirt counts (safe default for bare checkouts)."""
    import subprocess

    out = subprocess.run(["git", "-C", str(root), "status", "--porcelain"],
                         capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        return False
    drift_list = root / "scripts" / "drift_files.txt"
    drift = set()
    if drift_list.exists():
        drift = {ln.strip() for ln in drift_list.read_text().splitlines()
                 if ln.strip() and not ln.startswith("#")}
    for line in out.stdout.splitlines():
        if line[3:] not in drift:
            return True
    return False


def _in_earnings_window(inputs_dir: Path) -> bool:
    """True when any name's reporting window (start−1d .. end+3d, the overdue
    tail) spans today — tightens DIRTY-TOO-LONG to 12h and promotes
    FETCH-FAILED to a page: a blind fetch layer in season is an incident."""
    from .refresh import load_earnings_calendar

    _, names = load_earnings_calendar(inputs_dir)
    today = date.today()
    for v in names.values():
        if not isinstance(v, dict) or "window_start" not in v:
            continue
        end = v.get("window_end") or v["window_start"]
        if v["window_start"] - timedelta(days=1) <= today <= end + timedelta(days=3):
            return True
    return False


def _as_of_default(inputs_dir: Path, filename: str):
    """The `as_of.default` of a market-data file (WO2 1.2) — the date of its
    last deliberate refresh EVENT. None when the file carries no as_of block
    (legacy fixtures, other files) — lanes stay silent rather than guess."""
    import yaml

    path = inputs_dir / "market_data" / filename
    if not path.exists():
        return None
    doc = yaml.safe_load(path.read_text()) or {}
    a = doc.get("as_of")
    return a.get("default") if isinstance(a, dict) else None


def _newest_dated_file(root: Path):
    """Newest ISO-date filename prefix under a staging tree, at any depth."""
    import re

    best = None
    if not root.exists():
        return None
    for p in root.rglob("*"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", p.name)
        if m:
            d = date.fromisoformat(m.group(1))
            if best is None or d > best:
                best = d
    return best


def _newest_csv_date(path: Path):
    """Max value of a leading ISO-date column in a date-keyed CSV."""
    if not path.exists():
        return None
    best = None
    for line in path.read_text().splitlines()[1:]:
        head = line.split(",", 1)[0]
        try:
            d = date.fromisoformat(head)
        except ValueError:
            continue
        if best is None or d > best:
            best = d
    return best


def _business_days_between(a: date, b: date) -> int:
    n, d = 0, a
    while d < b:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def _edgar_manifest_entries(inputs_dir: Path, pure: bool) -> list:
    """Arrival records: the state-side jsonl locally (authoritative, R-2);
    the tracked snapshot (commit_drift promotes it) for --pure / fallback."""
    if not pure:
        state_side = inputs_dir.parent / "state" / "edgar_manifest.jsonl"
        if state_side.exists():
            out = []
            for line in state_side.read_text().splitlines():
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
            return out
    snapshot = inputs_dir / "filings" / "_manifest.json"
    if snapshot.exists():
        try:
            return json.loads(snapshot.read_text())
        except Exception:
            return []
    return []


def _filing_event_flags(inputs_dir: Path, watchlist: dict,
                        manifest_entries: list, now=None) -> list[str]:
    """WO2 2.3 — filings as events, shared by both sentinel modes.

    FILING-LANDED (page): manifest arrivals in the last 48h (+AMENDED marker).
    STALE-BALANCE-SHEET / EARNINGS-DUE / CALENDAR-UNSEEDED (digest): the ONE
    canonical calendar implementation (refresh.check_earnings_calendar) — the
    F-13 rule, never a second copy.
    FILING-OVERDUE (page): window_end + 3 business days passed, nothing
    arrived, no balance sheet on file — also the Oslo trio's net (no EDGAR
    poller; self-clears when the reconciliation lands the balance sheet).
    """
    from .refresh import check_earnings_calendar, load_earnings_calendar

    flags: list[str] = []
    now = now or datetime.now(timezone.utc)
    for e in manifest_entries:
        try:
            ts = datetime.fromisoformat(str(e.get("ts")))
        except Exception:
            continue
        if (now - ts).total_seconds() <= 48 * 3600:
            am = " AMENDED" if e.get("amended") else ""
            flags.append(f"FILING-LANDED {e.get('ticker')}: {e.get('form')}{am} "
                         f"{e.get('accession')} filed {e.get('filed')} -> "
                         f"{e.get('staged_path') or 'manifest-only'}")

    meta, cal = load_earnings_calendar(inputs_dir)
    if not cal or not watchlist:
        return flags
    quarter = meta.get("quarter")
    today = now.date()

    # Quarter rollover (WO2 2.1): a calendar still on last season's quarter
    # ~3.5 months after that quarter ended is an unseeded NEXT season.
    if quarter:
        import re as _re

        m = _re.match(r"(\d{4})-Q([1-4])", str(quarter))
        if m:
            q_end = date(int(m.group(1)), int(m.group(2)) * 3, 1) + timedelta(days=31)
            q_end = q_end.replace(day=1) - timedelta(days=1)
            if today > q_end + timedelta(days=105):
                flags.append(f"CALENDAR-UNSEEDED (meta): calendar still on {quarter} "
                             f"(quarter ended {q_end}) — seed the next season's windows")
    for it in check_earnings_calendar(quarter, watchlist, inputs_dir, today=today):
        if it.status == "missing":
            flags.append(f"STALE-BALANCE-SHEET {it.label}: {it.detail}")
        elif it.status == "warn":
            tag = ("CALENDAR-UNSEEDED" if "no earnings date on file" in it.detail
                   else "EARNINGS-DUE")
            flags.append(f"{tag} {it.label}: {it.detail}")

    by_ticker: dict = {}
    for e in manifest_entries:
        by_ticker.setdefault(e.get("ticker"), []).append(e)
    for ticker, entry in cal.items():
        if not isinstance(entry, dict) or "window_start" not in entry:
            continue
        end = entry.get("window_end") or entry["window_start"]
        deadline, n = end, 0
        while n < 3:
            deadline += timedelta(days=1)
            if deadline.weekday() < 5:
                n += 1
        if today <= deadline:
            continue
        bs = inputs_dir / "balance_sheets" / f"{ticker.lower()}_{quarter}.yaml"
        if bs.exists():
            continue
        start = entry["window_start"]
        arrived = any(str(e.get("filed", "")) >= start.isoformat()
                      for e in by_ticker.get(ticker, []))
        if not arrived:
            flags.append(f"FILING-OVERDUE {ticker}: window ended {end}, +3bd "
                         f"passed, no filing arrival and no {quarter} balance "
                         "sheet — check the wire (Oslo names have no EDGAR "
                         "poller; this IS their net)")
    return flags


def _load_state(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def _save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=1))
    tmp.replace(path)   # invariant 10: temp+rename, never a half-written cursor


_urlopen = None   # stdlib bound lazily; module attr so tests can stub it


def _ping(sends_ok: bool) -> None:
    """Invariant 2: the dead-man ping asserts 'checks ran AND pages reached
    the owner' — withheld on a failed send so healthchecks pages by absence
    (its own channel; the recursion stops there)."""
    import os
    import urllib.request

    global _urlopen
    if _urlopen is None:
        _urlopen = urllib.request.urlopen
    url = os.environ.get("CRUDE_FV_HEALTHCHECK_URL")
    if not url:
        print("PING-SKIPPED: CRUDE_FV_HEALTHCHECK_URL unset")
        return
    if not sends_ok:
        print("PING-WITHHELD: a required send failed — healthchecks will page")
        return
    try:
        _urlopen(url, timeout=10)
        print("PING-SENT")
    except Exception as exc:
        print(f"PING-FAILED: {exc} — healthchecks will page by absence")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="read-only owner-attention sentinel")
    ap.add_argument("--log", type=Path, default=None,
                    help="append one dated status line to this file")
    ap.add_argument("--notify", action="store_true",
                    help="email PAGE-routed flags + the unconditional daily digest")
    ap.add_argument("--ping", action="store_true",
                    help="fire the healthchecks dead-man ping if the run completed "
                         "and required sends succeeded (invariant 2)")
    ap.add_argument("--state", type=Path, default=Path("state/sentinel_state.json"),
                    help="run-over-run state (digest streaks, dark gap, dirty-since)")
    ap.add_argument("--pure", action="store_true",
                    help="repo-content checks only (the GitHub Action's clean-clone "
                         "mode); no state, no meta-mode, no machine-local checks")
    args = ap.parse_args(argv)

    now = datetime.now(timezone.utc)
    state = _load_state(args.state)
    in_window = _in_earnings_window(INPUTS_DIR)

    meta_note = None
    dirty_since = None
    if args.pure:
        flags = collect_flags(INPUTS_DIR, OUTPUTS_DIR, pure=True)
    elif _tree_dirty(INPUTS_DIR.parent):
        # META-MODE (invariant 3): content checks read half-finished surgery —
        # suspend them; liveness (heartbeat/digest/ping) must keep running.
        dirty_since = state.get("dirty_since") or now.isoformat()
        hours = (now - datetime.fromisoformat(dirty_since)).total_seconds() / 3600
        limit = 12 if in_window else 36
        flags = []
        if hours >= limit:
            flags.append(f"DIRTY-TOO-LONG tree dirty {hours:.0f}h (limit {limit}h"
                         f"{', earnings window open' if in_window else ''}) — content "
                         "checks suspended all this time; finish the surgery or PAUSE")
        meta_note = (f"META dirty-tree: content checks suspended "
                     f"(dirty since {dirty_since}, {hours:.0f}h)")
        print(meta_note)
    else:
        flags = collect_flags(INPUTS_DIR, OUTPUTS_DIR)   # module-attr lookup at call time (testable)
    for f in flags:
        print(f)
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        stamp = now.isoformat(timespec="seconds")
        mode = " META-DIRTY" if meta_note else ""
        with args.log.open("a") as fh:
            if flags:
                fh.write(f"{stamp}{mode} FLAG {len(flags)}: " + " | ".join(flags) + "\n")
            else:
                fh.write(f"{stamp}{mode} OK\n")

    sends_ok = True
    if args.notify:
        from . import notify

        routes = notify.load_routes(INPUTS_DIR)
        page, digest = notify.route_flags(flags, routes)
        if in_window and any(f.startswith("FETCH-FAILED") for f in digest):
            # A blind fetch layer in reporting season is an incident, not a digest line.
            page += [f for f in digest if f.startswith("FETCH-FAILED")]
            digest = [f for f in digest if not f.startswith("FETCH-FAILED")]
        prefix = routes["subject_prefix"]
        if page:
            body = "PAGE-class flags:\n" + "\n".join(f"  {f}" for f in page)
            if digest:
                body += ("\n\nDigest-class also present (detail rides the daily "
                         "digest):\n" + "\n".join(f"  {f}" for f in digest))
            sends_ok = notify.send_email(f"{prefix} PAGE: {len(page)} flag(s)", body)

        # Digest-streak escalation (0.3): a tag present escalate_after
        # consecutive runs pages ONCE, then stays escalated until it clears.
        streaks_prev = state.get("streaks") or {}
        escalated = set(state.get("escalated") or [])
        present = {f.split()[0] for f in digest}
        streaks = {t: streaks_prev.get(t, 0) + 1 for t in present}
        escalated &= present   # a cleared tag may escalate again after a new streak
        overrides = routes.get("escalate_after_overrides") or {}
        n_default = routes.get("escalate_after", 3)
        due = sorted(t for t in present
                     if streaks[t] >= overrides.get(t, n_default) and t not in escalated)
        if due:
            body = ("Digest-class tags at their consecutive-run limit "
                    "(one-time escalation):\n" +
                    "\n".join(f"  {f}" for f in digest if f.split()[0] in due))
            if not notify.send_email(f"{prefix} PAGE (escalated): {', '.join(due)}", body):
                sends_ok = False
            escalated |= set(due)

        # The unconditional daily digest — sent on OK days too. First run after
        # a >48h gap carries the DARK prefix (the machine slept; say so).
        dark_days = 0
        if state.get("last_run"):
            gap_h = (now - datetime.fromisoformat(state["last_run"])).total_seconds() / 3600
            if gap_h > 48:
                dark_days = int(gap_h // 24)
        lines = []
        if dark_days:
            lines.append(f"DARK {dark_days} days — accumulated:")
        if meta_note:
            lines.append(meta_note)
        lines += [f"  {f}" for f in flags] if flags else ["All checks quiet."]
        subject = (f"{prefix} daily digest — "
                   + (f"DARK {dark_days}d — " if dark_days else "")
                   + (f"{len(flags)} flag(s)" if flags else "OK"))
        if not notify.send_email(subject, "\n".join(lines)):
            sends_ok = False
        _save_state(args.state, {"last_run": now.isoformat(), "streaks": streaks,
                                 "escalated": sorted(escalated),
                                 "dirty_since": dirty_since})
    if args.ping:
        _ping(sends_ok)
    return 1 if flags else 0


if __name__ == "__main__":
    sys.exit(main())

"""The owner's weekly report — one email that replaces reading the daily digest.

    python -m crude_tanker_fv.weekly_report            # write outputs/weekly_report_<date>.md
    python -m crude_tanker_fv.weekly_report --send     # ...and email it (notify.py channel)
    python -m crude_tanker_fv.weekly_report --stdout   # print it, write nothing

Answers, in the order the owner reads them: what moved in the book, what needs a word,
whether the machine is alive, and what lands in the next fortnight. Every number is DERIVED
from a committed surface or machine state — nothing here is hand-written prose that can go
stale silently (the F-8 rule, audit 2026-07-02).

Sources, all read-only:
  outputs/book_scorecard.json   the decision surface, diffed against its own git history
  outputs/book_scorecard.md     the generated edge-cleared sentence (the 4-conjunct truth)
  RATIFY_LOG.md                 baseline re-anchors since the last report
  state/heartbeat/*             per-job liveness (the sentinel's own check 6 source)
  state/ping_status.json        dead-man ping outcome (Stage 0)
  state/reauth/*.json           credential surfaces needing renewal (Stage 0)
  state/automation_runs.log     fetch initiators + skip streaks
  state/notify_sent.log         what actually reached the owner
  inputs/earnings_calendar.yaml + inputs/reweight_triggers.yaml   the 14-day calendar
  outputs/sp_print_candidates.md + outputs/ffa_ocr_queue.md       the promotion queues
  sentinel.collect_flags        today's flags, summarised by tag

This module NEVER writes governed state: one report file, and only from `main()` (the
production entry — the 2026-07-18/08-14 shared-state doctrine).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUTPUTS = ROOT / "outputs"
STATE = ROOT / "state"
INPUTS = ROOT / "inputs"
SCORECARD_JSON = "outputs/book_scorecard.json"

# A move worth a line in section 1. Deliberately the drift gate's own thresholds so the
# report and the gate never disagree about what "moved" means.
NAV_MOVE_PCT = 2.0
EV_MOVE_PP = 2.0


def _git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout
    except Exception:
        return ""


def _scorecard_at(rev: str) -> dict | None:
    raw = _git("show", f"{rev}:{SCORECARD_JSON}")
    try:
        return json.loads(raw) if raw.strip() else None
    except Exception:
        return None


def _prior_revision(days: int = 7) -> tuple[str, str] | None:
    """(sha, date) of the newest scorecard commit at or before `days` ago."""
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    out = _git("log", "-1", f"--before={cutoff}T23:59:59", "--format=%h %ad",
               "--date=short", "--", SCORECARD_JSON).strip()
    if not out:
        return None
    sha, _, when = out.partition(" ")
    return sha, when.strip()


def _rows(doc: dict) -> dict[str, dict]:
    return {r["ticker"]: r for r in (doc.get("names") or [])}


def _edge_cleared_from_md(md_path: Path, known: set | None = None) -> tuple[list[str], str] | None:
    """The edge-cleared long set as the SCORECARD computed it (all four conjuncts).

    scorecard.py derives this sentence from the rows; the committed JSON (schema 2.8)
    carries no `read_par`, so the JSON alone cannot reproduce the parity conjunct. Parse
    the generated sentence rather than approximate it — and `_edge_cleared_crosscheck`
    below says so out loud when the 3-conjunct approximation disagrees.
    """
    if not md_path.exists():
        return None
    m = re.search(r"validated-and-actionable-long surface is \*\*(\d+)\s*\(([^)]*)\)\*\*",
                  md_path.read_text())
    if not m:
        m2 = re.search(r"validated-and-actionable-long surface is \*\*(\d+)\*\*", md_path.read_text())
        return ([], "none") if m2 and m2.group(1) == "0" else None
    inner = m.group(2)
    # Intersect with the book's real tickers: the sentence carries prose ("cheap on both
    # NAV bases") whose capitalised words otherwise read as tickers.
    names = [t for t in re.findall(r"\b([A-Z]{2,5}|\d{4})\b", inner)
             if known is None or t in known]
    return names, inner


def _edge_cleared_approx(rows: dict[str, dict]) -> list[str]:
    """Three of the four conjuncts (the JSON has no read_par). Cross-check only."""
    return sorted(t for t, r in rows.items()
                  if r.get("confidence_tier") == "VALIDATED-TIGHT"
                  and r.get("read_flag") == "robust"
                  and str(r.get("position", "")).startswith("BUY"))


@dataclass
class Move:
    ticker: str
    kind: str
    detail: str


def _book_moves(now: dict[str, dict], prior: dict[str, dict]) -> list[Move]:
    moves: list[Move] = []
    for t, r in sorted(now.items()):
        p = prior.get(t)
        if p is None:
            moves.append(Move(t, "NEW", f"entered the book at {r.get('position')}"))
            continue
        if r.get("position") != p.get("position"):
            moves.append(Move(t, "BAND", f"{p.get('position')} → {r.get('position')}"))
        if r.get("confidence_tier") != p.get("confidence_tier"):
            moves.append(Move(t, "TIER", f"{p.get('confidence_tier')} → {r.get('confidence_tier')}"))
        if r.get("read_flag") != p.get("read_flag"):
            moves.append(Move(t, "READ", f"read_flag {p.get('read_flag')} → {r.get('read_flag')}"))
        nav_now, nav_was = r.get("nav_per_share"), p.get("nav_per_share")
        if nav_now and nav_was:
            d = (nav_now / nav_was - 1.0) * 100.0
            if abs(d) >= NAV_MOVE_PCT:
                moves.append(Move(t, "NAV", f"{nav_was:.2f} → {nav_now:.2f} ({d:+.1f}%)"))
        ev_now, ev_was = r.get("ev_pct"), p.get("ev_pct")
        if ev_now is not None and ev_was is not None and abs(ev_now - ev_was) >= EV_MOVE_PP:
            moves.append(Move(t, "EV", f"{ev_was:+.1f}% → {ev_now:+.1f}% ({ev_now - ev_was:+.1f}pp)"))
    for t in sorted(set(prior) - set(now)):
        moves.append(Move(t, "GONE", "left the book"))
    return moves


def _cadence_limit_hours(plist: Path) -> float:
    """Staleness limit from the plist's OWN schedule — the sentinel's check-6 rule.

    A weekly job (StartCalendarInterval carries a Weekday key) is not late at 96h; judging
    every job on a daily limit is exactly the false alarm this report exists to remove.
    """
    try:
        import plistlib
        doc = plistlib.loads(plist.read_bytes())
    except Exception:
        return 48.0
    cal = doc.get("StartCalendarInterval") or {}
    if isinstance(cal, list):
        cal = cal[0] if cal else {}
    if "Weekday" in cal:
        return 9 * 24.0
    if "Hour" not in cal:          # hourly (Minute only)
        return 6.0
    return 48.0


def _heartbeats() -> list[tuple[str, str, str, float | None, bool]]:
    """(job, outcome, ts, age_hours, late) per committed plist, cadence-aware."""
    out = []
    scripts = ROOT / "scripts"
    plists = sorted(scripts.glob("com.crude-tanker-fv.*.plist"))
    now = datetime.now(timezone.utc)
    for pl in plists:
        job = pl.stem.replace("com.crude-tanker-fv.", "")
        limit = _cadence_limit_hours(pl)
        hb = STATE / "heartbeat" / job
        if not hb.exists():
            out.append((job, "NO HEARTBEAT", "—", None, True))
            continue
        fields = dict(kv.split("=", 1) for kv in hb.read_text().strip().split() if "=" in kv)
        ts = fields.get("ts", "")
        age = None
        try:
            age = (now - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() / 3600
        except Exception:
            pass
        outcome = fields.get("outcome", "?")
        late = outcome == "error" or (age is not None and age > limit)
        out.append((job, outcome, ts, age, late))
    return out


def _reauth() -> list[dict]:
    d = STATE / "reauth"
    out = []
    if d.exists():
        for p in sorted(d.glob("*.json")):
            try:
                out.append(json.loads(p.read_text()))
            except Exception:
                out.append({"surface": p.stem, "reason": "unreadable register file"})
    return out


def _ping_status() -> dict | None:
    p = STATE / "ping_status.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def _ratifies_since(when: str) -> list[str]:
    log = ROOT / "RATIFY_LOG.md"
    if not log.exists():
        return []
    rows = []
    for line in log.read_text().splitlines():
        if not line.startswith("| 20"):
            continue
        stamp = line.split("|")[1].strip()
        if stamp[:10] >= when:
            cells = [c.strip() for c in line.split("|")]
            rows.append(f"{stamp[:10]} — {cells[3][:150] if len(cells) > 3 else ''}")
    return rows


def _sends_since(when: str) -> tuple[int, int, str | None]:
    """(pages, digests, last_send_ts) from the notify ledger."""
    p = STATE / "notify_sent.log"
    if not p.exists():
        return 0, 0, None
    pages = digests = 0
    last = None
    for line in p.read_text().splitlines():
        if not line[:10] >= when:
            continue
        last = line.split()[0]
        if " PAGE" in line:
            pages += 1
        elif "digest" in line:
            digests += 1
    return pages, digests, last


def _calendar(days: int = 14) -> list[tuple[str, str]]:
    today = date.today()
    horizon = today + timedelta(days=days)
    items: list[tuple[str, str]] = []
    cal_path = INPUTS / "earnings_calendar.yaml"
    if cal_path.exists():
        doc = yaml.safe_load(cal_path.read_text()) or {}
        for t, e in (doc.get("names") or {}).items():
            if not isinstance(e, dict) or "window_start" not in e:
                continue
            ws = e["window_start"]
            ws = ws if isinstance(ws, date) else date.fromisoformat(str(ws))
            if today <= ws <= horizon:
                items.append((ws.isoformat(), f"{t} reports ({e.get('status', '?')})"))
    trig = INPUTS / "reweight_triggers.yaml"
    if trig.exists():
        for name, card in (yaml.safe_load(trig.read_text()) or {}).items():
            if not isinstance(card, dict):
                continue
            due = card.get("due")
            if not due:
                continue
            due = due if isinstance(due, date) else date.fromisoformat(str(due))
            if due <= horizon:
                tag = "OVERDUE" if due < today else "due"
                items.append((due.isoformat(), f"trigger {name} {tag}"))
    return sorted(items)


def _queue_lines(flags: list[str]) -> list[str]:
    """What needs an owner word, derived from live flags + the promotion queues."""
    out: list[str] = []
    for f in flags:
        tag = f.split()[0]
        if tag in ("TRIGGER-DUE", "REAUTH-NEEDED", "SURFACE-INCOHERENT", "FILING-OVERDUE"):
            out.append(f"{tag} — {f.split(':', 1)[-1].strip()[:180]}")
    fleet = [f for f in flags if f.startswith("FLEET-TRANSACTION")]
    if fleet:
        n = re.search(r"(\d+)", fleet[0])
        out.append(f"S&P queue — {n.group(1) if n else 'some'} unreviewed print candidate(s): "
                   "promote or dismiss, then `sp_scan --mark-reviewed`")
    ffa = [f for f in flags if f.startswith("UNINGESTED-PRINTS ffa")]
    if ffa:
        out.append("FFA queue — a parsed widget is newer than the committed curve vintage "
                   "(review outputs/ffa_ocr_queue.md)")
    stale = [f for f in flags if f.startswith("STALE-BALANCE-SHEET")]
    for f in stale:
        out.append(f"Refresh owed — {f.split(' ', 1)[1].split(':')[0]} reported and has no "
                   f"balance sheet on file")
    return out


def build_report(today: date | None = None, days: int = 7) -> str:
    today = today or date.today()
    since_rev = _prior_revision(days)
    now_doc = json.loads((ROOT / SCORECARD_JSON).read_text()) if (ROOT / SCORECARD_JSON).exists() else {}
    now_rows = _rows(now_doc)
    prior_rows: dict[str, dict] = {}
    prior_label = "no prior scorecard commit found"
    if since_rev:
        sha, when = since_rev
        prior = _scorecard_at(sha)
        if prior:
            prior_rows = _rows(prior)
            prior_label = f"{when} ({sha})"
    since_date = (today - timedelta(days=days)).isoformat()

    from .sentinel import collect_flags
    try:
        flags = collect_flags()
    except Exception as exc:                     # a broken input must not kill the report
        flags = [f"SURFACE-INCOHERENT the sentinel could not run: {exc}"]

    moves = _book_moves(now_rows, prior_rows) if prior_rows else []
    edge = _edge_cleared_from_md(OUTPUTS / "book_scorecard.md", known=set(now_rows))
    edge_names = edge[0] if edge else []
    approx = _edge_cleared_approx(now_rows)
    queue = _queue_lines(flags)
    hbs = _heartbeats()
    reauth = _reauth()
    ping = _ping_status()
    pages, digests, last_send = _sends_since(since_date)
    ratifies = _ratifies_since(since_date)
    cal = _calendar()
    dirty = [ln for ln in _git("status", "--porcelain").splitlines() if ln.strip()]
    unpushed = len([ln for ln in _git("log", "--oneline", "origin/main..HEAD").splitlines() if ln.strip()])

    dead = [j for j, _o, _ts, _age, late in hbs if late]
    verdict = (f"{len(queue)} owed · {len(edge_names)} long{'s' if len(edge_names) != 1 else ''} · "
               f"{len(moves)} move{'s' if len(moves) != 1 else ''} · "
               f"{'health OK' if not dead and not reauth else 'HEALTH ATTENTION'}")

    w: list[str] = []
    a = w.append
    a(f"# Weekly report — {today.isoformat()}")
    a("")
    a(f"**{verdict}**")
    a("")
    a(f"Window: {since_date} → {today.isoformat()}. Book compared against the scorecard "
      f"committed {prior_label}.")
    a("")

    a("## 1. The book")
    a("")
    if edge:
        a(f"**Actionable long set: {', '.join(edge_names) if edge_names else 'empty'}** "
          f"— `{edge[1]}` (the scorecard's own four-conjunct read: construction-validated, "
          f"read-robust, cheap on parity, and a BUY).")
        if sorted(edge_names) != approx:
            a("")
            a(f"> ⚠ Cross-check disagrees: deriving the set from the committed JSON's three "
              f"available conjuncts gives {approx or 'nothing'}. The JSON carries no `read_par`, "
              f"so the sentence above is authoritative — but the gap is worth a look.")
    else:
        a("Actionable long set: could not be read from `outputs/book_scorecard.md`.")
    a("")
    if not prior_rows:
        a("_No prior scorecard to diff against — this is the first report._")
    elif not moves:
        a("Nothing crossed a threshold: no band flips, no tier changes, no NAV move ≥2% "
          "and no EV move ≥2pp.")
    else:
        a("| Name | What | Detail |")
        a("|---|---|---|")
        for m in moves:
            a(f"| {m.ticker} | {m.kind} | {m.detail} |")
    a("")

    a("## 2. Needs your word")
    a("")
    if queue:
        for q in queue:
            a(f"- {q}")
    else:
        a("Nothing owed.")
    a("")

    a("## 3. What the machine did")
    a("")
    try:
        from .promote import evaluate_price_absorb
        pv = evaluate_price_absorb()
        if pv.ok:
            a(f"- **Standing drift is AUTO-ABSORBABLE** ({pv.rows_considered} gate rows): "
              f"price-vintage only, no NAV move, no band exit, no BUY-ward flip. This is the "
              f"shape a one-word ratify takes.")
        else:
            a(f"- **Standing drift needs your eye** ({pv.rows_considered} gate rows):")
            for r in pv.freeze_reasons:
                a(f"    - {r}")
    except Exception as exc:
        a(f"- Lane-D check unavailable: {exc}")
    a(f"- Notifications sent in the window: {pages} page(s), {digests} digest(s)"
      + (f"; last send {last_send}" if last_send else "; **no sends at all — check the notifier**"))
    if ratifies:
        a("- Baseline re-anchors:")
        for r in ratifies:
            a(f"    - {r}")
    else:
        a("- No baseline re-anchor in the window.")
    a(f"- Uncommitted files: {len(dirty)} · unpushed commits: {unpushed}")
    autopilot = ROOT / "AUTOPILOT_LOG.md"
    a(f"- Autopilot landings: {'see AUTOPILOT_LOG.md' if autopilot.exists() else 'none (no lane has authority yet)'}")
    a("")

    a("## 4. Health")
    a("")
    a("| Job | Outcome | Age (h) | Late? | Last heartbeat |")
    a("|---|---|--:|:--|---|")
    for job, outcome, ts, age, late in hbs:
        a(f"| {job} | {outcome} | {'—' if age is None else f'{age:.0f}'} | "
          f"{'**LATE**' if late else 'ok'} | {ts} |")
    a("")
    if reauth:
        for r in reauth:
            a(f"- **REAUTH NEEDED — {r.get('surface')}**: {r.get('reason')} (since "
              f"{str(r.get('since', ''))[:10]})")
    else:
        a("- Credentials: no surface has reported an auth failure.")
    if ping:
        a(f"- Dead-man ping: {ping.get('status')} at {ping.get('ts', '')[:19]}"
          + (f" — {ping.get('detail')}" if ping.get("detail") else ""))
    else:
        a("- Dead-man ping: no status recorded yet.")
    a("")

    a("## 5. Next 14 days")
    a("")
    if cal:
        for when, what in cal:
            a(f"- **{when}** — {what}")
    else:
        a("Nothing dated in the next fortnight.")
    a("")

    a("## 6. Flag counts (what the daily digest would have mailed)")
    a("")
    tags: dict[str, int] = {}
    for f in flags:
        tags[f.split()[0]] = tags.get(f.split()[0], 0) + 1
    if tags:
        for tag, n in sorted(tags.items(), key=lambda kv: (-kv[1], kv[0])):
            a(f"- {tag}: {n}")
    else:
        a("No flags.")
    a("")
    a(f"_Generated by `crude_tanker_fv.weekly_report` at "
      f"{datetime.now(timezone.utc).isoformat(timespec='seconds')}. Every figure is derived "
      f"from a committed surface or machine state; nothing here is hand-maintained._")
    return "\n".join(w) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="the owner's weekly report")
    ap.add_argument("--send", action="store_true", help="email it through the notify channel")
    ap.add_argument("--stdout", action="store_true", help="print only; write no file")
    ap.add_argument("--days", type=int, default=7, help="comparison window (default 7)")
    args = ap.parse_args(argv)

    text = build_report(days=args.days)
    if args.stdout:
        print(text)
        return 0
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    path = OUTPUTS / f"weekly_report_{date.today().isoformat()}.md"
    path.write_text(text)
    print(f"weekly report -> {path.relative_to(ROOT)}")
    if args.send:
        from . import notify
        subject_line = text.splitlines()[2].strip("* ")
        ok = notify.send_email(f"[crude-fv] WEEKLY · {subject_line}", text)
        print("emailed" if ok else "SEND FAILED — see state/notify_down.log")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

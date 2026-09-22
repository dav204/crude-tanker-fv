"""Accepted committed snapshots. Regeneration alone never publishes a valuation."""
import argparse
import hashlib
import json
import subprocess
from datetime import date, datetime, timezone
from pathlib import Path

from .runtime import atomic_json, locked

ROOT = Path(__file__).resolve().parents[2]
PRODUCTION = Path('/Users/dan_personal/Projects/crude-tanker-fv')


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True).strip()


def validate(root, now=None):
    from .promote import evaluate_land
    from .scorecard import handoff_coherence_flags
    from .loaders import load_watchlist
    now = now or datetime.now(timezone.utc)
    path = root / "outputs/book_scorecard.json"
    committed = subprocess.check_output(["git", "show", "HEAD:outputs/book_scorecard.json"], cwd=root)
    if path.read_bytes() != committed:
        raise ValueError("surface is not the committed version")
    doc = json.loads(committed)
    if doc.get("schema_version") != "2.9":
        raise ValueError("publication requires schema 2.9")
    generated = datetime.fromisoformat(doc["generated_at"].replace("Z", "+00:00"))
    if generated.tzinfo is None or not 0 <= (now - generated).total_seconds() <= 72 * 3600:
        raise ValueError("generated_at is invalid, future, or older than 72h")
    names = doc.get("names", [])
    tickers = [n.get("ticker") for n in names]
    if len(set(tickers)) != len(tickers) or set(tickers) != set(load_watchlist(root / "inputs")):
        raise ValueError("publication must contain each watchlist name exactly once")
    problems = handoff_coherence_flags(doc)
    for row in names:
        if not row.get("void"):
            if not row.get("cycles") or any(c.get("ratio") is None or not c.get("label") or not c.get("anchor_basis") for c in row["cycles"]):
                problems.append(row["ticker"] + ": missing cycle basis")
    from .calendar import policy, quarter as calendar_quarter
    if policy(root / "inputs")["enabled"]:
        valuation_date = date.fromisoformat(doc["valuation_date"])
        if not 0 <= (now.date() - valuation_date).days <= 3:
            problems.append("live publication has a future or stale valuation date")
        if doc.get("projection_start_quarter") != calendar_quarter(valuation_date):
            problems.append("valuation date/projection quarter mismatch")
        for row in names:
            if row.get("void"):
                continue
            timeline = row.get("valuation_timeline") or {}
            if timeline.get("valuation_date") != doc["valuation_date"] or timeline.get("projection_start_quarter") != doc["projection_start_quarter"]:
                problems.append(row["ticker"] + ": inconsistent valuation timeline")
    verdict, _ = evaluate_land(root, now)
    problems.extend(verdict.freeze_reasons)
    if problems:
        raise ValueError("; ".join(problems))
    return doc, committed


def publish(root=ROOT, now=None):
    now = now or datetime.now(timezone.utc)
    store = root / "state/publications"
    with locked(store / "publish.lock"):
        try:
            doc, raw = validate(root, now)
            content_hash = hashlib.sha256(json.dumps(doc, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            source = git(root, "rev-parse", doc["source_commit"])
            output = git(root, "log", "-1", "--format=%H", "--", "outputs/book_scorecard.json")
            identity = hashlib.sha256((output + content_hash).encode()).hexdigest()
            envelope = {"publication_id": identity, "content_hash": content_hash,
                        "source_commit": source, "output_commit": output,
                        "accepted_at": now.isoformat(), "generated_at": doc["generated_at"],
                        "validation": "accepted", "scorecard": doc}
            path = store / "accepted" / (identity + ".json")
            if not path.exists():
                atomic_json(path, envelope)
            else:
                envelope = json.loads(path.read_text())
            atomic_json(store / "current.json", {k: envelope[k] for k in envelope if k != "scorecard"})
            atomic_json(store / "status.json", {"status": "accepted", "publication_id": identity, "at": now.isoformat()})
            return envelope
        except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
            atomic_json(store / "status.json", {"status": "held", "at": now.isoformat(),
                                               "reason": str(exc), "resolver": "producer workflow"})
            raise


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=["publish", "status"])
    args = ap.parse_args(argv)
    if args.command == "status":
        print((ROOT / "state/publications/status.json").read_text())
        return 0
    if ROOT.resolve() != PRODUCTION:
        raise SystemExit("publication CLI is production-only; shadow regeneration cannot publish")
    try:
        print(json.dumps(publish(), indent=2))
        return 0
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as exc:
        print("PUBLICATION HELD: " + str(exc))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

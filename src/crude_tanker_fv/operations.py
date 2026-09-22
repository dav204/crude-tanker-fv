"""Production run receipts and five-minute publication/delivery recovery worker."""
import argparse
import json
import os
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

from . import delivery, notify, publication
from .runtime import atomic_json, locked, commit_paths

ROOT = Path(__file__).resolve().parents[2]
GOVERNOR = ROOT.parent / "portfolio-governance"


def utc():
    return datetime.now(timezone.utc).isoformat()


def start(root=ROOT):
    identity = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ-") + uuid.uuid4().hex[:10]
    atomic_json(root / "state/operations/runs" / (identity + ".json"),
                {"run_id": identity, "started_at": utc(), "status": "started"})
    return identity


def finish(identity, stages, root=ROOT, governor=GOVERNOR, ping=True):
    from .sentinel import _ping
    path = root / "state/operations/runs" / (identity + ".json")
    receipt = json.loads(path.read_text())
    receipt.update(stages=stages, finished_at=utc(), status="completed")
    pubstatus = root / "state/publications/status.json"
    receipt["publication"] = json.loads(pubstatus.read_text()) if pubstatus.exists() else {"status": "unavailable"}
    receipt["consumer_check"] = "queued" if receipt["publication"]["status"] == "accepted" else "not_published"
    if receipt["publication"]["status"] == "accepted":
        try:
            _, land = import_governor(governor)
            checked = consume(land.load_accepted(root), governor)
            receipt["consumer_check"] = {"status": "checked", "publication_id": receipt["publication"]["publication_id"], "events": checked["events"]}
            stages["consumer_check"] = 0
        except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
            receipt["consumer_check"] = {"status": "failed", "reason": str(exc)}
            stages["consumer_check"] = 1
    failures = {k: v for k, v in stages.items() if v != 0 and not (k == "checks" and v == 2)}
    if failures:
        receipt["status"] = "held" if set(failures) <= {"publication", "auto_land", "auto_push"} else "failed"
        key = "operation-failure:" + json.dumps(failures, sort_keys=True) + ":" + receipt["publication"].get("reason", "")
        delivery.enqueue("[crude-fv] PAGE: publication workflow " + receipt["status"],
                         "Stages: " + json.dumps(failures, sort_keys=True) + "\nPublication: " + json.dumps({k: receipt["publication"].get(k) for k in ("status", "reason", "resolver")}, sort_keys=True) +
                         "\nACTION: OWNER — inspect the producer run receipt and resolve its blocking stage.", root / "state", key=key)
    atomic_json(path, receipt)
    environ = notify.load_env_file(notify.ENV_FILE)
    for directory in (root / "state", governor / "monitor/state"):
        delivery.drain(directory, environ=environ)
    receipt["delivery"] = "pending" if delivery.pending(root / "state") or delivery.pending(governor / "monitor/state") else "accepted"
    atomic_json(path, receipt)
    if ping:
        _ping(receipt["delivery"] == "accepted" and receipt["status"] == "completed", root / "state")
        receipt["healthcheck"] = json.loads((root / "state/ping_status.json").read_text())["status"]
    else:
        receipt["healthcheck"] = "shadow"
    atomic_json(path, receipt)
    return receipt


def import_governor(governor):
    directory = str(governor / "monitor")
    if directory not in sys.path:
        sys.path.insert(0, directory)
    import seam
    import land
    return seam, land


def consume(envelope, governor=GOVERNOR, *, shadow=False, now=None):
    seam, _ = import_governor(governor)
    if envelope.get("validation") == "accepted" and seam.fingerprint(envelope.get("scorecard")) != envelope.get("content_hash"):
        envelope = {"validation": "unavailable", "reason": "publication hash mismatch"}
    state = governor / "monitor/state"
    observed = state / "seam_observed.json"
    previous = json.loads(observed.read_text()) if observed.exists() else {}
    registry = json.loads((governor / "monitor/seam_registry.json").read_text())
    result = seam.check(envelope, registry, previous, now)
    changed, next_state = seam.transitions(result, previous)
    result["changes"] = changed
    if shadow:
        return result
    identity = envelope.get("publication_id", "unavailable")
    with locked(state / "landing.lock"):
        if changed:
            report = seam.render({"events": changed}, identity)
            key = "seam:" + identity + ":" + seam.fingerprint(changed)
            outbox = governor / "monitor/outbox" / ("seam-" + seam.fingerprint(key) + ".md")
            outbox.parent.mkdir(parents=True, exist_ok=True)
            outbox.write_text("# [portfolio] valuation seam changed\n\n" + report)
            commit_paths(governor, [str(outbox.relative_to(governor))], "monitor: seam " + identity[:12])
            queued = delivery.enqueue("[portfolio] valuation seam changed", report, state, key=key)
            result["delivery_id"] = queued.stem
        # Queue persistence precedes the observed-state advance, so failures cannot eat events.
        receipt = {"publication_id": identity, "checked_at": utc(), **result}
        receipt_path = state / "seam_receipts" / (identity + ".json")
        if not receipt_path.exists():
            atomic_json(receipt_path, receipt)
        atomic_json(state / "seam_latest.json", receipt)
        atomic_json(observed, dict(next_state, publication_id=identity, checked_at=utc()))
    return result


def worker(root=ROOT, governor=GOVERNOR, *, shadow=False):
    state = root / "state"
    with locked(state / "operations/worker.lock"):
        if shadow:
            _, land = import_governor(governor)
            try:
                envelope = land.load_accepted(root)
            except (OSError, ValueError, KeyError):
                envelope = {}
            return consume(envelope, governor, shadow=True)
        # Catch manual accepted commits too; a refusal never overwrites the accepted pointer.
        try:
            publication.publish(root)
        except (ValueError, KeyError, OSError, subprocess.CalledProcessError):
            pass
        observed_path = governor / "monitor/state/seam_observed.json"
        last = json.loads(observed_path.read_text()).get("publication_id") if observed_path.exists() else None
        accepted = sorted((state / "publications/accepted").glob("*.json"), key=lambda p: json.loads(p.read_text())["accepted_at"])
        start_index = 0
        if last:
            matches = [i for i, p in enumerate(accepted) if p.stem == last]
            start_index = matches[-1] + 1 if matches else 0
        for path in accepted[start_index:]:
            consume(json.loads(path.read_text()), governor)
        if accepted:
            # Re-evaluate freshness even when no publication arrives.
            envelope = json.loads(accepted[-1].read_text())
            pubstatus = json.loads((state / "publications/status.json").read_text())
            if pubstatus["status"] == "held":
                envelope["publication_hold"] = pubstatus["reason"]
            consume(envelope, governor)
        else:
            consume({}, governor)
        for directory in (state / "operations/runs", governor / "monitor/state/runs"):
            for path in directory.glob("*.json"):
                run = json.loads(path.read_text())
                if run.get("status") == "started" and not run.get("report") and (datetime.now(timezone.utc) - datetime.fromisoformat(run["started_at"])).total_seconds() > 2 * 3600:
                    run.update(status="interrupted", blocker="run started over two hours ago without a persisted outcome", resolver="workflow repair")
                    atomic_json(path, run)
                    delivery.enqueue("[crude-fv] PAGE: interrupted scheduled run", "Run " + run["run_id"] + " has no completed outcome. ACTION: OWNER — inspect the scheduled task and repair its blocked stage.", state, key="interrupted:" + run["run_id"])
        from .work_items import refresh_worker
        if (root / "work_items.yaml").exists():
            refresh_worker(root)
        environ = notify.load_env_file(notify.ENV_FILE)
        for directory in (state, governor / "monitor/state"):
            delivery.drain(directory, environ=environ)
        _, land = import_governor(governor)
        run_paths = sorted((governor / "monitor/state/runs").glob("*.json"))
        weekly_paths = [p for p in run_paths if json.loads(p.read_text()).get("job", "weekly") == "weekly"]
        for path in run_paths:
            run = json.loads(path.read_text())
            age = (datetime.now(timezone.utc) - datetime.fromisoformat(run["started_at"])).total_seconds()
            land.recover(path, root=governor, allow_ping=bool(weekly_paths) and path == weekly_paths[-1] and 0 <= age <= 7 * 86400)
        # Recover only previously attempted daily receipts, never manufacture a new daily run.
        if not delivery.pending(state) and not delivery.pending(governor / "monitor/state"):
            paths = sorted((state / "operations/runs").glob("*.json"))
            if paths:
                path = paths[-1]; receipt = json.loads(path.read_text())
                age = (datetime.now(timezone.utc) - datetime.fromisoformat(receipt["started_at"])).total_seconds()
                if receipt.get("status") == "completed" and receipt.get("finished_at") and receipt.get("healthcheck") != "SENT" and 0 <= age <= 54 * 3600:
                    from .sentinel import _ping
                    os.environ.update({k: v for k, v in environ.items() if k.startswith("CRUDE_FV_")})
                    _ping(True, state)
                    receipt.update(delivery="accepted", healthcheck=json.loads((state / "ping_status.json").read_text())["status"])
                    atomic_json(path, receipt)
        pubstatus = json.loads((state / "publications/status.json").read_text())
        result = {"at": utc(), "publication": pubstatus, "consumer_publication": json.loads((governor / "monitor/state/seam_latest.json").read_text())["publication_id"], "status": "pending_delivery" if delivery.pending(state) or delivery.pending(governor / "monitor/state") else ("held" if pubstatus["status"] == "held" else "ok")}
        atomic_json(state / "operations/worker.json", result)
        return result


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("start")
    f = sub.add_parser("finish"); f.add_argument("run_id"); f.add_argument("stages", nargs="+")
    w = sub.add_parser("worker"); w.add_argument("--shadow", action="store_true")
    r = sub.add_parser("retry"); r.add_argument("channel", choices=["producer", "governor"]); r.add_argument("message_id")
    c = sub.add_parser("commit"); c.add_argument("subject"); c.add_argument("paths", nargs="+")
    args = ap.parse_args(argv)
    if args.cmd == "start":
        print(start()); return 0
    if args.cmd == "finish":
        receipt = finish(args.run_id, {k: int(v) for k, v in (item.split("=", 1) for item in args.stages)})
        print(json.dumps(receipt, indent=2))
        return 0 if receipt["status"] == "completed" and receipt["delivery"] == "accepted" and receipt["healthcheck"] == "SENT" else 1
    if args.cmd == "retry":
        delivery.retry(ROOT / "state" if args.channel == "producer" else GOVERNOR / "monitor/state", args.message_id)
        return 0
    if args.cmd == "commit":
        print(commit_paths(ROOT, args.paths, args.subject)); return 0
    if ROOT.resolve() != publication.PRODUCTION and not args.shadow:
        raise SystemExit("worker is production-only")
    print(json.dumps(worker(shadow=args.shadow), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

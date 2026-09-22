"""Durable, bounded SMTP retries. Accepted means SMTP accepted, not inbox delivery."""
import hashlib
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

from .runtime import atomic_json, locked

RETRY_SECONDS = (300, 900, 3600, 21600)


def clock():
    return datetime.now(timezone.utc)


def enqueue(subject, body, state_dir, *, key=None, now=None):
    now = now or clock()
    identity = key or hashlib.sha256((subject + "\0" + body).encode()).hexdigest()
    message_id = hashlib.sha256(identity.encode()).hexdigest()
    path = Path(state_dir) / "delivery" / (message_id + ".json")
    with locked(path.parent / "queue.lock"):
        if not path.exists():
            atomic_json(path, {"id": message_id, "message_id": f"<{message_id}@portfolio.local>",
                              "subject": subject, "body": body, "status": "pending", "attempts": 0,
                              "created_at": now.isoformat(), "next_attempt": now.isoformat()})
        else:
            old = json.loads(path.read_text())
            if old["subject"] != subject or old["body"] != body:
                raise ValueError("delivery key already belongs to a different message")
    return path


def attempt(path, *, environ, smtp_factory=None, now=None):
    from .notify import _send_email
    now = now or clock()
    path = Path(path)
    with locked(path.parent / "queue.lock"):
        msg = json.loads(path.read_text())
        if msg["status"] in ("accepted", "blocked", "exhausted"):
            return msg
        if datetime.fromisoformat(msg["next_attempt"]) > now:
            return msg
        if msg["attempts"] >= len(RETRY_SECONDS) + 1:
            msg.update(status="exhausted", next_attempt=None)
            atomic_json(path, msg)
            return msg
        msg.setdefault("first_attempt", now.isoformat())
        msg["attempts"] += 1
        msg.update(status="sending", last_attempt=now.isoformat())
        atomic_json(path, msg)
        result = {}
        ok = _send_email(msg["subject"], msg["body"], environ=environ,
                         smtp_factory=smtp_factory, state_dir=path.parent.parent,
                         message_id=msg["message_id"], receipt=result)
        msg["last_result"] = result
        if ok:
            msg.update(status="accepted", accepted_at=now.isoformat(), next_attempt=None)
        elif result.get("failure_class") in ("authentication", "configuration", "permanent"):
            msg.update(status="blocked", next_attempt=None)
        elif msg["attempts"] > len(RETRY_SECONDS):
            msg.update(status="exhausted", next_attempt=None)
        else:
            due = datetime.fromisoformat(msg["first_attempt"]) + timedelta(seconds=RETRY_SECONDS[msg["attempts"] - 1])
            msg.update(status="pending", next_attempt=max(due, now + timedelta(seconds=1)).isoformat())
        atomic_json(path, msg)
        return msg


def drain(state_dir, *, environ, now=None, smtp_factory=None):
    return [attempt(p, environ=environ, now=now, smtp_factory=smtp_factory)
            for p in sorted((Path(state_dir) / "delivery").glob("*.json"))]


def pending(state_dir):
    return [json.loads(p.read_text()) for p in sorted((Path(state_dir) / "delivery").glob("*.json"))
            if json.loads(p.read_text())["status"] != "accepted"]


def retry(state_dir, message_id):
    if len(message_id) != 64 or any(c not in "0123456789abcdef" for c in message_id):
        raise ValueError("invalid message id")
    path = Path(state_dir) / "delivery" / (message_id + ".json")
    with locked(path.parent / "queue.lock"):
        msg = json.loads(path.read_text())
        if msg["status"] != "accepted":
            msg.pop("first_attempt", None)
            msg.update(status="pending", attempts=0, created_at=clock().isoformat(), next_attempt=clock().isoformat())
            atomic_json(path, msg)

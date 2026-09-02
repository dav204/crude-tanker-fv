"""Credential / authorization failure register (2026-09-02, Stage 0).

A fetcher or sender refused for AUTH reasons marks its surface here; the next
success clears it; the sentinel emits `REAUTH-NEEDED <surface>` (page_once, so the
owner is told once and the digest carries it until cleared). Surfaces today:
rocketchat (HTTP 401/403 on the PAT), smtp (SMTPAuthenticationError on the app
password), healthchecks (two consecutive 4xx on the ping URL). Files under
state/reauth/ — machine-local like every other cursor.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

STATE_DIR = Path(__file__).resolve().parents[2] / "state" / "reauth"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def mark(surface: str, reason: str, state_dir: Path = STATE_DIR) -> Path:
    state_dir.mkdir(parents=True, exist_ok=True)
    path = state_dir / f"{surface}.json"
    since = _now()
    if path.exists():
        try:
            since = json.loads(path.read_text()).get("since") or since
        except Exception:
            pass
    path.write_text(json.dumps({"surface": surface, "reason": reason,
                                "since": since, "last_seen": _now()}, indent=1))
    return path


def clear(surface: str, state_dir: Path = STATE_DIR) -> bool:
    path = state_dir / f"{surface}.json"
    if path.exists():
        path.unlink()
        return True
    return False


def pending(state_dir: Path = STATE_DIR) -> list[dict]:
    out = []
    if not state_dir.exists():
        return out
    for p in sorted(state_dir.glob("*.json")):
        try:
            out.append(json.loads(p.read_text()))
        except Exception:
            out.append({"surface": p.stem, "reason": "unreadable register file",
                        "since": _now(), "last_seen": _now()})
    return out

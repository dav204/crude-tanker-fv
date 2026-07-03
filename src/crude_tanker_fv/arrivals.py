"""Arrival validation + arrival ledger (WO2 1.5, invariant 6).

Every fetched document is validated AT STAGING: a PDF must carry the %PDF
magic, open, and contain >=1 page — anything else moves to a quarantine dir
beside its staging tree and flags, never sits in the archive looking like
data. Every arrival (staged, quarantined, or page-only) appends one line to
state/arrivals.jsonl with its disposition — the join target the WO2
acceptance compiles against sent notifications.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def validate_pdf(path: Path) -> "tuple[bool, str]":
    try:
        with path.open("rb") as fh:
            if fh.read(5) != b"%PDF-":
                return False, "no %PDF magic"
        from pypdf import PdfReader

        n = len(PdfReader(str(path)).pages)
        if n < 1:
            return False, "zero pages"
        return True, f"{n} pages"
    except Exception as exc:
        return False, f"unreadable: {exc}"


def quarantine(path: Path, reason: str) -> Path:
    """Move a failed arrival to <staging-parent>/_quarantine/ — visible,
    inspectable, and never mistaken for data by anything reading the tree."""
    qdir = path.parent / "_quarantine"
    qdir.mkdir(parents=True, exist_ok=True)
    dest = qdir / path.name
    path.replace(dest)
    (dest.with_suffix(dest.suffix + ".reason")).write_text(
        f"{datetime.now(timezone.utc).isoformat(timespec='seconds')} {reason}\n")
    return dest


def record_arrival(kind: str, identity: str, disposition: str, detail: str = "",
                   state_dir: Path = Path("state")) -> None:
    """One ledger line per arrival. identity = the stable arrival identity
    (invariant 4): staged path, RC message-id, or EDGAR accession number.
    disposition: staged | quarantined | duplicate | page-only."""
    state_dir.mkdir(parents=True, exist_ok=True)
    line = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "kind": kind, "identity": identity, "disposition": disposition}
    if detail:
        line["detail"] = detail
    with (state_dir / "arrivals.jsonl").open("a") as fh:
        fh.write(json.dumps(line) + "\n")


def stage_pdf(path: Path, kind: str, identity: str,
              state_dir: Path = Path("state")) -> "tuple[bool, Path]":
    """Validate-or-quarantine a just-written PDF and ledger the outcome.
    Returns (ok, final_path). Callers treat ok=False as a FETCH-FAILED-class
    event to surface, not an exception."""
    ok, note = validate_pdf(path)
    if ok:
        record_arrival(kind, identity, "staged", note, state_dir)
        return True, path
    dest = quarantine(path, note)
    record_arrival(kind, identity, "quarantined", note, state_dir)
    return False, dest

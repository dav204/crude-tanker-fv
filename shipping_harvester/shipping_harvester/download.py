"""Fetch issues to a local cache, de-duplicated by (broker, ISO week).

Cache is content-addressed-ish: <broker>/<YYYY>W<WW>_<sha8>.pdf, so re-running
is cheap and idempotent. A JSONL manifest records every issue seen.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from . import config
from .models import ReportRef
from .net import PoliteSession


def dedupe(refs: list[ReportRef]) -> list[ReportRef]:
    """One ref per (broker, ISO year, ISO week).

    Tie-break: prefer a ref that actually has a PDF link, then the most
    recently published. This collapses HSN+CapitalLink duplicates of the same
    issue.
    """
    best: dict[tuple, ReportRef] = {}
    for r in refs:
        cur = best.get(r.dedupe_key)
        if cur is None:
            best[r.dedupe_key] = r
            continue
        better = (
            (r.pdf_url is not None, r.published)
            > (cur.pdf_url is not None, cur.published)
        )
        if better:
            best[r.dedupe_key] = r
    return sorted(best.values(), key=lambda r: (r.broker_id, r.published))


def _cache_path(ref: ReportRef, sha8: str) -> Path:
    name = f"{ref.iso_year}W{ref.iso_week:02d}_{sha8}.pdf"
    return config.PDF_CACHE / ref.broker_id / name


def _already_have(ref: ReportRef) -> Path | None:
    """If any PDF for this (broker, week) is cached, return it."""
    folder = config.PDF_CACHE / ref.broker_id
    if not folder.exists():
        return None
    prefix = f"{ref.iso_year}W{ref.iso_week:02d}_"
    for p in folder.glob(f"{prefix}*.pdf"):
        return p
    return None


def _append_manifest(record: dict) -> None:
    config.MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with config.MANIFEST.open("a") as f:
        f.write(json.dumps(record) + "\n")


def download_pdf(session: PoliteSession, ref: ReportRef) -> Path | None:
    """Download one issue's PDF (cached). Returns local path or None."""
    cached = _already_have(ref)
    if cached is not None:
        return cached
    if not ref.pdf_url:
        _append_manifest({**ref.to_dict(), "status": "no_pdf_url"})
        return None
    try:
        resp = session.get(ref.pdf_url, expect="pdf")
        content = resp.content
    except Exception as e:  # noqa: BLE001
        _append_manifest({**ref.to_dict(), "status": f"download_error:{e}"})
        return None
    if not content[:5].startswith(b"%PDF"):
        _append_manifest({**ref.to_dict(), "status": "not_a_pdf"})
        return None

    sha8 = hashlib.sha256(content).hexdigest()[:8]
    path = _cache_path(ref, sha8)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    _append_manifest({**ref.to_dict(), "status": "ok", "path": str(path), "sha8": sha8})
    return path

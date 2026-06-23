"""Recover Allied Weekly Market Report PDFs (2019-2020) from the Wayback Machine.

Capital Link's live site is behind a 202 bot-challenge, but archive.org swept its
media library. The value age-curve lives in the Weekly Market Report
(`Allied<wk><yy>.pdf` / `ALLIED-Weekly-Market-Report_*`), NOT the `*SnP*` /
`*Statistics*` supplement — we drop the latter. PDFs are dated by upload-path
year, so we DON'T filter the CDX by capture date.

Downloads to data/wayback/allied/ + a sidecar manifest (orig url, timestamp).
urllib only — WebFetch is blocked for web.archive.org and curl needs a grant.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
import urllib.request
from pathlib import Path

CDX = ("http://web.archive.org/cdx/search/cdx?url=capitallinkshipping.com/"
       "wp-content/uploads*&output=json&filter=urlkey:.*allied.*"
       "&collapse=urlkey&limit=2000")
OUT = Path("data/wayback/allied")


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "shipping-harvester research"})
    return urllib.request.urlopen(req, timeout=90).read()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = json.loads(_get(CDX))[1:]   # drop header row
    manifest = []
    got = 0
    for r in rows:
        ts, orig = r[1], r[2]
        low = orig.lower()
        if not low.endswith(".pdf"):
            continue
        if "snp" in low or "statistics" in low:   # supplement carries no value grid
            continue
        m = re.search(r"/uploads/(\d{4})/", orig)
        yr = m.group(1) if m else ""
        if yr not in ("2019", "2020"):
            continue
        try:
            data = _get(f"https://web.archive.org/web/{ts}id_/{orig}")
        except Exception as e:  # noqa: BLE001
            print(f"  ERR {orig.split('/')[-1]}: {str(e)[:60]}")
            continue
        if not data[:5].startswith(b"%PDF"):
            print(f"  not-a-pdf: {orig.split('/')[-1]}")
            continue
        sha8 = hashlib.sha256(data).hexdigest()[:8]
        name = f"{orig.split('/')[-1].rsplit('.',1)[0]}_{sha8}.pdf"
        (OUT / name).write_bytes(data)
        manifest.append({"file": name, "orig": orig, "timestamp": ts, "upload_year": yr})
        got += 1
        print(f"  {yr}  {name}  ({len(data)} bytes)")
        time.sleep(1.0)
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))
    print(f"\ndownloaded {got} Allied 2019-2020 Weekly PDFs -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

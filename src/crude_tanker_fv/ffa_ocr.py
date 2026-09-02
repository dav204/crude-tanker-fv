"""FFA-OCR Stage 1 — classify + parse the daily dry-bulk FFA widget.

Source: Rocket.Chat clipboard screenshots in ``inputs/ffa_drybulk/`` (one
poster's habit — single-source dependence is a designed-for risk; the
weekly staleness alarm exists because this feed must die loudly).

Target format (the "modern" widget, verified Nov-2025 → Jun-2026): a
three-panel "Markets" table — Cape / Pmax / Smax — each with five tenors
(front month, next month, Q-next, Q-following, Cal-year), green-on-dark.

OCR recipe (locked 2026-06-11 on live samples): grayscale -> 4x LANCZOS
upscale -> tesseract --psm 6. Color-original OCR drops the panel headers;
grayscale recovers them. Scratch files go under ``state/ffa_scratch/``
(NOT /tmp — tesseract cannot read /tmp under the agent sandbox).

Sanity model (discovered, not assumed): monthly and Cal tenors tick in
$25 steps; Q tenors are displayed as the UNROUNDED 3-month average, so a
correct Q value satisfies ``min_dist(3*v, 25) <= 2`` while months/Cal
satisfy ``v % 25 == 0``. A 31766 that looks like digit noise is a real
95300/3. Day-over-day continuity (vs the previous parsed curve) flags
moves >10% per tenor.

Output: review queue at ``outputs/ffa_ocr_queue.md`` + machine-readable
``state/ffa_ocr_curves.json``. Promotion to the pipeline-loaded
``inputs/market_data/ffa_forward_curve.yaml`` is HUMAN-ONLY (same rule
as S&P print candidates; automation never writes pipeline-loaded YAMLs).

Run: ``python -m crude_tanker_fv.ffa_ocr [--since YYYY-MM-DD] [--full]``
— incremental via the cursor in ``state/ffa_ocr_state.json``.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
FFA_DIR = ROOT / "inputs" / "ffa_drybulk"
SCRATCH = ROOT / "state" / "ffa_scratch"
STATE_PATH = ROOT / "state" / "ffa_ocr_state.json"
CURVES_PATH = ROOT / "state" / "ffa_ocr_curves.json"
QUEUE_PATH = ROOT / "outputs" / "ffa_ocr_queue.md"

PANELS = ("cape", "pmax", "smax")
MONTHS = ("jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec")

# OCR confuses Q with O/G/a/0 in tenor labels.
_TENOR_RE = re.compile(r"^(?:(?P<month>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"
                       r"|[qoga0](?P<q>[1-4])"
                       r"|cal(?P<cal>2\d))$", re.IGNORECASE)
_PRICE_RE = re.compile(r"^\d{4,6}$")

DAY_MOVE_BAND_PCT = 10.0
QTR_AVG_TOLERANCE = 2  # |3*v - nearest multiple of 25| for Q-tenor averages


def ocr_image(src: Path, psm: int = 6) -> tuple[str, list[dict]]:
    """Locked recipe: grayscale -> 4x LANCZOS -> tesseract psm 6, TSV out.

    Returns (plain_text, words) where words carry x-position + confidence —
    positional parsing assigns cells to panels by x-band, so one garbled
    cell no longer drops a whole row (the Jun-11 Smax "Q4"-read-as-"4"
    case). plain_text is reassembled from the TSV for the classifier.
    """
    SCRATCH.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("L")
    im = im.resize((im.width * 4, im.height * 4), Image.LANCZOS)
    prep = SCRATCH / "ocr_probe.png"
    im.save(prep)
    r = subprocess.run(["tesseract", str(prep), "-", "--psm", str(psm), "tsv"],
                       capture_output=True)
    words = []
    for line in r.stdout.decode("utf-8", errors="replace").splitlines()[1:]:
        f = line.split("\t")
        if len(f) == 12 and f[0] == "5" and f[11].strip():
            words.append({"line": (f[2], f[3], f[4]), "x": int(f[6]),
                          "y": int(f[7]), "width": int(f[8]),
                          "conf": float(f[10]), "text": f[11].strip()})
    text = ""
    last = None
    for w in words:
        text += ("\n" if w["line"] != last and last else " ") + w["text"]
        last = w["line"]
    return text, words


def is_ffa_widget(text: str) -> bool:
    """Classifier: Cape header + a Cal2x tenor + the tabular header riff."""
    return (re.search(r"\bcape\b", text, re.IGNORECASE) is not None
            and re.search(r"\bcal2\d\b", text, re.IGNORECASE) is not None
            and re.search(r"produc\w*\s+price\s+change", text, re.IGNORECASE) is not None)


def _norm_tenor(tok: str) -> str | None:
    m = _TENOR_RE.match(tok.strip(".:|"))
    if not m:
        return None
    if m.group("month"):
        return m.group("month").lower()
    if m.group("q"):
        return f"q{m.group('q')}"
    return f"cal{m.group('cal')}"


def parse_widget(words: list[dict]) -> dict[str, dict[str, int]]:
    """Positional parse: TSV words -> {panel: {tenor: price}}.

    Two layouts exist in the wild. Joeri.van.der.Sman's desktop widget
    lays the three panels side-by-side (Cape, Pmax, Smax) — a word's
    panel is its x-band third. Chris.Palun's phone screenshots
    (2026-07-20 →) STACK the same three panels vertically — there the
    "Cape"/"Pmax"/"Smax" header y-positions bound each panel's rows and
    x-bands would mis-bucket everything. The header anchors decide which
    layout applies. Each visual row carries one tenor (repeated per panel
    in the wide layout) — the row tenor is decided by majority vote of
    the row's normalized tenor tokens, so a single garbled label can't
    drop the row. Change-column tokens are ignored (sign glyphs mangle;
    continuity checks run against our own archive instead).
    """
    curves: dict[str, dict[str, int]] = {p: {} for p in PANELS}
    if not words:
        return curves
    span = max(w["x"] + w["width"] for w in words)

    headers: dict[str, dict] = {}
    for w in words:
        name = w["text"].strip(".:|").lower()
        if name in PANELS and name not in headers:
            headers[name] = w
    stacked = len(headers) >= 2 and (
        max(h["y"] for h in headers.values()) - min(h["y"] for h in headers.values())
        > max(h["x"] for h in headers.values()) - min(h["x"] for h in headers.values())
    )
    bands = sorted((h["y"], p) for p, h in headers.items()) if stacked else None

    def _panel_of(w: dict) -> str | None:
        if not stacked:
            return PANELS[min(2, int(3 * w["x"] / span))]
        panel = None
        for y0, name in bands:
            if w["y"] >= y0:
                panel = name
        return panel  # None above the first header (cropped chrome) — skip
    rows: dict[tuple, list[dict]] = {}
    for w in words:
        rows.setdefault(w["line"], []).append(w)
    for row in rows.values():
        tenors = [t for t in (_norm_tenor(w["text"]) for w in row) if t]
        if not tenors:
            continue
        tenor = max(set(tenors), key=tenors.count)
        # prices: first plausible 4-6 digit token per panel band, skipping
        # change-column tokens (those carry +/-/~/# glyphs or trail ')')
        for w in row:
            # Trailing-punct strip ONLY: a leading stray glyph ("(3800" for
            # 31800) means a digit was eaten — stripping it would yield a
            # plausible-but-wrong price that can pass the tick check.
            tok = w["text"].rstrip(",.|;:»«=)")
            if not _PRICE_RE.match(tok) or w["conf"] < 60:
                continue
            panel = _panel_of(w)
            if panel is not None and tenor not in curves[panel]:
                curves[panel][tenor] = int(tok)
    return curves


MONTH_END_ROLL_DAY = 24   # from this day of the month the widget has dropped the
                          # expiring month, so 4 tenors (m2/Qn/Qf/Cal) IS the complete
                          # grid — the month-end structure ratified 2026-09-01
                          # (sp_promotion_round_2026-09-01 §Leg 2); the 8/25-8/31 rows
                          # had flagged structurally complete captures as incomplete.


def expected_tenors(curve: dict[str, int], print_date: date | None) -> int:
    n_months = sum(1 for t in curve if t in MONTHS)
    if print_date is not None and print_date.day >= MONTH_END_ROLL_DAY and n_months == 1:
        return 4
    return 5


def sanity_issues(curves: dict[str, dict[str, int]],
                  prev: dict[str, dict[str, int]] | None = None,
                  print_date: date | None = None) -> list[str]:
    issues = []
    n_tenors = {p: len(c) for p, c in curves.items()}
    expect = {p: expected_tenors(c, print_date) for p, c in curves.items()}
    if any(n_tenors[p] < expect[p] for p in curves):
        issues.append(f"incomplete grid {n_tenors} (expect {expect} tenors/panel)")
    for panel, curve in curves.items():
        if curve and max(curve.values()) > 3 * min(curve.values()):
            issues.append(f"{panel}: intra-curve spread "
                          f"{min(curve.values())}-{max(curve.values())} >3x — "
                          f"likely a digit-loss misread")
    for panel, curve in curves.items():
        for tenor, v in curve.items():
            # Months/Cal tick in $12.5 steps displayed truncated, so 2v sits
            # within 1 of a 25-multiple; Q tenors display the unrounded
            # 3-month average, so 6v sits within 6 of a 25-multiple.
            if tenor.startswith("q"):
                if min((6 * v) % 25, 25 - (6 * v) % 25) > 6:
                    issues.append(f"{panel}.{tenor}={v}: not a 3-month average "
                                  f"of $12.5-tick months")
            elif min((2 * v) % 25, 25 - (2 * v) % 25) > 1:
                issues.append(f"{panel}.{tenor}={v}: not on $12.5 tick")
            if prev and tenor in prev.get(panel, {}):
                p0 = prev[panel][tenor]
                move = (v / p0 - 1.0) * 100.0
                if abs(move) > DAY_MOVE_BAND_PCT:
                    issues.append(f"{panel}.{tenor}: {move:+.1f}% vs previous "
                                  f"curve ({p0} -> {v}) exceeds ±{DAY_MOVE_BAND_PCT:.0f}%")
    return issues


def _iter_images(since: date | None):
    for p in sorted(FFA_DIR.rglob("*.png")) + sorted(FFA_DIR.rglob("*.jpg")):
        m = re.match(r"(\d{4}-\d{2}-\d{2})_", p.name)
        if not m:
            continue
        d = date.fromisoformat(m.group(1))
        if since and d <= since:
            continue
        yield d, p


def _load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default


def run_scan(since: date | None, full: bool = False) -> tuple[int, int, int]:
    """Walk images newer than the cursor; OCR, classify, parse, queue.

    One curve per calendar day: the first classified FFA hit wins (the
    poster's morning capture; afternoon reposts are intraday snapshots).
    Returns (n_images, n_widgets, n_flagged).
    """
    state = _load_json(STATE_PATH, {})
    curves_db: dict = _load_json(CURVES_PATH, {})
    cursor = None
    if not full and since is None and state.get("last_scanned_date"):
        cursor = date.fromisoformat(state["last_scanned_date"])
    elif since:
        cursor = since

    n_images = n_widgets = n_flagged = 0
    newest = cursor
    queue_entries = []

    def _prev_curves(iso: str):
        """Nearest earlier parsed day — continuity is calendar-ordered,
        never scan-ordered (Apr-01 must not be judged against Jun-11)."""
        earlier = [d for d, e in curves_db.items()
                   if d < iso and e.get("status") in ("ok", "flagged")]
        return curves_db[max(earlier)]["curves"] if earlier else None

    by_day: dict[str, list[Path]] = {}
    for d, path in _iter_images(cursor):
        n_images += 1
        newest = max(newest, d) if newest else d
        by_day.setdefault(d.isoformat(), []).append(path)

    for iso in sorted(by_day):
        if not full and iso in curves_db and curves_db[iso].get("status") != "no_widget":
            continue
        # Best-of-day: parse EVERY classified image that day, keep the entry
        # with the fewest issues (a clean afternoon repost beats a mangled
        # morning capture). Continuity is judged against the previous day's
        # accepted curve, not intra-day reposts.
        prev_for_day = _prev_curves(iso)
        best = None
        for path in by_day[iso]:
            text, words = ocr_image(path)
            if not is_ffa_widget(text):
                continue
            curves = parse_widget(words)
            issues = sanity_issues(curves, prev_for_day,
                                   print_date=date.fromisoformat(iso))
            entry = {
                "status": "flagged" if issues else "ok",
                "source": str(path.relative_to(ROOT)),
                "curves": curves,
                "issues": issues,
            }
            if best is None or len(entry["issues"]) < len(best["issues"]):
                best = entry
            if not issues:
                break
        if best is None:
            curves_db.setdefault(iso, {"status": "no_widget"})
            continue
        n_widgets += 1
        if best["issues"]:
            n_flagged += 1
        curves_db[iso] = best
        queue_entries.append((iso, best))

    CURVES_PATH.parent.mkdir(parents=True, exist_ok=True)
    CURVES_PATH.write_text(json.dumps(curves_db, indent=1, sort_keys=True))
    if newest:
        state["last_scanned_date"] = newest.isoformat()
        state["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
        STATE_PATH.write_text(json.dumps(state, indent=1))
    _write_queue(curves_db)
    return n_images, n_widgets, n_flagged


def days_since_last_widget(curves_db: dict | None = None) -> int | None:
    """Staleness probe for the weekly runner (the feed must die loudly)."""
    db = curves_db if curves_db is not None else _load_json(CURVES_PATH, {})
    hits = [d for d, e in db.items() if e.get("status") in ("ok", "flagged")]
    if not hits:
        return None
    return (date.today() - date.fromisoformat(max(hits))).days


_MONTH_ORDER = ["jan", "feb", "mar", "apr", "may", "jun",
                "jul", "aug", "sep", "oct", "nov", "dec"]


def _tenor_sort_key(tenor: str, print_month: int) -> tuple:
    """Chronological queue order: months (from the print month, Dec→Jan
    wraps), then quarters, then Cal. The naive alphabetical sort put AUG
    before JUL, so the queue's m1/m2 header lied — the 2-Jul Supra spot
    proxy took the wrong month off it (decisions/ffa_promotion_2026-07-13.md)."""
    if tenor in _MONTH_ORDER:
        return (0, (_MONTH_ORDER.index(tenor) + 1 - print_month) % 12)
    if tenor.startswith("q") and tenor[1:].isdigit():
        # Chronological from the print's own quarter (2026-09-02): a September
        # print's Q1 is NEXT year's and sorts after Q4 — the alphabetical/numeric
        # order put Q1 first and scrambled the queue's Qn/Qf columns (8/31 trap).
        print_q = (print_month - 1) // 3 + 1
        return (1, (int(tenor[1:]) - print_q) % 4)
    return (2, tenor)


def _write_queue(curves_db: dict) -> None:
    lines = [
        "# FFA-OCR review queue — dry-bulk forward curves",
        "",
        "Parsed from the Rocket.Chat FFA widget screenshots (ffa_ocr.py).",
        "Review flagged rows against the source image; promote approved",
        "curves to `inputs/market_data/ffa_forward_curve.yaml` BY HAND —",
        "automation never writes pipeline-loaded YAMLs.",
        "",
        "| Date | Status | Cape (m1/m2/Qn/Qf/Cal) | Pmax | Smax | Issues | Source |",
        "|---|---|---|---|---|---|---|",
    ]
    for iso in sorted(curves_db, reverse=True):
        e = curves_db[iso]
        if e.get("status") == "no_widget":
            continue
        print_month = int(iso[5:7])

        def fmt(panel):
            c = e["curves"].get(panel, {})
            return "/".join(str(v) for _, v in sorted(
                c.items(), key=lambda kv: _tenor_sort_key(kv[0], print_month)))
        lines.append(f"| {iso} | {e['status']} | {fmt('cape')} | {fmt('pmax')} "
                     f"| {fmt('smax')} | {'; '.join(e['issues']) or '—'} "
                     f"| {e['source']} |")
    QUEUE_PATH.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="FFA widget OCR scan (Stage 1)")
    ap.add_argument("--since", help="scan images strictly after this date (YYYY-MM-DD)")
    ap.add_argument("--full", action="store_true", help="ignore the cursor")
    ap.add_argument("--staleness", action="store_true",
                    help="print days since last parsed widget and exit "
                         "(exit 1 if >7 — weekly-runner alarm)")
    args = ap.parse_args(argv)

    if args.staleness:
        days = days_since_last_widget()
        if days is None:
            print("FFA-OCR STALENESS: no parsed widgets at all")
            return 1
        print(f"FFA-OCR staleness: last parsed widget {days} day(s) ago")
        return 1 if days > 7 else 0

    since = date.fromisoformat(args.since) if args.since else None
    n_images, n_widgets, n_flagged = run_scan(since, full=args.full)
    print(f"scanned {n_images} images -> {n_widgets} widgets "
          f"({n_flagged} flagged) -> {QUEUE_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

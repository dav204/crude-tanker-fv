"""Dry-bulk FFA promote as a lane (2026-09-13), replacing the by-hand sitting that ran 13
times in 60 days (decisions/ffa_promotion_*.md).

    python -m crude_tanker_fv.ffa_promote            # packet only (default)
    python -m crude_tanker_fv.ffa_promote --apply    # write the curve + 12M files

It executes ONE ruled construction — the straddling-panel shape the owner ratified
2026-09-02 (decisions/ffa_promotion_2026-09-02.md, rulings Q-1/Q-2/Q-3/Q-7) — and FREEZES on
anything else. What it will not do is decide: an unruled panel shape, a flagged parse, a
missing panel, or a cycle-BAND crossing (Q-7, the one conjunct that always needed a word) all
stop the lane with the reason.

The construction, verbatim from the ruling:
  q1 = the front month ALONE (Q-2: the second month is a component of the quoted next quarter
       and would be double-counted) · q2 = that quarter · q3 = the following Q1
  q4..q6 solve the Cal-27 identity EXACTLY (mean of the four 2027 quarters = Cal-27)
  q7,q8 = the committed per-class 2028 deltas (Cape -500/-500 · Pana -400/-300 · Supra -300/-300)
  Post-Panamax = Pana · Handy-Bulk = Supra-Ultra x 0.90 to nearest 10 (locked §11.7.11)
  12M proxy = (q2 + q3)/2, unrounded, half-up to the integer the file stores (Q-1)
Handy-Bulk's 12M TC is NOT touched: it has no FFA panel and rides the MB dry weekly.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

import yaml

from .loaders import INPUTS_DIR

ROOT = INPUTS_DIR.parent
CURVES_DB = ROOT / "state" / "ffa_ocr_curves.json"
CURVE_FILE = INPUTS_DIR / "market_data" / "ffa_forward_curve.yaml"
TWELVE_FILE = INPUTS_DIR / "market_data" / "twelve_month_tc.yaml"
MEANS_FILE = INPUTS_DIR / "market_data" / "historical_tce_means.yaml"

PANELS = ("cape", "pmax", "smax")
PANEL_TO_CLASS = {"cape": "Cape", "pmax": "Pana", "smax": "Supra-Ultra"}
DELTAS_2028 = {"Cape": (-500, -500), "Pana": (-400, -300), "Supra-Ultra": (-300, -300)}
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
MAX_PRINT_AGE_DAYS = 10
# The cycle bands the promote may not cross unattended (cycle._BANDS thresholds, Q-7).
BAND_EDGES = (1.5, 1.2, 0.8, 0.5)


class Freeze(Exception):
    """The lane stops and says why; a frozen promote is a correct outcome, not a failure."""


def _band(ratio: float) -> str:
    for edge in BAND_EDGES:
        if ratio > edge:
            return {1.5: "late-cycle/peak", 1.2: "elevated", 0.8: "mid-cycle", 0.5: "below-mid"}[edge]
    return "trough"


def load_curves_db(path: Path = CURVES_DB) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def select_print(db: dict, *, today: date | None = None, committed: str | None = None) -> tuple[str, dict]:
    """The newest clean print (status ok, every panel complete) that is NEWER than the
    committed vintage. A flagged parse is never promoted (the 9/02 lesson: an incomplete
    cape panel is a parse failure, not a market move)."""
    today = today or date.today()
    for iso in sorted(db, reverse=True):
        entry = db[iso]
        if entry.get("status") != "ok":
            continue
        if (today - date.fromisoformat(iso)).days > MAX_PRINT_AGE_DAYS:
            break
        if committed and iso <= committed:
            break
        curves = entry.get("curves") or {}
        if all(len(curves.get(p) or {}) == 5 for p in PANELS):
            return iso, entry
    raise Freeze(f"no promotable print: no clean 5-tenor capture for all three panels "
                 f"newer than the committed vintage {committed} within {MAX_PRINT_AGE_DAYS} days")


def read_panel(iso: str, panel: dict) -> dict:
    """Map one panel's OCR keys onto the ruled legs, or freeze on an unruled shape."""
    months = [k for k in panel if k in MONTHS]
    quarters = [k for k in panel if k.startswith(("q", "cal"))]
    if len(months) != 2 or "cal27" not in quarters:
        raise Freeze(f"unruled panel shape {sorted(panel)} — the ruled construction (2026-09-02) "
                     f"expects two month tenors, the next quarter, the following Q1 and Cal-27")
    m1, m2 = sorted(months, key=lambda m: MONTHS.index(m))
    # Straddle test: the front month closes its own quarter and the second month opens the
    # NEXT one, which is the quarter column quoted beside them. Anything else is unruled.
    if MONTHS.index(m1) % 3 != 2 or MONTHS.index(m2) != MONTHS.index(m1) + 1:
        raise Freeze(f"panel {iso} is not the ruled STRADDLING shape (front month {m1} does not close "
                     f"its quarter, or {m2} is not the next month) — a mid-quarter panel needs a word")
    qnext = next((q for q in quarters if q in ("q1", "q2", "q3", "q4") and q != "cal27"
                  and int(q[1]) == (MONTHS.index(m2) // 3) + 1), None)
    qfollow = next((q for q in quarters if q not in (qnext, "cal27")), None)
    if not qnext or not qfollow:
        raise Freeze(f"panel {iso} quarters {sorted(quarters)} do not carry both the next quarter and the following Q1")
    return {"front_month": m1, "q1": panel[m1], "q2": panel[qnext], "q3": panel[qfollow],
            "cal27": panel["cal27"], "legs": (qnext, qfollow)}


def build_class(legs: dict, deltas: tuple[int, int]) -> list[int]:
    """q1..q8 per the ruling: the three read legs, the exact Cal-27 identity, the deltas."""
    q1, q2, q3, cal = int(legs["q1"]), int(legs["q2"]), int(legs["q3"]), int(legs["cal27"])
    rest = 4 * cal - q3                      # q4+q5+q6, so mean(q3..q6) == cal27 exactly
    base, rem = divmod(rest, 3)
    q4, q5, q6 = (base + (1 if i < rem else 0) for i in range(3))
    return [q1, q2, q3, q4, q5, q6, q6 + deltas[0], q6 + deltas[0] + deltas[1]]


def twelve_month(curve: list[int]) -> int:
    """Q-1: the 12M proxy is (q2 + q3)/2, unrounded, half-up to the stored integer."""
    total = curve[1] + curve[2]
    return total // 2 + (total % 2)


def construct(iso: str, entry: dict) -> dict:
    out: dict = {"as_of": iso, "curves": {}, "twelve_month": {}, "legs": {}}
    for panel in PANELS:
        cls = PANEL_TO_CLASS[panel]
        legs = read_panel(iso, entry["curves"][panel])
        out["legs"][cls] = legs
        out["curves"][cls] = build_class(legs, DELTAS_2028[cls])
        out["twelve_month"][cls] = twelve_month(out["curves"][cls])
    out["curves"]["Post-Panamax"] = list(out["curves"]["Pana"])          # shared freight basin
    out["twelve_month"]["Post-Panamax"] = out["twelve_month"]["Pana"]
    out["curves"]["Handy-Bulk"] = [int(round(v * 0.90 / 10.0)) * 10 for v in out["curves"]["Supra-Ultra"]]
    return out                                                            # Handy-Bulk 12M: MB weekly, untouched


def band_check(built: dict, inputs_dir: Path = INPUTS_DIR) -> list[dict]:
    means = (yaml.safe_load((inputs_dir / "market_data" / "historical_tce_means.yaml").read_text())
             or {}).get("historical_tce_means") or {}
    old = (yaml.safe_load((inputs_dir / "market_data" / "twelve_month_tc.yaml").read_text())
           or {}).get("twelve_month_tc") or {}
    rows = []
    for cls, new_tc in built["twelve_month"].items():
        mean = means.get(cls)
        if not mean:
            raise Freeze(f"no historical mean for {cls} — the cycle ratio cannot be checked")
        was, now = old.get(cls, 0) / mean, new_tc / mean
        rows.append({"class": cls, "tc_was": old.get(cls), "tc_now": new_tc,
                     "ratio_was": round(was, 4), "ratio_now": round(now, 4),
                     "band_was": _band(was), "band_now": _band(now),
                     "crossed": _band(was) != _band(now)})
    return rows


def committed_vintage(inputs_dir: Path = INPUTS_DIR) -> str | None:
    d = yaml.safe_load((inputs_dir / "market_data" / "ffa_forward_curve.yaml").read_text()) or {}
    return str((d.get("as_of") or {}).get("Cape") or "") or None


def _set_curve_block(text: str, cls: str, values: list[int], note: str) -> str:
    m = re.search(rf"^  {re.escape(cls)}:[^\n]*\n((?:^\s+#[^\n]*\n)*)((?:^  - \d+\n)+)", text, flags=re.M)
    if not m:
        raise Freeze(f"{cls} block not found in the curve file")
    body = "".join(f"  - {v}\n" for v in values)
    head = m.group(0)[:m.start(1) - m.start()] + f"                     # {note}\n" + m.group(1)
    return text[:m.start()] + head + body + text[m.end():]


def _set_scalar(text: str, block_re: str, cls: str, value) -> str:
    m = re.search(block_re, text, flags=re.M)
    if not m:
        raise Freeze(f"block {block_re!r} not found")
    start, end = m.end(), len(text)
    nxt = re.search(r"^[a-z_]+:", text[start:], flags=re.M)
    if nxt:
        end = start + nxt.start()
    seg = text[start:end]
    seg2, n = re.subn(rf"^(  {re.escape(cls)}:\s*)\S+", lambda mm: f"{mm.group(1)}{value}", seg, count=1, flags=re.M)
    if n == 0:
        raise Freeze(f"{cls} not found under {block_re!r}")
    return text[:start] + seg2 + text[end:]


def apply(built: dict, inputs_dir: Path = INPUTS_DIR, *, today: date | None = None) -> None:
    stamp = (today or date.today()).isoformat()
    note = (f"FFA {built['as_of']} promoted {stamp} by crude_tanker_fv.ffa_promote (ruled construction, "
            f"decisions/ffa_promotion_2026-09-02.md): q1 = front month alone; Cal-27 identity exact")
    cf = inputs_dir / "market_data" / "ffa_forward_curve.yaml"
    text = cf.read_text()
    for cls, values in built["curves"].items():
        text = _set_curve_block(text, cls, values, note if cls in DELTAS_2028 else
                                f"derived from Supra-Ultra x 0.90 (nearest 10) — {note}" if cls == "Handy-Bulk"
                                else f"= Pana (shared basin) — {note}")
        text = _set_scalar(text, r"^as_of:", cls, built["as_of"])
    cf.write_text(text)
    tf = inputs_dir / "market_data" / "twelve_month_tc.yaml"
    text = tf.read_text()
    for cls, tc in built["twelve_month"].items():
        text = _set_scalar(text, r"^twelve_month_tc:", cls, tc)
        text = _set_scalar(text, r"^as_of:", cls, built["as_of"])
    tf.write_text(text)


def packet(built: dict, bands: list[dict], *, today: date | None = None) -> str:
    lines = [f"# Dry FFA promote — the {built['as_of']} print (lane: crude_tanker_fv.ffa_promote, "
             f"{(today or date.today()).isoformat()})", "",
             "Ruled construction (owner 2026-09-02, decisions/ffa_promotion_2026-09-02.md): q1 = the front "
             "month alone (Q-2), q2 = the quoted quarter, q3 = the following Q1, q4-q6 solve the Cal-27 "
             "identity exactly, q7/q8 = the committed 2028 deltas; 12M = (q2+q3)/2 unrounded (Q-1); "
             "Post-Panamax = Pana; Handy-Bulk = Supra-Ultra x 0.90 to nearest 10.", "",
             "## Legs read from the panel", "", "| Class | front month | q1 | q2 | q3 | Cal-27 |", "|---|---|--:|--:|--:|--:|"]
    for cls, legs in built["legs"].items():
        lines.append(f"| {cls} | {legs['front_month']} | {legs['q1']} | {legs['q2']} | {legs['q3']} | {legs['cal27']} |")
    lines += ["", "## Curves written", "", "| Class | q1..q8 |", "|---|---|"]
    for cls, values in built["curves"].items():
        lines.append(f"| {cls} | {' / '.join(str(v) for v in values)} |")
    lines += ["", "## 12M TC proxy and the cycle band (Q-7: a crossing FREEZES the lane)", "",
              "| Class | 12M was | 12M now | move | ratio was | ratio now | band |", "|---|--:|--:|--:|--:|--:|---|"]
    for r in bands:
        move = "n/a" if not r["tc_was"] else f"{(r['tc_now'] / r['tc_was'] - 1) * 100:+.2f}%"
        band = r["band_now"] if not r["crossed"] else f"**{r['band_was']} -> {r['band_now']} CROSSED**"
        lines.append(f"| {r['class']} | {r['tc_was']} | {r['tc_now']} | {move} | {r['ratio_was']} | {r['ratio_now']} | {band} |")
    lines += ["", "Handy-Bulk's 12M TC is untouched (no FFA panel; it rides the MB dry weekly, §11.7.11).", ""]
    return "\n".join(lines)


def run(inputs_dir: Path = INPUTS_DIR, *, apply_it: bool = False, today: date | None = None,
        db_path: Path = CURVES_DB) -> dict:
    db = load_curves_db(db_path)
    committed = committed_vintage(inputs_dir)
    iso, entry = select_print(db, today=today, committed=committed)
    built = construct(iso, entry)
    bands = band_check(built, inputs_dir)
    crossed = [r for r in bands if r["crossed"]]
    if crossed:
        raise Freeze("cycle BAND crossing (Q-7 — the one conjunct that needs the owner's word): "
                     + "; ".join(f"{r['class']} {r['band_was']} -> {r['band_now']} "
                                 f"(ratio {r['ratio_was']} -> {r['ratio_now']})" for r in crossed))
    if apply_it:
        apply(built, inputs_dir, today=today)
    return {"built": built, "bands": bands, "packet": packet(built, bands, today=today),
            "applied": apply_it, "committed_was": committed}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="dry-bulk FFA promote (the ruled construction only)")
    ap.add_argument("--apply", action="store_true", help="write the curve + 12M files (default: packet only)")
    ap.add_argument("--packet-out", type=Path, help="write the packet to this path")
    args = ap.parse_args(argv)
    try:
        res = run(apply_it=args.apply)
    except Freeze as exc:
        print(f"FREEZE: {exc}")
        return 2
    print(res["packet"])
    if args.packet_out:
        args.packet_out.write_text(res["packet"])
        print(f"packet written: {args.packet_out}")
    print("APPLIED" if res["applied"] else "DRY RUN — nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main())

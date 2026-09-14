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


def _span(text: str, top: str) -> tuple[int, int]:
    """The body of a top-level block — class keys are not unique across blocks (`Cape`
    appears under both as_of and the data), so every edit is scoped to one span."""
    m = re.search(rf"^{re.escape(top)}:\n", text, flags=re.M)
    if not m:
        raise Freeze(f"block {top!r} not found")
    nxt = re.search(r"^[a-z_]+:", text[m.end():], flags=re.M)
    return m.end(), (m.end() + nxt.start() if nxt else len(text))


def _comment(first: str, rest: list[str], indent: int) -> str:
    pad = " " * indent
    return f"# {first}\n" + "".join(f"{pad}# {line}\n" for line in rest)


def _set_curve_block(text: str, cls: str, values: list[int], note: list[str]) -> str:
    """Replace the class's values AND its citation comment — a promoted row that keeps the
    prior promote's comment is a citation that no longer describes the value (2026-09-14)."""
    m = re.search(rf"^  {re.escape(cls)}:[^\n]*\n((?:^\s+#[^\n]*\n)*)((?:^  - \d+\n)+)", text, flags=re.M)
    if not m:
        raise Freeze(f"{cls} block not found in the curve file")
    head = f"  {cls}:              " + _comment(note[0], note[1:], 21)
    body = "".join(f"  - {v}\n" for v in values)
    return text[:m.start()] + head + body + text[m.end():]


def _set_twelve(text: str, cls: str, value: int, note: list[str]) -> str:
    start, end = _span(text, "twelve_month_tc")
    seg = text[start:end]
    m = re.search(rf"^  {re.escape(cls)}:[^\n]*\n((?:^\s+#[^\n]*\n)*)", seg, flags=re.M)
    if not m:
        raise Freeze(f"{cls} not found under twelve_month_tc")
    line = f"  {cls}: {value}".ljust(24) + _comment(note[0], note[1:], 24)
    return text[:start] + seg[:m.start()] + line + seg[m.end():] + text[end:]


def _advance_as_of(text: str, top: str, moved: list[str], print_date: str, note: str) -> str:
    """The as_of contract (WO2 1.2, guard tests/test_market_data_vintages.py): every override
    is a HOLD, so it must be <= default. A print NEWER than the default therefore advances the
    default and stamps every class that was riding it with an explicit hold at the old value —
    otherwise the classes this promote never touched would silently claim its vintage."""
    doc = yaml.safe_load(text)
    a, old_default = doc["as_of"], doc["as_of"]["default"]
    riders = [c for c in doc[top] if c not in a]
    start, end = _span(text, "as_of")
    block = text[start:end]
    if str(print_date) > str(old_default):
        block = re.sub(r"^  default:[^\n]*\n(?:^\s+#[^\n]*\n)*",
                       f"  default: {print_date}".ljust(28) + _comment(note, [
                           f"advanced from {old_default}; every class this promote did not touch "
                           f"carries an explicit hold below."], 28),
                       block, count=1, flags=re.M)
        block = block.rstrip("\n") + "\n" + "".join(
            f"  {c}: {old_default}".ljust(28) + f"# held at the prior default ({old_default}) — "
            f"untouched by the {print_date} dry FFA promote\n" for c in riders)
    for cls in moved:
        # value AND comment: an as_of line that keeps the prior promote's note describes a
        # vintage the value no longer has (the same defect as the data rows, 2026-09-14).
        block = re.sub(rf"^  {re.escape(cls)}:[^\n]*\n(?:^\s+#[^\n]*\n)*",
                       f"  {cls}: {print_date}".ljust(28) + f"# {note}\n",
                       block, count=1, flags=re.M)
    return text[:start] + block + text[end:]


def apply(built: dict, inputs_dir: Path = INPUTS_DIR, *, today: date | None = None,
          packet: str | None = None) -> None:
    iso = built["as_of"]
    stamp = (today or date.today()).isoformat()
    packet = packet or f"decisions/ffa_promotion_{stamp}.md"
    src = f"FFA {iso} promoted {stamp} by crude_tanker_fv.ffa_promote ({packet})"
    # Handy-Bulk has NO FFA panel: its curve is DERIVED from Supra-Ultra, but its vintage rides
    # its own MB dry-weekly cadence and this lane must never stamp it (2026-09-14).
    moved = [c for c in built["curves"] if c != "Handy-Bulk"]

    cf = inputs_dir / "market_data" / "ffa_forward_curve.yaml"
    text = cf.read_text()
    for cls, values in built["curves"].items():
        if cls in DELTAS_2028:
            legs = built["legs"][cls]
            d1, d2 = DELTAS_2028[cls]
            note = [f"{src}:",
                    f"q1 = front month {legs['front_month']} {legs['q1']} ALONE (ruling Q-2); "
                    f"q2 = {legs['legs'][0].upper()} {legs['q2']}; q3 = {legs['legs'][1].upper()}-27 {legs['q3']};",
                    f"q4-q6 make the Cal-27 {legs['cal27']} identity exact ({values[3]}/{values[4]}/{values[5]});",
                    f"2028 committed deltas {d1}/{d2}."]
        elif cls == "Post-Panamax":
            note = [f"= Pana, shared freight basin (§11.7.10). {src}"]
        else:
            note = [f"DERIVED = Supra-Ultra x 0.90 to nearest 10 (§11.7.11 locked). {src}.",
                    "Its as_of is NOT stamped here: no Handy FFA panel exists; the vintage rides",
                    "the MB Dry Bulk weekly (§11.7.11)."]
        text = _set_curve_block(text, cls, values, note)
    text = _advance_as_of(text, "ffa_forward_curve", moved, iso, src)
    cf.write_text(text)

    tf = inputs_dir / "market_data" / "twelve_month_tc.yaml"
    text = tf.read_text()
    for cls, tc in built["twelve_month"].items():
        legs = built["legs"].get(cls) or built["legs"]["Pana"]
        text = _set_twelve(text, cls, tc, [
            f"({legs['q2']} {legs['legs'][0].upper()} + {legs['q3']} {legs['legs'][1].upper()}-27)/2 "
            f"= {tc}, unrounded half-up (ruling Q-1).", src])
    text = _advance_as_of(text, "twelve_month_tc", list(built["twelve_month"]), iso, src)
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
        db_path: Path = CURVES_DB, packet_name: str | None = None) -> dict:
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
        apply(built, inputs_dir, today=today, packet=packet_name)
    return {"built": built, "bands": bands, "packet": packet(built, bands, today=today),
            "applied": apply_it, "committed_was": committed}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="dry-bulk FFA promote (the ruled construction only)")
    ap.add_argument("--apply", action="store_true", help="write the curve + 12M files (default: packet only)")
    ap.add_argument("--packet-out", type=Path, help="write the packet to this path")
    args = ap.parse_args(argv)
    try:
        res = run(apply_it=args.apply, packet_name=str(args.packet_out) if args.packet_out else None)
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

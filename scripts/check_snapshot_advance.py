#!/usr/bin/env python3
"""Warn when a fleet-manifest diff looks like a SNAPSHOT ADVANCE without a
report_date bump — the one hole the pair guard is structurally blind to
(stale label + stale-quarter sheet resolve coherently and pass; the SB
2026-07-31 refresh f8809d0 is the observed instance).

A WARNING TOOL, not a gate: the signature (age-basis line change, or a
uniform same-increment shift across many `age:` lines) was fitted on a
single observed true positive, so it earns no enforcement authority —
0/22 false positives on history is the tested half (decision record
2026-08-08 in decisions/q2_cluster_transition_2026-07-31.md). Run it
before committing a manifest edit (WORKFLOWS.md report-day step).

    .venv/bin/python scripts/check_snapshot_advance.py            # vs HEAD
    .venv/bin/python scripts/check_snapshot_advance.py HEAD~3     # vs a ref

Exit 1 on a suspect diff (so `&&` chains stop), 0 otherwise.
"""

import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = "inputs/fleet_manifests/"
# Mid-line match: most manifests carry flow-style vessel rows
# (`- {id: X, class: Pana, age: 13.25, ...}`), so `age:` is rarely at column 0.
# \b keeps `avg_age_*`/`coverage` keys from matching (underscore/letter = word char).
AGE_LINE = re.compile(r"^[-+].*?\bage:\s*([0-9.]+)")
AGE_BASIS_LINE = re.compile(r"^[-+]\s*#.*Ages\s*=", re.IGNORECASE)
REPORT_DATE_LINE = re.compile(r"^[-+]report_date:")
UNIFORM_SHIFT_MIN = 5  # vessels moving by the same increment to call it a shift


def _diff(ref: str) -> str:
    return subprocess.run(
        ["git", "diff", ref, "--", MANIFESTS],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout


def suspects(diff_text: str) -> list[str]:
    out = []
    current = None
    per_file: dict = {}
    for line in diff_text.splitlines():
        if line.startswith("+++ "):
            # `+++ /dev/null` (a deleted manifest) must not attribute its
            # `-` lines to the previous file in the diff.
            current = line[6:] if line.startswith("+++ b/") else None
            if current:
                per_file[current] = {"basis": False, "report_date": False,
                                     "minus": [], "plus": []}
            continue
        if current is None:
            continue
        f = per_file[current]
        if REPORT_DATE_LINE.match(line):
            f["report_date"] = True
        elif AGE_BASIS_LINE.match(line):
            f["basis"] = True
        else:
            m = AGE_LINE.match(line)
            if m:
                f["minus" if line[0] == "-" else "plus"].append(float(m.group(1)))
    for name, f in per_file.items():
        if f["report_date"]:
            continue
        uniform = False
        if len(f["minus"]) >= UNIFORM_SHIFT_MIN and len(f["minus"]) == len(f["plus"]):
            deltas = Counter(round(p - m, 3)
                             for m, p in zip(sorted(f["minus"]), sorted(f["plus"])))
            shift, n = deltas.most_common(1)[0]
            uniform = shift != 0 and n >= UNIFORM_SHIFT_MIN
        if f["basis"] or uniform:
            why = "age-basis line changed" if f["basis"] else \
                f"uniform age shift across {len(f['minus'])} vessels"
            out.append(f"{name}: {why} but report_date did NOT change — "
                       f"if this is a snapshot advance, bump report_date and land "
                       f"the {Path(name).stem}_<quarter>.yaml sheet WITH it")
    return out


def main() -> int:
    ref = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    hits = suspects(_diff(ref))
    for h in hits:
        print(f"SNAPSHOT-ADVANCE? {h}", file=sys.stderr)
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())

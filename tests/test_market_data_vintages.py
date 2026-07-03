"""Machine as_of blocks on the rate files (WO2 1.2) — the structured mirror
of the vintage comments. Two-surfaces rule (2026-07-02): surfaces assumed to
agree get a TEST that they agree — here the as_of maps against their own data
rows and against each other across files."""

from datetime import date
from pathlib import Path

import yaml

MD = Path(__file__).resolve().parents[1] / "inputs" / "market_data"

FILES = [("spot_tce.yaml", "spot_tce"),
         ("twelve_month_tc.yaml", "twelve_month_tc"),
         ("ffa_forward_curve.yaml", "ffa_forward_curve")]


def _as_of(fname):
    return yaml.safe_load((MD / fname).read_text())["as_of"]


def test_as_of_blocks_internally_coherent():
    for fname, top in FILES:
        doc = yaml.safe_load((MD / fname).read_text())
        a = doc.get("as_of")
        assert isinstance(a, dict) and isinstance(a.get("default"), date), \
            f"{fname}: as_of block with a date default is required (WO2 1.2)"
        for cls, vintage in a.items():
            if cls == "default":
                continue
            assert cls in doc[top], f"{fname}: as_of override '{cls}' names no data row"
            assert vintage <= a["default"], \
                f"{fname}: override {cls} ({vintage}) newer than default ({a['default']}) — incoherent"


def test_held_class_sets_agree_across_surfaces():
    """A class held at an old vintage on one rate surface must be held on the
    surfaces that share its determinant event: every ffa_forward hold appears
    held in twelve_month_tc (same tanker/container/gas hold families), and
    spot_tce's holds are a subset of twelve_month_tc's. Empties out cleanly
    when the holds resolve — this pins agreement, not the dates themselves."""
    def holds(fname):
        a = _as_of(fname)
        return {k for k, v in a.items() if k != "default" and v < a["default"]}

    assert holds("ffa_forward_curve.yaml") == holds("twelve_month_tc.yaml")
    assert holds("spot_tce.yaml") <= holds("twelve_month_tc.yaml")

"""Guards on COMMITTED decision documents — the repo ships its outputs.

outputs/*.md are tracked and read by the owner (and the governance repo) as
decision surfaces, so a rendering bug that ships garbage into them is a P1
even when the engine numbers underneath are right. External audit 2026-07-02
F-3: six committed scenario docs carried ~1e29 Assumed/Breakeven ratios (the
breakeven bisection's 50/2^101 lower-bound residue rendered at fixed point).
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_committed_handoff_sign_label_coherence():
    """F-13 semantic guard (2026-07-02): in the COMMITTED handoff JSON, every
    non-void row with a literal position label must have an ev_pct consistent
    with that label under the ONE canonical band (scenarios.position_recommendation,
    ±5%). No BUY below the band, no TRIM/SHORT above it — '+28% upside · SHORT'
    can never ship again. Relabeled rows ('cycle position', 'unreliable read')
    are explicitly non-directional and exempt; a ±0.15pp edge tolerance absorbs
    the JSON's 1-dp rounding (CMBT sits at −5.05)."""
    import json

    path = ROOT / "outputs" / "book_scorecard.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    assert doc["schema_version"] == 2
    offenders = []
    for n in doc["names"]:
        ev, pos = n.get("ev_pct"), n.get("position") or ""
        if n.get("void") or ev is None:
            continue
        if pos.startswith("BUY") and not ev > 5 - 0.15:
            offenders.append(f"{n['ticker']}: BUY at {ev:+.1f}%")
        elif pos.startswith("TRIM/SHORT") and not ev < -5 + 0.15:
            offenders.append(f"{n['ticker']}: TRIM/SHORT at {ev:+.1f}%")
        elif pos.startswith("HOLD") and not (-5 - 0.15 < ev < 5 + 0.15):
            offenders.append(f"{n['ticker']}: HOLD at {ev:+.1f}%")
    assert not offenders, f"sign/label contradictions in the committed handoff: {offenders}"


def test_no_degenerate_ratios_in_committed_scenario_docs():
    """No committed scenario doc may carry an implausible (>100x) rendered ratio.

    The degenerate NAV-covered case must render 'n/a', not the bisection
    residue (see test_breakeven_sensitivity.test_breakeven_degenerate_is_exact_zero).
    """
    offenders: list[str] = []
    for doc in sorted((ROOT / "outputs").glob("*_scenarios.md")):
        text = doc.read_text(encoding="utf-8")
        for m in re.finditer(r"([\d,]+\.\d{2})×", text):
            if float(m.group(1).replace(",", "")) > 100.0:
                offenders.append(f"{doc.name}: {m.group(0)[:40]}")
    assert not offenders, (
        "Degenerate rendered ratios in committed scenario docs (regenerate the "
        f"outputs after the breakeven sentinel fix): {offenders[:6]}"
    )

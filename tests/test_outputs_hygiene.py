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
    the JSON's 1-dp rounding (CMBT sits at −5.05).

    + containment guard (2026-07-15): a printed §9.10 family range must CONTAIN
    the printed point EV — the family includes the adopted weight set, so an
    out-of-range point means the sidecar lags an EV-moving determinant outside
    the WO1-F4 sha scope (TEN +45.0 printed against family max +44.9 after the
    MR mark re-anchor). Remedy: re-run the family diagnostic scripts at the
    current tape, then regenerate the surface from clean HEAD."""
    import json

    path = ROOT / "outputs" / "book_scorecard.json"
    doc = json.loads(path.read_text(encoding="utf-8"))
    assert str(doc["schema_version"]).split(".")[0] == "2"
    # WO1-F1: the COMMITTED decision surface never points at a state that is
    # no commit — dirty stamps are for local scratch surfaces only. (The stamp
    # scopes 'dirty' to the run's determinants, src/ + inputs/; regenerate
    # from a clean tree before committing outputs.)
    assert not (doc.get("source_commit") or "").endswith("-dirty"), (
        "committed book_scorecard.json carries a -dirty source_commit — "
        "regenerate from clean HEAD before committing the surface")
    # WO1-F4: the committed surface's family fields match their determinants —
    # a stale/unstamped sidecar may never ship as current.
    assert (doc.get("weight_family_basis") or {}).get("status") == "current", (
        "committed surface shipped with a non-current weight-family sidecar — "
        "re-run the family diagnostics against the current scenario_inputs.yaml")
    # S-2 coverage guard: every name in a reweighted family must CARRY the
    # sign-stability flag — a null next to a run diagnostic was F-13 in
    # miniature (narrative said '⚠', field said null).
    uncovered = [n["ticker"] for n in doc["names"]
                 if n["sector"] in ("crude", "product", "lng")
                 and n["weight_sign_stable"] is None]
    assert not uncovered, f"reweighted-family names missing weight_sign_stable: {uncovered}"
    # One implementation, two callers (test + sentinel) — scorecard.handoff_coherence_flags.
    from crude_tanker_fv.scorecard import handoff_coherence_flags

    offenders = handoff_coherence_flags(doc)
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

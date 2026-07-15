"""Thread 1 structural guards — uniform prompt-resale age-0 NAV anchor.

See PRE_REGISTRATION_NAV_RESALE_ANCHOR.md. These are the guards that make the
basis fix mechanical (fix the class of error, not the instance):
  - age-0 == dated prompt_resale  (single-source: the two files can't drift)
  - monotone depreciation ordering (guard #1)
  - production-curve depreciation floor (guard #2 — the one that can fire on a
    stale age-0 mark)
  - basis_status covers every curve class with a valid value
"""

import yaml

from crude_tanker_fv.loaders import (
    INPUTS_DIR,
    VALID_BASIS_STATUS,
    load_basis_status,
    load_market_data,
)
from crude_tanker_fv.transactions import (
    apply_transaction_anchored_curves,
    load_all_transactions,
)

# The 9 classes carrying a dated prompt-resale mark (Thread 1 corrected them).
MARKED = (
    "VLCC", "Suezmax", "Aframax", "LR2", "MR",
    "Cape", "Pana", "Supra-Ultra", "Post-Panamax",
)
# Registered guard-#2 floor: production new->5yr depreciation must exceed this.
# Pre-registered at 8% BEFORE the recompute (do not loosen after seeing a number).
DEPRECIATION_FLOOR = 0.08


def _prompt_resale() -> dict[str, float]:
    doc = yaml.safe_load(open(INPUTS_DIR / "market_data" / "newbuild_contract_prices.yaml"))
    return {k: float(v) for k, v in doc["prompt_resale"].items()}


def test_curve_age0_equals_prompt_resale():
    """Single-source invariant: the NAV age-0 anchor IS the dated prompt-resale
    mark for every marked class, so the two inputs can never silently diverge."""
    curves = load_market_data().vessel_value_curves
    resale = _prompt_resale()
    for cls in MARKED:
        assert curves[cls].newbuild == resale[cls], (
            f"{cls}: curve age-0 {curves[cls].newbuild:,.0f} != prompt_resale "
            f"{resale[cls]:,.0f} — the two must stay consolidated"
        )


def test_curve_anchors_monotonic():
    """Guard #1: newbuild >= 5yr >= 10yr >= scrap for every class (ordering)."""
    for cls, c in load_market_data().vessel_value_curves.items():
        assert c.newbuild >= c.five_year_benchmark >= c.ten_year_benchmark >= c.scrap_25yr, (
            f"{cls}: age anchors not monotone decreasing "
            f"({c.newbuild:,.0f} / {c.five_year_benchmark:,.0f} / "
            f"{c.ten_year_benchmark:,.0f} / {c.scrap_25yr:,.0f})"
        )


def test_crude_production_depreciation_floor():
    """Guard #2 (the tripwire): on the PRODUCTION (transaction-anchored) curve,
    new->5yr depreciation must exceed the registered floor for every marked
    class. Fires if an age-0 resale mark is wired implausibly close to the
    transaction-anchored 5yr (the stale-mark failure mode)."""
    md = load_market_data()
    txs = load_all_transactions(INPUTS_DIR)
    prod, _ = apply_transaction_anchored_curves(md, txs)
    for cls in MARKED:
        c = prod.vessel_value_curves[cls]
        dep = (c.newbuild - c.five_year_benchmark) / c.newbuild
        assert dep >= DEPRECIATION_FLOOR, (
            f"{cls}: production new->5yr depreciation {dep:.1%} below the "
            f"{DEPRECIATION_FLOOR:.0%} floor — investigate the age-0 mark or the "
            f"transaction-anchored 5yr (one may be stale)"
        )


# Classes whose age-0 is wired to the xclusiv Resale line (Amendment B). Post-Panamax
# has no xclusiv PPMX (= Kamsarmax replacement); Handysize/Handymax are Group-A pending
# (Thread 1A) — excluded from this guard.
# 2026-07-15 (product_handysize_resource doc): product "Handysize" LEAVES the wired set —
# its Thread-1A wiring asserted equality against what the harvester cache proved is the
# xclusiv BULK row (the guard was enforcing the contamination). "Handy-Bulk" JOINS: the
# renamed extract row is the bulk row, correctly labeled, read directly (alias retired).
# 2026-07-15 (mr_secondhand_resumption doc): "MR" JOINS — xclusiv RESUMED the MR2
# secondhand line in the 2026-07-13 issue; the no-current-line exception is retired.
XCLUSIV_WIRED = ("VLCC", "Suezmax", "Aframax", "LR2", "MR", "Cape", "Pana", "Supra-Ultra", "Handy-Bulk")


def test_curve_age0_equals_xclusiv_resale():
    """The guard that would have caught the original bug: each wired class's age-0
    anchor must equal the xclusiv RESALE line (the just-delivered top of the
    secondhand age curve), NOT the 5-year value. Thread 1 set crude age-0 to the
    5yr price; Amendment B reverts it to Resale and this test locks it."""
    curves = load_market_data().vessel_value_curves
    xcl = yaml.safe_load(open(INPUTS_DIR / "market_data" / "xclusiv_age_curve.yaml"))
    resale = xcl["resale"]
    for cls in XCLUSIV_WIRED:
        want = resale[cls] * 1_000_000
        assert abs(curves[cls].newbuild - want) < 1.0, (
            f"{cls}: curve age-0 {curves[cls].newbuild:,.0f} != xclusiv Resale "
            f"{want:,.0f} ({xcl['report_date']}) — age-0 must be the Resale line, not the 5yr"
        )
    # Negative assertion: age-0 must NOT equal the 5yr (the original mislabel).
    fy = xcl["five_year"]
    assert curves["VLCC"].newbuild != fy["VLCC"] * 1_000_000, "age-0 must not be the 5yr value"


# Every curve class's age-0 basis, explicitly registered. A class absent from this
# map fails the completeness guard below — so a future off-basis age-0 on a "small"
# class (the MR / crude-mislabel re-entry point) cannot slip through silently.
#   xclusiv-resale : age-0 must == xclusiv resale[cls]
#   alias:<cls>    : age-0 must == xclusiv resale[<cls>] (no distinct xclusiv line)
#   exception:<why>: no current xclusiv line to assert against — registered with a reason
AGE0_BASIS = {
    "VLCC": "xclusiv-resale", "Suezmax": "xclusiv-resale", "Aframax": "xclusiv-resale",
    "LR2": "xclusiv-resale", "Cape": "xclusiv-resale", "Pana": "xclusiv-resale",
    "Supra-Ultra": "xclusiv-resale",
    "Post-Panamax": "alias:Pana",        # = Kamsarmax Resale; no xclusiv PPMX line
    "MR": "xclusiv-resale",              # line RESUMED 2026-07-13 (mr_secondhand_resumption doc)
    "LR1": "exception:Group A; MB Tanker 2026-06-26 LR1 NB $64M/5yr $58M (col order verified vs crude inversion), NO Resale line; tool age-0 $59M within ~8% of MB NB (cross-check OK). Kept cross-check NOT wired — MB->calibration is owner-gated + immaterial (no LR1-heavy name).",
    "Handysize": "exception:RE-SOURCED 2026-07-15 (product_handysize_resource doc) — age-0 "
                 "$44.9M = ASC Q1-2026 6-K issuer CONTRACT (acc 0001104659-26-056715: two "
                 "40,500 dwt Handysize at $44.9M/vessel, April-2026; Pareto 2026-04-30 echoes). "
                 "No broker tabulates product-Handy secondhand (xclusiv/MB/Intermodal stop at "
                 "MR, checked 2026-07-15); contract = prompt-resale FLOOR, conservative. The "
                 "prior Thread-1A $36M was the xclusiv BULK row (section-mislabel, corrected).",
    "Handy-Bulk": "xclusiv-resale",     # §11.7.11: reads the committed extract's Handy-Bulk row
                                        # DIRECTLY (renamed from "Handysize" 2026-07-15 — it is
                                        # and always was the bulk row; alias retired).
    "Handymax": "exception:no broker tabulates product-Handymax secondhand; Group A, needs chem-tanker source",
    "LNGC": "exception:non-tanker/dry-bulk sector, own basis",
    "MGC": "exception:non-tanker/dry-bulk sector, own basis",
    "Ctr-Feeder": "exception:container sector, MB China yard basis",
    "Ctr-Intermediate": "exception:container sector, MB China yard basis",
    "Ctr-Large": "exception:container sector, MB China yard basis",
    "VLGC": "exception:LPG sector (WO3 Phase 2, 2026-07-09) — no broker gas resale line in corpus "
            "(xclusiv/Intermodal/Banchero print bulker+tanker only; Advanced prints gas S&P but no age "
            "curve); age-0 = NB-parity $115-120M mid (sec99 print hunt 2026-07-06). Resolve on first "
            "VLGC resale print or the Advanced full-year re-harvest.",
}


def test_every_curve_class_age0_basis_registered():
    """Completeness backstop: every curve class's age-0 is EITHER == the xclusiv
    Resale line (direct or alias) OR an explicitly-registered, reasoned exception.
    A class missing from AGE0_BASIS fails loudly — the guard that stops a future
    off-basis age-0 on a 'small' class (the MR re-entry point) slipping through."""
    curves = load_market_data().vessel_value_curves
    resale = yaml.safe_load(open(INPUTS_DIR / "market_data" / "xclusiv_age_curve.yaml"))["resale"]
    for cls in curves:
        assert cls in AGE0_BASIS, (
            f"{cls}: age-0 basis UNREGISTERED — add it to AGE0_BASIS as xclusiv-resale "
            f"or a documented exception. No class may sit off-basis silently."
        )
        rule = AGE0_BASIS[cls]
        if rule == "xclusiv-resale":
            ref = cls
        elif rule.startswith("alias:"):
            ref = rule.split(":", 1)[1]
        else:  # exception:<reason> — must carry a non-empty reason; no value assertion
            assert rule.startswith("exception:") and rule.split(":", 1)[1].strip(), f"{cls}: bad exception"
            continue
        assert abs(curves[cls].newbuild - resale[ref] * 1_000_000) < 1.0, (
            f"{cls}: age-0 {curves[cls].newbuild:,.0f} != xclusiv Resale[{ref}] {resale[ref]*1e6:,.0f}"
        )
    for cls in AGE0_BASIS:
        assert cls in curves, f"{cls}: in AGE0_BASIS but absent from the curve"


def test_basis_status_covers_curve_classes():
    """basis_status is the single per-class source: every curve class has a valid
    status; the corrected classes are resale-uniform. (MR's registered unverified
    exception RETIRED 2026-07-15 — the flip is loud, via the dated
    mr_secondhand_resumption prereg, not silent: xclusiv resumed the MR2 line.)"""
    status = load_basis_status()
    curves = load_market_data().vessel_value_curves
    for cls in curves:
        assert cls in status, f"{cls} missing a basis_status entry"
        assert status[cls] in VALID_BASIS_STATUS, f"{cls}: bad basis_status {status[cls]!r}"
    for cls in MARKED:
        assert status[cls] == "resale-uniform", f"{cls} should be resale-uniform"

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


def test_basis_status_covers_curve_classes():
    """basis_status is the single per-class source: every curve class has a
    valid status; the 9 marked classes are resale-uniform."""
    status = load_basis_status()
    curves = load_market_data().vessel_value_curves
    for cls in curves:
        assert cls in status, f"{cls} missing a basis_status entry"
        assert status[cls] in VALID_BASIS_STATUS, f"{cls}: bad basis_status {status[cls]!r}"
    for cls in MARKED:
        assert status[cls] == "resale-uniform", f"{cls} should be resale-uniform after Thread 1"

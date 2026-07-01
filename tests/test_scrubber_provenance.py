"""Tier-2 book-wide scrubber-provenance guard (METHODOLOGY §3.1).

`scrubber` is a value-adding equipment flag (+$1.0-2.5M/vessel) with NO build-year rule, so it
must trace to the vessel's own disclosure — never a peer default or a copied-forward claim. The
NEWBUILD rows are guarded strictly in test_newbuild_convention.py; this extends the audit to the
OPERATING fleet, where the same flag adds the same premium across hundreds of vessels.

Three-level severity gradient (the failure, not "aggressive vs lenient"):
  1. CONTRADICTED by disclosure -> HARD fail, everywhere. A verified name whose manifest diverges
     from its audited ledger (the CAPT-class fabrication). Newbuilds: the count check in the NB
     guard. Operating: `test_verified_operating_scrubber_count` below.
  2. UNTRACED on a newbuild -> HARD fail (high fabrication risk, small surface, gates the
     convention queue). In test_newbuild_convention.py.
  3. UNTRACED on an operating row -> xfail-strict (tracked-soft; large surface, low fabrication
     base-rate, gate stays operable). The audit queue below.

The queue xfail is STRICT, and the queue test xpasses (-> fails) if a name is cleared EITHER by
verifying it OR by removing/zeroing its operating scrubber flags. So the queue can only be emptied
deliberately — by tracing the flags to disclosure and updating the registry — never by silently
dropping the inconvenient flag to get a green suite.
"""

import pytest

from crude_tanker_fv.loaders import load_company_inputs, load_watchlist

QUARTER = "2026-Q1"

# name -> verified operating scrubber-fitted COUNT (the contradiction anchor). A name lands here
# only after its operating-fleet scrubber flags are traced to its own disclosure; the count is
# asserted, so a later manifest change that contradicts the audited ledger hard-fails.
OPERATING_SCRUBBER_VERIFIED = {
    "CAPT": 5,   # full Pareto initiation 2026-04-20 per-vessel ledger (all 30 vessels) verified 2026-06-30
    "SB": 20,    # FY2025 20-F (acc 0001628280-26-014408) "21 scrubbers, all 8 Capes" ftn-15 per-vessel; 20 operating at 3/31 (Michalis H HFS). Verified 2026-07-01
}

# Operating-scrubber audit queue: names whose operating-fleet scrubber=true is not yet traced to
# the name's own filing. Each leaves ONLY by verifying it (and moving to OPERATING_SCRUBBER_VERIFIED).
# Likely to clear fast — operating specs are settled public fact (surveys/sales/charters), not
# copied forward-looking claims — but the guard enforces it rather than assuming it.
OPERATING_SCRUBBER_QUEUE = {   # SB left 2026-07-01: scrubber set traced to the FY2025 20-F (ftn-15)
    "DHT", "ECO", "FRO", "GNK", "HAFN", "INSW", "SBLK", "STNG", "TEN", "TRMD",
}


def _has_operating_scrubber(ci) -> bool:
    return any(v.scrubber and not (v.years_to_delivery or 0) for v in ci.fleet.vessels)


def _operating_scrubber_count(ci) -> int:
    return sum(v.count for v in ci.fleet.vessels if v.scrubber and not (v.years_to_delivery or 0))


def _operating_scrubber_names() -> list[str]:
    return sorted(t for t in load_watchlist() if _has_operating_scrubber(load_company_inputs(t, QUARTER)))


def test_verified_and_queue_are_disjoint():
    overlap = set(OPERATING_SCRUBBER_VERIFIED) & OPERATING_SCRUBBER_QUEUE
    assert not overlap, f"names both verified and queued: {overlap}"


def test_every_operating_scrubber_name_classified():
    """Enumeration (clause 3): every name with operating scrubber=true must be EITHER verified or
    queued. A new operating-scrubber name cannot land unclassified — it hard-fails until placed."""
    for name in _operating_scrubber_names():
        assert name in OPERATING_SCRUBBER_VERIFIED or name in OPERATING_SCRUBBER_QUEUE, (
            f"{name}: carries operating scrubber=true but is neither in OPERATING_SCRUBBER_VERIFIED "
            f"nor OPERATING_SCRUBBER_QUEUE — verify it against its filing or queue it; a value-adding "
            f"flag may not sit unclassified."
        )


@pytest.mark.parametrize("name", sorted(OPERATING_SCRUBBER_VERIFIED))
def test_verified_operating_scrubber_count(name):
    """Contradiction-hard (operating): a verified name's operating scrubber-fitted count must equal
    the audited count. A manifest change that diverges from the ledger hard-fails here."""
    got = _operating_scrubber_count(load_company_inputs(name, QUARTER))
    assert got == OPERATING_SCRUBBER_VERIFIED[name], (
        f"{name}: operating scrubber count {got} != audited {OPERATING_SCRUBBER_VERIFIED[name]} — "
        f"the manifest contradicts the verified ledger (re-verify or correct)."
    )


def _queue_param(name: str):
    return pytest.param(name, marks=pytest.mark.xfail(strict=True, reason=f"{name}: operating scrubber not yet traced"))


@pytest.mark.parametrize("name", [_queue_param(n) for n in sorted(OPERATING_SCRUBBER_QUEUE)])
def test_operating_scrubber_traced(name):
    """Operating-soft (clause 3, xfail-strict): an untraced operating scrubber flag is a tracked
    red. The assertion passes — making this a strict XPASS that fails the suite — if the name is
    cleared EITHER by verifying it (into OPERATING_SCRUBBER_VERIFIED) OR by removing its operating
    scrubber flags. Both force a deliberate queue update; neither lets the red clear silently."""
    ci = load_company_inputs(name, QUARTER)
    assert (name in OPERATING_SCRUBBER_VERIFIED) or (not _has_operating_scrubber(ci)), (
        f"{name}: operating scrubber=true not traced to disclosure (audit queue)."
    )

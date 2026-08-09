# The APPROX roster pin — owner ruling 2026-08-09 ("stop enumerating names in the
# workflow prose at all... pin the current expected set in a test").
#
# TWO APPROX SENSES exist in this repo and they collided (MPCC slipped the recapture
# roster for two months because onboarding touched the sector docs, not the prose list):
#   (1) CONSENSUS-PAIR sense — the name is IN the Pareto daily's share-price table but
#       the P/NAV cell is blank: recapture sittings transcribe price + fwd P/E only,
#       pnav stays APPROX-flagged with its own basis note ("flag, don't fake").
#   (2) COVERAGE sense — the name is ABSENT from Pareto's table entirely: sittings
#       leave the FULL static pair at its current vintage (never move a watchlist
#       price against a stale pnav — the TEN $44 lesson).
# The recapture workflow now DISCOVERS sense-1 per sitting from the transcription
# itself; this pin is what makes a silent divergence (a new onboard, a Pareto
# coverage change) a TEST FAILURE instead of two months of stale prose.
# Empirical basis: the 2026-08-07 daily transcription
# (inputs/watchlist_rebase_2026-08-07.yaml.draft, verified against the rendered page).

from crude_tanker_fv.reconcile import APPROX_PNAV_TICKERS

# Sense 1: covered, price + P/E printed, P/NAV blank (the recapture partial-update set).
PARETO_TABLED_NO_PNAV = {"NAT", "ASC", "CCEC", "MPCC"}

# Sense 2: not in Pareto's share-price table at all (the recapture leave-alone set).
PARETO_UNTABLED = {"TEN", "SB", "CMDB", "2343", "GSL"}


def test_approx_set_is_the_union_of_the_two_senses():
    assert APPROX_PNAV_TICKERS == PARETO_TABLED_NO_PNAV | PARETO_UNTABLED, (
        "reconcile.APPROX_PNAV_TICKERS diverged from the pinned two-sense partition — "
        "if a name was onboarded or Pareto coverage changed, move the pin HERE "
        "deliberately (and place the name in the right sense), don't let prose rot."
    )


def test_the_two_senses_are_disjoint():
    assert not (PARETO_TABLED_NO_PNAV & PARETO_UNTABLED)


def test_every_approx_name_is_on_the_watchlist():
    from pathlib import Path
    from crude_tanker_fv.loaders import load_watchlist
    wl = set(load_watchlist())
    missing = APPROX_PNAV_TICKERS - wl
    assert not missing, f"APPROX roster names off the watchlist: {missing}"

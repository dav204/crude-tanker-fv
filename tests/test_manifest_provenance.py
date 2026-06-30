"""General manifest-claim provenance guard.

The DHT catch (2026-06-30) was the existence proof: a manifest line said the fleet was
"100% scrubber-fitted **(confirmed)**" while the cited 6-K says "scrubber" zero times — a claim
carrying the word *confirmed* that the filing did not confirm. "(confirmed)" ≠ confirmed. The
annotation was load-bearing (a future reader, or a guard that trusted the word, would read it as
"done, don't re-check") and it was hollow.

So the clearance bar for any verification CLAIM in a manifest / balance sheet is a *resolvable
citation* — a specific filing, note, broker source, owner attestation, or dated verification —
never the bare word. This guard is field-GENERAL (the defect is "manifest claims lack enforced
provenance", of which scrubber was only the instance under the light): it reds any "confirmed"/
"verified"/"confirms" assertion that does not reference a source. Honest forms — imperative TODOs
("confirm at H1", "VERIFY at…") and negations ("unconfirmed", "unverified") — are not claims and
are exempt. The value-moving FLAGS themselves are covered by the field-specific provenance guards
(test_scrubber_provenance, test_newbuild_convention, AGE0_BASIS); this layer catches hollow
verification CLAIMS in any field.
"""

import glob
import re

import pytest

# Asserting forms (past / 3rd-person). NOT "confirm"/"verify" (imperative TODO) and NOT
# "unconfirmed"/"unverified" (negations) — \b... \b means the "un"-prefixed words don't match.
CLAIM_RE = re.compile(r"\b(confirmed|verified|confirms)\b", re.IGNORECASE)

# A resolvable source reference. A confirmation claim must cite at least one of these — a primary
# filing, a note/accession, a named broker/independent source, an owner/issuer attestation, an
# adversarial-verification marker, or a dated/vintage reference (yyyy-mm-dd or a 4-digit year).
CITATION_RE = re.compile(
    r"6-?k|10-?[qk]|20-?f|note\s*\d|accession|\bpareto\b|xclusiv|clarksons|compass|\bvie\b|"
    r"euronext|newsweb|\bledger\b|\bissuer\b|owner-confirmed|adversarial|\bmb\b|gmail|"
    r"\d{4}-\d{2}-\d{2}|\b(?:19|20)\d{2}\b",
    re.IGNORECASE,
)

_FILES = sorted(
    glob.glob("inputs/fleet_manifests/*.yaml") + glob.glob("inputs/balance_sheets/*.yaml")
)


def test_no_unbacked_verification_claims():
    """Every 'confirmed'/'verified'/'confirms' assertion in a manifest or balance sheet must carry
    a resolvable citation on the same line. A bare claim (the DHT '(confirmed)' case) hard-fails —
    so the word can never again stand in for the source."""
    violations = []
    for path in _FILES:
        if "_template" in path:
            continue
        for lineno, line in enumerate(open(path, encoding="utf-8"), 1):
            if CLAIM_RE.search(line) and not CITATION_RE.search(line):
                violations.append(f"{path}:{lineno}: {line.strip()}")
    assert not violations, (
        "Unbacked verification claim(s) — a 'confirmed'/'verified' assertion with no resolvable "
        "citation (filing / note / broker / owner / date). '(confirmed)' is not a source; add the "
        "reference or rephrase as an explicit pending TODO:\n  " + "\n  ".join(violations)
    )


def test_guard_actually_discriminates():
    """The guard must reject a bare claim and accept a cited one (so it can't silently pass all)."""
    assert CLAIM_RE.search("100% scrubber-fitted (confirmed)")
    assert not CITATION_RE.search("100% scrubber-fitted (confirmed)")          # bare -> would fail
    assert CITATION_RE.search("scrubber-fitted, confirmed per Q1-2026 6-K Note 5")  # cited -> passes


# ---------------------------------------------------------------------------
# NAV-FIGURE provenance (the NAT instance, 2026-06-30). The principle is field-general:
# any manifest figure that MOVES NAV must resolve to a citation; a figure flagged as an
# ESTIMATE (a tilde, "approx", "[ESTIMATE]", "typical", "assumed") is a red regardless of
# whether it is populated — "present but uncited" fails identically to "absent", because for
# a NAV-driver an uncited number is worse than a missing one (the missing one fails loudly,
# the uncited one silently drives a move). Applied first to the §9.6-driving newbuild
# commitment/advance figures, where NAT exposed it and where the convention queue acts.
import glob as _glob  # noqa: E402
import re as _re  # noqa: E402

import yaml as _yaml  # noqa: E402

_ESTIMATE_RE = _re.compile(
    r"~|\bapprox\b|\[est|estimate|\bassumed\b|\btypical\b|placeholder|~equal", _re.IGNORECASE
)
_MONEY_RE = _re.compile(
    r"\$\s?[\d,]+|\b\d+(?:\.\d+)?\s?(?:M\b|bn\b|million|billion)|\b\d{6,}\b"
)
_NB_CTX_RE = _re.compile(r"newbuild|under construction|commitment|advance|instal|capex|\bnb\b", _re.IGNORECASE)

# Names whose §9.6 newbuild commitment/advance figures are estimate-flagged and NOT cited —
# the figure-provenance audit queue. Each clears ONLY by sourcing the real figure (filing /
# 20-F note / dated disclosure) and removing the estimate marker. xfail-strict so a name
# can't leave by deleting the figure either. THIS GATES THE CONVENTION QUEUE: a name here has
# an unsourced commitment, so wiring its newbuilds on-curve (§9.6) would build the NAV move on
# an uncited number — pending-data until sourced.
NB_FIGURE_ESTIMATE_QUEUE = {
    "asc", "brut", "cmbt", "hafn", "nat", "stng", "ten", "trmd",
}


def _nb_figure_estimate_flagged(path: str) -> bool:
    doc = _yaml.safe_load(open(path))
    if not (doc.get("newbuild_capex_commitments") or doc.get("newbuild_advances_paid")):
        return False
    for line in open(path, encoding="utf-8"):
        if (
            _NB_CTX_RE.search(line)
            and _ESTIMATE_RE.search(line)
            and _MONEY_RE.search(line)
            and not CITATION_RE.search(line)
        ):
            return True
    return False


def _nb_balance_sheets():
    out = {}
    for p in sorted(_glob.glob("inputs/balance_sheets/*.yaml")):
        doc = _yaml.safe_load(open(p))
        if doc.get("newbuild_capex_commitments") or doc.get("newbuild_advances_paid"):
            out[p.split("/")[-1].replace("_2026-Q1.yaml", "")] = p
    return out


def test_every_estimate_flagged_newbuild_figure_is_queued():
    """Enumeration: a name whose newbuild commitment/advance is an uncited estimate must be in
    the figure-provenance queue. A NEW such name (the next NAT) hard-fails until placed — so an
    unsourced NAV-driver can never silently enter the on-curve §9.6 wiring."""
    for name, path in _nb_balance_sheets().items():
        if _nb_figure_estimate_flagged(path):
            assert name in NB_FIGURE_ESTIMATE_QUEUE, (
                f"{name}: newbuild commitment/advance is an uncited estimate (tilde/[ESTIMATE]) but "
                f"is not in NB_FIGURE_ESTIMATE_QUEUE — source the figure to a citation, or queue it; "
                f"a NAV-driving figure may not rest on '~'."
            )


def _figq_param(name: str):
    return pytest.param(name, marks=pytest.mark.xfail(strict=True, reason=f"{name}: newbuild figure uncited estimate"))


@pytest.mark.parametrize("name", [_figq_param(n) for n in sorted(NB_FIGURE_ESTIMATE_QUEUE)])
def test_newbuild_figure_sourced(name):
    """xfail-strict figure-provenance queue. Clears ONLY by sourcing the figure (estimate marker
    gone, citation present) — a strict xpass if a queued name is cleared by removing the marker
    or the figure, so the queue can't be emptied by hiding the tilde."""
    bs = _nb_balance_sheets()
    assert name in bs and not _nb_figure_estimate_flagged(bs[name]), (
        f"{name}: newbuild commitment/advance still an uncited estimate (figure-provenance queue)."
    )

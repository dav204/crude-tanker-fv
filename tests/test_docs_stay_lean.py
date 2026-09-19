"""Guard the ALWAYS-LOADED context against re-bloat — "compound-engineering the compounding."

CLAUDE.md is read into the agent's context at the START of every session, so its size is a
RECURRING cost, not a one-time one. The compounding-knowledge habit (append a rule on every
mistake) is monotonically growing by construction, so without a mechanical cap it re-bloats —
which is exactly what happened (357 lines / ~6.2k tokens) before the 2026-07-01 restructure to a
176-line router.

This test makes re-bloat FAIL THE BUILD. When adding a rule would breach the cap you must first,
in order: (1) prefer a GUARD/TEST over prose — a test enforces the rule forever at ZERO context
cost, so reduce the CLAUDE.md rule to a one-line pointer at the test (or drop it); (2) if this is
the Nth instance of a pattern, GENERALIZE the existing rule and DELETE the specifics (the way the
four provenance catches collapsed into one field-general rule + guard); (3) MIGRATE any detail to
a companion (WORKFLOWS / METHODOLOGY / CHANGELOG) and leave a pointer — the narrative NEVER lives
in CLAUDE.md. CHANGELOG/METHODOLOGY/TICKER_NOTES are read on demand, so their growth is cheap; the
cap is only on what's loaded every session.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ~4k-token budget for the always-loaded router (chars ≈ 4× tokens). Current ~14.0k chars / 176
# lines after the 2026-07-01 restructure, so this leaves headroom for a handful of new one-liner
# rules before a compaction pass is forced. Raise this ONLY with a deliberate decision that the
# router genuinely needs to be bigger — the default answer is "compact, don't raise the cap."
CLAUDE_MD_CHAR_CAP = 16_000

# PLAN.md is the handoff EVERY new agent reads after CLAUDE.md, so its size is a recurring cost
# too. F5 (decisions/prune_ledger_2026-09-02.md) ruled it stays under 150 lines; the ruling was
# never executed and the file reached 980, of which a 2026-09-18 audit found roughly three quarters
# was work already finished. The failure mode is specific and worth naming: completion is recorded
# in inputs/forks.yaml, RATIFY_LOG.md and the trigger register, while PLAN kept the REQUEST and
# nobody struck it — so the owner's backlog appeared to grow with every automation that shipped.
PLAN_MD_LINE_CAP = 150
# Dated snapshot blocks stacked newest-on-top were how it grew: nine of them, each saying "read
# this, then the one below". One current-state section, or none.
PLAN_MD_MAX_STATE_INSERTS = 1


def test_readme_status_counts_match_the_watchlist():
    """The README Status block is a hand-maintained counter — exactly the kind
    that rots (said 20 tickers / 378 tests while the repo held 22 / 460; audit
    2026-07-02, F-9). Assert the ticker headline and per-sector split against
    inputs/watchlist.yaml so the block can never silently drift again."""
    import re

    import yaml

    wl = yaml.safe_load((ROOT / "inputs" / "watchlist.yaml").read_text())
    entries = {t: e for t, e in wl.items() if isinstance(e, dict)}
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    m = re.search(r"\*\*(\d+) tickers\*\* across (\d+) sectors", readme)
    assert m, "README Status block lost its '**N tickers** across S sectors' line"
    assert int(m.group(1)) == len(entries), (
        f"README says {m.group(1)} tickers; watchlist has {len(entries)}")
    sectors = {str(e.get("sector") or "crude") for e in entries.values()}
    assert int(m.group(2)) == len(sectors)

    counts: dict[str, int] = {}
    for e in entries.values():
        s = str(e.get("sector") or "crude")
        counts[s] = counts.get(s, 0) + 1
    status = readme.split("## Status", 1)[1]
    for label, key in (("crude", "crude"), ("LNG", "lng"), ("product", "product"),
                       ("dry bulk", "dry_bulk"), ("containerships", "containerships")):
        sm = re.search(rf"{label} \((\d+)", status)
        assert sm and int(sm.group(1)) == counts[key], (
            f"README sector count for {key} does not match the watchlist ({counts[key]})")


def test_claude_md_stays_a_lean_router():
    text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    n = len(text)
    assert n <= CLAUDE_MD_CHAR_CAP, (
        f"CLAUDE.md is {n} chars (~{n // 4} tokens); cap is {CLAUDE_MD_CHAR_CAP} (~4k). It is loaded "
        f"EVERY session — do not grow it to fit a new rule. In order: (1) can a guard/test enforce "
        f"the rule instead? add the test, reduce the CLAUDE.md line to a pointer (or drop it); "
        f"(2) is this the Nth instance of a pattern? generalize the existing rule and delete the "
        f"specifics; (3) migrate detail to a companion (WORKFLOWS/METHODOLOGY/CHANGELOG) and leave "
        f"a pointer. The narrative NEVER goes in CLAUDE.md. Raise the cap only as a deliberate decision."
    )


def test_readme_test_count_claim_tracks_the_suite():
    """audit N-7 (2026-07-14): the '**N+ tests**' README claim is the exact counter
    class whose rot motivated F-9, but it was the one number the F-9 guard didn't
    cover (said 460+ while collection ran 600 — a 26% understatement). Assert the
    claimed floor N against the suite's own static test-function census: N must be
    >= the def-count (collection >= defs, so the claim stays a true floor) and
    <= 1.25x the def-count (so it can't overstate). Adding tests eventually reds
    this until the README floor is raised — by design."""
    import re

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"\*\*(\d+)\+ tests passing\*\*", readme)
    assert m, "README lost its '**N+ tests passing**' line"
    claimed = int(m.group(1))
    defs = sum(
        len(re.findall(r"^def test_", p.read_text(encoding="utf-8"), re.MULTILINE))
        for p in (ROOT / "tests").glob("*.py")
    )
    # 2026-09-02 (prune ledger row 73): the band is now a FLOOR check — the claim
    # must be <= the census (a true "N+") and the census may not run more than
    # 25% above it (the N-7 understatement). Adding tests no longer reds the
    # README; letting the claim rot 25% behind the suite still does.
    assert claimed <= defs <= int(claimed * 1.25), (
        f"README claims {claimed}+ tests; static census is {defs} defs. Keep the "
        f"claim in [{int(defs / 1.25) + 1}, {defs}] — update the README, not this band."
    )


def test_plan_stays_a_handoff_not_an_archive():
    """PLAN.md holds what is still OWED; CHANGELOG.md holds what happened. F5 ruled the 150-line
    cap on 2026-09-02 and nothing enforced it, so the file grew to 980 lines and a new agent's
    "start here" section was ~95% closed history. When this reds: strike the finished lines, move
    dated commitments to inputs/reweight_triggers.yaml, and push narrative to CHANGELOG.md — do
    NOT raise the cap."""
    plan = (ROOT / "PLAN.md").read_text()
    lines = plan.splitlines()
    assert len(lines) <= PLAN_MD_LINE_CAP, (
        f"PLAN.md is {len(lines)} lines against a {PLAN_MD_LINE_CAP}-line cap (F5). Strike what is "
        f"done — the registries already record it — before adding anything."
    )
    inserts = sum(1 for ln in lines if "STATE INSERT" in ln)
    assert inserts <= PLAN_MD_MAX_STATE_INSERTS, (
        f"PLAN.md carries {inserts} STATE INSERT blocks. They stack and never get removed (nine by "
        f"2026-09-18). Keep ONE current-state section and let CHANGELOG.md hold the rest."
    )


def test_plan_points_at_the_registries_rather_than_copying_them():
    """Regenerated state copied into PLAN rots within days: by 2026-09-18 its tier snapshot, its
    opportunity-set counts and its trigger dates all contradicted the files that produce them, and
    it still listed a trigger card folded eight days earlier. The rewritten PLAN names the
    authorities instead."""
    plan = (ROOT / "PLAN.md").read_text()
    for authority in ("inputs/reweight_triggers.yaml", "inputs/forks.yaml",
                      "outputs/book_scorecard.md", "CHANGELOG.md"):
        assert authority in plan, f"PLAN.md no longer points at {authority} as the source of truth"

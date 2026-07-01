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

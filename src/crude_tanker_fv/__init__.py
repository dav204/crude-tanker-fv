"""Crude Tanker Fair Value Tool.

Produces an independent fair value estimate per share for crude tanker
equities by blending two lenses — net asset value (NAV) and a forward
dividend strip — with the blend weight set by cycle position.

See METHODOLOGY.md for the full framework. Module map:

- ``schemas``        — input data structures (METHODOLOGY.md section 4)
- ``loaders``        — YAML input loaders (section 4)
- ``vessel_values``  — vessel market-value curve construction (section 3.1)
- ``nav``            — NAV per share (section 3.1)
- ``dividend_strip`` — forward dividend strip (section 3.2)
- ``cycle``          — cycle-position weighting (section 2.3)
- ``blend``          — blended fair value (sections 2.1–2.2)
- ``breakeven``      — implied breakeven TCE (section 3.3)
- ``sensitivity``    — 5x5 sensitivity grid (section 3.4)
- ``report``         — per-company report + watchlist roll-up (section 7)
- ``pipeline``       — orchestration / build order (section 8)
"""

__version__ = "0.1.0"

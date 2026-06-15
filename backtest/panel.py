"""Curated wide shipping panel for Amendment 1.

Only USD-listed names with real published Pareto P/NAV (returns must be
currency-consistent — Yahoo adjusted close, USD). Oslo/EUR-only names
(AWILCO, BWLP, DIS, ODFB, SNI, MPCC) are excluded by the USD filter and noted
in the report. Sector labels are curated here, auditable; INSW (crude+product
hybrid) is filed crude per the repo's primary-sector treatment.

  ticker -> (yahoo_symbol, sector)
"""

PANEL: dict[str, tuple[str, str]] = {
    # crude
    "DHT":  ("DHT",  "crude"),
    "FRO":  ("FRO",  "crude"),
    "ECO":  ("ECO",  "crude"),
    "TNK":  ("TNK",  "crude"),
    "INSW": ("INSW", "crude"),
    "CMBT": ("CMBT", "crude"),     # CMB.TECH, NYSE; P/NAV only from 2025-12
    # product
    "STNG": ("STNG", "product"),
    "TRMD": ("TRMD", "product"),   # TORM, Nasdaq USD
    "HAFN": ("HAFN", "product"),   # Hafnia, NYSE USD (listed 2024)
    # dry bulk
    "SBLK": ("SBLK", "dry_bulk"),
    "GNK":  ("GNK",  "dry_bulk"),  # P/NAV from 2025-03
    "HSHP": ("HSHP", "dry_bulk"),  # Himalaya, capesize
    # lng
    "GLNG": ("GLNG", "lng"),       # Golar
    "FLNG": ("FLNG", "lng"),       # Flex LNG, NYSE USD
    # lpg
    "LPG":  ("LPG",  "lpg"),       # Dorian
    "NVGS": ("NVGS", "lpg"),       # Navigator; P/NAV from 2025-12
}

SECTOR_OF = {t: s for t, (_, s) in PANEL.items()}
YAHOO_OF = {t: y for t, (y, _) in PANEL.items()}

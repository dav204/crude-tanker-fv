# Methodology question — pure-product names read the DIRTY LR2/LR1 lines

Opened 2026-09-14 by fork `stage_b_open_items` (item 3 of
`decisions/stage_b_promotion_2026-09-09.md` §6), which directed a note and **no promotion**.
This is a question, not a change. Nothing in any rate file moves until it is ruled.

## The finding

Stage B's §4 routing work surfaced that **pure-product names bypass the clean-rate remap**: a
name whose fleet is entirely product tonnage reads the DIRTY `LR2` / `LR1` rate lines rather
than the `LR2_clean` / `LR1_clean` lines, because routing is decided per CLASS, not per name's
trade. The clean lines exist and carry their own committed values (Stage B 2026-09-09:
`LR2_clean` 57,128 / 51,500 / 29,500 and `LR1_clean` 32,608 / 37,000 / 21,350 against dirty
`LR2`/`LR1` at the Aframax-shaped 81,000 / 56,000 / 40,000).

## Why it is not obviously a bug

The dirty and clean lines are not two estimates of one rate. They are two different trades, and
the war-era spread between them is itself a documented feature (Stage B open item 2: the
D-3 war-inverted clean/dirty term ratio survives — LR2 clean term 29,500 against dirty 40,000).
A name carrying LR2 hulls may trade them dirty, clean, or switch; the manifest records the hull
class, not the cargo it is carrying this quarter. Routing every pure-product name to the clean
line would assume a trade the manifest does not assert.

## What a ruling has to decide

1. Is the routing key the CLASS (as today) or the NAME's disclosed trade?
2. If the name's trade: what is the evidentiary standard — the issuer's own description of its
   fleet employment, or a per-vessel disclosure?
3. What happens to a name that switches, and does the switch re-vintage its rate basis?
4. Blast radius: which names change, and by how much, before anything is promoted.

## Standing

No owner action is owed. It sits here until someone rules it or a refresh forces the question.
The names affected are the pure-product set; the crude, dry-bulk, gas and container sleeves are
untouched by it.

---
name: numbers-carry-units
description:
  "Write like a professional engineer: every quantity value carries its unit, a space between
  number and unit, in conversation as well as in documents."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-09-04T15:10:51.395Z
---

Communicate the way a professional engineer does: a reader must be able to tell what a number
measures without hunting for it. Attach the unit to the value, with a space between: `3 mm`, not
`3mm` and not a bare `3`.

This applies to **conversation with the user (Mike), not only to committed files**. No check runs on
chat output, so this memory is the only thing enforcing it there. The document half is enforced by
the units rule in `.claude/rules/parts/prose-style.md`; see [[one-fact-one-home]] and do not
restate it
elsewhere.

What the rule covers:

- **Ranges and tolerances carry the unit on both parts** — `0.15 mm to 0.45 mm`, `10 mm × 20 mm`,
  `25 mm ± 2 mm`. This follows NIST SP 811 rather than the looser habit of putting it once at the
  end.
- **A symbol's value carries it every time**, however often the symbol was defined: `t = 0.05 mm`.
  A symbol inside an equation is bare, because it is not a value: `3.414 t` is correct.
- **Hoisting is allowed where it governs a whole set** — a column header `Length (mm)` or an axis
  label `Force / N` — and the unit MUST then appear there. Repeating `mm` down forty rows is noise.
- **Bare numbers are for what has no unit**: counts, indices, revisions, ratios, coefficients and
  other dimensionless quantities.
- **Drawings in this repo do not hoist**; every dimension carries its unit on the sheet. See
  [[drawing-conventions]].

**Why:** a bare quantity value reads as an error to an engineer, and it is unrecoverable for a
reader who was not present when the unit was last stated. The user (Mike) asked for this after
finding bare values throughout an analysis I gave him.

**How to apply:** the misses are predictable and are not in running prose. Check table columns,
axis labels, and any symbol being reused after its definition; those are where I drop units. Pair
it with significant figures: do not quote `8.8387 mm` in prose when the printed part is held to
hundredths of a millimeter, even where the value is exact inside `make_plans.py`.

---
name: modeling-practice
description:
  "The design-intent standard every reference model must meet: the first sketch on the origin,
  every later sketch anchored to geometry that already exists, variables only where the build
  plan asks for them, and the acceptance test that changing a driving dimension reproportions
  the model rather than breaking it. Read before building or fixing a reference model."
---

# Modeling practice — design intent

This is the standard every model in this project must meet. It is also the standard the current
reference model **fails**, which is why this file exists.

## The standard

A model encodes *why* geometry sits where it does, not merely where it sits. Concretely:

- **The first sketch is a center point rectangle on the origin.** Symmetry becomes structural
  rather than arithmetic — you never type the same number twice with opposite signs.
- **Every later sketch is anchored to something that already exists.** Use **Use (Project/Convert)**
  (`u`) to pull an existing edge into the sketch, then tie to it with **Coincident** (`i`),
  **Collinear**, **Equal**, **Symmetric**, or **Tangent**.
- **Named variables come from the build plan's Variables table and nowhere else**, not from
  wherever a number repeats. A model uses the rows that table holds, under the names it gives them,
  and invents none of its own. The table names them for what they mean — `#bodyW`, `#bodyH`,
  `#eyeR`, not `#d1` — and a model that wants one the table lacks asks for a row rather than
  adding a variable.
- **Every sketch is fully defined (black) before it is extruded.**
- **Mirror rather than draw twice.** A second leg produced by an in-sketch mirror about the
  vertical axis is related to the first; a second rectangle typed at negative coordinates is not.

**The acceptance test is not "the render looks right".** It is two things:

1. Every sketch reports **fully defined**.
2. Changing one driving dimension — a variable where the part has one, the dimension itself where
   it does not — produces a correctly proportioned model rather than a pile of disconnected parts.

## What the current reference model does instead

All ten sketches in the first taught-path model were emitted with `constraints: []` and every
coordinate as an absolute literal in world space.

- The eye circles are not symmetric about anything. They are two independent circles that happen
  to sit at x = ±1.9.
- The legs do not touch the body because they are constrained to it. They touch because `z = 3`
  was typed twice.
- Nothing references anything else. Change the body width from 8 to 10 and every other number in
  the model is silently wrong.

This is worse than merely under-defined. Under-defined geometry can still be *related*; this is
under-defined **and** magic-numbered, which is the worst of the two.

## Why it happened, and the rule that follows

The Onshape REST API makes raw geometry trivial to emit and constraint webs laborious. The model
drifted toward what was easy to POST.

> **Never let the tool dictate the pedagogy.** When a scripting path makes the wrong practice cheap
> and the right practice expensive, that is a reason to spend more effort, not a reason to ship the
> cheap thing.

This matters more here than on an ordinary model, because the deliverable is a class about learning
to CAD. A reference built from magic numbers teaches the exact habit the course exists to prevent,
and it teaches it invisibly, because it looks correct.

## What the constrained version looks like

| Element | How it should be tied down                                                              |
| ------- | ---------------------------------------------------------------------------------------- |
| Body    | Center point rectangle on the origin; two dimensions `#bodyW`, `#bodyH`                  |
| Legs    | One leg drawn, top edge **Collinear** with the projected body bottom edge; second leg by in-sketch **Mirror** |
| Arms    | Inner edge **Coincident** with the projected body side; height dimensioned from the body top edge |
| Hands   | Half-disc flat edge **Coincident** with the arm's end edge, centered on its **midpoint**  |
| Eyes    | Two circles with an **Equal** radius constraint and **Symmetric** about the vertical axis |
| Teeth   | Top edge **Coincident** with the grin's top edge; symmetric about the vertical axis       |

Then `#bodyW = 8 → 12` widens him correctly — and that demonstration teaches design intent far
better than any explanation of it.

## Note for the course itself

The variable-change demo is worth building a session moment around. Changing one number and
watching the model update is, for most students, the point at which CAD stops being drawing and
starts being modeling. Put it somewhere on purpose.

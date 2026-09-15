---
name: limbs-are-twelve-mm-cylinders
description:
  "Robot limbs are Ø12 cylinders and the joints are designed to fit inside them; settled
  2026-08-11, do not reopen."
metadata: 
  node_type: memory
  type: project
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-12T21:34:49.864Z
---

Every limb of the 150 mm robot is a **Ø12 mm cylinder** (`#limbD` = `#torsoH / 4`). Settled
2026-08-11 after the limbs went to Ø16 and came back. **The joints are sized to fit inside the
limb, never the limb grown to fit a joint.**

The reasoning worth keeping: the first hinge did not fit because nobody checked that a flat
clevis paddle's **diagonal** must fit the rod, √(w² + t²) ≤ 12. The root cause was that the
joint had been scaled off the torso — a fraction of 48 — instead of off the 0.4 mm nozzle. A
6 mm blade is fifteen extrusion widths for a hinge this small. Redesigned from the nozzle up,
ears became exactly three perimeters. The later slice design removed the constraint entirely by
letting every layer of the fork run out to the Ø12 arc, so there is no rectangle and no corner.

**The trap:** the build plan's Stage 5 lists four *teaching routes* for the limbs — sloppy
quadrilateral, ellipse, loft, filleted box — chosen so each limb teaches a different tool. These
are not section specifications. Reading them as dimensions and inventing sections (a 14 × 10
ellipse) contradicts the Ø12 decision and manufactures wall-thickness problems that do not
exist.

Related: [[cad-models-need-design-intent]] — `#armX` and `#legX` are computed from `#limbD/2`,
so the limb's radius is load-bearing in the layout and a changed section silently breaks the
stated relation that the legs' outer surfaces land on the torso's sides.

**Check the session logs before calling a design question open.** This one was decided in
conversation and lives in no single file.

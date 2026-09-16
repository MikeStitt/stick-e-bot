# The project, and where it currently stands

The audience is deliberately wide — middle-schoolers who have never opened CAD through to
high-schoolers with some Fusion or TinkerCAD behind them. That is why every session needs a floor
and a ceiling.

This repository holds the **text**: session plans, step-by-step instructions, rubrics, and the
registry of reference documents. The models live in Onshape.

## The live Onshape documents

Owned by Mike Stitt (not the Spires Robotics team space).

## Status

Done and verified:

- The reference model builds 22/22 `OK`, and its geometry is confirmed by bounding box rather than
  by status code. Nine parts, classified from their bounding boxes and colored.
- The build and capture pipeline is committed, not living in a scratchpad.
- The GUI vocabulary in [`taught-path.md`](experiments/taught-path.md) is read from the live UI,
  not recalled — including the correction that the extrude flip is an arrow button, not the
  Direction checkbox.

Open:

- **The reference model has no constraints.** Every sketch is absolute coordinates. This remains
  the significant outstanding problem — see
  [`modeling-practice`](../.claude/skills/modeling-practice/SKILL.md). The encoding needed to fix it
  is now known, so this is work rather than research.
- No reference-document links are recorded in `README.md` yet; the table there is still `TODO`
  placeholders. The IDs above are the raw material for filling it in.
- Per-session folders under `.parts/session-<N>-<slug>/` do not exist yet, and how they reconcile
  with the generated guide is undecided.
- Nobody has walked the click-path. A script did.

# The project, and where it currently stands

## What we're building

A four-session, eight-hour introduction to CAD. Students model a 150 mm articulated robot figure
in Onshape, starting from never having opened a CAD tool. The figure is a vehicle: thirteen
joints of two kinds, built from blocks, rods and pockets, which is to say it is sketch, extrude,
revolve and fillet in roughly the order you'd want to learn them — and then assembly mates, which
the sponge had nowhere to teach. See [`robot-build-plan.md`](robot-build-plan.md).

The audience is deliberately wide — middle-schoolers who have never opened CAD through to
high-schoolers with some Fusion or TinkerCAD behind them. That is why every session needs a floor
and a ceiling.

This repository holds the **text**: session plans, step-by-step instructions, rubrics, and the
registry of reference documents. The models live in Onshape.

## The live Onshape documents

Owned by Mike Stitt (not the Spires Robotics team space).

**`CAD Class — SpongeBob reference`** — the one that matters.
`experiments/spongebob-guide/model.py` builds it and the capture pipeline rebuilds it on every
run, so it is *generated*, not hand-maintained. Editing it by
hand will be undone by the next `make all`.

| Thing        | ID                         |
| ------------ | -------------------------- |
| Document     | `50ac6c40b6437e06a2d0a515` |
| Workspace    | `78d3b986d158fc34e0937e8b` |
| Part Studio  | `8802a808a7dd9b07da9ad6dc` |

Three older documents are debris from earlier work and can be deleted once nothing points at them:

| Document                        | ID                         | Why it exists |
| ------------------------------- | -------------------------- | ------------- |
| `SpongeBox - Blocky SpongeBob`   | `c18297d7aedf651093678b34` | First taught-path model, plus a FeatureScript version built as a capability probe |
| `CAD Class — Extrude 1 capture` | `2d671812bce4f3be440184d1` | The single-step experiment |
| `CAD Class — scratch`           | `ffc2e89592db8d63cb0eda42` | Where the sketch-constraint encoding was worked out |

The FeatureScript version in the first of those does **not** satisfy the Constitution's "built the
taught way" requirement — a student who opens that tab sees one opaque feature instead of 22. It was
never meant for the classroom.

## Status

Done and verified:

- The reference model builds 22/22 `OK`, and its geometry is confirmed by bounding box rather than
  by status code. Nine parts, classified from their bounding boxes and colored.
- **The student guide covers the whole taught path** — four session pages, 38 documented steps, 38
  annotated screenshots taken from the live UI. See
  [`experiments/spongebob-guide/`](experiments/spongebob-guide/README.md).
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

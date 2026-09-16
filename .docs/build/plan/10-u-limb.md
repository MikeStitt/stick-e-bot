# 10. The upper limb

Starts from two finished joints. Ends with a limb carrying a socket at one end and a fork at the
other.

**This is the tutorial where the robot's shape becomes obvious.** A limb is a Ø12 cylinder with a
joint on each end, and both joints already exist. Almost nothing here is new geometry — it is
derive, place, union, four times over with the parts swapped.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.u_limb.tab` | a Part Studio of its own, named `u limb` | the tab |
| `cad.parts.u_limb.socket.derive` | bring the socket in first, where it belongs | `add socket` |
| `cad.parts.u_limb.section_sketch` | the limb's circle, drawn on the socket | `limb section` |
| `cad.parts.u_limb.body` | extrude it `#limbCenter - #collar - #ear_free` long | `limb` |
| `cad.parts.u_limb.fork_connector` | where the fork goes, on the limb | `mate for fork` |
| `cad.parts.u_limb.fork.derive` | bring the fork in | `add fork` |
| `cad.parts.u_limb.fork.place` | onto its connector | `move fork` |
| `cad.parts.u_limb.combine` | union all three | `combine parts` |
| `cad.parts.u_limb.rename` | call the part `u limb` | |
| `cad.parts.u_limb.shoulder_connector` | the end that mates to the shoulder | `shoulder end` |
| `cad.parts.u_limb.elbow_connector` | the end that mates to the elbow | `elbow end` |

**This tab declares no variable of its own.** It reads `#limbD` and `#flat` for the section and
`#limbCenter`, `#collar` and `#ear_free` for the length, and all five are `robot sizes` rows by the
time this tutorial starts — `#limbD` from tutorial 6 and the rest from tutorial 9. The table used
to carry a `cad.parts.u_limb.variables` step declaring `#limbD` here, which would have shadowed the
studio's row; [`onshape`](../../../.claude/skills/onshape/SKILL.md) § *Modeling standards* is
what that breaks.

**One joint is derived into place and the other is moved onto a connector, and that asymmetry is
the reference's, not an oversight.** The socket comes in first at the origin, the limb's circle is
sketched on it, and the extrude runs away from it — so the socket never needs a connector or a
Transform. Only the far end does. Building it the other way, with a connector and a move for each
joint, reaches the same part through two extra features and puts a number where a pick would do.
[`../../experiments/runs/2026-08-29-draft9p3/reference/u-limb.json`](../../experiments/runs/2026-08-29-draft9p3/reference/u-limb.json)
is the order this table now follows.

**`Mate connector 1` and `Mate connector 2` are not names.** They become `shoulder end` and
`elbow end`, and the assembly picks them by those names.

**The part is renamed, and a step table built by reading a feature tree cannot see that.** Renaming
a part happens in the parts list and is never a feature. 9p1p1 calls this one `u limb`, and the
assembly's instances carry that name four times over.

**`#limbCenter` drives the length.** Stickbot has 35.42 typed here and 37.91 in the lower limb,
with no variable anywhere. The Variable Studio built in tutorial 1 is what this step spends, and it
spends it on **`#limbCenter - #collar - #ear_free`, 17 mm**. The rod is what is left of the 48 mm
between joint centers once the two joints have taken their share: the socket's ball center is
`#collar` 10 mm above the face the rod starts on, and the fork's slot is rooted `#ear_free` 21 mm
past the face the rod ends on. Neither typed number is 48 or half of it, so there is nothing to
carry across; build the expression.

**`#ear_free` is `#slot_deep - #nose`, and it is not `#limbD / 2`.** This page carried
`#limbD / 2` = 12 mm, which is where the ear's round end reaches and not where its slot is rooted.
A rod built to the round end runs 9 mm too far and fills the slot back in, and the joint is then a
different joint that looks the same. [`09-hinge.md`](09-hinge.md) has the rest of it.

**Stickbot calls them `Limb section` and `Limb`.** Lowercase, like every other feature.

## What changes from stickbot, and what it costs

**draft9p0 sat its joints on the end faces, and the sheet buries them.** Its extrude was 48 long,
the socket then stood 7.4 off one end face and the fork 45 off the other, and the segment measured
**100.4** between centers where the sheet said 48. That looked like a disagreement about the
number. It was a disagreement about placement: `clevis()` draws the fork's root 21 mm back from the
pin and inside the rod, and `make_plans.py:87` says it in words — each joint takes about 21 mm of
the segment it ends. Stack them instead of burying them and every one of their reaches is added to
the stock, which is where 100.4 came from.

**Stickbot has the same disagreement, about a twelfth the size.** Measured read-only on 2026-08-24,
its `u limb` is 35.42 long with **28.26** between centers, against a 1× sheet that said 24 — an
overshoot of 4.26. draft9p0 overshoots by 52.4.

**It is settled: `#limbCenter` is the center distance, and this page's number is 27.** The rod is
extruded 27 down from the collar's underside, and the fork is landed on the rod's far end so that
its ears reach `#limbD / 2` further. What comes out is 9 + 27 + 12 = 48 between centers, and the
fork's arm ends up buried inside the rod rather than sitting on it. draft9p1 wrote 53 here, which
was the same idea with the socket placed differently; 9p1p1 is what draft9p3 builds. Recorded in
[`../../experiments/runs/2026-08-25-draft9p1/a1-limb-center.md`](../../experiments/runs/2026-08-25-draft9p1/a1-limb-center.md).

## The shots this tutorial needs by name

**Requirements in play.** `req.model.derive` — the joint is brought in from the studio that
owns it, never resketched here.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the limb, both joints on | `req.page.hero` |
| `#limbCenter - #collar - #ear_free` resolving in the extrude's depth field | the second payoff of the Variable Studio, and the one a student can change | |
| each of the two derives, as arrived | shorter than the head's arc by now | |
| each transform's two connectors, medium and close-up with a ring | four picks | `req.shot.two_frame` |
| the two end connectors, medium and close-up with a ring | these are what the assembly will pick, so they have to be recognizable | `req.shot.two_frame` |
| the tree, the version dialog | | |

## What we do not know yet

**Whether the two derives can be shown side by side.** Socket at one end and fork at the other is
one picture if the limb fits in frame at a useful zoom, and two if it does not.

**Whether this tutorial and the next should be written as one page with a difference section.**
The lower limb is the same eleven moves with a ball stud and a blade instead of a socket and a
fork. Two nearly identical pages is a lot of reading for one idea. See
[`11-l-limb.md`](11-l-limb.md).

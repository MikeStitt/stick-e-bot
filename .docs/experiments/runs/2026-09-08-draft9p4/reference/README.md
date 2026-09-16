# The reference construction

**How `stickbot-draft9p1p6` is built, read off the model itself and off nothing else.** draft9p4
teaches this model, so a take follows what is here and the check document is diffed against it. A
part that reaches the right shape by a different construction is a finding, not a pass.

The reference is `stickbot-draft9p1p6`, document `500752af84dc92deea53f9e4`, workspace
`f30bf96cfeece59f61e0e7b2`. Every file here was read at version `80c22eb7b8b0342ac03f8a6d`, which is
the version draft9p1p6's register published. It is read only.

## Why the version and not the workspace

The workspace sits at microversion `1009393f43c6384ece39b921` and the published version at
`dd821b5b9c8498eb568aee67`, so something touched the workspace after the version was cut. All five
tabs' feature lists are identical across the two, which means the bump was not a change to the
model. Reading the version gives a record that cannot move under a later edit, and the register's
numbers describe the same construction.

## What each file holds

| File | What it is |
| ---- | ---------- |
| `robot-sizes.features.json` | 23 features, all of them variables |
| `variables.json` | the 23 rows of `robot sizes` as Onshape resolves them, with values |
| `ball-and-socket.features.json` | 14 features |
| `ball-and-socket.faces.json` | 22 faces, each with its surface type, radius, axis and area |
| `ball-and-socket.geometry.json` | 3 sketches, with every entity and every constraint |
| `hinge.features.json` | 46 features |
| `hinge.faces.json` | 510 faces |
| `hinge.geometry.json` | 10 sketches |
| `u-limb.features.json` | 9 features |
| `u-limb.faces.json` | 270 faces |
| `u-limb.geometry.json` | 1 sketch |
| `l-limb.features.json` | 9 features |
| `l-limb.faces.json` | 260 faces |
| `l-limb.geometry.json` | 1 sketch |

[`../scripts/p0_read.py`](../scripts/p0_read.py) wrote them. The face files come through
[`../../../../tools/read_shape.py`](../../../../tools/read_shape.py) and the geometry files through
[`../../../../tools/read_sketches.py`](../../../../tools/read_sketches.py).

## What is in these files that draft9p3's record did not have

draft9p3 recorded each feature's name, its place in the order, and what it was built on. This record
carries that and three things more.

- **Every parameter of every feature, with its expression.** An extrude's end condition, its second
  direction, and the variable its depth names.
- **Every sketch entity and every constraint.** `blade profile` is 4 entities held by 11 constraints,
  and the record says which 11.
- **Every face of every part.** Surface type, radius, axis and area, which is what proves a shape
  without trusting a feature name.

## What a feature stores that it is not using

Onshape keeps a value on every parameter a feature could have, switched on or not. An extrude that is
neither drafted nor offset still carries `draftAngle 3 deg`, `offsetDistance 25 mm` and
`secondDirectionDepth 25 mm`. A transform that moves a part to a mate connector still carries
`distance 25 mm` and `angle 30 deg` from the translate and rotate options it is not using. Reading
those as though a builder typed them buries the numbers a builder did type.

The switch that matters is beside the value. An extrude's depth is live when `endBound` is `BLIND`; a
revolve's angle is dead when `fullRevolve` is true; a transform's distance is live only when
`transformType` is `TRANSLATION_DISTANCE`.

A sketch dimension is the same story. Its value is the `length` or `angle` parameter.
`labelRatio` and `labelAngle` place the label on the screen, in radians and meters, and are not the
dimension.

[`../scripts/typed_numbers.py`](../scripts/typed_numbers.py) reads the record through those switches
and prints the two tables below.

## Where draft9p1p6 types a number

Twenty-four numbers in the whole reference are typed. Everything else is derived from one of them.

**`robot sizes`, 11 typed of 23 rows.**

| Row | Value |
| --- | ----- |
| `#torsoH` | 96 mm |
| `#torsoW` | 72 mm |
| `#torsoD` | 48 mm |
| `#limbCenter` | 48 mm |
| `#fit` | 0.08 mm |
| `#ballLoss` | 0.10 mm |
| `#t_print` | 0.10 mm |
| `#blade` | 10 mm |
| `#wedge_h` | 0.75 mm |
| `#wedge_c` | 0.15 mm |
| `#blade_out` | 32 mm |

**`ball and socket`, 1 typed.** `#slit` at 1.6 mm.

**`hinge`, 12 typed.**

| Feature | What is typed |
| ------- | ------------- |
| `#stub` | 4 mm |
| `#leaf_root` | 4.20 mm |
| `#leaf_tip` | 1.50 mm |
| `#wedges` | 24 |
| `#ring_in` | 6.00 mm |
| `blade wedge` | draft angle 45 deg |
| `blade wedges` | pattern angle 360 deg |
| `fork blade top cut outline` | three dimensions at 2 mm |
| `ear wedge` | draft angle 45 deg |
| `ear wedges` | pattern angle 360 deg |

**`u limb` and `l limb`, none.** Both tabs derive every number they use, and their one sketch each is
fully driven.

## Numbers typed inside an expression that otherwise derives

A ratio is how one size is built from another. A length added to a variable is a typed size wearing
an expression, and it is worth seeing in the same list.

| Tab | Row | Expression |
| --- | --- | ---------- |
| `robot sizes` | `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball - #ballLoss) ^ 2)` |
| `robot sizes` | `#slot_deep` | `#blade_out + 1 mm` |
| `hinge` | `#stub_proud` | `2 * #wedge_h + 1.50 mm` |
| `hinge` | `#bore_d` | `#stub + 0.1 mm` |

Two more rows match the same search and are not the same thing. `#wedge_eps` ends in `* 1 rad`,
which converts a ratio into an angle, and `#wedge_w` starts from `180 deg / #wedges`, which is a half
turn shared out. Neither is a size somebody chose.

## The two variable naming conventions in `hinge`

A variable is a feature, so it has a feature name as well as a variable name. Onshape's default
feature name for one is the literal string `###name = #value`. Renaming the feature to the variable's
own name makes the tree readable; leaving it makes eight rows in a row that all read alike.

`hinge` does both, and this is how it stands:

- **Renamed, 8 rows.** `#nose`, `#ear`, `#stub`, `#stub_proud`, `#bore_d`, `#slit_h`, `#rod_blade`,
  `#rod_fork`.
- **Left at the default, 10 rows.** `#leaf_root`, `#leaf_tip`, `#wedges`, `#ring_in`, `#ring_out`,
  `#wedge_bind`, `#wedge_inset`, `#wedge_eps`, `#wedge_w`, `#backlash`.

The split follows the drafts. The renamed eight came in at draft9p1p4 or earlier; the ten defaults
are the wedge ring, added at draft9p1p5 and draft9p1p6.

`ball and socket` renames all 5 of its rows. `robot sizes` leaves all 23 at the default, where the
Variable Studio shows the variable name in its own column and the feature name never shows.

This is recorded as it is. Which convention draft9p4 teaches is a question for the plan, not
something to settle by tidying the reference.

## What the feature trees hold

| Tab | Features | Types |
| --- | -------- | ----- |
| `robot sizes` | 23 | 23 variables |
| `ball and socket` | 14 | 5 variables, 3 sketches, 2 extrudes, 2 mate connectors, 1 revolve, 1 boolean |
| `hinge` | 46 | 18 variables, 10 sketches, 10 extrudes, 3 mate connectors, 2 circular patterns, 2 mirrors, 1 boolean |
| `u limb` | 9 | 3 mate connectors, 2 derives, 1 sketch, 1 extrude, 1 transform, 1 boolean |
| `l limb` | 9 | 3 mate connectors, 2 derives, 1 sketch, 1 extrude, 1 transform, 1 boolean |

`hinge`'s ten sketches, in tree order: `blade profile`, `stub axle outline`, `blade wedge outline`,
`blade rod outline`, `relief slit outline`, `fork outline`, `fork blade top cut outline`,
`pocket axle sketch`, `ear wedge outline`, `fork arm outline`.

`ball and socket`'s three: `stud profile`, `collar profile`, `slit profile`.

Both limbs have one sketch each, `limb section`, and both reach their shape by deriving the joint
parts and transforming them onto mate connectors rather than by drawing them again.

## What this record does not cover

**The five tabs draft9p4 also teaches that draft9p1p6 does not have.** `body`, `head`, `foot`,
`gripper` and the assembly are not in this document. Their reference is draft9p1p1, recorded at
[`../../2026-08-29-draft9p3/reference/`](../../2026-08-29-draft9p3/reference/), and what draft9p3
built on top of it. A take of tutorials 1, 2, 3, 5, 6, 7, 8 and 12 reads there.

**The assembly.** draft9p1p6 has no assembly tab.

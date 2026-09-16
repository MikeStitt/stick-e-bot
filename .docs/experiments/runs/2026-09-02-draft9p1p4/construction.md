# draft9p1p4 — the construction, feature by feature

`req.model.same_structure` is about how the model is built rather than what it measures, and the
construction only lives in `/features`. That endpoint refused for the whole build, so
[`register.md`](register.md) recorded the requirement as deferred. This is the audit it was waiting
for, read on 2026-09-03 once the quota cleared.

Read with [`build-notes.md`](build-notes.md), which says why each tab is shaped the way it is, and
with [`check.py`](check.py), which measures what came out.

## What the audit read

Every feature of all six Part Studios, through `GET /api/partstudios/d/{d}/w/{w}/e/{e}/features`,
plus one FeatureScript call per tab to turn each sketch's plane id into a name. A sketch's
dimension lives in a constraint's `length` or `angle` parameter; `labelRatio`, `labelDistance` and
`labelAngle` sit beside them and place the label, so a first pass that reads every expression
reports label positions as though they were typed dimensions. The numbers below come from the
first pair only.

## The feature order, per tab

| Tab | Features, in order |
| --- | ------------------ |
| `ball and socket` | five variables, `stud profile`, `revolve stud`, `collar profile`, `collar blank`, `cavity from ball`, `slit profile`, `relief slits`, two robot connectors |
| `hinge` | fifteen variables, `blade profile`, `blade blank`, `stub axle outline`, `stub axle`, `blade bump outline`, `blade bump`, `axis for circular patterns`, `blade bumps`, `mirror blade`, `blade rod outline`, `blade arm`, `relief slit outline`, `relief slit`, `fork outline`, `fork blank`, `fork blade top cut outline`, `trim fork to arm`, `pocket axle sketch`, `pocket axle on fork`, `ear valley outline`, `ear valley`, `ear valleys`, `two forks`, `fork arm outline`, `fork arm`, `combine fork parts`, two robot connectors |
| `u limb` | `add socket`, `mate for fork`, `limb section`, `limb`, `add fork`, `move fork`, `combine parts`, `shoulder end`, `elbow end` |
| `l limb` | `add blade`, `limb section`, `limb`, `mate for ball stud`, `add ball stud`, `move ball stud`, `combine parts`, `elbow end`, `wrist end` |
| `ball with cylinder` | `add ball stud`, `cylinder section`, `cylinder` |
| `socket with cylinder` | `add socket`, `cylinder section`, `cylinder` |

The joint is drawn once and arrives everywhere else through `importDerived`. Symmetry and
repetition are features rather than second drawings: `mirror blade`, `two forks`, and the two
circular patterns `blade bumps` and `ear valleys`, each driven by `#teeth`.

## Every dimension, and what drives it

Each of the 17 sketches carries a constraint web, from 2 constraints on the simplest circle to 26
on `slit profile`. None is the empty list that `.parts/onshape.md` names as draft9p1p2's failure.

Of 42 sketch dimensions, 39 read a `robot sizes` row or an expression over one: `#ball / 2`,
`#stalk / 2`, `#stand`, `(#ball / 2 + #wall) * 2`, `#slit / 2`, `#slit_in`, `#slit_out`, `#nose`,
`#tab_free`, `2 * #flat`, `#stub`, `#bump_r`, `#cone_d`, `#flat`, `#limbD`, `#nose + 1 mm`,
`#slit_h / 2`, `#seat / 2`, `#bore_d`, `#valley_d`.

Every extrude and revolve takes its depth and its start offset from a variable too:
`#limbCenter - #collar - #ear_free` on the upper limb, `#limbCenter - #stand - #tab_free` on the
lower, `#blade + 2 * #stub_proud` on the axle, `#limbD / 2` on both coupon handles.

**Three dimensions are typed, all of them `2 mm`, all in `fork blade top cut outline`.** They hold
the cutting rectangle's left, right and top edges clear of the Ø`#limbD` circle. The edge that
decides the cut is the fourth one, at `#seat / 2`; the other three only have to fall outside the
part, and any number that does will do. That is a typed number with a reason, which
`req.model.design_intent` allows and which was not written down until now.

## What each sketch is drawn on

Fifteen of the 17 sit on a default plane, and two sit on a face: `slit profile` in `ball and
socket`, and `limb section` in `u limb`, which sits on the collar's end face.

**No sketch anywhere projects an existing edge.** There is no `PROJECTED` constraint in the
document. Where a shape is placed from the origin that is the right answer, and most of this joint
set is placed from the origin. It is recorded here because
[`../../../../.parts/modeling-practice.md`](../../../../.parts/modeling-practice.md) reaches for
**Use (Project/Convert)** first, and a page written from these tabs will teach dimensions from the
origin instead.

## The finding: the two limbs start their rods by two different rules

Both limbs measure the same 48 between joint centers and both pass every row of `check.py`. They
are built differently:

| | `u limb` | `l limb` |
| - | -------- | -------- |
| `limb section` sits on | the collar's end face | the Top plane |
| `limb` start offset | none | `#tab_free`, in the opposite direction |
| so the rod begins at | where the socket ends | a distance computed from the pin |

The lower limb's blade is derived before its sketch, so the blade's root face is there to be picked
and was not. Picking it is what the upper limb does, and it is what
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) asks for: a face when the shape is
placed from that part. Two constructions of the same feature is the thing
`req.model.same_structure` exists to catch, and no measurement can see it, because both spellings
put the rod in the same place.

This is left as it stands. The model is proved and versioned, and re-cutting `l limb`'s sketch onto
the blade's root face changes a construction that every Phase C number was read from, so it is
Mike's call rather than a repair to make while he is away.

## Where the requirements now stand

| Requirement | Standing |
| ----------- | -------- |
| `req.model.same_structure` | Met, with the limb finding above recorded against `l limb`. |
| `req.model.design_intent` | Met. 39 of 42 dimensions read a variable; the three that do not are the cut profile's clearances, and the reason is written down here. |
| `req.model.anchored` | Met for the upper limb and `slit profile`. The lower limb offsets from a plane where the blade's root face was available. |
| `req.model.visible_geometry` | Met everywhere except that same offset. |
| `req.model.derive` | Met. The joint is drawn once and derived four times. |

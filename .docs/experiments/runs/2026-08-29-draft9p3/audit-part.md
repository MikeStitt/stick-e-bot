# draft9p3 — `audit.part`, the construction half

[`plan.md`](plan.md) asks `audit.part` to diff construction before it measures shape, feature for
feature and sketch for sketch, because the page is written from the construction and a part can
measure right for the wrong reason. Neither half of that diff ran during Phase T. The sketch half
needs `/api/partstudios/.../features`, which was refused for the whole build, and the dependency
half was never run against the reference records that were waiting for it. The tutorials went ahead
on shape alone.

Both halves ran on 2026-09-04 over the six tabs draft9p3 has built. **Every tab reproduces the
reference's feature list in the reference's order.** Two tabs are clean, three carry a difference
that a page is already written from, and one is the tab whose tutorial has not finished.

## What the audit read

draft9p3's `body`, `head`, `ball and socket`, `u limb`, `hinge` and `foot`, against
[`reference/`](reference/README.md), which is `stickbot-draft9p1p1` read the same two ways.

- **The sketch half**, [`../../../../tools/diff_sketches.py`](../../../../tools/diff_sketches.py),
  over `/features`. It reports each sketch's plane, its entities, its constraints by type, and
  every id its constraints reach for outside itself.
- **The dependency half**,
  [`../../../../tools/read_construction.py`](../../../../tools/read_construction.py) into
  [`../../../../tools/diff_construction.py`](../../../../tools/diff_construction.py), over
  `Show dependencies…` in the GUI. It reports what each feature was built on, and the tally of
  features standing on the model's own geometry rather than on a default plane and some variables.

The sketch half's caution applies to ids: an id is not promised to mean the same thing in two
documents, so a difference there is worth reading and a match is worth nothing. The dimensions, the
entity counts, the feature lists and the dependency lists do not depend on ids.

Three features returned an empty dependency panel on the first pass — `torso shoulder profile`,
`hip connector on torso` and `collar blank` — and a record that lists a feature in `order` and not
in `features` reads downstream as a feature the tab does not have. They were re-read before any of
the numbers below were taken.

## What each tab came back as

| Tab | Features | In order | Built on the same | Sketches differing |
| --- | -------- | -------- | ----------------- | ------------------ |
| `body` | 33 of 33 | yes | 29 | 5 of 6 |
| `head` | 26 of 26 | yes | 24 | 1 of 3 |
| `ball and socket` | 10 of 14 | yes | 8 | 3 of 3 |
| `u limb` | 10 of 10 | yes | 8 | 2 of 2 |
| `hinge` | 49 of 49 | yes | 47 | 7 of 9 |
| `foot` | 24 of 24 | yes | 21 | 3 of 3 |

## The three findings

### `torso shoulder profile` draws the line the reference projects

The dependency graph says these two sketches are built on the same five things: `pivot lines`,
`plane for shoulder`, `#boss_len`, `#boss_d` and `#tilt`. It is the sketch half that separates
them:

| | draft9p3 | 9p1p1 |
| - | -------- | ----- |
| curve segments | 4, the rectangle | 5, the rectangle and one construction line |
| `PROJECTED` constraints | 0 | 3 |

Every other constraint matches exactly: 4 coincident, 2 parallel, 2 lengths, a perpendicular, a
midpoint and an angle, on both. The whole difference is that the reference brings one construction
line in with **Use (Project/Convert)** — the three `PROJECTED` constraints are that line and its two
ends — and stands the rectangle's midpoint on it. draft9p3 has no such line, so its rectangle is
held in the same place by other means.

Both stand on `pivot lines` and the dependency graph cannot tell them apart, which is the case
`audit.part`'s sketch half exists for and the reason [`plan.md`](plan.md) makes it blocking.

This is task #125, opened off the shape half during tutorial 6 and now measured. The torso joints
page is written from the drawn version.

### The upper limb's last step is a sketch, not a mate connector

Nine of ten features reproduce. The tenth does not:

| | draft9p3 | 9p1p1 |
| - | -------- | ----- |
| tenth feature | sketch `elbow station`, on Top and Front | mate connector `elbow end`, on the model |
| anchoring tally | 6 on the model, 1 floating | 7 on the model, nothing floating |

`elbow station` is the only floating feature in either tab, and it is floating because a sketch on
two default planes stands on nothing the model made. Tutorial 10 is task #139 and is unfinished;
this is where it stopped, so finishing it means replacing that sketch rather than adding to it.

### The ball and socket is four variables short, and the sketches carry the arithmetic instead

Task #119 says draft9p3 does not have four of the tab variables 9p1p1 has. Both halves agree on
what that costs. The dependency half finds the four missing outright, and finds the two sketches
that read them in the reference reading nothing in draft9p3:

| Feature | draft9p3 is built on | 9p1p1 is built on |
| ------- | -------------------- | ----------------- |
| `stud profile` | Origin, Front | Origin, Front, `#stalk`, `#stud_len` |
| `slit profile` | Origin, `#slit`, `collar blank` | Origin, Front, Right, `#slit`, `#slit_in`, `#slit_out`, `collar blank` |

The sketch half says where the numbers went instead:

| Sketch | draft9p3 | 9p1p1 |
| ------ | -------- | ----- |
| `collar profile` | `#collar * 2` | `#ball + 2 * #wall` |
| `slit profile` | `#ball`, `#ball * 5 / 12`, `#slit / 2`, `#slit / 2` | `#slit / 2`, `#slit / 2`, `#slit_in`, `#slit_out` |
| `stud profile` | `#ball / 2`, `#ball / 4`, `#stand` | `#ball/2`, `#stalk/2`, `#stud_len` |

Every one of these is a driven dimension, so the shape follows the design either way. What differs
is where the rule lives: the reference puts it in a named tab variable and the sketch reads the
name, and draft9p3 puts the arithmetic in the sketch. `#ball * 5 / 12` is the sharp case — the
reference calls that number `#slit_in` and derives it from the ball, the wall and the fit, and
draft9p3 carries a ratio no reader can trace back to a rule.

## The pattern behind most of the rest

**The reference constrains a sketch to a second default plane, and draft9p3 does not.** It shows up
in both halves, on five tabs, and it accounts for most of the remaining differences:

| Sketch | draft9p3 is built on | 9p1p1 adds |
| ------ | -------------------- | ---------- |
| `pivot lines`, in `body` | Origin, Front | Top |
| `mouth profile`, in `head` | Origin, Front | Right |
| `slit profile`, in `ball and socket` | Origin | Front, Right |
| `blade profile`, in `hinge` | Origin, Front, Right | Top |
| `foot outline`, in `foot` | Origin, Top | Front |
| `groove profile`, in `foot` | Origin, Top | Front |

Every one is a symmetric shape, and the second plane is the plane it is symmetric about. The
sketch half reads the same difference from the other side: on `mouth profile` draft9p3 reaches for
the origin twice where the reference reaches for the origin once and a plane once, and six sketches
across `hinge`, `foot`, `body` and `u limb` hold one more `HORIZONTAL` or `VERTICAL` than the
reference while reaching for the origin one more time. Both spellings leave every sketch fully
defined. `pocket axle sketch` is the same trade the other way round, holding a horizontal where the
reference holds a vertical.

The mouth is the one already written down, in [`notes.md`](notes.md) § *A sketch has no axis, so the
mouth is dimensioned instead*.

## Where draft9p3 stands on more than the reference does

Three features are anchored in draft9p3 and float in 9p1p1, which is why draft9p3's tally is the
higher one on `body` and on `hinge`:

- `trim shoulder pattern` is built on `torso outline`; the reference builds it on Origin, Front and
  `#boss_d` alone.
- `hip connector location` and `neck connector location` are built on `torso outline`; the reference
  builds both on the Origin.
- `fork blade top cut outline` is built on `axis for circular patterns` and `#limbD`; the reference
  builds it on `#nose` and floats.

The hinge one also shows in the dimensions, and it is the sketch draft9p1p4 inherited:

| draft9p3 | 9p1p1 |
| -------- | ----- |
| `#limbD`, `#slot / 2`, `2 mm`, `2 mm`, `2 mm` | `2 * #nose`, `#slot / 2`, `#nose + 2 mm`, `#nose + 2 mm`, `#nose + 2 mm` |

Only one edge of that rectangle decides where the cut lands, `#slot / 2`, and both spell it the
same. The other three only have to fall clear of the part: the reference places them from the
origin at `#nose + 2 mm`, and draft9p3 places them 2 mm from the circle. `#limbD` and `2 * #nose`
are the same number under two names. draft9p1p4's own audit recorded those three `2 mm` as
clearances with a reason, and that reading stands; the reference shows a spelling that carries the
reason in the expression.

## The two smaller differences

- **`second eye`, in `head`**, is built on Right and `eye` in draft9p3, and on `#headD` and `#face`
  as well in the reference.
- **`mate to robot`, in `foot`**, is built on Origin and `foot pedestal` in draft9p3, and on
  `add socket` as well in the reference. The pick that builds this connector is the subject of
  [`notes.md`](notes.md) § *One pick fills a Mate connector, and a second pick empties it again*;
  it resolves now, and it still stands on one thing fewer than the reference's.

## What the record could not say, and what settled it

All three of draft9p3's foot sketches record the Top plane. All three of the reference's record a
plane query with no geometry id in it, and so does the gripper's `clip profile` — four sketches in
the whole reference, where every other sketch in every other tab names a plane. The dependency read
settles it: 9p1p1's `foot outline`, `groove profile` and `pedestal outline` are all built on Top,
the same as draft9p3's. The empty query is how the record came out, not a difference in the model.

## Where this leaves the requirements

| Requirement | Standing |
| ----------- | -------- |
| `req.model.same_structure` | Missed on `torso shoulder profile`, on `u limb`'s tenth feature, and on `ball and socket`'s four variables. Every other feature in all six tabs reproduces, in order. |
| `req.model.design_intent` | Met. Every dimension in every tab reads a variable or an expression over one. Four rules that the reference keeps in a named variable are carried as sketch arithmetic. |
| `req.model.anchored` | Missed on `u limb`, whose tenth feature floats on two default planes. Met elsewhere: draft9p3's tally is the higher one on `body` and `hinge`, the same on `head`, `ball and socket` and `foot`. |
| `req.model.visible_geometry` | Missed on `torso shoulder profile`, which redraws what the reference projects, so the curves do not follow. |

## What is still owed

The three tabs `l limb`, `gripper` and the assembly are not built, so neither half has run on them.
`audit.part` runs again per tab as tutorials 10 to 14 are taken.

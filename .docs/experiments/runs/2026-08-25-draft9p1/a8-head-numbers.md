# A8 — the head gets variables, a depth, and no pupils

`head` is the only one of the eight Part Studios that declares no variables. Its sketches read
`#torsoH` straight out of the Variable Studio, and its depth reads nothing at all.

## Which number the head's width follows

The built profile carries `RADIUS #torsoH * 3 / 8` and `LENGTH #torsoH * 3 / 8`, so the head is
`0.75 × #torsoH` across — 72. The torso is `#torsoW` across — also 72. Nothing on the model says
which of the two the head is meant to be, because at the robot's size they are the same number.

**The head is as wide as the body: `#headW = #torsoW`.** The two failures are not symmetric.

| driven | with `#headW = #torsoW` | with `#headW = #torsoH * 3 / 4` |
| --- | --- | --- |
| `#torsoW` 72 → 90 | head widens with the body | head stays 72 on a 90 body — a narrow head |
| `#torsoH` 96 → 120 | head stays 72 on a taller body | head goes to 90 on a 72 body — **wider than the torso it sits on** |

A head wider than the torso is the one of these that stops being a robot, and it is the one the
plan sheet's next round number produces. The equality is also load-bearing elsewhere:
[`../../build-briefs/head.md`](../../build-briefs/head.md) works the head's tilt from the fact that
the head overhangs the torso fore and aft and **not** side to side, which is only true while the
two widths are equal.

**The profile keeps its two dimensions and gains nothing.** Radius `#headW / 2` and length
`#headW / 2`, which is what makes the front square — a semicircular arch of r36 sitting on a 36
straight. `#headH` is not a variable; it is what those two come to.

## The depth becomes `#headD`, and it follows the torso's depth

`#headD = #torsoD * 5 / 4` — 60 at the robot's size, 30 at half size, which is what stickbot has
and what draft9p0 retyped by hand.

The head's underside is `#headW × #headD` = 72 × 60 and the torso's top face is
`#torsoW × #torsoD` = 72 × 48, so the head hangs **6 mm over the torso's front face and 6 over its
back**. That overhang is the thing the head brief's tilt argument turns on: the head's fore-and-aft
corners never meet the torso's top face, they swing down its back. Tying the depth to `#torsoD`
keeps the overhang a fixed proportion at every size, so the argument survives being driven. Tying
it to `#headW` or to `#torsoH` would not: drive `#torsoD` alone to 72 and the torso becomes deeper
than the head, and the corners that the brief says overhang are inside the footprint instead.

**This is the fifth variable `02-head.md` has been asking about since draft8.** That page says a
number retyped every time the robot resizes is a variable nobody has written down yet, and this one
was retyped once already — 30 to 60.

## The pupils are dropped

Three things say so, and the third is the one that settles it.

- **The example stickbot has no pupils.** Its head runs `eye profile` → `eye` → `second eye` →
  `mouth profile` → `mouth`, and there is no pupil sketch or extrude anywhere in it
  — [`a3-eye-ellipse.md`](a3-eye-ellipse.md).
- **Nothing has ever built one.** The pupil exists in `make_plans.py` and on the sheets' *eye and
  pupil* label. No robot in this repository has one.
- **As drawn, it consumes the whole eye.** `PUPIL_R` was `HEAD_W / 18`, which is `EYE_RY` — the
  eye's own minor radius. A circle of the ellipse's semi-minor radius, on the ellipse's center,
  touches it at the top and the bottom and nowhere else. There is no eye above the pupil or below
  it, and the two crescents left and right meet at a point of zero width. Cutting or adding that in
  Onshape gives a non-manifold edge rather than a face.

So it was never a pupil that could be built at any size — it was a circle inscribed in an ellipse,
drawn from the same fraction twice by accident.

**Putting them back costs one circle and one extrude.** The radius has to be smaller than `#eyeRy`
for there to be an eye left around it; `#eyeRy / 2` = 2 leaves a 2 mm ring top and bottom. This is
recorded so the decision can be reversed by someone who wants a face with pupils, not to argue that
it should be.

## What the head tab declares

| variable | expression | mm |
| --- | --- | --- |
| `#headW` | `#torsoW` | 72 |
| `#headD` | `#torsoD * 5 / 4` | 60 |
| `#eyeX` | `#headW / 6` | 12 |
| `#eyeUp` | `#headW / 9` | 8 |
| `#eyeRx` | `#headW / 9` | 8 |
| `#eyeRy` | `#headW / 18` | 4 |
| `#face` | `#headW / 24` | 3 |
| `#mouthW` | `#headW * 5 / 9` | 40 |
| `#mouthH` | `#headW * 5 / 36` | 10 |
| `#mouthDn` | `#headW * 13 / 72` | 13 |
| `#chamfer` | `#headW / 12` | 6 |

`#face` is one number for two features: the eye is an `Add` that stands `#face` proud of the front
and the mouth is a `Remove` that cuts `#face` into it. draft9p0 built both at 3 and stickbot built
both at 1.5, so they have moved together twice without anyone writing down that they are the same
number.

`upper rounds` is not in this table. Its radius is A9's row.

**None of these belongs in the Variable Studio.** No tab outside `head` dimensions anything with
them, which is the test `01-torso.md` states.

## Found while reading

**The parts sheet printed `grip 1.9464840096954308 mm`.** A2 made `GRIP` a derived float and the
label had always interpolated it bare. It goes through `mm()` now and reads `grip 1.95 mm`, which
is what the drawing conventions ask for. The brief keeps 1.9465, because a brief is where the
arithmetic lives.

**The head brief calls the head's width `#headD`.** Its first row reads *across | 72 | `#headD` =
`#torsoH * 3/4`* while a later row uses `HEAD_D` for the depth, so one name means two dimensions
three lines apart. Both rows are corrected here.

**The head brief still specifies Ø20 eyes at x ±16, z +16, with Ø8 pupils.** A3 changed the eye to
a 16 × 8 ellipse at x ±12, z +8 and did not reach this row. Corrected here.

**The head brief specifies a 1.2 mm shell that nothing builds.** `02-head.md` says out loud that
there is no shell and none was built, and the brief's table still carries one. The row is marked
rather than deleted, because what to do about a shell is a design question this row does not settle.

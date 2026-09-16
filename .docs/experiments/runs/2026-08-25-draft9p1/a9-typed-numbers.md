# A9 — the shoulder's typed numbers, and the head's rounding

Four numbers in the shoulder and one on the head were typed rather than derived. The sheet had
them right because A2 retyped every one of them by hand when the robot doubled. The model has them
right for the same reason, which is not a reason at all: nothing in either place would follow the
next time a driving number moves.

## `#boss_d` is a third wider than the ball it carries

The pad the shoulder ball sits in is a typed 16, and the ball is `#torsoH / 8`:

| `#torsoH` | ball Ø | pad Ø, typed | shoulder around the ball |
| --- | --- | --- | --- |
| 96 | 12.0 | 16 | 2.0 |
| 120 | 15.0 | 16 | 0.5 |
| 128 | 16.0 | 16 | **none — the pad is inside the ball** |

There is a size at which this model stops having shoulders and it is 8 mm past the plan sheet's
next round number.

**`#boss_d = #ball * 4 / 3`.** It gives 16 at the robot's size and 8 at half size, which are the
two the sheet has been drawn at, and it holds the shoulder at `#ball / 6` — a sixth of the ball's
diameter — at every size. Writing it against the ball rather than against `#torsoH` says what the
number is for: the pad exists to carry that ball.

## Three more in the same feature

`STAND`, `SHOULDER_L` and `SHOULDER_DROP` were typed in `make_plans.py` too, and the history shows
all three being retyped in the doubling commit — 5 → 10, 13 → 26, 4 → 8. They are the same defect
as `#boss_d` in the same feature, so they are fixed in the same pass:

| name | now | mm | why that number |
| --- | --- | --- | --- |
| `#stand` | `#ball * 5 / 6` | 10 | how far a ball center stands off the face it grows from |
| `#shoulder_drop` | `#torsoH / 12` | 8 | where the stud roots, below the torso's top |
| `#shoulder_len` | `#torsoH * 13 / 48` | 26 | side face to ball center, along the stud |

**`#shoulder_len`'s fraction is odd because it is a result, not a proportion.** The sheet's own
comment works it out: a Ø`#limbD` arm on a ball standing `#stand` clear fouls the torso through the
first 12.19° of its travel, and at 26 along the stud the ball stands 13.55 clear, the whole arc is
free, and the closest the arm comes anywhere in it is 1.46. The same comment says the angle is the
same at any size because it is a ratio of lengths that all scale together — which is exactly the
argument that this number has to scale, and the reason it is written as a fraction of `#torsoH`
rather than left at 26.

`#boss_len` was already `#shoulder_len - #stand`, and follows both. `#tilt` and `#yaw` stay typed:
they are angles, and an angle is what stays the same when a length changes.

## `upper rounds` is `#headW / 6`

The plan types 6 and draft9p0 built 12. Nobody decided that; the builder doubled it along with
everything else, and the register recorded it as a number nobody had decided.

**`#round = #headW / 6`** gives 12 at the robot's size and 6 at half size, so it reproduces both
without either one having to be retyped.

**It also keeps the eye clear of the fillet.** `upper rounds` eats the front face down from the top
by its own radius, so the face stops at `#headW / 2 - #round` = 24. The eye reaches
`#eyeUp + #eyeRy` = 12, which clears by 12 — and both sides of that comparison are fractions of
`#headW`, so the clearance is the same fraction at every size.
[`a3-eye-ellipse.md`](a3-eye-ellipse.md) has the arithmetic; A3 could only state it because the eye
had become a fraction of the head, and this row is what makes the other side of it one too.

**Where it stops working is the depth, not the width.** A8 made `#headD` follow `#torsoD` while
`#headW` follows `#torsoW`, so the fillet and the face it has to fit across are now driven by
different numbers. A fillet of `#round` on each of the two arch edges needs `#headD > 2 × #round` —
`#torsoD > #torsoW / 3`. At the robot's size that is 48 against 24, so there is a factor of two in
hand, and driving `#torsoD` below a third of `#torsoW` turns the head's top into a full round.

## The head on the sheet was a square

`make_plans.py` drew the head as a plain rectangle on both sheets. The head's profile is a radius
and a straight length, both `#headW / 2` — a semicircular arch sitting on a straight — so the
picture a student compared their model against did not have the shape of the part.

Both sheets draw the arch now, and the parts sheet says `arch r36, top edges rounded r12` under the
size. A fillet radius cannot be called out on a shape the drawing does not have, which is part of
why this row went unsettled for as long as it did.

## Found while reading

**The parts sheet labeled a rod `Ø24 × 49.9465 mm`.** A1 derived the rod lengths and A2 then made
`GRIP` irrational, so one of the four came out at full float precision. It goes through `mm()` now
and reads 49.95. The brief keeps the exact number.

**Deriving a constant is how a bare `{NAME}` in a label gets found.** Three labels printed `26.0`
and `10.0` the moment `SHOULDER_L` and `STAND` became expressions, the same way `LIMB` printed
`Ø24.0` in A7 and `HEAD_D` would have in A8. Every one of them was a label that had been correct
only because the constant happened to be an integer.

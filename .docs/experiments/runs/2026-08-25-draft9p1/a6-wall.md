# A6 — `#wall` gets one home

Three tabs declare `#wall`. `ball and socket` says `3 mm`; `foot` and `gripper` say `#torsoH / 32`.
They agree at the robot's current size and nowhere else.

## What the disagreement costs

`foot` and `gripper` each build their own collar as `#ball / 2 + #wall` and wrap it around a socket
**derived** from `ball and socket`, whose collar was built off the literal 3. So there are two
collars per part and they only coincide by arithmetic accident:

| `#torsoH` | the part's own collar | the derived socket's collar | what happens |
| --- | --- | --- | --- |
| 96 | 9.000 | 9.000 | they merge into one face — the defect is invisible |
| 120 | 11.250 | 10.500 | the foot grows a sixth cylindrical face and a 0.75 ledge at z −7.4 |

The gripper fails differently, and worse: its x follows its own collar to 22.500 while its y
follows the derived socket to 21.000, so **the part changes shape rather than size**. A driving
dimension is supposed to scale a robot, not deform one part of it.

## The fix is a rule, and `01-torso.md` is where it goes

A dimension read by two Part Studios is declared in the Variable Studio, which is the one element
whose variables reach every tab. That rule was reasoned out here and written onto `01-torso.md`,
the page that builds the studio; A7 corrected this section, which first claimed the page already
carried it. What the page did say is that the joint's variables stay in `ball and socket` because
the collar's diameter is `#ball + 2 × #wall`. That is the step that does not follow: `foot` and `gripper` build a collar from `#wall` too, so it
is read by three tabs, and its own rule moves it.

**`#wall` is declared in the Variable Studio and nowhere else.** The other nine of the joint's ten
stay in `ball and socket`, because nothing outside the joint builds geometry from them. The test is
not whether a number belongs to the joint conceptually — it is whether another tab dimensions
something with it.

**Onshape is why this had to happen rather than being a matter of taste.** A variable is scoped to
its Part Studio. `foot` and `gripper` could not read `ball and socket`'s `#wall` even if they
wanted to, so they re-declared it, and re-declaring is what let the two meanings drift apart.

## Which meaning wins: `#torsoH / 32`

The two candidates are the literal `3 mm` and the expression `#torsoH / 32`.

- **`#torsoH / 32` reproduces every value the robot has ever been built at.** It gives 1.5 at
  `#torsoH` 48 and 3.0 at 96, which are the 1× and 2× walls. The literal 3 reproduces only the
  current one.
- **The printing objection does not bite.** A wall is a printing minimum — three perimeters at a
  0.4 mm nozzle is 1.2 — and the worry about an expression is that it scales below what prints.
  `#torsoH / 32` reaches 1.2 at `#torsoH` **38.4**, which is well under half the robot's size.
  Anything a student would plausibly type stays printable.
- **It keeps the wall a fixed fraction of the ball it wraps.** `#ball` is `#torsoH / 8` and `#wall`
  is `#torsoH / 32`, so the wall is a quarter of the ball's diameter at every size, and the collar
  is `#ball + 2 × #wall` = 1.5 × the ball. That is a proportion somebody chose, and writing it as
  an expression is what records that they chose it.

## What this contradicts, for A13

[`../../../robot-build-plan.md`](../../../robot-build-plan.md) lists `#wall` among the joint's ten
at **1.5**, marked **not scaled**, with the note *three perimeters at a 0.4 mm nozzle*. Two things
in that row are now wrong: it did scale, 1.5 to 3.0, and it is not one of the ten any more. A13
moves it into the table of drivers and drops the *not scaled* mark. This is the second row in that
table found to be marked *not scaled* on a number that scaled — `#fit` was the first.

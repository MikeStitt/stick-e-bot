# A3 — the eye, read off the example rather than guessed

U1 asks for the eye to be an ellipse taken from the example stickbot, scaled and positioned 2×, so
that it clears the head's rounding. It names two things to be read rather than assumed: which
document is the example, and which rounding feature the eye runs into. Both were read over REST on
2026-08-25, read-only, and both are answered.

## Which document is the example — the question dissolves

| | tabs |
| --- | --- |
| `stickbot` `5dc85bc3` | `body`, `head`, `robot sizes`, `Assembly 1`, a BOM |
| `stickbot-for-bot-review` `111f9750` | those, plus `ball and socket`, `hinge`, `u limb`, `l limb`, `foot`, `gripper` |

`stickbot` stops where tutorial 2 stops. `stickbot-for-bot-review` is the same document carried on
to a whole robot: **its head's first nine features are `stickbot`'s head's nine features, in the
same order, with the same names.** Both therefore hold the same `eye profile`, and it does not
matter which one is called the example. The eye was read off `stickbot`.

## The eye

`eye profile` holds one entity, and it is an ellipse — not a circle with an ellipse somewhere
nearby. At the example's `#torsoH` of 48, which is half the robot's:

| | example, 1× | as `make_plans.py` drew it, 2× | draft9p1, 2× |
| --- | --- | --- | --- |
| shape | ellipse, Ø8 across × Ø4 tall | circle, r10 | ellipse, r8 × r4 |
| center | 6 out, 4 up | 16 out, 16 up | 12 out, 8 up |
| as a fraction of `HEAD_W` | out `1/6`, up `1/9` | out `2/9`, up `2/9` | out `1/6`, up `1/9` |
| radii as a fraction | `1/9` and `1/18` | `5/36` | `1/9` and `1/18` |

**The major axis runs across the face.** The ellipse carries no `majorAxisAngle`, so it is
unrotated and the Ø8 is the horizontal one: the eye is wider than it is tall.

**The sheet had the position wrong as well as the shape.** The circle was not an ellipse squashed
to a circle — it sat at `2/9` of the head's width in both directions, where the example sits at
`1/6` out and `1/9` up. Scaling the example gives both back.

**The numbers were already on disk.** [`../../../build/plan/02-head.md`](../../../build/plan/02-head.md)
records `eye profile` as `HORIZONTAL`, major 8 mm, minor 4 mm, 6 across by 4 up, in its read-back
of the example. So A3 is `make_plans.py` catching up with a plan page rather than anything new
being learned — the design source and the plan page have disagreed about the eye since draft9p0.

## Which rounding it runs into: `upper rounds`, and here is the arithmetic

`upper rounds` is a fillet on the head's top edges. It is **r6** in the example and **r12** in
`stickbot-draft9p0`, and it eats that much of the front face down from the top.

- The head is `HEAD_H` 72 at 2×, so the front face runs to y 36 and the fillet consumes everything
  above **y 24**.
- draft9p0's eye is a circle centered at y 16 with r10, so it reaches **y 26**. That is **2 mm
  inside the fillet**, and it is the collision.
- The example's eye, scaled, is centered at y 8 with a minor radius of 4, so it reaches **y 12**
  and clears the fillet by **12 mm**.
- At the example's own size the same check gives y 6 against a fillet starting at y 12 — clear by
  6. The example was drawn to clear its own rounding, and scaling it keeps that.

**This is why the example's eye is both lower and flatter**, and it is the whole reason U1 asks for
the profile to be taken rather than invented.

## Found while reading, for A8

**The example builds no pupils.** Its head runs `eye profile` → `eye` → `second eye` → `mouth
profile` → `mouth`, and there is no pupil sketch or extrude anywhere in it. `make_plans.py` draws a
pupil inside each eye and the sheet labels it *eye and pupil*. A8 decides whether the pupils are
built or dropped; the example is evidence for dropping them.

**The example's eye stands proud rather than being cut in.** Its `eye` extrude is an **Add** of
1.5 mm at 1×, so the eye is a raised disc on the face. Whether draft9p1's is added or removed is
not settled here.

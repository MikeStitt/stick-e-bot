# A2 — `#fit` to 0.08, worked

U2 in [`../2026-08-23-draft9p0/register.md`](../2026-08-23-draft9p0/register.md) asks for the joint
to be dimensioned at an extreme fit so the socket's height does not move when `#fit` moves, with
the ball's position as the free variable, and it says the item is owed a worked drawing before it
is built. This is that file.

## What the joint is made of

The socket's hollow is a sphere of radius `#ball / 2 + #fit`, and its center sits `#grip` below the
face the ball goes in through. Where that sphere cuts the face is the mouth. So the mouth's
diameter is `2 √(cavity² − grip²)`, and it is smaller than the ball — that difference is the whole
snap. The ball's center rests at the cavity's center, so **`#grip` is the ball's position**: how
deep the ball sits below the socket's face.

Everything else follows from those three. The swing is how far the stalk can lean before it touches
the mouth's rim, which is `acos(grip / cavity) − asin(stalk / ball)`, and the second term is a flat
30° because the stalk is exactly half the ball.

## The two ways to read the requirement

Both hold the socket's height and let the ball move. They differ over which dimension is the one
taken at the extreme.

**A — the mouth is the dimension, and `#grip` is an expression on `#fit`.** The mouth is drawn at
`0.96 × #ball`, which is what `make_plans.py` already prints as *96% of the ball*, and the ball's
depth is whatever puts the cavity through it.

**B — `#grip` is the dimension, fixed at its `#fit` 0 value of 1.68.** The cavity grows about a
center that does not move, so the mouth opens up as the fit loosens.

| | `#fit` | `#grip` | cavity | mouth | of the ball | snap interference | swing | cavity depth |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| as built | 0.8 | 3.6 | 6.8 | 11.538 | 96.1% | 0.462 | ±28.0° | 10.400 |
| **A** | 0.8 | 3.6142 | 6.8 | 11.520 | 96.0% | 0.480 | ±27.9° | 10.414 |
| **A** | **0.08** | **1.9465** | **6.08** | **11.520** | **96.0%** | **0.480** | **±41.3°** | **8.026** |
| **A** | 0 | 1.68 | 6.0 | 11.520 | 96.0% | 0.480 | ±43.7° | 7.680 |
| B | 0.8 | 1.68 | 6.8 | 13.178 | 109.8% | −1.178 | ±45.7° | 8.480 |
| B | 0.08 | 1.68 | 6.08 | 11.687 | 97.4% | 0.313 | ±44.0° | 7.760 |
| B | 0 | 1.68 | 6.0 | 11.520 | 96.0% | 0.480 | ±43.7° | 7.680 |

## A is adopted, because B breaks the part when a student edits it

At `#fit` 0.8 reading B opens the mouth to 109.8% of the ball. The interference goes negative: the
ball is not held, it drops out. B is only sound near the fit it was dimensioned at, and `#fit` is a
variable precisely so that somebody with a different printer can change it. A model has to survive a
change to a driving dimension, so B is out.

A survives every value. The mouth is 96% of the ball whatever the fit is, so the snap does not
change, and the only thing that moves is how deep the ball sits.

**The range of motion is what tightening the fit buys.** The swing goes from ±28.0° to ±41.3° —
about half again — because a smaller cavity puts the ball's center closer to the face, and the
stalk clears the rim sooner. That is the *reasonable range of motion* U2 asks for, and it arrives
without anything being widened.

**The consequences U2 listed do not arise.** Widening the slits and shrinking the socket height
were named against the mouth closing to Ø9.80, which is what happens if `#grip` 3.6 is carried
across unchanged. Holding the mouth at 96% keeps the interference at 0.480 against 0.462 today, so
the tabs flex the same amount and `#collar_l` stays 11.0. The collar simply has 2.97 of solid below
the cavity where it had 0.6.

## Three sources give `#fit` three values and two histories

- [`../../../robot-build-plan.md`](../../../robot-build-plan.md) gives **0.2**, marked **not
  scaled**, in both the tables that carry it.
- [`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) says it **was
  0.02 until draft9p0**, where it was raised to what a 0.4 nozzle holds between two printed parts.
- [`../../../build/plan/04-ball-and-socket.md`](../../../build/plan/04-ball-and-socket.md) says it
  **moves from 0.2 to 0.8**, which is four times a number `make_plans.py:41` says is not scaled.

**Which of 0.2 and 0.02 it started at is not established here, and neither is who raised it.** What
is established is that the three live sources do not agree and that the built value was 0.8. 0.08
supersedes all of them, and A13 is where the two table rows are corrected.

## What this changes outside the joint

**`#grip` moves, and the thigh's stock length is derived from it.**
[`a1-limb-center.md`](a1-limb-center.md) gives the thigh as `#limbCenter + #grip`. The expression is
unchanged; the number it evaluates to goes from 51.6 to **49.95**. The other three rods do not
touch `#grip` and do not move.

**Nothing else reads `#grip`.** The socket's placement on the head, the foot and the gripper all
take it from the same derived body, so they follow it without an edit.

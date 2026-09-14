# Run 4 — parked decisions

Written unattended, and the framing needs stating honestly: only some of these are questions I
lacked the standing to answer. Items 4, 5 and 7 are genuine design decisions. **Items 1, 2 and 3
are not** — the shoulder boss was asked for directly, the hinge rebalance was approved with "do
it", and an unslit socket collar is a defect rather than a choice. Those three were modeling work
I did not attempt, and calling them parked overstates the case.

Format: what is known, what it turns on, what the options cost, and the cheap answer.

Run 4's brief was to reach an assembly, and it did. Everything below is a place where the run 4
CAD and the briefs disagree and I left the CAD alone rather than spend the assembly on it. All of
it is 4.5 work.

---

## 1. The torso's shoulders are plain radial stalks

**Known.** Measured at (±23, 0, +24): a Ø3 stalk leaving the side face square, ball center 5 clear
of it. [`torso.md`](../../build-briefs/torso.md) settled a different shoulder in r2 — 53° below
horizontal, 30° toward the front, 13 mm long, on a Ø8 boss coaxial with the stalk and cut flush at
the top face, ball center at (±24.775, −3.912, +13.618).

**Turns on.** Whether run 5's instructions teach the shoulder that r2 designed or the one run 3
built. They are different lessons: the settled one needs a doubly-rotated plane before it needs a
sketch, which is most of what makes the torso worth building.

**Costs.** Rebuilding it is a rotated mate connector, a revolve, a mirror and a flush cut — five
features on a part that currently has eleven, and it moves four numbers in the assembly. Leaving
it costs the thing the r2 shoulder exists to buy: with a plain 5 mm stand-off the Ø12 upper arm
fouls the torso through the first 12.19° of its swing, so the joint's ±37.09° is not available.

**Cheap answer.** Build the r2 shoulder in 4.5, before run 5 is written. The assembly does not need
it — at zero pose the arm is straight out and clear — but the instructions do.

---

## 2. The hinge in the CAD is run 3's, not the rebalanced one

**Known.** Measured on `limb-socket-clevis` and `limb-blade-ball`:

| | run 4 CAD | briefs and `make_plans.py` |
| --- | --- | --- |
| ear | 1.200 thick, at y ±1.8 … ±3.0 | 3.200 |
| slot | 3.600 | 5.600 |
| blade | 3.000, solid | 5.000, slit 0.8 × 16 into two tabs of 2.100 |
| rounded end | r 5.810 | r 6.000, which is `NOSE` = `LIMB`/2 |
| slot root | 6.110 behind the pin | 11 behind |

The snap itself is right in both: stub faces at y ±1.000 against blade faces at ±1.500 is
**0.5 mm of interference per side**, which is `STUB_PROUD − GAP` exactly. The detent is 13 valleys
of r 0.5 at 15°, on a radius of 4.800, with two blind bores of r 1.1 on the pin axis for the stubs
to drop into.

**Turns on.** Whether the parts that run 5's screenshots are taken from carry the hinge the
sketches now explain.

**Costs.** The as-built joint works, and it is worth saying why: the 1.2 ear is 16.8 times more
flexible than the solid blade, so it takes **0.472 of the 0.5** and the blade takes 0.028. That
puts the ear at **46.2 MPa** against PETG's 50 — it survives on 8% margin, and only because it is
thin enough to be the spring. Press force is 3.99 kgf. The rebalanced joint splits the movement
0.20 / 0.30 at **19 MPa**, on 62% margin, at 3.22 kgf.

So the parked cost is not "it breaks". It is that the joint sits at 92% of yield with nothing to
absorb a print that came out 0.1 thick, and the sketches in
[`../../sketches/README.md`](../../sketches/README.md) now explain a joint the model does not have.

**Cheap answer.** Rebuild the hinge in 4.5. It is two part studios and the numbers are all derived
in `make_plans.py` already.

---

## 3. The foot's socket collar has no relief slits and is 7.35 long

**Known.** Measured: the foot's collar is a **single** cylindrical face of r 4.700, 7.35 long. The
limb's is **four** faces totaling 26.3 of a possible 29.5 circumference — the missing 3.2 is four
slits of 0.8, over the full 5.5. So the limb was slit and the foot was not.

**Turns on.** Whether a ball can be pressed into the foot at all. An unslit collar has to stretch
its whole circumference to pass a Ø6 ball through a Ø5.803 mouth; a slit one only has to bend four
tabs outward.

**Costs.** Nothing to fix — it is the same circular pattern of a thin rectangular cut that the limb
already carries. Leaving it means the ankle is the one joint nobody can assemble.

**Cheap answer.** Slit it in 4.5. Also decide the collar length deliberately: 7.35 is what got
built, 5.5 is what [`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) says, and nobody
chose 7.35.

---

## 4. The two feet touch at the centerline

**Known.** The foot plate is y ±12.000 in its own frame and the hips are at x = ±12, so after the
foot's 90° turn the two inner edges both land on x = 0. **Zero clearance, exactly.**

**Turns on.** Nothing structural — they touch, they do not overlap. But a printed pair will rub,
and a student who poses the legs even slightly inward will see them collide.

**Costs.** Three ways out and none has been costed: narrow the foot, widen the hips, or accept it
and tell people the legs splay. Widening the hips moves `#hipHalf`, which is a driver.

**Cheap answer.** Accept it for run 5's screenshots, which are taken at zero pose, and raise it as
a design question rather than a CAD fix.

---

## 5. The head sits 3.65 above the torso, not 6

**Known.** The head's socket center is 16.65 below its own center, so seating it on the neck ball
at z = +29 puts the head's underside at **z = +27.65**, and the torso's top is at +24.
[`head.md`](../../build-briefs/head.md) says the gap is 6 and derives the head's center at z = +48;
measured it is at +45.65.

And the gap cannot be 6: the socket sits `#grip` above the head's underside and the ball stands
`#stand` off the torso, so it is `5 − 1.35` and no dimension on the head reaches it.

**Turns on.** The tilt calculation. `asin(clearance / 23.43)` is the whole argument for the neck,
and it was worked from a 6 the model does not have. The surface that binds is the *recessed*
underside, 1.0 above the boss face, so the clearance is 4.65 and the head binds at **11.4°** — not
the 17.4° the brief used to claim, and nowhere near 42°.

**Costs.** Free to fix in the brief — the number was derived, not measured, and the model is the
authority. Costly to fix in the CAD, because raising the head raises the figure past 152.65.

**Done in the brief, still open in the design.** [`head.md`](../../build-briefs/head.md) now
carries the measured stations and 11.4°. What nobody has decided is whether 11.4° is acceptable.
The four ways out are listed there; one of them is lengthening `#stand`, which buys 2.6° per
millimeter and costs the same millimeter at every other joint in the figure.

There is a second half to this that is a torso problem, not a head one: the 42° assumed **two**
Ø12 boss faces 4 mm apart, and the torso has no neck boss at all. Its own brief asks for one; runs
3 and 4 built a plain stalk.

---

## 6. The mates — settled, not parked

This entry was written as a parked item and then done, so it is kept for the estimate it got
wrong. It said the coordinates were all known so mating was "work, not research". It was research:
five encodings of the mate query failed silently before the right one
(`BTMPartStudioMateConnectorQuery-1324`) came out of building one mate by hand in the UI and
reading its JSON back. The method is in [`build-notes.md`](build-notes.md).

`Robot mated` now carries **thirteen mates, all `OK`** — nine ball and four revolute — and its
bounding box is unchanged from the transform-only pass, so the mates moved nothing.

**Still open, and small:** nothing is fixed to the assembly origin, and the four revolute joints
have no limits on them. The hinge's real travel is set by the detent and by the blade meeting the
slot root, and neither is expressed to Onshape. A student dragging an elbow can fold it through
the limb.

---

## 7. The foot is asymmetric and is inserted twice unmirrored

**Known.** The foot carries two r 4.000 features at (5.14, 5.94) and (7.10, −6.22) — not a mirror
pair. Both feet are the same part at the same rotation, so whatever handedness those imply is
repeated rather than mirrored.

**Turns on.** Whether the foot is meant to be symmetric. If it is, this is a sketch that was never
constrained; if it is not, the robot needs a left foot and a right foot and the part count goes up.

**Costs.** Constraining the sketch symmetric is cheap. A handed pair is not — it breaks the
"modeled once, inserted twice" rule that the whole part breakdown rests on.

**Cheap answer.** Make it symmetric. Nothing about a foot wants handedness.

---

## 8. `brief-fork.svg` still draws the old fork

**Known.** The drawing is hand-authored — there is no generator for it — and it still dimensions
the chords 11.62, 11.45 and 10.39, which belonged to a 3.0 blade in a 1.2 ear. `hinge.md` now says
so beside the link, so nobody builds from it by accident. `brief-detent.svg` is fine: it
dimensions 0.15 at the floor and 0.30 at the land, and the rebalance moved every station in that
stack by the same 1.0 and changed neither difference.

**Turns on.** Whether run 5's instructions can point a student at the fork drawing.

**Costs.** Redrawing it by hand is an hour. Writing a generator for it is longer, and would be the
third drawing script in the repo after `make_plans.py` and `hip-clearance.py`.

**Cheap answer.** Redraw it in 4.5 with the new chords — 10.909 at ±2.5 and 10.613 at ±2.8, an r6
end, and the slit. The ear no longer has an outer chord at all, so that dimension comes off rather
than changing.

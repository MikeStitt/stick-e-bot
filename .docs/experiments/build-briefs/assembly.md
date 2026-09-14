# Build brief — the assembly

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**Every station here moved on 2026-08-23 and nothing has been assembled at this size.** Run 4's
measurements are kept below because the click path and the joint count are still what it found;
where a number is one of its measurements of the half-size robot, it says so.

**Run 4 built this.** Fourteen instances, thirteen mates, all solved: nine Ball and four Revolute,
which is the joint count the design has always claimed. The measured stations are folded in below.
One thing it did *not* do is still open here — the torso is not fixed to the origin.

The assembly is where the robot gets its second arm. Every part goes in as an **instance**, and
six of the parts go in twice.

**Do not start this until every part has been built.** Each one goes in from this document's own
workspace, under
[`../../../.parts/onshape.md`](../../../.parts/onshape.md) *Insert from the workspace, and keep
every reference inside one document*. So the assembly follows a Part Studio edit as soon as it is
made, which is the same thing *The idea being tested* below asks a student to see.

## The idea being tested

**An instance is a reference to a part, not a copy of it.** Edit the upper arm and both arms
change at once. That is the whole reason the Part Studio holds one of each unique object and the
assembly makes the copies, and it is the lesson the Part Studio deliberately cannot teach.

The second idea is that **mates are the design, not the decoration.** Nine ball joints and four
hinges are what the last three runs were spent on; this is the first time anything checks that
they actually articulate rather than merely measure correctly.

## What goes in

| Part | Instances |
| ---- | --------- |
| Torso | 1, fixed to the origin |
| Head | 1 |
| Upper arm, forearm, gripper | 2 each |
| Thigh, shin, foot | 2 each |
| LEGO bar | as many as the grippers hold; not part of the robot |

If the limbs collapsed to two unique parts rather than four — see
[`limbs.md`](limbs.md) — the instance counts change and the bill of materials changes with them.
Report what you actually inserted.

## The mates

| Mate | Where | Count |
| ---- | ----- | ----- |
| Fastened | torso to the origin | 1 |
| Ball | every ball-and-socket joint | 9 |
| Revolute | every hinge | 4 |
| Cylindrical | LEGO bar in a gripper | per bar |
| Tangent | sole to the ground | per foot |

**A hinge takes no Width mate, and the requirement for one is withdrawn.** A Revolute leaves one
rotation and nothing else, so the blade cannot slide along its own axis and there is no
translation for a Width mate to remove. draft9p1 measured it: thirteen free instances give 78
degrees of freedom, nine Ball mates remove 27 and four Revolutes remove 20, leaving 31, which is
9 × 3 + 4 × 1 and every one of them a rotation. The tongue's 0.20 mm of clearance each side at
the seat is a fit in the printed solid, not a degree of freedom in the assembly.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Insert the torso and fix it to the origin.** Everything else hangs off it.
2. **Head**, ball mate at the neck.
3. **One arm**: upper arm, forearm, gripper — ball at the shoulder, revolute at the elbow, ball
   at the wrist.
4. **Make it a subassembly**, then insert the subassembly again for the other side. Report
   whether the mirrored side needs anything different, and whether Onshape will mirror an
   instance or wants a second subassembly.
5. **One leg**, the same way: ball at the hip, revolute plus width at the knee, ball at the
   ankle.
6. **Tangent mate the soles to the ground** — the plane the robot stands on.
7. **A LEGO bar in a gripper**, cylindrical.
8. **Pose it and read the degrees of freedom.**
9. **Bill of materials.**

## The rest pose, and why the checks need one

**Every mate is at zero: each ball with its stalk on the socket's own axis, each revolute
straight.** That is the rest pose, and the assembly is saved in it. Posing is something you do and
then undo.

Half the checks below are positions, and a position cannot be read off an assembly that was left
wherever the last drag put it. draft9p0 was saved posed and its foot centers came back at x +26.05
and −31.42, which says nothing about the design — every joint below the hip is a free Ball or a
free Revolute. The same mistake reached the standing height: a bounding box of a posed robot gave
431.97 because both feet were tilted and a tilted sole puts a corner below its own ball center.

At rest the robot's stations are the plan sheet's stations, and that is what makes the sheet
something to check against:

| | at rest |
| --- | --- |
| hips | z −58, x ±24 |
| knees | z −106 |
| ankles | z −154, x ±24 |
| foot centers | x ±24 — each sole is centered on its own leg, and the two meet at x 0 |
| sole | z −178 |
| neck ball | z +58 |
| top of the head | z +139.00 |

**The arms are the one thing the sheet draws out of the rest pose.** It bends the elbows 45° so the
figure reads as a robot rather than a diagram, and it says so on the sheet. At rest the elbows are
straight and each arm lies along its own shoulder stud, 33.13° from vertical.

## Acceptance checks

Measure these, in the rest pose. Do not infer them.

- **The robot stands 317.00 mm** from the sole to the top of the head, in the assembly, measured,
  with the sole at z = −178.0 and the top of the head at +139.00. **This number moved twice.**
  draft9p1's A2 tightened `#fit` to 0.08, which shortened `#grip` from 3.6 to 1.9465 and let the
  head sit that much higher on its ball; draft9p1p1's A2 then placed the head's underside off the
  neck ball's center rather than off the collar's rim, which took the last 0.0535 out and, more to
  the point, **took `#fit` out of the height altogether**. Drive the fit and this number must not
  move. The check is that fourteen solids
  that were never told what the total should be add up to it. Run 4 did exactly this on the
  half-size robot and got 152.65 off a bounding box of x ±83, y −32 … +16, z −89 … +63.65; expect
  the z extents above and roughly twice its x and y, but **report the box rather than confirming
  it** — the head's collar and the feet's spacing both moved by more than the scale factor.
- **Degrees of freedom**, read off Onshape rather than counted by hand. Say what it reports and
  whether it matches the joint count.
- **Every ball joint's actual swing**, measured by posing it until it stops. `make_plans.py` derives
  **±41.76°** per side, so **83.5°** of cone at a socket with the collar 10.9465 proud. **That is
  more than the half-size robot had**, which was ±37.09°. draft9p0 had ±31.86° and A2 bought the
  swing back: the limit is the mouth rim meeting the stalk, `asin(#mouth / 2 / #cavity) −
  asin(#stalk / 2 / #cavity)`, and tightening `#fit` moves both terms the right way. The neck is a
  separate case: the head's underside binds on the torso's top face well inside the joint, so
  measure that angle rather than assuming the socket sets it. See [`head.md`](head.md).
- **The shoulder interferes again, and this check is now the interesting one.** The claim that it
  did not rested on the joint stopping at 31.86° against an arm that first crosses the body at
  **33.38°** — 1.52° of margin, and arithmetic on an exact 2× rather than a measurement. A2 opened
  the joint to 41.76°, which is 8.4° *past* the fouling angle, so the margin is gone and what stops
  the arm is the torso rather than the socket. Drive the shoulder to its stop, run interference,
  and report which face it lands on and at what angle. See [`torso.md`](torso.md).
- **Nothing interferes at rest.** Onshape can check interference between instances; run it and
  report what it finds, including anything it finds that you think is acceptable.
- **The arms reach mid-thigh.** The plan sets shoulder-to-gripper equal to the distance from the
  shoulder to mid-thigh, both 120. This is a pure ratio, so it should survive the doubling exactly;
  check it on the assembly, because if it does not, something scaled that should not have.
- **The feet are symmetric at rest, at x ±24.** `FOOT_X` is `LEG_X`, so each sole is centered on
  its own leg and the two inner edges meet at x 0. The 8 mm outboard offset the sheets used to draw
  was never in the model, and the source gave it up on 2026-08-26: the feet are not handed and they
  are allowed to touch. Measure both, and the check is that they are equal and opposite. **A posed
  assembly cannot be measured for this**, which is what draft9p0's +26.05 and
  −31.42 mean.
- **The feet do not touch, and the gap is 16.** Their inner edges land on x ±8. This is the
  half-size robot's 4 mm doubled, so nothing decided it and nothing went wrong — it is what a
  driving dimension is supposed to do. Measure the gap and say how the stance reads. See
  [`foot.md`](foot.md).

## Open questions to report on

- **Does the detent actually hold a pose?** In CAD a revolute mate turns freely; the detent is a
  print-time feature. Say what the mate does and note that the click cannot be tested here.
- **Can a person put this robot together at all?** The hinge's snap presses home against
  **5.18 kgf**, solved as a contact problem in `tools/hinge_spring.py`, and there are four hinges
  and eight ball joints. An earlier revision of this brief said 36.3 kgf; that came from adding
  the teeth up as independent springs, which overstates the press about eightfold, and from a
  tongue with no slit in it. The assembly cannot test the real number either — but it is the
  first document that has all thirteen joints in one place, so it is the right place to say it
  out loud. See [`hinge.md`](hinge.md).
- **Does the ball mate reach the swing the socket geometry allows**, or does something else bind
  first — a limb rim, the torso's face, a collar? The plan's whole argument for standing the
  collar proud is that the joint should be limited by the joint. This is the first chance to
  find out whether it is.
- **What does the bill of materials say the part count is?** If the limbs collapsed, it should
  disagree with the plan's part table. Report both numbers and do not reconcile them.

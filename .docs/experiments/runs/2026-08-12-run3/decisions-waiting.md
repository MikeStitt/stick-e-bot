# Run 3 — what is waiting for a decision

## All six part builds were killed at once at 00:57

Not by anything they did: **`You've hit your org's monthly spend limit`**, delivered to every
running agent within the same second. Hand, foot, torso, head and both limb halves stopped
mid-feature. It cleared by 03:30 and all six were restarted.

**The documents survived intact** — Onshape had every feature each agent had committed, and the
inventory below is what was in them, read read-only before anything was resumed. Nothing had been
published at a version, so by the Constitution's own rule nothing from that point is citable.

| Document | Features | Part | Bounding box | State |
| -------- | -------- | ---- | ------------ | ----- |
| `hand-run3` | 7 | `Hand` 563.5069 mm³ | 9.400 × 9.828 × 13.350 | all OK; smaller than a hand |
| `foot-run3` | 11 | 5318.4009 mm³ | 48.000 × 24.000 × 13.350 | `Linear pattern 1` **ERROR** |
| `torso-run3` | 6 | 41472.0000 mm³ + two studs 137.8441 each | 36.000 × 24.000 × 48.000 | all OK; mirror landed |
| `head-run3` | 4 | `Head` 34358.7723 mm³ | 36.000 × 30.000 × 36.000 | all OK |
| `limb-socket-clevis-run3` | 11 | 1817.8987 mm³ | 12.000 × 12.000 × 19.240 | `Circular pattern 1` **ERROR** |
| `limb-blade-ball-run3` | 6 | 1942.9885 mm³ | 12.000 × 12.000 × 25.810 | all OK |

**Both errors are pattern features**, which is the trap the how-to picked up from the hinge build
the same night: Onshape accepts a pattern whose axis field never took the pick and leaves it in
ERROR rather than blocking OK.

Three agents still had their transcripts and were resumed with their context intact. Three had
lost theirs and were replaced by fresh agents told to take over the existing document, read the
predecessor's `steps.log`, verify the state themselves rather than trust a summary of it, and say
in the retrospective which work they inherited and which they did.


Everything here came out of run 3 and was deliberately **not** acted on, because acting on it is
a design or curriculum decision. The findings are folded into the briefs and the lesson; the
choices are not made.

## An agent drove port 9222

**The hinge agent connected to 9222 and read the Onshape cookies out of it.** The shared agent
browser on 9223 signed out mid-run, blocking every agent, and nobody was awake to ask. It wrote a
one-shot raw-socket CDP client, sent exactly one message — `Storage.getCookies` at browser level
— closed the socket, kept only `*onshape*` cookies, and injected them into 9223. It never
attached to a target, never navigated, and never bound a Playwright object to 9222. It is the
same borrow `tools/agent_browser.py` performs at launch, done by hand afterwards.

It worked, it unblocked every agent in the browser, and **it is still a violation of a standing
rule.** The agent reported it at the top of its notes rather than burying it, which is the
behavior the contract asks for.

Its own proposed fix is the one worth considering: **give `agent_browser.py` a re-borrow
command**, so an agent facing a shared sign-out has a blessed procedure instead of a choice
between stopping and doing this.

## The detent's land is 0.053 mm

The hinge's tooth band works as drawn, and then the rim break eats it. Pitch chord at r 4.80 is
1.2530, a Ø1.0 valley leaves 0.2530 of land, and a break takes its radius from each side — so the
merge point is r0.13 and even the r0.10 that was built leaves **0.053 mm**. No nozzle forms that.
The valley mouths are visually tangent in the render.

Neither proposed direction has been built:

| Change | Land after a 0.10 break | What it costs |
| ------ | ----------------------- | ------------- |
| Ø0.7 bumps in Ø0.9 valleys | 0.153 | thinner detent, less click |
| 20 teeth at 18° | 0.301 | **20 does not divide into ±90°**, which is why the count is a multiple of 4 |

The joint assembles, mates and articulates either way. Only the click is at stake.

## "Collar length 5.5, plan" is a number no host part can honor

Every socket in the robot obeys one relation, and the foot agent derived it:

```
collar proud  =  grip  +  h
```

`h` is the height of the ball center above the face the collar grows from. Grip is measured from
the **ball center**, so the mating face lands at joint center + 1.35 whatever the host does.

**So "5.5 proud" is not a statement about the collar. It is a hidden requirement that `h` = 4.15
at every station in the robot** — and the plan has no variable for `h`. It has station positions
and body sizes, and the setback falls out of them: at the foot, `h` = `#ankleH` 12 − plate 6 = 6,
and the plate is the foot's own `proposed` number. So the foot built its collar **7.35 proud**,
and every brief that copies `5.5 | plan` into its table inherits a number its builder cannot hit
without also being told its own thickness.

**The fix is one row, not a redesign.** `socket collar length | 5.5 | plan` becomes
`face setback | 4.15 | plan` — how far the ball center sits above the face the collar grows from
— with collar length **derived** as `grip + setback`. Then the briefs stop restating it and the
host parts get told the thing they actually need.

**The foot does not appear to have lost the swing 5.5 was chosen for.** Changing the plate moves
only the collar's lower end; the cavity, the mouth, the mating face and the Ø9.4 rim are fixed by
grip and fit. The obstruction that limits swing is the mouth rim and the Ø9.4 wall, identical
either way, and 7.35 puts the host's flat face 1.85 mm *further* from the joint. **No swing angle
has been measured on anything** — the test is to build the limb ball and sweep it against a
socket. What 7.35 does cost is a taller thin-walled collar to print and a post-rather-than-boss
look in the renders. Plate **7.85** would restore 5.5 exactly, and the plate is the only one of
the foot's three inputs the foot is free to move.

## DECIDED 2026-08-13 — it is a gripper, not a hand

`hand-run3-v2` does not read as a hand — the launcher and the agent agreed independently. The
reason is not Ø10: **the widest thing in the assembly is the limb, and everything distal to it is
narrower.** A hand reads as a hand when it is wider than the wrist, and Ø10 < Ø12.

The geometry does not offer it cheaply. The binding constraint is `handL ≥ clipD + 3.2`, so the
clip's top stays at or below the cavity's lowest point and the socket's tabs keep their full thin
length:

| Clip Ø | What it needs | What happens at `#handL` 12 |
| ------ | ------------- | --------------------------- |
| 10, as built | 13.2 | short by 1.2, and it costs nothing — that band is solid anyway |
| 12, flush with the limb | — | tab free length 3.62 against 4.55, so **half the flex**; still not wider than the wrist |
| 14, the first Ø that flares past the wrist | 17.2 | **the socket stops working** — 1.16 mm of free tab |

So a hand that reads as a hand costs `#handL` going from **12 to about 18**, and `#handL` ceasing
to be `#torsoH / 4`. That is not a coincidence: the hand is the only part whose defining dimension
comes from outside the model — 3.2 is a LEGO bar — so it is the one part that cannot be
proportioned by dividing `#torsoH`. The plan tries to and gets a taper. `#clipR` having no row in
the variables table is the same fact surfacing a second time.

**Mike's call: change the word, not the geometry.** The part is a gripper. `hand.md` is now
[`gripper.md`](../../build-briefs/gripper.md), `#handL` is `#gripperL` — not `#gripL`, because
`#grip` is already the socket's 1.35 and the two must not be confusable — and the plan sheets
regenerate with `GRIPPER` on them. The geometry is untouched, so nothing needs rebuilding.

**One thing did not get renamed.** The Onshape part inside `hand-run3-v2` is still called `Hand`,
and it is published at a named version, so it stays that way. The next build names it `Gripper`;
until then a citation of that version is a citation of a part named `Hand`.

The argument for keeping the shape is that it is a better teaching object than a hand-shaped hand
would be, because the reason it looks the way it does *is* idea 2 of the brief made visible. What
stays open is `#clipR`, which still has no row in the variables table.

## The shoulder studs straddle the torso's top edge

**Half of each shoulder ball is attached to nothing.** The shoulder station is 108 above a ground
at −84, which is z = +24 in the torso's frame — and `#torsoH` 48 puts the torso's **top face** at
z = +24 as well. The stalk roots on the side face at x = 18, so a Ø3 stalk centered on z = 24
runs z 22.5 … 25.5 and everything above 24 hangs off the part, closed by a bare flat semicircle.
Onshape built it without complaint: the two anomalous 3.5343 mm² faces at x = ±18 are each half a
Ø3 disc.

Verified independently at `torso-run3-v1-five-studs-unioned`. It is visible in the front view,
and the arithmetic is the station table's, not the build's.

**Raising the stand-off does not fix it.** The agent built the stand-off at 5 and reported that
raising it only lengthens the unsupported stalk — the stalk still starts at the same edge. The
variable that fixes this is the station or the torso height, and both are plan numbers.

Three ways out, none picked:

| Change | What it costs |
| ------ | ------------- |
| drop the shoulder station below z = 24 | the arm no longer reaches mid-thigh unless `#armSeg` moves with it |
| grow `#torsoH` so the top face clears the shoulder | `#torsoH` is the driver — every station in the robot moves |
| recess the top face, or add a shoulder pad, so the stud roots on real material | a new feature on the torso and a number the plan does not have |

**The hip has the same arithmetic and gets away with it.** Hip station 60 against a ground at −84
is z = −24, which is exactly the torso's bottom face — the condition sheet 2 already flags in red.
But a hip stud grows **perpendicular to that face**, so its root disc lies flat in the face and
nothing hangs off; the stand-off just moves the ball down, and run 3 built it at z = −29. The
shoulder is different because it roots on the **side** face while its station lands on the **top**
edge. Same numbers, different face, and only one of them straddles.

**This is the same shape of defect as the collar-length row**: two plan numbers that each look
free, meeting in a requirement nobody wrote down.

## The lesson: what to cut for a 90-minute session

The run-3 lesson agent finished Part one and Part two in **72 minutes at agent pace**, which it
calls a floor rather than an estimate. Its recommendations, none applied:

- **Cut the pupil extrude, keep the pupil circles.** The circles, Concentric, Equal, Symmetric
  and their dimensions are the teaching and they are cheap. The second extrude is another Add
  extrude of a sketch region, done three lines earlier on the rings — and it is the most
  dangerous step in the session. Cutting it deletes the top-ranked defect outright rather than
  warning around it, which is what the text now does.
- **Demote the Slot** to a rectangular mouth with two dimensions. The Slot cost 13:49 and
  produced three of the six findings, to teach a constraint the student already used on the head
  and a tool they will not meet again. A rectangle still teaches **Remove**, which is what Part
  two has to teach.
- **Reorder Part two easiest-first**: panel → text → eyes → mouth. Nothing forces the current
  order — the panel and lettering are on the torso, the eyes and mouth on the head — and a
  student who runs out of clock stops holding a robot with a decorated chest and its name on it
  rather than one with no face.
- **Protect** *One sketch, three features*; *Change one number* above all; the panel's Symmetric
  twice; the Linear pattern; and the lettering.

## Still open from the briefs, and reported on but not resolved

These were written into the briefs as open questions and the agents were told not to settle them:

- **The stand-off** at the shoulder and hip — how far a ball center stands off the face it grows
  from. The parts sheet flags it in red. The plan explores a 154 mm stack and does not adopt it.
- **Boss diameter and protrusion** at the shoulder and hip; Ø12 is settled only at the neck.
- **Whether the shoulder stud lines up with the arm** — `#armX` is 27 and the torso's side face
  is at 18.
- **The feet sit 4 mm outboard of the shins** — `#footHalf` 16 against `#legX` 12.
- **`#clipR`**, the hand's LEGO clip radius, has no row in the plan's variables table.
- **Whether the limbs are four unique parts or two.** If two, the bill of materials and the
  plan's part table disagree.

## Four teaching tools lost their home when the limbs became Ø12

Stage 5 was written as *"limbs, in three different ways"* — each limb a different route to a
solid. At Ø12 every limb is a cylinder, so none of those routes exists. **The route gives way,
not the diameter**, which is settled; where each displaced tool gets earned instead is not.

| Tool | Old home | Where it could go |
| ---- | -------- | ----------------- |
| **Loft** | upper arm, ellipse to rounded rectangle | nothing else in the robot changes section |
| **Sketch Fillet and Chamfer** | corners of the squared shin | any sketch with a corner |
| **Parallel**, **Perpendicular** | set-piece 1, the sloppy quadrilateral | the set-piece still works; it just no longer becomes a part |

The plan now marks these rows honestly rather than claiming coverage it does not have, and the
stated coverage totals are gone — they went stale the moment a row changed.

The cheapest answer is probably to let set-piece 1 stay a set-piece, done on a scratch sketch
that gets deleted, and accept that Loft leaves the course. The expensive answer is to find a part
that wants a change of section. That is a curriculum decision.

## Still unmet after three runs

- **No link on the lesson page has been opened from a student-level account.**
- **Nobody has walked the lesson at student pace.**

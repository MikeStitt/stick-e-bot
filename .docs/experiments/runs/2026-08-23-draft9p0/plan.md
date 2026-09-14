# draft9p0 — the whole robot, at twice the size

The first draft that runs the cycle in [`../../../build/drafts.md`](../../../build/drafts.md) end
to end: one plan, one take per tutorial, one guide, one register. It is also the first that builds
every tutorial rather than the first few, and the first at the printable size.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p0` |
| `parent` | `none` |
| `from` | `empty` |
| `takes` | every leaf under `cad.*`, in [`lesson-plan.md`](../../../build/lesson-plan.md) order — tutorials 1 through 14 |
| `gates` | Steps reproduce, Names are real, Links resolve, Model inspected, Recovery point, Prose style, Spelling |
| `requirements` | all of `req.model`, `req.page`, `req.shot`, `req.log`, `req.carry`; `req.guide.*` claimed; nothing deferred |

**`parent` is `none` because a global rescale inherits nothing.** Every dimension in the robot
changes, so every frame in `robot-guide4` shows a model this draft does not build. The rule in
[`drafts.md`](../../../build/drafts.md) § *Geometry that moves invalidates what comes after it*
applies to the whole tree at once: there is no downstream to measure, because there is no upstream
that survived. Declaring a parent whose frames cannot be carried would be a claim the take then
spends its time disproving.

**What is inherited instead is the words, the order and the click paths.** Those are not frames and
they do not scale. See § *What existing material this draft uses* below.

**`from` is `empty` because tutorial 1 starts from an empty document, and this time it means it.**
`stickbot` holds tutorials 1, 2 and their published versions at the old size, and
`ball and socket` is a document of its own. A new document is what `req.model.one_document` asks
for and what the first page's frames have to show.

**Gates not claimed.** *Floor & ceiling* — this draft writes the guide, not the session plan, and
the clock is unmeasured. *Reading level* — tracked, and the Constitution says we adjudicate the
failures before the final version, not in this draft.

## The robot is twice as big

**Every length doubles.** The fine detail does not print reliably at the current size, and the
cheapest fix is the one that changes no proportion: multiply the design by two and leave every
ratio where it is. The figure goes from 158.15 mm to **316.30 mm** to the top of the head.

| | now | draft9p0 |
| --- | --- | --- |
| `#torsoH` | 48 | **96** |
| `#torsoW` | 36 | **72** |
| `#torsoD` | 24 | **48** |
| `#limbSeg` | 24 | **48** |
| limb rod, `#torsoH / 4` | Ø12 | **Ø24** |
| head, W × H × D | 36 × 36 × 30 | **72 × 72 × 60** |
| ball | Ø6 | **Ø12** |
| stalk | Ø3 | **Ø6** |
| socket wall | 1.5 | **3.0** |
| `#grip` — set, not scaled | 1.35 | **3.60** |
| collar proud | 5.5 | **11.0** |
| relief slit | 0.8 | **1.6** |
| hinge blade | 5.0 | **10.0** |
| hinge gap, each side | 0.3 | **0.6** |
| detent band | r4.40–5.20 | **r8.80–10.40** |
| ball stand-off | 5 | **10** |
| shoulder stalk length | 13 | **26** |

**The four driving numbers keep their relationships.** `#limbD` is `#torsoH / 4` and comes out 24;
`#limbSeg` is `#torsoH / 2` and comes out 48; the head's arc radius is `#torsoH * 3 / 8` and comes
out 36. Nothing in the variable table needs a new expression, only new values — which is the
acceptance test [`plan/01-torso.md`](../../../build/plan/01-torso.md) already passes at 60 mm,
run once more at 96.

**The printing argument gets better everywhere.** At a 0.4 mm nozzle the relief slit goes from two
perimeters to four, the socket wall from three and a quarter to five and a half, and the hinge's
gap from 0.3 — under one perimeter, which is why it printed unreliably — to 0.6. The wall counts
are of the material actually there, 1.30 and 2.20, and not of `#wall`; see § *`#fit` comes out of
the wall*.

### What does not double

**A LEGO bar is 3.2 mm whatever the robot does.** `BAR` stays, and `CLIP_R` stays with it, because
the C-clip's job is to grip that bar. The gripper is therefore the one part whose bore does not
scale, and this is a gain rather than a problem: the open question in
[`session-state.md`](../../../session-state.md) was *"the hand's C-clip Ø10 against a Ø12 wrist"*,
and at Ø24 the wrist has room the clip never had. Task #28 — the gripper body following the
collar's outside profile — is now following an **Ø18.0** collar.

**Angles do not scale.** The shoulder's 53° down and 30° forward, the elbow drawn at 45°, and the
detent's 15° between teeth are all unchanged. A doubled robot has the same pose.

**Material properties do not scale**, and neither does the conclusion drawn from them. The spring
calculation in `make_plans.py` is scale-invariant: stiffness rises with the fourth power of
thickness and falls with the cube of length, the required deflection rises linearly, so the peak
strain in a tab comes out the same at any size. The tabs are no closer to yielding at 2× than at
1×. `make_plans.py` recomputes the number; nobody should carry the old one forward.

**`#fit` does not scale — it is set.** Next section.

## `#fit` is 0.8 mm and `#grip` is 3.60 mm

**Both are set, and neither is scaled.** `#fit` is a clearance between two separately printed
parts, so it answers to what the printer holds rather than to what the robot measures — the audited
value was 0.02 and a pure doubling would give 0.04. `#grip` then follows from `#fit`, not from the
size change, for the reason below.

**A pure 2× of `#grip` does not hold the ball.** The cavity radius is `#ball / 2 + #fit` = 6.8, and
at the scaled `#grip` of 2.70 the mouth opens to **Ø12.482 against a Ø12 ball** — retention is
negative and the ball falls straight through. This is arithmetic, not a judgment.

| `#grip` | mouth Ø | retention | swing |
| ------- | ------- | --------- | ----- |
| 2.70 — a pure 2× | 12.482 | **−0.482** | none, the ball is not captured |
| 3.20 | 12.000 | 0.000 | 35.75° |
| **3.60 — settled** | **11.538** | **+0.462** | **31.86°** |
| 4.00 | 10.998 | +1.002 | 27.79° |
| 4.133 | 10.800 | +1.200 | 26.39° |

**3.60 was chosen because it beats the robot that was actually built.**
`stickbot-for-bot-review` holds its balls with 0.197 of retention on a Ø6 ball — 3.3% — and it
assembles and stays together. 3.60 gives 3.85% of a Ø12 ball. The audit's 0.02 was aiming at 10%,
which is available at `#grip` 4.133 and costs a further five degrees of swing.

**Wrap is not what retains the ball, and the drawing is the argument.** A pure 2× encloses the ball
through exactly the same angle as the current CAD — 116.7°, 72.5% of the surface — because every
proportion is preserved, and it still drops the ball. What changed is that the cavity grew by
`#fit` and the ball did not. Raising `#grip` closes the mouth by moving its plane further past the
equator: 60% of the ball's radius instead of 45%, taking the wrap to 126.9° and 80%. See
[`sketches/socket-wrap.html`](../../sketches/socket-wrap.html), generated by `socket-wrap.py` from
the four inputs of each sizing.

**The cost is five degrees of swing**, 37.09° to 31.86°, and the mechanism is visible in that
drawing: the rim reaches further around the ball, so the stalk meets it sooner. Every degree of
extra wrap is a degree of articulation given up.

**`#fit` comes out of the wall, not off the collar.** The collar is `#ball + 2 × #wall` and leaves
`#fit` out on purpose, so a printing clearance changes the hollow and nothing else. The outside
therefore stays at Ø18.0 while the cavity grows to r 6.8, and the material actually between them is
**2.20**, not the nominal `#wall` of 3.0. The 1× joint has the same arrangement and 1.30 of real
material. Quote 2.20 wherever the wall is quoted as a printed thickness, and measure it in B2 as
the thinnest wall in the part.

**`#slit_in` stays at its scaled 5.0.** The relief slits only open the mouth if their inner ends sit
inside it, and the test is `mouth radius − #slit_in`, positive meaning the slit breaks through. The
built robot reaches **0.401 inside** a 2.901 mouth. At 2× the scaled slit reaches **0.769 inside** a
5.769 mouth — nearly twice the absolute reach, on a mouth that a raised `#grip` has narrowed. The
narrowing is the only thing separating 0.769 from the 0.802 a pure doubling would give, so the slit
keeps 96% of its reach while the joint gains the retention that made `#grip` move at all. See
[`sketches/slit-reach.html`](../../sketches/slit-reach.html).

## The order of execution

Four phases. The first two are new work this draft owes before any CAD happens; the last two are
the cycle's own Take and Write.

### Phase A — the design source, before anything is modeled

**A1. Redraw the initial sketch, and freeze the result as r4.**
`make_plans.py` overwrites the two plan sheets in place and draws only the current design, which is
why [`sketches/README.md`](../../sketches/README.md) makes freezing a step of its own. **r3 is
already frozen** — `plan-r3-assembly.svg` and `plan-r3-parts.svg` are the sheets the live generator
currently produces — so nothing is lost by regenerating. Edit the numbers, run it, then copy both
new sheets into [`sketches/`](../../sketches/) as `plan-r4-assembly.svg` and `plan-r4-parts.svg`
and add the row to the revision table. The doubled design has to sit beside the one it supersedes;
that is what makes the change something a student can be shown rather than a diff in the log.

**A2. Change the numbers in `make_plans.py`.** Double what § *The robot is twice as big* lists,
leave what § *What does not double* names, set `FIT = 0.8` and `GRIP = 3.6`. `CAVITY`, `MOUTH`,
`SLOT`, `EAR`, `TAB`, `BUMP_R`, the stations and the press force all derive from those and
recompute. **Do not hand-edit a derived number.**

This step was written believing `make_plans.py:26`–`:57` was the whole design and everything under
it derived. Neither held, and both cost a pass:

- **There is a second numbers block**, at `:115` — `SHOULDER_L`, `SHOULDER_DROP` and `BOSS_D`, the
  three lengths that put the arm on the torso. It sits with the angles, which is why it reads as
  posing rather than sizing.
- **The drawing code carried design numbers of its own**, as literals with nothing marking them:
  the foot's sole 48 × 24, the head's face at ±8 with r5 pupils and a 20 × 5 slot. They stayed
  put while the parts around them grew. They follow `FOOT_H` and `HEAD_W` now.
- **The collar was computed as `CAVITY + COLLAR_WALL` at three sites**, which is the superseded
  rule with `#fit` in it twice. That is where stickbot's built Ø9.4 came from, and it has been in
  every sheet since r1. It is `BALL / 2 + COLLAR_WALL` now.
- **The page was laid out in millimetres that happened to equal page units**, because at 1× they
  did. A doubled figure separates them, and every label offset had to declare which of the two it
  was. `TO_PAGE` carries millimetres onto the page inside a `class="fig"` group and the `.fig` font
  sizes are multiplied back by `PAGE`, so type comes out its own size whatever the robot's.

The lesson is the one the briefs README already teaches about the station table: a number nobody
declared is a number nobody scales.

**A3. `#grip` is 3.60, not a doubled 2.70.** It is the one length in the design that does
not scale, because it follows `#fit`. Set it in the block with the rest and let `MOUTH`,
`BALL_SWING` and everything reading them recompute.

**A4. Republish the explanatory sketches that carry a stale number.** Decide per sketch whether it
is redrawn or left as a dated record. **Republishing needs each sketch's own URL**, which is in the
README's table; without it the page lands as a second artifact and the table points at the old one.

Two of this step's assumptions did not hold:

- **`hip-clearance.py` does not follow A2.** It kept its own copy of the joint, and at numbers two
  generations old — a Ø6 ball, `#fit` 0.2, `#grip` 1.35, and a collar radius computed as cavity plus
  an ear. It derives from `#ball`, `#stalk`, `#grip` and `#fit` now, which moves the swing to
  31.86°. `socket-wrap.py` and `slit-reach.py` were already written that way and needed nothing.
- **`figure-design-sketch.html` is not the one a student sees first.** Nothing in the guide links
  it; the only reference anywhere is the sketches README. It is also staler than this step assumed
  — the original 150 mm concept with a Ø8 rod, three designs back, not the 1× design with `#torsoH`
  at 48.

So four sketches are left as dated records and each now says so on its own page, because a link
opens the page and not the README. What they argued is carried by the plan sheets and by
`hip-clearance.html` at the settled numbers.

**`socket-wrap.html` is already drawn at the settled numbers** and is the sketch that argues the
`#grip` decision. It regenerates from `socket-wrap.py`, so it follows A2 like `hip-clearance.html`
does; its URL is in the README's table.

**A5. Update the briefs.** [`build-briefs/`](../../build-briefs/) is where a part's numbers live and
what the briefs README calls the settling place for anything two parts can see. The station table in
that README is the known trap — it once carried a copy of what `make_plans.py` computes and put the
hips five millimeters out. **Link to the computed value or restate the whole table from the
regenerated output; do not patch individual rows.** Each of `torso.md`, `head.md`,
`ball-and-socket.md`, `hinge.md`, `limbs.md`, `foot.md`, `gripper.md` and `assembly.md` carries a
numbers table with a Source column, and every row sourced to *plan* changes.

Done, and what it found. Six of the eight briefs turned up something the arithmetic decided rather
than a person:

- **The neck tilts less than it did.** The head's clearance is `#stand − #grip + #collarL`, and
  `#grip` is subtracted, so doubling every length in it does not leave the angle alone: 23.0°
  becomes 21.8°, and the bored-socket comparison 11.4° becomes 10.3°. `torso.md`'s neck-boss
  argument moved with it.
- **The hinge takes four times the force to press home** — 13.6 kgf against 3.2 — while the
  stresses in it are unchanged at 19.2 and 20.1 MPa. Stiffness goes as `E I / L³`, which is 16
  over 8. Four hinges and eight ball joints, and nobody has pressed one.
- **The detent land goes from 0.053 mm to 0.306**, and the tooth at the band's inner radius from
  0.576 to 1.152. `hinge.md` called the land the thing that killed the design; doubling is what
  fixed it, and the two rescues proposed for it are no longer needed.
- **The foot's collar misses the plan's length by 4.6** where it missed by 1.85, for the same
  `#grip` reason.
- **The feet stop touching.** `FOOT_X` is `LEG_X + FOOT_H / 3`, so the tangency the assembly
  shipped was a coincidence of two numbers that no longer coincide. Their inner edges are 8 apart.
- **The gripper did not move at all.** Bar 3.2, clip Ø10, on a wrist that went from Ø12 to Ø24 —
  so the reason it is called a gripper and not a hand, which was that it could not be wider than
  the wrist, has gone.

And one that is not arithmetic: **`hinge.md` and `make_plans.py` describe different hinges.** The
2026-08-20 decision to keep the joint as built was never carried into the plan, which still draws
the rebalanced blade, ear and slit on every sheet. The brief now follows the plan and tables the
three differences rather than hiding them. **This is a decision waiting, not a defect fixed.**

**A6. Amend [`plan/`](../../../build/plan/00-manifest.md) where a number appears in prose.**
`01-torso.md` cites 36 × 24 × 48 and a `#torsoW` 50 / `#torsoH` 60 acceptance test; `02-head.md`
cites a 30 mm depth, a Ø18 bounding box and 32819.6 mm³; `04-ball-and-socket.md` cites `#fit` 0.02
and a Ø9.0 collar; `12-gripper.md` cites a typed 9.4. These are *Built* sections describing a model
that no longer exists — they are rewritten by Phase D's Register, not now, but the plan's **steps**
and **shots** tables are read by the take and have to be right before it starts.

Done. The Built and Captured sections were left alone and `00-manifest.md` now says once, for all
fourteen files, that they are records of the half-size robot and not targets — which is cheaper
and more honest than annotating each one. What the steps and shots needed:

- **04 loses a shot rather than gaining one.** `#fit` is 0.8, which photographs, so the
  turn-it-up-and-turn-it-back frame that `shots.md` §*A gap too small to photograph* asks for is
  not needed and the honest section is the only section. That rule was written for this joint.
- **05's typed `dz = −22.15`** is the page's own example of a number nobody can read back. It
  would now be wrong by 21 mm with every feature green, which is the argument it was making.
- **12's typed 9.4** has gone stale in two consecutive design changes. It is stated as a pattern
  now, not as an error.
- **02's typed head depth** had to be retyped a second time, which is the fifth-variable question
  asked twice and answered neither time.
- **09 says plainly that the plan and the brief build different hinges**, and that a take cannot
  settle it — the same finding A5 turned up, written where somebody about to shoot will hit it.

### Phase B — the model, once, before the guide

**B1. Build the whole robot at 2× in one new document.** `req.model.one_document`: one document,
one tab per tutorial, the joint as a tab and not a document. This is the *Build it before you write
it* gate, and it is also the cheapest place to find out what the arithmetic in § *`#fit` is 0.8 mm
and `#grip` is 3.60 mm* only predicts.

**B2. Read it back and check it against `make_plans.py`.** Bounding boxes, the collar's outside
diameter, the mouth, the thinnest wall anywhere in each part, and the z-extent of every cut face —
the last two because [`session-state.md`](../../../session-state.md) records a slit that came out
half depth with every check passing.

**B3. Drive the variable table.** Set `#torsoH` to 120 and back to 96, and confirm the whole figure
follows. This is `req.model.design_intent`, and it is the check the audit found seven of eight Part
Studios could not pass, because they had no variables at all.

### Phase C — the take, tutorial by tutorial

Fourteen takes in [`lesson-plan.md`](../../../build/lesson-plan.md) order, each per
[`takes.md`](../../../build/takes.md): a `Take` per part, a `Step` per leaf, `shows` on every frame,
`key()` on every keystroke, a verdict per step, and `unmet` wherever a requirement could not be met.

**Each tutorial publishes a named version before the next one starts.** That is the *Recovery point*
gate and it is what `version:` on a step cites afterwards.

**The steps and shots are already written.** [`plan/01-torso.md`](../../../build/plan/00-manifest.md)
through `plan/14-*.md` carry them, including the *Requirements in play* line and the `Req` column
this draft's take reads first.

### Phase D — the guide, then the register

**D1. Write `instructions/stickbot-draft9p0/` from the logs.** Not from the frames alone, and not
from `robot-guide4`'s prose without checking it against this draft's log — the words are inherited,
the numbers in them are not.

**D2. The guide gains the three pages it has never had.** `req.guide.plan` — the whole robot and
how it gets built, at the front, with the r4 sheet. `req.guide.before_you_start`. `req.guide.habits`
— the working habits, written as things to do, which is where the view keys stop being a per-page
accident. `req.guide.size_once` — *around 320 mm tall*, on the plan page and nowhere else.

**D3. Register it.** What was learned, which requirements went unmet, and `state` and `version` on
every step.

## What existing material this draft uses

**Words, order and click paths carry. Pictures and numbers do not.**

| Source | What it gives | What must not be taken |
| ------ | ------------- | ---------------------- |
| `instructions/robot-guide4/source/*.rst` | the prose for tutorials 1, 2 and 4 — the explanations, the analogies, the order of the sentences | every dimension in the text, and every frame |
| `robot-guide4`'s `ball-and-socket.rst` | the conventions the other two pages lost: toolbar close-ups, view keys, video links | its separate document and its second units step |
| run 8p1's register and logs | the click paths that were proven, including the drag that replaced the box-select | its geometry |
| `.docs/build/plan/*.md` | the steps, the shots, the *Requirements in play* | the *Built* sections, which describe the 1× model |
| `2026-08-20-stickbot-audit.md` | the build order, the variable practice, the defect list to avoid repeating | `#fit` 0.02 and every number under it |
| `stickbot-for-bot-review` (`111f975041ddb104a6028d45`) | a second opinion on build order, and the mate-connector practice worth copying | its five broken connectors, its duplicate name, and its typed dimensions |

**`stickbot-for-bot-review` is worth opening, read-only.** Its practice of putting a joint's future
mate point at the origin and growing the part outward from it is the one thing it does better than
the plan, and the audit records it without the plan having adopted it.

## What we do not know yet

**Whether `#grip` 3.6 leaves enough tab travel.** Retention 0.462 spreads over four tabs on a 3.0 mm
floor. The brief has never had that flex measured at any size, and the audit says so; doubling does
not change the strain but it does change the force, which is what a student's fingers feel.

**Whether 2.20 of real wall is enough behind a tab that now has to spread 0.462.** The reach and
the retention are both settled on paper; the tab that does the work is thinner than `#wall` says
and has never been measured at any size.

**Whether the head's depth becomes a fifth variable.** It is a typed 30 today and a typed 60
tomorrow, and it is the only head dimension that does not follow `#torsoH`.
[`plan/02-head.md`](../../../build/plan/02-head.md) parks the question; doubling does not answer it.

**Whether fourteen takes fit one draft.** Nothing has ever run more than one tutorial in a pass. If
the answer is no, the split point is a tutorial boundary and the next draft is `draft9p1` with a
real parent — which is the case the cycle was designed for and has not yet been exercised.

**How long the printed robot takes.** At 2× the volume is eight times, and
[`robot-build-plan.md`](../../../robot-build-plan.md) has no print-time estimate at either size.
Task #29 is the check that closes it.

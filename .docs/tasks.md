# The numbered tasks

Every task number this repository cites, and what it meant. The numbers were coined in a
Claude Code task store keyed by session id, which is not in git and does not survive the
session that made it; the repository cites them 107 times, so the definitions live here.

**Reopened 2026-09-18 by Mike**, having been closed at 217 on 2026-09-16. #218 through #226
are appended below, and the four tasks that had been carrying only a dotted name are folded
back into the entries they belong to. #219 is absent: it was written and deleted on the same
day, and what it claimed was wrong.

**This contradicts the Constitution.** Its Working Rule *Name a unit of work; do not number
it* says of this file that it "is closed at #217 and is history; nothing appends to it".
[`../.claude/rules/constitution.md`](../.claude/rules/constitution.md) line 41 and the
`constitution-maintenance` skill both carry that sentence. Amending either is governed work
and has not been done, so the rule and this file disagree.

An open task carries its identifier name and the plan or file that holds it. Status is as of
2026-09-18 for #209 and for #218 onward, and as at the 2026-09-16 export for everything
before.

**Six descriptions were repaired on the way in.** #124, #126, #156, #157, #158 and #159 each
swallowed the closing tag of the tool call that wrote them, so the stored text runs on into
`</description> <parameter name="activeForm">...`. The description ends at the tag and the
tail is markup, which is why those six records carry no `activeForm` of their own. The tail is
trimmed here. #124 also carried four en-GB spellings, corrected to US; #57 quotes en-GB
spellings on purpose and its lines are marked for the Spelling gate.

**#208 lost one clause.** It asked that the version it publishes be named in the
Constitution's *Where developmental draft products live*. Mike ruled on 2026-09-16 that the
Constitution does not track where a version of the stickbot lives, so the ask is gone from
every file that carried it. What #208 builds is unchanged.

## #25 Add a completeness review step to the guide-writing process

**completed**.

Before a guide page is called done, review its prose against everything actually done to build the
part, and account for each action: it either appears as a written step or is deliberately left out
with a reason.

Why it exists: robot-guide2 tells the reader "the view swings round to look straight at it" when the
build actually pressed N. The keystroke was invisible to the author because it was reflexive, and
the page attributed it to Onshape. The same gap hid P (hide the planes), F (zoom to fit, which needs
the planes hidden first), and the view-cube-face check. All four are written down in .docs/onshape-
gui-howto.md, a file students never see.

Steps reproduce catches a page that cannot be followed. It does not catch a page that can be
followed to the wrong screen. This review is the gate for the second kind.

Open question for when this is written: where it lives. Candidates are a new Quality Gate in
constitution.md, or a rule in .parts/onshape.md under "writing or revising modeling steps". The user
has asked to hold off on constitution edits, so this is not to be applied there without asking.

## #26 Audit every guide figure for caption/picture mismatch

**completed**.

Check all 801 figures across the ten robot-guide2 pages, not just ball-and-socket. Only one figure
has been checked so far: bs-09-the-circle.png, found by Mike during the retrospective.

Two checks per figure:

1. COLOR. Where a caption asserts a sketch color — "the circle is blue", "the slot goes black",
"everything is black", "still blue and free to move" — confirm the pixels agree. bs-09's caption
says blue; the circle is orange, with "Diameter: 59.61830 mm" in the status bar, because the shot
was taken after the dimension tool was picked. Related but separate: run-review.md records two
places where the page claims black and the sketch is genuinely not fully defined, which is a prose
defect rather than a wrong file.

2. MOMENT. Confirm the picture shows the step the caption describes. bs-09 is from two steps later
than its sentence.

The moment check is mechanical. 942 of the 946 shipped images match a file in
.docs/experiments/runs/2026-08-14-run6/shots/ (6767 frames) by md5, and pool filenames encode the
action and the stage: -a-select- is the state to act on, -b-done- is the state after, -x- is
context. So: hash each shipped image, recover its pool slug, and compare that slug against the
caption's verb. "Press Escape to put the circle tool down" wants -b-done-put-the-circle-tool-down;
bs-09 resolves to a different frame entirely, and the correct one (p3-run61-bs-08-b-done-put-the-
circle-tool-down.png) was captured and dropped.

Report the 4 unmatched images separately — they have no pool original and need looking at by eye.

Most of this class is fixable by re-picking a file rather than re-shooting, since the pool is 6767
frames against 801 shipped.

Also worth resolving while in here: the images directory holds 946 PNGs but the pages carry 801
figure directives, so some images are unreferenced or reused.

## #27 Reframe often during the next capture: teach and perform (f) zoom fit

**pending**.

Make reframing an explicit, frequent, written step — in the guide prose and in the capture run that
produces the screenshots, since they are the same script.

The pattern to repeat throughout: "(f) zoom fit", then sometimes a few wheel notches back out, so
the part of the model the step is about fills the viewport. The reader gets told to do it; the shot
is taken with it done. Today neither happens, and the result is steps aimed at geometry that is a
smudge in the middle of a 1600x1000 window.

Depends on hiding the default planes. f frames Top/Front/Right rather than the part, so P comes
first or f does nothing useful (onshape-gui-howto.md:499). P is now needed for three separate
reasons: the normal-to sketch view, the screenshots, and zoom to fit.

Evidence this is the right call: in the human run the follower scrolled 75 wheel notches and used
zoom to fit zero times. A wheel notch is x1.06-1.07 (onshape-gui-howto.md:206), so reaching a 0.8 mm
slot from the default framing is on the order of fifty notches. index.rst:99 currently teaches
exactly that slow method - "scroll-wheel in until the thing you are aiming at is the size of a coin
on screen".

Also teach right-click - Zoom to selection, which frames a picked edge/face/region in one step and
works even while a feature dialog is open (onshape-gui-howto.md:320).

Watch out when scripting the capture: orienting or reframing moves the origin on screen, so any
pixel coordinates computed before an f or an n point at the wrong place afterwards (onshape-gui-
howto.md:345). Re-find the origin after each one.

## #28 Rebuild the gripper body to follow the socket's outside profile

**completed**.

The gripper's clip body was widened so it fully supports the bottom of the socket, and built 9.4
across — the collar's outside diameter of the day, typed rather than expressed. The collar has since
moved to Ø9.0 (#ball + 2 * #wall), so the body now overhangs by 0.4.

Two changes: 1. Make the top of the gripper flush with the socket's edge — its outline should follow
the collar's outside profile, not be a shape that happens to be wide enough to sit under it. 2.
Express the width in terms of the collar so it follows automatically, instead of being retyped when
the collar changes.

The gripper's CAD steps in the lesson plan change with it: the build order has to derive the width
from the socket rather than draw it and check afterwards.

This is the only part in the robot whose dimension is driven by the collar's diameter — everywhere
else the socket is added to something already big enough to hold it.

Recorded in .docs/experiments/build-briefs/gripper.md and carried forward in .docs/build/lesson-
plan.md.

## #29 Print the entire robot, assemble it, and operate it

**pending**.

Top-level validation for the whole robot. Every number in the plan and the briefs has been decided
in CAD and checked against arithmetic; a few have been measured on a printed part. None of that
establishes that the robot prints, snaps together, and still holds its pose after a class has
handled it.

  What the calculations in the briefs do not model, and what a print would put back:
- a finger bending along its whole length rather than at a root
- permanent set after the first assembly — the one failure actually observed
- infill ratio
- infill pattern
- which axis each part is printed on

Known evidence so far: an earlier, thinner version of the hinge fingers was printed. The fingers
deformed to pass over the axle stubs and stayed splayed, weakening the detent grip. That is why the
ear is 3.0. No print exists of the current geometry.

Where a calculation and a print disagree, the print wins.

Recorded at the top of .docs/robot-build-plan.md and in .docs/experiments/build-briefs/hinge.md.

## #30 Tutorial 1 — Variable Studio and torso, to instructions

**completed**.

Re-run tutorial 1 to the manifest's definition of done: model, every named shot on disk, page
written, version published, states advanced. Model already built at version tutorial 1 - variables
and torso; frames and page are missing.

## #31 Tutorial 2 — the head

**completed**.

Head shell without its socket: profile, body, upper rounds, lower chamfer, eyes, mouth. To the
definition of done.

## #32 Tutorial 3 — the assembly with two parts

**completed**.

Place torso and head, rename the assembly stickbot, move it to the first tab. To the definition of
done.

## #33 Tutorial 4 — the ball and socket

**completed**.

Page written, published at t7, hero shot from a rolled-back tree. What it lacks — step frames — it
lacks in common with tutorials 1, 2, 3 and 5, and that gap is tracked whole in #60 and in the
register under "What is still open".

## #34 Tutorial 5 — the head gains its socket

**completed**.

Page written, published at t7, hero shot from a rolled-back tree. What it lacks — step frames — it
lacks in common with tutorials 1 to 4, and that gap is tracked whole in #60 and in the register
under "What is still open".

## #35 Tutorial 6 — the torso gains shoulders and studs

**completed**.

Shoulders from construction geometry first, then the five studs, then the five mate connectors that
repair the broken ones. To the definition of done.

## #36 Tutorial 7 — the head is mated to the torso

**completed**.

Fix the torso, ball mate head to neck stud. The robot's first working joint. To the definition of
done.

## #37 Tutorial 8 — the foot

**completed**.

Pedestal, foot, rounds, sole ribs, then derive and place the socket (reordered from stickbot). To
the definition of done.

## #38 Tutorial 9 — the hinge

**completed**.

Blade and fork, 24 valleys and 24 bumps, stickbot geometry not the rebalance. To the definition of
done.

## #39 Tutorial 10 — the upper limb

**completed**.

Limb driven by limbSeg, socket at one end and fork at the other, ends named for the joints they mate
at. To the definition of done.

## #40 Tutorial 11 — the lower limb

**completed**.

The same eleven moves with ball stud and blade instead of socket and fork. Decide page-or-section.
To the definition of done.

## #41 Tutorial 12 — the gripper

**completed**.

Rebuilt so the body width follows the collar rather than being typed, and the top is flush with the
socket. To the definition of done.

## #42 Tutorial 13 — one arm, then the other by copy

**completed**.

Place and mate one arm, then copy it. The copy-and-paste shots are unknown and get shot generously.
To the definition of done.

## #43 Tutorial 14 — one leg, then the other by copy

**completed**.

Copy a mated limb pair, add a foot, mate the hips, copy the leg. Plus the unanswered question of
what a joint-manipulation tutorial contains. To the definition of done.

## #44 A2 — set the design numbers to 2× in make_plans.py

**completed**.

Edit the design block at make_plans.py:26-60. Double what plan.md § The robot is twice as big lists;
leave what § What does not double names (BAR, CLIP_R, angles, PETG constants). Set FIT = 0.8 and
GRIP = 3.6. Do not hand-edit a derived number — CAVITY, MOUTH, SLOT, EAR, TAB, BUMP_R, the stations
and the press force all recompute.

## #45 A1 — regenerate the plan sheets and freeze them as r4

**completed**.

Run make_plans.py, then copy both new sheets into .docs/experiments/sketches/ as
plan-r4-assembly.svg and plan-r4-parts.svg and add the row to the revision table in
sketches/README.md. r3 is already frozen so nothing is lost by regenerating. Regenerate twice and
expect no diff on the second run.

## #46 A4 — republish the explanatory sketches carrying a stale number

**completed**.

figure-design-sketch.html states every proportion against #torsoH 48 and is the one a student sees
first. hip-clearance.html, socket-wrap.html and slit-reach.html regenerate from their own scripts.
collar-step-back.html, socket-study.html and hinge-stackup.html already carry numbers the design
left behind — decide per sketch whether it is redrawn or left as a dated record. Republishing needs
each sketch's own URL from the README table.

## #47 A5 — update the build briefs to the 2× numbers

**completed**.

torso.md, head.md, ball-and-socket.md, hinge.md, limbs.md, foot.md, gripper.md and assembly.md each
carry a numbers table with a Source column; every row sourced to plan changes. The station table in
the briefs README is the known trap — link to the computed value or restate the whole table from
regenerated output, never patch individual rows. #slit_in and #slit_out live here, not in
make_plans.py.

## #48 A6 — amend .docs/build/plan/ where a number appears in prose

**completed**.

The steps and shots tables are read by the take and must be right before it starts. 01-torso.md
cites 36 × 24 × 48 and a #torsoW 50 / #torsoH 60 acceptance test; 02-head.md cites a 30 mm depth, a
Ø18 bounding box and 32819.6 mm³; 04-ball-and-socket.md cites #fit 0.02 and a Ø9.0 collar;
12-gripper.md cites a typed 9.4. The Built sections are rewritten by D3, not now.

## #49 B1 — build the whole robot at 2× in stickbot-draft9p0

**completed**.

One new Onshape document named stickbot-draft9p0, one tab per tutorial, the joint as a tab and not a
document (req.model.one_document). This is the Build it before you write it gate, and the cheapest
place to find out what the #fit 0.8 / #grip 3.60 arithmetic only predicts. CAD it myself through the
GUI; REST stays read-only for verification.

## #50 B2 — read the model back and check it against make_plans.py

**completed**.

Bounding boxes, the collar's outside diameter, the mouth, the thinnest wall anywhere in each part,
and the z-extent of every cut face. The last two because session-state.md records a slit that came
out half depth with every check passing. Expect 2.20 of real material from cavity to outside, not
the nominal #wall of 3.0.

## #51 B3 — drive the variable table

**completed**.

Set #torsoH to 120 and back to 96, and confirm the whole figure follows. This is
req.model.design_intent, and it is the check the 2026-08-20 audit found seven of eight Part Studios
could not pass because they had no variables at all.

## #52 D1 — write instructions/stickbot-draft9p0/ from the logs

**completed**.

Not from the frames alone, and not from robot-guide4's prose without checking it against this
draft's log — the words are inherited, the numbers in them are not. Carry the conventions ball-and-
socket.rst had and the two pages after it lost: toolbar close-ups, view keys, video links
(req.carry.conventions).

## #53 D2 — give the guide the three pages it has never had

**completed**.

req.guide.plan — the whole robot and how it gets built, at the front, with the r4 sheet.
req.guide.before_you_start. req.guide.habits — the working habits written as things to do, which is
where the view keys stop being a per-page accident. req.guide.size_once — around 320 mm tall, on the
plan page and nowhere else.

## #54 D3 — register draft9p0

**completed**.

What was learned, which requirements went unmet and why, and state and version on every step.
Rewrite the Built sections in .docs/build/plan/*.md against the model this draft actually built.

## #55 A7 — take the slit out of make_plans.py and the hinge sheet

**completed**.

Settled 2026-08-23: the hinge blade carries no slit, on the evidence that stickbot-for-bot-review's
joints printed with solid blades and work well. make_plans.py still computes SLIT_W, SLIT_DEEP and
TAB and still draws the slit on the hinge sheet, so the sheets disagree with the model draft9p0 is
building.

Careful: SLIT_W also sizes the ball socket collar's four relief slits (make_plans.py:48, 362-367,
586) — a different part, and those stay. Only the hinge blade's slit goes.

Touches: make_plans.py lines 53, 60, 111, 637, 653, 672, 680, 739-740; then regenerate the plan
sheets (this reopens A1's r4 freeze); then the brief's "Sizing the snap" arithmetic, which is
flagged in hinge.md as computed for a blade that is no longer built.

## #56 Reconcile the hinge's snap direction between the brief's table and the built model

**completed**.

draft9p0 built the stub on the blade with a hole straight through the fork, following 09-hinge.md's
step tables. make_plans.py still draws the opposite — stub on each ear, pocket in the blade — and
the hinge brief's numbers table says the opposite of its own prose. A7 fixed the slit but
deliberately left this alone, because the task named the slit. Pick one and carry it into
make_plans.py, the plan sheets, the brief and 09-hinge.md together.

## #57 Fix the fourteen British spellings that predate draft9p0

**completed**.

`ninja check` fails on fourteen en-GB spellings in files this run did not
write: pre-plan.md (grey, labelled, centre, catalogue), <!-- codespell:ignore -->
instructions/robot-guide4/source/head.rst (grey ×2, labelled), <!-- codespell:ignore -->
instructions/robot-guide4/source/torso.rst (centre), .docs/onshape-gui- <!-- codespell:ignore -->
howto.md (centre ×2), .docs/build/plan/01-torso.md (cancelled), <!-- codespell:ignore -->
.docs/build/plan/02-head.md (centre, neighbour), <!-- codespell:ignore -->
.docs/experiments/sketches/slit-reach.py (millimetre). They date from <!-- codespell:ignore -->
2026-08-21 and 2026-08-23. The whole draft9p0 guide has been converted to
US spellings already; this is the remainder, and it is what keeps the
Spelling gate red.

## #58 Capture frames for the guide's first five pages

**completed**.

instructions/stickbot-draft9p0/source/{torso,head,assembly,ball-and-socket,head-socket}.rst carry
their steps, traps and measured numbers with no figures at all — tutorials 1 to 5 were built before
any capture ran in this build, so req.page.hero is unmet on all five. The pages name what each frame
would show, so the shot list is already written. The index's front page says which pages are in this
state; remove that paragraph when they are shot.

## #59 Retake the five frames that could not be used

**completed**.

Five captured frames were left out of the guide. hinge/blade.pattern_axis.closeup draws its red ring
beside the part instead of on it. u-limb/move_fork.closeup is zoomed so far in that it is a gray
wall with a triad on it. l-limb/move_stud.source.closeup does not say which of its two triads the
ring marks. torso-joints/connectors.r_shoulder.closeup and connectors.r_hip.closeup read identically
to the left-hand pair and are redundant rather than wrong. The first three are the same mistake: a
close-up framed without checking what was in the frame. Related to #27.

## #60 Re-run tutorials 1 to 5 for step frames

**pending**.

All five pages now have a hero but no frame of any single step. A hero can be recovered from a
rolled-back tree; a step cannot. Closing this means re-running the five tutorials with the capture
harness, which is five pages of clicking rather than a repair. Recorded in b1/unmet.md and the
register.

## #61 Reshoot the eight figures the audit could not fix in prose

**completed**.

Done. Five retaken (torso-joints/connectors.medium, foot/connector, u-limb/elbow_end.closeup,
l-limb/tree, plus arms/hero fixed in prose because it cannot be retaken). Three stay wrong and are
documented in b1/unmet.md: arms/hero (no legless arms-down pose exists on record), legs/hero.front
and legs/knee.straight (stray "Go to documents" tooltip; the pose has been dragged out of),
legs/pair.floating.closeup (mid-build state never published).

## #62 9p1 A1 — #limbSeg becomes #limbCenter, rod lengths derived

**completed**, blocks #73.

make_plans.py, plan/10-u-limb.md, plan/11-l-limb.md, robot-build-plan.md variable row. Decision
recorded in runs/2026-08-25-draft9p1/a1-limb-center.md.

## #63 9p1 A2 — #fit to 0.08, socket height invariant, ball the free variable

**completed**, blocks #73, #74.

Owed its own worked drawing file in the draft directory. Blocks B2. make_plans.py, build-
briefs/ball-and-socket.md, plan/04-ball-and-socket.md.

## #64 9p1 A3 — the eye becomes an ellipse off the example stickbot

**completed**, blocks #73.

Settle which document is the example, take the ellipse over REST read-only, scale and position 2x
clear of the head's rounding. make_plans.py, plan/02-head.md.

## #65 9p1 A4 — hinge protrusions to the blade, recesses to the fork

**completed**, blocks #73.

Re-derive the snap direction against the new arrangement. make_plans.py, build-briefs/hinge.md,
plan/09-hinge.md.

## #66 9p1 A5 — foot groove pattern phased off zero, solid at both ends

**completed**, blocks #73.

Remove #foot_l - #heel_y. Repeat distance an even divisor of the foot length. make_plans.py, build-
briefs/foot.md, plan/08-foot.md.

## #67 9p1 A6 — #wall gets one meaning across three tabs

**completed**, blocks #73, #74.

Declared in three tabs with two meanings that agree only at the current size. make_plans.py and the
tabs' variable rows in plan/.

## #68 9p1 A7 — hips stop being placed by #torsoH, shoulders by #torsoW

**completed**, blocks #73.

Or the sheet says why they are. make_plans.py, plan/01-torso.md, plan/06-torso-joints.md.

## #69 9p1 A8 — head numbers become variables, depth reconciled, pupils decided

**completed**, blocks #73.

Head's own tab gets the variables; depth reconciles against HEAD_D; pupils built or dropped.
make_plans.py, plan/02-head.md.

## #70 9p1 A9 — #boss_d stops being typed, upper rounds gets an agreed radius

**completed**, blocks #73, #74.

make_plans.py, plan/01-torso.md, plan/06-torso-joints.md.

## #71 9p1 A10 — gripper disagreements settled, body follows the socket profile

**completed**, blocks #73.

Three source disagreements settled; the mouth's facing stated once against the robot's own facing.
Supersedes task #28. make_plans.py, build-briefs/gripper.md, plan/12-gripper.md.

## #72 9p1 A11 — Width mates, rest pose, symmetric foot stations

**completed**.

Elbows and knees gain a Width mate in the specification. build-briefs/assembly.md, plan/13-*.md,
plan/14-*.md.

## #73 9p1 A12 — regenerate the plan sheets and freeze them as r6

**completed**, blocked by #62, #63, #64, #65, #66, #67, #68, #69, #70, #71, #74.

Republish every explanatory sketch carrying a number that moved. make_plans.py outputs. Runs last in
Phase A.

## #74 9p1 A13 — republish the Variables table at the built size

**completed**, blocked by #63, #67, #70, blocks #73.

All fourteen rows of robot-build-plan.md are the pre-doubling document: #torsoH 48, #ball 6, #wall
1.5, #fit 0.2. Found during A1. Runs after A2, A6 and A9, before A12.

## #75 9p1 A2 fallout — swing and height stale in five documents

**completed**.

A2 changed #fit to 0.08, so #grip 3.6 -> 1.9465, cavity 6.8 -> 6.08, ball swing ±31.86 -> ±41.76 and
standing height 315.4 -> 317.05. head.md, torso.md, ball-and-socket.md, sketches/README.md and
design-into-cad.md still carry the old numbers. assembly.md was corrected in A11.

## #76 9p1 B0 — copy t14 legs into stickbot-draft9p1 and record its ids

**completed**.

9p1 B0 — copy t14 legs into stickbot-draft9p1 and record its ids

## #77 9p1 B1 — robot sizes: rename #limbSeg, add the promoted rows

**completed**.

In stickbot-draft9p1's Variable Studio: rename #limbSeg to #limbCenter, and add #ball, #limbD,
#wall, #stand, #collar, #fit, #grip per A13. Check every dimension that reads a renamed variable.

## #78 9p1 B2 — ball and socket: the A2 rearrangement and a black slit sketch

**completed**.

Rebuild the cavity so the mouth is 96% of the ball and #grip derives from #fit. Constrain the slit
profile's pattern center coincident with the origin so the sketch is fully defined.

## #79 9p1 B3 — hinge: protrusions to the blade, recesses to the fork

**completed**.

Move every click bump onto the blade and every valley into the fork, per build-briefs/hinge.md as A4
rewrote it. Re-derive the snap direction.

## #80 9p1 B4 — body: hip and shoulder placement, #boss_d, upper rounds

**completed**.

#hip_half becomes #torsoW/2 - #limbD/2; #boss_d, #stand, #shoulder_drop, #shoulder_len become
expressions per A9. #limbD declared in body.

## #81 9p1 B5 — head: its own variables, the eye ellipse, the depth, no pupils

**completed**.

Add the eleven head variables from A8, replace the eye circle with the example's ellipse per A3, set
#headD = #torsoD*5/4, set upper rounds to #headW/6, build no pupils.

## #82 9p1 B6 — foot: the groove pattern phased off #rib_w/2

**completed**.

Replace the #foot_l - #heel_y offset with #rib_w/2 so eight grooves sit on a 96 sole with 3 mm of
land at each end.

## #83 9p1 B7 — u limb and l limb: joints buried at their stations

**completed**.

Place each derived joint by mate connector at its station and combine, rather than stacking it on an
end face. Rod lengths derive from #limbCenter: 53, 49.95, 38, 38.

## #84 9p1 B8 — gripper: the body follows the socket's outside profile

**completed**.

Top face becomes a disc of the collar's diameter coaxial with the socket, necking in fore-and-aft to
the clip's Ø10. #clipW = 2 × #collarR. Mouth opens -Y at asin(#mouth/#bore).

## #85 9p1 B9 — stickbot assembly: width mates, version instances, rest pose

**completed**.

Add a Width mate at the first elbow so all four hinges get one, re-insert instances from a named
version, set every mate to zero for the rest pose, and leave the feet symmetric.

## #86 9p1 Phase C — read the model back and prove it

**completed**.

Compare every number in the design source against the model over REST, drive the variable table,
drive #fit to its extreme, open and turn the model, publish a named version.

## #87 9p1 Phase D — write draft9p1's register

**completed**.

Record what A decided and on what evidence, what B edited, what C measured, and every 9p0 defect now
closed, by name.

## #88 9p1p1 A3 — cut the clip's top flat and square, redraw make_plans.py

**completed**.

B8 rounded the gripper's body top to the collar's own Ø18 circle, necking to Ø10 over 4 mm
(`#collarR - #clipR`). `instructions/robot-guide/make_plans.py` still draws it as a slab: `clip()`
draws `rect(cx - CLIP_R, cy, 2 * CLIP_R, c - cy)` and `clip_front()` draws a plain 18 x 24
rectangle, while `clip_front()`'s own docstring already claims the top is "flush with the socket
standing on it all the way round". So the r6 sheets and the model disagree about the gripper. This
is design-source work, not a Phase B row, which is why B8 recorded it rather than fixing it.

## #89 Settle the foot: not handed, feet may touch

**completed**.

a11-assembly.md and make_plans.py both put the feet at x ±32 with inner edges at ±8 and a 16 mm gap,
and a11 says "the offset is in the part". The built foot is symmetric: bounding box x -24 to +24
about a socket sphere at x 0. B9 measured this and centered the ankle connector, so the feet are now
symmetric at x ±24 and meet on the center plane. Giving the part the 8 makes the foot handed, which
is a second part, a second print and a second BOM line — a design-source decision, not a B row.
Onshape's Assembly mirror is at (874, 58) if the answer is a mirrored instance instead. Record the
outcome in draft9p1's register.

## #90 Withdraw the requirement for a width mate

**completed**.

A11 asks for a Width mate at the first elbow, riding the copies to four, on the premise that "all
four hinges in draft9p0 are a bare Revolute, so every lower limb can slide sideways in its fork". B9
measured the assembly: the elbow and knee revolutes are built on coincident mate connectors, and the
assembly's 31 remaining degrees of freedom are exactly 9 x 3 rotations at the balls plus 4 x 1 at
the revolutes. No translation is left for a Width mate to remove, so B9 withdrew it. assembly.md's
"A Width mate is not optional decoration on a hinge" and A11's paragraph both need amending, or the
elbow mate needs rebuilding on faces so that a Width mate has work to do.

## #91 9p1p1 B0 — copy Recovery point into stickbot-draft9p1p1 and record its ids

**completed**.

Copy stickbot-draft9p1 at version "Recovery point" 8504f457723606c65c2ab48f into a new document
stickbot-draft9p1p1. Write down every tab's element id before any edit, the way
2026-08-25-draft9p1/register.md does. stickbot, stickbot-for-bot-review, stickbot-draft9p0 and
stickbot-draft9p1 stay read-only.

## #92 9p1p1 B1 — robot sizes: #collar becomes #ball / 2 + #wall

**completed**.

In the robot sizes Variable Studio, #collar becomes #ball / 2 + #wall = 9.0 and stops being a typed
number. Check every dimension that reads it.

## #93 9p1p1 B2 — ball and socket: collar blank's second depth and the slit's end

**completed**.

collar blank's second direction depth becomes #collar (was #collar - #grip). The relief slits' end
becomes #grip + #ball / 4 = 4.9465 so the floor sits at z -3.0 and the cut is a slot for its whole
depth. The slit pattern stays circular, 4 over 360. Every sketch ends fully defined.

## #94 9p1p1 B3 — the socket's consumers lose their #grip term

**completed**.

head, foot, u limb and l limb: the expressions that carried a #grip term because the root moved.
foot's #collar_down becomes #collar; u limb's limb end becomes #limbCenter - #collar - #limbD / 2.
Measure each part's overall height before and after, because A2's claim is that these stop moving.

## #95 9p1p1 B4 — gripper: the clip's top cut flat and square

**completed**.

The slab in clip profile dimensioned #collarR both ways so the platform is a flat 18 x 18 square,
necked by a 45 degree chamfer of leg #collarR - #clipR landing on the mouth's upper lip, run 4.7000.
Plus whatever B3 changes everywhere else.

## #96 9p1p1 B5 — stickbot assembly: update references, confirm the rest pose

**completed**.

Update all references to latest versions against the new part versions, confirm the rest pose, and
re-read the stations. The instances stay version-linked.

## #97 9p1p1 Phase C — read it back and prove the height holds under #fit

**completed**.

Drive #fit and show the standing height, every joint station and every part's overall size hold
while only the mouth moves — the measurement that decides whether A2 worked. Show no face at r 5.0
bounds the slit cut. Measure the gripper's flat 18 x 18 top and the mouth still 2.6 open. Feet at
±24 with inner edges at 0. Put the variable table back. Open and turn the model. Publish a named
version, Recovery point.

## #98 9p1p1 Phase D — write the register and amend 9p2's plan

**completed**.

register.md records what Phase A decided and on what evidence, what B edited, what C measured, and
every item 9p1's register left open, closed or carried by name. Amend 9p2's plan where it names
9p1's version as the model it takes.

## #99 9p2 Phase P — amend drafts.md, takes.md and the tutorial files

**completed**.

Add the model-repair draft and the req.audit family to .docs/build/drafts.md; add the audit log
record to .docs/build/takes.md; amend the tutorial files under .docs/build/plan/ where 9p1 or 9p1p1
moved a number, a feature name or a step boundary; teach .parts/onshape.md's "Insert from the
workspace" rule in every tutorial that inserts an instance.

## #100 9p2 Phase P — inherit the guide and carry back what 9p0 dropped

**completed**.

Copy instructions/stickbot-draft9p0/ to instructions/stickbot-draft9p2/ and delete every frame under
it. Carry back from robot-guide4 what 9p0 dropped: the toolbar close-ups, the video links, the
image:: step shots, and the section teaching how to pin a pattern's center.

## #101 9p2 Phase P — create stickbot-draft9p2 empty and record its element ids

**completed**.

Create the empty stickbot-draft9p2 document, and record the element id of the Variable Studio, of
every Part Studio and of the assembly. Needs Mike's agreement to add documents to the account.

## #102 9p2 Phase T and W — the fourteen tutorials, take then page

**completed**.

Superseded by draft9p3. Tutorials 1-6 were built, captured, written and audited; tutorial 7 was not
started. The run ends on the structural finding that its CAD reaches 9p1p1's shape by a different
construction.

## #103 9p2 Phase R — write the register

**completed**.

Done: register.md written, recording what was built, what the audits attacked and found, which gates
closed, and the construction finding that ends the run. Committed in 3438ded.

## #104 9p3 P0 — read 9p1p1's construction and write it down per tab

**completed**.

Dependency level done for all nine tabs plus variables. Constraint level still owed on all nine;
needs /api/partstudios/.../features, refused until ~12:30 Sat 29 Aug. Tracked as its own task.

## #105 9p3 Phase P — write the draft9p3 plan

**completed**.

New run directory .docs/experiments/runs/2026-08-29-draft9p3. Carry 9p2's plan forward and fix what
let the machine-way construction through: same-structure requirement with a real check, sketches
anchored to existing geometry, the assembly pose step, and the rule that a take may not start until
the reference construction is written down.

## #106 9p3 Phase P — amend drafts.md with the structure requirements

**completed**.

Done: req.model.same_structure, req.model.anchored and req.model.posed added to the req.model table
in drafts.md, with the paragraph saying why draft9p2's measurements could never have caught it.
check-wrap and check-spell clean.

## #107 9p3 Phase P — create stickbot-draft9p3 and stickbot-draft9p3-check

**completed**.

Create both documents empty, record every element id, and add them to the scope list in the plan.
The check document is the one audit.page reproduces into.

## #108 9p3 Phase P — inherit the guide as instructions/stickbot-draft9p3

**completed**.

Done: instructions/stickbot-draft9p3 is draft9p2's guide with every model frame removed. 43 files,
22 toolbar close-ups kept because a button close-up is a picture of Onshape rather than of this
draft's robot; the plan records that decision.

## #109 9p3 — build the structural check script

**completed**.

A script with no memory of the build that diffs construction between two documents: per sketch, its
constraints and what each dimension references; per feature, its type and parameters. Plus the
mechanical anchoring test — how many entities a sketch locates from an axis rather than from used
geometry.

## #110 9p2 — close the run as superseded

**completed**.

Write draft9p2's register recording what it built, what the audits found, and the structural finding
that ends it: the CAD reaches 9p1p1's shape by a different construction, so its pages teach a path
the reference model does not use.

## #111 9p3 P0b — correct the reference record against /features once it answers

**completed**.

/features answers again as of 29 Aug. The body tab is read and saved as
reference/body.features.json, and it has already settled the mate connector's parameters (ownerPart
empty, attachmentOption NONE). Still to do: the other seven 9p1p1 tabs, folding the parameter level
into reference/, and resolving assembly.json's mate-connector featureIds. Only one browser-driving
script may run at a time, so this fits between tutorial-6 runs.

## #112 9p3 Phase T tutorial 1 — variables and the torso

**completed**.

Take tutorial 1 in stickbot-draft9p3, following reference/body.json's construction: units, Variable
Studio, the five sizes, the tab renamed body, torso outline picked onto Front, torso block extruded
symmetric, the Variable Studio renamed robot sizes. Then publish the named version and run
audit.step and audit.part.

## #113 9p3 Phase T tutorial 2 — the head

**completed**.

Take tutorial 2 in stickbot-draft9p3's head tab, following reference/head.json's construction and
.docs/build/plan/02-head.md. Then audit.step and audit.part, and publish the named version.

## #114 9p3 Phase T tutorial 3 — the assembly with two parts

**completed**.

Build tutorial 3 in stickbot-draft9p3 to .docs/build/plan/03-assembly.md: the assembly holding the
torso and the head, the head raised so it floats above the torso rather than sitting in the middle
of it. Take frames step by step, then write audit.step and audit.part (or audit.block for the
assembly) reading the model and the frames rather than the log, and close with a named version.

## #115 9p3 Phase T tutorial 4 — the ball and socket

**completed**.

Build tutorial 4 in stickbot-draft9p3 to .docs/build/plan/04-ball-and-socket.md, picking existing
geometry rather than re-dimensioning from the origin wherever the reference allows. Take frames step
by step, close with a named version, then write audit.step and audit.part that read the model and
the frames.

## #116 9p3 Phase T tutorial 5 — the head gains its socket

**completed**.

Build tutorial 5 in stickbot-draft9p3: derive the socket into the head tab and join it, following
9p1p1's construction (socket mount point, get socket, drop socket to neck, add socket to head, head
mate). Take step frames, run audit.step and audit.part with a drive test, cut the version, and
commit the log and frames on audited-draft9p2-plan.

## #117 9p3 Phase T tutorial 6 — the torso gains shoulders and studs

**completed**.

Build tutorial 6 in stickbot-draft9p3's body tab, following .docs/build/plan/06-*.md and
reference/body.json: step by step with frames, then audit.step and audit.part with a drive test,
then the version. Commit the log and the frames on audited-draft9p2-plan; do not push.

## #118 9p3 tutorial 4 fix — socket connect to robot infers CENTROID, not CENTER

**completed**.

Folded into .docs/build/plan/04-ball-and-socket.md as a step: both connectors are inferred CENTROID,
and the step reads entityInferenceType back off the feature.

The task as written is backwards against the settled joint. stickbot-draft9p1p6 has socket connect
to robot on CENTROID and stud connect to robot on CENTER, and CENTROID is the majority across the
settled joints — the hinge's fork and blade, u limb's mate for fork, l limb's mate for ball stud. So
the stud is the one out of step, not the socket.

Neither face can tell the two apart: the stalk's top face is a Ø6 mm disc of 28.2743 mm² and the
socket's root face is a Ø15.6 mm disc of 191.1345 mm², and a disc's center and centroid are the same
point. read_shape.py cannot see the difference.

The build happens in task #198.

## #119 9p3 tutorial 4 fix — the four tab variables 9p1p1 has and draft9p3 does not

**completed**.

9p1p1's ball and socket tab defines #stalk = #ball / 2, #stud_len = 10 mm, #slit_in = 5 mm and
#slit_out = 12 mm. draft9p3 made only #slit and spelled the other four out in the sketches: #ball /
4 for #stalk / 2, #stand for #stud_len, #ball * 5 / 12 for #slit_in, #ball for #slit_out, and
#collar * 2 for #ball + 2 * #wall.

Two of those hold at every size. Three do not: the reference's are constants and the substitutes all
scale with the ball, so the joint matches 9p1p1 at 96 mm and diverges everywhere else (at 120 mm the
stud is 12.5 mm long where 9p1p1's stays 10 mm).

Blocked on Mike: the reference's typed 10 mm, 5 mm and 12 mm are magic numbers, so draft9p3's
expressions may be the better model. The decision is whether to match the reference or record the
improvement as an agreed departure. Recorded in the run's notes under "Tutorial 4 built a ball and
socket that is 9p1p1's only at 96 mm".

## #120 9p3 Phase T tutorial 7 — the head is mated to the torso

**completed**.

Two steps per .docs/build/plan/07-assembly-head.md: cad.assembly.fix_body (fix the torso) and
cad.assembly.mate_head (ball mate, head mate to neck connector, named "head to neck").

The reference settles the pick order: 9p1p1's head to neck holds head mate first, then neck
connector, so the part that moves is picked first. The brief also wants a frame of a wrong pick and
a drag sequence, neither of which the record can supply.

Then audit.step, audit.part, and the sketch diff. Commit on audited-draft9p2-plan; do not push.

## #121 9p3 Phase T tutorial 8 — the foot

**completed**.

Build the foot tab in stickbot-draft9p3 following .docs/build/plan/08-foot.md and the reference
construction in reference/foot.json, step by step with audit.step, then audit.part with
tools/diff_features.py against reference/foot.features.json. Publish the named version at the end.

## #122 9p3 — run the construction half of audit.part once /features answers

**completed**.

/features on the draft9p3 foot tab is rate limited to zero until about 12:39 on Sunday 30 August
2026. tools/diff_features.py, tools/diff_sketches.py and tools/diff_construction.py all read it, so
the construction half of audit.part could not run for tutorial 8. The shape half did run, off
bodydetails, and is recorded in
.docs/experiments/runs/2026-08-29-draft9p3/reference/foot.faces.json.

When the endpoint answers again: run the three diff tools on the foot tab against
reference/foot.features.json, and also re-check the tutorial 8 steps whose parameters were never
read back — `sole groove`, `sole ribs`, `add socket`, `combine parts` and `mate to robot`, the last
of which needs entityInferenceType to read PART_ORIGIN and attachmentOption TO_SELECTION.

## #123 9p3 Phase T tutorial 9 — the hinge

**completed**.

Build the hinge tab in stickbot-draft9p3 following 9p1p1's recorded construction, step by step with
audit.step, then audit.part over the tab. Brief: .docs/build/plan/09-hinge.md. Reference record:
.docs/experiments/runs/2026-08-29-draft9p3/reference/hinge.features.json.

/features is rate limited until about 12:39 on Sunday 30 August 2026, so verification is off
bodydetails, parts, boundingboxes and the GUI. A shape check must name something only the right
answer has.

## #124 9p3 tutorial 8 fix — the pedestal is 0.98 mm off the origin

**completed**.

draft9p3's foot has its pedestal circle centered 0.98 mm along +y, where 9p1p1's pedestal outline is
a circle of r 9 mm at [0, 0, 0] with a construction center point. The socket lands on the origin, so
it sits off-center on the pedestal, which Mike saw on screen.

The face record already held the number: the 3.00 mm tall r=9 cylinder reads origin [0, 0.98, -12.0]
where 9p1p1's is [0, 0.0, -12.0], and the two odd 17.6 mm2 planes at z = -9 are the crescents left
over, 2 * 9 * 0.98 = 17.6.

Redraw pedestal outline with the center coincident with the origin, rebuild the foot from there, and
re-audit. Then sweep every built tab for the same disease: a sketch point placed by clicking rather
than snapped, which no constraint pulls back.

## #125 9p3 tutorial 6 fix — the shoulder profile has no projected edge

**completed**.

Folded into .docs/build/plan/06-torso-joints.md as a step: torso shoulder profile stands its
rectangle on a projected edge, with a midpoint and an angle of 90° - #tilt, the way stickbot-
draft9p1p1 does.

Decided rather than carried, because .parts/onshape.md § Anchor each sketch to the geometry that
gives it meaning asks for it: a rectangle standing on an edge follows the torso, one placed by
arithmetic has to be recomputed. draft9p4's plan already lists torso shoulder profile among what
tutorial 6 retakes.

The build happens in task #200.

## #126 9p3 tutorial 8 — drive the pedestal sketch step again for true frames

**completed**.

The model is right and the pictures are not. The five frames of cad.parts.foot.pedestal_sketch show
the circle placed 0.98 mm off the origin and the sketch under-defined, and one caption calls it
fully defined.

Driving the step again means putting a new sketch where the old one sits in the tree, which is a
rollback insert rather than an append, or rebuilding the whole tab from t8a. Settle which before
Phase W writes the foot's page, because the page is written from the frames.

Every step that computes a pixel from the camera needs the same guard the fix used: check that the
pick landed on the thing it aimed at, through the sketches route.

## #127 9p3 Phase W tutorial 1 — write the torso page

**completed**.

Done: torso.rst rewritten from log/torso.jsonl and this run's 32 frames; page_sweeps clean (no
duplicate figures, no missing files, every keystroke written, every picture has an instruction above
it); zero build warnings; six duplicate-frame findings recorded in notes. audit.page reproduction
into stickbot-draft9p3-check is tracked separately.

## #128 9p3 Phase W tutorial 2 — write the head page

**completed**.

Done: head.rst rewritten from log/head.jsonl and this run's 62 frames; both carried caption findings
honored (tab order, Value reads 0 mm); the no-sketch-axis mouth deviation explained in an advice
block; page_sweeps clean; zero build warnings; two more duplicate-frame findings recorded.

## #129 9p3 — reproduce the written pages into stickbot-draft9p3-check

**pending**.

PAUSED 2026-09-04 at Mike's request, mid-page. Where it got to and what it found are in
.docs/experiments/runs/2026-08-29-draft9p3/notes.md, section "audit.page drove tutorial 1 as far as
the version, and one of its sentences does not work" (commit 1b7d0024).

State: stickbot-draft9p3-check holds tutorial 1 built through cad.variables.rename. Tabs read body,
robot sizes, Assembly 1; tree reads torso outline, torso block, Parts (1) torso; all five variables
at their page values. No version published.

Resume with: publish "tutorial 1 - variables and torso"; read the bounding box against the page's
check table (72 x 48 x 96 mm at x +/-36, y +/-24, z +/-48); frame the box while torsoW is 50 to
check the page's "still centered, still fully defined" claim; then tutorials 2 to 9. Nine pages, 143
.. step: blocks, about 8 driven.

Found so far: task #169.

## #130 9p3 Phase W tutorial 3 — write the assembly page

**completed**.

Done: assembly.rst rewritten from log/assembly.jsonl and this run's 21 frames. The new
cad.assembly.pose step is written up with its three frames, and the inherited "there is nothing to
drag apart" advice is replaced by advice that dragging is not mating. page_sweeps clean, no reading-
level flags, zero build warnings.

## #131 9p3 Phase W tutorial 4 — write the ball and socket page

**completed**.

Rewrite instructions/stickbot-draft9p3/source/ball-and-socket.rst from log/ball-and-socket.jsonl and
the 81 frames under source/images/ball-and-socket/. Carry the two open tutorial 4 findings (#118
CENTROID vs CENTER, #119 the four missing tab variables) into the prose or say they are open. Run
page_sweeps and ninja check; build the page to zero warnings.

## #132 9p3 Phase W tutorial 5 — write the head socket page

**completed**.

Write instructions/stickbot-draft9p3/source/head-socket.rst from log/head-socket.jsonl and the tab's
42 frames. Fifth of the eight pages the takes owe. Gates: page_sweeps blockcheck + instruction_first
+ keycheck, ninja check exit 0, and the page building with zero warnings. head-socket.rst already
reports zero build warnings without having been rewritten, which is unverified and should be checked
while writing it. Commit on audited-draft9p2-plan; do not push.

## #133 9p3 Phase W tutorial 6 — write the torso joints page

**completed**.

Write instructions/stickbot-draft9p3/source/torso-joints.rst from log/torso-joints.jsonl and the
tab's 152 frames. Sixth of the eight owed pages, and the largest: the inherited page carries 36
build warnings, the most in the guide. Task #125 (the shoulder profile has no projected edge) is
unresolved and is Mike's; write around it the way tutorial 5's page was written around head mate,
and record what the decision would change. Gates: page_sweeps blockcheck + instruction_first +
keycheck, ninja check exit 0, zero build warnings. Commit on audited-draft9p2-plan; do not push.

## #134 9p3 Phase W tutorial 7 — write the mate head page

**completed**.

Write instructions/stickbot-draft9p3/source/mate-head.rst from log/mate-head.jsonl and the tab's 19
frames. Seventh of the eight owed pages. The take measured the head coming to rest 0.8 mm off the
plane of symmetry, caused by head mate's second entity in tutorial 5; that is Mike's to settle and
the page must be written around it the way head-socket.rst was. The inherited page carries 4 build
warnings. Gates: page_sweeps blockcheck + instruction_first + keycheck, ninja check exit 0, zero
build warnings. Commit on audited-draft9p2-plan; do not push.

## #135 9p3 Phase W tutorial 8 — write the foot page

**completed**.

Write instructions/stickbot-draft9p3/source/foot.rst from log/foot.jsonl and the tab's 96 frames.
Last of the eight owed pages. The inherited page carries 15 build warnings. Task #126 is open:
tutorial 8's pedestal sketch step needs driving again for true frames, because the frames on disk
predate the pedestal fix; check which frames that affects and write around them or leave the step's
frames flagged. Gates: page_sweeps blockcheck + instruction_first + keycheck, ninja check exit 0,
zero build warnings. Commit on audited-draft9p2-plan; do not push.

## #136 9p3 tutorial 8 fix — mate to robot does not resolve its entities

**completed**.

`mate to robot` in the foot tab is red: "did not regenerate properly: Cannot resolve entities." Its
Origin entity field is empty. It was already red in the connector step's own accepted frame, so it
never worked. Fix the feature, then retake cad.parts.foot.connector's five frames plus hero-01,
hero-02 and tree-01, which all show the red row.

## #137 9p3 Phase W tutorial 9 — write the hinge page

**completed**.

Write instructions/stickbot-draft9p3/source/hinge.rst from the hinge take's log and the frames it
names, then run audit.block and audit.page. Mention the two ear valleys that open onto the ear's
edge.

## #138 9p3 hinge fix — the two parts are still Part 1 and Part 2

**completed**.

The hinge tab renames neither part, in draft9p3 or in 9p1p1. upper-limb.rst says to derive "the fork
body only" and lower-limb.rst does the same for the blade, and neither name says which is which.
Mike decides: rename the two parts in the tab, or reword the two limb pages. Recorded in the run's
notes.md.

## #139 9p3 Phase T tutorial 10 — the upper limb

**pending**.

PAUSED 2026-08-30 at Mike's request while the hinge is fixed. Get elbow end on the pin axis, retake
its frames, rewrite the page's elbow section, correct the notes, audit.step + audit.part, ninja
check, build, commit.

## #140 9p3 hinge fix — BLADE_OUT is typed where the rule beside it derives it

**completed**.

Answered, not changed. .docs/experiments/runs/2026-09-02-draft9p1p4/build-notes.md records that
make_plans.py types #blade_out on purpose and says why: two noses is the shortest the joint can
close at, and the nine millimeters past that are the free length that makes the joint pressable by
hand. A derived #blade_out would be the shortest joint that closes rather than the one that works.
It stays typed, in the Variable Studio, with the reason in the design source.

## #141 9p3 hinge fix — the two robot connectors are placed by two different rules

**completed**.

Read back with evMateConnector, in the hinge's own axes with the pin on the origin: blade to robot
connector sits at z -26.4, on the blade's own end face, z axis pointing out of the part; fork to
robot connector sits at z +12, which is NOSE, 15.4 short of the fork's end face at +27.4 and inside
its solid, z axis pointing into the part.

So the fork buries 15.4 mm of itself in the upper limb's rod while the blade butts flush onto the
lower limb's, the two limbs' rods are figured differently (27 and 21.6), the fork's slot runs 9 mm
past the fork's own end into the rod, and move fork has to press Transform's flip where the blade's
placement does not.

BLOCKED ON MIKE, because there are two coherent conventions and picking one is a design call: put
both connectors on their own end faces, or put both at NOSE from the pin. Either way both z axes
should point out of the joint.

## #142 9p3 tutorial 9 fix — the blade's robot connector is off its axis and short

**completed**.

draft9p3's hinge reads back three mate connectors. Two match the reference; the third, which by
elimination is `blade to robot connector`, sits at (0, -7.884, -20) with z (0, 0, 1) where the
reference has (0, 0, -26.4) with z (0, 0, -1). It is 6.4 mm short of the blade's end face and 7.9 mm
off the axis, and it points into the part. Tutorial 11 mates the lower limb's rod to it, so fix it
before building the lower limb. Confirm the connector's name against /features first; /features was
rate limited until about midday on Sun 30 Aug. Recorded under "The hinge's blade connector is 6.4 mm
short and 7.9 mm off its axis" in the run notes.

## #143 Write the hinge review as a Sphinx document with figures

**completed**.

Mike asked for what is wrong with the hinge written down with pictures from the CAD or the sketches,
as a Sphinx document. Build .docs/reviews/hinge/ with a figures script deriving every number from
make_plans.py, annotated shadedviews frames from the sweep, ninja targets, and the findings from the
run notes.

## #144 Hinge fix — EAR_FREE is measured from where the rod roots the ear

**completed**.

make_plans.py computes EAR_FREE = SLOT_DEEP - NOSE = 21, but each limb's rod stops NOSE short of the
pin and roots the ear at 12. Read off 9p1p1: u limb slot walls z -60..-36 with the elbow at -48; l
limb tongue faces z -12..+12 with the elbow at 0. At 12 the same cantilever gives 194.78 kgf and
157.11 MPa against PETG's 50, not 36.3 and 51.3. Change EAR_FREE to NOSE, re-run make_plans, and
carry the new PRESS_F and EAR_STRESS into .docs/experiments/build-briefs/hinge.md and assembly.md.
Written up in .docs/reviews/hinge/.

## #145 Hinge fix — detail_hinge draws the slot's root at SLOT_DEEP from the pin

**completed**.

In instructions/robot-guide/make_plans.py, detail_hinge's ear_path roots the ear at y = -SLOT_DEEP,
but SLOT_DEEP is measured from the fork's tip. The published plan sheet therefore shows a 33 mm free
ear where the Part Studio has 21 and the print has 12. Root it at SLOT_DEEP - NOSE from the pin, re-
render the two sheets, and re-freeze them. Written up in .docs/reviews/hinge/.

## #146 9p1p2 A — the settled hinge into make_plans.py

**completed**.

New hinge constants (GAP 0.20 at the seat, RELIEF 0.60, the land, 24 Ø1.2 valleys on r 9.109, the
1.6 cone with a 0.4 flat top, the axle 1.00 proud, SLIT 4.0), the spring block moved onto
tools/hinge_spring, and roots 20 / 21 restored. Then ninja plan.

## #147 9p1p2 A — redraw detail_hinge to the settled hinge

**completed**.

The slot root at SLOT_DEEP - NOSE (#145), the relieved slot and its land, the cone ring at r 9.109,
the axle 1.00 proud, the names fork and blade (#138), and the sheet notes off the new press force
and stresses.

## #148 9p1p2 B — rewrite the hinge review page

**completed**.

.docs/reviews/hinge/source/index.rst carries the settled decisions: retire the three answered "Mike
decides" admonitions, fix the stand-off table, the "no row is a joint a middle-schooler can press"
claim and the 0.6 gap.

## #149 9p1p2 C — briefs and sketches to the settled numbers

**completed**.

The build brief and the assembly brief still carry 36.3 kgf and 51.3 MPa; the explanatory sketches
still draw the 0.6 gap and the old tooth band.

## #150 9p1p2 D — write the draft9p1p2 plan

**completed**.

.docs/experiments/runs/2026-08-30-draft9p1p2/plan.md: a print-and-test document holding robot sizes,
ball and socket, hinge, u limb and l limb only. Records Mike's standing permission to build by the
API for this run.

## #151 9p1p2 E — build stickbot-draft9p1p2

**completed**.

Copy what carries over from stickbot-draft9p1p1, then bring the hinge, the u limb and the l limb to
the settled design. Five tabs and no more.

## #152 9p1p2 F — read the model back and export the print files

**completed**.

Measure the built hinge against make_plans.py, then export the u limb and the l limb as STL so Mike
can print and test them.

## #153 9p1p2 G — the slit cuts the axle, rather than the axle bridging the slit

**completed**.

The blade's axle was ADDed after the slit was cut, so a Ø STUB cylinder bridges the two leaves at
the pin. hinge_spring models the axle as a contact on a leaf that is free to bend at that station,
so a bridge contradicts the 5.18 kgf press and the whole two-leaf spring. Cut the slit last in
build_blade, repair the hinge and l limb tabs, add an acceptance row that the axle reads as two
cylindrical patches, re-export l-limb.stl, and correct the register.

## #154 Settle the ball and socket: it needs 0.240 mm of mouth opening and has 0.196 elastic

**completed**.

tools/socket_spring.py (commit a36f8cc4) finds the socket does not snap together on a spring: the
mouth must open 0.240 mm to pass the ball's equator, the finger roots reach PETG's 50 MPa at 0.196,
and the peak would be 40 kgf if it were elastic. Blocked on Mike, because every fix moves a number
the whole robot reads: MOUTH from 0.96 to 0.98 of the ball gives 23 kgf, COLLAR_WALL from 3.0 to 2.0
gives 14 kgf, and the two together give 8.3 kgf at 23 MPa. Not started; make_plans.py is untouched.

## #155 Regenerate the plan and brief sheets after the socket wall change

**completed**.

make_plans.py now has COLLAR_WALL 1.5, so COLLAR_R and COLLAR_L are 7.5, CLIP_W is 15 and HEAD_B is
65.5. `ninja plan` has not been run, so the guide's plan sheets and the brief sheets still draw the
Ø18 collar, the wider gripper body and the old neck station. Waiting on Mike, because regenerating
touches the guide he has not asked to change.

## #156 Hinge: lock in STUB_PROUD 1.30 and its four numbers

**completed**.

In make_plans.py set STUB_PROUD 1.0 -> 1.30, GAP 0.20 -> 0.15, TOOTH_FLAT 0.4 -> 0.8, VALLEY_D 1.2
-> 1.70, and let SEAT, EAR, LAND_PROUD, CONE_D, TOOTH_PROUD, CLIMB, ENGAGED and BUMP_R follow. Mike
locked this in after being shown that an exact printer leaves 0.24 mm of air and that the wall is at
1.374.

## #157 Limbs: flatten the top and bottom to the fork's highest point

**completed**.

The limbs print with the limb axis on the bed and the chord in the build direction. Trim the rod's
top and bottom to the highest material on the fork, which is the land's outer corner at sqrt(NOSE^2
- (SEAT/2)^2). Give it a name, feed it to BUMP_R, and carry the trimmed section into
tools/hinge_spring.py so the leaf's stiffness is the trimmed one.

## #158 Verify joint center to joint center is one number on both limbs

**completed**.

Check that the u limb and the l limb both measure LIMB_CENTER from one joint center to the other,
and that the rods differ only because the joints eat different amounts. Report rather than change if
it already holds.

## #159 Socket: double the insertion force by grip and collar wall

**completed**.

Take the ball and socket from 5.24 kgf to about 10.5 kgf by narrowing the mouth for a print
allowance and widening COLLAR_WALL, keeping the finger elastic. Carry COLLAR_R, COLLAR_L,
COLLAR_PROUD, SLIT_D, SLIT_IN, ROD_FORK, CLIP_W, CLIP_CHAM and BALL_SWING with it.

## #160 9p1p4 B1 — robot sizes, written fresh from the corrected table

**completed**.

Rewrite stickbot-draft9p1p4's `robot sizes` Variable Studio from the corrected Variables table in
.docs/robot-build-plan.md. No Part Studio may redeclare a name this studio holds. Delete `robot
sizes (1)`.

## #161 9p1p4 B2 — ball and socket to the settled socket

**completed**.

Eight moved rows (COLLAR_WALL 1.8, COLLAR_R 7.8, COLLAR_L 10, COLLAR_PROUD 12.2205, MOUTH 11.32,
GRIP 2.2205, SLIT_D 6.2205, SLIT_IN 3.6789), the four tab variables draft9p3 lacks (#119), and the
connect-to-robot connector inferring CENTROID where it wants CENTER (#118).

## #162 9p1p4 B3 — hinge, the settled joint edited in over draft9p3

**completed**.

Rename the twenty default `###name = #value` variable features. Two stages with a read-back between:
the mechanical joint with no teeth, then valleys and cones. Name the parts fork and blade (#138),
derive BLADE_OUT (#140), place both robot connectors by one rule (#141, #142).

## #163 9p1p4 B4 — u limb: ROD_FORK, the flats, the projected edge

**completed**.

ROD_FORK 17, the limb cut flat top and bottom to LIMB_FLAT 21.6774, and the shoulder profile's
missing projected edge (#125).

## #164 9p1p4 B5 — l limb: re-point its derives, ROD_BLADE, the flats

**completed**.

Re-point `add blade` and `add ball stud` from the draft9p1 copies to this document's own hinge and
ball and socket, then delete hinge (1), ball and socket (1) and robot sizes (1). ROD_BLADE 18 and
LIMB_FLAT 21.6774.

## #165 9p1p4 B6 and B7 — the two printable coupons

**completed**.

`ball with cylinder` and `socket with cylinder`: each joint half derived from `ball and socket`, on
a diameter #limbD cylinder, joint center 22 from the cylinder's far face, taken from #stand and
#collar being equal rather than typed. Neither resketches a joint that already exists.

## #166 9p1p4 Phase C — prove it

**completed**.

Every sketch fully defined; drive #torsoH and #limbD and rebuild all six studios; no reference
leaves the document; the geometry table from plan.md checked with draft9p1p2's check.py brought
forward and its sk_slot and relieved-slot row corrected for the removed land; then open and look at
all six.

## #167 9p1p4 — audit the construction through /features once it answers

**completed**.

req.model.same_structure is the one requirement draft9p1p4 deferred: GET
/api/partstudios/.../features answered 429 with retry-after in the hours for the whole run, so the
six tabs were read through the feature tree and the dialogs instead. When the endpoint answers, read
every feature back and compare the construction — feature order, the geometry each is built on, each
sketch's constraints, and what each dimension measures from — against the reference. Recorded in
.docs/experiments/runs/2026-09-02-draft9p1p4/register.md under Requirements.

## #168 9p1p4 l limb — cut limb section onto the blade's root face

**completed**.

Mike's call, found by the construction audit. u limb draws limb section on the collar's end face and
extrudes with no start offset, so its rod begins where the socket ends. l limb draws the same sketch
on the Top plane and offsets the extrude start by #tab_free, opposite direction, even though add
blade runs first and the blade's root face is available to pick. Both limbs measure 48 between joint
centers and pass all 108 rows of check.py, so this is construction rather than shape. Fixing it
means re-cutting l limb's limb section onto the blade's root face, dropping the start offset, and
re-proving Phase C. Recorded in .docs/experiments/runs/2026-09-02-draft9p1p4/construction.md.

## #169 9p3 page fix — the pages tell the reader to click a dialog title to rename a feature

**completed**.

Folded into .docs/build/plan/00-manifest.md § What "do tutorial N" means as a standing obligation: a
carried page carries its mistakes, so when a rule in .parts/onshape.md § Modeling standards changes,
every inherited page is swept for the sentence it replaces before the draft's first new page is
written.

The rule itself now lives in .parts/onshape.md § Modeling standards (task #189): the name box opens
from a pencil that appears right of the dialog title on hover, not from a click on the title; and a
Variable feature has no name box at all, so a page must not tell a reader to name a variable.

The sweep of instructions/stickbot-draft9p4/source/*.rst happens in task #192.

## #170 9p1p5 Phase A — the wedge joint into the design source

**completed**.

make_plans.py: the wedge block replaces TEETH/STEP/VALLEY_D/TOOTH_FLAT/CONE_D/TOOTH_PROUD/BUMP_R;
GAP, SEAT, EAR, FLAT, LIMB_FLAT, SLIT, LEAF, STUB_PROUD take new values or rules.
tools/hinge_spring.py gains the variable-EI member and the wedge ring, keeping the 454 N*mm
reproduction of the old geometry as its check. .docs/robot-build-plan.md Variables table loses five
rows and gains seven. Regenerate the plan and brief sheets.

## #171 9p1p5 Phase B — the sketches and the hinge brief

**completed**.

detail_hinge redrawn: the wedge ring in plan, the section at a detent and riding, the tapered leaf,
the axle's engagement at both positions. The hinge build brief rewritten to the settled numbers,
including that assembly is now a pinch rather than a push. The hinge review document reconciled,
since it argues from the tooth and the valley.

## #172 9p1p5 Phase C — copy draft9p1p4 to draft9p1p5

**completed**.

Copy stickbot-draft9p1p4 to stickbot-draft9p1p5 from its named version. Record the document id and
every element id. Check that no feature still references stickbot-draft9p1p4, which is the defect a
copy creates and nothing else reports.

## #173 9p1p5 Phase D — the CAD, GUI only absent a REST grant

**completed**.

robot sizes: Variable Studio rows added, changed, removed. hinge: teeth and valleys deleted, the
wedge ring patterned on both faces, the leaves tapered, the axle lengthened, the slot widened. u
limb and l limb re-read, since both derive the hinge and both carry the flat that #seat moved. The
two coupons reconsidered against a joint that is pinched rather than pressed.

## #174 9p1p5 Phase E — draft9p1p4's open constructions, folded in

**completed**.

E1: l limb's rod starts on the blade's root face rather than at a #tab_free offset (task #168); its
sketch is one D3 re-reads, so it costs nothing extra here. E2: Ball stud and Socket body take the
lower-case convention the other six parts use.

## #175 9p1p5 Phase F — prove it, then Phase R register it

**completed**.

check.py forward from draft9p1p4 with the hinge rows rewritten to the wedge; rows describing teeth
or valleys deleted rather than made to pass. Every sketch fully defined. #torsoH and #limbD driven
and put back. No reference leaves the document. Look at the model per the Model inspected gate.
Publish a named version. Then write register.md carrying where the work is, what was built, what is
open, and the acceptance numbers.

## #176 9p1p5 F2 fix — ear wedges pattern errors when #limbD is driven

**completed**.

Root cause found. In `ear wedge outline`, line `DlTCtEZyBAvU` has COINCIDENT on its `.start` with
the outer circle's center and an ANGLE of `180 deg / #wedges - #wedge_w / 2`, but no COINCIDENT on
its `.end` with the outer circle. The blade's sketch has that constraint on all three of its lines.
So the ear line's length is free; it sits at a leftover 10.0459 mm. While `#ring_out` is under that,
the line overshoots the circle and the pie slice closes; `#ring_out` reaches 10.0459 mm at `#limbD`
24.013 mm, and above that the slice never closes, `ear wedge` extrudes the whole annulus, and `ear
wedges` errors patterning twelve coincident rings. Sweep: 18, 20, 22, 24 mm clean; 25, 26, 27, 28,
30 mm broken. Two consequences beyond the fix: the sketch is under-defined, so F2's "all 17 sketches
read fully defined" is wrong and the blue-pixel triage that produced it cannot be trusted; and the
built model clears this by 0.0535 mm.

## #177 The blade loses one wedge per face at #limbD 34 mm and more above it

**pending**.

draft9p1p6 (24 wedges): the blade holds 96 cone faces from #limbD 18 mm to 33.5 mm and comes back
with 94 at 34 mm, 90 at 36 mm and 82 at 40 mm; the fork holds 96 to 33.5 mm, then 92 at 36 mm and 84
at 40 mm. No feature reports an error at any size. draft9p1p5 (12 wedges) broke at 35 mm instead.
The built size is 24 mm, so 34 mm is 1.42x the design, and this was not chased.

## #178 9p1p6 Phase A — 15 degree detents into the design source

**completed**.

make_plans.py: WEDGES 24, WEDGE_C 0.15, RING_OUT = FLAT, STUB_PROUD 3.00, BORE_D = STUB + 0.1.
hinge_spring.hold returns carrying wedges rather than carrying projections. robot-build-plan.md
Variables table to the new values. Regenerate the plan and brief sheets.

## #179 9p1p6 Phase B — the sketches and the hinge brief

**completed**.

detail_hinge redrawn to 24 wedges: ring in plan, section through a detent and through the ride, the
axle at both positions. The hinge build brief to the settled numbers including the 100 N pinch
budget. The hinge review reconciled off the 30 degree step and the low carrying count.

## #180 9p1p6 Phase C — copy draft9p1p5 to draft9p1p6

**completed**.

Copy stickbot-draft9p1p5 from its named version to stickbot-draft9p1p6. Record the document id,
workspace id and every element id. Check that no feature still references stickbot-draft9p1p5.

## #181 9p1p6 Phase D — the CAD, REST granted for this document

**completed**.

D1 robot sizes: the changed rows. D2 hinge: ring repatterned to 24 on both faces, outline redrawn to
WEDGE_W 11.5127 and RING_OUT 10.4494, axle to 3.00 proud, bore to 4.1, gap to 0.90. D3 u limb and l
limb re-read. D4 the two coupons re-read. Edit existing features; do not re-emit geometry.

## #182 9p1p6 Phase F — prove it, then Phase R register it

**completed**.

F1 check.py forward from draft9p1p5 with the hinge rows rewritten. F2 face census holds with #torsoH
and #limbD driven and put back. F3 no reference leaves the document. F4 look at it. F5 publish a
named version. Then write register.md.

## #183 9p4 P0 — read draft9p1p6's construction into reference/

**completed**, blocks #186, #187, #194.

Five tabs of stickbot-draft9p1p6 at version `F done - Phase F proved`, id 80c22eb7b8b0342ac03f8a6d:
`robot sizes`, `ball and socket`, `hinge`, `u limb`, `l limb`. One record per tab under
.docs/experiments/runs/2026-09-08-draft9p4/reference/: every feature's type, name and position, what
each is built on, and for every sketch its entities, its constraints and what each dimension
measures from. Record holds `expression`. Record where draft9p1p6 types a number. Record hinge's two
naming conventions as they are; do not tidy. Paced reads so /features is not rate limited.
draft9p3's nine records for body, head, foot, gripper and the assembly are carried, not re-read.

## #184 9p4 P — drive the Variable dialog's title box and settle what the page teaches

**completed**, blocks #189, #194.

In stickbot-draft9p3-check: add a Variable feature, photograph what the title box holds as it
arrives, find out whether that box can be typed into at all and what reaches it (draft9p3 found a
sketch dialog's name box opens from a hover pencil, not a title click), and whether typing ###name =
#value back over a typed title restores the substitution. Delete the variable afterward. Touches no
reference model. If the template cannot be restored by typing, the thirteen renamed variables in
`hinge` and `ball and socket` get repaired by delete-and-re-add, and the page teaches whatever the
box actually does. Settles the rule in plan.md § The variable naming rule.

## #185 9p4 P — rewrite 09-hinge.md to the wedge ring

**completed**, blocked by #183, blocks #194.

.docs/build/plan/09-hinge.md describes bumps, valleys, a Ø4.4 bore and a 6.4 mm ear. draft9p1p6
built twenty-four wedges on a ring with a fifteen degree step, a Ø4.0 stub in a Ø4.1 bore and a 6.10
mm ear. Its steps, its shots and its prose all need rewriting against the P0 record for `hinge`.

## #186 9p4 P — amend the seven joint plan files and 01-torso for #wall

**completed**, blocked by #183, blocks #194.

Where a joint number or a joint variable appears: 04-ball-and-socket.md, 05-head-socket.md,
06-torso-joints.md, 08-foot.md, 10-u-limb.md, 11-l-limb.md, 12-gripper.md. Plus 01-torso.md, where
#wall reads #torsoH / 32 (3 mm) and the model now says #torsoH * 3 / 160 (1.8 mm). Joint variables
changed since 9p1p1: #wall, #collar became #stand, #grip gained #ballLoss, and `ball and socket`
gained #stalk, #slit_in, #slit_d, #slit_out.

## #187 9p4 P — assign every new robot sizes row to the tutorial that first needs it

**completed**, blocked by #183, blocks #194.

`robot sizes` grew from eleven rows to twenty-three between draft9p1p1 and draft9p1p6, and no plan
file says which tutorial types which. A row typed before a tutorial needs it is a number with
nothing to explain it. Write the assignment into the plan files.

## #188 9p4 P — fold tasks #118, #119, #125 and #169 into the plan files

**completed**, blocks #194.

Make them steps rather than a list somebody has to remember. #118: `socket connect to robot` infers
CENTROID, not CENTER (04). #119: the four tab variables 9p1p1 has and draft9p3 does not (04). #125:
the shoulder profile has no projected edge (06). #169: every page that names a feature tells the
reader to click a dialog title; the box is summoned by a hover pencil, and letters typed at the
title reach the sketch as tool shortcuts. #169 is fixed on every page before the first page of this
draft is written.

## #189 9p4 P — amend .parts/onshape.md § Rename features with the variable exception

**completed**, blocked by #184, blocks #194.

Blocked on the title-box test. § Rename features says every feature gets a typed name; a variable
feature keeps Onshape's ###name = #value title so its tree row reads its name and its value. Write
the exception only once Phase P has driven the box and knows what a page can tell a reader to do.

## #190 9p4 P — prove what carries, by walking the dependency graph

**completed**, blocks #194.

DONE. Diffed stickbot-draft9p1p1's 11 rows against stickbot-draft9p1p6's 23: three moved (#wall,
#collar, #grip), twelve are new, nothing renamed or removed. Walked each moved row downstream
through draft9p1p1's per-tab dependency graphs. head (31 rows) and body (38 rows) contain no feature
that reads any of the three, so tutorials 2, 3 and the ahead-of-derive half of 6 carry. foot does
not: #collar_r and #collar_down are typed 9 mm locals feeding pedestal outline and foot pedestal.
Recorded in notes.md § Three rows moved; plan.md's carry table and 08-foot.md corrected; task #202
rescoped.

The measurement half is task #211, which cannot run until tutorial 1 has driven the settled rows
into stickbot-draft9p4.

## #191 9p4 P — create stickbot-draft9p4 and stickbot-draft9p4-check

**completed**, blocks #194.

The build document branches the last version stickbot-draft9p3 published, read at Phase P rather
than recalled. The check document starts empty. Record every element id in the plan folder. REST may
create and copy workspaces and publish versions; it may not build the model.

## #192 9p4 P — inherit the guide as instructions/stickbot-draft9p4

**completed**, blocks #194.

Copy instructions/stickbot-draft9p3/ to instructions/stickbot-draft9p4/ and clear only the frames
the retaken steps own. Tutorials 2 and 3 keep every frame they have. Keep images/toolbar/ entire: a
close-up of a button is a picture of Onshape, not of this draft's robot.

## #193 9p4 P — test the free-plan claim on before-you-start.rst

**completed**, blocks #194.

The guide carries one link, https://www.onshape.com/ on before-you-start.rst:9. What is untested is
the sentence beside it, "the free plan does everything in this guide", where the guide uses a
Variable Studio, an assembly and derived parts. Testing it needs a free plan account, not an account
without ownership rights. A Phase P check on one page, not a gate over fourteen. Report what could
not be tested rather than claiming the gate.

## #194 9p4 P — close Phase P by rereading draft9p3's notes.md and draft9p1p6's register

**completed**, blocked by #183, #184, #185, #186, #187, #188, #189, #190, #191, #192, #193, blocks
#195.

Last thing before Phase T. Report anything either document holds that the plan does not, and amend
the plan rather than carrying it in memory.

## #195 9p4 tutorial 1 — variables.sizes, then the page, then reproduce

**completed**, blocked by #194, blocks #196, #211.

Take `variables.sizes` only: #wall becomes #torsoH * 3 / 160, which is 1.8 mm, where the page types
#torsoH / 32 and reads 3 mm. The torso block does not move. Then write the page, then audit.page
into stickbot-draft9p4-check. The check document starts empty and this is the last chance at the two
frames that can only be taken once: the Workspace units dialog as it arrives, on Inch with 0.123,
and the empty document before the units are set. Not done until all five conditions in
00-manifest.md § What "do tutorial N" means are true.

## #196 9p4 tutorial 2 — rebuild the head page, then reproduce it

**completed**, blocked by #195, blocks #197.

No longer a carry. The head's twelve variables are now typed at seven steps interleaved with the
geometry instead of one block into an empty tab, so the page's variable section and its frames both
change. Take the seven variable steps and the features that follow them, then write the page from
those frames.

## #197 9p4 tutorial 3 — carry the assembly page, then reproduce it

**completed**, blocked by #196, blocks #198.

No take: both instances are the parts as tutorials 1 and 2 leave them. The page carries with its
frames, subject to the read_shape.py carry check. audit.page reproduces it into stickbot-
draft9p4-check.

## #198 9p4 tutorial 4 — the ball and socket, whole tab

**completed**, blocked by #197, blocks #199.

The settled socket from draft9p1p4: #wall #torsoH * 3 / 160, #collar became #stand, #grip took
#ballLoss off the mouth's half width, and the tab gained #stalk, #slit_in, #slit_d and #slit_out.
Carries tasks #118 (socket connect to robot infers CENTROID, not CENTER) and #119 (the four tab
variables 9p1p1 has and draft9p3 does not). Take against the P0 record with it open; every sketch
step reads back what it drew before the next step runs. Then the page, then audit.page.

## #199 9p4 tutorial 5 — the head gains its socket, from socket mount point onward

**completed**, blocked by #198, blocks #200.

Take the derive, the transform, the boolean and `head mate`. The shell, rounds, chamfer, eyes and
mouth are ahead of it and carry. `head mate` sits 0.8 mm off the sphere's center because the rim
edge comes along in secondaryOriginQuery; find out whether it can be picked without the rim, and if
not, take the deviation and say so in a sentence rather than rewriting the step. Two shots from
draft9p3's tutorial 5 were findings that never got honored. Then the page, then audit.page.

## #200 9p4 tutorial 6 — the torso joints, from copy ball stud onward

**completed**, blocked by #199, blocks #201.

The stud half moves with #stand. Also retake `torso shoulder profile`, which is task #125: the
profile has no projected edge, and the dependency graph reads it and the reference as identical
because they stand on the same five things and carry every constraint but one projected line. Only
diff_sketches.py sees it. Then the page, then audit.page.

## #201 9p4 tutorial 7 — mate the head, whole tutorial

**completed**, blocked by #200, blocks #202.

The socket's connector moved, and the tutorial is a handful of steps, so it is retaken entire rather
than in halves. An assembly pick gets the medium view and the close-up. Then the page, then
audit.page.

## #202 9p4 tutorial 8 — the foot, from pedestal outline onward

**completed**, blocked by #201, blocks #203.

Retake from `pedestal outline`, not from `add socket`. The pedestal's two numbers are typed in
stickbot-draft9p1p1: #collar_r = 9 mm and #collar_down = 9 mm, both with nothing upstream. They are
#ball / 2 + #wall and #collar copied out as constants, and at the settled rows they are 7.8 mm and
10 mm, which takes #pedestal from 3 mm to 2 mm. They become expressions in this draft.

Everything ahead of pedestal outline — foot outline, foot, top round, groove profile, sole groove,
sole ribs — carries; none of it reads a moved row.

Recorded in .docs/experiments/runs/2026-09-08-draft9p4/notes.md § Three rows moved, and in
.docs/build/plan/08-foot.md.

## #203 9p4 tutorial 9 — the hinge, whole tab

**in_progress**, blocked by #202, blocks #204.

A different joint: twenty-four wedges on a ring with a fifteen degree step where the page describes
bumps and valleys. Built against the rewritten 09-hinge.md and the P0 record. `blade profile` is
four entities and cost draft9p1p5 eight attempts, no two the same mistake, and four of five findings
left a blade that looked right; read_sketches.py and diff_geometry.py run after every sketch step.
The two parts get their names, not Part 1 and Part 2. Then the page, then audit.page.

## #204 9p4 tutorial 10 — the upper limb, whole tab

**pending**, blocked by #203, blocks #205.

Never taken in any draft. Derives both joints: `add socket` and `add fork`. Check whether the rod
reproduces volume the derived fork's arm already occupies, which has never been checked for u limb
at all. Then the page, then audit.page.

## #205 9p4 tutorial 11 — the lower limb, whole tab

**pending**, blocked by #204, blocks #206.

Never taken in any draft. Derives both joints: `add blade` and `add ball stud`. Settle whether the
rod reproduces volume the derived blade's arm already occupies, seen in draft9p1p5's Phase E and
never run to ground. Then the page, then audit.page.

## #206 9p4 tutorial 12 — the gripper, whole tab

**pending**, blocked by #205, blocks #207.

`clip profile` follows the socket's outside profile and is drawn after `copy socket`, so the whole
tab moves with the settled socket. Then the page, then audit.page.

## #207 9p4 tutorial 13 — one arm, then the other by copy

**pending**, blocked by #206, blocks #208.

Never taken in any draft. The assembly gains both arms. An assembly pick gets the medium view and
the close-up. Then the page, then audit.page.

## #208 9p4 tutorial 14 — one leg, then the other by copy

**pending**, blocked by #207, blocks #209.

Never taken in any draft. The assembly gains both legs and the robot stands. Then the page, then
audit.page. This is the last tutorial: the version it publishes is the one the Recovery point gate
wants.

## #209 9p4 Phase R — write the register

**completed** 2026-09-18. `task.draft9p4.register`.

What was built, what each audit attacked, what it found and what was done about each finding. Every
step gets its `state` and its `version`. Every gate claimed in the declaration gets the evidence
that closes it, by name, and a gate that did not close says so. Floor & ceiling is not claimed and
the register says why. Record which audit.page findings reached the next tutorial's take.

Written to .docs/experiments/runs/2026-09-08-draft9p4/register.md, from the nine logs and the tree
rather than from memory: 160 step identifiers, 1,464 frame records and 206 verdicts, and all 371
document lines naming stickbot-draft9p4-check where the plan said the build document. Steps
reproduce closed on tutorials 1, 2 and 3 only; Names are real fails on hinge.rst, which says bump,
dome or valley 95 times and wedge zero times; Model inspected did not close, and the foot is why;
Recovery point closed through tutorial 8. It also records that the 587 committed frames did not
come across in the 2026-09-14 move and are in the archive repository.

It had been placed under Phase 5 in .docs/2026-09-14-move-to-stick-e-bot.md, which builds a model
and writes no record of draft9p4.

## #210 Bring ball-and-socket.md up to the settled socket

**completed**.

The build brief .docs/experiments/build-briefs/ball-and-socket.md still describes the socket as it
was before draft9p1p4. It says wall 3.0 (make_plans.py has COLLAR_WALL = TORSO_H * 3 / 160 = 1.8),
collar length 9.0 (COLLAR_L = STAND = 10), collar Ø18.0 (2 * COLLAR_R = 15.6), grip 1.9465 (GRIP =
2.2205), collar proud 10.9465 (12.2205), mouth Ø11.520 (MOUTH = 0.96*BALL - 2*BALL_LOSS = 11.32),
swing ±41.76 deg (BALL_SWING = 39.0132), slits 4.9465 deep (SLIT_D = 6.2205) and #slit_in 5.0
(SLIT_IN = 3.6789). BALL_LOSS does not appear in the brief at all. Its build recipe section quotes z
= +1.9465 and 10.9465 upward, so following it builds the old socket. make_plans.py and stickbot-
draft9p1p6 agree with each other; the brief is the only source out of step. Found while amending the
plan files for draft9p4 task #186.

## #211 9p4 tutorial 1 check — read_shape.py on head and body against draft9p3's logs

**completed**, blocked by #195.

The measurement half of task #190, split out because it cannot run in Phase P.

Once tutorial 1 has driven robot sizes to the settled 23 rows in stickbot-draft9p4
(fe052e606c96bb7cc5aaf59f, workspace 0ff70e8921be572d630dd9cc), run read_shape.py on the head and
body tabs and compare against draft9p3's log/head.faces.json and log/body.faces.json.

The dependency walk says both carry: head's 31 rows and body's 38 contain no feature reading #wall,
#collar or #grip. This measures whether that is true of the built shape. A face that moved takes
`captured` off its step, and tutorials 2 and 3 stop being carries.

Element ids are in .docs/experiments/runs/2026-09-08-draft9p4/reference/documents.json.

## #212 9p4 spike — reach the concave ball's center with shift-hover and a turned view

**completed**.

Done 2026-09-11. The 0.8 mm came from the camera being on the socket's axis, not from the pick
point. `head mate` holds face `Jr6` (the cavity sphere, center (0, 0, -45) mm, radius 6.08 mm) plus
edge `KrVB`, a slit-wall circle centered on (0, -0.8, -45) mm; the circle wins the position. The
socket's cross slit is 1.6 mm wide, so its four traces on the sphere all sit within 0.8 mm of the
axis, and the derived socket's own `socket connect to robot` sits at (0, 0, -36) mm in front of the
cavity. Four runs: square on the axis fails with and without Shift, catching `socket connect to
robot`; turned 45 deg passes with and without Shift, giving `Jr6` alone, inference CENTER, origin
(0, 0, -45) mm. Shift does reach Onshape (it outlines the whole body, 230395 pixels of difference)
but does not thin the candidates under the pointer. The turned view passes with nothing hidden, so
tutorial 5's step loses its hide and gains a turn. Head tab left as found at 26 features. Written up
in the run's notes.md, plan.md, .docs/build/plan/05-head-socket.md and .docs/onshape-gui-howto.md §
4.

## #213 9p4 P — variables arrive at the step that needs them

**completed**.

Restructure the design source so no tutorial opens with a block of variables. A row of `robot sizes`
and a Part Studio variable alike are declared immediately before the first feature that reads them,
derived from the construction records rather than inferred. Touches 00-manifest.md (the rule and the
ledger), 01-torso, 02-head, 04-ball-and-socket, 06-torso-joints, 09-hinge, 10-u-limb, and lesson-
plan.md. Also fixes two placement defects found on the way: tutorial 1 carries `#limbCenter` and
`#wall` before anything reads them, and 10-u-limb.md still calls `#limbD` a tab variable when
tutorial 6 puts it in the studio.

## #214 9p4 — re-run the head and body carry diff once the settled rows are back

**pending**.

The copy half of #211 is proved: draft9p4 at its Start version matches draft9p3's log face for face,
47 on head and 20 on body. The settled half cannot be run yet — emptying the studio in tutorial 1
put both tabs in error, and draft9p1p6 has no head or body tab to read instead. After tutorial 6
types #limbD back, re-read both tabs from the draft9p4 workspace with read_shape.py and diff against
.docs/experiments/runs/2026-08-29-draft9p3/log/head.faces.json and body.faces.json. A face that
moved takes `captured` off its step in 02-head.md or 03-assembly-first-parts.md.

## #215 9p4 tutorial 8 fix — sole groove cuts up into the foot, not down to the sole

**pending**.

`sole groove` has two Opposite direction arrows and only the Starting offset one was turned, so the
cut starts 22 mm below the sketch and runs 2 mm back up. The result is eight tunnels across the
foot's width, 2 mm above an unbroken sole at z -24 mm, instead of eight open notches. Both stickbot-
draft9p4-check and stickbot-draft9p4 carry it.

Fix: edit `sole groove` in the check document and turn the Depth arrow; `sole ribs` follows. Repeat
in the build document. Publish `tutorial 8 - the foot` again in both. Add the check that catches it:
the sole at z -24 mm is nine faces, not one, and no face stands at z -20 mm. Amend
`.docs/build/plan/08-foot.md`'s `## Built` and `## Captured`.

Written up in `.docs/experiments/runs/2026-09-08-draft9p4/notes.md`, "The foot has no tread".

## #216 9p4 tutorial 8 fix — shift+5 is the top view, and the retakes that follow

**pending**.

foot.rst tells the reader to press shift+5 to look from underneath. That key gives the Top view.
hero-02, parts.foot.groove-09 and parts.foot.ribs-01 are top views captioned as the sole with
grooves across it, so the page never shows the sole once.

Find the key that does give the bottom view. Correct shift+5 at the hero (line 23), in the groove
and ribs steps (lines 781 and 795) and in the measure table (line 1157). Rewrite the alt text of the
three frames.

Retake, after task #215 fixes the model: the 15 frames from parts.foot.groove-06 through
parts.foot.ribs-11; hero-02; and whichever of the 28 frames from parts.foot.socket.derive-01 onward
have the foot's lower edge in them, where the slot mouths show. Check each rather than assuming.

## #217 Move to stick-e-bot — REST granted for stickbot-draft9p4 by name

**completed**.

Mike granted REST for `stickbot-draft9p4` by name on 2026-09-14, so Phase 4 of
`.docs/2026-09-14-move-to-stick-e-bot.md` may write geometry over REST in that document. The grant
covers `stickbot-draft9p4` only; per the draft9p1p6 precedent a grant does not carry to another
document.

Two conditions come with it, both from `.docs/experiments/runs/2026-09-08-draft9p1p6/plan.md`:

- REST writes geometry by editing the features the parent already holds, with their constraints,
  patterns and mirrors intact, not by emitting fresh geometry because emitting is cheaper.
- draft9p4 is the reference model now. It publishes no pages and takes no frames; it is proved by
  read_shape.py, diff_shape.py and rendered views.

Write this into the plan file's Phase 4 once Mike is out of it in the IDE.

## #218 Survey the CAD for the best reference, part by part

**completed**.

Find the CAD closest to make_plans.py and make_brief_sheets.py, working backwards from the most
recently built. Per part: document, workspace, version, tab; agreement measured and eyeballed from
enough views and cross sections; hero frames into .docs/experiments/build-briefs/images/ with
provenance in its README.md. Defined in .docs/2026-09-17-reorg-drawings-and-notes.md.

## #219 — deleted

Written and deleted on 2026-09-18. It claimed draft9p1p6's workspace was damaged, on a read that
returned 258 faces on hinge and 24 on u limb against the version's 510 and 270. The cause was a
rollback bar Mike had set at feature 31, fork outline, and then cleared; nothing was wrong with the
document. The word damaged is reserved for something that stops Onshape operating correctly, and it
does not mean inaccurate CAD. The number is left standing so the gap is not read as an export
failure.

## #220 Bring the six stale briefs up to the settled socket

**completed**.

assembly.md, foot.md, head.md, limbs.md and torso.md hold 21 occurrences of 10.9465 mm and 1.9465 mm
between them, against make_plans.py's COLLAR_PROUD 12.2205 mm and GRIP 2.2205 mm; gripper.md writes
2 x #collarR out as 18.0 mm where it is now 15.6 mm. ball-and-socket.md was brought forward by task
#210 and hinge.md never had a socket. head.md also asks for the head to be shelled, and
cad-head-section.png shows the built head solid. Found by the survey, 2026-09-18.

## #221 Steps reproduce did not close on tutorials 4, 5, 6, 8 and 9

**pending**. `task.reproduce.draft9p4`. Waits on the guide draft that follows draft9p5.

Each of those tutorials was driven into stickbot-draft9p4-check from the session that built it, so
the page was followed by someone with the build in front of them, which is not what the gate asks.
Tutorials 1, 2 and 3 logged real reproduction language; from tutorial 4 onward the logs record only
the take. All nine logs name stickbot-draft9p4-check and no other document, and the build document's
foot carries the same wrong tread down to the same face positions, which is what re-running the same
clicks looks like.

draft9p5 does not claim the gate and writes no pages, so this cannot close there.
.docs/2026-09-14-move-to-stick-e-bot.md says under task.reproduce.draft9p3 that the gate moves to
draft9p5; that sentence predates Phase 5 becoming a model build and this entry replaces it.

## #222 The head page's eye step reproduces 1.5 percent oversize

**completed** 2026-09-18, by moving into draft9p5's plan rather than by being fixed.

Each eye's end face measures 102.0857 mm2 in stickbot-draft9p4-check against 100.531 mm2 in
stickbot-draft9p4, and 100.531 mm2 is pi x EYE_RX 8 mm x EYE_RY 4 mm exactly. diff_shape reports 5
faces each way, all of them trimmed to a different size in the same place. Found by the survey,
2026-09-18.

The original description said to fix the step so the ellipse is dimensioned rather than dragged.
That is wrong: head.rst:510 already dimensions both axes as #eyeRx * 2 and #eyeRy * 2, locates the
center on #eyeX and #eyeUp, and says the ellipse goes black. There is no round on the eye and no
draft on the extrude, so the page as written gives 100.531 mm2. #headW is not the difference either,
because the head's other faces match face for face and the box is drawn from #headW.

The area does not say what moved. Two departures fit 102.0857 mm2 exactly: both radii larger by a
factor of 1.0077, or both offset outward by 0.0411 mm. The 0.06 mm first written down is the first
of the two, inferred from the area rather than measured off the sketch.

Carried to .docs/experiments/runs/2026-09-18-draft9p5/plan.md, "The head, where the eye reproduces
1.5 % oversize". Phase A reads the sketch to name the cause; Ring 2's acceptance on head is
math.pi * EYE_RX * EYE_RY.

## #223 Grant REST for stickbot-draft9p5 by name

**completed**.

The REST grant is per document and does not carry: draft9p1p6's plan records the earlier permission
covering stickbot-draft9p1p2 and stickbot-draft9p1p4 and not extending, and Mike granted REST for
stickbot-draft9p4 by name on 2026-09-14. Phase B of draft9p5's plan adds every feature over REST and
cannot start until stickbot-draft9p5 has its own grant. This is Mike's to give, not work to be done.

Granted 2026-09-18.

## #224 Re-open task.capture.tutorials_1_to_5 against the guide draft

**pending**.

It was closed as superseded on the reasoning that draft9p5 captures every page from empty. As of
2026-09-18 Phase 5 is a model build over REST that takes no frames and writes no pages, so that
reasoning no longer holds. draft9p0's first five pages still have a hero and no frame of any single
step. It belongs to the guide draft that follows draft9p5, which is not planned yet.

## #225 Rename EAR, EAR_FREE, EAR_MOVE and EAR_STRESS in make_plans

**pending**. `task.hinge.ear_rename`. No plan holds it; the scope question below is why.

The word ear was retired for fork prong on 2026-09-17. The briefs' prose, their step tables and the
four brief-*.svg sheets carry the new vocabulary; the identifiers do not. make_plans.py exports EAR,
EAR_FREE, EAR_MOVE and EAR_STRESS across 19 lines, make_brief_sheets.py reads them on 9 and
make_target.py on 3, and .docs/experiments/build-briefs/hinge.md cites EAR beside a sentence that
says fork prong.

Where the rename stops is the open question. hinge_spring.py carries the same concept in lowercase
as its public interface -- ear_free as a Hinge keyword, Hinge.ear, and press()'s internals -- and
make_plans.py:290 passes ear_free=EAR_FREE, so a rename stopping at the constants leaves the retired
word in the interface they feed. .docs/reviews/hinge/make_figures.py builds its own frozen namespace
holding EAR and EAR_FREE and hands it to hinge_spring.press; that generator is labeled superseded
and frozen at its own snapshot. And make_plans.py prints ear and tongue as drawing text at lines
1025, 1055, 1109 and 1110, so plan-parts.svg carries 1 EAR, 7 ear, 1 ears and 8 tongue. Renaming the
constants alone leaves every SVG byte-identical; renaming the drawing text does not.

The CAD variable #ear is not part of this. draft9p5 drops it, with #backlash.

## #226 Retake cad-body-section and cad-l-limb-section

**pending**. `task.briefs.section_retakes`. draft9p5's Ring 2 is where the retake happens.

cad-body-section.png and cad-l-limb-section.png carry a selection highlight from the session that
shot them, and l limb's section is cut on the Front plane where the Right plane shows the blade. The
geometry in both is sound, so a builder can read them as they are.

draft9p5's Ring 2 shoots sections off the new model and opens every frame it keeps, which is where
these are retaken rather than off the documents draft9p5 replaces. The plane for l limb wants
deciding before Ring 2 reaches that tab.

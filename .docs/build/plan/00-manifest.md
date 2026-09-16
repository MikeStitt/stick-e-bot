# The build plan — the manifest

**Order is position: this list, then position within each file.** There is no step number and no
`order` field — [`steps.md`](../steps.md) says why. Moving a file in this list moves everything in
it.

One file per tutorial, because a tutorial starts and ends when the work moves from one Part Studio
or the assembly to the next, and that is exactly where a file wants to end.

| # | File | Tab |
| - | ---- | --- |
| 1 | [`01-torso.md`](01-torso.md) | Variable Studio, then `body` |
| 2 | [`02-head.md`](02-head.md) | `head` |
| 3 | [`03-assembly-first-parts.md`](03-assembly-first-parts.md) | the assembly |
| 4 | [`04-ball-and-socket.md`](04-ball-and-socket.md) | `ball and socket` |
| 5 | [`05-head-socket.md`](05-head-socket.md) | `head` |
| 6 | [`06-torso-joints.md`](06-torso-joints.md) | `body` |
| 7 | [`07-assembly-head.md`](07-assembly-head.md) | the assembly |
| 8 | [`08-foot.md`](08-foot.md) | `foot` |
| 9 | [`09-hinge.md`](09-hinge.md) | `hinge` |
| 10 | [`10-u-limb.md`](10-u-limb.md) | `u limb` |
| 11 | [`11-l-limb.md`](11-l-limb.md) | `l limb` |
| 12 | [`12-gripper.md`](12-gripper.md) | `gripper` |
| 13 | [`13-assembly-arms.md`](13-assembly-arms.md) | the assembly |
| 14 | [`14-assembly-legs.md`](14-assembly-legs.md) | the assembly |

**Fourteen tabs is not fourteen class hours.** Numbers 5 and 7 are a handful of steps each and
will likely be read as the tail of the tutorial before them. The tab rule draws the boundaries;
it does not claim they are even. [`lesson-plan.md`](../lesson-plan.md) already says the same.

## A variable is typed at the step that first reads it

**No tutorial opens with a table of numbers.** A number that arrives with nothing to explain it is
a number a reader copies, and a page that opens with twelve of them is a page a reader endures
before the CAD starts. So a variable is typed immediately before the first feature that reads it,
and its own terms come with it, because a rule cannot be typed before the names it is made of.

**The rule is the same for both kinds of variable, and the two kinds behave differently.** A
`robot sizes` row lives in a table in the Variable Studio, and reaching it means leaving the Part
Studio; a Part Studio variable is a feature in the tree, and it goes in where any feature goes in.
The studio takes rows at any point in the build, so neither kind needs to be front-loaded.

**Where several rows are one chain, they arrive together, at the step that forces the chain.**
`#grip` cannot be typed before `#fit` and `#ballLoss`, so all three land at `collar blank`. This is
not a block of variables; it is one number and the terms it is written from.

`robot sizes` holds twenty-three rows. This is where each one enters.

| Tutorial | Rows | |
| -------- | ---- | - |
| 1 | `#torsoH`, `#torsoW`, `#torsoD` | 3 |
| 4 | `#ball`, `#stand`, `#wall`, `#fit`, `#ballLoss`, `#grip`, `#collar` | 7 |
| 6 | `#limbD` | 1 |
| 9 | `#blade`, `#wedge_h`, `#wedge_c`, `#gap`, `#seat`, `#blade_out`, `#tab_free`, `#flat`, `#t_print`, `#limbCenter`, `#slot_deep`, `#ear_free` | 12 |

**Tutorials 2, 3, 5, 7, 8 and 10 to 14 add no studio row.** Each reads rows that are already
there. The head's twelve numbers are the head's own, because one tab reads them; the same rule
keeps the hinge's sixteen in `hinge` and the socket's five in `ball and socket`.

**`#limbD` waits for tutorial 6 even though the limbs are what it is for.** `hip stud location` is
where the torso first has to know how thick a limb is, and it is read again by the foot, the
gripper, the hinge and both limbs.

**`#limbCenter` and `#wall` used to be typed in tutorial 1, and nothing read them for three
tutorials.** `#wall` is first read by `#slit_in` in tutorial 4 and `#limbCenter` by `#rod_blade` in
tutorial 9, so that is where each is typed now. Tutorial 1 keeps the three the torso is drawn from.

**Ten of tutorial 9's twelve land on the hinge's first sketch, and that is the geometry talking.**
`blade profile` is the limb's cross-section, the section is what the wedge seat leaves, and
`#flat` reads `#seat` reads `#gap` reads `#wedge_h` and `#wedge_c`. The chain cannot be broken up
without typing a rule before its terms, so the page says what the ten are for rather than pretending
they arrive one at a time.

**Which feature first reads which variable is measured, not assumed.** It comes from walking the
expressions in the construction records under
[`../../experiments/runs/2026-09-08-draft9p4/reference/`](../../experiments/runs/2026-09-08-draft9p4/reference/),
including `robot-sizes.features.json`, so a row that only ever appears inside another row's
expression still lands ahead of it.

## What "do tutorial N" means

**A tutorial is done when all five of these are true.** Anything less is reported as what it is,
with the step's `state` saying how far it got — `proposed`, `built`, `captured`, `published`.

| | Done when |
| - | --------- |
| 1 | the model is built in Onshape and every acceptance number measured off it, not recalled |
| 2 | every shot the file names is on disk under the guide, named by its step identifier |
| 3 | the page is written from those frames |
| 4 | a named Onshape version is published, and this file cites it |
| 5 | `state` on every step in the tutorial matches what actually happened |

**Done is per draft, and a step carried forward is done.** A draft inherits the previous draft's
guide entire, so a tutorial nobody retook arrives complete with the frames and the version it
already had. Which draft proved each step is its `version`, and how a draft inherits is
[`drafts.md`](../drafts.md).

**A carried page carries its mistakes, so a rule that changes sweeps every page at once.** An
inherited tutorial arrives complete and nobody rereads it. That is how nine pages came to tell a
reader to click a dialog's title to rename a feature: the box opens from a pencil that appears on
hover, and letters typed at the title reach the sketch as tool shortcuts, so Onshape answers
*A constraint must involve something from the sketch* and the feature keeps its old name. When a
rule in [`onshape`](../../../.claude/skills/onshape/SKILL.md) § *Modeling standards* changes,
every inherited page is swept for the sentence it replaces, before the draft's first new page is
written. Task #169 is the sweep this draft owes, and the variable exception in the same section is
what it sweeps for.

**Frames are taken on the first pass, not a second one.** The expensive part of a capture is
driving the browser into the state; once it is there the frame costs one line. A run that works
out the click sequence without capturing pays that cost twice and throws the first payment away —
and it never finds out whether the shot it planned can be taken at all. Two shots in
[`01-torso.md`](01-torso.md) turned out to be unreachable, and both would have surfaced at the
moment of the click rather than afterwards.

**Building the model is step 1 of 5, not the tutorial.** "CAD tutorial N" and "do tutorial N" mean
the same thing, and a run that stops after the model says so out loud.

## How to read a file

Each one carries the same three parts.

**The steps**, as a table: the identifier, the move, and `creates` — the Onshape feature the step
adds, by the name that feature is given. **`creates` carries the name the feature gets, not the
name stickbot gave it.** Nine of stickbot's features are named badly — `Boolean 1`, two features
called `r shoulder connector`, a sketch and an extrude sharing a name in two places — and the
tables below hold the corrected names, with the file saying what stickbot had. `creates` is what
the retake diffs against the feature list read back off the model, so a wrong one is caught rather
than believed.

**The shots this tutorial needs by name.** Only the frames a rule cannot produce.
[`shots.md`](../shots.md) says which frames the harness makes on its own, and those are not
repeated here.

**What we do not know yet**, as questions the run answers. A step whose frames are not knowable
ahead of the run says what it is trying to show and leaves the framing to whoever is at the CAD.

## Where the steps came from

**The feature names are read off the stickbot document**, not invented. Where this plan and
stickbot disagree — the order of the shoulders and the studs, the head's typed offset, the five
broken connectors, the derive that comes first in `foot` — the plan wins and the model is what
gets rebuilt. Each of those disagreements is written down in the file it falls in.

**Every step is `state: proposed` unless its file says otherwise.** A file that has been performed
says so at the top of its steps table and carries, in its own **Built** section, the named version
it was proven against.

## A Built section records one draft, and the older ones are the half-size robot

**On 2026-08-23 the robot doubled.** Every **Built** and **Captured** section written before that
records `stickbot` at the old size, cited to a published version, and they are correct as records
— a torso that measured 36 × 24 × 48 measured that, and saying otherwise would be rewriting
history rather than the design. A file rewritten by a later draft cites that draft's document and
version instead, and the document named in the section is what says which robot it is.
**Do not read a number out of a Built section as a target.**

The targets are in `src/stickbot/make_plans.py` and in the build briefs under
`.docs/experiments/build-briefs/`. Where a file's **steps**, **shots** or **what we do not know
yet** carried a number that a retake would build to, it has been amended; the Built sections have
not. A tutorial retaken at the new size replaces its own Built section with what it measures.

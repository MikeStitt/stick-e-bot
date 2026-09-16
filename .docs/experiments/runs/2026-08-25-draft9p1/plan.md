# draft9p1 — the CAD made right, before anything is captured

draft9p0 built the whole robot and then found, by measuring it, that the model and the design source
disagree in a dozen places. This draft settles those disagreements on paper, edits the model until
it matches, and proves the match by measurement. **It captures nothing and writes no guide page.**
Its product is a correct reference model and a design source that describes it, which is what
draft9p2 needs in front of it to build the robot again from empty and photograph every step.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p1` |
| `parent` | `draft9p0` |
| `from` | `version stickbot-draft9p0 t14 legs`, `737db64e2567c96e2d3de63f` |
| `takes` | none |
| `gates` | Model inspected, Recovery point, Links resolve, Prose style, Spelling |
| `requirements` | all of `req.model`; `req.carry.register`; `req.page`, `req.shot`, `req.guide` and `req.log` deferred to draft9p2 and not in play here |

**`takes` is empty, and that is the whole shape of this draft.** A take performs a step and
photographs it. Every step in this robot is going to be performed and photographed again in 9p2,
from empty, once the model is right. Performing them here would produce frames of an intermediate
model that no page will ever show.

**Gates not claimed.** *Steps reproduce* — this draft writes no steps to reproduce. *Names are
real* — no page names a tool here. *Floor & ceiling* and *Reading level* — no session material.

## draft9p1 has no guide directory, on purpose

[`drafts.md`](../../../build/drafts.md) § *The guide is inherited* says to copy the parent's guide
before anything is taken, so that a partial retake still produces a whole guide. **That rule does
not fit a draft that retakes nothing and moves all the geometry.** Copying
`instructions/stickbot-draft9p0/` to `instructions/stickbot-draft9p1/` would produce a complete
guide in which every picture shows a robot this draft has just stopped building — the exact failure
§ *Geometry that moves invalidates what comes after it* exists to prevent, applied to every page at
once.

So `instructions/stickbot-draft9p1/` is not created. draft9p0's guide stays where it is and stays
readable, and **draft9p2 declares `parent: draft9p0`** for its pages while taking its model from
9p1. That is a deviation from `drafts.md` and it is named here rather than discovered later; if it
turns out to be the shape every model-repair draft wants, `drafts.md` gains a fourth kind of draft
in 9p2's Plan phase, not in the middle of this one.

## The order, and why it is this order

**The design source is settled first, then the model is edited to match, then the match is
measured.** The register's defects are almost all of the form *the model and the sheets disagree*,
and a disagreement cannot be fixed at the model — editing the model to match a sheet nobody has
checked just moves the argument. Phase A decides what is true. Phase B makes the model true. Phase
C proves it, by reading the model back and comparing it with the source that now claims to describe
it.

**Nothing in Phase B starts until Phase A is committed.** Two of the A items — `#fit` and the eye —
change numbers that other numbers hang off, and a model edited against a half-settled source gets
edited twice.

## Phase A — the design source

Every row is a defect or a user requirement already recorded in
[`../2026-08-23-draft9p0/register.md`](../2026-08-23-draft9p0/register.md). The register is where
the finding lives; this table is what to do about it and where the change lands. The design source
is [`../../../../instructions/robot-guide/make_plans.py`](../../../../instructions/robot-guide/make_plans.py)
and the sheets it prints, [`../../../build/plan/`](../../../build/plan/00-manifest.md), and
[`../../build-briefs/`](../../build-briefs/).

| | What changes | Where |
| --- | --- | --- |
| **A1** | `#limbSeg` becomes `#limbCenter` and means joint center to joint center. `ARM_SEG`/`LEG_SEG` follow it. The parts-sheet label stops reading `Ø24 × 48 mm` and becomes a derived stock length. | `make_plans.py`, `plan/10-u-limb.md`, `plan/11-l-limb.md` |
| **A2** | `#fit` goes to 0.08, dimensioned at the extreme case, with the socket's height invariant to it and the ball's position the free variable. `#grip` is re-derived. | `make_plans.py`, `build-briefs/ball-and-socket.md`, `plan/04-ball-and-socket.md` |
| **A3** | The eye profile becomes an ellipse taken off the example stickbot, scaled and positioned 2×, clear of the head's rounding. | `make_plans.py`, `plan/02-head.md` |
| **A4** | Every protrusion moves to the blade and every recess to the fork, so the click bumps cannot meet the axle stub during mating. The snap direction is re-derived against the new arrangement. | `make_plans.py`, `build-briefs/hinge.md`, `plan/09-hinge.md` |
| **A5** | The foot's groove pattern is phased off zero and leaves solid material at both ends. `#foot_l - #heel_y` goes. | `make_plans.py`, `build-briefs/foot.md`, `plan/08-foot.md` |
| **A6** | `#wall` gets one meaning. It is declared in three tabs with two, and they agree only at the current size. | `make_plans.py`, the tabs' variable rows in `plan/` |
| **A7** | The hips stop being placed by `#torsoH` and the shoulders by `#torsoW`, or the sheet says why they are. | `make_plans.py`, `plan/01-torso.md`, `plan/06-torso-joints.md` |
| **A8** | The head's numbers become variables in the head's own tab, its depth reconciles against `HEAD_D`, and the pupils are decided — built or dropped. | `make_plans.py`, `plan/02-head.md` |
| **A9** | The torso's `#boss_d` stops being typed, and `upper rounds` gets a radius the sheet and the model agree on. | `make_plans.py`, `plan/01-torso.md`, `plan/06-torso-joints.md` |
| **A10** | The gripper's three source disagreements are settled, the mouth's facing is stated once against the robot's own facing, and the body follows the socket's outside profile. | `make_plans.py`, `build-briefs/gripper.md`, `plan/12-gripper.md` |
| **A11** | The elbows and knees gain a Width mate in the specification, the assembly's rest pose is defined, and the foot stations become symmetric. | `build-briefs/assembly.md`, `plan/13-*.md`, `plan/14-*.md` |
| **A13** | The Variables table is republished at the size the robot is actually built at. All fourteen rows are the pre-doubling document: `#torsoH` 48, `#ball` 6, `#wall` 1.5, `#fit` 0.2. | `robot-build-plan.md` |
| **A12** | The plan sheets are regenerated and frozen as `r6`, and every explanatory sketch carrying a number that moved is republished. | `make_plans.py` outputs |

**A2 is owed its own worked drawing and is the one item that can hold up the phase.** Making the
socket's height independent of `#fit` while the ball moves is a rearrangement of the joint, not a
number change, and the register asks for detailed drawings and a detailed plan before it is built.
It gets a file of its own in this draft's directory, and Phase B does not open the joint tab until
that file is settled.

**A13 was found during A1 and is why A12 runs last.** The Constitution calls
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) the design source, and its
Variables table never received the doubling that draft9p0 applied to `make_plans.py` and the
briefs. A1 renamed its one row and left the rest, so the table is inconsistent until A13 runs.
A13 goes after A2, A6 and A9, because those three decide what several of the numbers become.

**A3 reads the example rather than guessing.** Which document is the example — `stickbot`
`5dc85bc34f28cf4f6cee1f26` or `stickbot-for-bot-review` `111f975041ddb104a6028d45` — is settled
first, and the ellipse's dimensions come off it over REST. Both stay read-only.

**Where a defect is a question rather than an error, A answers it in writing before B builds it.**
The head's depth, the pupils and the gripper's facing are all of that kind: the model made a choice
and no source records one.

## Phase B — the model

**B0 — copy, and record what the copy is.** `stickbot-draft9p0` is copied at its named version
`t14 legs` `737db64e2567c96e2d3de63f` into a new document, `stickbot-draft9p1`. The copy carries
every tab's feature history, which is what makes the rest of this phase edits rather than a rebuild.
The new document id, workspace id and every tab's element id are written down before any edit, the
way [`../2026-08-23-draft9p0/register.md`](../2026-08-23-draft9p0/register.md) § *Where the work is*
records them. `stickbot`, `stickbot-for-bot-review` and `stickbot-draft9p0` stay read-only for the
whole draft.

**The edit order follows the derive graph, because a derived body updates under its consumer.**
`ball and socket` is derived into `head`, `foot`, `u limb`, `l limb` and `gripper`; `hinge` is
derived into `u limb` and `l limb`. Editing a consumer before its source means measuring it twice.

- **B1 — `robot sizes`.** Rename `#limbSeg` to `#limbCenter`, set `#fit`, and add whatever variables
  Phase A decided the head and the torso should own. Every rename is checked for the dimensions that
  read it, because a variable renamed out from under an expression fails the feature, not the table.
- **B2 — `ball and socket`.** The A2 rearrangement, and the slit profile's pattern center
  constrained to the origin so the sketch goes black. The step is written out in
  [`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md).
- **B3 — `hinge`.** The detent swap, and the snap direction the new arrangement gives.
- **B4 — `body`.** The shoulder and hip placements, `#boss_d`, `upper rounds`.
- **B5 — `head`.** Its own variables, the eye ellipse, the depth, the pupils.
- **B6 — `foot`.** The groove pattern's phase.
- **B7 — `u limb` and `l limb`.** The joints carved into the segment rather than stacked on the end
  of it, which is what `#limbCenter` means and is where the robot's extra 106.4 mm went.
- **B8 — `gripper`.** The body following the socket's profile, and the mouth's facing.
- **B9 — `stickbot`.** Width mates on the elbows and the knees, instances re-inserted from a named
  version rather than the workspace, the rest pose, and the feet symmetric.

**Every sketch this phase touches ends fully defined.** That is `req.model.design_intent`, and 9p0
shipped at least one sketch that was not. Blue is measurable — 9p1 checks it rather than looking at
it.

**Features are named in their dialog titles as they are made,** for the features this phase adds.
No frame is being taken here, but 9p2 photographs this model's tree, and a default name in the tree
is a default name in 9p2's pictures.

**What this phase writes down is the click path, not the picture.** `log/<part>.jsonl` records what
was edited, what it measured, and where a dialog did not behave as
[`../../../onshape-gui-howto.md`](../../../onshape-gui-howto.md) says. 9p2 replays that record; it
does not read the 9p0 guide to find out how a feature was built.

## Phase C — read it back and prove it

**Every number in the design source is compared against the model over REST.** This is 9p0's B2
repeated against a source that has changed, and it is the only thing that makes Phase B's claim
checkable. The comparison covers what B2 covered — bounding boxes, collar diameter, mouth, thinnest
wall, and the z-extent of every cut face — plus the numbers Phase A moved.

- **The robot's height comes out at what the sheets draw.** 9p0 measured 421.8 against a drawn
  315.4, and A1 says all of the difference is the two limb segments.
- **The variable table is driven and put back**, as 9p0's B3 did, so a `#limbCenter` or `#fit`
  change is shown to move the robot rather than break it.
- **`#fit` is driven to its extreme.** The point of A2 is that the socket's height does not move
  when the fit does; the way to show that is to move the fit and measure the socket.
- **The model is opened and turned.** *Model inspected* is a gate this draft claims, and reading a
  report about a model is not looking at it.
- **A named version is published**, which is *Recovery point* and is what 9p2 starts from.

## Phase D — register, and what 9p1 hands on

`register.md` records what Phase A decided and on what evidence, what Phase B edited, what Phase C
measured, and every defect from 9p0's register that is now closed — by name, so the two registers
read as a pair rather than as two lists. A defect that turns out to be wrong is withdrawn in
writing, the way 9p0 withdrew the 431.97 height.

**What 9p2 inherits from 9p1 is a version, a design source and a log.** Not a guide and not a frame.

## Sketch of draft9p2, which gets its own plan

Enough to say what 9p1 has to leave behind. The plan itself is written after 9p1's register.

- **A new document, `stickbot-draft9p2`, from empty**, built tutorial by tutorial with the harness
  capturing, which is the *Steps reproduce* gate this draft does not claim.
- **One page reading `stickbot-draft9p1` and one page building `stickbot-draft9p2`, in the one
  driven context.** Settled by experiment on 2026-08-25 rather than assumed: two authenticated
  Onshape documents hold open in one profile, and a second driven browser buys nothing a second
  page does not. What the page count does cost is the attach — `connect_over_cdp` reaches every
  target, so 9p2 connects once, keeps both handles, and closes what it opens. The measurements and
  the failure mode are in
  [`../../../browser-access.md`](../../../browser-access.md) § *Two Onshape pages at once*.
- **`parent: draft9p0` for the pages**, so 9p2 inherits the words, the order and the click paths
  that survived, and replaces every frame.
- **The materials it reads** are 9p1's register and log, 9p0's register and `b1/notes.md`,
  [`../../../build/plan/`](../../../build/plan/00-manifest.md), the briefs, the corrected sheets,
  and the earlier guides for the conventions draft9p0 lost — `robot-guide4` carries the toolbar
  close-ups, the video links, the `image::` step shots and the sections draft9p0 dropped, including
  the one that teaches a student to pin a pattern's center.
- **The conventions are a requirement, not a memory.** `req.carry.conventions` is the rule 9p0 broke
  by taking prose from three pages and conventions from none.

## What we do not know yet

- **Whether A2's rearrangement holds the ball at 0.08.** The mouth goes from 96% of the ball to
  about 82%, and whether that snaps together by hand at this wall thickness is a print question.
  Nobody has printed the 2× robot.
- **Whether the head's depth and the pupils are decisions or defects.** Phase A has to make the call
  with nothing in the record to appeal to.
- **Whether `#wall`'s three declarations can be one variable** or whether the three tabs genuinely
  want different numbers that happen to coincide today.
- **Whether copying the document carries the tab element ids.** If it does not, every id in 9p0's
  register is stale for 9p1 and B0's first job is to re-read them all.
- **How much of the gripper is a re-CAD.** Following the socket's outside profile may be a new body
  rather than an edited one, which is the one item in Phase B that could turn into a rebuild.

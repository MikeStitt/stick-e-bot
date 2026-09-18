# Reorganizing drawings and engineering notes

Running notes. Mike's decisions are the record; anything I add is marked *(mine)*. Nothing here is
applied until it says it is. **The past is not being fixed** — this changes what future runs and
future engineering investigations capture, and touches an existing file only where that file is the
thing being changed.

## Settled

### A label describes what is inside the document, not the document

**Settled 2026-09-17 by Mike.** `superseded` applies to a document that describes an engineering
approach we are no longer using. It is a statement about the content, not about the artifact, and
not about whether anything has replaced the artifact.

So the question *is this document out of date* is not the one being asked. A frozen record of a
dead approach is `superseded` and is doing its job; the label warns the reader what is inside.

### `.docs/reviews/hinge/` stays `superseded`

**Mike ruled on 2026-09-17, overturning his own earlier reading of it as illustrative.** It
describes the cone-and-valley detent, which is an approach we no longer use, so it is superseded by
the definition above.

*(mine)* The label it was given on 2026-09-16 was right, and for the right reason: the joint it
draws is not the joint the robot has. I then argued the label belonged to the artifact rather than
the content, and proposed splitting it into a role axis and a subject axis. That is withdrawn. One
axis, and it points at the content.

**The nine labels of 2026-09-16 all stand**, because every one of them was assigned on what the file
contains. Nothing has to be relabeled.

Nothing about the three changes below turns on this. They follow from what `ninja hinge` reads,
which is nothing outside `.docs/reviews/hinge/source/`:

- **The PNGs come out.** They are renders of SVGs that are already tracked, and `.gitignore:31`
  `*.png` refuses every one of them, so the raster half of this document has never been in git.
- **The document runs on the SVGs.** `index.rst` carries eleven `.. figure::` directives and every
  one names a `.png`.
- **The build fails when an input is missing.** Today it warns and exits 0.

## What is measured, before any of it is done

- **Eleven figures, all pointing at `.png`**: `frames`, `slot`, `burial`, `ear`, `axle`, `wedge`,
  `beams`, `stroke`, `rim`, `connectors`, `blade-connector`.
- **Five of those PNGs exist on disk; six do not.** All eleven SVGs exist and are tracked.
- **`ninja hinge` exits 0 with six `WARNING: image file not readable`.** Measured 2026-09-17 after
  deleting `build/`. A fresh clone has no PNGs at all and still exits 0.
- **Which five exist is a property of this machine, not of the repository.** `render()` only runs
  when the agent browser answers on 9223, and it has only ever run for part of the set.
- **One reference to a PNG lives outside the review**:
  [`build-briefs/hinge.md:65`](experiments/build-briefs/hinge.md) links
  `../../reviews/hinge/source/images/burial.png` in its table of what to look at. It repoints to
  the SVG with the same edit.

## How the build is made to fail

**Settled 2026-09-17: the wide `-W`.** `rule sphinx` in `build.ninja` is shared by `guide`,
`draft9p4`, `hinge` and whatever comes next, so `-W` goes on that one rule and every Sphinx
document in the repository fails on a warning. The guides may be carrying warnings nobody has
looked at; finding out is the point.

## Settled: a roots figure joins the brief sheets

**The right-hand panel of `burial.png` becomes a derived figure in `make_brief_sheets.py`.** It is
the one half of that figure that is still true of the robot, and it belongs beside the briefs rather
than inside a superseded review.

What it draws: the section Mike is looking at in `stickbot-draft9p1p6` — fork's limb up the page,
blade's limb down, pin on the origin, tongue in the slot with its relief slit, axle stub in the
bore — carrying `burial.png`'s right-hand dimensions:

| | from the pin | source |
| --- | ---: | --- |
| the fork's free length | 21 mm | `EAR_FREE` |
| the blade's free length | 20 mm | `TAB_FREE` |
| the fork's rod | 17 mm | `ROD_FORK` |
| the blade's rod | 18 mm | `ROD_BLADE` |
| each member, pin to the end of its rod | 38 mm | derived, and symmetric |

**Every number comes from `make_plans`, so it cannot go stale.** That is the difference between it
and the figure it replaces: `burial.png`'s numbers are frozen at the cone joint, and its captions
read 7.16 kgf and 33.21 kgf where the current joint is 18.63 and 96.21.

*(mine)* Two things the new figure should not inherit. It needs no left-hand panel — the mistake it
contrasted against is draft9p1p1's and is recorded in the review. And it should not carry a press
force unless the figure says which motion: the review's number is `press()`, pushing the tongue down
the slot, while the joint's headline 75.2 N is `pinch()`.

*(mine)* `make_brief_sheets.py` has no ninja target, so this figure would be hand-run like the other
three. Worth fixing in the same change.

## Settled: one vocabulary for the joint

**Settled 2026-09-17 by Mike**, amended the same day to `blade leaf` and `stub axle`:

| Term | What it names | Cost |
| ---- | ------------- | ---- |
| `stub axle` | the protrusion that stands off the blade | **none — already the CAD's name** |
| `axle bore` | the hole it enters | two feature names |
| `blade leaf` | one of the two halves the relief slit divides the blade into | **none — already the word everywhere** |
| `fork prong` | the fork's arm that the axle bore passes through | the whole of *ear* |

**Three of the four adopt a word the work already uses.**

- **`stub axle`** is what the settled CAD calls it: features `stub axle outline` and `stub axle`,
  variables `#stub` and `#stub_proud`. `axle stub` would have renamed all four and gained
  nothing.
- **`blade leaf`** is what the variables and the solver already call it: `#leaf_root = 4.20 mm`,
  `#leaf_tip = 1.50 mm`, and `hinge_spring.py` builds `self.leaf` and opens *"The fork's ear and the
  blade's leaf are cantilevers cut out of the same rod."* It is also the right mechanical word: the
  thing is a leaf spring.
- **`axle bore`** is the only small rename: `pocket axle sketch` and `pocket axle on fork`.
  `#bore_d` already fits.

**And `blade leaf` removes the hazard.** Under `blade ear` the word *ear* would have moved from the
fork to the blade, so `EAR_FREE = 21` — the fork's free length — would have kept its name while its
meaning inverted, with nothing to catch it. Under `blade leaf`, *ear* is simply retired in favor of
*prong*. Nothing changes meaning; one word is replaced by another.

**What is left to rename is `ear`, and only `ear`**, counted 2026-09-17:

| | uses of *ear* |
| --- | ---: |
| `reviews/hinge/changes.md` | 103 |
| `instructions/stickbot-draft9p4/source/hinge.rst` | 101 |
| `src/stickbot/make_plans.py` | 42 |
| `reviews/hinge/make_figures.py` | 39 |
| `build-briefs/hinge.md` | 27 |
| `reviews/hinge/source/index.rst` | 23 |
| `instructions/stickbot-draft9p4/source/upper-limb.rst` | 21 |
| `build/plan/09-hinge.md` | 16 |
| `hinge_spring.py`, `wedge_figures.py`, `make_brief_sheets.py`, limbs brief | 40 |

Identifiers that move with it: `EAR`, `EAR_FREE`, `ear_free`, `EAR_MOVE`, `#ear`, and the CAD's
`ear`, `ear wedge`, `ear wedge outline`, `ear wedges`.

*(mine)* The superseded documents are left alone, per *do not fix the past* — which is a quarter of
the count, `changes.md` and the review between them.

**`blade blank` names the whole blade body, and `tongue` is dropped.** Settled 2026-09-17. That
completes the set: `blade blank` is the body, `blade leaf` is one of the two halves the relief slit
divides it into, `stub axle` stands off it, `axle bore` takes the stub, and `fork prong` is the
fork's arm the bore passes through.

`blade blank` is the CAD's own name for the extrude that makes it, so this is the same move as the
other three: adopt the word the model already uses. *tongue* appears **zero** times in the settled
hinge tab and **311** times in the tree, of which the live share is `make_plans.py` 32,
`build-briefs/hinge.md` 19, `robot-build-plan.md` 13, `09-hinge.md` 7, `hinge_spring.py` 5,
`make_brief_sheets.py` 3, `make_target.py` 3, `what-you-are-building.md` 4, and the two limb briefs
6. The rest is superseded documents and run records, which stay.

**`relief slit` stays the last feature on the blade.** Settled 2026-09-17. Task #153 put it there:
the axle is one extrude across the blade, so cutting the slit first lets a Ø `#stub` cylinder bridge
the two leaves at the pin, which contradicts the two-leaf spring `hinge_spring` solves. The name
`blade blank` carries its meaning without the build order having to argue for it.

## Settled: the briefs drop their CAD renders and point at the reference model

**Settled 2026-09-17 by Mike. The edits are held until the reference model has a name.**

The briefs carry pictures because they once had none. The commit that added them says why: *"The
briefs had no pictures. Every agent so far has built the hinge from prose and a table, and the two
failures that cost the most were shape failures that passed their numbers."* A live reference model
answers that better than a still — it turns, it sections, and it measures.

**The three `study-socket-*` renders were looked at on 2026-09-17, beside views rendered from the
current CAD the same hour. None is current, and each fails differently:**

- **`study-socket-in-a-limb`** — the limb is round. Today's is flatted top and bottom, `FLAT`
  10.4494, settled by task #157. The collar also fills the end face where today it leaves a broad
  shoulder: 15.6 in 24 against the study's 9.4 in 12.
- **`study-socket-in-the-head`** — the head is a plain cube. The real head is an arch with a domed
  top, two elliptical eyes and a mouth slot.
- **`study-socket-sectioned`** — the same round limb, cut.

What all three get right is the socket's own topology, collar and four slits and a spherical
cavity, which is what `brief-socket.svg` already carries in section and dimensioned. What they add
is context, and all three get the context wrong.

**What goes**, once the reference has a name: five rows from
[`build-briefs/ball-and-socket.md`](experiments/build-briefs/ball-and-socket.md)'s drawings table —
the three `study-*` and the two `run2-*` — leaving `brief-socket.svg`; the sentence *"The `.png`
beside the `.svg` is the same drawing"*, which is false now; and the paragraph in
[`build-briefs/README.md`](experiments/build-briefs/README.md) explaining `run2-*.png`, which
describes files this repository does not have.

**What stays.** The paragraph *"The socket is round. Run 2's socket reads as a square block because
the brief told it to stand the collar on a 20 x 20 pad, and it did."* That is a warning against a
mistake that was made, the reference model cannot show it because the defect is not in the current
model, and the prose carries the argument without the picture.

**Why the edits are held.** A brief that cites *the reference CAD* has to name a document and a
version. draft9p1p6 holds the settled joints; draft9p4 is meant to be the whole robot and is not
finished. Until one of them is the answer, the citation cannot be written.

## Done: the CAD surveyed for the best reference, part by part

**Performed 2026-09-18.** Every stickbot document was listed from Onshape, every Part Studio in
the twelve draft documents was read through `bodydetails`, the leading candidate for each part was
compared against `make_plans.py`, and each one was then rendered, turned and sectioned and looked
at. The frames and their provenance are in
[`build-briefs/images/`](experiments/build-briefs/images/) and
[`build-briefs/README.md`](experiments/build-briefs/README.md) § *Where the `cad-*.png` frames
came from*.

### What each part's reference is

| Part | Document | Version | Tab | Agrees |
| ---- | -------- | ------- | --- | ------ |
| body | `stickbot-draft9p4` | `tutorial 8 - the foot` | `body` | yes |
| head | `stickbot-draft9p4` | `tutorial 8 - the foot` | `head` | yes |
| ball and socket | `stickbot-draft9p4` | `tutorial 8 - the foot` | `ball and socket` | yes |
| foot | `stickbot-draft9p4` | `tutorial 8 - the foot` | `foot` | no, the tread |
| hinge | `stickbot-draft9p1p6` | `F done - Phase F proved` | `hinge` | yes |
| u limb | `stickbot-draft9p1p6` | `F done - Phase F proved` | `u limb` | yes |
| l limb | `stickbot-draft9p1p6` | `F done - Phase F proved` | `l limb` | yes |
| gripper | `stickbot-draft9p1p1` | `Recovery point` | `gripper` | no, the collar |

**The answer is per part, as the task expected.** draft9p4 is the newest document and its `hinge`
tab still holds 264 faces with 48 spheres and 48 tori, which is the bump-and-valley joint
draft9p3 built; draft9p1p6's holds 258 faces with 96 cones, which is the wedge ring. No document
holds the whole robot at the settled joints.

### `stickbot-draft9p4-check` holds work the plan did not put there

**Found 2026-09-18, after the survey above was first written, by reading the run's own log.** The
plan gives the two documents one job each: *the build document branches the version named in
`from`; the check document starts empty*, and Phase W reproduces the written page into the check
document. Every `document` row in
[`runs/2026-09-08-draft9p4/log/`](experiments/runs/2026-09-08-draft9p4/log/) names
`stickbot-draft9p4-check` and none names `stickbot-draft9p4`, and the `why` beside them splits in
two.

| Log | What its `why` says | Phase |
| --- | ------------------- | ----- |
| `torso`, `head`, `assembly` | `audit.page follows <page> from an empty document` | W, as the plan asks |
| `ball-and-socket` | `tutorial 4 is built and captured in the reader's document` | T, in the wrong document |
| `head-socket` | `tutorial 5 is built and captured in the reader's document` | T, in the wrong document |
| `torso-joints` | `tutorial 6 is built and captured in the reader's document` | T, in the wrong document |
| `foot` | `tutorial 8 is built and captured in the reader's document` | T, in the wrong document |
| `hinge` | `tutorial 9 is built and captured in the check document` | T, in the wrong document |

Tutorial 4's 39 rows run the whole take there: `tab`, `stud_variables`, `stud_profile_sketch`,
`stud_revolve`, `cavity`, `slit_extrude`, both connectors, `hero`, `section` and `version`.

**The cost is the gate this draft exists for.** *Steps reproduce* asks that the page be followed by
someone who does not have the build in front of them. For tutorials 4, 5, 6, 8 and 9 the build was
in the same document, so nothing written down closes that gate for them.

**Both documents carry the same eight version names**, the check document stamped first every
time: tutorial 4 at 18:18 against 19:52, tutorial 8 at 08:55 against 09:39. The work reached the
build document as well, by a route the log does not record.

### What is in each document, measured

| Tab | Check against build | What it means |
| --- | ------------------- | ------------- |
| `ball and socket` | same shape, face for face | the survey's citation stands |
| `body` | same shape, face for face | the survey's citation stands |
| `foot` | same shape, face for face | the survey's citation stands |
| `head` | 5 faces each way, the eyes | the build document is the right one to cite |
| `hinge` | 264 faces on 2 bodies against 508 on 3 | different joints entirely |

- **The check document's eyes are 1.5 % oversize.** Each eye's end face is 102.0857 mm² there
  against 100.531 mm² in the build document, and 100.531 mm² is π × 8 mm × 4 mm exactly, which is
  `EYE_RX` by `EYE_RY`. The front face they are cut from differs by the same amount the other way.
  Nothing moved; the ellipse came back about 0.06 mm large on its major radius. That is a finding
  about the head page's eye step, and it is the near miss `diff_shape.py` exists to catch.
- **The check document's hinge is the settled wedge joint and the build document's is not.**
  Against draft9p1p6 at `F done - Phase F proved` it is 508 faces to 510, with 5 of its faces and 7
  of the reference's unmatched and none of them a face that moved.
- **Its fork is two loose prongs.** draft9p1p6's fork is one body of 252 faces. The check
  document's is two bodies of 125 faces each, `RMGD` and `RJED`, and the render shows them floating
  either side of the blade with no rod under them and nothing joining them. The blade, `JHD`, is
  whole at 258 faces and matches. Tutorial 9 is task #203 and still open, so this is unfinished work
  rather than a finished part that came out wrong.

**None of this moves the survey's answers.** The three tabs that agree are identical in both
documents, the head is exact in the one that was cited, and the hinge reference stays
draft9p1p6's version, which is complete, proved and published, where the check document's is
neither joined nor versioned.

**What is wrong with each construction moved to draft9p5's plan on 2026-09-18**, at
[`runs/2026-09-18-draft9p5/plan.md`](experiments/runs/2026-09-18-draft9p5/plan.md) § *What is
wrong with each construction available*. It belongs with the run that is going to fix it: a list
of what is defective in three half-right models is a statement about a date, and it dies when
draft9p5 ends. The briefs carry the frames and the rules; they do not carry the verdicts.

### What the numbers said

Every number below is `make_plans.py`'s, and the read agreed with it to the fourth decimal.

- **The settled socket** is in draft9p4, draft9p1p6, draft9p1p5 and draft9p1p4: collar radius
  7.8 mm, cavity 6.08 mm, ball 6 mm, stalk 3 mm. draft9p3, draft9p2, draft9p1p1 and draft9p1 read
  9 mm at the collar, which is the wall before `COLLAR_WALL` became `TORSO_H * 3 / 160`.
- **The head** is 84.221 mm tall, which is `HEAD_H` 72 mm plus `COLLAR_PROUD` 12.2205 mm. Its
  eyes stand 3 mm proud of a 60 mm deep body, which is what `head.md` asks for.
- **The foot** reaches 2.221 mm above the ankle center, which is `GRIP`.
- **The hinge and both limbs** carry `RING_OUT` 10.4494 mm, `RING_IN` 6 mm, `LIMB_FLAT`
  20.8988 mm, 24 wedges as 48 cone faces a ring, a Ø4.0 stub axle on the blade and a Ø4.1 bore in
  the fork. draft9p1p5 reads 10.392 mm across the flat and 9.992 mm at the ring, so it is the
  joint before the fifteen degree step.
- **Both hinge sources agree on the flat**, re-measured 2026-09-18 after `brief-fork.svg` turned
  out to have been drawing 10.3923 mm. draft9p1p6's `hinge`, `u limb` and `l limb` and
  draft9p4-check's `hinge` all read 20.8988 mm across, which is `LIMB_FLAT`. The stale number was
  draft9p1p5's, and draft9p1p5 is a source for nothing. draft9p4's own `hinge` reads 24.0000 mm and
  has no flats at all, because it is still the round-limb bump joint.

### Four findings the survey turned up

- **Two of the 59 reads were wrong, and the finding drawn from them is withdrawn.** The survey
  first read draft9p1p6's `hinge` at 258 faces on one body and its `u limb` at 24 faces, against
  510 on two and 270 at the named version, and concluded the workspace had lost the fork and most
  of the upper limb. Re-read later the same day, both tabs give exactly what the version gives,
  and all 46 hinge features report OK with the rollback bar at the bottom in both. Nothing is
  wrong with that document. Re-reading all 59 tabs put the error at those two and no others.
  **The cause was a rollback bar at feature 31 of the hinge**, which is `fork outline`, the first
  feature of the fork. It left the blade whole and reached `u limb` through its `add fork`
  derive, which is why those two tabs and no others. Mike saw it and cleared it.
  [`verification-lessons.md`](verification-lessons.md) § *A short read is a rollback bar* carries
  what to check, and why reading twice would not have caught it.
- **The foot's tread grooves are closed voids inside the sole.** The sole renders smooth from
  below, and the section on the Right plane shows eight rectangular cavities buried in the foot
  with material under every one of them. Task #215 already said the groove cuts the wrong way;
  the picture says it does not reach the outside at all.
- **No gripper has been built since the socket wall changed.** draft9p1p1's is the newest of the
  three and its collar is Ø18. The part is otherwise right: `CLIP_R` 5 mm and a Ø3.3 clip bore
  both read true.
- **Six of the eight briefs still carry the pre-wall socket.** `assembly.md`, `foot.md`,
  `head.md`, `limbs.md` and `torso.md` hold 21 occurrences of 10.9465 mm and 1.9465 mm between
  them, against the settled 12.2205 mm and 2.2205 mm, and `gripper.md` writes `2 × #collarR` out
  as 18.0 mm where it is now 15.6 mm. Only `ball-and-socket.md` was brought forward, by task
  #210, and `hinge.md` never had a socket in it. `head.md` also asks for the head to be shelled,
  and the section shows it solid.

### What the survey did not do

**The `stickbot` assembly was never read, rendered or measured.** The survey covered the eight
parts and stopped there, so `assembly.md` has no frame and nothing is known about whether
draft9p4's assembly is current.

That leaves three numbers in the briefs standing on arithmetic alone, and none of them can be
checked from a part's geometry:

- **`HEAD_B` 68.0 mm and `HEAD_T` 140.0 mm**, the head's underside and the top of the robot. These
  are robot-frame stations and exist only once the head is mated.
- **`BALL_SWING` 39.013&#176; per side.** A kinematic limit; `bodydetails` carries no such thing.

The briefs say so themselves rather than implying a check: the foot's row is marked `derived`, and
`assembly.md` writes *`make_plans.py` derives* beside a bullet asking for the swing to be measured
by posing the joint until it stops.
[`runs/2026-09-18-draft9p5/plan.md`](experiments/runs/2026-09-18-draft9p5/plan.md) § *Ring 3* is
where they get checked, because that is the first time there is a robot to check them on.

**One number that did stand on arithmetic now does not.** The foot's ankle boss, `#grip + #plate`
= 14.2205 mm, was inferred from a bounding box on 2026-09-18 and measured the same day: the plate's
top is a real face at z = −12.0000 mm with 1669.26 mm&#178; of area. The same read shows the tread
groove's faces at z = −22 mm and −20 mm, never reaching the sole at −24 mm, which is the closed-void
defect a third way.

### What the task got wrong about the order

Reverse chronological by creation date is draft9p4 and draft9p4-check on 09-09, draft9p1p6 on
09-08, draft9p1p5 on 09-04, draft9p1p4 on 09-02, **draft9p1p3 on 08-31**, draft9p1p2 on 08-30,
draft9p3 on 08-29, draft9p2 on 08-28, draft9p1p1 on 08-27, draft9p1 on 08-25 and draft9p0 on
08-23. The task's list left draft9p1p3 out and put draft9p3 and draft9p2 ahead of draft9p1p2
rather than behind them. Neither changed an answer: draft9p1p3 is draft9p1p2's hinge unchanged in
every measured number, and both are behind draft9p1p4 on the socket.

The task also says *don't go farther back than draft9p4* under a heading that lists eight
documents ending at draft9p0. It was read as naming where to start.

### How a section is produced

`shadedviews` cannot section. `cutPlane` and `sectionPlane` were passed to it and the image came
back identical to the call without them, byte for byte, so Onshape ignores the parameter rather
than refusing it. Sections come from the GUI's Section view instead, driven at a version where
the document is read only. The route, the view keys and the scale each frame was shot at are in
[`build-briefs/README.md`](experiments/build-briefs/README.md).

**The hinge sections on the Right plane and not the Front**, because its pin axis is Y: the Front
plane is perpendicular to the pin and cuts the gap between the blade's two leaves. The tab also
lays the fork and the blade end to end rather than engaged, so the section holds the blade alone
and `cad-hinge-right.png` carries the two of them meshing.

### The two cross rules, resolved

Both of the rules this task flagged were settled by the Constitution before the survey ran.

- **Citing a workspace** is allowed as of 7.0.0. The table above cites versions anyway, for the
  reason draft9p1p6 supplied.
- **The Capture-is-out gate** stopped denying these frames at 6.0.0: `check_images.py` scopes the
  capture rule to `^\.docs/experiments/runs/`, and `.gitignore` denies raster only under that
  path and under any `capture/`. The 23 frames are 1.9 MB in total and `ninja check` passes with
  them tracked.

## To do: clarify the definition in the memory

`memory/deciding-is-never-done.md` defines `superseded` as *"an older approach we are not doing any
more. Kept as the record of what was decided and why it changed."* That is close but leaves the
subject implicit, which is what let the reading drift. It gains the sentence that the label
describes what is inside the document and never the document itself.

## Not yet written down anywhere

Carried from the conversation of 2026-09-16 and 2026-09-17, so it is not lost:

- **CAD inputs are a closed, generated set** — `plan-assembly`, `plan-parts` from `make_plans.py`;
  `brief-fork`, `brief-detent`, `brief-socket` from `make_brief_sheets.py`. Both generators write to
  absolute paths off `repo_root()`, so the set can be enumerated mechanically rather than judged.
- **An engineering note is a dated argument** and files by when it was valid.
- **`plan-r1` … `r7` are CAD inputs frozen by hand, seven times.** Five map to a run by that run's
  own record: r3 to run6, r4 and r5 to draft9p0, r6 to draft9p1, r7 to draft9p1p1. r1 and r2 predate
  a run declaring the sheets as an input.
- **The brief sheets have no equivalent freeze.** Three SVGs, overwritten every run.
- **r3 is the case that decides the wording**: generated by the head-collar work on 2026-08-13,
  frozen by run6's phase 1 on 2026-08-14. Content and freeze point at different runs.
- **CAD capture is already outside `.docs/`.** `find .docs -type d -name capture` returns nothing.

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
draft9p3 built; draft9p1p6's holds 258 faces with 96 cones, which is the wedge ring. Neither
document holds the whole robot at the settled joints.

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

### Four findings the survey turned up

- **draft9p1p6's workspace has lost the fork and most of the upper limb.** Its register records
  `hinge` as two parts, `blade` and `fork`, and `u limb` at 270 faces. Read on 2026-09-18 the
  workspace gives one part and 258 faces for `hinge`, and 24 faces for `u limb`. `diff_shape.py`
  against the version puts it exactly: 252 hinge faces and 249 upper-limb faces are in the
  version and not in the workspace, and none of them is a face that moved. The document was last
  modified 2026-09-17. **This is the risk Branch Policy's original rule named, happening to a
  document this note was about to cite by workspace**, and it is why the table above cites
  versions. draft9p4's workspace, diffed the same way against `tutorial 8 - the foot`, is
  face for face identical on all four of its parts.
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

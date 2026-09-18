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

## To do: survey the CAD for the best reference, part by part

**Find the CAD closest to `make_plans.py` and `make_brief_sheets.py`, working backwards from the
most recently built.** The survey is what settles which document a brief cites, and it is owed
before the edits above can be made.

- **Reverse chronological, by build date**, not by version number: draft9p4, draft9p1p6,
  draft9p1p5, draft9p1p4, draft9p1p2, draft9p1p1, draft9p1, draft9p0, and the run documents behind
  them. The first match wins for each part, so the newest agreeing tab is the one cited. Don't go
  farther back than draft9p4.
- **Identify the workspace and the tab** for each part. A part's best CAD may not all live in one
  document: on 2026-09-17 draft9p4's `hinge` was still bumps and valleys while draft9p1p6's was the
  settled wedge ring, so the answer is per part, not per document.
- **Agreement measured, and eyeballed from enough views and cross sections to confirm it is the
  desired part.** `read_shape.py` and `diff_shape.py` against what `make_plans` computes, so
  *closest* is a number; and then the part is looked at, turned, and sectioned until it is known to
  be the part wanted. This is the Constitution's own rule — *look at the model, and keep turning it
  until you know what it is*, and *a measurement never stands in for the picture: when a number and
  a picture disagree, believe the picture and go fix the check*. An earlier draft of this task said
  *measured, not eyeballed*, which had it backwards.
- **Take a set of hero images per part, including cross sections.** A section is what the three
  study renders could not do and what `shadedviews` does not offer, so the survey settles how a
  section is produced before it promises one.
- **Cite the workspace.** Settled 2026-09-17 by Mike: the cited workspaces will not be moved out
  from under the citation. That is what makes a workspace citation safe here and it is why the
  survey does not wait on versions several of these documents do not have.
- **The frames live with the briefs**, in
  [`build-briefs/images/`](experiments/build-briefs/images/), tracked, so a brief can point at them
  and a reader gets them from a clone.
- **[`build-briefs/README.md`](experiments/build-briefs/README.md) records where each frame came
  from**, in enough detail to re-capture it: document name and id, workspace id, tab name and id,
  the view, and the render call. A frame that cannot be re-taken from its own record is not
  finished.
- **Record, per part**: the document, the workspace, the tab, the frames taken, and where each
  frame disagrees with the design source. A part with no agreeing CAD says so.

*(mine)* Two of those cross rules that are written down, and both need a decision rather than
silence.

- **Branch Policy says cite a named version, not a workspace.** Its words: *"Material that depends
  on a reference document MUST cite a named version, not the live workspace — a workspace moves
  under the class."* Mike's undertaking not to move them is the reason the risk is gone, but the
  rule is a MUST and this is a deliberate departure from it. Either Branch Policy gains the
  exception, or each citation carries both — the workspace to re-capture from, the version to prove
  what was seen.
- **The Capture-is-out gate refuses these frames.** `.gitignore:31` denies `*.png` everywhere and
  un-ignores exactly one place, `instructions/*/source/images/**`. These are `shadedviews` output
  and cannot be vector, so tracking them needs `.docs/experiments/build-briefs/images/**` un-ignored
  and `check_images.py` widened to match. That is the gate written for 1,235 MB of interim capture
  being asked to admit a small, deliberate, cited set — which is a real distinction and one the gate
  cannot currently express.

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

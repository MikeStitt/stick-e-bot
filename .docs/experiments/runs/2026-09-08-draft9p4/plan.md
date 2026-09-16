# draft9p4 — the whole robot at the settled joints, with every page followed to a part

**This draft retakes every tutorial the settled ball joint and the fifteen degree hinge reach, and
reproduces every page it writes into a second document by following its own words.** What it hands
on is a guide whose steps have been performed by someone who did not build the model.

## Why this draft exists

draft9p3 took nine tutorials and wrote nine pages against `stickbot-draft9p1p1`'s joints. Both
joints have moved since. draft9p1p4 settled the socket: `#wall` became `#torsoH * 3 / 160`,
`#collar` became `#stand`, `#grip` took `#ballLoss` off the mouth's half width, and the tab gained
`#stalk`, `#slit_in`, `#slit_d` and `#slit_out`. draft9p1p6 settled the hinge as twenty-four wedges
on a ring with a fifteen degree step, a Ø4.0 stub in a Ø4.1 bore, and a 6.10 mm ear. Neither reached
the guide, so [`09-hinge.md`](../../../build/plan/09-hinge.md) still describes bumps, valleys, a
Ø4.4 bore and a 6.4 mm ear, and `#wall` reads 3 mm on the torso page where the model now says
1.8 mm.

Two other debts come with it. draft9p3 ran nine takes back to back and wrote its pages afterwards,
so four findings that should have changed the next take became retakes instead. And the
*Steps reproduce* gate has never closed on any page in any draft: draft9p2 never made its check
document, and draft9p3 drove one page into its own and stopped with 143 blocks still in front of the
gate.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p4` |
| `parent` | `draft9p3` for the guide, its pages and its conventions; `draft9p1p6` for the joints' geometry **and construction**; `draft9p1p1` for the construction of `body`, `head`, `foot`, `gripper` and the assembly |
| `from` | the last version `stickbot-draft9p3` published, read at Phase P |
| `takes` | `variables.sizes` in tutorial 1, and everything under tutorials 4 to 14 in plan order |
| `gates` | every Quality Gate in [`.claude/rules/constitution.md`](../../../../.claude/rules/constitution.md) except *Floor & ceiling*, which this draft does not claim |
| `requirements` | all of `req.carry`, `req.model`, `req.page`, `req.shot`, `req.guide`, `req.log` and `req.audit` |

**`parent` names three ancestors and `from` names one.** The joints come from draft9p1p6 because
that is where they were settled and proved. The five tabs draft9p1p6 does not have keep the
construction draft9p3 built from draft9p1p1 and audited against it, and those audits stand for the
features ahead of each derive.

**This draft is its own reference for what it retakes.** No document holds the whole robot at the
settled joints, and none is built to make one. `audit.part` therefore diffs the four joint tabs
against draft9p1p6 and the rest against draft9p1p1's records, and the features after each derive in
`head`, `body`, `foot` and `gripper` have no counterpart in either. Those are checked against the
design source and by `diff_shape.py` against the previous attempt, which is weaker than a model
diff, and the register says so by name rather than reporting a pass.

**One gate is claimed here that no draft has claimed.** *Steps reproduce* is Phase W's
`audit.page`, and it is the reason this draft is shaped the way it is.

**One gate is not claimed.** *Floor & ceiling* asks that a session name the work every student
finishes and the work for whoever finishes early. Nothing under `instructions/` is a session plan:
the guide is fourteen tutorial pages, with no clock, no rubric and no session to name a floor in.
Cutting the pages into class sessions is teaching work and it is not this draft's job.

**And one gate has almost nothing in front of it.** *Links resolve* asks that every Onshape link be
opened in the access mode a student will have, and the guide carries one link: `www.onshape.com` on
[`before-you-start.rst`](../../../../instructions/stickbot-draft9p3/source/before-you-start.rst).
Every page has the reader open a document they made themselves, so no page asks anyone to open a
document Mike owns. What is untested on that page is the sentence beside the link, *the free plan
does everything in this guide*, and testing it needs a free plan account rather than an account
without ownership rights: the guide uses a Variable Studio, an assembly and derived parts, and the
claim is about what a free plan can do. That is a Phase P check on one page, not a gate over
fourteen.

## What the joint change reaches, tutorial by tutorial

Every consumer derives the joint rather than resketching it: `head` has `get socket`, `body` has
`copy ball stud`, `foot` has `add socket`, `gripper` has `copy socket`, `u limb` has `add socket`
and `add fork`, `l limb` has `add blade` and `add ball stud`. So the head's shell, the torso block,
the foot's pedestal and sole and the eyes and mouth do not move when the joint does. What moves is
the derive, where it lands, and any feature drawn after it or reading a joint variable.

| Tutorial | What this draft takes | Why |
| -------- | --------------------- | --- |
| 1 torso | `variables.sizes` only | `#wall` reads `#torsoH * 3 / 160`, which is 1.8 mm, where the page types `#torsoH / 32` and reads 3 mm. The torso block does not move. |
| 2 head | nothing | The head's shell, rounds, chamfer, eyes and mouth are all ahead of `get socket`. |
| 3 assembly | nothing | Both instances are the parts as tutorials 1 and 2 leave them. |
| 4 ball and socket | the whole tab | The settled socket, its five named tab variables, and tasks #118 and #119. |
| 5 head socket | `socket mount point` onward | The derive, the transform, the boolean and `head mate`. |
| 6 torso joints | `copy ball stud` onward, plus `torso shoulder profile` | The stud half moves with `#stand`; the profile is task #125, which is owed either way. |
| 7 mate head | the whole tutorial | The socket's connector moved, and the tutorial is a handful of steps. |
| 8 foot | `pedestal outline` onward | The foot, rounds, groove and ribs are ahead of the derive and carry. The pedestal does not: `#collar_r` and `#collar_down` are typed 9 mm, and the settled rows make them 7.8 mm and 10 mm. |
| 9 hinge | the whole tab | A different joint: a wedge ring where the page describes bumps and valleys. |
| 10 u limb | the whole tab | Never taken. Derives both joints. |
| 11 l limb | the whole tab | Never taken. Derives both joints. |
| 12 gripper | the whole tab | `clip profile` follows the socket's outside profile and is drawn after `copy socket`. |
| 13 assembly arms | the whole tutorial | Never taken. |
| 14 assembly legs | the whole tutorial | Never taken. |

**A carried tutorial proves it carried by measurement.** Tutorials 2 and 3 and the ahead-of-derive
half of 5, 6 and 8 keep draft9p3's frames only where `read_shape.py` says their geometry is what
draft9p3's log holds. Where a number differs, that step loses `captured` and this draft takes it.

**One step lost `captured` before the measurement, because a typed number cannot move.** Walking the
three moved rows downstream through draft9p1p1's dependency graph put `pedestal outline` and
`foot pedestal` on the retake list: they read `#collar_r = 9 mm` and `#collar_down = 9 mm`, which are
the settled `#ball / 2 + #wall` and `#collar` written out as constants, so at the settled rows they
are 7.8 mm and 10 mm. `read_shape.py` cannot find this, because the foot measures as exactly what
draft9p3 built. [`notes.md`](notes.md) § *Three rows moved* carries the walk.

## What changes in the process, and why each change is here

Each of these exists because draft9p3 did the other thing and wrote down what it cost.

- **A tutorial is one unit of work, and it is not finished until its page is written and
  reproduced.** draft9p3's plan asked for the interleave and the run batched anyway, because the
  thing driving it read Phase T and Phase W as two blocks. Nine takes stood against one commit to
  the guide, and four findings sat unhonored: two captions from tutorial 2 and two shots from
  tutorial 5, each of them a retake rather than a sentence written differently. The unit here is
  [`00-manifest.md`](../../../build/plan/00-manifest.md) § *What "do tutorial N" means*, all five
  conditions, and `audit.page` is inside it. Tutorial N + 1 does not start until tutorial N is done.

- **The take hashes each frame as it writes it and refuses a second name for the same bytes.**
  Hashing draft9p3's captures found five repeated images in `torso`, two each in `assembly`, `foot`,
  `head` and `mate-head`, and one each in `ball and socket` and `hinge`. The take knew the bytes and
  the caption at the moment it wrote them and checked neither, so `version-03` in `torso` claims a
  Versions and history panel that is not in the picture.

- **`cad.version` opens Versions and history before it shoots, and `cad.tree` frames the tree.**
  The tail of every tab was `cad.hero`, `cad.tree` and `cad.version` shooting the same window, so
  every page lost its picture of the versions list and got the same hero three times.

- **A frame that can only be taken once is taken on the first pass.** Two of tutorial 1's
  duplicates can never be retaken: the Workspace units dialog as it arrives, on Inch with `0.123`,
  and the empty document before the units are set. `stickbot-draft9p4-check` starts empty and is the
  last chance at both, so `audit.page` on tutorial 1 captures them.

- **Every sketch step reads back what it drew before the next step runs.** `blade profile` is four
  entities and cost eight attempts, no two of them the same mistake, and four of the five findings
  left a blade that looked right: two moved nothing visible, two left it 0.03 mm and 0.002 mm off
  center. `read_sketches.py` and `diff_geometry.py` caught all of them and keep answering while
  `/features` is refused.

- **`audit.part` runs both halves on every tab, and compares `order` against `features` first.**
  The dependency graph reads `torso shoulder profile` and the reference as identical, because they
  stand on the same five things and carry every constraint but one projected line; only
  `diff_sketches.py` sees it. And a read failure looks exactly like a missing feature: three
  features returned an empty dependency panel, and `read_construction.py` still lists those in
  `order` while leaving them out of `features`.

- **The shape half says how far a face moved.** `diff_shape.py` follows each unmatched face to the
  nearest face of its kind and size in the reference and reports the distance, compares a cylinder
  by its axis line rather than by whatever origin the read carried, and rounds before it compares.
  The audit that lacked all three passed a foot whose pedestal was 0.98 mm off the origin.

- **The rename sentence is fixed on every page before the first page of this draft is written.**
  `audit.page` drove tutorial 1 into `stickbot-draft9p3-check` and found that clicking a dialog's
  title does not open the name box: the box is summoned by a pencil that appears on hover, and the
  letters typed at the title reach the sketch as tool shortcuts. Every page that names a feature
  carries a version of that sentence. Task #169.

- **The reference is read in full before Phase T starts, and the record holds `expression`.**
  draft9p3 read draft9p1p1's construction through the GUI because `/features` was rate limited to
  zero, then had to correct the record when the route answered. Phase P0 below reads draft9p1p6
  once, paced, before any tutorial is taken.

- **A tutorial whose numbers are not settled is not taken.** Tutorial 5's page had to be written
  around two decisions that are Mike's, and tutorial 4 built a ball and socket that is
  draft9p1p1's only at `#torsoH` 96 mm. § *What is settled before the take starts* lists what is
  open now.

## What REST may do in this draft

REST reads, and it moves whole documents. It does not build the model.

- **Reading, without limit.** `/features`, `bodydetails`, `parts`, `boundingboxes`, `getVariable`
  and every other read route, in any tab of any document in scope. Every check script and every
  audit runs this way.
- **Making and copying workspaces.** Creating `stickbot-draft9p4` and its check document, copying
  one workspace into another, and publishing a version.
- **Moving the camera.** Pan, zoom and rotate, so a frame can be taken of what a page will show.
- **Not the CAD.** Every sketch, extrude, mirror, pattern, derive, mate connector and variable a
  page teaches is made in the GUI, at the clicks the page will print. A page is written from the
  frames of a feature being made, and a feature written over REST has no frames.

## Phase P0 — the construction record for the settled joints

**Nothing in Phase T starts until this exists for the tab that tutorial builds.** `reference/` under
this draft holds one record per tab of `stickbot-draft9p1p6`, at the version
`F done - Phase F proved`, id `80c22eb7b8b0342ac03f8a6d`: the feature list with each feature's type,
name and position, what each is built on, and for every sketch its entities, its constraints and
what each dimension measures from.

- **Five tabs to read**: `robot sizes`, `ball and socket`, `hinge`, `u limb`, `l limb`. The two
  coupons are printing aids and are not tutorials.
- **draft9p3's `reference/` is carried, not re-read.** `body`, `head`, `foot`, `gripper` and the
  assembly still take their construction from draft9p1p1, and those nine records are on disk.
- **Record where draft9p1p6 itself types a number**, the way draft9p3 recorded it for draft9p1p1.
  Where the reference is not anchored either, this draft matches the reference and the departure is
  written down as a question for the design source.
- **`hinge`'s two variable naming conventions are recorded as they are**, not tidied. Ten of its
  variables carry the GUI's `###name = #value` template and six carry a bare name; the naming is a
  Phase P decision, not a P0 one.

## Phase P — the plan, and what it amends

- **Rewrite [`09-hinge.md`](../../../build/plan/09-hinge.md)** to the wedge ring. Its steps, its
  shots and its prose all describe a joint that no longer exists.
- **Amend [`04-ball-and-socket.md`](../../../build/plan/04-ball-and-socket.md)**,
  [`05-head-socket.md`](../../../build/plan/05-head-socket.md),
  [`06-torso-joints.md`](../../../build/plan/06-torso-joints.md),
  [`08-foot.md`](../../../build/plan/08-foot.md),
  [`10-u-limb.md`](../../../build/plan/10-u-limb.md),
  [`11-l-limb.md`](../../../build/plan/11-l-limb.md) and
  [`12-gripper.md`](../../../build/plan/12-gripper.md) where a joint number or a joint variable
  appears, and [`01-torso.md`](../../../build/plan/01-torso.md) for `#wall`.
- **Assign every new Variable Studio row to the tutorial that first needs it.** `robot sizes` grew
  from eleven rows to twenty-three between draft9p1p1 and draft9p1p6, and no plan file says which
  tutorial types which. A row typed before a tutorial needs it is a number with nothing to explain
  it.
- **Amend [`onshape`](../../../../.claude/skills/onshape/SKILL.md) § *Rename features*** with the variable exception, once Phase P has driven the box and knows what the page can tell a reader to do.
- **Fold tasks #118, #119, #125 and #169 into the files they fall in**, so they are steps rather
  than a list somebody has to remember.
- **Create `stickbot-draft9p4` and `stickbot-draft9p4-check`**, and record every element id. The
  build document branches the version named in `from`; the check document starts empty.
- **Copy `instructions/stickbot-draft9p3/` to `instructions/stickbot-draft9p4/`** and clear only the
  frames the retaken steps own. Tutorials 2 and 3 keep every frame they show, except the version
  dialog: it shows draft9p3's version list under `Main`, which is a picture of a document the reader
  is not building, so it is cleared in every tutorial including the two that carry. Done
  2026-09-09; 199 of 796 frames carried, and the accounting is in
  [`notes.md`](notes.md) § *The guide inherits 199 of draft9p3's 796 frames*.
- **Keep `images/toolbar/`.** A close-up of a button is a picture of Onshape, not of this draft's
  robot.
- **Close by rereading draft9p3's `notes.md` and draft9p1p6's register.**

## Phase T — the take

The tutorials in [`00-manifest.md`](../../../build/plan/00-manifest.md)'s order, each a loop of
*step, `audit.step`*, then `audit.part` over the whole tab, then straight into Phase W for that
tutorial. What this draft adds to [`takes.md`](../../../build/takes.md):

- **The construction record is open while the step is driven, and the step follows it.** A departure
  is recorded and carried; it is not made silently and it is not fixed mid-take.
- **A frame is hashed and captioned at the moment it is written**, and a second name for the same
  bytes is refused.
- **A pick inside a Part Studio gets the medium view and the close-up**, the same as an assembly
  pick.
- **A named version is published at the end of each tutorial**, and the tutorial's steps cite it.

## Phase W — the page, and the reproduction that closes it

One page per tutorial, written from that tutorial's log and the frames it names, immediately after
its `audit.part` passes and before the next tutorial is taken.

- **`page_sweeps.py` runs on the page first.** It was clean on all nine of draft9p3's pages across
  765 figures, 143 `.. step:` blocks and 58 recorded keystrokes, and it is what catches a figure
  published twice, a picture with no sentence above it and a keystroke the page never mentions.
- **`audit.page` then reproduces the page into `stickbot-draft9p4-check`,** following only what is
  written, by someone who does not have the build in front of them. This is the *Steps reproduce*
  gate and it is the reason the interleave is enforced: a sentence that does not work is found while
  the next tutorial can still be written differently.
- **A finding from `audit.page` reaches the next tutorial's take**, and the register says which ones
  did.

## Phase R — the register

`register.md` records what was built, what each audit attacked, what it found and what was done
about each finding. Every step gets its `state` and its `version`. Every gate claimed in the
declaration gets the evidence that closes it, by name, and a gate that did not close says so.

## The variable naming rule

**A variable feature keeps Onshape's title, `###name = #value`, so its tree row reads its name and
its value.** Every other feature gets a typed name. Settled 2026-09-08.

The tree row is the picture a reader checks a number against, and the title is what puts the number
there. `#wedges = 24` names the variable and gives its value; `stub` gives the name only, and a
reader has to open the feature to see 4 mm. It costs a student nothing, because the title arrives
holding that string and the GUI offers no way to type over it.

**Two tabs are out of step and this draft brings them back.** `hinge` has eight typed titles
(`nose`, `ear`, `stub`, `stub_proud`, `bore_d`, `slit_h`, `rod_blade`, `rod_fork`) and `ball and
socket` has five (`#stalk`, `#slit`, `#slit_in`, `#slit_d`, `#slit_out`), all of them renamed at
draft9p1p4 and draft9p1p5. Every one of `stickbot-draft9p1p1`'s 69 variables is on the template, so
the template is what a tab looks like when nobody types over it.

**What the display tracks is the title and nothing else.** Six of the ten templated titles in
`hinge` hold equations and still show a computed value; `stub` holds `4 mm` and shows no value
because its title was typed over. Whether an expression is a constant or an equation does not
change what the row reads.

**Phase P drove the box on 2026-09-09, and there is no box.** A variable was added in
`stickbot-draft9p3-check`, framed at each step and deleted, by
[`scripts/variable_title.py`](scripts/variable_title.py). Frames are in
[`capture/variable-title/`](capture/variable-title/).

- **The title arrives reading `#? = 0`, and it tracks the dialog as it fills.** Typing the name
  alone leaves it at `#? = 0 mm`; committing the value turns it into `#probe = 7 mm`. The row and
  the title are the same string, and it is computed, not stored.
- **The Variable dialog has no rename pencil.** The pencil's element is in the page and stays sized
  to nothing, whether the title is hovered, its 28 px hover area is hovered, the variable is empty
  or the variable is complete. In the same session an `Extrude` dialog put its pencil at the same
  spot on the first hover.
- **The variable's tree row has no Rename.** Its menu is *Edit…*, *Add selection to folder…*,
  *Suppress*, *Dynamic suppression*, *Add comment*, *Show dependencies…*, *Delete*. `torso block`'s
  menu carries *Rename* second. `F2` on the selected row does nothing.
- **The same is true of a variable that already carries a typed name.** `nose` in draft9p1p6's
  `hinge` is offered no Rename either, so the thirteen typed titles cannot be put back by renaming.

So the rule stops being a preference. **A student cannot type over a variable's title, so every
variable a page builds arrives on the template and stays there.** The page says nothing about
naming a variable, and the naming sentence every other feature's step carries is left out of this
one. The thirteen typed titles come back to the template by being built fresh in draft9p4, which is
what every tutorial does anyway.

## What is settled before the take starts

Each of these changes a number a page would teach, and none of them is a question for whoever is at
the CAD.

**A sketch stands on a face of the robot.** A stock plane is used where the sketch needs the torso's
center, which is where the planes are and where no face is. Where a face and a plane are about
equally good, the face wins. That decides `pivot lines`, which draft9p1p1 stood on `Origin`, `Top`
and `Front` and draft9p3 followed. Settled 2026-09-09.

The fifteen degree joint has been printed and Mike reports it good in the hand. That settles
`#t_print` 0.10 mm, `#wedge_h` 0.75 mm and `#wedge_c` 0.15 mm, and no page waits on a printer.
One thing stays open and does not block a take: the pinch has never been measured.

## Variables arrive at the step that needs them

**Settled on 2026-09-11 by Mike: entering a lot of variables at the start of a lesson is boring,
and no tutorial opens with a table of numbers any more.** A `robot sizes` row and a Part Studio
variable alike are typed immediately before the first feature that reads them, with the terms a
rule is written from going in alongside it. The rule and the ledger are
[`../../../build/plan/00-manifest.md`](../../../build/plan/00-manifest.md) § *A variable is typed at
the step that first reads it*.

**Which feature first reads which variable was measured, not decided.** Walking every expression in
`reference/*.features.json`, `robot-sizes.features.json` included, gives the first geometry feature
that depends on each name once chains of variable-reads-variable are followed through. That is what
placed all twenty-three studio rows and the tabs' own.

| Tutorial | Was | Is |
| -------- | --- | -- |
| 1 | five studio rows before the sketch | three, and the box is drawn from all three |
| 2 | twelve tab variables into an empty tab | seven steps, each above the feature that reads it |
| 4 | eleven in one step | four steps, the largest of them four rows |
| 6 | one studio row and eight tab rows up front | four steps |
| 9 | eleven studio rows, then eighteen tab rows, then the geometry | nine steps |

**Two placement defects came out of the same walk.** `#limbCenter` and `#wall` were typed in
tutorial 1 and read by nothing until tutorials 9 and 4; and `10-u-limb.md` carried a
`cad.parts.u_limb.variables` step declaring `#limbD` in the tab, which would have shadowed the
studio row tutorial 6 types.

**The hinge keeps a block, and it is the geometry's doing.** Eight of its twelve studio rows are
the chain under `#flat`, and `blade profile` is the limb's cross-section, so the first sketch
genuinely needs all eight. The page introduces them as the cross-section rather than as a table.

**`#ear` and `#backlash` are dropped.** Nothing read either one — no feature and no other row
names them — so they were readouts a student would type and get no geometry for. Mike settled it
the same day: drop them. The hinge tab types sixteen rows rather than draft9p1p6's eighteen, and
the tab's tree is forty-four features rather than forty-six.

## What this costs

**Eleven tutorials of take, eleven of page, and fourteen of `audit.page`.** draft9p2 budgeted
fourteen tutorials at two robots' worth of CAD and reached six; draft9p3 reached nine takes and nine
pages and no reproduction. The reproduction is the new cost and it is the one the guide has never
paid.

**What is not thrown away**: draft9p3's fourteen pages, their order and their conventions, tutorials
2 and 3 entire, the ahead-of-derive half of tutorials 5, 6 and 8, every frame under
`images/toolbar/`, the nine construction records under draft9p3's `reference/`, and every tool in
`tools/` that draft9p3 built to make its audits separable.

## What we do not know yet

- **Whether `head mate` keeps its 0.8 mm.** Settled on 2026-09-11 by a spike, and the cure is a
  camera angle: turn the view off the socket's axis before picking, and the pick lands on the
  sphere's center with nothing else in `secondaryOriginQuery`. Tutorial 5's step changes from
  *look at the head from below and hide `socket mount point`* to *turn the view off the axis*, and
  it loses the hide. The spike, its four runs and what each one caught are in
  [`notes.md`](notes.md) § *The socket's own axis is what puts `head mate` 0.8 mm off center*.
  This bullet sat under *What is settled* until 2026-09-09, under a heading saying none of them is a
  question for whoever is at the CAD; it was one, and the answer is now in hand.
- **How the five joint connectors are spelled.** Settled on 2026-09-11 by Mike: a connector is
  named for the joint it is, in the style `left shoulder` or `left hip`, with `left` and `right`
  written out and the word *connector* left off, because the feature list already says it is one.
  So `body` carries `neck`, `left shoulder`, `right shoulder`, `left hip` and `right hip`, and the
  hinge's two lose the same word to become `fork to robot` and `blade to robot`. Three connectors on
  the torso mark where a stud is transformed to rather than naming a joint, and dropping the word
  leaves them nothing to be called; they take the idiom the limbs already use for the same job,
  `mate for fork`, and become `mate for shoulder stud`, `mate for hip stud` and `mate for neck stud`,
  with the two sketches under them `hip stud location` and `neck stud location`. Those three names
  are a reading of the ruling rather than the ruling itself.
- **`l limb`'s rod may reproduce volume the derived blade's arm already occupies**, and `u limb` has
  never been checked for the same thing. Both limbs are rebuilt here, so both are measured.
- **Whether `audit.page` can be driven at fourteen pages.** It reached the version step of one page
  in draft9p3. Nothing yet says what a full page costs to reproduce.
- **What the four features after each derive should be measured against.** `head`, `body`, `foot`
  and `gripper` have no model at the settled joint, and the design source is arithmetic rather than
  geometry.
- **Whether tutorials 2 and 3 carry.** They should, and `read_shape.py` is what says so.
- **Where the finished robot lives for a student who falls behind.** The *Recovery point* gate
  wants a published named version to start from, and the first page that links a document Mike owns
  is the first page *Links resolve* has real work to do on. The Constitution does not answer this:
  Mike ruled on 2026-09-16 that it does not track where a version of the stickbot lives.

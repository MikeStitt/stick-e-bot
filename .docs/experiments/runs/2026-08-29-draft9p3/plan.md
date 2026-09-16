# draft9p3 — the robot built from empty, the way the reference model was built

**This draft builds the robot from an empty document using `stickbot-draft9p1p1`'s construction, not
only its shape, and writes the guide from the frames that build produces.** What it hands on is a
set of instructions whose steps put a student's feature tree where the reference model's is.

## Why this draft exists

draft9p2 built six tutorials from empty, captured 470 frames, wrote six pages and audited every
step, part, block and page it produced. Every one of its `audit.part` records measured the shape
against 9p1p1 and matched: the torso's twenty faces, its 343120.267 mm³, its bounding box, all
identical face for face. Not one blocking finding was ever against the geometry.

It is superseded because the shape was the wrong thing to measure. draft9p2 reached 9p1p1's shape by
a construction of its own invention, and a page written from that build teaches that construction.
Its `pivot lines` block says so in its own words:

> Dimension it from the sketch's vertical axis with `#shoulder_half`. That is the torso's own half
> width, so the line stands exactly on the side face. Dimension the line's top end from the
> horizontal axis with `#torsoH / 2`, which is the top of the torso.

The side face and the top face are in the model already. That block re-derives both by arithmetic
from the origin and lands on them by agreement rather than by reference, which is what
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) § *Anchor each sketch to the
geometry that gives it meaning* is written to prevent: *"Never type a number to place or size
something a reference would have given you."*

**The rule was already written. The audit had no way to test it.** `bodydetails`,
`massproperties` and `boundingboxes` measure the finished solid, and two different constructions of
the same solid measure the same. `sketches?includeGeometry=true` returns evaluated geometry, and
draft9p2's six body sketches are coordinate-identical to 9p1p1's to four decimal places. The
difference lives in the constraints and in each feature's parameters, and nothing draft9p2 ran ever
read either.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p3` |
| `parent` | `draft9p2` for the pages, their order and their conventions; `draft9p1p1` for the geometry **and the construction** |
| `from` | `empty` |
| `takes` | the whole plan — every identifier in [`../../../build/plan/00-manifest.md`](../../../build/plan/00-manifest.md), in plan order |
| `gates` | every Quality Gate in [`../../../../constitution.md`](../../../../constitution.md) except *Links resolve* and *Floor & ceiling* |
| `requirements` | all of `req.carry`, `req.model`, `req.page`, `req.shot`, `req.guide`, `req.log`, `req.audit`, and `req.model.same_structure`, which this draft adds |

**`parent` splits three ways rather than two.** draft9p2 already split the pages from the geometry.
This draft takes the construction from 9p1p1 as well, and that is the field draft9p2 had no name
for.

## What changes, and why each change is here

Each of these exists because draft9p2 did the opposite and nothing caught it.

- **Read the reference's construction and write it down before taking a single step.** Phase P0
  below. draft9p2 was told to replay 9p1's log for the click path and rebuilt the shoulder from
  9p0's page instead, because the log was long and the page was to hand. A written construction
  record removes the choice: the take has one source and it is not a page.

- **A take reproduces the recorded construction, and reports a departure instead of making one.**
  Reaching the same shape another way is a deviation, and `Step.deviate` is where it goes.

- **`audit.part` diffs construction before it measures shape.** Feature for feature by type and
  parameter, sketch for sketch by constraint and by what each dimension references. A part whose
  shape matches and whose construction does not is a finding, and it is blocking, because the page
  is written from the construction. `tools/diff_sketches.py` is the sketch half and exits 1 on any
  difference; `tools/diff_construction.py` reads the dependency graph, which cannot see a
  constraint. Tutorial 6 passed every shape measure and failed this, which is what it is for.

- **The shape half says how far a face moved, not how many faces agreed.**
  `tools/read_shape.py` writes every face of a tab in millimeters and `tools/diff_shape.py` diffs
  two of those reads. A part built a millimeter out of place still shares nearly every face with
  the reference, so a count of the ones that agree reads as a pass; each face that does not match
  is followed to the nearest face of its kind and size in the reference, and the distance between
  them is the finding. The foot's pedestal is 0.98 mm off the origin, and the audit that preceded
  this tool called that residue a merged face and passed the tutorial.

- **A sketch step checks where its own geometry landed before it moves on.**
  `/api/partstudios/.../sketches?includeGeometry=true` answers while `/features` is refused, so a
  step can ask what it just drew and hold it against `reference/<tab>.geometry.json` with
  `tools/diff_geometry.py`. The pedestal was 0.98 mm off from the tab's first sketch and nothing
  looked until the whole tab was audited eight steps later. A step that computes a pixel from the
  camera proves the pick landed on what it aimed at, and a sketch that does not land where the
  reference's does is a failed attempt rather than a finding to carry.

- **A sketch is placed by picking the geometry that already says where it goes.** Where an edge, a
  face or a vertex would give the position, picking it is the step; a dimension from an axis to the
  same place is the finding. `req.model.visible_geometry` says this and was never tested, so Phase P
  gives it a test rather than another sentence.

- **The assembly is posed before it is mated.** draft9p2 left the head buried inside the torso
  because the identity transform is where Insert drops it, and the inherited page went on to tell
  students not to drag the parts apart. A person moves the head clear so the thing reads as a robot,
  and then mates it. The move is a step with frames, not a tidy-up.

- **Both documents exist before Phase T starts.** `stickbot-draft9p3` to build in, and
  `stickbot-draft9p3-check` for `audit.page` to reproduce into. draft9p2 never created its check
  document, so the *Steps reproduce* gate went unclaimed on all six finished tutorials and the miss
  had to be carried.

## Reading the construction while `/features` is refused

**`/features` answered from about 12:30 on Sat 29 Aug, and all eight of 9p1p1's tabs are now read
through it into `reference/*.features.json`.** What follows is how the run started before it
answered, kept because the GUI reads are still the quickest way to look at one feature.

`/api/partstudios/.../features` is the one route that carries constraints and parameters, and it
was rate limited to zero on both documents until then. Nothing this client does shortens that. The
GUI is not rate limited, and it carries the same skeleton.

- **`Show dependencies…` on a feature's right-click menu names what the feature was built on and
  what was built on it.** It is the anchoring test in one panel: a sketch placed by picking the
  block depends on the block; a sketch placed by arithmetic from the origin depends on the origin,
  a default plane and some variables. On 9p1p1's `pivot lines` it reads `Origin`, `Top`, `Front`,
  `#shoulder_half = 36 mm`, `#shoulder_drop = 8 mm`.
- **`Show dimensions` draws a sketch's dimensions without opening it for edit**, so what a
  dimension measures from can be read off a frame.
- **A published version opens dialogs that cannot write.** 9p1p1 carries `Start` and
  `Recovery point`, and a feature read there cannot damage the reference.
- **`/features` is read anyway once it answers, and the record is corrected against it.** The GUI
  route is what makes the work start today, not a replacement for the route that carries parameters.

## Phase P0 — the reference construction

**Nothing in Phase T starts until this exists for the tab that tutorial builds.** One file per tab
under `reference/`, holding for every feature its type, its name, its position in the tree, what it
depends on, and for every sketch its entities, its constraints and what each dimension measures
from.

- **Read it off `stickbot-draft9p1p1` and off nothing else.** Not 9p0's pages, not draft9p2's log,
  not this draft's memory of building it once already.
- **Record where the reference itself types a number.** 9p1p1's shoulder chain hangs off
  `#shoulder_half`, `#shoulder_drop`, `#boss_len`, `#boss_d`, `#tilt` and `#yaw` and not off the
  torso's faces. Where the reference is not anchored either, this draft matches the reference and
  the departure is written down as a question for the design source, not fixed in passing.
- **The record is the input to `audit.part`,** which is what makes the audit separable: a script
  diffing this draft's construction against a file has no memory of the build.
- **[`../../../../tools/read_construction.py`](../../../../tools/read_construction.py) writes the
  record and [`../../../../tools/diff_construction.py`](../../../../tools/diff_construction.py)
  reads two of them against each other.** The first walks a Part Studio's tree and takes
  `Show dependencies…` on every feature; the second prints the features that are built on different
  things, and the tally of how many features in each document stand on the model's own geometry
  rather than on a default plane and some variables.

## Phase P — the plan, and what it amends

- **Amend [`drafts.md`](../../../build/drafts.md)** with `req.model.same_structure`, with the
  anchoring test `req.model.visible_geometry` never had, and with the assembly pose.
- **Amend the fourteen files under [`plan/`](../../../build/plan/)** where P0 shows the brief's
  steps do not match how the reference is built.
- **Create `stickbot-draft9p3` and `stickbot-draft9p3-check`, both empty**, and record the element
  id of the Variable Studio, of every Part Studio and of the assembly in each.
- **Copy `instructions/stickbot-draft9p2/` to `instructions/stickbot-draft9p3/`** and delete every
  frame of the model under it. The guide is inherited for its words, its order and the four
  conventions draft9p2 established; its construction paragraphs are rewritten from P0.
- **The guide builds, and warns once for every frame that is gone.** `ninja draft9p3` reports 520
  unreadable images on a clean build. That number is the work left in Phase W, and it falls as each
  page is rewritten from its own capture; a page whose warnings have not gone to zero is not
  finished.
- **Keep `images/toolbar/`.** A close-up of the **Extrude** button with its tooltip showing is a
  picture of Onshape, not of this draft's robot, and `req.shot.true_state` is about model states.
  Twenty-two of them carry across, and a button whose look changes is retaken when the page that
  names it is written.
- **Close by rereading 9p1p1's register and draft9p2's.**

## Phase T — the take, tutorial by tutorial

The tutorials in [`plan/00-manifest.md`](../../../build/plan/00-manifest.md)'s order, each a loop of
*step, `audit.step`*, then `audit.part` over the whole tab. What this draft adds to
[`takes.md`](../../../build/takes.md):

- **The construction record is open while the step is driven,** and the step follows it. What that
  obliges is in [`takes.md`](../../../build/takes.md) § *Before it runs* and § *Running it*.
- **A pick inside a Part Studio gets the medium view and the close-up** the assembly picks already
  get, per [`shots.md`](../../../build/shots.md) § *Selecting a point always takes two frames*.
  Picking geometry rather than typing a number is what the page has to teach, and a page with no
  frame of the pick falls back on describing the number.
- **Publish a named version at the end of each tutorial.**

## Phase W — the pages

One page per tutorial, written from that tutorial's log and the frames it names, immediately after
its `audit.part` passes. `audit.block` runs on each `.. step:` block as it is written; `audit.page`
runs when the page is done, reproducing it into `stickbot-draft9p3-check`.

The four conventions draft9p2 established carry forward: a step's picture after the sentence that
gives the instruction as `image::` with `:class: shot`, a `.. step:` tag on every block, a toolbar
close-up for every tool the reader has to find, and the clip link at the end of every block.

**Run [`../../../../tools/page_sweeps.py`](../../../../tools/page_sweeps.py) on every page before
its `audit.page`.** draft9p2 wrote it after finding a byte-identical figure pair, twenty-two
pictures with no instruction above them and eleven unrecorded keystrokes on a page two close
readings had already passed.

## Phase R — the register

`register.md` records what was built, what each audit attacked, what it found, and what was done
about each finding. Every step gets its `state` and its `version`. Every gate claimed in the
declaration gets the evidence that closes it, by name, and a gate that did not close says so.

## What this costs

**The whole build again.** draft9p2's fourteen tutorials were budgeted at two robots' worth of CAD
and reached six. This draft carries P0 on top of that, and P0 is a read of nine tabs.

**What is not thrown away:** draft9p2's pages, their order, their conventions, `page_sweeps.py`, the
audit vocabulary, and everything its audits found about frames and captions. The words survive. The
construction paragraphs inside them do not.

## What we do not know yet

- **How much of draft9p2's construction actually differs.** The body tab is read in
  [`notes.md`](notes.md): four of thirty-three features are built on different things, and the
  dependency graph cannot see the constraints the difference actually lives in. The other eight tabs
  are still to read.
- **Whether 9p1p1's own construction is anchored.** Its `pivot lines` depends on `Origin`, `Top`,
  `Front` and two variables, and not on `torso block`. Matching the reference and anchoring to
  visible geometry are different targets there, and only the design source can say which this draft
  builds. [`notes.md`](notes.md) carries it as a block.
- **Whether `Show dimensions` is readable enough to record what a dimension measures from,** or
  whether that has to wait for `/features`.
- **Whether the check document is one document rolled forward or a tab per tutorial.** Rolling one
  forward makes each tutorial's reproduction depend on the last, which is how a student works and
  is also how one bad tutorial stops the audit.

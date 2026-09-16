# draft9p2 — the robot built from empty, audited at every part and every step

**This draft builds the robot from an empty document with the harness capturing, writes the guide
from those frames, and audits both as it goes.** What it hands on is a set of instructions that has
been followed to a measured part.

## Why this draft exists

draft9p1 and draft9p1p1 made the model right and proved it by measurement. Between them they
captured nothing and wrote no page, and neither claimed *Steps reproduce* nor *Names are real*.
draft9p0 has the words, the order and the click paths that survived; every picture in it shows a
robot at half size.

Guide 4 lost its conventions when every page was written after every take. 9p0 dropped sections of
`robot-guide4` and broke `req.carry.conventions`. 9p0 published a 431.97 mm standing height read
off the bounding box of a posed assembly, which is not a standing height, and withdrew it. 9p1's B2
counted blue pixels and told a selection from a miss badly. 9p1 deleted a variable from the foot,
watched the feature that read it get shorter, and measured no change in volume, because a union had
welded that material into the derived socket.

The model this draft takes is `stickbot-draft9p1p1`, which is 9p1's model with the socket's slit,
the collar's base and the gripper's clip top repaired —
[9p1's register](../2026-08-25-draft9p1/register.md) and
[9p1p1's Phase B](../2026-08-26-draft9p1p1/plan.md) record the repairs.

## The declaration

| Field | Value                                                                                                                          |
| ----- |--------------------------------------------------------------------------------------------------------------------------------|
| `draft` | `draft9p2`                                                                                                                     |
| `parent` | `draft9p0` for steps, `draft9p1p1` for geometry and Onshape modeling structure                                                 |
| `from` | `empty`                                                                                                                        |
| `takes` | the whole plan — every identifier in [`../../../build/plan/00-manifest.md`](../../../build/plan/00-manifest.md), in plan order |
| `gates` | every Quality Gate in [`../../../../constitution.md`](../../../../constitution.md) except *Links resolve* and *Floor & ceiling* |
| `requirements` | all of `req.carry`, `req.model`, `req.page`, `req.shot`, `req.guide`, `req.log`, and the `req.audit` family this draft adds    |

**`parent` names two ancestors.** [`drafts.md`](../../../build/drafts.md) assumes one ancestor
supplies both the guide and the model. A **model-repair draft** splits them, and Phase P settles it
in `drafts.md` as a kind of draft.

**`from: empty` is why the gates are claimed.**
[`takes.md`](../../../build/takes.md) § *Where it starts decides what it may claim* says a take
starting from a version cannot report that the steps work. This one starts from nothing, so it can,
and owes the evidence.

**Two gates are out of scope, and saying so before the run is what keeps the rest honest.**
*Links resolve* asks that every link be opened in the access mode a student will have; the only
account available owns every document, so a link that opens proves ownership rather than access.
This draft reports that its links resolve for the owner and claims no more. *Floor & ceiling* is a
property of a session plan under `instructions/`, and this draft takes none.

## What "adversarial" means here

An audit that is handed the builder's account agrees with it. These rules apply to every audit
below.

- **The audit reads the artifact and the design source, not the account.** A step's audit gets the
  model, the frames and the tutorial file's acceptance numbers. It does not get the log record
  saying the step went as written.
- **A clean audit lists what it attacked.** An audit with no attack list is not a pass.
- **A finding stands until it is answered in writing.** A builder who disagrees withdraws it in the
  register by name, with the measurement that withdraws it. Silence closes nothing.
- **The auditor is separated by its inputs, not by who runs it.** Where a check can be a script it
  is a script, because a script has no memory of the build. Where it cannot, it runs in a session
  whose only input is the artifact. `audit.page` is the check that needs one.

## The audits

Each audit writes one `audit` record into `log/<part>.jsonl` beside the `step`, `frame` and
`verdict` records [`takes.md`](../../../build/takes.md) already defines: the identifier it covers,
what it attacked, and what it found.

### `audit.step` — what the step left behind

- **Read the feature back off the model and match it to the step's `creates`**, by name. A name
  that differs is a finding, not a rename.
- **Count under-defined sketch geometry with `is_sketch_blue`** from
  [`../../../../tools/onshape_screen.py`](../../../../tools/onshape_screen.py), with the sketch
  dialog closed and the tree green — `req.model.design_intent`.
- **Open every frame against its own `shows`**, written at the moment of capture.
- **Check that every keystroke's reason names something the reader can see on screen.**
- **The attack: roll the tree to this step and ask what a reader who stopped here would have.** A
  step whose part makes sense only once the next one lands is a step boundary in the wrong place,
  and that is a plan finding, not a take finding.

### `audit.part` — the part against the source, and against 9p1p1

- **Measure every acceptance number off `bodydetails` and `massproperties`**, never off the dialog
  it was typed into.
- **Measure the same numbers off `stickbot-draft9p1p1` on the second browser target.** A
  difference here outranks every other finding in the tutorial.
- **Match the sketches and features to `stickbot-draft9p1p1`'s, one for one.**
- **Drive the variable table and remeasure the part.** A number typed instead of linked does not
  move.
- **Confirm every sketch is fully defined, every feature and part carries its own name, and
  nothing is resketched that a derive already owns** — `req.model.design_intent`,
  `req.model.named_features`, `req.model.derive`.
- **The attack: what in this part holds only because of the order it was built in?**

### `audit.block` — the words against what happened

- **Write every keystroke in the block's log records into the block, or leave it out with a
  reason** — `req.page.view_keys`.
- **Check that every frame the block names is present, that every frame the step shot is used or
  accounted for, and that no two figures on the page share bytes.**
- **Read each figure against its own caption and its own alt text**, with the figure on screen.
- **Check the block against the conventions of every page written before it** —
  `req.carry.conventions`, while the block is fresh.
- **The attack: read the block as a student who has not seen the model.** Every noun it uses is
  either on the screen in the figure above it or was named earlier on the page.

### `audit.page` — the page followed to a part

**This is the *Steps reproduce* gate, per tutorial rather than once at the end.** A reader follows
the finished page and the part that comes out is measured against 9p1p1's.

- **Reproduce from the page and the pages before it, and nothing else.** The log is not an input,
  and neither is what the builder remembers of the build.
- **Hand the account of that reproduction to a reviewer that did not watch the build**, and let it
  rule on whether the page was followed or the build was recalled. A builder cannot judge that
  about itself, and that separation is what this check has in place of a clean session.
- **Return a measured diff and the point where the words ran out**, not prose about how the page
  reads.
- **Record a reproduction that stops as a finding at the step it stopped on**, which is the step
  boundary the page owes a sentence to.
- **Reproduce into `stickbot-draft9p2-check`,** never into the document the guide's frames come
  from. Adding it to the account needs the user's agreement, which Phase P gets before Phase T
  starts.

## The documents, and which one is written to

`connect_over_cdp` reaches every target, so this draft attaches once and keeps both handles —
[`../../../browser-access.md`](../../../browser-access.md) § *Two Onshape pages at once*.

- **Build in `stickbot-draft9p2`.** It starts empty and every geometry action lands here.
- **Read `stickbot-draft9p1p1` and never write to it.** It is the reference `audit.part` measures
  against.
- **`stickbot`, `stickbot-for-bot-review`, `stickbot-draft9p0` and `stickbot-draft9p1` stay
  closed.**
- **The context closes what it opened and nothing else.**

## The order, and why it is this order

**Nothing in Phase T starts until 9p1p1 has published its version and written its register.** A
tutorial built against a half-repaired reference gets built twice.

**The tutorials run as a pipeline, not as two phases.** `drafts.md` orders Take before Write for
the draft; within the draft this one runs tutorial N's take, its `audit.part`, its page and its
`audit.page` before tutorial N+1's take begins.

- **`req.carry.conventions` can only carry forward if the page ahead of it exists.**
- **`audit.page`'s findings are about steps, and a step is cheap to redo while its model is the one
  on screen.**
- **The cost: a later tutorial that moves earlier geometry reopens an earlier page.** `audit.part`
  on the later tutorial detects it — `drafts.md` § *Geometry that moves invalidates what comes
  after it* — and the reopened page is retaken, not patched.

## Phase P — the plan, and what it amends

- **Reread 9p1's and 9p1p1's registers and logs** and amend the tutorial files where either moved a
  number, a feature name or a step boundary.
- **Teach [`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) *Insert from the
  workspace, and keep every reference inside one document* in every tutorial that inserts an
  instance.** An assembly instances the Part Studios beside it in its own workspace, never a
  version.
- **Amend [`drafts.md`](../../../build/drafts.md)** with the model-repair draft — `parent` for the
  pages, `from` for the model — and with the `req.audit` family, so the audits are an obligation on
  every later draft, not this draft's habit.
- **Amend [`takes.md`](../../../build/takes.md)** with the `audit` log record.
- **Create `stickbot-draft9p2`, empty**, and record the element id of the Variable Studio, of every
  Part Studio and of the assembly.
- **Copy `instructions/stickbot-draft9p0/` to `instructions/stickbot-draft9p2/`** and delete every
  frame under it. The guide is inherited for its words and its order.
- **Carry back from `robot-guide4` what 9p0 dropped** — the toolbar close-ups, the video links, the
  `image::` step shots, and the section that teaches pinning a pattern's center.
  `req.carry.conventions` reaches backward as well as forward.
- **Close by rereading 9p1p1's register.**

## Phase T — the take, tutorial by tutorial

The tutorials, in the order [`plan/00-manifest.md`](../../../build/plan/00-manifest.md) lists them,
each one a loop of *step, `audit.step`* and then `audit.part` over the whole tab. That manifest's
§ *What "do tutorial N" means* says what each tutorial owes; [`takes.md`](../../../build/takes.md)
says what a take does. What this draft adds:

- **Set the units on the first page and nowhere else.**
- **Name every feature in its dialog title before filling the dialog in.** The tree row and the
  dialog header are both inside the frame, so a name typed afterwards cannot repair a picture
  already taken.
- **Shoot frames on the first pass.** The expensive part is driving the browser into the state.
- **Publish a named version at the end of each tutorial**, for the *Recovery point* gate, and it
  is where the next tutorial starts.
- **Replay 9p1's log for the click path, and 9p1p1's for what it changed.** Do not rebuild the
  step from 9p0's page. Only 9p1p1 records the gripper's clip top: the platform is the slab's own
  `2 * #collarR` width, and a sketch **Chamfer** of leg `#collarR - #clipR` necks it down onto
  the mouth's upper lip.

## Phase W — the pages

One page per tutorial, written from that tutorial's log and the frames it names, immediately after
its `audit.part` passes. `audit.block` runs on each `.. step:` block as it is written; `audit.page`
runs when the page is done, in its own session.

Four conventions reach every page, and the inherited pages hold none of them. Phase P counted:
across 9p0's eighteen pages there are no `image::` directives, no `.. step:` tags, no toolbar
close-ups and no clip links, where `robot-guide4`'s three pages carry between thirty-five and
ninety-two step shots each.

- **Put a step's picture after the sentence that gives the instruction, as `image::` with
  `:class: shot`** — `req.page.instruction_first`. `figure::` is the overview form and belongs at
  the top of a page.
- **Tag every block with `.. step:`, naming its identifier** — `req.page.step_tag`.
- **Give every tool the reader has to find a close-up of its button with the tooltip showing** —
  `req.shot.toolbar`.
- **End every block with its clip, worded *'Bot video of similar steps.*** — `req.page.video`.

## Phase R — the register

`register.md` records what was built, what each audit attacked, what it found, and what was done
about each finding — closed, withdrawn with the measurement that withdraws it, or carried. Every
step gets its `state` and its `version`. Every gate claimed in the declaration gets the evidence
that closes it, by name, and a gate that did not close says so rather than going quiet.

## What this costs

**Two robots' worth of CAD.** The build is one; `audit.page` following every page is close to
another.

**The cheaper arrangement, considered and not chosen:** running `audit.page` once at the end, over
the whole guide, costs the same CAD, but every finding lands after every page is written, when it
is a rollback rather than an edit.

## What we do not know yet

- **Whether the reproduction can be scheduled as described.** The mechanism for handing a session a
  page, a browser and no history has not been built.
- **How much of 9p0's prose survives 9p1's and 9p1p1's geometry.** A page whose words describe a
  feature either draft moved is a rewrite, not an edit. Phase P answers it page by page.
- **Whether the check document is one document rolled forward or a tab per tutorial.** Rolling one
  forward makes each tutorial's reproduction depend on the last, which is how a student works and
  is also how one bad tutorial stops the audit.
- **What a new document's workspace defaults are.** 9p0 inherited its units from a copy.
- **Whether the print questions 9p1 and 9p1p1 left open belong here.** Nobody has printed the 2×
  robot, so `#fit` at 0.08, the socket's retention at a 2.92 mm wall, and the 4.9465 mm of free tab
  the relief slit leaves are unproven in plastic. This draft's measurements cannot settle them.
- **Whether a tutorial that builds a part its neighbor derives can be audited on its own.**
  `audit.part` measures one part at a time, and a defect welded into a derived body is invisible to
  it.

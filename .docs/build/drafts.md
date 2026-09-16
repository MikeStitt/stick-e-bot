# The draft — one turn of the cycle

A **draft** is one pass at the whole guide: plan it, take it, write it, register it. A draft
inherits the previous draft's guide entire and replaces only the part it retook, so every draft is
a complete set of instructions rather than a patch on the one before it.

**The build plan is one thing and it changes. The drafts are many and they do not.**
[`plan/`](plan/00-manifest.md) holds the current understanding of what the robot is and how it is
built, and a draft that learns something amends it. `.docs/experiments/runs/YYYY-MM-DD-draftMpN/`
holds what one attempt did, and nothing edits it after its register is written.

What a step is, is [`steps.md`](steps.md). How one take runs is [`takes.md`](takes.md). Which
frames a take owes is [`shots.md`](shots.md).

## The four phases, in order

| Phase | Reads | Writes |
| ----- | ----- | ------ |
| **Plan** | the parent's `register.md` and `log/`, and [`plan/`](plan/00-manifest.md) | this draft's `plan.md`; amendments to [`plan/`](plan/00-manifest.md) |
| **Take** | this draft's `plan.md`, [`plan/`](plan/00-manifest.md), [`shots.md`](shots.md), and the parent's `log/` | `log/<part>.jsonl`, frames under this draft's guide, `capture/`, a named Onshape version |
| **Write** | `log/<part>.jsonl` and the frames it names, the parent's guide | `instructions/stickbot-draftMpN/source/*.rst` |
| **Register** | `log/`, the guide, what happened | `register.md`; `state` and `version` on every step taken |

**Plan and Register are where the build plan changes; Take and Write only read it.** A take that
finds the plan wrong records the deviation and carries on — [`takes.md`](takes.md) says how — and
the plan is corrected in the next draft's Plan phase, where the correction is a decision somebody
made rather than a side effect of a run.

**A retake reads the parent's log, and does not read the parent's guide.** The log holds what the
last attempt actually did — the keystrokes and why each one was pressed, what each frame shows, what
was measured — which is the only written record of the click path, and a retake that cannot see it
improvises the step again from a one-line plan row. The guide is Write's output, and feeding it back
into Take closes a loop: a sentence that is wrong in one draft gets read back and built into the
next draft's model. **Replay the record; do not rebuild from the page.**

**Every phase reads the phase before it from a file, not from memory.** The Write phase does not
have the take in front of it, and the next Plan phase does not have the Write. If a fact is not in
the log or the register, it is not carried forward.

## What a draft declares before it starts

`plan.md` opens with the declaration, and nothing in the draft may contradict it.

| Field | Means |
| ----- | ----- |
| `draft` | this draft's name, `draftMpN` |
| `parent` | the draft whose guide and frames this one inherits, or `none` |
| `from` | `version <id>` — the parent's published version — or `empty` |
| `takes` | the identifiers this draft performs; everything under each one, in plan order |
| `gates` | which of the Constitution's Quality Gates this draft claims to close |
| `requirements` | which `req.*` below this draft claims to meet, and which it knowingly defers |

**The user says when a draft bumps `M`; otherwise it bumps `N`.** Nothing derives the increment
from what the draft does — it is a judgment about how far the work has moved, made before the draft
starts, alongside `gates`.

**What each start may conclude is [`takes.md`](takes.md).** It is the difference between a draft
that tests the frames and one that tests the words.

**A partial take starts from the parent's published version and no other.** The frames it keeps
show that model. Start from anything else and the guide holds two sets of pictures of models that
never existed at the same time, which nothing on the page would show.

**A model-repair draft publishes no page, so the draft after it names two parents.** Ordinarily one
ancestor supplies both the guide and the model. A draft whose whole purpose is to repair geometry
leaves the guide where it was, and the next draft inherits its pages from the last draft that wrote
any and its model from the repair — `parent: draft9p0 for steps, draft9p1p1 for geometry`. `from`
still names one thing, because a take starts in one place.

**`gates` is agreed before the draft runs, not claimed after it.** An early draft closes few gates
on purpose; what makes it honest is having said so first.

**`requirements` is the same promise at finer grain.** A gate is a property of the whole repository;
a `req.*` is one obligation on one artifact, and § *The requirements* below is the register. A draft
that cannot meet one says so in its declaration rather than in its register, where it would read as
an excuse.

## The guide is inherited, then partly replaced

**Copy the parent's guide to this draft's guide before anything is taken.** `stickbot-draft10p9`
starts as a byte copy of `stickbot-draft10p8` — every page, every frame. The draft is complete from
that moment, and everything the take does after it is a replacement.

This is what makes a partial retake produce a whole guide. It also makes the difference between two
drafts readable directly: `diff -r` over the two guide trees is exactly what this draft changed.

**A step's frames reach the guide only when an attempt is published, and publishing clears what
was there.** Every `images/<part>/<stem>-*.png` the step owns goes, then the winning attempt's
frames are copied in. Writing over them instead leaves the tail behind — a take that shoots six
frames where the last shot nine leaves frames seven, eight and nine in place, pictures of a model
this draft no longer builds, in a directory the page is free to point at.

**A step driven twice is two attempts, and both are kept until one is chosen.**
[`takes.md`](takes.md) covers the staging and the verdict. It matters here because it is what makes
the guide's frames a decision rather than a side effect of whichever pass happened to run last.

**Frames live under the guide and the log lives under the draft.** They are joined by the step
identifier and by nothing else, so the draft names the guide it wrote into and the guide names the
draft that wrote it.

## Geometry that moves invalidates what comes after it

**A retake that changes geometry invalidates every later step in the same Part Studio, and every
step in any part derived from it.** A Part Studio is an ordered feature list: change the third
feature and every frame of the fourth through the last shows a different model. The foot derives
the socket, so the socket moving reaches the foot the same way.

**A retake proves it changed no geometry by measurement, not by intent.** Read the model back and
compare each downstream step's numbers against the parent's log. Where they match, the parent's
frames stand and nothing downstream is retaken. Where they differ, those steps lose `captured` and
this draft either retakes them or is not complete.

This is the escape hatch for a frames-only retake — a bad framing, a stray dimension in shot, a
caption pointing at the wrong thing. Those change no geometry, and the measurement says so.

## Provenance is the step's `version`, and completeness is read off the plan

**A step's `version` names the Onshape version it was proven against, and the version name carries
the draft.** A step reading `state: published`, `version: stickbot-draft10p8-v1` inside draft 10.9
says its evidence came from 10.8 and was carried forward. No second field records that, and no list
of carried steps is maintained anywhere.

**A tutorial is complete in a draft when every leaf step under it is `captured` or `published`.**
That is a property of [`plan/`](plan/00-manifest.md), which is one file set rather than one per
draft, so the answer is the same for whoever asks. [`plan/00-manifest.md`](plan/00-manifest.md)
carries what *done* means for a tutorial.

**Which frames this draft took is read off its log, not declared.** The log holds one record per
frame taken. A frame in the guide with no record in this draft's log was carried forward, and the
most recent ancestor whose log names it is where it came from.

## Redoing part of the foot, worked

Draft 10.8 published every tutorial. Draft 10.9 needs two foot steps again, because the pedestal's
frames were shot at a framing that cuts off the collar.

- **Declare it.** `parent: draft10p8`, `from: version stickbot-draft10p8-v1`,
  `takes: cad.parts.foot.pedestal, cad.parts.foot.detent_ring`.
- **Inherit.** Copy `instructions/stickbot-draft10p8/` to `instructions/stickbot-draft10p9/`. All
  fourteen pages are now present and every frame they name is on disk.
- **Clear.** Delete `images/foot/pedestal-*.png` and `images/foot/detent_ring-*.png`.
- **Take.** Branch a `stickbot-draft10p9` workspace off the parent's version, roll the foot's
  feature list back to just before `pedestal`, and perform the two steps with the harness capturing.
- **Measure.** Read the foot back. Every step after `detent_ring` measures what 10.8's log holds, so
  their frames stand and nothing else is retaken. Publish `stickbot-draft10p9-v1`.
- **Write.** Rewrite the paragraphs of `foot.rst` that point at the new frames, from the log's
  record of what each one shows. Thirteen pages are untouched, and so is the rest of `foot.rst`.
- **Register.** Record the framing that failed, and set `version: stickbot-draft10p9-v1` on the two
  steps. Every other step still cites 10.8, which is what says the guide is two drafts deep.

The result is a complete, valid `stickbot-draft10p9` in which two steps are new and the rest is
inherited, and the plan says which is which without anybody maintaining a list.

## Where everything lives

```
.docs/build/                              the plan — one set, amended, never per draft
  lesson-plan.md steps.md shots.md
  takes.md drafts.md
  plan/00-manifest.md .. plan/14-*.md

.docs/experiments/runs/YYYY-MM-DD-draftMpN/
  plan.md                                 what this draft will do, and what it inherits
  log/<part>.jsonl                        what happened, one record per step and per frame
  register.md                             what was learned, and what is still open
  capture/                                events and footage

instructions/stickbot-draftMpN/
  source/<page>.rst                       the guide
  source/images/<part>/<stem>-NN.png      the frames
  build/                                  Sphinx output, not committed
```

**The final product is `instructions/stickbot-guide/`,** built from whichever draft is declared
finished. Until then there is no such directory, and a draft is not promoted by copying it there
early.

## What is committed

| Committed | Not committed |
| --------- | ------------- |
| `plan.md`, `register.md`, `log/<part>.jsonl` | `capture/*/frames/` and `capture/video*/` |
| the guide entire, carried-forward frames included | `instructions/*/build/` |
| `capture/*/events.jsonl` and `session.json` | |

**Carrying a frame forward costs nothing, because a copied file is the same object.** Git addresses
a blob by the hash of its contents, so a frame that thirteen drafts inherit unchanged is stored
once. The full-copy rule above is therefore free in history and costs only working-tree disk. Only
the frames a take actually shoots are new bytes.

**A screenshot does not compress and the events do.** Measured on run 7: a guide frame is 227 KB
and deflates to 221 KB, while `events.jsonl` deflates 9.3 times, so the 8.6 MB of events across the
whole run is under a megabyte in the object store. That ratio is the whole argument — the events
are the cheapest evidence in the tree and the footage is the most expensive.

**The footage is what gets dropped, and it is dropped permanently.**
`onshape_record.render()` builds the video out of `frames/`, timed by the events; the events alone
cannot reconstruct it. Run 7's `capture/` is 1.2 GB of exactly that, against 8.6 MB of events. The
record of what happened survives; the moving picture of it does not.

**The ignore lives once, at `runs/`, and not once per draft.**
`2026-08-16-human-run1/` has a `.gitignore` reading `capture/` and run 7 never got one, so 1.2 GB
has been sitting in `git status` as an untracked directory that every commit since has had to dodge
by hand. A rule that has to be remembered per draft is a rule that fails on the draft nobody
remembered.

## The requirements

Every obligation a draft carries, with a name. A requirement is here because it was learned the
hard way — from a run that went wrong, a page that regressed, or a review that found something
missing — and the register exists so the next draft inherits the lesson along with the frames.

**A requirement names an obligation; it does not restate the mechanism.** The third column is where
the mechanism lives, and that file stays the one place the rule is explained. Where the third column
says *here*, this file is that place.

**Three slots cite a requirement, and each belongs to a different actor at a different moment.**
A name with nowhere to be written is a name nobody uses.

| Slot | Written by | Says |
| ---- | ---------- | ---- |
| *Requirements in play*, and the `Req` column in [`plan/`](plan/00-manifest.md) | Plan | what this tutorial is holding, before the take |
| `.. req:` beside `.. step:` in the `.rst` | Write | which requirements shaped this block, for whoever edits it next |
| `unmet` in `log/<part>.jsonl` | Take | which one the attempt could not meet, and why |

**The first two say what should be true and the third says where it was not.** A requirement met
needs no record — the plan named it and the page holds it. Only the miss has to be written down,
because a requirement quietly dropped is indistinguishable from one that was never in play.

**Identifiers follow [`steps.md`](steps.md)'s grammar** — lowercase segments joined by dots, each
matching `[a-z][a-z0-9_]*` — so a requirement can be cited in a `plan.md`, a `register.md` or a
commit message the same way a step can. **A requirement's name is permanent.** Retiring one strikes
it through and says why; it never gets reused for something else.

### `req.carry` — what a draft owes its parent

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.carry.conventions` | A convention proven on one page applies to every page written after it. A page written later may not be poorer than one written earlier. | here |
| `req.carry.register` | A draft reads this register before it writes a page, and its `register.md` says which requirements it met, missed and deferred. | here |

**This is the requirement the others hang from.** Guide 4 taught the view keys, the toolbar
close-ups and the video links on `ball-and-socket.rst` and carried none of the three into the two
pages written after it. Nothing had gone wrong at the CAD and nothing failed a check — the second
and third pages were simply written without the first in front of them, which is the same failure
[`takes.md`](takes.md) fixes for the log and § *The guide is inherited* fixes for the frames.

### `req.model` — what the CAD must be

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.model.one_document` | The whole robot is built in one document, `stickbot`. A tutorial is a tab in it, never a document of its own. | [`plan/00-manifest.md`](plan/00-manifest.md) |
| `req.model.derive` | A joint is built once and derived wherever it is used. No part resketches a joint another part already owns. | [`lesson-plan.md`](lesson-plan.md) |
| `req.model.design_intent` | Every sketch is fully defined, and every dimension that follows the robot's size reads the variable table rather than a typed number. A typed number is allowed and the page says why. | [`modeling-practice`](../../.claude/skills/modeling-practice/SKILL.md) |
| `req.model.visible_geometry` | Where construction geometry and a typed offset would both work, the geometry wins, because a student can see it and change it. | [`lesson-plan.md`](lesson-plan.md) |
| `req.model.named_features` | A feature is named in its dialog's title before the dialog is filled in, the way a function is named before its body. Parts and tabs are renamed as they are made. No `Sketch 1` or `Part 1` survives into a frame except where the page is teaching the rename: the tree row and the dialog header both sit inside the picture, so a name typed afterwards cannot repair a frame already taken. | [`takes.md`](takes.md) |
| `req.model.same_structure` | The construction matches the reference model's, not only the shape: the same features in the same order, each built on the same geometry, each sketch carrying the same constraints, and each dimension measuring from the same thing. A part whose shape matches and whose construction does not is a finding, because the page is written from the construction. | here |
| `req.model.anchored` | A sketch is placed by picking the geometry that already gives its position. Where an edge, a face or a vertex says where something goes, picking it is the step; a dimension from an axis to the place that geometry already occupies is the finding. | [`onshape`](../../.claude/skills/onshape/SKILL.md) |
| `req.model.posed` | An assembly is posed before it is mated. Insert drops every instance at the identity transform, which buries the head inside the torso, and a mate picked in that state teaches a reader to leave it there. | here |

**`req.model.same_structure` is the requirement draft9p2 had no way to test.** Its `audit.part`
measured every face, the volume, the bounding box and a driven variable table against
`stickbot-draft9p1p1` and matched on all of them, because two constructions of the same solid
measure the same. `bodydetails`, `massproperties` and `boundingboxes` cannot see a construction,
and `sketches?includeGeometry=true` returns evaluated geometry, which is identical to four decimal
places whichever way the sketch was constrained. The difference lives in
`/api/partstudios/.../features` and in `Show dependencies…` on the feature's own right-click menu,
and the audit that claims this requirement reads one of the two.

**`req.model.one_document` is the one with a bill attached.** `ball-and-socket.rst` starts a
separate document because run 8p1 built it standalone, so meeting this requirement moves the joint
into `stickbot` and re-takes whatever derives from it.

### `req.page` — what a guide page must do

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.page.document` | The page names the document and the tab the reader is in when it opens, and the version it publishes when it closes. | [`onshape`](../../.claude/skills/onshape/SKILL.md) |
| `req.page.hero` | The page opens with a figure of the finished part and a caption giving its size. | here |
| `req.page.units` | Workspace units are set once, on the first page. No later page sets them, because they belong to the workspace and not to a tab. | [`plan/01-torso.md`](plan/01-torso.md) |
| `req.page.view_keys` | Where the build pressed a view key, the page tells the reader to press it and says what they will see. A reframe that happened silently between two frames leaves the reader looking at a different screen from the one in the figure. | [`onshape`](../../.claude/skills/onshape/SKILL.md) |
| `req.page.shortcut_form` | A tool is named, then its key in parentheses — **Extrude** (or press **shift+e**), dropping to (**shift+e**) once the reader has seen the pattern. Lower case, bold, no spaces inside the parentheses. | [`onshape`](../../.claude/skills/onshape/SKILL.md) |
| `req.page.key_as_action` | When the key press *is* the action, the sentence says to press it, and the key's letter is bolded inside the word it comes from — press **n** to look **n**ormal. | [`onshape`](../../.claude/skills/onshape/SKILL.md) |
| `req.page.direct_tool` | A tool with a toolbar button is reached by that button. **Search tools** is taught once, as itself, and is not the route to anything that has a button. | here |
| `req.page.step_tag` | Every block of steps carries the `.. step:` tag naming its identifier, so a paragraph can be traced to the step that produced it. | [`steps.md`](steps.md) |
| `req.page.instruction_first` | A step's picture follows the sentence that gives the instruction, as a plain `image::` carrying `:class: shot`. `figure::` and its caption are for the overview pictures at the top of a page. A caption sits under its picture, so a reader who follows one cannot read the instruction before doing the thing. | `custom.css` |
| `req.page.video` | Each block of steps ends with its clip, worded *'Bot video of similar steps.* | here |
| `req.page.advice` | An aside is `.. admonition::` with `:class: advice` — a nudge forward, not a hazard sign. | `custom.css` |
| `req.page.positive` | The page says what to do and what the reader will see when it works. The same facts, never framed as what goes wrong. | [`.claude/rules/parts/prose-style.md`](../../.claude/rules/parts/prose-style.md) |
| `req.page.unnumbered` | Headings and parts are not numbered, so inserting or reordering one costs no renumbering. | here |
| `req.page.plain_words` | The reader is a middle-schooler and the vocabulary is real CAD vocabulary. Say *handedness*, not *chirality*. | [`.claude/rules/parts/prose-style.md`](../../.claude/rules/parts/prose-style.md) |
| `req.page.spelling` | US English. | `src/stickbot/check_spelling.py` |
| `req.page.part_names` | A part is called the same thing in prose, headings, captions and frame stems. It is a *gripper*, never a *hand*. | [`steps.md`](steps.md) |
| `req.page.typed_values` | What the student types is set in ``literals`` and rendered black, not the theme's red, so a value to copy does not read as a value that went wrong. | `custom.css` |
| `req.page.no_counts` | The prose does not count what the reader can see. No *three things*, no running tallies, nothing that has to be re-edited when an item is added. | [`.claude/rules/parts/prose-style.md`](../../.claude/rules/parts/prose-style.md) |

**`req.page.view_keys` is the complaint that started this register.** A reader following guide 4's
head never returns to isometric, never zooms to fit and never hides the planes, because no sentence
tells them to — and the keys appear in no specification, so nothing caught it.
[`takes.md`](takes.md) now records every keystroke with the reason the reader will be given, which
is what makes this requirement checkable rather than a habit.

### `req.shot` — what a frame must be

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.shot.toolbar` | Every tool the reader has to find gets a close-up of its button with the tooltip showing, so a reader who does not know where it lives can still follow. | [`shots.md`](shots.md) |
| `req.shot.two_frame` | A pick gets two frames: one at medium range for context, one close up with the ring on what was picked. This reaches edges, not only points. | [`shots.md`](shots.md) |
| `req.shot.planes_hidden` | A sketch shot has the default planes hidden, so nothing gray sits behind what is being drawn. | [`shots.md`](shots.md) |
| `req.shot.caption_moment` | The caption describes the frame beside it, at the moment the frame was taken. | [`takes.md`](takes.md) |
| `req.shot.true_state` | A frame shows a state the build actually passed through. A composed picture of a model that never existed is thrown away, not shipped. | [`takes.md`](takes.md) |
| `req.shot.one_use` | A frame appears once. Two figures on a page with the same bytes are one picture used twice, and the second shows the reader nothing. | [`takes.md`](takes.md) |
| `req.shot.width` | A step image is four-fifths width and centered. A figure fills the column it sits in, because it carries a caption under it. | `custom.css` |

**`req.shot.true_state` is owed to the head's mouth.** One frame showed a 20 mm slot alongside
dimensions that were placed later, which is a state the build never passed through; it was thrown
away and the dimensions it contradicted were deleted so the reshoot could follow the true order.

### `req.guide` — what the guide has that no page has

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.guide.plan` | The guide opens with the whole robot — a picture of it finished, and the plan of how it gets built — before the first part. | here |
| `req.guide.before_you_start` | A page saying what the reader needs in front of them before step one. | here |
| `req.guide.habits` | A page of working habits, written as things to do. | here |
| `req.guide.size_once` | The robot's overall size is stated once, on the plan page, so a design change edits one line. | here |

### `req.log` — what a take must write down

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.log.shows` | Every frame carries what it shows, written at the moment it is taken. | [`takes.md`](takes.md) |
| `req.log.keys` | Every keystroke is recorded with the reason the reader will be given for it. | [`takes.md`](takes.md) |
| `req.log.verdict` | Practice and performance are separated. A verdict says which attempt stands, and only that attempt's frames reach the guide. | [`takes.md`](takes.md) |
| `req.log.deviation` | A step that did not work as written records what happened instead, and the plan is corrected in the next Plan phase rather than mid-take. | [`takes.md`](takes.md) |

### `req.audit` — what checking the work must be

| Requirement | What it says | Where the mechanism lives |
| ----------- | ------------ | ------------------------- |
| `req.audit.artifact` | An audit reads the artifact and the design source. It does not read the builder's account of what it did. | [`takes.md`](takes.md) |
| `req.audit.attacked` | An audit says what it attacked. An audit with no attack list is not a pass. | [`takes.md`](takes.md) |
| `req.audit.answered` | A finding stands until it is answered in writing, in the register, by name and with the measurement that withdraws it. | here |
| `req.audit.reproduced` | Every page is followed to a part by someone who does not have the build in front of them, and the part is measured against the reference model. | [`takes.md`](takes.md) |

**This family is the *Steps reproduce* gate taken apart into things that can be checked while the
work is still warm.** Every draft before draft9p2 checked its own model against its own account of
building it, which is the one comparison that cannot fail. `req.audit.reproduced` is the expensive
one and the only one that settles whether a page is any good; the other three are what make it
affordable, by catching at the step what would otherwise be found at the page.

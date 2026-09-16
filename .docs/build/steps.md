# The step, and its identifier

A **step** is one conceptual move in building the robot. Its **identifier** is the name that move
is called by — in this build plan, in the Python that performs it, in the log of what was
performed, and in the page a student reads. One move, one name, whoever is doing it.

This file is the grammar. What the steps are, and in what order, is the build plan itself —
[`lesson-plan.md`](lesson-plan.md) for the order of the tutorials, [`plan/`](plan/00-manifest.md)
for the steps inside them.

## The grammar

**An identifier is lowercase segments joined by dots.** Each segment matches `[a-z][a-z0-9_]*`,
words inside a segment are joined by underscores, and hyphens do not appear anywhere.

```
design.robot_plan_sketch
cad.parts.ball_and_socket.stud.profile_sketch
cad.parts.ball_and_socket.stud.revolve
fabricate.orientation
```

**One spelling, because the string is used verbatim wherever it is used at all** — a heading here,
an argument to the harness, the stem of every frame the step captures, a key in the log, a comment
in the `.rst`. A segment that has to be transliterated between two of those is a segment that will
one day be transliterated wrongly.

## The root is the pipeline

**There are three roots, and their order is the order of the work.**

| Root | Holds |
| ---- | ----- |
| `design` | the sketches that decide what the robot is, and what each one settled |
| `cad` | building it in Onshape — `cad.parts.*` and `cad.assembly.*` |
| `fabricate` | printing it, and putting the printed parts together |

**`cad.assembly` and `fabricate.assembly` are different work.** `cad.assembly` is the Onshape
assembly: mates, degrees of freedom, the bill of materials. `fabricate.assembly` is fourteen
printed instances and a LEGO bar in someone's hands.

## Structure at the top, procedure at the bottom

**The upper segments name a thing; the lower segments name what is done to it.**
`cad.parts.ball_and_socket` is a thing. `stud.profile_sketch` and `stud.revolve` are moves made on
it. Where the boundary falls is not fixed and does not need to be.

**Depth is not uniform, and a leaf is whatever the build plan declares a leaf.** In
`robot-guide4`'s `ball-and-socket.rst`, which is in the archive,
`stud.profile_sketch` runs from `bs-04` to `bs-11` — an arc, three lines and three dimensions —
while `stud.revolve` is one click and one figure. Both are leaves. A leaf that later needs its
parts named separately gains children and stops being a leaf.

## Order comes from position

**A step's order is where it appears: the position of its file in the manifest, then its position
within that file.** The manifest is the list of build plan files, in order. There is no step
number, and no `order` field.

**Moving a paragraph moves the step.** That is how work is reordered. The log records the order
actually performed, so a reorder nobody intended shows up as a difference between the plan's order
and the last run's, rather than as nothing at all.

**Identifiers are never numbered.** `step_1` and `step_2` name a position, and a position is the
one thing about a step that changes without the step changing.

## Renaming and supersession are pointers, not states

**A renamed step carries `was`, naming the identifier it had.** Frames, logs and pages written
under the old name stay findable, and two runs either side of a rename stay comparable.

**A step overtaken by later work carries `superseded_by`, naming what overtook it.** Supersession
is not retirement: `design.preliminary_sketch` was overcome by more detailed sketches and still
has a job on the page, showing a reader where the design started. A state would say it was
finished with; a pointer says what happened to it.

## What a step carries

Anything not stated takes its default.

| Field | Means | Default |
| ----- | ----- | ------- |
| `creates` | the Onshape feature the step adds, by the name that feature is given | `none` |
| `generator` | the Python that performs the step | `none` — performed by hand |
| `state` | `proposed`, `built`, `captured`, `published` | `proposed` |
| `version` | the named Onshape version the step was proven against | required when `state: published` |
| `audience` | `human`, `bot`, `page` — where the step is only for some of them | all three |
| `teaches` | the tool or idea a student earns here | `none` |
| `session` | which class session the step falls in | unassigned |
| `was` | the identifier this step had before | — |
| `superseded_by` | the identifier that overtook this one | — |

**`creates: none` is a statement, not an omission.** A step that adds a feature can be checked
against the feature list read back off the model; a step that adds none cannot, and says so. A
step silent about it has not been decided yet.

**`state` separates a step that works from a step somebody believes will work.** Run 8p1's plan
called for a box-select over two coincident points, and the box selects one of them — prose that
had never been performed, sitting in a document that did not distinguish the two. The Constitution
already forbids the claim; the field is where the answer is kept.

**A step's `version` names the draft that proved it, and that is the only record of provenance.**
Version names carry the draft — `stickbot-draft10p9-v1` — so a step inside draft 10.9 still citing
`stickbot-draft10p8-v1` says its frames were carried forward from the draft before. No second field
records that, and no list of carried steps is kept.

**A step can lose its `state` without being touched.** Changing geometry earlier in the same Part
Studio changes what every later step's frames show. [`drafts.md`](drafts.md) says when that costs a
step its `captured` and how remeasuring gives it back.

**`audience` marks the exceptions only.** Opening the document and parking the pointer are `bot`.
Pressing **n** to look normal at the plane is `human` and `page`, because the harness sets the
camera directly.

## Coverage and sessions are fields, not roots

**A step names what it teaches, and the coverage tables are read off the steps.**
[`robot-build-plan.md`](../robot-build-plan.md) carries a *Teaches* column on every feature and
three coverage tables counted by hand against the Onshape lessons. Once `teaches` is a field, the
tables are derived and the count cannot drift from the steps it counts.

**Which session a step falls in is a slice of `cad.*`**, not a root beside it. So is the clock.

## What the identifier ties together

| Where | How it appears |
| ----- | -------------- |
| the build plan | the step's heading |
| the Python | the argument the harness step is entered with |
| the frames | the stem of every image the step captures |
| the log | the key each entry is written under |
| the `.rst` | `.. step: <identifier>`, optionally `req: <list>`, and the frame names the page already references |

**The tag carries the requirements that shaped the block.** The form is a comment, so Sphinx
renders nothing:

```rst
.. step: cad.parts.body.outline
.. req: req.page.view_keys, req.model.design_intent
```

**`req` is what the paragraph is holding, not everything that applies.** The universal obligations
— US spelling, the advice class, the positive framing — are in
[`drafts.md`](drafts.md) § *The requirements* and go in no tag. A requirement is named here when
somebody editing this block could undo it without noticing: the sentence that presses **n** exists
because of `req.page.view_keys`, and it reads like a stray aside to anyone who does not know that.

**This is the slot for whoever writes the page next.** The plan says what is in play before the
take, the log says where the last attempt fell short, and the tag is the only one of the three that
survives into the guide and sits beside the words it constrains.

**An identifier appears many times in a page and once in a log.** Eight figures and five
paragraphs can belong to one step. So the check that page and plan agree is that every leaf
appears at least once and every tag resolves to a real identifier — not that the two match one for
one.

## The tutorial, and how it relates to a step

**A tutorial is the coarse unit: it starts and ends when the work moves from one Part Studio or
the assembly to the next.** It is the class-sized piece, and it is what a student and a teacher
experience as one sitting. Its boundaries are uneven on purpose — a tutorial is however long that
tab's work takes.

**A step stays what this file says it is**, one conceptual move: `stud.revolve` is a step, and so
is the whole of `stud.profile_sketch`. A tutorial holds many steps. Nothing about identifiers,
frame stems, log keys or `.. step:` in the `.rst` changes, because the noun that moved is the one
that had no name yet.

**A tutorial is not a field on a step and not a segment of an identifier.** It is implied by the
order in [`lesson-plan.md`](lesson-plan.md) — the tab changes, so the tutorial changes — which
means it cannot disagree with the order it is read from. This replaces `session` in the table
above.

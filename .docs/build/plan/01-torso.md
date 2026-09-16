# 1. The torso, and the three numbers it is drawn from

Starts from an empty document. Ends with a Variable Studio every later tab inherits, and a torso
box.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.document.units` | set the workspace to millimeters, five decimals | nothing |
| `cad.variables.studio` | make the Variable Studio | the element — no feature |
| `cad.variables.sizes` | `#torsoH`, `#torsoW`, `#torsoD` | three rows in the table |
| `cad.parts.body.rename` | name the Part Studio `body` | nothing |
| `cad.parts.body.outline` | sketch the torso rectangle, dimensioned from the variables | `torso outline` |
| `cad.parts.body.block` | extrude it `#torsoD` deep, and name the part `torso` | `torso block` |
| `cad.variables.rename` | name the Variable Studio `robot sizes` | nothing |

**Units come first, before the Variable Studio and before any sketch.** A new document is in
inches, and the setting is per workspace rather than per Part Studio, so it belongs to the
document. Opening the dialog part-way through a sketch closes the sketch.

**The Part Studio is renamed before the geometry; the Variable Studio after it.** `Part Studio 1`
and `Variable Studio 1` are not names. The body's rename comes first because every frame taken in
that tab afterwards shows the tab strip, and a stale name in the strip contradicts the page. The
Variable Studio's rename sits at the end because that is where it was performed and where its two
frames were taken — its canvas shows the finished torso, so the frames cannot move earlier without
being retaken.

**A dimension read by two Part Studios is declared in the Variable Studio.** That is this page's
rule for what the studio holds, and it is written here because this is the page that builds the
studio. It is not about whether a number belongs to a part conceptually — it is about whether a
second tab dimensions something with it.

**Three rows, because three is what the torso is drawn from.** The rectangle reads `#torsoH` and
`#torsoW` and the extrude reads `#torsoD`, and nothing else on this page or the next reads anything
else. The other twenty rows are typed on the page where each first means something —
[`00-manifest.md`](00-manifest.md) § *A variable is typed at the step that first reads it* has the
rule and which tutorial types what. It is one table either way, which is what stops a tab from
declaring a name the studio already carries and quietly shadowing it.

**The three arrive in one visit rather than two.** `#torsoD` is not read until the extrude, one step
after the sketch, and sending the reader back to another tab for a single number between two
adjacent features costs more than it teaches. They are the box's three dimensions and they are typed
together.

**`#limbCenter` and `#wall` used to be here and are not any more.** Nothing read either one until
tutorial 4 at the earliest, so the page opened with two numbers a reader could only copy.
`#wall` is now typed in [`04-ball-and-socket.md`](04-ball-and-socket.md), which is where `#slit_in`
first reads it, and `#limbCenter` in [`09-hinge.md`](09-hinge.md), where `#rod_blade` does.

## The shots this tutorial needs by name

**Requirements in play.** `req.page.units` — this is the only tutorial that sets them, and no
later page may set them again. `req.model.one_document` — `stickbot` starts here.
`req.page.document` — the first page is the one that says what to open.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the torso box, at the top of the page | `req.page.hero` |
| the *insert into all* control, on | it is a button holding a tick, not a checkbox, and **on is what it looks like when you arrive** | |
| the same control, off | the two frames next to each other are the whole explanation, and off has to be staged by clicking it | `req.shot.true_state` |
| the sketch before and after **view normal to** | a new sketch does not arrive normal to its plane, and the skew is the reason the step exists | `req.page.view_keys` |
| a variable name resolving in the sketch's dimension field | the payoff — the studio reached a tab nobody typed into | `req.model.design_intent` |
| the tree | at the end, filter box cleared | |
| the version dialog | publishing the named version | `req.page.document` |

**The variable-resolving frame is the one to get right.** Nothing else on screen shows that the
Variable Studio did anything: inserting adds no feature, and the tab's own variable list stays
empty because it reports only local tables. A name resolving in a dimension field is the only
visible evidence, and it is the reason the studio comes first.

**The *insert into all* control arrives ticked, and the plan had it backwards.** Tested from
clean, by deleting every Variable Studio in the document and making one: the **first** Variable
Studio in a document arrives with the box already ticked, and a **second** one arrives unticked.
So the frame of it *off* is staged — click it off, shoot, click it back on — and the page says so
rather than pretending the reader will find it that way.

## Built

**`state: published`.** Document `stickbot-draft9p4`
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 1 - variables and torso**. Read back off the model: elements `body`, `robot sizes`,
`Assembly 1`, `BOM : Assembly 1`; variables `torsoH 96 mm`, `torsoW 72 mm`, `torsoD 48 mm` and
nothing else; features `torso outline` (newSketch) and `torso block` (extrude), no feature in
error; the part named `torso`; bounding box `lowX -36 / highX 36`, `lowY -24 / highY 24`,
`lowZ -48 / highZ 48` mm, which is 72 × 48 × 96 mm centered on the origin.

**The build document branched draft9p3, so the studio arrived holding eleven rows.** They were
deleted before the step was driven, because the page starts at an empty table and a take that
starts anywhere else photographs a screen no reader has. Everything downstream of the eight rows
that moved to later tutorials went red until those tutorials type them again, and no frame this
page keeps shows one of those tabs.

**The design-intent acceptance test passes, driven through the variable table rather than REST.**
The sketch is a center point rectangle whose center is coincident with the origin, and both
dimensions are expressions on the Variable Studio rather than typed numbers, so a change to
`#torsoW` or `#torsoH` moves the box and nothing else.

**A Part Studio that existed before the Variable Studio inherits it anyway.** The tab a new
document arrives with resolved `#torsoW` in a dimension field. Building the studio first is a
convenience, not a requirement — which means a student who sketches first is not stuck.

**A new document arrives with a Part Studio and an Assembly.** That Assembly is the one
[`03-assembly-first-parts.md`](03-assembly-first-parts.md) renames and moves, so no step needs to
create it.

## Captured

**`instructions/stickbot-draft9p4/source/torso.rst`**, written from the frames in
`instructions/stickbot-draft9p4/source/images/torso/`. Sphinx builds it with no warning; all 31
frames on disk are used by the page and every frame the page names is on disk. No picture is
published twice.

**The page was reproduced into `stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) one block at a time,
reading only what the page says, starting from Onshape's own `Part Studio 1` and `Assembly 1`. It
ended with the same three rows, the same tree and the same box on the origin, and published
`tutorial 1 - variables and torso` there too. The audit is in
[`../../experiments/runs/2026-09-08-draft9p4/log/torso.jsonl`](../../experiments/runs/2026-09-08-draft9p4/log/torso.jsonl)
and what it found is in
[`notes.md`](../../experiments/runs/2026-09-08-draft9p4/notes.md) § *Tutorial 1 reproduces*.

**The reproduction found three things, and the page carries all three now.**

- The page had the two square-on views backwards: the first **n** from the arrival camera gives the
  near side, not the far one. Which side comes first depends on where the camera starts, and a tab
  remembers its camera, so the page says that rather than promising an order.
- The insert-into-all control on and off, which this file asked for, had both frames taken and
  neither placed. So did the Workspace units dialog as it arrives on Inch. All three are on the
  page.
- `document.units-05`, the screen after the units dialog closes, is the same screen as
  `document.units-01`. The page already says a unit change moves nothing you can see, so the frame
  was left unpublished rather than given a sentence.

**Driving the sketch taught two things about picks.** A freehand rectangle's corner snaps, so a
pick computed from millimeters misses the line it wants and the edges have to be read off the
screen. And the first dimension scales the rectangle uniformly, so the other pair of edges has
moved by the time the second dimension is picked.

## What we do not know yet

Nothing. **Whether the Variable Studio earns its own hero shot** was the last open question, and
the page answers it with two frames: the table empty, and the table with the three rows typed. The
empty one is what tells a reader the placeholder row is where they click, and it is the only
picture of a Variable Studio that has no geometry in it at all.

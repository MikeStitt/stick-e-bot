# The take

A **take** performs part of the build plan in Onshape and records what happened. It produces
frames, a log, a named version, and a difference against the draft it inherits from. A **retake** is
a take of a step that has been taken before; everything here applies to both, and the only thing
that separates them is whether the step already has frames to replace.

**The obligations this file carries a mechanism for are named in**
**[`drafts.md`](drafts.md) § *The requirements*.**

**A take does not decide what to take.** That is declared in the draft's `plan.md` before it starts,
and the cycle it belongs to is [`drafts.md`](drafts.md). What a step is, and how it is named, is
[`steps.md`](steps.md). How to drive Onshape's GUI is
[`onshape-gui-howto.md`](../onshape-gui-howto.md), whose hard rules — 9223 only, never close a page
you did not create, REST is read-only — hold for every take and are not repeated here.

## Scope is a subtree, and the subtree is the sequence

**A take names one identifier and covers everything under it.** `cad.parts.ball_and_socket` is a
part; `cad.parts.ball_and_socket.stud` is an evening's work; a single leaf is a re-shoot of one
figure. Order is positional, so naming the subtree names the sequence and there is nothing else to
specify.

## Where it starts decides what it may claim

| `from` | Produces | May conclude |
| ------ | -------- | ------------ |
| `version <id>` | frames, measurements, a page | nothing about whether the written steps work |
| `empty` | the same, and the *Steps reproduce* gate performed | that the steps get someone from nothing to the part |

**A take `from: version` that reports "the steps work" is claiming a verification it did not
perform.** Starting from a built model tests the frames, not the words. The empty start is the
Constitution's *Steps reproduce* gate being performed, and it is the only start that settles
whether the page is any good.

**`from: empty` covers the whole plan or it covers nothing.** A student does not get to start
halfway, so a partial take from empty performs the gate for no one.

## Before it runs

**Know the state of every step in scope, because it decides what a difference means.** Against
`proposed`, a difference is a finding. Against `published`, a difference is a regression and the
version it regressed from is named in the step.

**Know which version is being started from, or that the document is empty.** A half-built document
is neither, and it hides exactly the thing an empty start exists to test.

**Nothing in the guide is touched until a step is settled.** A take stages its frames and
publishes them at the verdict, so the frames the guide already holds survive a take that dies
halfway through.

**Know how the reference built this tab, from the record and not from memory.** A draft that names
a parent for its construction reads that parent's record before the first step, and a take with no
record to follow is not ready to run. draft9p2 was told to replay its parent's log for the click
path, found the log long and a written page to hand, and rebuilt the shoulder from the page.

## Running it

**Every step is entered by identifier, and an identifier the plan does not contain is refused.**
From the identifier come the step's frame stems and its log entries, so a step performed under a
name the plan never had produces frames nothing can resolve.

**The guards are always on.** They are the run-by-run findings turned into code, and each one
exists because a run once shipped a frame or a number that was wrong in a way nothing on the screen
showed:

- refuse to shoot through a notification banner, and refuse to shoot a moving frame;
- after every canvas pick, require the selection to have grown — a pick that silently missed
  patterned three slots instead of four;
- put every number in through the field and read it back — a bare keystroke landed in a focused box
  and a depth read back as `f`;
- read the feature list before and after, so a take that changed the model says so.

**The step reaches the recorded construction, and a step that cannot is a deviation.** Reaching
the same shape another way is the deviation this is written for: it leaves no mark on any
measurement, so it is only ever caught by the person driving noticing that the record said
something else. Where the record says a sketch is placed by picking an edge, typing the distance to
that edge is the departure, and it goes in `Step.deviate` with what the record said.

**A step ends on the tab it started on.** The before-and-after read of the feature list is what
says whether a step changed the model, and every tab has its own list, so a step that wanders to
the Variable Studio and finishes there reports that the part lost every feature it had. Steps that
have to visit another tab go back before they end.

**A drag is only proof of a degree of freedom if the geometry moved.** Read the canvas before and
after and fail if the pixels match, because a drag that missed its target looks exactly like a
fully defined sketch.

**These are obligations on the take, not a description of `tools/gui_steps.py`.** They hold whoever
is driving. Where one can be code it belongs in the harness, and the harness is the only place a
guard stops depending on somebody remembering it.

## When a step does not work as written

**Record what was expected and what happened, deviate as little as needed, and change the plan —
not the caption.** Then drop the step's `state`, because a step that had to be deviated from is no
longer proven.

Run 8p1 is the worked example. The plan called for a selection box over the origin and a sketch
pattern's center, on the reasoning that two points on the same pixel cannot be separated by a click
and a shift-click. The box selects one of them. What works is dragging the pattern away from the
origin first, which is the step that teaches the degree of freedom anyway. The plan changed; the
page describes the drag; the register records that the box-select was tried and what it did. See
[`run8p1/register.md`](../experiments/runs/2026-08-19-run8p1/register.md).

**A step that fails and is quietly worked around is the failure this whole structure exists to
prevent.** The geometry was right in that run either way — only the intent was wrong — and nothing
on the screen would have caught it.

## Only a finding that stops the geometry existing blocks the next step

A number that moved, a feature that cannot be built, a face that comes out square where the plan
says round: let one of those through and it is embedded in everything built afterwards.

A finding that means the joint will not *work* — the detent will not click, the socket will not
retain, a wall is too thin to survive a print — blocks nothing. The part still models, still mates,
still assembles; only the printed plastic cares. Carry it forward and mark it not print-ready.

Mike's framing, 2026-08-12: *"push forward with imperfect joints, because you can make all of the
body parts, you can even mate them, the broken joints just won't work in the physical 3d printed
world."*

## When to stop and ask

- **A step fails twice for different reasons.** Once is a defect in the words. Twice, in two
  places, usually means the design is wrong rather than the description of it.
- **A finding contradicts a settled decision.** Settled means decided in conversation and recorded.
  Hitting one is a reason to check the record, not to reopen it.
- **A measurement disagrees with the log and nobody can say why.** Something happened that neither
  of us understands yet.

## The log — what happened, in the draft that did it

**One file per part, at `log/<part>.jsonl` inside the draft directory, written once.** It is JSON
Lines in the order things happened, and it is the only record that survives the take. The draft
directory is what keeps it, so nothing is overwritten and no earlier version has to be recovered
from git history to be read.

**No timestamps, no durations, no counts.** Anything that differs between two takes for no reason
buries the thing that differs for a reason. The events file below is where the clock lives.

**A step record says what the step did.** The identifier and which attempt it was, the `creates`
the plan declared, the features the model actually gained read back off it, every keystroke
performed, every number measured, and the deviation if there was one.

```jsonl
{"step":"cad.parts.foot.pedestal","attempt":2,"creates":"pedestal",
 "features_added":["pedestal"],"measured":{"collar_h_mm":7.35},
 "keys":[{"key":"p","why":"hide the planes so zoom to fit frames the part"},
         {"key":"f","why":"zoom to fit, so the collar fills the window"}],
 "deviation":null,"unmet":[]}
```

**Every keystroke is recorded with the reason the reader will be given for it.** `robot-guide2`
tells the reader *"the view swings round to look straight at it"* where the build pressed **n** —
the key was invisible to whoever wrote the page because pressing it was reflexive, and the page
handed the credit to Onshape. The same gap swallowed **p**, **f** and **shift+7**, all of which
change what is on the screen and all of which are written down only in
[`onshape-gui-howto.md`](../onshape-gui-howto.md), which no student reads. Typing a value is not a
keystroke in this sense: it goes in through the field, and the field's frame is its record.

**A miss is recorded where it happens, and nowhere else can hold it.** `deviate()` takes the
requirement the step could not meet, and `Take.unmet()` takes one that no single step owns — a clip
that was never captured, a named shot the take never got to. Both land in the log.

```jsonl
{"unmet":["req.page.video"],"why":"no clip captured for this block"}
```

**The plan says what is in play, the tag says what shaped the page, and only the log says what
fell short.** [`shots.md`](shots.md) carries the `Req` column and each tutorial's *Requirements in
play*; [`steps.md`](steps.md) carries the `.. req:` tag beside the words it constrains. Neither can
know that an attempt came up short, and a requirement quietly not met reads — in every other
artifact — exactly like one that was met.

**A miss in a rehearsal is not a miss.** `read_log` counts `unmet` only from the attempt the verdict
promoted, so a requirement missed on the practice pass and met on the performance leaves no mark.

**A frame record says what the frame shows, and it is written when the frame is taken.** The stem,
the step and attempt it belongs to, its kind from [`shots.md`](shots.md), and one sentence
describing what is on the screen.

```jsonl
{"frame":"pedestal-03","step":"cad.parts.foot.pedestal","attempt":2,"kind":"field",
 "shows":"the Depth box holding #collar - #wall, before Enter"}
```

**`shows` describes the screen; it is not the caption.** The page's voice depends on the paragraphs
around the figure, and a caption drafted at the CAD gets pasted in unedited. What the Write phase
needs from the log is what the picture contains, which is the thing only the person at the CAD
knows.

**A verdict record says which attempt stands, and it is what puts frames in the guide.** A step is
often driven once to find out what it takes and again to perform it cleanly. Both passes are real
work and both are captured, into `capture/attempts/<part>/<stem>/<n>/`; only one belongs on the
page.

```jsonl
{"verdict":"cad.parts.foot.pedestal","attempt":2,"frames":9,
 "why":"attempt 1 needed p then f before the fillet edge was pickable"}
```

**The last attempt stands unless an earlier one is named.** Driving a step to learn it and again to
perform it is the ordinary shape of the work, so it costs nothing to say. Promoting the trial pass —
because it turned out to be the clean one — is the thing that has to be written down.

**`why` is the difference between the attempts, and it is usually what the page owes the reader.** A
practice pass that needed **p** and then **f** before an edge could be picked has found a step the
clean pass will otherwise perform in silence.

**`shows` is required at the moment of capture, so an unlabeled frame cannot be taken.** Guide 4's
`head.rst` was written from contact sheets of ninety-three finished images, with the meaning of each
one reconstructed by looking at it. That is the failure this field exists to end.

## The audit — checking the work without asking the builder

**An audit reads the artifact and the design source, and does not read the log.** The log is the
builder's account of what it did, and an audit handed that account agrees with it. What an audit
gets is the model, the frames, the page, and the numbers the plan declared.

**A check that reaches for the log reads the rehearsal.** draft9p3's first `audit.step` on the
torso read the last record for each step and reported `cad.parts.body.rename` as standing on a
deviation. The rename had worked on the first pass; the deviation belonged to two later passes that
found the tab already renamed and stopped, and the verdict had already promoted the first. The log
is the builder's account, `gui_steps.read_log` is what resolves an account to the attempt that
stands, and neither is an input to an audit.

**Where a check can be a script it is a script**, because a script has no memory of the build.
Where it cannot, the separation comes from somewhere else — a session that did not watch the build,
or a reviewer handed the account afterwards and asked whether the page was followed or the build was
remembered. Which of the two a draft can afford is its own judgment, and its `plan.md` says which
it used.

**A page is followed to a part, and the part is measured.** Reading a page and finding it well
written is a different activity that produces a different answer. What this one returns is the diff
between the part that came out and the reference model, and the step where the words ran out — which
names a step boundary the page owes a sentence to.

**An audit writes one `audit` record per identifier it covers**, into the same `log/<part>.jsonl`
the step and frame records go to.

```jsonl
{"audit":"cad.parts.foot.pedestal","kind":"step",
 "attacked":["creates against the feature list read back","every frame against its shows",
             "under-defined sketch geometry with the dialog closed"],
 "found":[{"what":"collar_h_mm reads 7.35 where the plan declares 7.30","severity":"carried"}]}
```

**A finding is `blocking` or `carried`, and § *Only a finding that stops the geometry existing
blocks the next step* is the test.** `blocking` stops the next step, because everything built after
it is built over it. `carried` is a joint that will not click or a wall too thin to survive a print:
the part still models, still mates, still assembles, and only the printed plastic cares.

**`attacked` is what makes an empty `found` mean anything.** Without it the record says only that
somebody looked, and a check nobody can see the shape of is a check nobody can improve. Which audits
a draft runs, against which inputs, is declared in that draft's `plan.md`.

**A finding stands until the register answers it by name.** A builder who disagrees withdraws it
there, with the measurement that withdraws it. Silence closes nothing, and a finding carried
forward is carried by name rather than by being forgotten.

## The events — how a take in progress gets debugged

**Every click, every wait, every retry, with the clock.** They go under the draft's `capture/`,
beside the footage they are timed against, because a take runs for an hour and crosses session
boundaries that a scratchpad does not survive. `onshape_record.py` renders the video from this
stream, so discarding it discards any second cut.

**The events are also the only independent check on the log.** The log says what the harness
believed it did; the events say what the browser saw. Keep only the log and a defect in the
log-writer is undetectable.

## The comparison is against the parent draft

**Compare on the way past, while the take is fresh and somebody is watching.** Keeping every log
and comparing later defers it to a reader who has to go looking.

**Join the two logs on the step identifier.** They are not line-comparable — a draft whose plan
changed has steps the parent never had — so the comparison is: steps in one and not the other, and
for steps in both, which measurements moved. It reads the plan's `was` and `superseded_by`, because
a renamed identifier breaks the key.

**Across a changed plan, only the model-side numbers stay comparable** — features and their order,
measurements, bounding box, volume, face counts. A step-by-step difference means something only
where the steps were meant to be the same.

**The comparison reports what moved and stops there.** Whether a difference is the fix that was
intended or a regression nobody asked for is the register's judgment.

## Where the frames land

**Which frames a take has to shoot is [`shots.md`](shots.md).** What follows is where they go.

**Frames go under the draft's guide, one directory per page.** The stem is the step's identifier
relative to the subtree the page declares, so `cad.parts.ball_and_socket.stud.revolve` writes
`images/ball_and_socket/stud.revolve-01.png`. The page's declared subtree is what resolves a frame
back to a full identifier, and the per-page directory is what stops two parts with the same leaf
name colliding.

**The log lives with the draft and the frames live with the guide.** The identifier is the only
thing joining them, which is why a take refuses an identifier the plan does not contain.

## Where findings go

**A rule about driving Onshape goes to the harness, as code where it can be code.** A finding about
one step goes on that step. Nothing goes into a folder named after a date — a rule filed under the
day it was found is a rule nobody reaches for on the day it matters.

## Before a take is called done

The Constitution's Quality Gates apply and are not restated here. What a take adds to them:

- every step's `creates` diffed against the feature list read back off the model, and every
  `creates: none` still `none`;
- every acceptance number measured, not recalled;
- every step downstream of a geometry change either remeasured and unchanged, or retaken —
  [`drafts.md`](drafts.md) says why;
- a named version published, and its link opened rather than assembled;
- every frame the take shot carrying a `shows` in the log, and every keystroke a `why`;
- every step in scope carrying a verdict, so no step's frames are whichever pass ran last by
  accident;
- every keystroke in the log either written into the page or deliberately left out with a reason —
  the check that catches a page which can be followed to the wrong screen;
- every frame the page names present, and no frame on disk unused;
- every figure opened and read against its own caption and alt text, below;
- every identifier in scope carrying its `audit` record, with what was attacked written down;
- Sphinx building the guide with no warning.

## Every figure is read back against its own caption

A caption is written beside the frame it describes, with the frame on screen, so the two agree at
the moment they are written. What pulls them apart is everything after: a frame retaken at a
different zoom, a step reordered, a part renamed, a number corrected in the prose and not in the
alt text. Nothing else in the cycle re-reads the pair, which is what `req.shot.caption_moment` in
[`drafts.md`](drafts.md) asks for and no gate was checking.

So a page is not done until every figure it names has been opened and read against its own caption
and its own alt text, one at a time. Three checks cost nothing:

- **Hash a page's images against each other.** Two figures with the same bytes are one picture used
  twice, and the second one shows the reader nothing. A duplicate passes every caption check,
  because the picture it is read against is a real picture — it just is not this figure's.
- **Read the frame's own feature tree, not your memory of the step.** A caption that says *before
  the connector goes on* over a frame whose tree ends in that connector is the end state standing
  in for a mid-build state. It is the cheapest frame to take and the easiest one to caption wrongly.
- **Check every count and every name the caption asserts** against what is in the frame: feature
  and instance counts, how many slits or dimples read at that zoom, the text in a dialog's filled
  field, and which way round a copy and its original are.

**A frame carries the state of the tool as well as the state of the model.** A tooltip standing
under a parked pointer, a dialog still open behind a feature that was already accepted, a highlight
left from the previous selection — every one of those is in the picture and none of them are in the
caption. Park the pointer in `gui.EMPTY` before the shutter, and read the whole frame rather than
the part the caption is about.

**A mismatch a reshoot cannot fix is fixed in the prose.** No view of a flat plate shows both its
faces, so a caption that claims both is wrong about what a picture can do, and the tree beside it
is the proof instead. The same goes the other way: what is frozen in a published version
description cannot be edited at all, so the page says the number is superseded rather than
pretending it is not there.

## What ends a take, and what ends a draft

A take ends when every step in its scope is published against a named version and the frames are on
disk. A draft ends when its register is written — [`drafts.md`](drafts.md).

Neither answers whether the written steps get a student from an empty document to the part. That is
a take `from: empty` over the whole plan, and it is a different question from whether the model is
right.

## What this supersedes

[`build-and-verify.md`](../experiments/build-and-verify.md) is the procedure this replaces. Its
machinery is waves of subagents building parts from briefs, gated by a launcher with a watchdog,
and CAD is no longer handed to a subagent. The half of it that is alive — the geometry-blocking
rule, the stop-and-ask conditions, and what ends the cycle — is above. What is left there is
history.

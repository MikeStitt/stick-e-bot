# The shots — which ones the plan names, and which ones it does not

A **shot** is one frame a guide page can point at. This file says which shots the plan has to
name ahead of time, which ones the harness produces without being told, and which ones we do not
know yet and will decide at the CAD.

**The obligations this file carries a mechanism for are named in**
**[`drafts.md`](drafts.md) § *The requirements*.**

What a step is, is [`steps.md`](steps.md). How a frame is named and where it lands is
[`takes.md`](takes.md) — the stem is the step's identifier, so
`cad.parts.ball_and_socket.stud.revolve` writes `images/ball_and_socket/stud.revolve-01.png`.

## Which requirement a shot answers to

**All of `req.shot.*` applies to every tutorial's shots** — the toolbar close-up, the two frames on
a pick, the hidden planes, the caption at the same moment, the true state. Those are in
[`drafts.md`](drafts.md) § *The requirements* and a plan file does not restate them.

**A plan file names a requirement only where it is extra or at risk here.** Each tutorial's shots
table carries a `Req` column, and a row fills it when the shot exists *because of* a requirement
rather than because a rule cannot produce it — the staged frame, the close-up of a tool this
tutorial is the first to use. A blank cell means the universal set and nothing more.

**Each plan file opens its shots section with `Requirements in play`** — the ones this tutorial has
to work at, above the universal set. That line is what the CADer reads before the take, and it is
the answer to *which requirements am I holding when I redo this*.

## The plan does not carry a shot count

**A count would be a guess, and a guess about frames adds nothing.** The published ball-and-socket
page shoots a frame per click and a frame per field, and those frames come from the step being
performed, not from anyone having listed them. Writing the list down before the run means
maintaining a number the run produces anyway.

**What the plan carries is the shots a rule cannot produce.** A frame that has to exist because
the prose points at it, a frame whose framing is a decision rather than a default, and a frame
somebody has to edit. Those are below.

## The shots the harness makes on its own

No step needs to name these.

| Shot | When |
| ---- | ---- |
| the tool being picked | every tool, as it is chosen |
| a field, filled | every value typed into a dialog |
| the feature, accepted | after every green tick |
| the part, renamed | after every rename |

**A toolbar icon is not a shot of the model and is not tied to a step.** `tb-line.png` belongs to
the Line tool, is captured once, and is reused by every page that reaches for Line. The set needed
is read off the feature types in the plan, not listed by hand.

## The shots every Part Studio needs by name

Four, and they are the same four every time.

| Shot | What it is |
| ---- | ---------- |
| the hero | the finished part or parts, at the top of the page, before any step |
| the tree | the whole feature tree with the filter box cleared, at the end |
| the version dialog | the named version being published |
| the part list | the studio's parts, named, where a studio makes more than one |

The hero is two frames where a studio makes two parts that are used apart — the ball and the
socket, the blade and the fork.

## The empty document is a shot, and only the first tutorial takes it

**A draft that starts from nothing has to show the nothing.** The reader arrives at a document
holding three planes, no features and two tabs, and the frame that tells them they are in the right
place is a picture of exactly that. Its kind is `arrived`; it belongs to the first tutorial's first
step; no later page takes one. Before draft9p2 no take started `from: empty`, so nothing needed a
word for the state every reader begins in.

## Selecting a point always takes two frames

**Every pick of a point gets a medium view and a close-up.** This is the shot rule the assembly
work turns on, and it applies to a mate connector, a vertex, an origin, and the center of a stud.

**A pick inside a Part Studio is a pick.** An edge picked to place a sketch, a face picked as a
sketch plane, a vertex picked to dimension to: each gets the same pair. The frames are what a page
can teach picking from, and a page written without them falls back on describing a number instead,
which is the construction draft9p3 exists to stop reproducing.

**The medium view answers "what am I looking at".** Enough of the robot in frame that a student
can tell which shoulder, which end of which limb, which way up. Once the assembly holds more than
two parts, that generally means the whole robot in frame, because *which* shoulder is not
answerable from a picture of one shoulder.

**The close-up answers "which dot".** Magnified until the dot to pick is distinguishable from its
neighbors. A stud carries a connector at the ball's center and the sketch points that placed it,
and at medium range those are one blob.

**The close-up carries a ring, drawn on the dot.** The medium view stays clean, so the two frames
read as *here is where we are* and then *here is the one to click*.

### The harness draws the ring, because it knows the pixel

**The ring is not a hand edit.** The harness clicks at a pixel it computed, so it can draw a ring
centered on that same pixel before it clicks. Nothing is measured twice and nothing is drawn by
eye, so the ring and the click cannot disagree — which is the failure a hand-edited frame invites,
and it is invisible in the finished picture.

Pillow is already a dependency, so this is a drawing call on a frame the harness is holding.

### Shoot medium, zoom, shoot close, then click

**The order matters, because a camera move invalidates a screen-to-model mapping.** Opening a
sketch zoom-to-fits, and so does any zoom; a pixel computed before the move lands somewhere else
after it. So the pair is captured as: shoot the medium view, zoom in, shoot the close-up, and
click **from the close-up camera** — the camera the ring's pixel was measured in.

The medium view is therefore the cheap one and the close-up is the one that has to be right.

## A gap too small to photograph

**Turn the variable up, shoot it, and turn it back.** A clearance of a few hundredths does not
read at any zoom a page can carry, and it is a variable, so the part rebuilds from it. Setting it
to a value the picture can show, taking the frame, and setting it back costs two edits and gets a
picture of what the gap *is*.

**The caption names the value each frame was shot at.** A staged picture presented as the real one
is a lie whichever way it helps, and the pair only works because the reader is told which is which.
Shot honestly, it is also a better lesson than either frame alone: the gap is a number you set, and
here is the same part at two values of it.

**Try the honest close-up first.** A gap of 0.02 is not a gap of 0.00 — it is real geometry, and
the CAD draws it as two faces rather than one at enough magnification. If it reads at all, it is
better evidence than anything staged.

**The value goes back before the version is published.** The frame is the only thing that keeps
the exaggeration.

## A cut is view state, and it stacks

**Take the planes off the section dialog before picking one.** A section plane belongs to the
view, not to the model, so it survives a page load and it survives *Turn off section view*. A
second pass that opens the dialog and picks a plane adds a second cut beside the first, and by the
third pass the part is being cut from three directions at once. What that looks like is not an
error message: it is zoom-to-fit framing a crumb, and a camera read that comes back in the
thousands of pixels per millimeter. The dialog lists what it already holds, and every row has an
×.

**The camera stands on the side the cut faces, and the dialog says which side that is.** Picking
Right in the tree keeps the half away from wherever the camera happened to be standing, so the
same pick makes *Section plane 1 (Left)* on one pass and *Section plane 1 (Right)* on the next.
The word in brackets is the side to look from. From the other side the camera is inside the half
that was taken away and sees the outside of the far half, which photographs as an ordinary uncut
part. The hatching is how the frame says the surface is a cut rather than a wall.

## What we do not know yet, and what the plan says about it

**Where the frames are not knowable ahead of the run, the step names the question and the run
answers it.** The plan records what we are trying to show. Whoever is at the CAD decides the
frames, and the step gains the frames it actually needed afterwards. This is not the last run.

**Shoot generously in these three places and cut down afterwards.** A frame we did not take costs
another run; a frame we took and did not use costs nothing.

### Copy and paste in the assembly

Nothing in guide 4 does this, so the whole operation is unknown. Open questions, all of which a
generous first pass answers:

- whether the selection is made in the graphics area or in the instance list, and whether both work
- where the pasted instances land — on the originals, or offset
- what the pasted instances are called, and whether those names are usable
- whether the carried-over mates appear in the mate list as new features or as nothing at all
- what the instance list looks like before and after

**Shoot the tree, the instance list, and the graphics area both before and after the paste.** The
lesson is that a copied set of mated parts arrives already mated, and the evidence for that claim
is a before-and-after of the mate list, which is exactly the frame nobody thinks to take.

### Placing a mate

The picks are covered by the two-frame rule above. What is not known is the dialog:

- what it shows between the first pick and the second
- whether the first pick has to be the part that moves
- what the preview does when the second pick lands
- what a wrong pick looks like, which is worth one deliberate frame if it is cheap

**Shoot the dialog after each pick, not only when it is accepted.**

### Manipulating a joint

The lesson plan wants a tutorial or two on this in the leg section and does not say what they
contain. Dragging a mated part, reading the degrees of freedom, and whatever limits look like are
all unseen. This one is not "shoot generously" — it is a question to answer before it can be
planned at all.

## What ends a shot list

A step's shots are settled when the page that uses them is written and every frame it names is on
disk and used. Until then a step's shot list is a working note, and the run is allowed to change
it.

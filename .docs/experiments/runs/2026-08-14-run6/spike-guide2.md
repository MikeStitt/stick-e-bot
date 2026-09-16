# Spike — `robot-guide2`, and what writing it taught

Written after phase 3, before phase 4, on a human hold. The draft is
[`instructions/robot-guide2/`](../../../../instructions/robot-guide2/): a Sphinx page in the same
shape as `robot-guide`, covering **Before you start**, **The plan**, **How to work**, **The ball
and socket** and **The hinge**, built from run 6's own step logs and eight of its own shots.

It built clean, and check-spell and check-level were green on it — no paragraph above grade 8.

The point of spiking it now was to find out whether the *way* the parts get built makes them hard
to write down, while there are still six parts left to build.

## It does. Five things.

### The hinge narrative crosses between the two halves five times

The build order was: blade slab → blade limb → fork limb → fork's round end → fork's slot →
fork's stubs → blade's pockets → blade's slit → fork's teeth → blade's dimples. Written out, that
is five hand-offs between the two parts, and each one costs the reader a hide, a show, and a
re-orientation. Two of the crossings are forced — the blade has to exist before a slot can be cut
to fit it — but the last four are not. The stubs, pockets, slit, teeth and dimples are all driven
by numbers (2.0, 2.2, 0.8, 4.8), not by picking each other's geometry, so they can be done in any
order.

**Adjustment:** build in whole halves wherever the geometry allows, and say in the page which
crossings are unavoidable and why.

### Two Removes needed their direction flipped, and the page has to admit it

`Extrude 7` (the blade's pin pocket) and `Extrude 10` (the dimple) both used a **starting offset**
and both first ran the wrong way, burying a sealed void inside the blade. The volume removed is
identical either way, so nothing but a face count catches it. The draft therefore carries two
steps that read *"do this, then check it did not do the opposite"*, which is the weakest writing
on the page.

The starting-offset convention is not the same between Add and Remove — an Add with offset 2.2
travelled −Y, a Remove with offset 2.05 travelled +Y from the same sketch on the same plane.

**Adjustment:** stop using starting offsets on Removes. Sketch on the face being cut, or use
**Up to face**. Then there is no offset to get backwards and the instruction is one line with no
hedge.

### The revolve profile had to be re-opened to add a line

Sketch 1 was drawn as a circle and a rectangle, committed, and then re-opened to draw the axis
line that splits the circle — because a revolve needs regions on one side of its axis, which is
not obvious until the revolve refuses. In the draft that is three steps (commit, re-open, commit)
where it should be one.

**Adjustment:** draw the whole profile, split line included, before the first ✓. Generally: a
sketch is finished when the *next feature* can consume it, not when it looks like the shape.

### The habits section is the most valuable part of the page and has no pictures

Eight images, all of geometry. The **How to work** section — merge scope, view cube, field chips,
New/Add/Remove — carries the warnings that actually cost run 6 time, and illustrates none of them.
Run 6's shots are of finished features because that is what gets captured after a step succeeds.

**Adjustment for phase 4:** take a shot per *habit*, not only per step — the Extrude dialog with
the merge scope named, the underlined New/Add/Remove, a field with its chip in it, the view cube
after **n**. These are cheap: they are the dialog as it already stands before the click.

### Four of the habits are one habit

*Look at the view cube*, *read the dimension label back*, *read the field back*, *check which of
New / Add / Remove is underlined* are four costumes on **confirm what the software took, before
you accept**. Written as four they read as a list to skim; written as one with four instances they
are a thing a person can remember.

**Adjustment:** try the consolidation in phase 8 and see whether it survives contact with the
steps. Keep them separate if the merged version stops being actionable at the point of use.

## What worked, and stays

- **Joints first, then the parts that hang off them.** The two joints are the only geometry the
  robot repeats. A student who has built both has built the hard part, and everything after is
  insertion. This is a better opening than `robot-guide`'s torso.
- **Named headings, no numbers.** Nothing to renumber when a section moves.
- **Positive framing.** Every warning states the habit and *then* what it costs — *look at the
  view cube after you press n*, not *do not press n twice*. A rule without its reason gets
  dropped.
- **The design notes that answer "why this number".** 10.909 is a Ø12 cylinder's width at 2.5 off
  center; 5.6 is 5.0 plus 0.3 a side; the four slits start 2.5 out so they do not cut the collar's
  floor into pieces. These are the paragraphs worth keeping when the page is cut down.
- **Saying plainly what has not been proved.** Nobody has followed the page, nobody has printed
  the parts, and the 0.053 mm lands between dimples are below what a 0.4 mm nozzle can lay down.

## What the draft still does not have

The six parts, the assembly, and the split into sessions — so no floor, no ceiling, and no clock.
Those come from phases 4 through 7 and are marked in the page as not yet written.

## The redraft, from run 6.1's captures

The first draft above is superseded. The page was rewritten from the run 6.1 rebuild —
[`instructions/robot-guide2/`](../../../../instructions/robot-guide2/), now `index.rst` plus
`ball-and-socket.rst` and `hinge.rst`. It carries 204 figures: 198 frames taken while the step was
performed, four renders of the finished halves, and the two plan sheets. It builds clean,
check-spell is green, and check-level lists two of its paragraphs above grade 8, both at 8.3.

### The frame names are the captions

Every capture was named with the step description at the moment it was taken, so writing the page
was choosing frames and turning their names into sentences. 198 of the run's 914 joint captures
went on the page, and nothing had to be re-shot. This is the single largest difference from the
first draft, which had eight shots and a lot of prose standing in for them.

### The four habits merge into one, and it stayed actionable

Phase 8 was to try consolidating *look at the view cube*, *read the dimension back*, *read the
field back* and *check New / Add / Remove*. The redraft merged them into **read the dialog back
before you tick it**, naming the four things to run your eye over, and then every filled-dialog
step reads its own dialog back in those words — *Remove, one face, Through all, Symmetric*. It is
shorter than four habits and it fires at the point of use. Phase 8 confirms it against the six
parts rather than re-deciding it.

### Advice-only holds when the correction lives somewhere else

Run 6.1 corrected itself once in the ball and socket: the collar's two depths and the slits' two
depths run opposite ways round. The page carries the two numbers that produce the right part, and
`build-notes.md` carries why they differ. Nothing on the page hedges, and nothing about the
failure had to be smuggled in as a clause.

### A redone step's best frame can have the model hidden

`bs-192` is the only frame showing the slit extrude with its correct depths, and it was taken with
the parts hidden, so it teaches the dialog and not the result. **Adjustment for phase 4:** when a
step is redone, take the filled-dialog frame again with the model on screen.

### Two of the sequences were captured twice, and only one attempt is the clean path

The ball and socket's slit pattern and the blade's first extrude were each built, put aside, and
built again. The frames for the path the page teaches are the second attempt's; the first
attempt's frames sit in the same numbering right beside them. Choosing a frame means checking
which attempt it came from.

### A picture at every click makes a long page

58 figures for the ball and socket, 144 for the hinge, 23 MB of PNGs. The standard is right and
the page is worth it, but the hinge is two parts on one page. **Adjustment for phase 8:** one page
per part — split the hinge into the fork and the blade, and expect the same for the torso.

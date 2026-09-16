# Run 6, phase 0 — what a Boolean Union does to a mate connector

Phase 0 of [`plan.md`](plan.md). [`design-note.md`](design-note.md) names this the load-bearing
unknown of the joint rework: if a union drops the incoming half's connectors, then building a joint
once covers the geometry and not the part that matters most.

It was built and measured through the GUI, because `/features` was returning 429 account-wide, on a
brand-new empty document as well as on the torso.

Document `run6-spike-boolean` — did `9703072fb7d3e1e38b7360cb`, wid `e053028695616470588bf10e`,
Part Studio eid `972f49f485537c33b3fbf3b7`. Steps and frames in [`shots/`](shots/), log in
[`shots/spike.log`](shots/spike.log).

## What was built

Two overlapping blocks in one Part Studio. `Sketch 1` on the Top plane, two center point rectangles
that overlap; `Extrude 1` took one rectangle's regions as **Part 1**; `Transform 1` translated a
copy along X to make **Part 2**, so the two solids share a volume. Then one mate connector on each
block's top face.

The document opened in inches and was left that way. Nothing here turns on units.

**The dialog fills the owner in by itself.** Picking a face sets **Origin entity** to that face,
leaves **Owner entity** ticked, and fills **Select owner entity** with the part the face belongs
to — `Part 1` for the first, `Part 2` for the second, neither typed
([`shots/spike-1-owner-entity-fills-itself-in.png`](shots/spike-1-owner-entity-fills-itself-in.png)).
Ownership is not something a student has to know to set. It is something they have to know to
*check*.

Mate connector has a keyboard shortcut, **ctrl m**, printed next to it in the tool search.

## The answer

**Boolean → Union, Tools `Part 1` then `Part 2`.** One part out, named `Part 1`. In the Part Studio
both connector features stayed in the tree, neither errored, and **both triads still drew on the
merged solid**
([`shots/spike-3-after-the-union-both-triads-still-draw.png`](shots/spike-3-after-the-union-both-triads-still-draw.png)).

Inserted into an assembly, the instance carried **`Mate connector 1` only**
([`shots/spike-4-assembly-carries-mate-connector-1-only.png`](shots/spike-4-assembly-carries-mate-connector-1-only.png)).

**Reversed — Tools `Part 2` then `Part 1`.** A freshly inserted instance carried **`Mate connector 2`
only**
([`shots/spike-7-fresh-instance-carries-mate-connector-2-only.png`](shots/spike-7-fresh-instance-carries-mate-connector-2-only.png)).

So the behavior is symmetric, and it is the ordering that decides it:

**A Boolean Union keeps the mate connectors owned by the part listed first in Tools. Every other
tool's connectors are dropped.**

### The dropped connector does not look dropped

Nothing upstream says it is gone. The feature is in the tree, it has no error badge, and its triad
still draws on the merged part. The only place the loss shows is an assembly instance. A check that
reads the Part Studio — by eye or by feature list — reports a connector that no assembly can use.

That is the same shape of trap as the torso's `Shoulder R` and `Shoulder L`, which read as usable
while being stale. Both fail the acceptance check
[`torso.md`](../../build-briefs/torso.md) now carries: open each connector and report how it got
there, not just where it is.

## The second finding

**Reordering Tools on a committed Boolean breaks every assembly instance of the result.** After
dragging `Part 2` above `Part 1` in the Tools list, the existing instance went red with

> Part 1 &lt;1&gt; has error: Failed to resolve instance.

([`shots/spike-6-reorder-broke-the-instance.png`](shots/spike-6-reorder-broke-the-instance.png))

The Part Studio still showed one part called `Part 1` — the name was reused, and the part under it
was not the one the assembly had a reference to. The surviving part's identity follows the first
tool; the name does not follow the identity. Editing a Boolean's tool order is therefore not a
cosmetic change, and a rebuilt part that measures identically can still break the assembly above it.

## What this decides for the joint rework

The `Derive → Transform → Boolean Union` route in [`design-note.md`](design-note.md) works, with one
rule added: **the host is listed first in Tools**, so the host keeps its own connectors.

And the consequence the spike existed to find: **building a joint once does not carry its
connectors.** A half that arrives with a ball's connector on it loses that connector the moment it
merges into a host that was listed first. The connector has to be re-made on the host, against the
merged geometry, once per joint per part.

That does not undo the rework — the geometry, the detents and the handedness are still drawn once,
and those are what get drawn wrong when they are drawn six times. It does mean the shoulder-connector
question in [`design-note.md`](design-note.md) has its answer narrowed: the shoulders cannot get
their connectors by riding in on a derived half, so they get them the same way every other joint
does, placed on the ball face after the union.

## Not measured here

- **Whether `Keep tools` changes any of it.** The checkbox was left unticked in both runs. With the
  tools kept as separate parts, the consumed part still exists, so its connectors may well survive —
  untested, and it would produce a part count the torso brief's first acceptance check would fail.
- **Whether Derive carries connectors in.** The research says it does and Transform does not; this
  spike started from parts already in the document and used neither.
- **What Subtract and Intersect do.** Only Union was run.
- **Whether a connector with no owner survives.** `Owner entity` was left ticked both times.
  [`design-note.md`](design-note.md) already rules ownerless connectors out as a way around this,
  because an assembly cannot see them either.

# draft9p1p5 build notes

What the build actually did, tab by tab, including where it departed from
[`plan.md`](plan.md). Ids are read off Onshape, not transcribed.

## Where the work is

| What | Id |
| ---- | -- |
| document `stickbot-draft9p1p5` | `e5bdf1e586fb6c868066df22` |
| workspace | `e051660ad432c2cfabda245b` |

The live workspace is
<https://cad.onshape.com/documents/e5bdf1e586fb6c868066df22/w/e051660ad432c2cfabda245b>.

| Tab | Element | Type |
| --- | ------- | ---- |
| `robot sizes` | `488fdaefc4a17161539cd730` | Variable Studio |
| `ball and socket` | `f4b91f8171bbdb4a1f2887e2` | Part Studio |
| `hinge` | `fabf61fe1595cea004e698fc` | Part Studio |
| `u limb` | `be352936e6f596171a1a6b56` | Part Studio |
| `l limb` | `09f2d53343884f37576b8cda` | Part Studio |
| `ball with cylinder` | `4154b7a2226e8d0fa60f7ea4` | Part Studio |
| `socket with cylinder` | `02f1a0ea965ace742efad3a8` | Part Studio |

## C1 — the copy is of a named version, by a workspace route

`plan.md` asks for the copy to be taken from draft9p1p4's named version. Onshape has no
version-copy route; its whole route list, read from `GET /api/openapi`, holds three copy routes and
none of them takes a version. So the build copied the workspace, after first proving the workspace
and the version are the same bytes: `stickbot-draft9p1p4`'s workspace microversion and the
microversion of its version `C1 done - Phase C proved` (`be669c9b52ba1f351a4c0e79`) are both
`824b77837e057adce586b08b`. A copy of the one is a copy of the other.

`POST /api/documents/d/eca1f9c7feff156a3303d563/workspaces/3a7d66574eb06d933f843fae/copy`
answered 200 with the document and workspace ids above.

The copy is not a rename of draft9p1p4. `stickbot-draft9p1p4` is untouched and stays the recovery
point until draft9p1p5 publishes one of its own.

## C2 — which references leave the document

None, which is the defect C2 exists to find. Three independent reads agree:

- `GET /documents/d/{did}/w/{wid}/externalreferences` returns an empty list for all seven elements,
  under both `elementExternalReferences` and `elementRevisionReferences`.
- Every feature of all six Part Studios was fetched and its JSON searched for the 24-character id of
  `stickbot-draft9p1p1`, `-9p1p2`, `-9p1p3` and `-9p1p4`. Fourteen features in `ball and socket`,
  nine in `u limb`, forty-three in `hinge`, nine in `l limb`, three each in `ball with cylinder` and
  `socket with cylinder`. No hit.
- Nothing in the copy names `eca1f9c7feff156a3303d563` at all.

A workspace copy re-points every derive and every mate connector as it goes, which is why the
element ids above are all new and none of draft9p1p4's survive.

## D1 — `robot sizes` gains three rows and `#gap` changes meaning

Twenty-three rows now, in the order
[`../../../robot-build-plan.md`](../../../robot-build-plan.md) lists them. Nothing was removed.

| Row | Was | Is | Why |
| --- | --- | -- | --- |
| `#t_print` | not a row | `0.10 mm` | the printer's error per surface, which `#wedge_c` and `#wedge_w` are both checked against |
| `#wedge_h` | not a row | `0.75 mm` | how far a wedge stands proud of its own face |
| `#wedge_c` | not a row | `0.25 mm` | the air over a wedge tip at a detent |
| `#gap` | `0.15 mm` | `#wedge_h + #wedge_c` | it stopped being a fit and became a space; the two faces no longer touch |

`#seat` follows to 12.00, `#flat` to 10.3923 and `#ear` to 6.00, all without being touched, which is
the whole point of their being expressions.

**Every tab regenerated clean under the change.** All six Part Studios were read back through
`GET .../features` and not one of the ninety-six features across them reports a status other than
`OK`. A change of that size landing without a broken feature is worth stating rather than assuming.

**The table's row order is set by right-click → Move up, one step at a time.** There is no
insert-above, so a new row is typed into the placeholder at the bottom and then walked up. Past
twenty-two rows the placeholder falls under the *Insert into all Part Studios and Assemblies* bar
and a click at its un-scrolled position lands on that button instead, so the row has to be scrolled
into view first. The bar's checkbox was read back after the stray click and is still on.

## D2, first half — the hinge's own variables

Ten added, one changed, two repointed, one deleted. Every one reports `OK`.

| Variable | What it is now |
| -------- | -------------- |
| `#leaf_root` | `4.20 mm`, typed |
| `#leaf_tip` | `1.50 mm`, typed |
| `#slit_h` | `#blade - 2 * #leaf_root`, which is 1.60; it was a typed `4 mm` |
| `#stub_proud` | `2 * #wedge_h + 0.60 mm`, which is 2.10; it was a typed `1.30 mm` |
| `#wedges` | `12`, typed |
| `#ring_in` | `6.00 mm`, typed |
| `#ring_out` | `#flat - 0.4 mm` → 9.9923 |
| `#wedge_bind` | `#ring_out - #gap / 2` → 9.4923 |
| `#wedge_inset` | `2 * asin(#gap / 2 / #wedge_bind)` → 6.039° |
| `#wedge_eps` | `2 * #t_print / #wedge_bind * 1 rad` → 1.207° |
| `#wedge_w` | `180 deg / #wedges + #wedge_inset - #wedge_eps` → **19.832°** |
| `#backlash` | `2 * #wedge_eps` → **2.414°** |

`#leaf` is gone. It was `(#blade - #slit_h) / 2` and nothing read it; the leaf is now driven from
its own two ends rather than from the slit between them, so the arrow runs the other way.

**The model computes the wedge width rather than being told it.** `#wedge_w` and `#backlash` come
out of the same four-step chain the design source uses, so a change to `#gap`, `#t_print` or
`#wedges` moves them without anyone retyping a number.

**`#wedge_eps` needs `* 1 rad` to typecheck.** It is an arc length over a radius, which Onshape
evaluates as a plain number; multiplying by `1 rad` is what makes it an angle. The design source
writes the same step as `degrees(...)`.

### Two things the GUI cannot do to a Variable feature

- **It has no Rename.** Its context menu offers Edit, Suppress, Roll and Delete and nothing else,
  and its dialog title is not an edit box either: clicking the title focuses the *Value* field.
  Read back over REST, a GUI-made variable carries the literal name `###name = #value`, which
  Onshape renders from the contents. The six older variables in this tab read as bare names because
  draft9p1p4 built them over REST under an override that does not carry here. **So the tab now
  mixes two naming conventions, and closing that needs a REST grant.** It is cosmetic; no geometry
  depends on it. This also answers task #169 for this feature type: the pages tell the reader to
  rename by clicking the dialog title, and for a Variable that does not work.
- **It cannot be inserted above an existing feature except by rolling back.** Right-click →
  *Roll to here* puts the bar after the row you clicked, and features then land at the bar.
  Reordering afterwards is a tree drag, and a drag needs both rows on screen **at the same time**:
  scrolling to find the target and then scrolling again to find the source leaves the first
  position stale, which dropped `#leaf_root` six rows below where it was aimed on the first try.

## D2, second half — the hinge's geometry

The tab is fifty features and two parts, `blade` and `fork`. Read back over
`GET .../bodydetails`, the joint measures:

| What | Where it reads | What the brief asks |
| ---- | -------------- | ------------------- |
| tongue faces | `y ±5.0000 mm` | `#blade` 10.00 mm |
| ear inner faces | `y ±6.0000 mm` | `#seat` 12.00 mm, so 1.00 mm of air per side |
| blade wedge tops | `y ±5.7500 mm`, 12 faces, 37.85 mm² | `#wedge_h` 0.75 mm proud |
| ear wedge tops | `y ±5.2500 mm`, 12 faces, 37.85 mm² | the same ring, mirrored |
| axle ends | `y ±7.1000 mm`, 12.57 mm² | `#stub_proud` 2.10 mm, Ø4.0 mm |
| across the flats | `20.7846 mm` on both parts | `#flat` 10.3923 mm off the axis |

**The six dead variables are gone**: `#teeth`, `#valley_d`, `#tooth_flat`, `#cone_d`,
`#tooth_proud` and `#bump_r`. Every surviving variable was read back first and none of them named
one of the six. `#valley_deep` never existed in this tab. Features went 56 to 50 with no red rows.

**The leaves taper because the slit does.** `relief slit outline` was a parallel-sided 1.60 mm
rectangle and is now a symmetric trapezoid, fully defined, with no typed coordinate in it: bottom
edge at `#tab_free` below the origin at half-width `#slit_h / 2`, top edge at `#nose + 1 mm` at
half-width

```
#slit_h / 2 + (#nose + 1 mm + #tab_free) / (#nose + #tab_free) * (#blade / 2 - #leaf_tip - #slit_h / 2)
```

which is 3.58437 mm. The taper is set at the sketch's two ends, so at the round end the slit opens
to exactly 7.00 mm and the leaf tip is 1.50 mm, and at the root the slit is 1.60 mm and the leaf is
4.20 mm.

A sketch's origin axes are not pickable, so centering the trapezoid needs a construction line drawn
from the origin and given a vertical constraint. Snapping its far end onto a line adds a *midpoint*
constraint, which is two constraints, not one; pairing that with two half-width dimensions
over-constrains the sketch and Onshape answers **Sketch could not be solved**. One half-width
dimension is the right number.

## The ear wedges were drafted the wrong way

Both rings are extrudes with a 45° draft so they print without support on their flanks. The blade's
ring was right and the fork's was inverted: it widened as it rose instead of narrowing.

The face census is what caught it, not a dimension. Per ear the fork read **one** raised face of
270.40 mm² where the blade read **twelve** of 37.85 mm² total, and 13 cones per side where the blade
had 24. Reading the cone surfaces settled the direction:

- **Blade, correct.** Outer flank `9.9923 mm` at the tongue face narrowing to `9.2423 mm` at the
  wedge top; inner flank `6.00 mm` growing to `6.75 mm`. The wedge is widest where it meets the
  face.
- **Fork, wrong.** Outer flank `9.9923 mm` at the ear face *widening* to `10.7423 mm` at the top;
  inner flank `6.00 mm` shrinking to `5.25 mm`. The wedge is widest at its top.

Three things followed from it, and all three are the kind that a status of `OK` will never report:

- **The twelve wedges merged.** Flaring at 45° over 0.75 mm widens a wedge by `0.75 / r` radians on
  each side, which at `#ring_in` is 7.16° against the 5.08° of half-gap available. The tops ran
  together into one disc from the bore out to about `r 8.5 mm`, leaving only twelve short ridges at
  the rim. There were no fork teeth left for the blade's to mesh with.
- **The ring stood proud of the flat.** `#ring_out` is `#flat - 0.4 mm` precisely so the ring clears
  the flat; flaring outward put the base at `10.7423 mm`, which is `0.3481 mm` past it. Both limbs
  inherited it and `u limb` measured `21.4808 mm` across instead of `20.7846 mm`.
- **The flanks were overhangs.** A wedge that is widest at its top is the one shape the 45° was
  chosen to avoid.

The fix is the *Opposite direction* control beside the draft angle in the `ear wedge` extrude. After
it, the fork reads 12 tops per ear at 37.85 mm² and 24 cones per side, which is the blade's census
exactly, and every body measures `20.7846 mm` across the flats.

**The two rings clear each other at a detent, and the clearance is the backlash.** Over the 0.50 mm
where the rings overlap in `y`, each wedge is about 16.25° wide where the other is 9.07°, so the
pair spans 25.3° of the 30° pitch. The 4.7° left over is 2.35° per side, against the `#backlash`
`2.4144°` the design source derives. The two numbers agreeing was not arranged; it is the same
geometry read two ways.

## D3 — the limbs needed no edit of their own

Both tabs regenerate clean after the hinge change: `u limb` and `l limb` each report Features (13),
no red row, and Parts (1). Read back:

| What | `u limb` | `l limb` |
| ---- | -------- | -------- |
| across the flats | `20.7846 mm` | `20.7846 mm` |
| across the round | `24.0000 mm` | `24.0000 mm` |
| along the limb | `62.2205 mm` | `66.0000 mm` |
| joint center to joint center | `48.0000 mm` | `48.0000 mm` |

The limb lengths differ because the ends differ, not because the stations do: `u limb` runs from a
socket mouth standing `#grip` 2.2205 mm above its ball center to a fork axis, and `l limb` from a
blade axis to a ball tip `#ball / 2` below its center. Both carry `#limbCenter` 48.00 mm between
their two joint centers, which is what task #158 asks and what the assembly relies on.

`u limb`'s `20.7846 mm` is a result of the ear-wedge fix above. Before it the tab measured
`21.4808 mm`, and nothing in the tab was wrong.

## D4 — the two coupons stand, and a third is not this draft's to add

`ball with cylinder` and `socket with cylinder` are three features each: an `importDerived` of the
ball stud or the socket, a `cylinder section` sketch and a `cylinder` extrude. Neither reads the
hinge. They exercise the ball and socket's press fit, which this draft does not change, so the move
from a pressed hinge to a pinched one leaves them correct as they are. Both regenerate clean.

**There is no coupon for the wedge ring.** Whether the crest prints as a flat is the largest thing
this draft does not know, and a ring on a disc would answer it for the cost of a tab. Adding one is
a new tab rather than a repair to an existing one, so it is left for Mike to call.

## E1 — `l limb`'s rod now starts on the face it grows from

Task #168. `limb section` sketched on the Top plane and `limb` then pushed the profile back by a
`#tab_free` starting offset to reach the blade. Two numbers described one position, and neither
carried the reason.

The sketch plane is now **Face of add blade** — the blade's root face at `z −20 mm`, the crescent
between `y −12 mm` and `y −5 mm`, picked at model (0, −8.5, −20). The profile came across without
rotating and kept both `#flat` 10.3923 mm dimensions and its `#limbD` Ø24 mm. `limb`'s starting
offset is off; its depth is still `#limbCenter - #stand - #tab_free`, opposite direction.

The derived `blade` part is hidden in this tab, so there was no face to pick until it was shown from
its row in the Parts list. Showing a derived body is a display state, not a feature, and it does not
appear in the tree.

The body reads `−10.3923, −12.0000, −54.0000` to `10.3923, 12.0000, 12.0000`, which is the box it
had before the edit to four decimal places. The shape did not move; only the construction did, which
is what the task asked.

**Two things to raise.** Clicking a group's chevron rather than its checkbox collapses the group and
leaves the setting on; done to *Starting offset* here it split the limb into two bodies at
`z −74 mm` and read as accepted. The chevron and the checkbox are about 20 px apart. And the derived
blade already carries its own full Ø24 mm arm from `z −38 mm` to `z −20 mm`, which the `limb`
extrude then builds again over the same volume. That is harmless to the solid and outside #168, but
`u limb`'s fork looks like it has the same shape, and neither was chased here.

## E2 — every part name is lower case now

`Ball stud` and `Socket body` were the only two capitalized part names in the document. Renamed from
their rows in the Parts list to `ball stud` and `socket body`. Read back over `/api/parts`, all eight
parts across the six Part Studios:

| Tab | Parts |
| --- | ----- |
| `u limb` | `u limb` |
| `l limb` | `l limb` |
| `hinge` | `blade`, `fork` |
| `ball and socket` | `ball stud`, `socket body` |
| `ball with cylinder` | `ball with cylinder` |
| `socket with cylinder` | `socket with cylinder` |

The two coupons derive these parts and still list their own part, so the derives followed the rename.
Onshape carries a derive by part id, not by name.

## F1 — `check.py`, rewritten to the wedge

`check.py` comes forward from draft9p1p4 and reads the same way: it imports `make_plans.py`, asks the
model a question a face already answers, and compares. It ends **every row agrees**, 166 rows: 13 on
`ball and socket`, 62 on `hinge`, 40 on `u limb`, 39 on `l limb` and 6 on each coupon. draft9p1p4 ran
108.

Three groups of rows are new.

**A ring is four rows a face.** How many crests, the area of one crest, how many flanks at each of
the ring's two radii, and their draft. The area is the row that ties the wedge's angular width to its
two radii, and it is not a sector: a crest's two arcs are a wedge height in from the ring's radii,
but its two straight sides are a wedge height in from the pie slice's radial sides, and a line
parallel to a radius meets every other radius at a different angle. The half angle left at radius
`r` is the slice's less `asin(#wedge_h / r)`, and the area is that swept between the arcs. It comes
to `3.1538 mm²` and the model measures `3.1538 mm²` on all four rings.

**A fifth row asks which way each flank leans.** A cone states its radius at its origin and grows
that radius along its axis, so the direction is a fact the model reports and no dimension does. This
is the row that would have caught the inverted ear ring: the part regenerated, every station read
right, and the twelve crests had merged into a disc on flanks that print as overhangs.

**The slit is read off its own plane equation.** It tapers, so its walls are no longer at one
station. Each wall is found as the only kind of plane in the part that faces across the leaves
without being square to them, and then `y` is solved at the two `z` the design source names: the
tongue's root, where the slit is `1.60 mm`, and the tongue's tip, where the leaf is `1.50 mm`.

The rows that described teeth and valleys are deleted, not repaired. `check_teeth` and
`check_valleys` are gone with the six variables they read.

**One thing the run learned from the ring rows.** A cone's origin sits on the face the ring stands
on, which is how a ring is told from the ring facing it. In the `hinge` tab both members are present
and both rings on one side of the pin have the same sign of `y`, so a filter on the sign alone counts
each ring twice. The filter is on the station.

## F2 — one sketch was not fully defined, and driving the size is what found it

The gate has two halves, and the second half found what the first half missed.

**The first half, read the way a person reads it.** Each of the seventeen sketches opened for edit,
one frame, black is solved and blue is not: three in `ball and socket`, ten in `hinge`, one in each
limb and one in each coupon. Every curve came back black, and a count of saturated blue pixels over
the same region agreed, finding between 78 and 148 of them per frame and all of them in the view
cube's z axis and the origin triad.

**That read was wrong, and the method behind it cannot be trusted.** `ear wedge outline` is
under-defined. Its free endpoint is a dot a few pixels across; the crop the triage used was the
bounding box of everything darker than the plane's outline, and at the zoom that crop lands on, one
blue dot beside a black curve does not survive the count. A pixel test can say a sketch is
under-defined. It cannot say a sketch is not.

**The second half, drive the two sizes.** `#limbD` from 18 mm to 30 mm, and `ear wedges` reported
ERROR from 25 mm up. The fork's ring came back as a single full annulus: `cone r 6.0000` and
`cone r 10.5659` at each of `y ±6.0`, and one crest of 160.49 mm² at each of `y ±5.25`, against the
159.56 mm² a full annulus from r 6.75 mm to r 9.8159 mm computes to. Rolled to just after the
`ear wedge` extrude and before the pattern, the annulus is already there, so the seed changed and
the pattern then errored trying to lay twelve coincident rings.

**The cause is one missing constraint.** The two sketches differ by exactly one. In
`blade wedge outline` all three lines carry a coincident tying the far end to the outer circle; in
`ear wedge outline` the line `DlTCtEZyBAvU` has a coincident on its start with the circle's center
and an angle of `180 deg / #wedges - #wedge_w / 2`, and nothing on its end. Its length was free and
sat wherever the solver last left it, at 10.0459 mm. `#ring_out` is `#flat - 0.4 mm`, which crosses
10.0459 mm at `#limbD` 24.013 mm. Below that the line overshoots the circle and the pie slice
closes; above it the slice never closes and the extrude takes the whole annulus. The built size is
`#limbD` 24 mm, so the model was clearing the failure by 0.0535 mm.

**The fix is that coincident, added in the GUI.** The line's end now sits at r 13.3477 mm against a
circle of r 13.3477 mm at `#limbD` 30 mm, which is the same number rather than a near miss, and the
sketch reads fully defined.

**The sweep now passes.** Forty-eight cones on each body at `#limbD` 18, 20, 22, 24, 25, 26, 27, 28
and 30 mm, and at `#torsoH` 72, 84 and 120 mm, with no errored feature at any size. Forty-eight is
twelve wedges times two crest walls times two faces; a collapsed ring reads 4.

**The model holds to `#limbD` 34 mm and no further.** At 35 mm the blade keeps every feature but
comes back with 11 wedges per face instead of 12, so one wedge is lost on each of its two faces
while the fork keeps all twelve. That is 1.46 times the built size, and the failure is quiet: no
feature reports anything. Which wedge goes, and to what, is not chased here.

**What this changes about the gate.** A sketch that looks solved and a sketch that is solved are
different claims, and only the second one matters. The test that earns the claim is driving the
design's own dimensions and requiring the face census to hold, because that is what a free length
shows up in. Reading the colors is worth doing and is not worth believing.

Three dimensions in `fork blade top cut outline` are typed rather than named: two clearances of
`2 mm` and one of `6 mm` on a cut profile. These are draft9p1p4's three, carried forward unchanged.

## F3 — no reference leaves the document

Asked again after the edits, not only at copy time, because a copy is the operation that creates
this defect and the build has touched every tab since.
`GET /documents/d/{did}/w/{wid}/externalreferences` answers 200 and:

- `elementExternalReferences` is an empty list for each of the seven elements.
- `elementRevisionReferences` is an empty list for each of the seven.
- `elementToHasWorkspaceReferences` is `false` for each of the seven.
- The one document the route names is `stickbot-draft9p1p5` itself, and the one version is this
  document's own `Start`. There are no revisions.

**The route's `documents` and `latestVersions` entries are not by themselves a failure.** A first
pass called F3 failed because it counted every non-empty key, and those two are non-empty for a
document that references nothing outside itself. The test names the document and version instead,
and passes only when both are this document's own.

## F4 — the model inspected, and two dialogs that were still open

**Two tabs were sitting in an open sketch edit.** `u limb` and `l limb` each had `limb section`
open, which rolls the tree back behind the edited feature: the `u limb` tab was showing a socket
blank with no fork on it, and the `l limb` a blade with no limb. Nothing said so except the dialog
itself. Both were closed with the red **×**, which reverts an uncommitted edit and leaves every
committed feature alone, and `check.py` was run again afterward: 166 rows, every row agrees. So
nothing uncommitted was lost, and the two tabs had been displaying a part the document does not
have.

A script that opens a tab to look at it should ask whether a dialog is open before it believes
what it sees. The test is a bare `Sketch plane` label in the page, which nothing but a sketch
dialog puts there.

**What the model looks like.** In `l limb` the blade carries twelve tapered wedges in a ring around
the stub axle, with the axle standing proud at the ring's center and the slit running up between
the leaves. In `u limb` the fork carries the matching ring on the inner face of each ear, reached
through the fork's gap, with the axle bore on the ear opposite. The wedges are pie slices with a
flat top and a sloped flank, which is the shape the brief asks for and the shape that prints
without support.

The `hinge` tab shows the two mated, and shows nothing of the ring: the joint's working faces are
inside the assembled pair. That is the correct look for a joint that closes, and it is why the
inspection is done in the limb tabs.

## F5 — the named version

`F done - Phase F proved`, id `1f07c2dd2dd2e9f71653e336`, microversion
`3dbeeb7e2749ce6f6e6aaf58`. It is the document's second version; the first is the `Start` the copy
arrived with.

Published through the GUI, because the REST override draft9p1p4 held does not carry to this
document. **The left rail's buttons carry no label of any kind** — no `aria-label`, no `title`, no
`data-automation` — so a search for a button that says *version* finds nothing. Each one's `svg`
`<use>` names its sprite, and `#svg-icon-create-version-button` is the one.

## The gate F2 should have been, and now is

Counting saturated blue pixels asks whether a sketch looks solved. Driving the design's own
dimensions and requiring the face census to hold asks whether it is. The second question is the one
`ear wedge outline` failed, and the first one never could have caught it.

So the census was taken across the whole document rather than the hinge alone: every body in all six
Part Studios, counted by surface type, at `#torsoH` 96 mm and again at 120 mm.

| Body | Faces by surface type |
| ---- | --------------------- |
| `ball and socket` / socket body | 17 plane, 1 cylinder, 1 sphere |
| `ball and socket` / ball stud | 1 plane, 1 cylinder, 1 sphere |
| `hinge` / fork | 78 plane, 6 cylinder, 48 cone |
| `hinge` / blade | 84 plane, 6 cylinder, 48 cone |
| `u limb` | 94 plane, 7 cylinder, 48 cone, 1 sphere |
| `l limb` | 84 plane, 7 cylinder, 48 cone, 1 sphere |
| `ball with cylinder` | 2 plane, 2 cylinder, 1 sphere |
| `socket with cylinder` | 18 plane, 2 cylinder, 1 sphere |

All eight are identical at both sizes, no feature reports an error in either state, and driving back
to 96 mm reproduces the first census exactly.

A count is size-invariant where a position is not, which is what makes this readable as one table
rather than two.

# Foot — run 3 build notes

Built from [`../../../build-briefs/foot.md`](../../../build-briefs/foot.md), which had never been
built from before this run.

## Where the work is

| | |
| --- | --- |
| Document name | `foot-run3` |
| Document id | `40483ab1a6a310e833b3be41` |
| Workspace id | `bee74bfd1c5780e11aac4ea9` |
| Element id (Part Studio 1) | `f0566c848741fdf66f476388` |
| Version name | `foot-run3 v1` |
| Version id | `b5dfba92b6b36d6426880d47` |

- Version link:
  <https://cad.onshape.com/documents/40483ab1a6a310e833b3be41/v/b5dfba92b6b36d6426880d47/e/f0566c848741fdf66f476388>
- Workspace link, **live**:
  <https://cad.onshape.com/documents/40483ab1a6a310e833b3be41/w/bee74bfd1c5780e11aac4ea9/e/f0566c848741fdf66f476388>

I opened both, in this browser, after publishing. The version link came back with the banner
"Versions are view only. Viewing foot-run3 v1." and the document title `foot-run3  foot-run3 v1`
(`49-b-done-version-link-opened.png`). The workspace link came back on `Main` with the modeling
toolbar live (`49-b-done-workspace-link-opened.png`). Both carried volume 4945.503099 mm³ and one
part named `Foot`.

The page stamp used for this run was `FOOT_RUN3_NVS79W`.

## The click path that worked

Coordinate clicking throughout: move, wait, click. Screenshot after every click.

### 1. Document and units

| Step | Screenshot |
| --- | --- |
| Documents page → **Create** → **Document**, name `foot-run3` | `01-a-select-create-menu.png`, `01-b-done-new-document-dialog.png` |
| Hamburger → **Workspace units**, Length = Millimeter, decimals `0.12345` | `03-b-done-workspace-units-dialog.png`, `04-b-done-units-set.png` |

### 2. Foot outline — sketch on Top

| Step | Screenshot |
| --- | --- |
| Select **Top** in the tree, **Sketch** | `05-b-done-sketch-on-top.png` |
| Calibrate mm/px with a throwaway circle, read the dimension box's pre-filled value, delete both circles | `06-x-calibration-dimension.png`, `08-b-done-sketch-empty.png` |
| Arc flyout → **Center point arc**, heel arc | `09-x-arc-flyout.png`, `09-b-done-heel-arc.png` |
| **Center point arc** again (toolbar keeps the last choice), toe arc | `10-b-done-toe-arc.png` |
| **Line** twice for the two sides | `11-b-done-outline-drawn.png`, `12-b-done-outline-closed.png` |
| Dimension (`d`): heel r8, toe r12, origin→heel centre 8, origin→toe centre 20 | `13-b-done-dim-heel-r8.png`, `13-b-done-dim-toe-r12.png`, `13-b-done-dim-heel-x8.png`, `13-b-done-dim-toe-x20.png` |
| **Symmetric** (`shift+q`) on the two side lines about the X axis | `15-b-done-symmetric.png` |
| **Tangent** (`t`) upper line ↔ heel arc, upper line ↔ toe arc | `17-b-done-tangent-upper-heel.png`, `17-b-done-tangent-upper-toe.png` |
| Sketch black (fully defined), accept | `18-b-done-outline-fully-defined.png` |

The heel is r8 centred at x = −8 and the toe is r12 centred at x = +20, so the outline spans
x −16…+32 and y −12…+12. Two explicit tangents were enough: the Symmetric constraint carried
tangency to the lower line.

### 3. Foot plate — extrude

| Step | Screenshot |
| --- | --- |
| Click the region, **Extrude** | `19-a-select-foot-region.png`, `19-a-select-extrude-dialog.png` |
| Depth 6, tick **Starting offset**, offset 12, **flip the offset's own arrow** | `19-a-select-starting-offset-ticked.png`, `20-a-select-extrude-offset-flipped.png` |
| Accept | `20-b-done-extrude-accepted.png` |

The starting offset has a flip arrow of its own, on its Depth row, separate from the main
direction arrow. Without flipping it the plate builds upward from z = +12 instead of downward
from z = −12. Bounding box after the extrude: x −16.000…+32.000, y −12.000…+12.000,
z −12.000…−6.000.

### 4. Top edge fillet

| Step | Screenshot |
| --- | --- |
| Click the plate's **top face** (Area 892.44970 mm²), Search tools → **Fillet** | `23-a-select-top-face.png`, `23-x-search-fillet.png` |
| Radius 4, accept | `23-a-select-fillet-r4.png`, `23-b-done-fillet-r4.png` |

**Answering the brief's question on step 3:** selecting the whole top face gave Onshape the entire
boundary loop — both arcs and both tangent lines — in one Fillet feature. There was no
edge-by-edge picking and no tangent-chain prompt; the face selection is the tangent chain.
Volume fell 5354.698199 → 4963.984101 mm³.

### 5. Ankle ball

| Step | Screenshot |
| --- | --- |
| **Front** plane → **Sketch**, arc r3 on the origin plus a vertical axis line | `24-b-done-sketch-on-front.png`, `25-b-done-ball-profile-defined.png` |
| Accept, click the half-disc region, **Revolve**, axis = the profile's vertical line | `26-a-select-revolve-axis.png`, `26-b-done-revolve-accepted.png` |

Revolve produced 113.097336 mm³; a Ø6 sphere is 113.097.

### 6. Socket collar

| Step | Screenshot |
| --- | --- |
| **Top** plane → **Sketch**, circle on the origin, dimension Ø9.4 | `28-b-done-collar-circle.png` |
| Accept, click the region, **Extrude**, depth **1.35**, tick **Second end position** = 6 | `29-a-select-collar-second-end.png` |
| Operation **Add**, **Merge scope** = Part 1, accept | `29-a-select-collar-merge-scope-part1.png`, `29-b-done-collar-added.png` |

Two end positions, not a blind depth: the collar has to reach from the plate's top face at z = −6
up to the mating face at z = +1.35. It added 510.073696 mm³; π·4.7²·7.35 = 510.06.

### 7. Ankle socket — Boolean subtract with offset

| Step | Screenshot |
| --- | --- |
| **Boolean**, operation **Subtract** | `30-a-select-boolean-subtract.png` |
| **Tools** = Part 2 (the ball), **Targets** = Part 1 | `30-x-boolean-tools-only-part2.png`, `30-a-select-boolean-tools-targets.png` |
| Tick **Offset**, tick **Offset all**, distance **0.2** | `30-a-select-boolean-offset-ticked.png`, `30-a-select-boolean-offset-all.png` |
| Leave **Keep tools** unticked, accept | `30-a-select-boolean-ready.png`, `30-b-done-boolean-subtract.png` |

The Ø6.4 cavity is never drawn. It is the Ø6 ball grown 0.2 by the Boolean's own Offset.

### 8. Sole rib

| Step | Screenshot |
| --- | --- |
| **Top** plane → **Sketch**, zoom out, **Center point rectangle** | `31-b-done-sketch-on-top-for-rib.png`, `32-a-select-rib-rectangle.png` |
| Dimension 3 wide, left edge's own length 26, centre 10 from the origin | `32-b-done-rib-defined.png` |
| Accept, click the region, **Extrude**, **Remove**, depth 1, **Starting offset** 12 flipped | `33-a-select-rib-remove-offset.png`, `33-a-select-rib-offset-flipped.png` |
| Reopen and flip the **main** direction arrow (see below), accept | `34-a-select-extrude3-direction-unflipped.png`, `33-b-done-rib-cut.png` |

### 9. Sole ribs — linear pattern

| Step | Screenshot |
| --- | --- |
| Search tools → **Linear pattern**; it opens as **Part pattern** | `35-a-select-linear-pattern-dialog.png` |
| Open the type dropdown and pick **Feature pattern** — both clicks in one script call | `35-x-pattern-type-menu.png`, `35-a-select-feature-pattern.png` |
| **Features to pattern** = the rib extrude | `35-a-select-features-to-pattern.png` |
| Click the **Direction** field, then click **Right** in the feature tree | `37-a-select-direction-field-active.png`, `37-b-done-direction-right-plane.png` |
| **Distance** 6 mm, **Instance count** 7, Tab to refresh the preview | `38-a-select-pattern-preview-7.png` |
| Tick **Reapply features**, accept | `39-a-select-reapply-ticked.png`, `39-b-done-sole-ribs.png` |

**Answering the brief's question on step 5 — what the pattern wants for a direction, and whether
it will take an edge.** The `directionOne` parameter's own query filter, read from
`GET /features`, accepts `LINE`, `CIRCLE`, `ARC`, `CYLINDER`, `CONE`, `REVOLVED` and `PLANE`. I
put all three kinds in the field and watched what the field said:

| Given | Field read | Direction used |
| --- | --- | --- |
| `Right` plane from the feature tree | `Right plane` | the plane's normal, +X |
| the top fillet's cylindrical face | `Face of Top edge fillet` | the cylinder's axis |
| the straight edge where that fillet meets the flat top | `Edge of Top edge fillet` | the line |

So yes, it takes an edge (`50-b-done-edge-as-direction.png`). I kept the plane, because every
straight edge on this foot runs along the outline's tangent lines, which sit 8.213° off the X
axis — an edge here would have splayed the ribs. That edit was cancelled with the dialog's red X
and the feature verified unchanged afterwards.

### 10. Renaming and the version

Right-click a feature → **Rename** is the first item on the context menu. Near the bottom of the
panel the menu opens upward (`46-x-part-context-menu-full.png`). Features are now `Foot outline`,
`Foot plate`, `Top edge fillet`, `Ankle ball profile`, `Ankle ball`, `Socket collar profile`,
`Socket collar`, `Ankle socket`, `Sole rib profile`, `Sole rib`, `Sole ribs`; the part is `Foot`
(`46-b-done-renamed-tree.png`).

Left rail, second icon down: **Create version…** (`48-a-select-create-version-dialog.png`).

## The deliberate mistake — the plan outline on the wrong plane

Clearly labelled: every screenshot below has `MISTAKE` in its filename. These features were
deleted afterwards and the model returned to 11 features and 4945.503099 mm³.

| Step | Screenshot |
| --- | --- |
| Start a sketch on **Front** instead of Top. From the Top view the sketch plane is a single line — there is nothing to draw on | `42-x-MISTAKE-sketch-started-on-front-plane.png` |
| Look normal at it, draw the outline, extrude 6 | `42-x-MISTAKE-rectangle-on-front.png`, `43-x-MISTAKE-region-selected.png` |
| **The symptom**: the plan shape stands up as a wall, 6 mm thick across the foot's width, instead of lying flat as a plate | `44-x-MISTAKE-built-on-front-plane-side-view.png`, `44-x-MISTAKE-iso-plan-outline-built-as-a-wall.png` |
| Delete both features | `45-b-done-mistake-deleted.png` |

The isometric is the picture the lesson wants: the outline is geometrically exactly what was
drawn, and it is a signboard.

## Acceptance measurements

Every number below was measured on the built model. Nothing here is inferred from the numbers
table.

| Check | Expected | Measured | How |
| --- | --- | --- | --- |
| Parts | 1 | **1**, named `Foot` | `GET /api/parts` |
| Length | 48.000 | **48.000** (x −16.000…+32.000) | `GET /boundingboxes` |
| Width | 24.000 | **24.000** (y −12.000…+12.000) | `GET /boundingboxes` |
| Ground | z = −12.000 | **−12.000**; the sole's planar faces sit at z = −12.0 | `boundingboxes`, and `evSurfaceDefinition` on every planar face |
| Ankle ball centre | the origin | cavity sphere r 3.2 centred **(0, 0, 0)** | `evSurfaceDefinition` |
| Ankle height | 12.000 | **12.000** | 0 − (−12.000) |
| Symmetric about XZ | lands on itself | **0.000000000 mm³ removed** | Mirror → Intersect about `Front`, volume before and after |
| Outline tangent, no crease | tangent | **tangent to 4 decimal places** — see below | fillet arc centres against the external tangent points |
| Socket mouth Ø | 5.803 | **5.8026**, at z = **+1.350** | circular edge, radius 2.9013 |
| Cavity volume | 109.48 mm³ | **109.482017 mm³** | Part 1 volume 5474.057797 before the Boolean, 5364.575780 after |
| Collar stands proud | 5.5 | **7.350** — see the conflict below | collar cylinder runs z −6.000 (plate top face) to z +1.350 |
| Thinnest wall | — | **1.500 mm**, the socket collar wall at the ball's equator | `evDistance` between the Ø9.4 face and the cavity sphere |
| Flat around the Ø9.4 collar | — | **0.443 mm** at its narrowest | `evDistance` between the Ø9.4 face and the top fillet faces |

Supporting volumes, all from `GET /massproperties`:

| Stage | mm³ |
| --- | --- |
| Plate, before the fillet | 5354.698199 |
| Plate, after the r4 fillet | 4963.984101 |
| Ankle ball on its own | 113.097336 |
| Part 1 before the Boolean | 5474.057797 |
| Part 1 after the Boolean | 5364.575780 |
| After the first rib | 5318.400862 |
| Final | 4945.503099 |

The 27.78 mm³ the brief warns about is the spherical cap above z = +1.35, which is what a socket
built upside down leaves behind. This one measured 109.482017, so it is the right way up.

**Ribs, cross-checked two ways.** The seven groove floors measure 46.175, 51.962, 57.158, 62.354,
67.550, 71.812 and 62.063 mm², summing to 419.074 mm² at 1 mm deep. The volume fell 419.073 mm³
from the Boolean result to the final part. The grooves grow toward the toe because the foot is
wider there, and the last one shrinks again where the toe arc curves away.

**Tangency, measured rather than eyeballed.** The r4 fillet's arc centres at the ends of its two
straight runs sit at (−8.5714, ±3.9590) and (18.8571, ±7.9179). The external tangent points of a
circle r8 at (−8, 0) and a circle r12 at (+20, 0) are (−9.1429, ±7.9179) and (18.2857, ±11.8769);
offsetting those 4 mm inward gives exactly the measured centres. Separately, the outline's area
measures 892.45 mm², and the convex hull of those two circles computes to 892.43 mm². A creased
outline would not produce either agreement, and no crease appears in any of the four renders.

## Renders

`shadedviews`, one part in the studio, so each render is the part alone:
`47-render-isometric.png`, `47-render-top.png`, `47-render-front.png`, `47-render-right.png`.

What I saw. The plate reads as a rounded sole rather than a slab — the r4 fillet on a 6 mm plate
consumes 4 of the 6, so only a 2 mm vertical band is left at the rim, and from the side the plate
looks like a bar rather than a plate with a chamfer. The socket collar is the surprise: at 7.35
proud on a 6 mm plate it stands taller than the plate is thick, and from the end-on view it reads
as a post rather than a boss. Nothing in the numbers table implied that, because the table names
5.5 and the geometry cannot deliver 5.5 — see the conflict below.

**Is a 48 mm foot on a 150 mm figure goofy in the way the brief wants, or just big?** Goofy. At
48 long it is 32% of the figure's height, against roughly 15% for a person, and at 24 wide it is
16% against roughly 6%. That is clown-boot proportion, not merely a large foot, and the heavy
fillet reinforces it. It reads as deliberate.

**Does the figure appear to be tipping forward?** No. With 16 mm behind the ankle and 32 in
front, the ankle sits a third back, which is close to where a person's ankle sits. The long toe
gives ample forward support. If anything the short heel is the weaker direction, so the risk is
sitting back, not tipping forward.

## What did not work

**The linear pattern was left in ERROR twice, and Onshape accepted OK both times.**

1. The first time, the **Direction** field was empty. `GET /features` showed
   `directionOne.queries == []`. Onshape took the OK, created the feature, and marked it ERROR
   rather than blocking the dialog. Reopening it showed the Direction field outlined red —
   the dialog says what is wrong, but only if you reopen it (`37-a-select-linear-pattern-reopened.png`).
2. With `Right plane`, 6 mm and 7 instances filled in, it still errored. The message, read off the
   tooltip: *"Linear pattern 1 did not regenerate properly: Could not create all instances as
   entered. Try selecting "Reapply features" option."* (`38-x-pattern-error-tooltip.png`).
   Ticking **Reapply features** fixed it. Without it, a feature pattern transforms the resulting
   faces; the grooves cross a curved, filleted outline that is a different shape at every station,
   so the transformed faces had nothing valid to land on. Replaying the extrude works.

**The rib cut removed nothing.** After accepting the rib extrude the volume was unchanged at
5364.575780. `GET /features` showed the Remove extrude had arrived with `oppositeDirection = True`
while the plate's extrude had `False`; combined with the flipped starting offset the cut ran from
z = −12 downward into empty air. Flipping the main direction arrow dropped the volume by
46.174918 mm³. The preview did not make this visible — only the volume did.

**Part 1 landed in the Boolean's Tools list twice.** The Tools box had grown to two rows, so a
click aimed at Targets was still inside Tools. Fixed by removing Part 1 with its `×` and clicking
Targets at its real position.

**The pattern-type dropdown is not a `<select>`.** `page.locator("select:visible")` returns
nothing and `select_option` times out after 30 s. It has to be clicked open and the row clicked,
both within one script call, because the flyout closes between invocations.

**Two sketch dimensions picked the wrong entities.** The toe radius failed with "A constraint must
involve something from the sketch" because the pick at the arc's rightmost point landed on the X
axis; picking the arc 45° off-axis worked. The rib's length dimension picked the same two vertical
edges as its width dimension and turned the sketch red; dimensioning the left edge's own length
worked.

**`n` gave the Bottom view twice** — once opening the rib sketch on Top, once opening the
deliberate-mistake sketch on Front. Pressing `n` a second time gave the right view both times.
This reproduces the how-to's warning; it is not rare.

**The Onshape session idled out** during the two and a half hours this run was paused, with the
banner "Your Onshape session has timed out. Your document is saved. Click here to reconnect."
Read-only REST kept returning 200 throughout, so only the editing session had lapsed. One click on
the banner restored it (`36-b-done-reconnected.png`). This is not a sign-out and does not need a
password.

## What the brief never said

- **How many ribs, and at what pitch.** The brief gives 3 wide × 1 deep and "linear pattern". I
  chose 6 mm pitch and 7 instances, putting grooves at x = −10, −4, 2, 8, 14, 20 and 26.
- **How long a rib is.** I used 26, one millimetre proud of the 24 mm width at each side, so the
  groove runs clear off both edges instead of ending in a step.
- **That the plate extrude needs a starting offset.** The brief gives the plate thickness and says
  the ground is at z = −12, but not that reaching it from the Top plane means a starting offset of
  12, flipped. A student following the brief literally builds the foot 12 mm in the air.
- **Whether the socket gets relief slits.** The brief's acceptance check asks for a mouth Ø5.803,
  a single circle, so I built it without slits. Slits are step 6 of `ball-and-socket.md` and would
  make the mouth four arcs.
- **Whether the ball survives.** I left **Keep tools** unticked so the ball is consumed and the
  Parts (1) check passes.
- **Feature and part names.** Supplied from `.parts/onshape.md`'s requirement that features be
  renamed.

## Three things to report and not resolve

### The plate, the collar and the grip cannot all hold at once

The brief fixes four numbers that over-determine each other:

| | |
| --- | --- |
| ankle ball centre | the origin (brief, line 39) |
| plate top face | z = −6 (brief, line 40) |
| socket collar stands proud | 5.5 (plan) |
| grip, so the mating face | z = +1.35 (`ball-and-socket.md`) |

A mating face at z = +1.35 above a plate top at z = −6 makes the collar 7.35 proud, not 5.5. Going
the other way, 5.5 proud would put the mating face at z = −0.5 — below the ball's centre, on the
wrong side of the joint entirely.

I built to every plan number plus the proposed plate 6, so the collar came out **7.35 proud** and
the mating face landed exactly on z = +1.350 as measured. I did not adjust anything to make 5.5
appear. For the record, the plate thickness that would give 5.5 proud while keeping the mating
face at +1.35 is **7.85**; I name it so nobody has to re-derive it, and I have not adopted it.

### `#footHalf` 16 against `#legX` 12

What I found when I placed the socket: the socket goes on the foot's own origin, on the
fore-and-aft centreline, 16 mm from the heel and 32 mm from the toe, with the cavity's sphere
centre measuring exactly (0, 0, 0). Building the part standalone at the origin does not decide
anything about the 4 mm, so the placement itself is neutral.

What the built geometry does say: the foot is 24 wide. A Ø12 shin whose axis sits 4 mm inboard of
the foot's centreline spans −2…+10 against the foot's −12…+12 — entirely inside the footprint,
with 10 mm of foot outboard of it and 2 mm inboard. So the mismatch is neither a collision nor a
stability problem. It is a stance decision: either the ankle ball carries a permanent 4 mm lean,
or the foot sits visibly off-centre under the shin, or one of the two numbers changes. **I have
not picked a value.**

### The briefs disagree about which axis is fore-and-aft

`README.md` says "fore-and-aft is Y". `foot.md` says to make the outline "symmetric about the X
axis — that is the fore-and-aft centerline", and the acceptance check says to mirror about XZ. I
built the length along X, following `foot.md` and the launch instruction. If the robot's
fore-and-aft really is Y, this foot needs a 90° rotation about Z when it is placed, or one of the
two documents needs correcting. Reporting, not fixing.

### And an answer the brief asked for directly

**Do the r4 top fillets leave enough flat around the Ø9.4 collar to sit on?** Barely: **0.443 mm**,
measured with `evDistance` between the collar's Ø9.4 face and the fillet faces. The flat top is the
outline offset 4 mm inward, and its nearest boundary to the collar axis is one of the tangent
lines, 5.1429 mm away; the collar radius is 4.7. It is a fifth of a millimetre wider than the
nozzle. Independent confirmation that the collar is nonetheless entirely on the flat: the flat
face measures 395.70 mm², and the offset outline computes to 465.10 mm² less the collar's
69.398 mm² footprint, which is 395.70 exactly — an overhanging collar would not subtract cleanly.

## Retrospective

**What went well.** Volume is the only honest witness in this UI, and leaning on it caught two
faults the preview hid — the rib cut that removed nothing, and the pattern that regenerated into
nothing. The symmetry check was the cheapest good thing in the run: Onshape's Mirror feature has
an **Intersect** operation built into it, so mirroring the part about `Front` with Intersect is a
one-feature test that answers the question exactly. It removed 0.000000000 mm³, and then I deleted
it. Reading feature parameters back out of `GET /features` turned two silent failures into named
ones in a single call each. And the deliberate mistake took four minutes and produced the clearest
picture in the folder.

**What went poorly.** I accepted the linear pattern twice without reading what the dialog was
telling me. The Direction field was outlined red the whole time; I had a screenshot of it and did
not look before clicking OK. That cost the run its ERROR state across the interruption. I also
spent longer than I should have on the outline's tangency, because I assumed the constraint glyphs
that appeared automatically at the junctions were tangents; they were coincidences, and I only
found out by dragging a junction point and watching it slide along the arc. Checking the
constraint list first would have been faster than probing.

**What I would change.**

- *The brief.* Fix the plate/collar/grip conflict rather than leaving three numbers that cannot
  co-exist, and say which of the four gives way. Say the plate extrude needs a starting offset of
  12, flipped — this is the single step most likely to strand a student. Give the rib count and
  pitch, or say explicitly that they are the builder's choice. And settle the fore-and-aft axis
  between `README.md` and `foot.md` before anyone builds the leg.
- *The how-to.* Its warning that a pattern's axis field silently refuses a plane is right for the
  **circular** pattern and wrong for the **linear** one: `directionOne` accepts a plane, a
  cylindrical face and a straight edge, and I used all three. Add that a feature pattern of a
  Remove extrude across a curved outline needs **Reapply features**, and that Onshape will accept
  OK on a pattern with a required field empty and leave the feature in ERROR rather than blocking.
  Add that `n` gives the Bottom view often enough to expect it — twice in this run — and that the
  fix is to press it again.
- *The briefing.* Being told to build to `proposed` numbers and report rather than adjust was the
  right instruction and made the 7.35-against-5.5 conflict a finding instead of a silent
  correction. The one thing I would add is a rule to reopen any feature that goes red and read its
  message before doing anything else. I had the tooltip text available from the first accept and
  did not fetch it until after the interruption.

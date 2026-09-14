# Build notes — the upper arm / thigh: socket on top, clevis at the bottom, on Ø12 round stock

Run 3, 2026-08-13. Brief: [`limbs.md`](../../../build-briefs/limbs.md), with
[`ball-and-socket.md`](../../../build-briefs/ball-and-socket.md) and
[`hinge.md`](../../../build-briefs/hinge.md) for the two joint portions.

## Where the work is

| | |
| --- | --- |
| Document name | `limb-socket-clevis-run3` |
| Document id | `82547630224dea5fd5a9c17a` |
| Part Studio element id | `f2a096a499d62d7664be669f` |
| Workspace id (**live, moves**) | `8f6e261ecbb5303be2f84287` |
| Version name | `run3-limb-socket-clevis` |
| Version id | `761197dc9ca32c031b02ee56` |
| Part | `Upper arm / thigh`, part id `JID` |

- Version link (fixed): <https://cad.onshape.com/documents/82547630224dea5fd5a9c17a/v/761197dc9ca32c031b02ee56/e/f2a096a499d62d7664be669f>
- Workspace link (**live**): <https://cad.onshape.com/documents/82547630224dea5fd5a9c17a/w/8f6e261ecbb5303be2f84287/e/f2a096a499d62d7664be669f>

I did not open either link in a browser tab. I assembled them from ids, and I checked the version
itself through read-only REST: `GET /api/documents/d/{d}/versions` returned
`run3-limb-socket-clevis` / `761197dc9ca32c031b02ee56`, and
`GET /api/parts/d/{d}/v/{v}/e/{e}` under that version returned one part, `Upper arm / thigh`,
volume 2084.128778 mm³, bounding box 12.000 × 12.000 × 31.160 — the same numbers as the
workspace at the moment I published.

Everything else in this directory: `steps.log` (append-only, both agents), numbered screenshots,
and five `render-upper-arm-*.png` renders of the part alone.

## What I inherited and what I did

Two agents built this part. The first was killed by an API spend limit part-way through the
socket; I took over at 03:38 and stamped my own page `LIMBSC2_RUN3_c31d7e` (their page,
`LIMBSC_RUN3_9f4a1c`, was still open; I left it alone).

**Inherited, already built when I arrived** (11 features, verified by me before touching
anything — see *Acceptance measurements*): `Limb top plane`, `Limb section`, `Limb body`,
`Collar circle`, `Socket collar`, `Ball tool profile`, `Ball tool`, `Socket cavity`,
`Slit profile`, `Relief slit`, and `Circular pattern 1` **in ERROR**. Document, workspace units,
and the part name `Upper arm / thigh` were theirs too. Volume 1817.898684 mm³, bbox
12.000 × 12.000 × 19.240, no version published — which matched the user's own read-only reading
of the document exactly.

**Mine**: the pattern repair (`Relief slits x4`), the whole clevis (`Clevis fork profile`,
`Clevis fork blank`, `Trim fork to limb`, `Clevis slot`, `Ear inner plane`, `Stub circle`,
`Stub`, `Mirror stub`), every measurement below, the renders, the published version, and this
file.

## The error the pattern was left in

`Circular pattern 1` was **ERROR**, and Onshape's own words for it, read off the tooltip on the
red tree row (`19-x-pattern-error-tooltip.png`):

> Circular pattern 1 did not regenerate properly: Select features to pattern.

Reopening it showed why: `Features to pattern` and `Axis of pattern` were both **empty**, while
`Angle` already read `360 deg`, `Instance count` `4` and `Equal spacing` ticked. The predecessor
had filled the numbers, been killed before picking the two queries, and **Onshape accepted the
feature anyway** — it committed a feature with two required query fields empty and marked it
ERROR rather than refusing to close the dialog.

That is a finding about the tool, and it is the same family as the empty-merge-scope trap run 3's
hinge hit twice: **Onshape does not block OK on a missing required selection.** The brief's step
list cannot protect against it; only reading the field text back before accepting can.

Repair: `Features to pattern` = the `Relief slit` feature (tree row), `Axis of pattern` = the
limb's outer cylindrical face (graphics pick). Volume 1817.898684 → 1793.105216, delta
**−24.793467** = exactly three more slits at the 8.264489 mm³ the first slit removed
(`21-a-select-pattern-dialog-open.png`, `22-a-select-axis-field-focused.png`,
`22-b-done-axis-picked.png`, `23-b-done-pattern-fixed.png`, `23-b-done-pattern-renamed.png`).

## The click path that worked

Steps 1–11 are the predecessor's and are in `steps.log` from 00:24 to 00:53; screenshots
`00-x` … `17-a`. Summarised: `Plane` offset 4.15 from Top flipped to −Z → `Limb top plane`;
Ø12 circle on it → `Limb section`; `Extrude` **New** 13.74 down → `Limb body` (part renamed
`Upper arm / thigh`); Ø9.4 circle on the same plane → `Collar circle`; `Extrude` **Add** 5.5 up
→ `Socket collar`; a Ø6 circle on the origin plus a closing line on the axis → `Ball tool
profile`, whose half-disc region is revolved → `Ball tool` (a Ø6 sphere, 113.097336 mm³);
`Boolean` **Subtract** with *Offset* 0.2 and *Keep tools* → `Socket cavity`; 0.8 × 3.5 rectangle
from r2.5 outward → `Slit profile`; `Extrude` **Remove** 5.5 → `Relief slit`.

From the takeover on, these are mine:

| # | What I did | Screenshots |
| - | ---------- | ----------- |
| 12 | Verified the inherited state against the user's reading before touching anything | `18-x-takeover-initial-state.png` |
| 13 | Read the pattern's error text off the red row, reopened it, filled `Features to pattern` = `Relief slit` and `Axis of pattern` = the limb's cylindrical face, accepted → `Relief slits x4` | `19-x`, `21-a`, `22-a`, `22-b`, `23-b-done-pattern-fixed.png` |
| 14 | Sketch on **Front**: circle centred (0, −24) dimensioned Ø11.62, rectangle up from it, both sides **Tangent** to the circle, bottom line **Coincident** with the circle's centre, top at z = −17.89 → `Clevis fork profile`, fully defined (black) | `24-a`, `25-a/b/c`, `26-a/b`, `27-a/b/c-done-fork-profile-defined.png` |
| 15 | `Extrude` **Add**, *Symmetric*, depth **6**, merge scope `Upper arm / thigh` → `Clevis fork blank`, **+744.132947 mm³** against a predicted 744.132947 | `28-a`, `28-b-done-fork-blank.png` |
| 16 | Showed the hidden `Limb section` sketch, `Extrude` **Intersect**, *Symmetric*, depth 60, scope `Upper arm / thigh` → `Trim fork to limb`, **−11.991055** against a predicted −11.991080; hid the sketch again | `29-a-select-limb-section-shown.png`, `29-a-select-trim-intersect.png`, `29-b-done-fork-trimmed.png` |
| 17 | The **same** `Clevis fork profile` sketch again, `Extrude` **Remove**, *Symmetric*, depth **3.6** → `Clevis slot`, **−446.144879** against a predicted −446.144872 | `30-a`, `30-b-done-clevis-slot.png` |
| 18 | `Plane` offset **1.8** from Front → `Ear inner plane` | `31-a`, `31-b` |
| 19 | Sketch on it: Ø2.0 circle, 24 from the origin along the limb axis → `Stub circle` | `32-a`, `32-b-done-stub-circle.png`, `32-x-oversconstrained-undone.png` |
| 20 | Hid the part, `Extrude` **Add** 0.8 on the stub region, merge scope filled by hand, **flipped** → `Stub`, **+2.5132741228722** against a predicted 2.5132741228718 | `33-a-select-part-hidden.png`, `33-a-select-stub-region.png`, `34-a-stub-reopened.png`, `34-b-stub-flipped-preview.png`, `34-c-done-stub.png` |
| 21 | Showed the part, hid `Ear inner plane`, `Mirror` → *Feature mirror*, features `Stub`, plane **Front**, *Reapply features* → `Mirror stub`, **+2.5132741228717** | `35-b`, `36-a`, `36-b-mirror-feature-mode.png`, `36-c-select-mirror-plane.png`, `36-d-done-mirror.png` |
| 22 | Published version `run3-limb-socket-clevis` from the left rail's second icon (`#svg-icon-create-version-button`) | `38-a`, `38-b-version-named.png`, `38-c-version-created.png` |

Final tree, 19 features, every one `OK`:
`Limb top plane` · `Limb section` · `Limb body` · `Collar circle` · `Socket collar` ·
`Ball tool profile` · `Ball tool` · `Socket cavity` · `Slit profile` · `Relief slit` ·
`Relief slits x4` · `Clevis fork profile` · `Clevis fork blank` · `Trim fork to limb` ·
`Clevis slot` · `Ear inner plane` · `Stub circle` · `Stub` · `Mirror stub`.
One part: `Upper arm / thigh`, 2084.128778 mm³.

## Acceptance measurements

Every solid feature was checked by **volume delta against a number computed independently in
Python before the click**. Every dimension below was then read off the finished part with
read-only FeatureScript (`POST .../featurescript`, `evSurfaceDefinition`, `evCurveDefinition`,
`evBox3d`, `evArea`, `evLength`) — surface and curve definitions give the true radius, centre and
plane of a face, not a tessellation. Full dump in `steps.log` at 04:31.

| Check | Wanted | Measured | How |
| ----- | ------ | -------- | --- |
| 12.000 across X and Y, whole length | 12.000 | **12.000000000000002 × 12.000000000000002**, and the same at **every 5° from 0° to 85°** | `evBox3d` with `tight`, in 18 coordinate systems rotated about Z |
| Overall height | — | 31.160 (z −29.810 … +1.350) | same |
| Segment, joint centre to joint centre | 24.000 | **24.000** | cavity sphere centre (0, 0, 0) from `evSurfaceDefinition`; stub cylinder axes are the y line through z = −24 |
| Socket mouth | Ø5.803 | **Ø5.802586** (r 2.9012928, four arcs, not one circle) | `evCurveDefinition` on the four mouth edges at z = +1.350 |
| Cavity volume | 109.48 mm³ | **109.482017 mm³** | the volume the `Socket cavity` Boolean removed: 1935.645190 → 1826.163173 (predecessor's log). Closed form for a r 3.2 sphere truncated at z = 1.35 is 109.4822 |
| Socket right way up | material below the mouth | cavity sphere runs z **−3.200 … +1.350**, centre on the origin, mouth **above** it | `evSurfaceDefinition` + face bounding box |
| Collar stands proud | 5.5 | **5.500** (four cylinder faces r 4.700000, each z −4.150 … +1.350) | face bounding boxes |
| Collar diameter | Ø9.4 | **Ø9.400000** | `evSurfaceDefinition` |
| Slits run the collar's whole length | −4.150 … +1.350 | **−4.150 … +1.350**, four of them, walls 0.800 apart | face bounding boxes of the eight slit walls |
| Rim before the slits | 1.3 all round | **1.300** (6.000 − 4.700), and the ring is **unbroken** | the shoulder face at z = −4.150 has area 50.721378 = a complete 4.7→6.0 annulus (43.699) plus four slit floors (7.022); the slits stop at the collar's outside |
| Fork span | 6.000 | **6.000** (ear outer planes at y = +3.000 and −3.000) | `evSurfaceDefinition` |
| Ears equal | equal | outer faces **114.37000488706111 mm² both**; inner faces 119.71008725891483 and 119.71008725891404 | `evArea` |
| Ear thickness | 1.2 | **1.200** | plane-to-plane, y 1.800 → 3.000 |
| Round end / blade chord | r 5.81, 11.62 | **r 5.810000, Ø11.620000**, centred on (0, ·, −24) | `evCurveDefinition` on the round-end arcs |
| Stubs | Ø2.0 × 0.8 on each ear's inner face | **Ø2.000000**, y 1.000→1.800 and −1.000→−1.800, i.e. **0.800** each, both on the hinge axis at z = −24 | `evSurfaceDefinition` on both stub cylinders |
| Ball Ø6.000 | — | **not applicable** — this limb carries the socket, not the ball stud; the ball belongs to the torso side |
| Blade 3.000 | — | **not applicable** — this limb carries the clevis; the blade is on the `limb-blade-ball` part |
| Thinnest wall | say what it is and where | **see below** |

### What the slits left, and the thinnest wall

The brief asks for the thinnest wall anywhere in the part and where it is, and asks what the
slits left of the 1.3 rim.

- **The slits left the rim alone.** They are cut entirely inside the collar: their walls run out
  to the collar's own outside surface (x 4.68295 at y 0.4, which is r 4.7) and their floors sit
  at z = −4.150, flush with the limb's top face. Looking down the limb, the 1.300 rim is a
  continuous unbroken ring (measured as face area, above).
- **What they left of the collar is four fingers**, each **6.5818 mm of arc at the Ø9.4 outside**
  and **3.7548 mm at the mouth** — measured edge lengths, and they agree with
  `4.7 × (90° − 2·asin(0.4/4.7))` and `2.9013 × (90° − 2·asin(0.4/2.9013))` to twelve digits.
- **The socket's thinnest wall is 1.500**, at the ball's equator: collar r 4.700 less cavity
  r 3.200. That is the brief's own proposed wall, and it is what the sheet
  `images/brief-socket.png` labels.
- **The clevis ear is 1.200 thick** between its two planes — thinner than the socket wall.
- **But the true minimum is zero, at the outboard edge of each ear**, and it is there on purpose.
  The ear's outer plane (y = 3.000) is clipped by the Ø12 surface at |x| = **5.196152**, while the
  ear's inner plane (y = 1.800) runs on to |x| = **5.723635** — both measured. Between those two
  the ear's outer surface *is* the Ø12 cylinder, so the ear thins from 1.200 to 0.000 over a
  0.5275 band in x. Thickness falls below 0.4 (one nozzle) for the last **0.1415** of it, which
  is **0.0294 mm² of each ear's 13.1665 mm² cross-section**; the whole taper is 0.3479 mm² of it.

That taper is not a mistake in my build: it is exactly what the brief's own sheet
`images/brief-fork.png` draws. The sheet dimensions the ear faces as **full chords** — 10.39 at
±3 and 11.45 at ±1.8 — and my measured chords are 10.392 and 11.447. The knife edge is a
consequence of the settled rule that every layer of the fork is a full slice of the Ø12 limb.
**Say it in the brief**, because "thinnest wall anywhere in the part" has the answer 0.000 and
that reads like a defect until you look at the sheet.

### The check that could not have caught a proud corner

"12.000 across X and Y" passes on this part — but an **axis-aligned** bounding box could not have
failed it either way. Before `Trim fork to limb`, the fork blank's corners sat at
(x ±5.81, y ±3.0), radius **6.539**, standing 0.539 proud of Ø12 — and because 5.81 < 6 and
3.0 < 6, the axis-aligned box still reads exactly 12.000 × 12.000. What catches it is a rotated
box (I swept 0–85°) or the trim's own volume (−11.991055 against a predicted −11.991080, so the
proud material was real and is gone). If the acceptance list stays as written, it should say
**measure it in at least two rotations**, or measure the trim.

## Four limbs, two parts — the report the brief asks for

The brief says to report on "the upper arm and the thigh are one part", not to act on it. On the
evidence of this build the claim **holds**, and I found no reason they cannot be one part:

- Nothing in the geometry is arm-specific or leg-specific. `#armSeg` = `#legSeg` = 24, the socket
  is the same joint at shoulder and hip, and the clevis is the same joint at elbow and knee.
- **The part is not handed.** Every feature is centred on the origin axes: the socket is
  four-fold symmetric about Z, the fork profile is symmetric in X, and the two stubs are a mirror
  pair about Front. So the same printed part serves left and right as well as arm and leg — four
  limbs from one part, not two.
- The clocking between the socket's slits and the hinge axis does not constrain anything: the
  joint above this part is a ball in a socket, so the limb can be twisted about its own axis to
  put the hinge wherever the pose needs it. The only thing the clocking fixes is where the
  relief slits face, and they are four-fold symmetric anyway.
- The one thing I cannot answer from geometry: **load**. A thigh carries more than an upper arm,
  and the 1.5 socket wall and 1.2 ear are the same on both. Nobody has printed or loaded either.
  If the two limbs ever diverge, that is where it will come from, not from shape.

## Do the joints fight Ø12 round stock?

This was the first time either joint has been built onto a Ø12 cylinder instead of a 20 × 20 pad.

**The socket did not fight it at all.** It is concentric with the limb, it sits entirely inside
the limb's diameter, and it left the 1.300 rim the brief predicts, unbroken. Nothing about the
round stock changed a single step of the ball-and-socket click path.

**The clevis fought it in one place, and it is the taper above.** On a square pad the ear is a
1.2 rectangle everywhere; on Ø12 it is a crescent that runs out to a sharp edge. The trim itself
was easy — one Intersect against the same `Limb section` sketch that made the limb, exactly as
the hinge brief's "full slices of the Ø12 limb" says — but the result has a feature the pad
version does not.

One more thing the round stock changed, which the brief does not mention: because the limb body
is a cylinder and the fork is 6 wide, the step at z = −17.89 is not a simple shoulder — it is two
crescent-shaped ledges (22.111 mm² each, measured) plus the slot ceiling (42.543 mm²). Those two
ledges are unsupported overhangs if the limb prints socket-up. Nobody has printed it.

**A finding about the socket that is not about round stock**: the relief slits, at the brief's own
inner radius of 2.5, **break through into the ball bore** — as they must, since the mouth radius
is 2.9013 and the brief says explicitly that a slit stopping outboard of the mouth radius leaves
the mouth a continuous circle. I confirmed the break-through directly: the slit end wall exists
only below z = −1.9570 (where the sphere is still wider than the slit corner), and there are
edges of radius 1.9975 = √(3.2² − 2.5²) where the slit walls run into the sphere. So on the
finished part the ball will be visible through four windows. That is correct, it is what makes
the mouth open, and it is worth a sentence in the brief so the next reader does not "fix" it.

## Scope decision I made alone

I built the hinge's **Stage 1 clevis only** — fork, Ø12 trim, slot, two stubs — and **not** the
Stage 2 detent teeth. Reasons, recorded at the time: the limbs brief's acceptance list contains
no tooth check; run 3's hinge build already proved the teeth on these same numbers in its own
document and measured the inter-valley land at 0.053 mm, which it reports as unprintable; and
the teeth sit on the ear inner faces, where round stock changes nothing, so building them here
would test nothing new. Nobody was awake to ask.

## What did not work

1. **A circular pattern committed with both query fields empty, and Onshape kept it.** Covered
   above. The same class of trap as the empty merge scope: OK does not validate.
2. **A graphics-area pick went into the wrong field, and the dialog had moved.** With
   `Features to pattern` still focused, clicking the limb's cylindrical face added **`Limb body`**
   — the feature that *owns* the face — to the feature list. Filling a query list also grows the
   dialog, which pushed `Axis of pattern` down 42 px, so my earlier click into that field had
   missed. Fix: re-read every row's position after **every** pick, and assert the focus chain
   contains `axis` before picking. Three attempts.
3. **A second `Tangent` silently did nothing.** The sketch constraint tool **stays armed**, so
   pressing `t` again toggles it *off*. A pixel scan showed the right-hand line still 0.76 mm off
   the circle while the tree showed no complaint. Fix: press **Escape**, re-select, then `t`.
   Two attempts (`26-a-select-tangent-right2.png`).
4. **Selecting a sketch in the tree did not preselect it into Extrude** — the dialog opened on
   *New* with an empty, red-titled entities field. The ball-and-socket run saw the opposite, so
   this is not stable behaviour; click the sketch's tree row into the field once the dialog is
   open.
5. **Clicking a *hidden* sketch into Extrude silently makes a surface.** `Limb section` is
   consumed by `Limb body` and therefore hidden; clicking its row gave `Edges of Limb section`
   and switched the whole extrude from Solid to **Surface** with no warning. Right-click →
   **Show** first, and it gives `Faces of`. Hide it again afterwards.
6. **The rename helper broke twice, both times for the same reason** — the click it used to
   clear the selection landed on something. First on a feature row (the tree had grown), then on
   `Ear inner plane`, which is big enough to fill the canvas. The only reliable deselect is the
   context menu's own **Clear selection** item.
7. **The stub sketch over-constrained itself.** The Ø2 circle's centre snapped onto the fork
   round end's arc centre, so the "24" dimension I then added was already implied: *"Sketch could
   not be solved."* `Control+z` cleared it (`32-x-oversconstrained-undone.png`).
8. **The stub could not be picked from the tree at all.** Clicking `Stub circle` into the
   extrude's entities field did nothing, twice, with the field focused — its only region lies
   *inside* solid material. Fix: hide the part, then pick the region in the graphics area.
9. **With the part hidden the merge scope did not auto-fill** — it opened empty, the trap that
   accepts and does nothing. Filled by hand from the Parts list and read back before accepting.
10. **The stub extruded into the ear.** It built clean, looked right in preview, and added
    **exactly 0.000 mm³**. Only the volume caught it. Reopening and clicking the row-level
    direction arrow beside `Blind` (`oppositeDirection` — not the `Direction` checkbox, which is
    a custom-direction reference selector) gave +2.5132741228722 against a predicted
    2.5132741228718.
11. **`GET /features` started returning 429 "Too many requests."** while `/parts`,
    `/massproperties` and `/featurescript` kept answering. Verification continued on volumes,
    bounding boxes and FeatureScript. It recovered later.

## What the brief never said

- **That the ear tapers to nothing.** The sheet draws it and dimensions the chords, but no line
  of prose says the acceptance answer to "thinnest wall" is zero.
- **That the acceptance box check cannot see a proud corner.** See above.
- **That the relief slits open into the ball bore** — the ball-and-socket brief says the slit
  must reach inside the mouth radius and why, but not that the visible result is four windows
  onto the ball.
- **How long the limb body actually is.** The brief gives "24 long" between joint centres; the
  cylinder itself is **13.740** (z −4.150 to −17.890), because the collar eats 4.150 at the top
  and the clevis set-back `d` = 6.11 eats 6.110 at the bottom. That arithmetic is derivable but
  it is not written anywhere, and it is the first number a builder needs.
- **Which sketch the slot comes from.** The `Clevis fork profile` sketch is used *twice* — once
  Add symmetric 6 for the blank, once Remove symmetric 3.6 for the slot. That is what makes the
  ears exactly equal for free, and it is worth naming as the method rather than leaving each
  builder to invent it.
- **That the stub extrude needs flipping**, or more usefully: that a boss on an ear's inner face
  has a 50 % chance of vanishing into the ear with no error and no visual difference. The hinge
  brief says the stub faces inward; it does not say how to prove it did.
- **How to publish a version** — still not in the how-to. It is the second icon down the left
  rail, `#svg-icon-create-version-button`.

## Renders — what I saw

Five views of the part alone through `shadedviews`, at 900 × 900:
`render-upper-arm-{isometric,front,right,bottom,top}.png`. I looked at all five.

- **Isometric** — collar with four fingers at the top, the ball bore visible down the mouth, the
  limb, then the fork. Proportions match the numbers (limb 12 wide, 31.16 tall).
- **Top** — the check that matters for the socket: an unbroken 1.3 rim, four collar fingers, four
  slits, and each slit visibly crossing *inside* the mouth circle into the bore. This is the view
  that would have caught run 1's "decorative" slits.
- **Front** — the fork's rounded blade profile, 11.62 across the chord and its round end at
  z = −24.
- **Right** — the two ears with the two stubs facing each other across the slot, which is the
  only view that shows both stubs at once.
- **Bottom** — the two ears as 1.2-wide bands across the Ø12 circle with the 3.6 slot between
  them and both stubs; the ear bands visibly taper to a point where they meet the circle, which
  is the knife edge measured above. Nothing in the renders contradicts the numbers.

## Retrospective

**Which parts I inherited and which I did.** Stated plainly at the top: the socket end of this
part (11 features, one of them broken) was built by the agent before me and I did not rebuild any
of it — I verified it, repaired the pattern they left in ERROR, and built the entire clevis end,
the measurements, the renders and the version. Every volume number in the socket section of this
file that predates 03:38 is quoted from their log and is labelled as such; every number after it
I took myself.

**What went well.** Predicting each solid feature's volume in Python *before* clicking OK, and
asserting the delta afterwards. It agreed to ten or more digits on all five solid features, and
it is the only reason the stub bug took four minutes instead of surviving into the version:
+0.000 against +2.513274 is unambiguous where a preview image is not. Reading dialog fields back
by `data-parameter-id` before accepting caught the empty merge scope. Doing the final geometry
audit in FeatureScript rather than by clicking measurements in the GUI turned "the fork span is
6" into 36 faces with their true surface definitions, which is what let me answer the
thinnest-wall question with a location and a band width instead of a guess.

**What went poorly.** I picked into a dialog whose rows had moved, and I did it twice before I
started re-reading positions after every pick — the same mistake the hinge run wrote up, which I
had read. I also assumed a sketch selected in the tree would carry into Extrude because another
run said so; it did not, and the brief for that is "read the field, do not assume the click".
And I burned two rename failures on a helper that cleared selection by clicking a coordinate,
which is exactly the class of fragility I was avoiding everywhere else.

**What I would change.**

1. **The limbs brief** should state the two things its own sheet implies but its prose does not:
   the ear tapers to zero at the chord ends, and the acceptance box check needs a second
   rotation. It should also give the limb body's own length (13.740) rather than leaving it to be
   derived from three other numbers.
2. **The how-to** should get a line saying **Onshape's OK does not validate required query
   fields** — an empty merge scope no-ops silently, an empty pattern query commits to ERROR — and
   the version-publishing icon.
3. **The way I was briefed** was good in one specific way worth keeping: being told to verify the
   user's own reading of the document rather than trust it. It cost four minutes and it is what
   made the first checkpoint mean anything. The one thing I would add to a takeover brief is the
   predecessor's *last verified volume*, so the incoming agent has a single number to reconcile
   against before touching anything.

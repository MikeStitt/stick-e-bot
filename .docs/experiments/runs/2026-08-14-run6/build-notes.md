# Run 6 — build notes

What was built, in the order it was built, with the numbers measured off it. Phase by phase of
[`plan.md`](plan.md). The click paths that turned out to be worth knowing are in
[`../../../onshape-gui-howto.md`](../../../onshape-gui-howto.md); this file is what happened to
the models.

## Phase 3 — the ball and socket

**Where the work is.** `ball-socket-run6`, document `491fe2055ca07871a9595795`, Part Studio
`3ccd175be27c45f0552b4336`. Version **`ball-socket-run6-2026-08-14`**
(`14ca9e264e8aa2032b6de377`) —
[open](https://cad.onshape.com/documents/491fe2055ca07871a9595795/v/14ca9e264e8aa2032b6de377/e/3ccd175be27c45f0552b4336).
The [workspace](https://cad.onshape.com/documents/491fe2055ca07871a9595795/w/5c5bad37130f0600b0dd7362/e/3ccd175be27c45f0552b4336)
is live and will move.

Both halves in one Part Studio, as
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) requires, so the
cavity is the ball grown by the clearance rather than a second sphere.

**Eleven features.** `Sketch 1` on the Front plane — a Ø6 arc on the origin, a Ø3 stalk running
up from it, closed on the vertical axis — revolved full as `Ball stud`. `Sketch 2` on the Top
plane, a Ø9.4 circle on the origin, extruded 1.35 up and 4.15 down as `Socket body`. `Boolean 1`
subtracted the stud from the collar with **Offset all 0.2** and **Keep tools**. `Sketch 3`, four
slots on the Top plane, cut by `Extrude 2` with the merge scope set to `Socket body`.

### The stud stands on nothing, and the collar stands on nothing

The brief builds its stud on a Ø10 × 10 base and its collar on a Ø12 limb stub, both so a study
has something to hold. Phase 3 of [`plan.md`](plan.md) drops them: this stud goes on a torso face
and an arm end, and this collar goes on a head, a hand, a foot and a limb, so a stub would be
wrong on most of them.

That makes the brief's `Ball stud` volume check unusable as written — 935.2249 mm³ is the stud
*plus* its base. The base-less stud is **128.62 mm³**, which is the Ø6 sphere plus the Ø3 stalk
from the ball's surface to z = +5, less where the two overlap. What the check is actually for
still works: the number is the same before and after the slits, which is the only thing that
catches a Remove that was left merging with all and cut four slots into the ball.

### A slot through the axis would break this collar into four pieces

The brief cuts the relief slits as one slot straight through the axis, patterned twice over 90°,
and says so because on a limb stub that is right — **the stub holds the four tabs together.**
Standing on nothing, the collar has only its own floor holding them, the floor is 0.95 mm of
material between the cavity at z = −3.2 and the bottom at z = −4.15, and two crossed through-slots
cut that floor into quadrants. The part falls apart into four solids.

**So run 6 cut four separate slots, each from radius 2.5 out to 6.0**, which leaves the floor
whole inside radius 2.5 and gives the same four slits in the wall. The brief allows crossed slots
where the pattern fights; this is that permission taken one step further, for a reason the brief
does not have because it never builds the collar on its own.

The slit's inner end still has to reach inside the mouth, and 2.5 does — the mouth radius is
2.901. Cutting from 2.5 drives the slot through where the ball sits, which is why the merge scope
has to name `Socket body`.

### The slits came out 2.70 mm deep

Caught by measurement, not by looking. The two-sided cut had gone 1.35 **down** and 4.15 **up**,
so it spanned z −1.35 to +4.15 — half of it in the air above the collar — and only 2.70 mm of the
collar's 5.5 was cut. Every other acceptance check passed while that was true, exactly as the
brief warns.

The repair took three tries and two of them were wrong. Ticking the extrude's **Direction**
checkbox errored the feature; it is a custom-axis field, not a flip. Clicking **Opposite
direction** turned *both* ends the same way and errored it again. What worked was leaving the
directions alone and **swapping the two depths**, to 4.15 first and 1.35 second.

### Measured

Every row read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| parts | `Ball stud`, `Socket body` | 2 |
| ball | sphere r 3.0000 | Ø6.000 |
| stalk | cylinder r 1.5000 | Ø3.000 |
| `Ball stud` volume, before and after the slits | 128.6210 mm³ both times | unchanged |
| collar | cylinder r 4.7000, in four faces | Ø9.400 |
| cavity | sphere r 3.2000 | Ø6.400 |
| mouth | edges wholly at z = +1.3500, r 2.9013 | Ø5.8026 against 5.802586 |
| socket z-extent | −4.1500 to +1.3500 | all material below the mating face |
| slit cut faces | eight, each −4.1500 to +1.3500 | the collar's whole 5.5 |
| outer wall | four faces, 4 × 36.1998 = 144.7992 mm² | 144.803 |
| `Socket body` volume | 239.1478 mm³ | — |

The cavity is the right way up. The collar measured **272.2058 mm³** before the slits; a plain
Ø9.4 × 5.5 cylinder is 381.704, so the cavity took **109.50 mm³** — the sphere less the cap above
the mouth, not the cap on its own, which is the run 1 failure the mouth measurement cannot see.

### Looked at

Rendered on its own from three angles: isometric, front elevation, and from below. The collar
stands proud, the four slits run the full length top to bottom, and the mouth is a ring narrower
than the cavity behind it — something a ball is pushed past rather than dropped through.

Held next to [`../../build-briefs/images/brief-socket.svg`](../../build-briefs/images/brief-socket.svg),
the collar is the same shape: round, four tabs, the cavity centred one grip below the rim. The
drawing's Ø12 limb is absent, which is the deliberate change above and not a difference in the
joint.

## Phase 3 — the hinge

**Where the work is.** `hinge-run6`, document `17ece80eb53c332dd3c185ef`, Part Studio
`8a9c92f85c4a8d7483856aa1`. Version **`hinge-run6-2026-08-14`**
(`6fdeee5b50121f8c751c3612`) —
[open](https://cad.onshape.com/documents/17ece80eb53c332dd3c185ef/v/6fdeee5b50121f8c751c3612/e/8a9c92f85c4a8d7483856aa1).
The [workspace](https://cad.onshape.com/documents/17ece80eb53c332dd3c185ef/w/6e27c0b3b55276db37ad653d/e/8a9c92f85c4a8d7483856aa1)
is live and will move.

Both halves in one Part Studio, hinge axis on the origin running fore and aft, clevis limb up and
blade limb down, per [`../../build-briefs/hinge.md`](../../build-briefs/hinge.md). Like the ball
and socket, neither half stands on a base.

**The chain.** `Sketch 1`/`Extrude 1` make the blade slab; `Sketch 2` with `Extrude 2` and
`Extrude 3` grow the two Ø12 limbs; `Sketch 3`/`Extrude 4` round both ends to r6 about the axis;
`Sketch 4`/`Extrude 5` cut the 5.6 slot that leaves the two 3.2 ears; `Sketch 5`/`Extrude 6` and
`Mirror 1` put a Ø2 stub on each ear; `Sketch 6`/`Extrude 7` and `Mirror 2` sink the matching Ø2.2
pocket in each face of the blade; `Sketch 7`/`Extrude 8` slits the blade. Then the detent, twice
over: `Sketch 8` → `Extrude 9` → `Fillet 1` → `Circular pattern 1` → `Mirror 3` for the teeth, and
`Sketch 9` → `Extrude 10` → `Fillet 2` → `Circular pattern 2` → `Mirror 4` for the valleys.

### The degenerate crown fillet works, if you pick the crown and not the barrel

The brief's claim holds: an ordinary **Fillet** at r0.4 on a Ø0.8 boss 0.6 tall is accepted with
no warning, and turns the boss into a hemisphere on a 0.2 collar. Measured, the tooth is a
SPHERE r 0.4000 of area 1.0053 — exactly 2πr², a full hemisphere — over a CYLINDER r 0.4000 of
area 0.5027, which is π × 0.8 × 0.2.

Getting there took two failures, both reading **"Fillet 1 did not regenerate properly: Overlapping
fillets."** — at r0.4, then at r0.35 with edge overflow off. The second failure is what named the
cause: 0.35 cannot be degenerate against a 0.4 crown, so the pick was never the crown. It was the
**side wall**, whose top and bottom rims are 0.6 apart, and 0.35 + 0.35 overruns that. At 45.8
px/mm the crown is a 37-pixel ellipse sitting inside a barrel that reads as the same blob.
Zooming to about 116 px/mm separated them and the r0.4 fillet went in first try.

### A Remove with a starting offset buried the valley inside the blade

`Extrude 10` — Ø1.0, 0.45 deep, starting offset 2.05, scope `Detent blade` — took the settings
without complaint and removed exactly π × 0.5² × 0.45 = 0.35343 mm³. The bore came out at
**y −2.05 to −1.60**: it started at the right depth and then ran *inward*, leaving 0.45 mm of
blade roofed over a sealed void. `Extrude 9`, an **Add** from the same Front plane with the same
offset field filled, had run the other way.

**The face count says which happened before any picture does.** A sealed void adds two disc faces
and the blade counted 20 planes; an open pocket adds one floor and it counted 19. Clicking
**Opposite direction** beside the depth's `Blind` — not the `Direction` checkbox, which is a
custom-axis field — moved the bore to y −2.50 to −2.05 and dropped the count to 19.

### A pattern's Features field eats a click meant for the axis

With `Features to pattern` still collecting, clicking the pocket's rim in the graphics area added
**`Extrude 7`** to the features list. Onshape resolved the click to *the feature that made that
geometry*, and the empty `Axis of pattern` field below it never saw it. Clicking into the axis
field first is what fills it, and the chip then reads `Edge of Extrude 7`.

### Onshape commits a mirror with no mirror plane

`Mirror 4` went into the tree **in red** with `Mirror plane` empty. The green check accepted it,
the dialog closed, and the only visible sign was the feature's colour — the model was unchanged
and the volume identical to the feature before it. The plane had not taken because scrolling the
feature tree with the wheel dropped focus from the field; the click on `Front` after that
selected a tree row and nothing more. Scroll first, then click into the field, then pick.

### Measured

Every row read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| parts | `Clevis fork`, `Detent blade` | 2 |
| limbs | cylinder r 6.0000 on both | Ø12 |
| clevis extent | x ±6, y ±6, z −6.0000 to +16.0000 | blade stands 16 out of the joint |
| blade extent | x ±6, y ±6, z −15.0000 to +6.0000 | — |
| slot | ear inner faces at y ±2.8000 | 5.6 |
| slit | walls at y ±0.4000 | 0.8, two 2.1 tabs |
| pocket | cylinder r 1.1000, floors at y ±1.5000 | Ø2.2 × 1.0 |
| stub | cylinder r 1.0000, ends at y ±2.0000 | Ø2.0 × 0.8 |
| tooth crown | sphere r 0.4000, area 1.0053 mm², 48 of them | a full hemisphere per tooth |
| tooth band | 24 crowns per ear at r 4.8000, y ±2.4000 | 24 at 15° |
| valley | cylinder r 0.5000, floors at y ±2.0500 | Ø1.0 × 0.45 |
| valley rim break | torus, 48 of them | r0.10 on every valley |
| `Clevis fork` volume | 1377.2865 mm³ | — |
| `Detent blade` volume | 1228.5555 mm³ | — |

The volume answered every step of the detent, because each step's arithmetic is closed form.
One tooth is π × 0.4² × 0.6 = 0.30159 and the model moved 0.30159. The crown fillet takes
πr³/3 = 0.06702 and the model gave back 0.06702. `Circular pattern 1` added 23 × 0.234572 =
5.3952, so it carried 23 more *domes* rather than 23 bare cylinders. On the blade, cut plus break
is 0.35343 + 0.00704 = 0.36047 per valley — the 0.00704 by Pappus on the corner the break
removes — and the pattern took 23 × 0.36047 = 8.2909 and the mirror 24 × 0.36047 = 8.6513, ending
at 1228.5555 against 1228.5555 predicted.

### The land between valleys is 0.0531 mm, and run 3's number reproduces

Measured off the model rather than off the brief's arithmetic: neighbouring valley centres are
**1.2531** apart on the r 4.8000 band, which is the chord 2 × 4.80 × sin 7.5°. A Ø1.0 valley
leaves **0.2531** of land, and an r0.10 break takes 0.10 from each side, leaving **0.0531**. Run 3
measured 0.053. The same band carries the bumps 1.2531 apart, and a Ø0.8 dome leaves **0.4531** of
flat between neighbours — the brief predicted 0.46 from a 1.257 pitch.

Nothing has been printed, so what that land does on a 0.4 mm nozzle is still open, and the brief
says so. What the model now says is that the two are not independent: the break cannot grow past
r0.126 without the lands meeting and the valleys merging into one groove.

The **thinnest wall in either part is 1.10 mm** — the blade between a pocket floor at y ±1.5 and
the slit wall at y ±0.4. Behind a valley floor the tab is 1.65. Both are several passes of a
0.4 mm nozzle.

### Looked at

Rendered on its own from three angles, isometric, front and right. The fork's ring of 24 domes
sits inside the ear with none of them clipped — every crown measures the same full-hemisphere
area. The blade's valley ring is concentric with its pocket, and the slit runs down the middle of
the blade's 5.0 thickness, splitting it into the two 2.1 tabs that have to spring.

## Phase 3, rebuilt — the ball and socket in the run 6.1 documents

The joints above are geometrically right and every number in them stands. What they are not is a
record a beginner can learn Onshape from: the shots are of geometry after a step succeeded rather
than of the dialog with its fields filled, and the tree carries `Sketch 1`, `Extrude 7`,
`Mirror 3`. So phase 3 was performed again, from empty documents, to the capture and naming
standard in [`plan.md`](plan.md). The documents are called **run 6.1** so they stay separate from
the run 6 ones; the run, the phase and the plan are unchanged.

**Where the work is.** `ball-socket-run61`, document `de2c0d9bdbb02b3a345eada1`, Part Studio
`b6db2491eeffbc3a865fff4f` — ids in [`run61-documents.json`](run61-documents.json). Version
**`ball-socket-run61-2026-08-14`** (`cd146dc9becaaac2dc34c1d7`) —
[open](https://cad.onshape.com/documents/de2c0d9bdbb02b3a345eada1/v/cd146dc9becaaac2dc34c1d7/e/b6db2491eeffbc3a865fff4f).
The [workspace](https://cad.onshape.com/documents/de2c0d9bdbb02b3a345eada1/w/e73b85313fe2496ae852837b/e/b6db2491eeffbc3a865fff4f)
is live and will move.

**Seven features, each named as it was made.**

| Tree row | What it is |
| -------- | ---------- |
| `Stud profile` | Front-plane sketch: Ø6 circle on the origin, a 1.5 × 5 rectangle standing on it, and the axis line down the vertical — one sketch, so nothing is reopened |
| `Revolve stud` | Revolve, New, the three regions right of the axis, `Edge of Stud profile` as the axis, full revolve |
| `Collar circle` | Top-plane sketch: Ø9.4 circle on the origin |
| `Collar blank` | Extrude, **New**, Depth 1.35, Second end position 4.15 |
| `Cavity from ball` | Boolean Subtract: `Ball stud` as the tool, `Socket body` as the target, Offset all 0.2, Keep tools |
| `Slit profile` | Top-plane sketch: one 3.5 × 0.8 slot, 2.5 to 6 along the x axis and 0.4 either side of it, circular-patterned to four |
| `Relief slits` | Extrude, **Remove**, Depth 4.15, Second end position 1.35, merge scope `Socket body` |

Parts: `Ball stud`, `Socket body`.

### Measured

Read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| ball | sphere r 3.0000, area 105.5213 | Ø6.000 |
| stalk | cylinder r 1.5000, area 22.6376 | Ø3.000 |
| `Ball stud` volume | 128.6210 mm³ | run 6's 128.6210 |
| collar blank | cylinder r 4.7000, z −4.1500..+1.3500, 381.6878 mm³ | Ø9.400 × 5.500 |
| cavity | sphere r 3.2000, area 91.4832 | Ø6.400 |
| mouth | top face fell 69.3978 → 42.9534, so a circle of r 2.9013 | Ø5.8026 against 5.802586 |
| `Socket body` after the cavity | 272.2058 mm³ | 381.704 less 109.50 |
| outer wall after the slits | four cylinders, 4 × 36.1998 = 144.7992 mm² | 144.803 |
| slit side faces | eight, and the bottom face fell 69.3978 → 62.3760 | the collar's whole 5.5 |
| socket z-extent | −4.1500 to +1.3500 | all material below the mating face |
| `Ball stud` volume, before and after the slits | 128.6210 mm³ both times | unchanged |
| `Socket body` finished | 239.1478 mm³ | run 6's 239.1478 |

The cavity took 109.482 mm³ — the r3.2 sphere less the cap above z = +1.35, which is
137.258 − 27.777. The cap on its own is the run 1 failure the mouth measurement cannot see, and
this arithmetic is what separates the two.

Every one of the finished numbers is run 6's number to four decimals, from a build that copied
nothing.

### The two depths swap between the collar and the slits, and only measurement says so

The collar blank wanted **1.35 first, 4.15 second** on the Top plane, and landed at
z −4.1500..+1.3500 first time — where run 6 had needed that pair swapped. So the slit cut was set
the same way, and it was wrong: it spanned z −1.35..+4.15, half of it in the air above the collar,
cutting **2.70 mm of the collar's 5.5**.

Nothing in the GUI said so. The feature regenerated clean, the tree was green, four slits showed
through the wall from above, and the top face really had been cut into four tabs. What caught it
was the outer wall measuring 153.7699 mm² where four full-length slits leave 144.7992 — a
0.8-wide slot takes 0.8012 of arc at r 4.7, so 8.6504 mm² of missing wall over four slits is
2.699 mm of depth and not 5.5. The bottom face still reading its full 69.3978 says the same thing.

Swapping to **4.15 first, 1.35 second** fixed it, and every number then matched run 6. Run 6 hit
this on the same feature and repaired it the same way, having first tried the **Direction**
checkbox (which errors — it is a custom-axis field, not a flip) and **Opposite direction** (which
turns *both* ends the same way).

So: the first depth's direction is not a property of the plane. `Collar blank` runs its first
depth up and `Relief slits` runs its first depth down, on the same Top plane, in the same
document. Set both, then measure — a preview looked right in both cases.

### The slit sketch was built twice

The first `Slit profile` closed with one slot in it, not four. Escape had been pressed to put the
circular pattern tool down, and Escape discards the pattern — the sketch still closed clean and
still read fully defined, so the loss only showed when the extrude previewed a single slot. The
sketch was reopened, patterned again, and settled by clicking clear of the geometry. Written up
in [`../../../onshape-gui-howto.md`](../../../onshape-gui-howto.md) § 7.

### Four separate slots, not two through the axis

Carried forward from run 6 and unchanged: the brief cuts the relief slits as one slot straight
through the axis, patterned twice over 90°, which is right on a limb stub because the stub holds
the four tabs together. Standing on nothing, this collar has only its own 0.95 mm floor between
the cavity at z = −3.2 and the bottom at z = −4.15, and two crossed through-slots cut that floor
into quadrants. So four separate slots, each from radius 2.5 out to 6.0, leaving the floor whole
inside radius 2.5.

The slot's inner end still reaches inside the mouth: 2.5 against a mouth radius of 2.901.

## Phase 3, rebuilt — the hinge in the run 6.1 documents

**Where the work is.** `hinge-run61`, document `aca8691bb83295fdde2015db`, Part Studio
`08688d842246482d3d09959a` — ids in [`run61-documents.json`](run61-documents.json). Version
**`hinge-run61-2026-08-14`** (`2d85fa248db742e137da6e96`) —
[open](https://cad.onshape.com/documents/aca8691bb83295fdde2015db/v/2d85fa248db742e137da6e96/e/08688d842246482d3d09959a).
The [workspace](https://cad.onshape.com/documents/aca8691bb83295fdde2015db/w/51cea5ef558233bb62482046/e/08688d842246482d3d09959a)
is live and will move.

Both halves in one Part Studio, hinge axis on the origin running fore and aft, per
[`../../build-briefs/hinge.md`](../../build-briefs/hinge.md). The fork is finished before the
blade is started, so no step ever has two solids overlapping each other, and the brief's forced
order — stub before pocket — falls out of that on its own.

**The clevis fork, each row named as it was made.**

| Tree row | What it is |
| -------- | ---------- |
| `Limb circle` | Top-plane sketch: Ø12 circle on the origin |
| `Fork limb` | Extrude, New, z −6 up to +16 |
| `Round end profile` | Front-plane sketch: the r6 round end about the hinge axis, split along the x axis so the lower half rounds the fork's tip and the upper half is there for the blade |
| `Fork round end` | Extrude, **Remove**, Through all, Symmetric — the tip comes out an exact r6 Steinmetz patch of 144.0000 mm² |
| `Slot profile` | Right-plane sketch: the 5.6-wide slot, 17 deep from the tip |
| `Fork slot` | Extrude, **Remove**, Through all, Symmetric, merge scope `Clevis fork` — leaves the two 3.2 ears with their faces at y ±2.8 |
| `Stub circle` | Sketch on the ear's inside face: Ø2 on the hinge axis |
| `Ear stub` | Extrude, Add, Depth 0.8 — y 2.8 in to 2.0 |
| `Tooth circle` | Sketch on the same face: Ø0.8, 4.8 out from the hinge axis |
| `Ear tooth` | Extrude, Add, Depth 0.6 |
| `Tooth crown` | Fillet, Radius 0.4, on the tooth's crown — a hemisphere on a 0.2 collar |
| `Tooth ring` | Circular pattern, **Feature pattern**, `Ear tooth` + `Tooth crown`, axis `Face of Ear stub`, 360° and 24 with Equal spacing |
| `Detents both ears` | Mirror, **Feature mirror**, those four features across the Front plane, **Reapply features** |

### The Front plane sits between you and the far ear, and eats every click

Zoomed in on a tooth, the Front plane fills the screen. It is in front of the ear at y = +2.8, so
every click meant for the tooth lands on the plane instead: the pick reads as the plane, the
readout goes blank, and nothing in the graphics area appears to respond.

Right-click any plane row → **Hide all planes** clears it in one step, and the same menu carries
**Clear selection**, which is what actually deselects — `Escape` sent from a script does not.

### The crown reports an area; the barrel reports a diameter

An ordinary **Fillet** at r0.4 on a Ø0.8 boss 0.6 tall turns the boss into a hemisphere on a 0.2
collar, exactly as run 6 found. Both the crown and the barrel put the same chip in the field —
`Face of Ear tooth` — so the chip cannot tell you which one you have.

The readout can. Click the crown and the bottom-right corner says **`Area: 0.50265 mm2`**; click
the barrel and it says **`Diameter: 0.80000 mm`**. Filleting the barrel asks for r0.4 on both of
its edges at once and errors; filleting the crown gives the dome. In the run 6.1 view the crown is
a thin sliver along the bump's near edge and the barrel is the whole bright face — aiming at the
middle of what looks like the tip gets you the barrel every time.

### The axis chip pushes Angle and Instance count down a row

Circular pattern's fields move when the axis lands in the field: `Angle` and `Instance count` each
drop by one row's height. Typing the count into the box that was `Instance count` a second earlier
puts `24` into `Angle`, and the feature commits happily as 24 instances over 24°.

Fill the axis first, then read the labels again before typing either number.

### The mirror plane took, because the plane field was clicked first

Run 6 recorded a mirror committing with an empty plane field. Clicking into `Mirror plane`
*before* going to the tree for the Front plane put it in the field on the first try, and the field
read `Front plane` before the tick. Same habit as the pattern's axis field.

### Measured — the clevis fork

Read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| `Fork limb` | cylinder r 6.0000, z −6.0000..+16.0000, 2488.1414 mm³ | Ø12 × 22 |
| round end | cylinder r 6.0000, area 144.0000 | the exact Steinmetz patch |
| ear inside faces | two planes at y ±2.8000 | the 5.6 slot in a Ø12 limb |
| slot root | plane of 64.6743 mm² at z = +11 | 17 deep from a tip at z = −6 |
| `Ear stub` | cylinder r 1.0000, y 2.0000..2.8000, area 5.0265 | Ø2 × 0.8 |
| tooth barrel | cylinder r 0.4000, area 0.5027, ×48 | π × 0.8 × 0.2 |
| tooth crown | sphere r 0.4000, area 1.0053, ×48 | 2πr², a full hemisphere |
| tooth band | z 4.4000..5.2000 | the brief's r 4.40 → 5.20 |
| `Clevis fork` volume | 1377.2865 mm³ | run 6's 1377.2865 |
| `Clevis fork` extent | x ±6, y ±6, z −6.0000..+16.0000 | run 6's box |

Every finished number is run 6's number to four decimals, from a build that copied nothing.

**The detent blade, each row named as it was made.**

| Tree row | What it is |
| -------- | ---------- |
| `Blade slice` | Top-plane sketch: a Ø12 construction circle on the origin and a centre-point rectangle inside it, one corner coincident with the circle and the short side dimensioned 5 — so the long side comes out 10.9087 without anyone typing it |
| `Blade slab` | Extrude, **New**, 6 up and 10 down |
| `Blade round end` | Extrude, **Remove**, the upper-outside region of the fork's `Round end profile`, Through all, Symmetric, merge scope `Detent blade` |
| `Blade limb circle` | Sketch on the slab's bottom face: Ø12 on the origin |
| `Blade limb` | Extrude, Add, Depth 5 — z −10 down to −15 |
| `Blade slit profile` | Right-plane sketch: a centre-point rectangle on the vertical, 16 long with its far end 10 from the axis, 0.8 wide |
| `Blade slit` | Extrude, **Remove**, Through all, Symmetric, merge scope `Detent blade` — leaves the two 2.1 tabs with their walls at y ±0.4 |
| `Blade pocket circle` | Sketch on the blade's near face: Ø2.2 on the hinge axis |
| `Blade pocket` | Extrude, **Remove**, Depth 1 — floor at y −1.5 |
| `Blade valley circle` | Sketch on the same face: Ø1.0, 4.8 up the vertical from the hinge axis |
| `Blade valley` | Extrude, **Remove**, Depth 0.45 |
| `Blade valley rim` | Fillet, Radius 0.1, on the valley's rim **edge** — the field reads `Edge of Blade valley`, and a pick that got the bore instead reads `Face of` |
| `Blade valley ring` | Circular pattern, **Feature pattern**, `Blade valley` + `Blade valley rim`, axis `Edge of Blade pocket`, 360° and 24 with Equal spacing |
| `Detents both faces` | Mirror, **Feature mirror**, those four features across the Front plane, **Reapply features** |

### Construction is a mode, and it stays on until it is turned off

Pressing `q` turns the picked entity into construction geometry and leaves the sketch in
construction mode, so the next thing drawn is construction too. `Blade slice`'s rectangle came out
as four construction lines: the sketch closed clean, the tree showed nothing wrong, and the
extrude that followed had no region to find. Selecting the four sides and pressing `q` again made
them edges and the shaded region appeared.

Two habits come out of it: check the construction button is dark before drawing anything that has
to become a face, and read the new sketch as a shape, not as lines.

### A sketch inside a solid cannot be picked, so hide the solid first

Two of the blade's sketches sit inside something. `Blade slice` is on the Top plane, buried in the
fork, and `Blade slit profile` is on the Right plane, buried in the blade itself once the slab
exists. The click meant for the sketch region lands on the solid's face, the extrude's field fills
with `Face of Blade slab`, and the preview splits the part in two.

Right-click the part row in the parts list → **Hide**. The part is still pickable from that list
for the merge scope while it is hidden, so the cut can still be aimed at it.

### Ticking Symmetric moves Merge scope up a row

Symmetric removes the **Second end position** row from the Extrude dialog, and every field below
it rises by one row. A click aimed where Merge scope sat a moment earlier misses the field, and
the field stays red. Tick Symmetric first, then read the labels again before filling anything
under them.

### Sizing a circle moves it

The valley circle was drawn 4.8 up the vertical by eye and constrained only to the vertical.
Setting its diameter to 1 let the solver slide the centre down to 3.34 from the axis. The next
pick, aimed where the circle had been drawn, found the blade's face instead, and Onshape refused
the dimension with *A dimension cannot be created between these items*. Look at where the centre
went, then dimension from the origin to it.

### The blade lands 0.0150 mm³ under run 6, and the closed form says run 6.1 is right

`Detent blade` finished at **1228.5404 mm³** against run 6's 1228.5555. Every detent step matched
run 6 exactly — 0.35343 for the valley cut, 0.00704 for the rim break, 8.2909 for the pattern's 23
more valleys, and 12.4526 for the mirror's 24 valleys and second pocket — so the gap is upstream
of the first pocket, in the blade body.

Worked from the geometry: the blade's face profile is 10.908712 × 10 below the hinge axis plus
54.712629 above it, where the r6 arc takes the corners off, which is 163.799749 in all. The model
reports that face as 163.7998. Times the 5 thickness the slab and round end are 818.998745, the
limb adds π × 36 × 5 = 565.4867, and the slit takes 0.8 × 163.799749 = 131.0398, leaving
**1253.4457** before the first pocket. Run 6 was carrying 1253.4607 there.

### Measured — the detent blade

Read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| `Blade slab` | x ±5.4544, y ±2.5, z −10.0000..+6.0000, 872.6970 mm³ | 10.9087 × 5 × 16 |
| `Blade round end` | face profile 163.7998 mm², 818.9988 mm³ | the r6 arc about the hinge axis |
| `Blade limb` | cylinder r 6.0000, area 188.4956, 1384.4855 mm³ | Ø12 × 5 |
| slit | walls at y ±0.4000, tabs 2.1 thick | 0.8 × 16, open at the round end |
| pocket | cylinder r 1.1000, floors at y ±1.5000, two of them | Ø2.2 × 1.0 |
| valley | cylinder r 0.5000, floors at y ±2.0500, 48 of them | Ø1.0 × 0.45 |
| valley rim break | torus, 48 of them | r0.10 on every valley |
| valley band | 24 a face at r 4.8000, 15.000° apart | 24 at 15° |
| land between valleys | pitch chord 1.2530, land 0.2530, 0.0530 after the break | run 3's 0.053 |
| teeth against valleys | the same 24 angles, 0.000° offset | the two rings in phase, or the detent never seats |
| `Detent blade` extent | x ±6, y ±6, z −15.0000..+6.0000 | run 6's box |
| `Detent blade` volume | 1228.5404 mm³ | run 6's 1228.5555 |
| `Clevis fork` volume, after the blade was built | 1377.2865 mm³ | unchanged |

### Looked at

Both halves shown together and turned three ways. Isometric puts the blade's round end up inside
the fork's slot, with the two limbs running opposite ways along z. From the left the slit runs
down the middle of the blade's 5.0 and the fork's two tooth rings sit in the blade's two valley
rings, one each side of it.

## Phase 4 — the torso

**Where the work is.** `torso-run6`, document `a0aeea9c9b4061e021977e57`, Part Studio
`f83e5da0b21725c3d104196e` — ids in [`run6-documents.json`](run6-documents.json). Version
**`torso-run6-2026-08-14-2`** (`a802fa578af50f48eabadb06`) —
[open](https://cad.onshape.com/documents/a0aeea9c9b4061e021977e57/v/a802fa578af50f48eabadb06/e/f83e5da0b21725c3d104196e).
The earlier version `torso-run6-2026-08-14` (`dc7ea4a9e4a9350ee83aa287`) is the same geometry with
the top-face cut still carrying a starting offset; cite the `-2`.

**Front-first, as [`plan.md`](plan.md) requires.** The first sketch is the torso's front elevation
on the Front plane — a centre-point rectangle on the origin, 36 across by 48 tall — extruded
symmetric through 24 in y. Every overview sheet the student has just read is a front elevation, and
this is the sketch that matches it.

| Tree row | What it is |
| -------- | ---------- |
| `Torso outline` | Front-plane sketch: centre-point rectangle on the origin, 36 × 48 |
| `Torso block` | Extrude, **New**, symmetric, 24 |
| `Hip stud profile` | Front-plane sketch: the stud's half-section and its axis line |
| `Revolve hip stud` | Revolve, **New**, full, about `Edge of Hip stud profile` |
| `Mirror hip stud` | Mirror, **Part mirror**, `Hip stud`, Right plane |
| `Neck stud profile` | Front-plane sketch: the same half-section on the top face |
| `Revolve neck stud` | Revolve, **New**, full |
| `Shoulder stud profile` | Front-plane sketch: the shoulder's half-section, lying along +x from the origin, with its Ø8 boss run 10 back past its own root |
| `Revolve shoulder stud` | Revolve, **New**, full |
| `Shoulder pivot lines` | Right-plane sketch: a +y line and a +z line through the origin, which is what a Transform will accept as an axis |
| `Tip shoulder 53 deg` | Transform, **Rotate**, +53° about the +y line |
| `Swing shoulder 30 deg forward` | Transform, **Rotate**, −30° about the +z line |
| `Move shoulder to its station` | Transform, **Translate by XYZ**, (18, 0, 20) |
| `Mirror shoulder stud` | Mirror, **Part mirror**, `Shoulder stud`, Right plane |
| `Boss into torso, mirrored side` | Extrude, **Add**, the mirrored boss's back disc, into the block |
| `Boss into torso` | Extrude, **Add**, the same on the other side |
| `Top face cut outline` | A rectangle sketched **on the torso's top face**, big enough to cover both bosses |
| `Cut bosses flush with the top face` | Extrude, **Remove**, Blind 12 away from that face, merge scope the two shoulder studs |
| `Union the torso and its studs` | Boolean **Union**, all six bodies, `Keep tools` off |

Parts: `Torso`.

### Measured — the torso

Read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| block | x ±18.0000, y ±12.0000, z ±24.0000 | 36 × 24 × 48 |
| hip balls | r 3.0000 at (±12.0000, 0.0000, −29.0000) | ±12, 0, −29 |
| neck ball | r 3.0000 at (0.0000, 0.0000, +29.0000) | 0, 0, +29 |
| shoulder balls | r 3.0000 at (±24.7754, −3.9118, +9.6177) | ±24.775, −3.912, +9.618 |
| shoulder boss | cylinder r 4.0000, axis (0.5212, 0.3009, 0.7986) | Ø8 at 53° below horizontal, 30° toward the front |
| shoulder stalk | cylinder r 1.5000, same axis | Ø3 |
| the highest plane in the part | one, at z = +24.0000 | the top face, nothing standing proud of it |
| top face | 878.3647 mm² over x −20.1660..+20.1660 | the block's top plus what the two bosses add outboard of x = ±18 |
| bottom face | 849.8628 mm² | 36 × 24 less two Ø3 stalks |
| `Torso` extent | x ±27.7754, y ±12.0000, z ±32.0000 | symmetric about the Right plane |
| `Torso` volume | 42890.0333 mm³ | |

`highZ` = 32.0000 is the neck ball's top — centre +29 and r 3 — and it is the only thing above the
top face. Nothing of either shoulder boss survives the cut.

### The boss has to overrun its own root, and then be cut off

A revolved boss ends in a flat disc perpendicular to its own axis. Put that disc at the root and it
sits partly outside x = 18, so the boss meets the torso's side face along a slanted ellipse and
leaves an open wedge behind it. So the boss is revolved 10 mm long past its root instead, which
puts its whole back disc above the top face — z +25.58 to +30.39, measured before the cut — and the
excess comes off with the top-face cut. That is the construction
[`../../build-briefs/torso.md`](../../build-briefs/torso.md) describes, and now the reason it gives
one is written down.

### A plane is not accepted as a rotation axis

`Transform` ▸ `Rotate` wants an **axis**, and the `Axis` field will not take the Front plane: the
click lands, the field stays empty, and its required-field underline stays red. What it takes is a
line — so `Shoulder pivot lines` exists only to give the two rotations something to turn about: one
line up +y and one up +z, both through the origin, on the Right plane.

The two rotations then take +x to (0.5212, −0.3009, −0.7986), which is 53° below horizontal and
30° toward the front. Both were measured after their own feature rather than after the pair, so a
sign error could not hide behind the other rotation.

### Onshape rescales the whole sketch when the first dimension goes on

`Top face cut outline` was drawn by eye at roughly 24 × 10, and setting its width to 80 took the
height to **35.3** — Onshape scaled the sketch about its centre rather than moving one edge. The
second dimension then missed, because the edge it was aimed at had moved off screen. Zoom out and
re-read the geometry's position from the screen after the first dimension, not before it.

### The cut belongs on the face, not on a plane 24 above it

The first `Cut bosses flush with the top face` was a Top-plane sketch with a **starting offset** of
24, and it ran the wrong way first: it removed the band z +12 to +24 out of the middle of each
stud, splitting each into three bodies, with every feature green. Flipping it needed the
**Opposite direction** arrow beside the depth's `Blind` — the same control, and the same wrong
first guess, as the detent valley above.

That is exactly what [`plan.md`](plan.md) phase 4 forbids, so the cut was rebuilt: the sketch's
plane was changed from `Top plane` to `Face of Torso block`, and the extrude's `Starting offset`
was unticked. It then starts on the face it is drawn on and runs away from the material, there is
no direction to check, and the arrow does not come into it. The sketch survived being re-planed —
its dimensions and its rectangle came with it, and the whole tree below it regenerated green.

### Two graphics picks in one dialog, and only the first one lands

The `Extrude` that pushes the bosses into the block was tried once with both back discs clicked in
the same dialog. The second click never registered — the faces list kept one chip. Splitting it
into `Boss into torso` and `Boss into torso, mirrored side`, one face each, works.

The far boss's disc also cannot be picked from isometric, where it presents nearly edge-on. From
the **Top** view — the view cube's top face, not the View menu, which has no Top entry — it
presents as a full ellipse and picks first time.

### Boolean keeps its tools unless you tell it not to

`Keep tools` arrives **ticked**. The union ran, the tree went green, and `Parts` went from 6 to 7 —
a new `Part 7` with the six originals still sitting inside it. Untick `Keep tools` and the six
inputs are consumed, leaving `Parts (1)`.

### A hidden part measures as nothing at all

`GET .../boundingboxes` on a hidden part returns all zeros rather than an error, so a part that was
right-click-hidden to get it out of the way reads as if it had no geometry. Un-hide before
measuring.

### The document was not empty when this phase started

`torso-run6` already held a front-first block from an earlier sitting, built without shots and with
`Sketch 1` / `Extrude 1` still in the tree. It was deleted and the part rebuilt from the empty
document, because a part whose first two features have no record is not the record phase 4 exists
to produce.

## Phase 4 — the head

**Where the work is.** `head-run6`, document `d0d75cf75bd29b2e576093e4`, Part Studio
`ef77897fabbaa144d9f2176a` — ids in [`run6-documents.json`](run6-documents.json). Version
**`head-run6-2026-08-14`** (`2c594a3ade6bbc9e50bcb377`) —
[open](https://cad.onshape.com/documents/d0d75cf75bd29b2e576093e4/v/2c594a3ade6bbc9e50bcb377/e/ef77897fabbaa144d9f2176a).

**Front-first.** The first sketch is the head's front elevation on the Front plane: a centre-point
arc of radius 18 on the origin for the dome, two 18-long sides dropping from its ends, and a line
across the bottom. That is the shape on every overview sheet, and it is 36 across and 36 tall
before anything is cut out of it.

**Built to [`head.md`](../../build-briefs/head.md)'s order**, which puts the shell last for the
reason that brief gives.

| Tree row | What it is |
| -------- | ---------- |
| `Head profile` | Front-plane sketch: centre-point arc r18 on the origin, two sides 18 long, a line across the bottom |
| `Head body` | Extrude, **New**, symmetric, 30 |
| `Outline rounds` | Fillet, radius 3, on the four vertical edges |
| `Eye profile` | Sketch on the front face: an ellipse 10 the long way and 7 the short way, centre 8 out from the middle and 6 above the centre line |
| `Eye` | Extrude, **Add**, 1.5 — the eye stands proud, it is not a hole |
| `Second eye` | Mirror, **Feature mirror**, `Eye`, Right plane |
| `Mouth profile` | Sketch on the front face: a centre-point rectangle 16 × 4 with a Ø4 circle midpoint-constrained on each short edge, 6 below the centre line, held sideways by a vertical constraint from the origin to the rectangle's centre |
| `Mouth` | Extrude, **Remove**, 1.5, all five of that sketch's regions |
| `Collar circle` | Sketch on the underside: Ø9.4 on the origin |
| `Collar blank` | Extrude, **Add**, 5.5 — the collar hangs below z −18 |
| `Cavity profile` | Front-plane sketch: a Ø6.4 circle 22.15 below the origin, cut in half by a line from its top quadrant point to its bottom |
| `Cavity from ball` | Revolve, **Remove**, full, region `Face of Cavity profile`, axis `Edge of Cavity profile`, **Merge with all** |
| `Slit profile` | Sketch on the collar's rim face: centre-point rectangle on the origin, 0.8 across and 12 long, so it runs clear past the collar both ways |
| `Slit pair` | Extrude, **Remove**, Blind 5.5, merge scope `Head` — one rectangle through the middle makes two slits |
| `Second slit pair` | Circular pattern, **Feature pattern**, `Slit pair`, axis `Edge of Collar blank`, 90° and 2, Equal spacing, **Reapply features** |
| `Head shell` | Shell, faces to remove `Face of Head body` — the back, at y +15 — thickness 1.2 |

Parts: `Head`.

### Measured — the head

Read off the model through `bodydetails` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| head body | x ±18.0000, y ±15.0000, z −18.0000..+18.0000 | 36 across, 36 tall, 30 deep |
| whole part | x ±18.0000, y −16.5000..+15.0000, z −23.5000..+18.0000 | 41.500 tall, −23.500 to +18.000 |
| outline rounds | cylinder r 3.0000 at (±15, ±12), axis z, four of them | r3 on the four vertical edges |
| eyes | ellipse face 54.9779 mm² at y −16.5000, over x ∓13..∓3 and z +2.5..+9.5 | 10 × 7 at (±8, +6), standing 1.5 proud |
| mouth | floor 76.5664 mm² at y −13.5000, ends cylinder r 2.0000 at (±8, −13.5, −6.0), walls at z −4.0000 and −8.0000 | 20 × 4, cut 1.5, centre 6 below |
| collar | cylinder r 4.7000 at (0, 0, −23.5), axis z, z −23.5000..−18.0000 | Ø9.400, standing 5.500 proud |
| socket | sphere r 3.2000 at (0.0000, 0.0000, −22.1500) | centre 22.150 below the head centre |
| which way up the socket is | −22.1500 − (−23.5000) = **+1.3500** | 1.350 **above** the rim plane |
| socket mouth | rim annulus 42.9534 mm² before the slits, against r 4.7000 outside → r 2.9013, **Ø5.8025** | Ø5.803 |
| rim | four planes at z −23.5000, 9.2966 mm² each | four arcs, not a circle |
| one rim arc | from 4.88° to 85.12° about the axis, **80.23°** | four equal arcs with four 0.8 gaps |
| profile tangency | side plane x 18.0000 over z −18.0000..0.0000 meets cylinder r 18.0000 about the y axis at (0, −15, 0) over z 0.0000..+18.0000 | tangent, no crease |
| slits | eight walls at x ±0.4000 or y ±0.4000, every one z −23.5000..−18.0000 | 0.8 wide, the collar's whole 5.500 |
| shell, five face pairs | sides x ±18.0000/±16.8000, floor z −18.0000/−16.8000, front y −15.0000/−13.8000, mouth floor y −13.5000/−12.3000, socket sphere r 3.2000/4.4000 | 1.200 at each |
| thinnest wall | **1.200**, at all five of those | 1.2 |
| `Head` volume | 6019.0314 mm³ | |
| Parts | 1 | 1 |

The socket mouth is taken from the rim's area rather than from an edge, because the four slits
leave no single circular edge to measure: outside radius 4.7000 and annulus 42.9534 mm² give
inside radius 2.9013. The sphere says the same thing from the other direction — a r3.2 ball cut by
a plane 1.35 off centre leaves a circle of radius 2.9013 — and the two agree to four places.

Closest approaches that are **not** walls, so nobody has to re-derive them: the four slits are
0.800 apart across their own gap, and the rim's annulus is 1.799 wide from mouth to outside. The
collar's wall at the ball's equator is 1.500, thicker than the shell.

`Cavity from ball` took the volume down by 109.48 mm³, which is what phase 3 measured the
ball-and-socket's cavity at. Same sphere, same rim plane, same answer.

### The socket is upside down on purpose, and the sign is the check

The head sits on top of the neck ball, so the ball comes in from **below** and the material sits
**above** the mouth. Written out before cutting: the mouth is in the collar's end face at z −23.5,
the cavity centre is 1.35 **above** it at z −22.15, so `origin.z − lowZ` must come out **positive**.
It reads +1.3500. A socket built the wrong way up gives −1.35 with every feature still green, which
is why the sign is written down before the measurement rather than after it.

### A whole sketch can slide even when every line in it is black

`Mouth profile` looked finished — no blue anywhere, both circles midpoint-constrained to the
rectangle's short edges, all four sides dimensioned. Dragging the left circle slid the entire mouth
sideways as one rigid body: the shape was solved, but nothing tied it to the origin. Selecting the
origin and the rectangle's centre point and pressing `v` for vertical fixed it, and the sketch went
fully defined.

So the test for a sketch is a tug, not a colour. Pick one entity and drag it. If the whole thing
moves together, the missing constraint is where the sketch sits, not what shape it is.

### Overlapping circles and a rectangle make five regions, not three

`Mouth profile`'s two Ø4 circles have exactly the same diameter as the rectangle's 4 mm height, so
each circle passes through two of the rectangle's corners and the sketch has **five** faces: the
rectangle's middle, the two outer half-discs, and two inner half-discs where circle and rectangle
overlap. Picking the obvious three gave

> Mouth [Extrude] did not regenerate properly: Boolean operation would result in non-manifold body.

Adding the two inner half-discs cleared it. When a Remove complains about non-manifold, count the
regions on screen before doubting the direction — hover each patch and watch which one lights up.

### `Direction` is a reference field; the flip lives beside `Blind`

The first guess at the non-manifold error was that the cut ran the wrong way, so the Extrude
dialog's **Direction** tick box got ticked. It is not a reverse switch — it opens an *Extrude
direction* field wanting a line or axis to extrude along. What turns a cut around is the small
arrow to the right of the end-condition dropdown, the one whose tooltip reads *Opposite
direction*, and flipping the mouth with it gave *Selected tools and targets do not intersect* —
which is the proof the original direction was already into the head.

### Constraint shortcuts are printed in the constraints flyout

`m` does nothing for midpoint. The arrow at the right of the sketch toolbar's constraints group
opens a list with every constraint and its key beside it: coincident `i`, concentric `shift o`,
parallel `b`, tangent `t`, horizontal `h`, vertical `v`, perpendicular `shift l`, equal `e`,
**midpoint `shift m`**, normal `shift k`, pierce `shift g`, symmetric `shift q`, fix `shift j`,
curvature `shift u`. Open the flyout once and read them off rather than guessing letters.

### The Bottom view: `Shift` and the up arrow from Front

The View menu has no orthographic entries at all — Isometric, Dimetric and Trimetric, and nothing
else. The view cube's tilt arrows above and below it came back to Front from every starting point
tried. What works every time is to click the cube's **Front** label and then press
**`Shift` + ↑** with the pointer over the graphics area: one quarter turn, square on the underside,
+x to the right and +y down the screen. `n` is not *view normal to* in this build; it lands on
Bottom whatever the sketch plane is.

### Fill a dialog field by its label, not by remembered pixels

Picking a feature into `Circular pattern`'s first field pushes every row below it down, so a click
aimed at where `Angle` used to be lands on the graphics area instead — which closes the dialog and
leaves a red row in the tree. Worse, the `Meta+A` that clears a field then selects the whole page.
Find the input on the row whose label reads `angle`, and click that. Same for the dropdown at the
top: it opens from its arrow, not from the middle of the box.

### Deriving the cavity from the ball-and-socket was tried, and dropped

The head's socket is the same r3.2 cup as [phase 3](#phase-3--the-ball-and-socket)'s, so the first
route was **Derived**, pulling that geometry across from `ball-socket-run61`. Three things about
that tool are worth having written down: it is called `Derived`, not *derive*, so a search for the
short word finds nothing; the search result does not arm it, and the row inside the toolbar flyout
does, after about nine seconds; and in its document picker `Escape` closes the whole dialog and
`Enter` commits it, so the search box has to be clicked before anything is typed.

It was dropped in favour of a native Revolve, which is what the torso's studs and run 5.1's head
both use. Phase 3 measured that cavity at 109.482 mm³ — the r3.2 sphere less the cap above the rim
— so the stalk that comes with a derived part removes nothing a revolved half-disc does not.
`Cavity from ball` then removed 109.48 mm³, which closes the argument.

### Shell survives the cavity, and offsets it outward

`Head shell` at 1.2 leaves the socket as a 1.2 mm dome: the r3.2 cup keeps its face, and a second
sphere appears at **r 4.4000** about the same centre, with the collar's inside at r 3.5000 above
it. That is the brief's own prediction from run 3, and it is what the model does. The four collar
fingers went red in the preview at Shell's default 2.5 and clear at 1.2.

### Looked at

Isometric shows the face — two proud oval eyes and the slot mouth — with the arc running smoothly
into the two sides and no crease at the join. Tilted one quarter turn further it shows the
underside: the collar's four fingers, the two 0.8 slits crossing at the axis, and the cup of the
socket between them. From the back the shell's opening runs the whole height, and the eye and
mouth pockets read as raised patches on the inside of the front wall.

## Phase 4 — the socket-clevis limb

**Where the work is.** `limb-socket-clevis-run6`, document `99c49282225f3a7392b2d56b`, Part Studio
`da5a7f06c1ff110098bdafb9` — ids in [`run6-documents.json`](run6-documents.json). Version
**`limb-socket-clevis-run6-2026-08-15`** (`6f362f52291d44e89d84e193`) —
[open](https://cad.onshape.com/documents/99c49282225f3a7392b2d56b/v/6f362f52291d44e89d84e193/e/da5a7f06c1ff110098bdafb9).

**The ball's centre is the origin.** Everything on this limb is dimensioned from there: the socket
mouth is 1.350 above it, the collar's root — the top of the barrel — is 4.150 below it, the hinge
axis is 24 below it, and the slot stops 13 below it. Put the socket on the origin first and the
fork end costs two sketches with no arithmetic in either.

**Built to [`limbs.md`](../../build-briefs/limbs.md)**, socket end first, fork end second.

| Tree row | What it is |
| -------- | ---------- |
| `Limb circle` | Top-plane sketch: Ø12 on the origin |
| `Limb stock` | Extrude, **New**, Blind 25.85 downward, start offset 4.15 downward — the barrel runs z −4.150 to −30.000 |
| `Collar circle` | Sketch on the barrel's top face: Ø9.4 on the origin |
| `Collar blank` | Extrude, **Add**, Blind 5.5 — the collar stands up to z +1.350 |
| `Cavity profile` | Front-plane sketch: Ø6.4 circle on the origin, with a vertical line down its middle for the axis |
| `Cavity from ball` | Revolve, **Remove**, 30° forward and 330° back — a full turn — **Merge with all** |
| `Slit profile` | Sketch on the collar's rim face: centre-point rectangle on the origin, 0.8 across and 12 long, so it runs clear past the collar both ways |
| `Slit pair` | Extrude, **Remove**, Blind 5.5 — one rectangle through the middle makes two slits |
| `Second slit pair` | Circular pattern, **Feature pattern**, `Slit pair`, 90° and 2, Equal spacing, **Reapply features** |
| `Round end profile` | Front-plane sketch: Ø12 circle on the hinge axis 24 below the origin, and a 20 × 8 centre-point rectangle hanging below it with its top edge through that axis |
| `Fork round end` | Extrude, **Remove**, Through all, Symmetric — the one region inside the rectangle and outside the circle |
| `Slot profile` | Right-plane sketch: centre-point rectangle 5.6 across and 21 long, its top edge 13 below the origin and its bottom edge out past the tip |
| `Fork slot` | Extrude, **Remove**, Through all, Symmetric |
| `Stub circle` | Sketch on the ear's inside wall: the round end's arc brought in with **Use**, and a Ø2 circle **Concentric** to it |
| `Ear stub` | Extrude, **Add**, Blind 0.8 — the stub grows off the wall into the slot |
| `Tooth circle` | Sketch on the same wall: the round end's arc used again, and a Ø0.8 circle 4.8 from its centre, held there by a **Vertical** to the arc's centre point |
| `Ear tooth` | Extrude, **Add**, Blind 0.6 |
| `Tooth crown` | Fillet, radius 0.4, on the tooth's end face |
| `Tooth ring` | Circular pattern, **Feature pattern**, `Ear tooth` and `Tooth crown`, axis `Face of Ear stub`, 360° and 24, Equal spacing |
| `Second ear` | Mirror, **Feature mirror**, `Ear stub` `Ear tooth` `Tooth crown` `Tooth ring`, Front plane |

Parts: `limb-socket-clevis`.

### Measured — the socket-clevis limb

Read off the model through `bodydetails`, `massproperties`, `tessellatedfaces` and
`tessellatededges`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| barrel | cylinder r 6.0000 about the z axis, z −30.0000..−4.1500 | Ø12, 25.850 long |
| collar | cylinder r 4.7000, z −4.1500..+1.3500, in four pieces | Ø9.400, standing 5.500 proud |
| socket | sphere r 3.2000 centred on the origin, in four pieces | Ø6.400 |
| cavity volume | 3305.2539 − 3195.7719 = **109.4820 mm³** | 109.48 |
| socket mouth | edges on the z +1.3500 face: nearest the axis 2.9013, furthest 4.7000 → **Ø5.8026** | Ø5.803 |
| collar wall | 4.7000 − 3.2000 = **1.5000** | 1.500 |
| slits | eight walls at x ±0.4000 or y ±0.4000, every one z −4.1500..+1.3500 | 0.800 wide, the collar's whole 5.500 |
| slits into the bore | the sphere's four pieces are cut off at x, y = ±0.4000 and bottom out at z −3.1496 | the slits open into the ball bore |
| segment | ball centre z 0.0000 to hinge axis z −24.0000 | 24.000 |
| hinge axis | the two stub cylinders r 1.0000 run z −25.0000..−23.0000 | centred on z −24 |
| round end | cylinder r 6.0000 about the hinge axis, x −5.3066..+5.3066, z −30.0000..−26.8000, one on each ear | r6 about the hinge axis |
| slot | ear inner faces at y −2.8000 and +2.8000 | 5.600 |
| ears | y −6.0000..−2.8000 and +2.8000..+6.0000 | 3.200 each |
| slot root | plane at z −13.0000, 64.6743 mm² | 13 below the ball's middle, 11 behind the axis |
| ear taper | the inner faces run x −5.3066..+5.3066 | the 10.613 chord — the ear goes to nothing at each end |
| stubs | two cylinders r 1.0000, y 2.0000..2.8000 and −2.8000..−2.0000 | Ø2 standing 0.800 into the slot |
| teeth | 48 cylinder faces r 0.4000 and 48 sphere faces r 0.4000 | 24 on each ear, every one crowned |
| tooth ring | tooth centres 4.8000 from the hinge axis | 4.8 |
| furthest from the limb's axis | **r 6.0000**, over 411,060 tessellated surface points | nothing outside Ø12 |
| `limb-socket-clevis` volume | 2041.9142 mm³ | |
| Parts | 1 | 1 |

The brief asks for a thinnest wall, and on this limb the honest answer is two numbers, not one. The
collar's wall is 1.500 all round, which is what run 3 measured. The ears are a different story: they
are bounded by the round end's cylinder on one side and their own flat inner face on the other, and
those two surfaces meet tangentially at x = ±5.3066, so the ear goes to zero there. That is the
brief's own prediction, and the model agrees with it exactly.

The teeth check out arithmetically at every step, which is the cheapest confirmation there is that
the pattern and the mirror did what they look like they did. One bare tooth is 0.30159 mm³ = π ×
0.4² × 0.6. Crowning it takes off 0.06702, the difference between a 0.4 cylinder and a 0.4
hemisphere, leaving 0.23457 per finished tooth. `Tooth ring` adds 5.39516 = 23 × 0.23457, and
`Second ear` adds 5.62973 = 24 × 0.23457 for the far ear's teeth plus 2.51327 = π × 1² × 0.8 for its
stub. 2028.1415 → 2041.9142, with nothing left over.

### `Use` takes the curve, and the curve brings its centre with it

The ear's inside wall is a flat face with no circle drawn on it, but the hinge axis has to be found
on it twice — once for the stub and once for the ring of teeth. Press **`u`** with the round end's
edge under the pointer and Onshape drops a copy of that arc into the sketch, **and its centre point
with it**. That point is the hinge axis, exactly, for free.

Click the curve where it is plainly curving — a step or two round from the bottom of the arc. Right
at the tangent point the vertex is the nearer target, and a projected vertex has no centre to offer.
With the arc in, the stub is a circle **Concentric** to it and the tooth is a circle held
**Vertical** to its centre and dimensioned 4.8 away. Neither needs a number typed for position.

### The rectangle reaches past the bottom of the circle, so the cut is one region

`Round end profile` is a Ø12 circle on the hinge axis and a 20 × 8 rectangle hanging below it. The
rectangle's top edge runs through the circle's centre and its bottom edge sits at z −32, two below
the end of the barrel. That puts the whole bottom of the circle inside the rectangle, so the area
inside the rectangle and outside the circle wraps around underneath in **one connected region** —
one click, one chip, and the tip comes out round and symmetric.

Make the rectangle stop short of the circle's bottom and the same shape becomes two separate corner
regions that both have to be picked. Reaching past is the simpler sketch.

### An `Add` that ends exactly on a face does not join it

The stub was drawn first on the Front plane — the plane down the middle of the slot — and extruded
symmetrically out to the two ear walls, with `Merge with all` ticked. The extrude ran green and the
volume did not change: its two end faces landed exactly on the ear faces, and coincident is not
overlapping.

Sketch on the face the feature grows from and extrude **away** from it, and there is nothing to
merge — the material is continuous from the first millimetre. `Ear stub` is 0.8 off the ear's inside
wall into the slot, and `Ear tooth` is 0.6 off that same wall.

### When the region will not pick, hand the extrude the sketch row

`Tooth circle` and `Stub circle` both lie flat on the ear's wall, and the region inside the little
circle is the same colour, the same plane and the same place as the solid behind it — the click
lands on the face and the extrude fills up with `Face of Fork slot`. Hiding the part does not help
here the way it does for [a sketch buried inside a solid](#a-sketch-inside-a-solid-cannot-be-picked-so-hide-the-solid-first),
because the sketch is on the solid.

Open the extrude, then click the **sketch's own row in the feature list**. Onshape takes the whole
sketch as the region set, the preview appears, and the chip reads `Sketch region of Tooth circle`.
It is the quickest way in whenever the region is small or flush.

### A graphics pick with no field focused joins the list above

`Circular pattern` opens with `Features` already focused, so the first thing clicked in the graphics
area goes into the features list — including the face meant for `Axis of pattern`. The dialog reads
`Ear stub` twice and previews nothing useful.

Click **into** the axis field first and the same face lands where it belongs. If one has already
gone astray, the **×** at the right-hand end of the chip takes it back out. This is the same habit
[the mirror's plane field wants](#the-mirror-plane-took-because-the-plane-field-was-clicked-first),
and it is worth making automatic: focus the field, then pick.

### Right-drag turns the part, middle-drag slides it

Driving the view from a script needs no toolbar. **Right-drag rotates**, at about 0.75° per pixel,
and **middle-drag pans**. `pg.mouse.wheel(0, -120)` zooms in about 5% a call.

That is what makes the next one possible.

### The teeth face into the slot, so look in through the open side

Head-on to the ear, the teeth are behind their own ear and nothing shows. The rule that explains it:
sketch entities draw on top of solids, but solid features do not — a bump on the far side of a wall
is simply hidden.

Turn the part until the slot's open x side is facing you and look straight down into it. About 120 px
of right-drag from isometric is enough, and then the stub and the whole ring of teeth are in plain
view on the ear's inner wall.

### `Roll to here` lands after the feature, and the bar carries `Roll to end`

Weighing a feature by rolling back is the cleanest way to measure what it removed. Right-click the
feature's row → **Roll to here**, and the tree stops *after* that feature. So `Cavity from ball`
rolled to gives 3195.7719 and `Collar blank` rolled to gives 3305.2539, and the cavity is the
difference.

Coming back is the part worth writing down: a rolled-back feature's own row has no menu. The
**rollback bar** itself is a row in the tree — the blank one at the boundary — and right-clicking
*that* offers **Roll to end**.

### Versions live on the top icon of the left rail

`Create version` is not in the `Main` label beside the document name and not in the document's ☰
menu. The **top icon of the left rail** opens **Versions and history**, and the panel's own
create-version button is the one that opens the dialog. Name it, click **Create**, and the version
appears in the history graph under `Main`.

### Ø12 is checked by walking the surface, not by the bounding box

`limbs.md` asks that nothing sticks outside Ø12, and says a bounding box cannot answer it — a box
around this limb is 12 × 12 in x and y whether or not a tooth pokes out.

`GET .../tessellatedfaces?chordTolerance=0.00001` returns every facet of every face as points in
metres. Walking all 411,060 of them and taking `hypot(x, y)` gives a furthest radius of **6.0000**,
on the barrel at z −4.150. That is a direct answer over the whole surface, and it takes one call.
The reply is a **dict** with a `bodies` key, not a list; `tessellatededges` is the same shape and
gave the socket mouth the same way.

### Looked at

From isometric the limb reads as three things stacked: the collar at the top with its four fingers
and the two 0.8 slits crossing at the axis, the cup of the socket sitting between them; the plain
Ø12 barrel down the middle; and the fork at the bottom, its slot open toward the viewer with the
ring of teeth showing on the ear's inner wall and the tip rounded off about the hinge axis. Turned
to look straight into the slot, all 24 teeth on the near ear come up as a ring of even beads around
the stub, with the far ear's ring behind them.

## Phase 4 — the blade-ball limb

**Where the work is.** `limb-blade-ball-run6`, document `80a7c10c524313e8e741ebfd`, Part Studio
`bcbdca920469776909b1138b` — ids in [`run6-documents.json`](run6-documents.json). Version
**`limb-blade-ball-run6-2026-08-15-2`** (`6adf73417e7b344c74c03fed`) —
[open](https://cad.onshape.com/documents/80a7c10c524313e8e741ebfd/v/6adf73417e7b344c74c03fed/e/bcbdca920469776909b1138b).
The earlier version of the same day, `limb-blade-ball-run6-2026-08-15`, holds the slit as it was
first built; cite the `-2`.

**The hinge axis is the origin.** The blade's round end turns about it, the pocket and the ring of
valleys are concentric with it, and the ball's centre is 24 below it. Start the blade on the origin
and every later feature has something to be concentric or vertical to, so the only numbers typed
are the ones the briefs give.

**Built to [`limbs.md`](../../build-briefs/limbs.md) and
[`hinge.md`](../../build-briefs/hinge.md)**, blade end first, ball end second.

| Tree row | What it is |
| -------- | ---------- |
| `Blade profile` | Front-plane sketch: Ø12 circle on the origin, and a 12-wide rectangle hanging below it to z −10 |
| `Blade blank` | Extrude, **New**, Blind 5, **Symmetric** — the blade lands y −2.500 to +2.500 with no offset typed |
| `Limb section` | Top-plane sketch: Ø12 on the origin |
| `Trim blade to limb` | Extrude, **Intersect**, Through all, Symmetric — takes the blade's corners back onto the Ø12 surface |
| `Limb` | Extrude, **Add**, Blind 10 downward, on the same `Limb section` region — the round part of the limb, z −10 to −20 |
| `Ball stud profile` | Front-plane sketch: Ø6 circle 24 below the origin with a line closing it, and the stalk running up to 19 below the origin, one inside the limb |
| `Ball stud` | Revolve, **Add**, 30° forward and 330° back — a full turn |
| `Pocket circle` | Sketch on the blade's outer face: the round end's arc brought in with **Use**, and a Ø2.2 circle **Concentric** to it |
| `Pocket` | Extrude, **Remove**, Blind 1 |
| `Detent valley circle` | Sketch on the same face: the arc used again, and a Ø1.0 circle 4.8 from its centre, held on the blade's middle by a **Vertical** to that centre |
| `Detent valley` | Extrude, **Remove**, Blind 0.45 |
| `Break the valley rim` | Fillet, radius 0.1, on the valley's rim |
| `24 detent valleys` | Circular pattern, **Feature pattern**, `Detent valley` and `Break the valley rim`, axis `Edge of Pocket`, 360° and 24, Equal spacing, **Reapply features** |
| `Mirror the joint face` | Mirror, **Feature mirror**, `Pocket` `Detent valley` `Break the valley rim` `24 detent valleys`, Front plane, **Reapply features** |
| `Slit profile` | Right-plane sketch: centre-point rectangle on the origin, 0.8 across and 20 long, so its root lands 10 below the origin and its far end runs out past the blade |
| `Slit` | Extrude, **Remove**, Through all, **Symmetric** |

Parts: `limb-blade-ball`.

### Measured — the blade-ball limb

Read off the model through `bodydetails`, `massproperties`, `features` and `tessellatedfaces`, not
inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| blade | planes at y −2.5000 and +2.5000, 132.8551 mm² each | 5.000 thick |
| chord | those faces run x −5.4544..+5.4544, and √(36 − 6.25) is 5.4544 | 10.909 |
| round end | cylinder r 6.0000 about the hinge axis | r6 about the hinge axis |
| segment | hinge axis z 0.0000 to ball centre z −24.0000 | 24.000 |
| limb | cylinder r 6.0000 about the z axis | Ø12 |
| ball | sphere r 3.0000 centred (0.0000, 0.0000, −24.0000) | Ø6 at the far end of the segment |
| stalk | cylinder r 1.5000, z −21.4019..−20.0000 | Ø3 running into the limb |
| slit | walls at y −0.4000 and +0.4000, both z −10.0000..+6.0000 | 0.800 wide, 16 deep |
| slit root | plane at z −10.0000, 9.5929 mm² | the slit stops 10 below the hinge axis |
| tabs | 2.5000 − 0.4000 = **2.1000** each, free over the slit's whole 16 | 2.1 |
| pockets | two cylinders r 1.1000, y −2.5000..−1.5000 and +1.5000..+2.5000 | Ø2.2 × 1.0 in each face |
| behind a pocket | 1.5000 − 0.4000 = **1.1000** | 1.1 |
| valleys | 48 cylinders r 0.5000, floors at y −2.0500 and +2.0500 | Ø1.0 × 0.45, 24 a side |
| valley ring | every centre 4.8000 from the hinge axis, 15.000° apart | r4.80 at 15° |
| rim break | 48 torus faces, 0.5293 mm² each, y ±2.4000..±2.5000 | r0.10 |
| land between valleys | centres 1.2531 apart → 0.2531 of land, 0.0531 after the break | 0.2530, and 0.053 broken |
| rim outboard of the ring | 6.0000 − 4.8000 − 0.5000 = 0.7000, and 0.6000 after the break | 0.70 before, 0.60 after |
| furthest from the limb's axis | **r 6.0000**, over 434,274 tessellated surface points | nothing outside Ø12 |
| symmetry | all 161 faces map onto themselves reflected in Front, and again in Right | not handed |
| `limb-blade-ball` volume | 1949.1024 mm³ | |
| Parts | 1 | 1 |

The part closes arithmetically end to end. Before either joint face was cut it measured
**1974.0077**, against a closed form of 1974.0076 — blade 862.6482 plus rod π × 36 × 10 = 1130.9734
plus ball 121.5524 less slit 141.1664. The ball term is the one worth writing down, because the
stalk and the sphere share a spherical cap: the stalk meets the ball where the ball is 1.5 across,
at z −21.4019, so the cap is h = 3 − 3√3/2 = 0.4019 tall and π h² (9 − h) / 3 has to come off or it
is counted twice.

Each joint face then takes **12.452662** — a pocket at π × 1.1² × 1.0 = 3.801327, and 24 valleys at
0.360472 apiece. A valley is its bore, π × 0.5² × 0.45 = 0.353429, plus what the r0.10 break flares
off the mouth, π ∫₀^0.1 (r(u)² − 0.25) du with r(u) = 0.6 − √(0.01 − u²), which is 0.007043. Two
faces take 24.905323, and 1974.0077 − 24.9053 is 1949.1024 — the measured volume, to four decimals.

### The thinnest places on this limb are two rims, and they are the same size

[The land between neighbouring valleys](#the-land-between-valleys-is-00531-mm-and-run-3s-number-reproduces)
is 0.0531 here as well. This part adds a second rim of the same order that the hinge on its own
could not show: the ring puts a valley at every 15°, so two of them sit at ±90° from the top, right
where the blade's flank cuts the Ø12 cylinder. The blade's face reaches x 5.4544 there and the
broken valley mouth reaches 5.4000, leaving **0.0544**.

Both are rims — an edge of a face, with material behind them. The thinnest actual wall is still the
1.10 behind a pocket floor. Nothing needs changing: the ring's clocking comes from the brief's
15° and the flank comes from the Ø12 rule, and 0.0544 is the number those two produce when they
meet.

### The joint face is the outside of the blade, not the inside of the slit

The pocket and the valley ring went on a slit wall first. It looks right — the slit is where the
clevis's ears go — but the ears carry their teeth on *their* inner walls, so the two rings would
have faced each other across the tab instead of meshing with it. The mating surface is the blade's
**outer** face, y ±2.5.

The fix is worth more than the mistake. Sketching on the outer face puts the sketch plane exactly
where the feature starts, so the pocket is `Remove, Blind 1` with nothing else set, and the depth
that comes out is the depth that was typed.

### A starting offset on a Remove is what the plan warned about, and the slit proved it

The slit was first cut from the Top plane with **Through all** and a starting offset of 10. The
offset runs opposite to the extrude by default, so the step needed a second flip and a look to
confirm it had gone up rather than down — exactly the sentence [`plan.md`](plan.md) says a written
step must never have to contain.

Rebuilt, it is a **Right-plane** sketch of the slit seen side on: a centre-point rectangle on the
origin, 0.8 across and 20 long. Twenty long centred on the origin puts the root at z −10 by
construction and runs the far end out past the blade's top, so there is nothing to bound and
nothing to offset. `Remove, Through all, Symmetric` then cuts both ways from that plane and the
direction question does not arise. The volume came back to 1949.1024 and every slit face landed on
the same numbers, which is how you know a rebuild is a rebuild and not a new shape.

Same shape of answer as the socket-clevis's `Slot profile`. When a slot has to start inside the
part, sketch its side view on the plane it straddles.

### Four limbs, two parts holds, and the model can say why

[`limbs.md`](../../build-briefs/limbs.md) asks for this to be reported before anything else is
decided. With both limbs now built from empty documents, the measurement is in:

**Neither part is handed.** All 161 of this part's faces map onto themselves reflected in Front,
and again reflected in Right. The 24 × 15° ring maps onto itself because 24 is even and the ring
carries a valley at every multiple of 15° from the blade's centre line. Put the same test to
`limb-socket-clevis` and all 127 of its faces do it too — the collar's four slits cross on the axis
and its ring of teeth is the ring this one meshes with. So one printed `limb-blade-ball` serves as
a forearm or a shin, left or right, and one printed `limb-socket-clevis` serves as an upper arm or
a thigh.

That makes six unique parts for the robot rather than eight, and it is a bill-of-materials change,
so it stays a report. The load argument the brief raises — a shin carries weight and a forearm does
not — is still not something measurement settles.

### A full circle and a closing line revolves as happily as an arc

`hinge.md` draws the ball as a half-circle arc on the axis. A whole Ø6 circle with a single line
down the axis works just as well and is easier to place: the circle takes a diameter dimension and
a distance from the origin, the line takes the axis, and the revolve consumes the region between
them. There is no half-arc endpoint to snap and nothing to trim.

### Ask whether a dialog is open, and click the tick until it is not

`.feature-dialog` is the element that says a feature dialog is on screen. The tick at the top of
the dialog frequently needs **two** clicks — the first is eaten when the focus is still in a field
that was just typed into — and a rename attempted against a still-open dialog fails with no useful
message. Clicking the tick in a loop until `.feature-dialog` has gone makes both problems
disappear:

```python
def take(pg, st, tries=3):
    for _ in range(tries):
        if not pg.evaluate("() => !!document.querySelector('.feature-dialog')"):
            return
        st.click(424, 93, "the green tick")
        pg.wait_for_timeout(2600)
```

`.dialog-title-text` and `.os-dialog-title` do not exist in this build and quietly answer *no
dialog* forever.

### A decimal below one loses its point if it is typed at speed

`0.1` typed into the fillet's radius came out as `01`, and the fillet built at 1 mm. Typing it a
character at a time with `pg.keyboard.type("0.1", delay=180)` and reading the field back before
accepting is what makes it stick. This is the same habit as
[filling a field by its label](#fill-a-dialog-field-by-its-label-not-by-remembered-pixels): put the
value in, then ask the field what it says.

### A torus area measures a fillet radius exactly

The rim break's face reports 0.5293 mm². A fillet on a round mouth is a torus, and for one that
flares outward the ring's own radius runs ρ(θ) = R − r cos θ, so the area is
2π r ∫₀^{π/2} (R − r cos θ) dθ with R = 0.5 + r. At r 0.10 that is 0.52935. Getting the sign of the
cosine wrong gives 0.55636 and looks like a modelling error; the closed form is the check, and it
confirmed every one of the 48 breaks is a true r0.10 without a single dimension being opened.

### Looked at

From isometric the limb reads as a paddle: the blade at the top with its ring of 24 valleys sunk
into the near face and the pocket at the middle of the ring, the shoulders where the blade's 5
narrows onto the Ø12 rod, the plain rod below it, and the ball on its short stalk at the bottom.
Square on to the joint face the ring is even all the way round, each valley's broken rim a fine
bright circle inside it, and the two valleys at the sides sit right up against the blade's straight
flank. The slit does not show from the front — it is internal, opening only at the blade's round
end — which is the right answer for a slot that is 0.8 wide in a 5.0 blade.

## Phase 4 — the gripper

**Where the work is.** `hand-run6`, document `8887c2fc2657197fce7057c5`, Part Studio
`96e1f40644cfe1ce9bc50181` — ids in [`run6-documents.json`](run6-documents.json). Version
**`hand-run6-2026-08-15`** (`6f4f1d9a8c70581028b4d122`) —
[open](https://cad.onshape.com/documents/8887c2fc2657197fce7057c5/v/6f4f1d9a8c70581028b4d122/e/96e1f40644cfe1ce9bc50181).

**The wrist centre is the origin.** The socket's mouth is 1.350 above it, the collar's foot 4.150
below it, the clip's centre 7 below it and the bottom of the part 12 below it. Every dimension on
the gripper is one of those four numbers or the brief's own, and nothing is measured from anything
that moves.

**Built to [`gripper.md`](../../build-briefs/gripper.md) and
[`ball-and-socket.md`](../../build-briefs/ball-and-socket.md)**, clip first, socket second.

| Tree row | What it is |
| -------- | ---------- |
| `Clip profile` | Right-plane sketch: Ø10 and Ø3.3 held **Concentric** 7 below the origin, two horizontal lips 2.6 apart, trimmed to a C that opens +Y |
| `Clip` | Extrude, **New**, Blind 6, **Symmetric** — the clip lands x −3.000 to +3.000 with no offset typed. Part named `Gripper` |
| `Collar circle` | Top-plane sketch: Ø9.4 on the origin |
| `Collar` | Extrude, **Add**, Blind 1.35 up and a second end position Blind 4.15 down — the collar runs z −4.150 to +1.350 and lands inside the clip's crown, so the two are one solid with no blending feature |
| `Ball profile` | Front-plane sketch: Ø6 circle on the origin with a line down its middle, held on the axis by a **Coincident** to the `Origin` row |
| `Ball` | Revolve, **New**, 30° forward and 330° back — a full turn |
| `Wrist cavity from the ball` | Boolean, **Subtract**, tool `Ball`, target `Gripper`, **Offset** and **Offset all** at 0.2, `Keep tools` clear |
| `Slit profile` | Sketch on the collar's rim face: centre-point rectangle on the origin, 0.8 across and 12 long, so it runs clear past the collar both ways |
| `Slit` | Extrude, **Remove**, Blind 5.5 downward — one rectangle through the middle makes two slits |
| `Four slits` | Circular pattern, **Feature pattern**, `Slit`, axis `Face of Collar`, 90° and 2, Equal spacing, **Reapply features** |

Parts: `Gripper`.

### Measured — the gripper

Read off the model through `bodydetails`, `boundingboxes` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| clip bore | cylinder r 1.6500 at (3.0000, 0.0000, −7.0000), axis (−1, 0, 0) | Ø3.300, axis along X |
| clip outer | cylinder r 5.0000 about that same axis | Ø10.000 |
| mouth | lip planes at z −5.7000 and z −8.3000, 22.8715 mm² each | 2.600 at its narrowest |
| mouth, both sides | both lips run y 1.0161 to 4.8280 | the trim took the same arc on each side |
| clip length | planes at x −3.0000 and +3.0000, 48.8375 mm² each | 6.000, centred on Right |
| gripper length | z +1.3500 down to z −12.0000 | 12.000 from the wrist centre to the lowest point |
| collar | four cylinder faces r 4.7000 about the z axis | Ø9.400, cut into four tabs |
| cavity | four sphere faces r 3.2000 centred (0.0000, 0.0000, 0.0000) | r3.200 |
| cavity volume | 672.9889 before the subtract, 563.5069 after → **109.4820 mm³** | 109.48, and not 27.78 |
| mouth | four arcs r 2.9013 at z +1.3500 | Ø5.803, four arcs |
| grip face | four rim faces at z +1.3500, 9.2966 mm² each, all material below | 1.350 above the wrist centre |
| slits | walls at x ±0.4000 and y ±0.4000, floors at z −4.1500 | 0.800 wide |
| slit depth | +1.3500 − (−4.1500) = **5.5000** | 5.5, the collar's whole length |
| collar bottom edge | eight arcs r 4.7000 at z −4.1500 | eight, which is this part's stated exception |
| collar step | collar r4.7000 against the clip's x ±3.0000 and its y r5.0000 | irregular: 1.700 in x, nothing in y |
| thinnest wall | 4.7000 − 3.2000 = **1.5000**, at the socket collar | 1.500 |
| symmetry | all 36 face boxes land on themselves reflected in x, and do not reflected in y | symmetric left-right, handed front-back |
| `Gripper` volume | 520.4792 mm³ | |
| Parts | 1 | 1 |

The rim tab's 9.2966 mm² is the number worth writing down, because it closes the whole top of the
part in one line. The annulus is π (4.7² − 2.9013²) = 42.9538. A slit is the strip |y| < 0.4, and
the area of that strip inside a circle of radius R is 2 [0.4 √(R² − 0.16) + R² asin(0.4 / R)] —
7.5109 at R 4.7 and 4.6276 at the mouth's 2.9013, so each slit takes 2.8833 out of the annulus.
Two slits cross at the centre but the crossing sits inside the mouth, so nothing is double counted:
42.9538 − 2 × 2.8833 = 37.1872, and a quarter of that is **9.2968** against the measured 9.2966.
Collar diameter, cavity radius, grip height, slit width and slit count all appear in that one
arithmetic, and all five have to be right for it to land.

The slits took 43.0277 mm³ out — 563.5069 before, 520.4792 after.

### What put the clip's centre 7 below the wrist

`gripper.md` leaves the clip's centre open and asks what drove it. The clip's outer radius is 5 and
the bottom of the gripper is 12 below the wrist centre, so the centre goes at 12 − 5 = **7**, and
there is nothing else to choose. The consequence is worth having: the clip's crown then reaches
z −2.000, which is 2.150 above the collar's foot at −4.150, so the collar grows down *into* the
clip and the `Add` extrude leaves one solid. Step 6 of the brief's build order — blend the clip into
the socket body — needs no feature of its own on these numbers.

The same arithmetic says what a bigger clip would cost. At Ø12 the centre moves to z −6 and the
crown to z 0, which is above the collar's foot and above the cavity's equator, so the clip would
start eating the socket rather than sitting under it.

### What Sketch trim removes when an arc is crossed twice

The brief asks for this one exactly, so here it is. **Trim works on the piece under the cursor,
bounded by the nearest crossing on either side** — not on the entity you clicked and not on the
whole arc.

Each circle in the clip profile is crossed twice by the lips, so each becomes exactly two arcs: a
short one spanning the mouth and a long one going the other way round. Hovering the short one lights
just that piece in orange, from one lip to the other
([`shots/p4-gr-56-a-outer-arc-between-the-lips-hovering-outer-arc-between-the-lips.png`](shots/p4-gr-56-a-outer-arc-between-the-lips-hovering-outer-arc-between-the-lips.png)),
and one click takes it. Each lip line is crossed once by the outer circle, so it splits into two
pieces as well and the stub beyond the circle lights on its own. Four clicks — two arcs and two
stubs — turn two circles and two lines into a C.

So the rule at the point of use is: **hover first and look at what lights up.** The highlight is
the answer to "what will this click remove", and it is shown before anything is removed.

### Trim goes back to sleep after every cut

The first cut lands and the next one raises *Could not trim this selected entity*, with no
highlight on hover. Pressing `Escape` and then `m` before **every single cut** makes all four land:

```python
for x, y in CUTS:
    pg.keyboard.press("Escape"); pg.wait_for_timeout(600)
    pg.keyboard.press("m");      pg.wait_for_timeout(1200)
    assert gr.tool_active(pg, "sketch-trim-button")
    pg.mouse.move(600, 800); pg.wait_for_timeout(300)   # somewhere empty first
    pg.mouse.move(x, y);     pg.wait_for_timeout(1400)  # then onto the piece
```

The move through empty space matters as much as the re-arm: the highlight is computed on movement,
and a jump straight from one arc to the next can arrive with nothing lit.

### A plane cannot be projected into a sketch, and cannot be constrained to one

The ball's revolve needs a line on the axis. Three ways of getting one do not work, and the sketch
looks finished after all three:

- `u` on the `Right` plane answers *Could not project the selected entities into the current
  sketch*. A plane is not a projectable entity.
- Picking the plane and the line together and pressing `i` does nothing at all — no constraint, no
  message. The line stays blue.
- The vertical line drawn "on" the axis by eye measured **Parallel dist: 0.02840 mm** off it in the
  status bar, which is what a revolve about it would have built.

What works is a point: draw the line clearly off the axis, click the **`Origin` row in the feature
tree**, shift-click the line in the graphics area, and press `i`. The line snaps onto the axis and
the sketch goes black
([`shots/p4-gr-137-b-held-the-line-held-on-the-axis.png`](shots/p4-gr-137-b-held-the-line-held-on-the-axis.png)).
The status bar is the check here — select the line and the axis and read `Parallel dist`; on a held
line it reads 0.

This Onshape has no Sphere primitive to fall back on: searching the toolbar for *Sphere* answers
*No items match your search*.

### The Parts list counts the preview, not the model

Typing `5.5` into a depth and reading the model straight away reports **Parts (3)** — the field
still held the 25 mm it opened with, and 25 mm cuts the gripper into three pieces. Pressing `Enter`
made the same read say **Parts (1)**
([`shots/p4-gr-263-a-set-the-depth-taken-and-the-parts-list.png`](shots/p4-gr-263-a-set-the-depth-taken-and-the-parts-list.png)).

Nothing on screen distinguishes the two states, so commit the field before reading anything —
Parts list, bounding box or volume. The habit that covers it is the same one that
[fills a field by its label](#fill-a-dialog-field-by-its-label-not-by-remembered-pixels): put the
value in, read the field back, and only then ask the model what it is.

### The C-clip is not symmetric front-to-back, and that is the point

Reflecting all 36 face bounding boxes in x lands them on themselves; reflecting them in y does not.
That pair of answers is the whole design idea in
[`gripper.md`](../../build-briefs/gripper.md): the mouth opens forward, so the part is its own
mirror image left-to-right and **one part serves both wrists**. Had the mouth opened outward, the
two answers would have swapped and the robot would need a left gripper and a right one.

The check that catches the near miss is the bore's axis, and it reads **(−1, 0, 0)**. A clip built
on `Front` with its mouth opening down mirrors onto itself in x as well, and passes every other
number on the list, while the robot grips a bar pointing away from itself.

### Looked at

Rendered on its own from isometric, top, front and right —
[`shots/p4-gr-render-isometric.png`](shots/p4-gr-render-isometric.png) and its three companions.

From isometric the gripper reads as a crown on a hook: four collar tabs standing up with the
spherical cup between them, and the C-clip below, its mouth open toward the viewer. The collar does
stand proud, though only in x — from the front it overhangs the clip's 6 by 1.7 a side, and from
the right the clip's Ø10 is the wider of the two and the collar sits inside it. That is the
irregular step the brief said to expect on this part rather than the even 1.3 ring a Ø12 limb gives.

Top-down is where the slits answer for themselves: two 0.8 bands cross at the axis, the four tabs
are four equal quarters, and each band runs from the cup out past the collar's edge, so they are
through-cuts and not surface marks. Front and right show the same bands running the collar's whole
height and stopping at the foot.

The mouth looks like something a ball could be pushed into: the cup's opening is Ø5.803 against a
Ø6 ball, the four tabs are free over their whole 5.5, and the run of the tab from mouth to foot is
smooth. The right view is the clearest picture of the clip — bore, mouth and the two lips — and the
mouth is visibly narrower than the bore, which is the interference that makes it snap.

### Reported back to `gripper.md`

**`#clipR` still has no variables row, and this model does not settle it.** What it does settle is
what the 12 length can carry. Measured: the clip's crown sits at z −2.000 and the collar's foot at
z −4.150, so the two overlap by 2.150 and the slits, which stop at the foot, end 2.150 inside clip
material. Ø10 is the diameter that produces that overlap, because the crown is at 12 − 2 × 5 below
the wrist. The arithmetic — not a build — says Ø12 puts the crown at z 0.000, level with the
cavity's equator and with the 1.500 wall, which is the first diameter at which the clip arrives at
the socket's thinnest section. `gripper.md`'s answered question holds here too: the clip measures
r 5.0000 and the collar r 4.7000, so the collar overhangs nothing.

**The clip's leading edges are square, and the bar meets them face-on.** The lips are planes at
z −5.7000 and z −8.3000 and their edges are 90°. The mouth is 2.600 against a 3.2 bar, so each lip
has to be pushed 0.300 out of the way by an edge whose face is normal to the push. A chamfer would
turn that into a ramp. It is not modelled and not tuned — `gripper.md` calls the interference a
print question, and the chamfer is the same question — but the geometry the print will answer it
against is on record here.

## Phase 4 — the foot

**Where the work is.** `foot-run6`, document `f0fe0b1c973c187888d9386a`, Part Studio
`0b8eaea0e4902a2620b15093` — ids in [`run6-documents.json`](run6-documents.json). Version
**`foot-run6-2026-08-15-2`** (`418e39c06d54804cd87f737a`) —
[open](https://cad.onshape.com/documents/f0fe0b1c973c187888d9386a/v/418e39c06d54804cd87f737a/e/0b8eaea0e4902a2620b15093).
An earlier version, `foot-run6-2026-08-15`, was published before the sole grooves were rebuilt
without a starting offset. `-2` is the one to cite; both hold the same geometry.

**The ankle ball centre is the origin.** The ground is 12 below it, the plate's top face 6 below it
and the socket mouth 1.350 above it. Every dimension on the foot is one of those three numbers or
the brief's own.

**Built to [`foot.md`](../../build-briefs/foot.md) and
[`ball-and-socket.md`](../../build-briefs/ball-and-socket.md)**, outline first, socket second,
ribs last.

| Tree row | What it is |
| -------- | ---------- |
| `Foot outline` | Top-plane sketch: heel circle r8 centred y +8, toe circle r12 centred y −20, both centres on the vertical axis, joined by outer tangent lines |
| `Foot plate` | Extrude, **New**, Blind 6 downward with a **starting offset** of 6, also downward — the plate lands z −12.000 to −6.000. Part named `Foot` |
| `Top round` | Fillet r4 on **one** picked edge, **tangent propagation** on, which rounds the plate's whole top rim |
| `Collar circle` | Top-plane sketch: Ø9.4 on the origin |
| `Ankle collar` | Extrude, **Add**, Blind 7.35 up |
| `Ball profile` | Front-plane sketch: Ø6 circle on the origin with a line down its middle |
| `Ankle ball` | Revolve, **New**, 30° forward and 330° back — a full turn |
| `Ankle cavity from the ball` | Boolean, **Subtract**, tool `Ankle ball`, target `Foot`, **Offset** and **Offset all** at 0.2, `Keep tools` clear |
| `Slit profile` | Sketch on the collar's rim face: centre-point rectangle on the origin, 0.8 across and long enough to run past the collar both ways |
| `Relief slit` | Extrude, **Remove**, Blind 7.35 downward — one rectangle through the middle makes two slits |
| `Four slits` | Circular pattern, **Feature pattern**, `Relief slit`, axis `Face of Ankle collar`, 90° and 2, Equal spacing, **Reapply features** |
| `Groove profile` | Right-plane sketch: centre-point rectangle 3 along the foot by 1 deep, bottom edge 12 below the origin, centre 8 forward of it — four dimensions and it goes black |
| `Sole groove` | Extrude, **Remove**, Blind 30 **Symmetric** — the cut grows both ways from the Right plane, so it covers the sole's 24 and has no direction to get wrong |
| `Sole ribs` | Linear pattern, **Feature pattern**, `Sole groove`, direction `Front plane`, 6 apart, count 4, **Centered**, **Reapply features** |

Parts: `Foot`.

### Measured — the foot

Read off the model through `bodydetails`, `boundingboxes` and `massproperties`, not inferred.

| what | measured | wanted |
| ---- | -------- | ------ |
| bounding box | (−12.0000, −32.0000, −12.0000) to (12.0000, 16.0000, 1.3500) | toe at −Y, heel at +Y |
| width | 24.0000 | 24.000 |
| length | 48.0000 | 48.000 |
| ground | lowest z −12.000, ankle ball centre on the origin | ankle height 12.000 |
| plate | top face at z −6.000, one face, 410.0822 mm² | 6 thick |
| collar | four cylinder faces r 4.7000, 193.5042 mm² together | Ø9.400, cut into four tabs |
| collar rim | four faces at z +1.3500 → **7.3500** above the plate's top | 7.35, not the numbers table's 5.5 |
| cavity | four sphere faces r 3.2000 centred on the origin, 71.5694 mm² | r3.200 |
| cavity volume | 109.4820 mm³ | 109.48, and not 27.78 |
| mouth | four arcs r 2.9013 at z +1.3500 → Ø5.8026 | Ø5.803, four arcs |
| slits | walls at x ±0.4000 and y ±0.4000 | 0.800 wide |
| sole | eight faces at z −12.000, 473.3770 mm² | the ribs stand on the ground |
| groove floors | seven faces at z −11.000, 419.0727 mm² | seven floors, 1 deep |
| ribs removed | 5294.9418 − 4875.8691 = **419.0727 mm³** | run 3's 419.07 |
| one groove alone | 62.3539 mm³ before the pattern | not 72 — the sole is 20.785 wide there, not 24 |
| flat round the collar | 5.1429 − 4.7000 = **0.4429** | run 3's 0.443 |
| thinnest wall | 4.7000 − 3.2000 = **1.5000**, at the socket collar | 1.500, not the plate edge's 2 |
| symmetry | all 58 face boxes land on themselves reflected in x, and do not reflected in y | symmetric left-right, handed front-back |
| `Foot` volume | 4875.8691 mm³ | |
| Parts | 1 | 1 |

### The fillet's own boundary proves the outline is tangent

The check the brief asks for — no corner where an arc meets a line — is readable off the model
without opening the sketch. The plate's top face at z −6.000 is bounded by the r4 fillet's tangent
line, which is the outline offset inward by 4, and its four edges measure: an arc r 4.0000 centred
(0.0000, 8.0000), an arc r 8.0000 centred (0.0000, −20.0000), and two straight lines through
(±3.9590, 8.5714) with direction (0.1428571, −0.9897433).

Both lines sit exactly 4.000009 from the heel arc's centre and 8.000008 from the toe arc's — the
offset boundary is tangent, so the outline it came from is tangent too, and the sketch's own
constraints are not the only witness. Working back out by the 4: **heel r8 at y +8, toe r12 at
y −20.** Those are the two circles, and the tangent lines carry the width from 16 at the heel to 24
at the toe.

The same numbers answer how much flat is left around the socket. The nearest boundary to the collar
is a tangent line, at 3.9590 × 0.9897433 + 8.5714 × 0.1428571 = **5.1429** from the ankle axis, and
the collar's outer radius is 4.7000, so the flat is **0.4429** — run 3's 0.443, measured a second
time on a model built from an empty document.

That taper is also why one groove takes 62.3539 mm³ and not the 3 × 1 × 24 = 72 you would guess.
The sole is 24 wide only across the toe circle; 8 forward of the ankle it is 20.785 wide.

### A Remove that cannot go the wrong way

Phase 4's rule in [`plan.md`](plan.md) is **no starting offsets on a Remove**, so that no step ever
has to say "check it did not go the other way". The first groove was built with one anyway — a
Top-plane sketch, Remove, Blind 1 with a starting offset of 11 — and it went the other way. The cut
landed at z −11.000 to −10.000: a slot buried inside the plate, opening out both sides, with the
sole untouched. Nothing on screen says so from above; what says so is the model, where the plate's
side faces dropped from 55.4256 mm² to 52.3945 mm².

The rebuild takes the offset out of the picture entirely. The profile goes on the **Right plane**,
which carries the origin and both axes, drawn end-on: a rectangle 3 along the foot and 1 deep, its
bottom edge 12 below the origin — level with the sole — and its centre 8 forward. Four dimensions
and the sketch is black
([`shots/p4-ft-551-a-down-the-profile-fully-placed.png`](shots/p4-ft-551-a-down-the-profile-fully-placed.png)).
Then Extrude, Remove, Blind 30, **Symmetric**: the cut grows 15 each way from the Right plane,
covers the sole's 24, and has no direction to flip.

So the plan's rule has a third answer alongside "sketch on the face" and "up to face": **put the
profile on a datum plane through the middle of the part and cut symmetrically.** It suits any cut
that crosses the whole part, and it is the one of the three that gives the sketch a full set of axes
to dimension from — a sketch on a model face has none, because the origin is not in that face's
plane.

Two habits make the small profile easy to draw. **Untick `Show constraints`** while dimensioning and
the badges stop covering the rectangle's centre point; tick it back before closing. And **hide the
part** (hover its row in the tree, click the eye) so the origin is a point on an empty background
rather than something to hunt for on top of the model.

### `Centered` counts outward, so a count of 4 gives seven grooves

With **Centered** ticked, the instance count is the number of copies *each way plus the seed*: n
gives **2n − 1**. Count 5 laid down nine grooves and count 4 laid down the seven that were wanted
([`shots/p4-ft-474-a-four-four-committed-preview-showing.png`](shots/p4-ft-474-a-four-four-committed-preview-showing.png)).

The first try typed 7, expecting seven, and the sole came back with nine floors running y −32 to
+16 — thirteen instances, of which the outermost pair each way cut nothing but air past the toe and
heel, and the next pair cut into the very ends
([`shots/p4-ft-461-a-set-seven-grooves-6-apart-centred.png`](shots/p4-ft-461-a-set-seven-grooves-6-apart-centred.png)).
Count the floors on the model, not the instances in the field: at 6 apart on a 48 mm foot the sole
is what decides how many exist.

### One edge is enough for the whole top rim

`Top round` is a single pick — the plate's straight left edge — and **Tangent propagation** is on
when the dialog opens. Onshape follows the tangency round the arcs and takes the whole top rim in
one feature
([`shots/p4-ft-143-a-one-one-edge-picked-and-whatever-came-with-it.png`](shots/p4-ft-143-a-one-one-edge-picked-and-whatever-came-with-it.png)),
which is the answer to the brief's question and a direct consequence of the outline being tangent
throughout: an outline with a corner would stop the chain at that corner and need a second pick.

### The pattern's direction field takes a face and an edge, not only a plane

The brief asks this one exactly. All three work:

- **`Front plane`** — picked from the feature tree, and what shipped.
- **`Face of Foot plate`** — the plate's top face, picked in the graphics area. The field takes the
  face's normal
  ([`shots/p4-ft-454-a-face-the-direction-field-after-a-face-pick.png`](shots/p4-ft-454-a-face-the-direction-field-after-a-face-pick.png)).
- **`Edge of Four slits`** — a plain straight edge on the collar's rim, which is neither a plane nor
  a face
  ([`shots/p4-ft-504-b-picked-what-the-direction-field-took.png`](shots/p4-ft-504-b-picked-what-the-direction-field-took.png)).

A default plane is the one on that list that no later edit can take away, which is why the Front
plane is the one in the tree.

### Built wrong once on purpose

The brief asks for a picture of the failure, so here it is. The obvious reading of "sketch the
outline on the Top plane and extrude 6" is to extrude **up**, and it gives a foot of exactly the
right shape sitting at z 0.000 to +6.000 — the ankle ball centre would be at the bottom of the
plate rather than 12 above the ground, and the figure would stand with its ankles on the floor.
The deliberate mistake is
[`shots/p4-ft-103-b-WRONG-deliberate-mistake-the-plate-growing-up-from-the.png`](shots/p4-ft-103-b-WRONG-deliberate-mistake-the-plate-growing-up-from-the.png)
and
[`shots/p4-ft-109-c-WRONG-deliberate-mistake-the-whole-foot-sits-above-the.png`](shots/p4-ft-109-c-WRONG-deliberate-mistake-the-whole-foot-sits-above-the.png)
— those two, and no others on the foot, are the failure.

What makes it worth photographing is that the plate itself looks perfect. The shape is right, the
size is right, and only the ankle's height says otherwise. The fix is the flip and the starting
offset on `Foot plate`: 6 down, starting 6 down, which lands z −12.000 to −6.000.

### The mirror test, run and then thrown away

The brief says to check the symmetry rather than assume it. A scratch **Mirror** — Part mirror,
Add, part `Foot`, mirror plane `Right` — left the volume at 4875.8691 and the parts list at 1
([`shots/p4-ft-490-b-mirrored-the-foot-with-its-mirror-image-merged-in.png`](shots/p4-ft-490-b-mirrored-the-foot-with-its-mirror-image-merged-in.png)),
then it was deleted. Reflecting all 58 face bounding boxes agrees: they land on themselves in x and
they do not in y. **One foot serves both ankles.**

The first attempt at that test proved nothing at all, and the reason is worth knowing: the feature
tree scrolls, so the row at a remembered y was no longer `Right` when it was clicked, and the
Mirror accepted with an **empty** mirror-plane field. An unchanged volume means nothing if the
feature did nothing. Re-read the tree immediately before every row click, and after a scratch
feature, check that it did something before believing what it says.

### Looked at

Rendered on its own from isometric, top, front and right —
[`shots/p4-ft-render-isometric.png`](shots/p4-ft-render-isometric.png) and its three companions.

From isometric the foot reads as a boot sole with a post on it: a long rounded slab, the top rim
rounded so heavily that the flat top is a narrow island, and the socket collar standing clear of it
with its four tabs and the cup between them. The grooves show as square notches along the side, and
the toe end is visibly wider than the heel.

The right view is the one that answers the shape questions. The sole is flat, the collar stands
straight up from it, and the seven grooves are evenly spaced along a sole that runs level from toe
to heel — nothing about it leans. The collar sits about two thirds of the way back, which is the
32 forward and 16 back the brief asked for.

Top-down, the outline is one continuous curve — heel arc, two tangent lines, toe arc — with no
crease anywhere along it, and the collar sits on the centreline with the four slits crossing at the
ankle axis. The sole, seen from below, is seven grooves across a tapering oval
([`shots/p4-ft-597-a-ribs-the-ribbed-sole.png`](shots/p4-ft-597-a-ribs-the-ribbed-sole.png)).

### Reported back to `foot.md`

**The socket stands 7.3500 proud, and the gap to the numbers table's 5.5 is 1.85.** Measured, not
chosen: the rim is at z +1.3500 and the plate's top at z −6.000. The collar's proud length is
`grip + (ankle height − plate)` = 1.35 + (12 − 6), and the only way to make it 5.5 is to move the
plate or the ankle height. Neither was moved, and this run has nothing new to add to
[`decisions-waiting.md`](../2026-08-12-run3/decisions-waiting.md) beyond the second measurement.

**`#footHalf` 16 against `#legX` 12 is still a decision, and the part does not make it.** What the
part adds is what each choice looks like: the foot is 24 wide, so feet centred at ±12 put both
inner edges on x 0.000 and the two feet touch at a point, while feet centred at ±16 leave 8.000
between them. The socket sits on the foot's own centreline either way — nothing inside the part
records 12 or 16, and nothing about placing the socket revealed a preference. **No value picked.**

**Nothing about the foot reads as tipping forward.** The sole is flat from toe to heel, the ankle
axis is vertical, and the 32/16 split puts the ankle a third of the way back — where a person's
sits. The foot has twice as much sole in front of the ankle as behind it, which is support in the
direction a figure is most likely to be posed leaning.

**48 mm on a 150 mm figure is goofy in the way the brief wants.** It is 32% of the figure's height
against roughly 15% for a person, so the feet are about twice human proportion — big enough to read
as cartoon boots from across a room, and the r4 rounding is what keeps them reading as boots rather
than as slabs. They also do the job the size was chosen for: a 24 × 48 footprint under a 150 mm
figure stands up on its own.

**The ribs exist and they removed material** — seven floors at z −11.000 and 419.0727 mm³ gone,
against run 3's seven and 419.07. The pair of numbers is the check that catches a pattern that
regenerated into nothing, and it is worth measuring both: the floors say the grooves are there, the
volume says they cut.

**The thinnest wall is 1.5000 at the socket collar**, which is `4.7 − 3.2` and has nothing to do
with the plate. The plate edge that earlier drafts nominated is the 6 mm plate against its r4
fillet, 6 − 4 = 2, so it is real but it is not the thinnest.

## Phase 6 — the mate connectors

**Where the work is.** In each part's own Part Studio, added after every solid feature.

Phase 5 ended with six parts that measured right and could not be assembled: not one of them
carried a mate connector. A Part Studio connector reaches an assembly only when the **Part is its
owner entity**, so every one of these is attached to geometry and owned by the part.

**The tool is not on the top row.** Mate connector lives in the reference-geometry group button at
(1080, 58), or **Ctrl+M**. The group button remembers the last tool used *per document*, so on a
fresh document it opens **Plane** — read the dialog's title before filling anything in.

**Rest the pointer on the face before clicking it.** A click on a face the pointer has not hovered
selects nothing, the query list stays empty, and the dialog then refuses to close because there is
nothing to commit. Move, wait, click.

**What the inference gives you, measured on these parts.**

| you click | you get |
| --------- | ------- |
| a ball face, at its widest, `CENTER` | the sphere centre |
| a ball face near the neck junction, `CENTER` | the neck circle's centre — 2.5981 off for an r3 ball on a Ø3 neck |
| a slit socket cavity, `CENTER` | the collar rim circle, z +1.350 on the foot and hand — **not** the ball centre |
| a slit socket cavity near a slit edge | a quadrant arc's centre, off by the 0.4 slit half-width, or `MID_POINT` |

So studs take their connector from the ball face and sockets do not. A socket's connector comes
from the part's **Origin** vertex where the joint centre is the origin, and from a sketch vertex
where it is not — the head's neck socket sits 22.15 below its own origin and comes off
`Cavity profile`.

**A sketch vertex fills Owner entity with the sketch point.** That connector is ownerless and never
appears in an assembly. Clear the chip with its `×` and pick the part in the viewport.

**Every connector, as FeatureScript measures it** — `evMateConnector` on
`qBodyType(qEverything(EntityType.BODY), BodyType.MATE_CONNECTOR)`, which reads the built model
rather than the dialog:

| part | connector | made from | origin | z |
| ---- | --------- | --------- | ------ | - |
| torso | `Neck` | face of `Revolve neck stud` | (0, 0, 29) | +Z |
| torso | `Shoulder R` | face of `Revolve shoulder stud` | (24.7754, −3.9118, 9.6177) | +Z |
| torso | `Shoulder L` | face of `Mirror shoulder stud` | (−24.7754, −3.9118, 9.6177) | +Z |
| torso | `Hip R` | face of `Revolve hip stud` | (12, 0, −29) | +Z |
| torso | `Hip L` | face of `Mirror hip stud` | (−12, 0, −29) | +Z |
| head | `Neck socket` | vertex of `Cavity profile` | (0, 0, −22.15) | +Z |
| hand | `Socket` | vertex of `Origin` | (0, 0, 0) | +Z |
| foot | `Socket` | vertex of `Origin` | (0, 0, 0) | +Z |
| socket-clevis | `Socket` | vertex of `Origin` | (0, 0, 0) | +Z |
| socket-clevis | `Hinge` | vertex of `Round end profile`, realigned on its face | (0, 0, −24) | −Y |
| blade-ball | `Ball` | face of `Ball stud` | (0, 0, −24) | +Z |
| blade-ball | `Hinge` | vertex of `Origin`, realigned on an edge of `Pocket` | (0, 0, 0) | −Y |

No connector carries a typed translation: `transform` is false and all three translations are 0 mm
on all twelve. The two `Hinge` connectors read z (0, −1, 0) and x (1, 0, 0), which is what lets the
elbow and knee close as one revolute.

**Five of the twelve landed in the wrong place and measurement caught them**, all sockets or
near-misses: the foot's and hand's `Socket` at z +1.350, the head's `Neck socket` twice, the
clevis's `Hinge` at −28 instead of −24, and the torso's `Hip L` at z −26.4019. Placing a connector
and then reading its coordinates back is the step that makes them right; the dialog's own preview
does not distinguish a rim from a centre.

**Ticking Realign changes what the fields are.** The query lists become Origin entity, **Primary
axis entity**, Secondary axis entity, Select owner entity — the primary axis field is at (356, 235)
in that layout, not the (356, 272) the un-realigned dialog puts Owner entity at.

## Phase 6 — the assembly

**Where the work is.** `lesson-run6`, document `3862c2b969b83ea9de2b6430`, Assembly
`2609aa292927314e9533bb6d`. Version **`robot-run6-2026-08-15`** (`cab79923d9e94d9f908d359f`) —
[open](https://cad.onshape.com/documents/3862c2b969b83ea9de2b6430/v/cab79923d9e94d9f908d359f/e/2609aa292927314e9533bb6d).

**Fourteen instances, every one from a named version.**

| version | instances |
| ------- | --------- |
| `torso-run6-mates-2026-08-15` (`3a882a1ecb98644fa63a6e8e`) | `Torso <1>` |
| `head-run6-mates-2026-08-15` (`b2c9747847cf20e523105b66`) | `Head <1>` |
| `limb-socket-clevis-run6-named-2026-08-15` (`e316910ec9c9dc3dc6f155f2`) | `Upper limb <1>`–`<4>` |
| `limb-blade-ball-run6-named-2026-08-15` (`4e5e510f296c182db74ba8b1`) | `Lower limb <1>`–`<4>` |
| `hand-run6-mates-2026-08-15` (`fe622c2d51542d98056f0550`) | `Gripper <1>`, `<2>` |
| `foot-run6-mates-2026-08-15` (`f3a10c6ba450a92a22bf0c4a`) | `Foot <1>`, `<2>` |

The `-mates-` versions replace the ones phase 4 published: `foot-run6-2026-08-15-3` and
`hand-run6-2026-08-15-2` were both cut while their `Socket` still sat on the collar rim, so they
are the wrong thing to insert and are superseded, not amended.

**The two limb parts arrived carrying their document's name.** A part that is never renamed takes
the document name, so the studios held parts called `limb-socket-clevis` and `limb-blade-ball`.
Renamed to `Upper limb` and `Lower limb` and re-versioned as the `-named-` versions above; the
geometry is untouched.

**Insert reaches a version by searching for the document.** Insert → **Other documents** → the home
icon → type the document name → **Enter** (typing alone does not search). The hit's subtitle is the
newest version's name, and opening it lands the dialog on that version, which the breadcrumb states
in `.select-item-dialog-document-version-name`. Every instance's `documentVersion` was read back
from the API afterwards; none is a workspace.

**Pick mate connectors from the tree, not the viewport.** Every instance folds open to show the
connectors it brought with it, by name. With fourteen parts stacked on the origin before any mate
exists, the viewport triads overlap and the tree does not.

**Thirteen mates.**

| mate | type | connectors |
| ---- | ---- | ---------- |
| `Neck` | Ball | torso `Neck` — head `Neck socket` |
| `Right shoulder`, `Left shoulder` | Ball | torso `Shoulder R`/`L` — upper limb `Socket` |
| `Right hip`, `Left hip` | Ball | torso `Hip R`/`L` — upper limb `Socket` |
| `Right elbow`, `Left elbow` | Revolute | upper limb `Hinge` — lower limb `Hinge` |
| `Right knee`, `Left knee` | Revolute | upper limb `Hinge` — lower limb `Hinge` |
| `Right wrist`, `Left wrist` | Ball | lower limb `Ball` — gripper `Socket` |
| `Right ankle`, `Left ankle` | Ball | lower limb `Ball` — foot `Socket` |

`Torso <1>` is fixed, so the robot has a ground; every other instance is held only by its mates.

**The tree carries the dialog's own row while the dialog is open.** Snapshot the row names *before*
opening the mate tool, or the new row is already in the "before" set and looks like nothing
happened. The same is true of the mate connector dialog.

**A mate row appears seconds after the tick, not with it.** The solve runs first. Poll for the row
rather than reading the tree once.

**A tree row below y ≈ 955 is on the tab bar.** With several instances folded open the tree scrolls,
and a right-click aimed at the last mate row lands on the Part Studio tab and renames *that*
instead. Fold the instances up before naming the mate, and bring the row into the panel with
`scrollIntoView` if it is still low.

# Build log — the hinge, clevis and blade

## Where the work is

| What | Value |
| ---- | ----- |
| Document name | `joint-hinge` |
| Document id | `d2f74513ef2f1a7d753a7240` |
| Element id (Part Studio 1) | `32db338adbe37b8bd96142ba` |
| Published version | `hinge-stage2-teeth` |
| Version id | `a0d809042f316393f16d5809` |

- **Version link (recovery point, view-only):** <https://cad.onshape.com/documents/d2f74513ef2f1a7d753a7240/v/a0d809042f316393f16d5809/e/32db338adbe37b8bd96142ba>
- **Workspace link (live, moves under you):** <https://cad.onshape.com/documents/d2f74513ef2f1a7d753a7240/w/6f28b5d3073887b56a35a407/e/32db338adbe37b8bd96142ba>

**I opened both links, I did not just assemble them from ids.** The version link loaded showing
`joint-hinge — hinge-stage2-teeth`, the banner *"Versions are view only"*, Features (23), Parts (2)
— `25-b-published-version-hinge-stage2-teeth.png`. The workspace link loaded back into the editable
Part Studio — `26-b-done-finished-joint.png`. I opened both as the owning account (Mike Stitt); I
have **not** checked what a student account sees. The document was created inside the **Spires
Robotics** company because that is where the New document dialog defaulted.

## Verdict

- **Stage 1 built.** Two parts, no intersection, every dimension on spec. The blade limb rod went in
  backwards on the first attempt and had to be flipped; that is the only thing genuinely wrong
  rather than merely fiddly.
- **Stage 2 built on the clevis.** Twelve radial teeth 30° apart on both ear inner faces.
  Regeneration is a non-issue: the pattern costs **11 ms**, the whole 23-feature tree rebuilds in
  **122 ms**.
- **Stage 2 on the blade is only half done, and I am flagging it loudly.** I cut **one** matching
  tooth valley into the blade to prove the patterned-cut approach, but did **not** pattern it ×12 or
  mirror it before the budget ran out. As published the blade has one tooth valley and the clevis
  has twenty-four teeth. Two features are missing: a circular pattern of `Extrude 9` and a mirror of
  it.
- **A design correction came out of stage 2 that matters more than the modelling** — the brief's
  teeth cannot be built as written. See below.

## The click path that actually worked

GUI only for geometry. REST was read-only (`fetch` from inside the page) for bounding boxes, volumes
and the version list.

| # | Step | Screenshot |
| - | ---- | ---------- |
| 1 | **Create** ▸ **Document…**, name `joint-hinge` | `01-a`, `01-b` |
| 2 | ☰ ▸ **Workspace units…** ▸ *Length default unit* = **Millimeter** ▸ green ✓ | `02-a`, `02-b` |
| 3 | Select **Front** ▸ **Sketch**; press `n` to orient | — |
| 4 | **Center point circle** (`c`) on origin; **Dimension** (`d`) → **Ø12** | `03-a` |
| 5 | **Corner rectangle** (`g`) below; dimension **12** wide, **12** tall, origin→bottom edge **12** | — |
| 6 | Left edge + circle ▸ constraint flyout ▸ **Tangent** — this is what centres the tongue | `04-a`, `04-b` |
| 7 | `Sketch 1` ▸ **Extrude** ▸ **New** ▸ **Symmetric** ▸ **6 mm** → blade | `05-a`, `05-b` |
| 8 | Repeat on **Front** with the rectangle **above**; bottom edge fixed with **Coincident** (origin ↔ edge), since a zero dimension is illegal | `06-a`, `06-b` |
| 9 | `Sketch 2` ▸ **Extrude** ▸ **New** ▸ **Symmetric** ▸ **11.6 mm** → clevis blank | `07-a`, `07-b` |
| 10 | **Front** ▸ **Sketch**: corner rectangle **16 × 12.6** centred on origin (4 dimensions) | `08-a` |
| 11 | **Extrude** ▸ **Remove** ▸ **Symmetric 6.6**, **Merge with all** *off*, **Merge scope = Part 2** — opens the fork; scoping is not optional | `08-b`, `09-b` |
| 12 | **Top** ▸ **Sketch** ▸ circle **Ø12** on origin | `10-a` |
| 13 | **Extrude** ▸ **Add** ▸ **Starting offset 7** ▸ **Depth 17**, both directions flipped downward, scope Part 1 → blade limb z −7…−24 | `10-b` |
| 14 | Same sketch ▸ **Extrude** ▸ **Add** ▸ **Starting offset 12** ▸ **Depth 12** upward → clevis limb z +12…+24 | `11-b` |
| 15–16 | **Front** ▸ circle **Ø3** ▸ **Extrude Add**, offset **2.1**, depth **1.2**, scope Part 2 → stub | `12-a`, `12-b` |
| 17–18 | **Front** ▸ circle **Ø3.2** ▸ **Extrude Remove**, offset **1.5**, depth **1.5**, scope Part 1 → pocket | `13-a`, `13-b` |
| 19 | **Mirror** ▸ **Feature mirror** ▸ stub + pocket extrudes ▸ plane **Front** ▸ tick **Reapply features** | `14-a`, `15-b` |
| 20 | *(stage 2)* **Front** ▸ **Sketch**: circles **Ø4.4** and **Ø9** on origin, two lines origin→Ø9 circle, one **Vertical**, **15°** between | `21-a` |
| 21 | **Extrude Add**, offset **2.7**, depth **0.6**, scope Part 2 — selecting **only the wedge region** | — |
| 22 | **Circular pattern** ▸ **Feature pattern** ▸ **Axis = the stub's cylindrical face** ▸ **12** instances, 360°, equal spacing | `22-a` |
| 23 | **Mirror** ▸ **Feature mirror** ▸ tooth extrude + pattern ▸ **Front** ▸ **Reapply features** | `24-b` |
| 24 | *(candidate 3 probe)* same wedge ▸ **Extrude Remove**, offset **2.4**, depth **0.6**, scope Part 1 | — |
| 25 | Feature list stopwatch ▸ **Show regeneration times** | `23-b` |
| 26 | Left rail ▸ **Create version…** ▸ `hinge-stage2-teeth` | `25-b` |

## Every measurement

| What | Expected | Measured | How |
| ---- | -------- | -------- | --- |
| Slot width, ear inner face ↔ ear inner face | 6.6 | **6.600** | *Parallel dist* (`18-b`) |
| Blade face → blade limb axis | 3.0 | **3.000** | *Center axes dist* (`20-b`) |
| ⇒ Blade thickness | 6.0 | **6.000** | 2 × 3.000 |
| ⇒ **Ear-to-blade gap, each side** | **0.3** | **0.300** | (6.600 − 6.000)/2 |
| Ear outer face → limb axis | 5.8 | **5.800** | *Center axes dist* (`19-b`) |
| Limb rod radius | 6.0 | **6.000** | *Radius* |
| ⇒ **Wall left inside the Ø12 limb, per side** | 0.2 | **0.200** | 6.000 − 5.800 |
| Ear inner face area | 125.08 | **125.080** | face area (r6 disc + 12 × 6.3 root, less Ø3 stub base) |
| Tooth footprint area | 2.0175 | **2.017** | crest face area |
| Tooth height proud of ear face | 0.6 | **0.600** | Y component of *Max dist* |
| Blade bounding box | ±6, ±6, −24…+6 | **exact** | REST `boundingboxes` |
| Clevis bounding box | ±6, ±6, −6…+24 | **exact** | REST `boundingboxes` |
| Blade volume | 2756.8 (hand) | **2756.23** | REST `massproperties` |
| Clevis volume | 2857.4 (hand) | **2857.36** | REST `massproperties` |

Derived, pinned by the above:

- **Stub engagement.** Stub runs y 2.1→3.3; blade face y 3.0; pocket floor y 1.5. So the stub crosses
  the 0.3 gap and sits **0.9 mm inside a 1.5-deep pocket**, leaving **0.6 mm** to the floor. Visible
  and correctly scaled in `17-b-done-section-stub-in-pocket.png`.
- **Nothing in the fork is thinner than 2 mm.** Thinnest is the **ear at 2.5 mm**; the blade keeps
  **3.0 mm** of web between the two pockets.
- **Ear free length 12.3 mm** (root z +6.3 to tip z −6).

### Two measurement honesty notes

1. **I could not pick the ear inner face and the blade face together.** Inside the fork the blade
   covers the ear exactly — for z > 0 both are the same r6 disc, for z < 0 the blade is wider — so
   there is no line of sight to the ear's inner face from any camera angle. I measured slot and
   blade separately and subtracted. The 0.300 is arithmetic on two measured numbers, not a single
   picked distance.
2. **One face-area reading contradicted the model and was wrong, not the model.** A blade face read
   **148.587 mm²**, exactly a tongue face with *no* pocket. It came after a "click empty space to
   clear the selection" that landed on geometry, so the panel was summing more than one face (the
   same failure gave a nonsense 104.271 mm² earlier). The pockets are definitely there: the blade
   lost **25.86 mm³** against the hand-computed solid (2782.09 → 2756.23); one pocket plus one tooth
   cut accounts for only 13.27 mm³, two pockets plus one tooth cut for 25.34. I lost ~15 minutes to
   this phantom. **Verify what is in the selection list before trusting the number.**

## The teeth

**Approach 1 worked, first time, and is cheap.** Sketch one wedge, extrude 0.6 proud,
circular-pattern ×12 about the stub's cylindrical face, mirror. I never needed approach 2 (revolved
sawtooth). I probed approach 3 (patterned cut) — below.

- **Tooth arc width at the outer radius (r = 4.5): 1.178 mm** (9π × 15/360, from the measured Ø9 and
  measured 15°). The 30° **pitch arc is 2.356 mm** — that is the ~2.4 mm the brief warned about, but
  it is the pitch, not the tooth.
- **The tooth's inner end is the real problem: 0.576 mm** at r = 2.2, and the valley there is the
  same. That is a hair over one 0.4 mm extrusion width; a 0.4 mm nozzle will bridge those valleys
  and print the inner third of the ring as a solid disc — exactly where a detent needs crispness.
- **Regeneration is a non-issue.** Onshape's **Show regeneration times** panel: **Total 122 ms** for
  23 features, of which **Circular pattern 1 = 11 ms**, tooth extrude 9 ms; the most expensive
  feature in the whole model is `Mirror 1` at 13 ms.

**My honest view: keep 12 teeth, but move the inner radius.** Twelve is one dialog field and 11 ms —
dropping to 8 at 45° saves nothing and costs pose resolution. What is marginal is r = 2.2. Start the
band at **r = 3.2** and the narrowest tooth becomes 0.84 mm instead of 0.576, still twelve teeth at
30°, and it prints. That is the change I would make, not the tooth count.

### The brief's tooth geometry cannot be built as written

0.6 proud on **both** faces with a **0.3** gap is impossible:

- Ear face y 3.3, crest y 2.7. Blade face y 3.0, crest y 3.6. The crests **overlap by 0.9 mm** at
  nominal. There is no assembly in which that geometry exists. Even a boss on the ear alone
  interferes with a plain blade face by 0.3 mm.

So I built the only version that closes: **boss on the ear, matching valley cut into the blade**
(0.6 deep, y 3.0→2.4), so the crest at 2.7 sits in it with 0.3 clearance and rotation makes the
crest climb out and spread the ears. That is `Extrude 9`, and it is also candidate 3 proved on one
instance. **I did not pattern or mirror it.**

One thing to decide before printing: with 0.3 clearance in the valley the joint has **no tooth
preload** — all grip comes from the stub/pocket press fit. If you want the teeth sprung, cut the
valley **0.45** deep and accept 0.15 mm interference per side.

## What did not work

- **The blade limb rod extruded the wrong way and would have destroyed the joint.** With *Starting
  offset* enabled, the offset direction is **not** flipped by the main direction's *Opposite
  direction* button — it has its own flip control. Flipping only the main direction gave a rod from
  z +7 down to −10, a Ø12 cylinder straight through the fork intersecting both ears. Preview and
  isometric both looked plausible; only the REST bounding box (`highZ = 7` on a part whose top
  should be 6) caught it (`16-x`). **Check bounding boxes after any offset extrude.**
- **`Mirror 1` failed:** "Could not create all instances as entered." Fix is Onshape's own hint —
  tick **Reapply features**. Same for `Mirror 2`.
- **`Mirror 2` then failed again:** "Select a mirror plane." The click meant for `Front` hit the
  panel header because the tree had scrolled and `Front` was off the top. Typing `Front` into the
  feature list's **filter box** is the reliable route; clear the filter afterwards.
- **Midpoint constraint would not take** (3 attempts, shortcut and flyout) —
  `04-x-midpoint-constraint-did-not-apply.png`. I used a **Tangent** constraint between the
  rectangle's side edge and the Ø12 circle instead, which is better design intent anyway: "the
  tongue is as wide as the round end."
- **Typing a value while drawing does nothing.** The live `Ø111.187` readout looks editable. It is
  not; digits are discarded and Enter commits whatever the cursor was at.
- **Double-clicking that readout made it worse** — produced a `Ø0` label and a half-size circle with
  no clean way back. I cancelled the sketch and restarted. Two attempts wasted.
- **The extrude dialog picks the solid, not the sketch region**, when the sketch is buried inside the
  model. Selecting a single tooth wedge required hiding both parts first, and on the second pass
  switching the sketch's own visibility on.
- **A sketch on the Front plane did not auto-orient**, contrary to `.docs/browser-access.md`; I had
  to press `n`, and `n` looked at the plane from *behind* (view cube read **Back**, +X ran left).
  Harmless here since everything is Z-symmetric, but it would silently mirror any left/right
  feature.
- **Reaching a named constraint took 4 attempts.** The last toolbar slot is a *most-recently-used*
  button, so the only reliable route is opening the flyout and clicking the item **within the same
  interaction** — the flyout closes between script invocations.

## What the brief never said, and I had to work out

1. **Where the limb rods stop.** A Ø12 blade rod reaching the hinge axis passes clean through the
   ears. It must stop outside the ears' r6 envelope: I put its top face at **z = −7** (1 mm clear of
   the ear tips) and joined it to the round end with the flat 6-thick tongue. Clevis rod starts at
   **z = +12**.
2. **How the fork closes at the top.** The blade's round end sweeps r6 about the axis, so the bridge
   must start outside it: slot **12.6 tall** (±6.3), ear root at z = +6.3, 0.3 mm swept clearance.
   That single number sets the ear free length.
3. **The slot must be open in X too** — cut 16 wide against a 12-wide clevis so it runs out both
   sides.
4. **Merge scopes everywhere.** Almost every Add/Remove must be scoped by hand. The slot cut with
   **Merge with all** on would have deleted most of the blade; the stub with it on would have fused
   the two parts. Onshape defaults to **Merge with all**.
5. **The stub must be added before the pocket is cut.** The parts genuinely interfere between those
   two features. Feature order is load-bearing.
6. **The tooth wedge needs a rotational lock** — two radial lines and two arcs are not fully
   defined; one **Vertical** constraint fixes it.
7. **Onshape's Front plane normal points into −Y**, so every "starting offset" lands on the far side
   from what you would guess.

## Ø12 stock, for an 11.6 mm clevis: tight, and tighter than the number suggests

**0.200 mm of wall per side, measured.** The ear's outer face is 5.800 from the limb axis; the limb
surface is at 6.000. The clevis eats **96.7 % of the stock diameter**, and 0.2 mm is half a nozzle
width — on a printed part the ear faces and the limb surface are the same surface.

There is a second, larger effect the brief's arithmetic does not capture. The clevis is not a
cylinder, it is a **12 × 11.6 paddle**, and that rectangle **circumscribes** the Ø12 limb — its
corners stand up to 2.5 mm proud of the rod. You can see it at the shoulder in
`26-b-done-finished-joint.png` and in the plan view `10-a`, where the Ø12 circle bulges past the
block's flats while the block's corners sit outside the circle. For the clevis to be genuinely
*inside* Ø12 stock at 11.6 thick it could only be 3.07 mm wide, which is absurd.

**So: Ø12 works, but it is the minimum and it is not roomy.** It satisfies "11.6 fits within 12"
with 0.2 mm to spare and nothing else. **Ø14 would take the wall to 1.2 mm per side** and make the
joint printable rather than nominal. If the limbs cannot grow, expect the ear outer faces to merge
into the limb surface on the printer, and design the shoulder as a deliberate step rather than
pretending it is flush.

### The failure mode you cannot test in CAD, with numbers to reason about it

To push the blade in, the gap between stub tips is 6.6 − 2 × 1.2 = **4.2 mm** against a **6.0**
blade, so **each ear must deflect 0.9 mm**. Over a **12.3 mm** free length in a **2.5 mm**
cantilever, peak surface strain ≈ 3·t·δ / 2·L² = 3 × 2.5 × 0.9 / (2 × 12.3²) ≈ **2.2 %**. That is a
calculation, not a measurement. PLA yields at about 2–3 %, so assembly sits right on the edge — the
ears will probably survive one insertion and may not survive several. Lengthening the ears (taller
slot) or shortening the stub protrusion are the cheap levers; the stub is safer, because slot height
is what gives the blade its rotation clearance.

## Timing

Two hard timestamps, both from Onshape's own version history:

- Document `joint-hinge` created — **09:17**.
- Version `hinge-stage2-teeth` published — **11:17**.

**Two hours of wall clock** for both stages, plus ~15 minutes reading the brief and drawing
beforehand and ~20 minutes afterwards verifying links and writing this. I did **not** clock the
stage 1 / stage 2 boundary separately, so I am not going to invent a split.

- **An agent driving a headless browser is not student pace, and it is not obviously faster.** A
  large share of those two hours went on things a human never experiences: measuring pixels to find
  the origin on screen, discovering that a 1 px miss on a sketch line silently produces no dimension
  at all, and rotating the model by trial and error. Someone who knows Onshape would build stage 1
  in well under an hour. A student who has never opened Onshape would **not** finish stage 1 in a
  two-hour session — 23 features, six sketches, five separate merge scopes.
- **This is a specification build, not a lesson.** Nothing here has been walked at student pace or
  timed as teaching steps.

## Feature tree as published

```
Origin, Top, Front, Right
Sketch 1  blade profile        Extrude 1  blade, symmetric 6, New
Sketch 2  clevis profile       Extrude 2  clevis, symmetric 11.6, New
Sketch 3  slot 16 x 12.6       Extrude 3  slot, Remove symmetric 6.6, scope clevis
Sketch 4  limb circle O12      Extrude 4  blade limb, offset 7 depth 17 down, scope blade
                               Extrude 5  clevis limb, offset 12 depth 12 up
Sketch 5  stub O3              Extrude 6  stub, offset 2.1 depth 1.2, scope clevis
Sketch 6  pocket O3.2          Extrude 7  pocket, offset 1.5 depth 1.5, Remove, scope blade
                               Mirror 1   Extrude 6 + 7 about Front, Reapply features
Sketch 7  tooth wedge 15 deg   Extrude 8  tooth, offset 2.7 depth 0.6, scope clevis
                               Circular pattern 1  Extrude 8, 12 about the stub axis
                               Mirror 2   Extrude 8 + pattern about Front, Reapply features
                               Extrude 9  one blade tooth valley, offset 2.4 depth 0.6, Remove
Parts (2)  Part 1 = blade, Part 2 = clevis
```

Features are **not renamed** — `Extrude 4` and friends are the names in the published version.
Deliberate for a spec build, and the first thing to fix before any of this becomes teaching
material.

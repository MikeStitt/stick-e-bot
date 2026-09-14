# The head — profile, face, neck socket and shell (run 3, picked up mid-build)

## Where the work is

| | |
| --- | --- |
| Document name | `head-run3` |
| Document id | `e4e890de0530e1c4df67aada` |
| Element id (Part Studio 1) | `e6f35e31754f2ac17c4d11ca` |
| Workspace id | `e4eb5c7ebf1862e98cdfb525` |
| Version name | `head v1 - face, neck socket, shell` |
| Version id | `e8ac2fd35a4b025bb57a0708` |
| Part | `Head`, part id `JHD` |

- **Version link (cite this one):**
  `https://cad.onshape.com/documents/e4e890de0530e1c4df67aada/v/e8ac2fd35a4b025bb57a0708/e/e6f35e31754f2ac17c4d11ca`
- **Workspace link — live, will drift:**
  `https://cad.onshape.com/documents/e4e890de0530e1c4df67aada/w/e4eb5c7ebf1862e98cdfb525/e/e6f35e31754f2ac17c4d11ca`

**I opened both links** in my own browser page after publishing. Both loaded to the Part Studio
with page title `head-run3 | Part Studio 1` (`79-a-version-link-open.png`,
`79-b-workspace-link-open.png`). The ids are read back from those loaded URLs, not typed from
memory.

The version was published from the state described below: 20 features, 1 part, every feature
`OK` read from `GET .../features` `featureStates`, volume 5804.703141 mm³. After publishing I ran
one further experiment (see *Order is the finding*) and undid it; the workspace was then re-read
and matches the version — same feature order, same 5804.703141 mm³.

No new document was created. This is the document my predecessor started. The document already
carried one version, `Start` (`190288824e6271f9cd23f763`, 04:20 UTC), made before either of us
touched the model; the takeover brief said there was no version, so that is a small correction.

Browser page stamp for this run: **`HEAD2_RUN3_9C2F41`**. I censused all 18 pages' `window.name`
before stamping, confirmed nothing carried that name, stamped my own `ctx.new_page()`, and
re-censused to exactly one match (`steps.log` 03:39:49). My predecessor's page, still carrying
`HEAD_RUN3_7Q4XZ`, was left alone and never touched. CDP endpoint 9223 only.

## What I inherited and what I did

My predecessor stopped after the body. It left 4 features, one part `Head`, volume
34358.772253 mm³, bbox 36 × 30 × 36, everything `OK`. **I verified all of that myself through
read-only REST before touching anything** (`steps.log` 03:40) and it was exactly as described.

| Feature | Whose |
| --- | --- |
| `Head profile` (sketch) | predecessor — kept as-is |
| `Head body` (extrude) | predecessor |
| `Outline rounds` (fillet, was `Fillet 1`) | predecessor — I renamed it |
| `Sketch 1` (unfinished eye sketch) | predecessor — **I deleted it** |
| `Face plane` | mine |
| `Eye profile`, `Eye`, `Second eye` | mine |
| `Mouth profile`, `Mouth` | mine |
| `Boss circle`, `Neck recess` | mine |
| `Ball profile`, `Neck ball tool`, `Neck socket` | mine |
| `Head shell` | mine |
| `Boss rim chamfer` | mine |

### The inherited sketches: one kept, one deleted

`Head profile` I **kept**. It is fully defined, symmetric, and carries **two real `TANGENT`
constraints** (arc-to-left-line and arc-to-right-line) plus `VERTICAL` on both sides,
`HORIZONTAL` on the bottom, `RADIUS 18` and `DISTANCE 18`. It is correct and redoing it would
have bought nothing.

`Sketch 1` I **deleted**. It was the start of the eye sketch: two ellipses, under-defined, not
held `Equal` to each other and not symmetric about the centreline — i.e. the two things the brief
specifically asks for were the two things missing. Finishing someone else's half-constrained
ellipse pair is slower than drawing one ellipse properly and mirroring it, which is what I did.

## The click path that actually worked

Steps 1–3 are my predecessor's, from its own log; I did not repeat them. Screenshot names are the
files in this directory.

4. **Face plane** — `cPlane`, `Front` picked from the tree, offset **15**, flip normal, so the
   plane lands on the front face at y = −15 (`28-a-select-plane-dialog.png`,
   `28-b-done-face-plane.png`).
5. **Eyes.** Sketch on `Face plane`. **Ellipse** drawn rough, then dimensioned: major **10**,
   minor **3.5** semi (7 across), centre **x = 8, z = 6**. Only **one** ellipse is in the sketch —
   the second eye is a **feature Mirror** about the `Right` plane (`Second eye`), which is what
   makes the pair exactly equal and exactly symmetric without a single sketch constraint
   (`29-…` through `34-…`, `37-b-done-two-eyes.png`). Extrude **Add, 1.5 proud**
   (`35-…`, `36-b-done-eye-proud.png`). Rendered check `38-x-eyes-front/right/isometric.png`.
6. **Mouth.** Sketch on `Face plane`; **Slot** tool; centre line 16 long on z = −6, slot width
   **4**, so the mouth is **20 × 4 overall with r2 ends**. Extrude **Remove, 1.5 deep**
   (`39-…` through `51-b2-done-mouth-cut.png`). Face render `52-x-face-front/isometric/bottom.png`.
7. **Neck boss and recess.** Sketch on the underside: a Ø12 circle plus a 40 × 34 rectangle to
   give a "region between". Extrude **Remove 1 mm**, merge with all, taking away everything
   outside the circle (`53-…` through `61-a3-select-merge-all.png`). The boss is the Ø12 island
   left standing at z = −18; the rest of the underside is now at z = −17.
8. **Neck socket.** Sketch on the `Right` plane: a half-disc r **3.2** whose centre sits **1.35**
   above the boss face, i.e. at z = −16.65. Revolve → `Neck ball tool` (a Ø6.4 ball, not the Ø6
   ball itself — 3.2 = ball 3.0 + fit 0.2). Boolean **Subtract** → `Neck socket`
   (`63-…` through `70-b2-done-socket.png`).
9. **Head shell** — thickness **1.2**, opening the **back face** (y = +15), *not* the underside.
   Why, at length, below.
10. **Boss rim chamfer** — 0.5 mm at 45° on the Ø12 boss rim, as the brief asks. It removed
    4.581 mm³; Pappus says 2π·(6 − 0.5/3)·(0.5·0.5/2) = 4.5815, so it is the chamfer and nothing
    else (`75-…`).

## Order is the finding

The brief's step 8 is *"Shell last, thickness 1.2, opening the underside."* **That cannot be
built.** Here is every order I tried and what each one did.

| # | What I tried | Result |
| --- | --- | --- |
| A | Brief's order. Shell last, remove the recessed underside face, t = 1.2 | **ERROR** — *"Shell 1 did not regenerate properly: Could not shell part with selections."* (`72-e-shell-error-tooltip.png`) |
| B | Same, t = **0.9** (under the 1.0 mm step, in case the step was too shallow for the wall) | **ERROR**, identically. So it is not a thickness problem. |
| C | Same, removing the recessed underside **and** the boss face, t = 1.2 | **ERROR**. Opening the socket from below does not rescue it either. |
| D | Recess face only, with `Neck socket` **suppressed**, t = 1.2 | **ERROR**. So the spherical cavity is not what breaks it. |
| E | Shell last, remove the **back face** (y = +15), t = 1.2 | **OK.** 1 part, 5809.284630 mm³ (5804.703141 after the chamfer). This is what shipped. |
| F | Shell **early** — dragged `Head shell` up the tree to sit before `Boss circle`, still opening the back face | **No error at all**, and the part is ruined. See below. |

### Why opening the underside cannot work

The recess takes away *the whole underside except the Ø12 boss*. So if you then hand that recessed
face to Shell as the face to remove, the wall Shell would grow inward from the boss face and its
1 mm riser has **no material path to the side walls** — the removed face is exactly the surface
that used to connect them. The shell falls into two disconnected solids, and Onshape refuses.
Tests B, C and D are the three ways of checking that this is topology and not thickness, cavity
or step depth. **A head cannot be both hollow-open-at-the-bottom and carry a neck boss in the
middle of that bottom.** The boss needs a floor.

So the shell opens the **back**. The head is still hollow, still prints without support, the
opening faces away from whoever is looking at the robot, and the floor that carries the neck
socket survives. It removes 27535 mm³ of the 33340 mm³ solid — **83% of the plastic**, not the
half the brief promises.

### What shelling early does — the answer to "report what breaks if you shell earlier"

Nothing goes red. That is the whole problem. With `Head shell` moved before `Boss circle`
(experiment F, `78-a-shell-moved-early.png`), all 20 features regenerate `OK` and the part looks
plausible in the tree. Measured:

- the inner floor lands at **z = −16.8**, 1.2 above the *original* bottom at z = −18;
- the recess then cuts the outside down to z = −17, so the floor outside the boss is
  **0.200 mm** thick;
- the socket's spherical face is down to **24.127 mm²** (from 91.483) and its box stops at
  z = −16.8: **the cavity has broken through the floor**. The socket is a hole, not a cup, and
  the ball would fall into the head (`78-early-bottom.png`, compare `76-final-bottom.png`).
- volume 4802.429163 mm³ against 5804.703141.

I undid the reorder and re-read the workspace to confirm it matches the published version.

**The rule this gives the curriculum:** Shell goes last because Shell measures its wall from
whatever faces exist *at the moment it runs*. Any cut made after it eats that wall silently.

## Acceptance checks

All measured on the finished part, via read-only `POST /featurescript` (`evBox3d`, `evArea`,
`evSurfaceDefinition`) and `GET .../massproperties`. Full numbers in `steps.log` at 05:34.

| Check | Measured | |
| --- | --- | --- |
| Parts (1) | `Head`, part id `JHD` | PASS |
| 36.000 across | tight box x −18.000000 … 18.000000 | PASS |
| 36.000 tall | tight box z −18.000000 … 18.000000 | PASS |
| top lands at 150 | head centre z = +48 → top 48 + 18 = 66; ground −84; 66 − (−84) = **150** | PASS (arithmetic on the plan's stations — not an assembly measurement; nothing is assembled yet) |
| underside recessed behind the boss | boss face plane **z = −18.000**, recessed underside plane **z = −17.000** → **z-step 1.000 mm** | PASS (non-zero) — but read the caveat below |
| socket mouth Ø5.803 | boss face area 86.652979 before the chamfer → **Ø 5.8026** | PASS |
| cavity 109.48 mm³ | 33449.256539 → 33339.774522 = **109.482017** | PASS |
| shell 1.200 at three places | floor −17.000/−15.800; front wall −15.000/−13.800; **next to a cut**: mouth floor −13.500 / wall behind it −12.300 | PASS, all **1.200** |
| profile tangent throughout | two `TANGENT` constraints; in the solid the top is `CYL r = 18.000` about the y axis through z = 0 and the sides are `PLANE x = ±18.000` — tangency exactly | PASS |
| thinnest wall anywhere | **1.200 mm**, and it is 1.200 everywhere the shell sets it | see below |

The socket volume expectation was **written into `steps.log` at 05:06, before the measurement**,
as the brief demands: 109.483 mm³ removed, *above* the mouth face, because the head sits on top of
the ball. The wrong-way-up answer would have been 27.776. It came out 109.482017. The socket is
the right way up.

### Where 1.200 turns up

The shell sets 1.200 in every place I could measure it, which is the real answer to *"does Shell
survive the socket cavity?"*:

| Outer | Inner | Wall |
| --- | --- | --- |
| floor z = −17.000 | z = −15.800 | 1.200 |
| front face y = −15.000 | y = −13.800 | 1.200 |
| mouth floor y = −13.500 | y = −12.300 | 1.200 |
| each eye face y = −16.500 | y = −15.300 | 1.200 |
| sides x = ±18.000 | ±16.800 | 1.200 |
| top arc r 18 | r 16.8 | 1.200 |
| outline rounds r 3 | r 1.8 | 1.200 |
| **socket cavity sphere r 3.200** | **dome r 4.400** | **1.200** |

**Shell survives the socket cavity.** It offsets the sphere outward to r 4.400 and leaves the cup
standing inside the hollow head as a 1.2 mm dome (visible in `76-final-back.png`). The socket
opens into the head's interior — there is no separate ceiling over it — which is fine for a ball
that enters from below, and it is why the head must not also be open at the bottom.

Nothing measured thinner than 1.200. The tightest *material* section that is not a shell wall is
the socket collar: at z = −18 the boss face is an annulus from the mouth (r 2.9013) to the
chamfered boss edge (r 5.500), so **2.599 mm of rim**. The brief's open question asks about
"1.3 mm of rim before the slits are cut", derived from a Ø9.4 collar in a Ø12 boss; because this
socket is bored into the boss rather than standing as a collar, the rim is 2.6, not 1.3. There
are no slits (see below).

### One thing that is not a wall but will bite the printer

Inside the boss the shell leaves a **0.400 mm wide, 1.000 mm deep annular slot** between the dome
over the socket (r 4.400) and the boss's inner wall (`CYL r = 4.800`, z −16.800 … −15.800). A
0.4 mm slot will not print at a 0.4 mm nozzle and will not clean out. It is a consequence of
shelling a 1 mm step with a 1.2 mm wall, and it wants a decision before anyone prints this.

## Where the brief was guessing, and where it is wrong

**The eyes and the mouth (the brief says "pick one, say what you picked and why").**
Eyes: ellipses **10 × 7**, centres at x = ±8, z = +6, standing **1.5 proud**. Chosen so the pair
spans 26 of the 36 mm width — wide-set reads as a face, and 1.5 proud is enough to catch light
without being a snag. Mouth: a slot **20 × 4 overall** (16 mm centre line, r2 ends) on z = −6,
cut **1.5 deep**. Render `76-final-front.png`: it reads as a face — a calm, slightly deadpan one.
Not agonised over; recorded so someone can change it in one dimension each.

**The recess depth: 1 mm, and it does not buy 42°.** I stepped it **1 mm** because that is as deep
as the 1.2 mm shell floor allows — 1 mm off a 1.2 mm floor is already all of it, and experiment F
shows what happens when the step and the floor fight. The brief's own figure comes from
`asin(4/6)` = 41.8°, i.e. **boss faces 4 mm apart**; whether this 1 mm step produces that 4 mm is
not knowable from the head brief, because it depends on how far the torso's boss stands proud of
the torso top, and the head brief only fixes the head's underside at station +30 with a 6 mm gap.
That number needs settling against `torso.md`, not guessing here.
**And whatever it settles at, the broad underside still binds first.**
Its far corner is 23.43 mm from the neck axis and the recess lifts it to 7 mm of clearance, so it
touches at `asin(7/23.43)` = **17.4°**, not 42°. For the boss to be the binding radius the
underside would have to clear 23.43·sin(41.8°) = 15.6 mm — a recess about **9.6 mm** deep, which
is a dish, not a step, and nothing a 1.2 mm shell can carry. The brief's sentence *"a boss only
buys tilt if the face it stands on steps back"* is right, and the amount it has to step back is
roughly ten times what anyone has been drawing. **This needs a decision:** either accept ~17°,
or round/chamfer the underside corners hard, or make the head's underside plan much smaller than
36 × 30.

**The brief never mentions the relief slits.** `ball-and-socket.md` cuts slits so the collar can
open and take the ball; the head brief has them in neither the build order nor the acceptance
checks, and with a boss only 1 mm proud there is no free tab length to slit. As built, the socket
is a rigid cup: the ball has to be pressed in past a 5.803 mm mouth for a 6 mm ball, into a 1.2 mm
dome that can flex a little because it is thin. Untested, and worth a real decision rather than a
silent omission.

**The collar numbers in the brief's table do not apply here.** `socket collar Ø 9.4` and
`socket collar length 5.5` describe a collar standing proud; step 7 asks for the socket *in the
boss face*, which is a different thing. I built the bored version, which is what step 7 says.

**"It is shelled, which halves the print."** It removes 83%.

## What did not work, and the calibrations that came out of it

- **`Could not shell part with selections`** carries no detail in `featureStates` — the REST reply
  is only `{"featureStatus": "ERROR"}`. The message lives in the tree row's tooltip; hover the
  row's error badge and read the DOM.
- **`chamfer` is its own toolbar button** in this build, not a member of the fillet toolgroup.
- **The middle mouse button pans**; Onshape **orbits on a right-button drag**. The view-cube
  arrows in this build rotate 180° per click, not 90°, and the view-cube dropdown offers only
  Isometric/Dimetric/Trimetric — there is no "Bottom" in it.
- **`evBox3d` over `qEverything(EntityType.BODY)` includes the datum planes** and returns
  152.4 mm cubed. Use `qBodyType(…, BodyType.SOLID)`.
- **`evSurfaceDefinition` on a torus** threw *"Can not divide undefined and ValueWithUnits"* on
  `majorRadius`. Dropping the torus branch and reporting those faces as `OTHER` was enough.
- **Feature reorder by dragging the tree row works** and regenerates cleanly, and one `cmd+Z`
  puts it back — which is what made experiment F cheap.
- Earlier in the session (all in `steps.log`): `SLOT` lives in the **OFFSET** toolgroup and, like
  Offset, **operates on an existing sketch line** — draw the centre line, select it, then invoke
  it; it takes its width from wherever the pointer last was, so dimension it afterwards, and step
  a big width change (20 → 12 → 4) or the solver gives up. A distance dimension is **unsigned**,
  so setting 2.65 flipped the ball profile to the wrong side of the edge. A no-op Extrude Remove
  **vanishes from the tree on Escape**. `gui.ok()` does not commit a Boolean — click the green
  tick.

## The five tools Stage 3 earns here

- **Arcs** — the head's whole silhouette is one arc and two lines. It worked; the arc is
  `CYL r = 18.000` in the solid, exactly the sketch radius. Nothing to complain about.
- **Tangent** — two constraints hold the chain. The brief asks whether it *holds when you drag*:
  in this sketch **there is nothing to drag**. Every curve draws black (`80-a-profile-open.png`),
  the sketch is fully defined, and a drag across the arc moved nothing at all
  (`80-b-after-drag.png`). That is the right answer for a production sketch but it means the drag
  demonstration a teacher wants has to be staged on a deliberately under-defined copy.
- **Ellipse** — the tool asks for **centre, then one axis end, then the other axis end**, in that
  order, and it will happily leave you with an under-defined ellipse afterwards. Dimensioning the
  minor axis needed a **construction line from centre to curve**; the ellipse's own minor axis has
  no pickable entity. Then one ellipse plus a **feature Mirror** beats two ellipses plus `Equal`
  plus `Symmetric` — fewer constraints, and the symmetry cannot drift.
- **Slot** — the awkward one. It is hidden in the Offset toolgroup, it needs a line to act on, it
  guesses its own width from the pointer, its dimension label is canvas-drawn (reach it by
  double-clicking the leader line) and its constraint badges sit exactly where you want to click,
  so untick *Show constraints* first. It does produce a clean 20 × 4 slot with r2 ends. A teacher
  should expect to spend real time here.
- **Shell** — earns its billing as "the part worth watching", and it fails the brief's own build
  order. See *Order is the finding*. Two lessons worth keeping: Shell must be last, and **a shell
  opening cannot be a face that something else stands on**.

## Retrospective

**What I inherited:** the profile sketch, the extruded body and the outline fillets — the head's
shape, and it was right. Also an unfinished eye sketch, which I deleted.

**What I did:** everything from `Face plane` onward — both eyes, the mouth, the neck boss and its
recess, the upside-down neck socket, the shell and the boss chamfer; every measurement in this
document; the six order experiments; the version; these notes.

**What I got wrong on the way.** I predicted a post-shell volume of about 4.5 cm³ and logged that
prediction before measuring, which was honest but was arithmetic for a *bottom-opened* shell — a
shape that turned out to be unbuildable. When the shell finally ran, on the back face, it came out
5.80 cm³ and my stated band did not contain it. The prediction that mattered — the socket cavity,
109.483 mm³ above the mouth face — I got right, and I wrote it down first.

**What I would tell the next person.** Do not trust a green feature tree. The most dangerous
result tonight was experiment F, where shelling early produced a 0.2 mm floor and an open socket
with every feature reading `OK`. The only reason it was caught is that face areas and plane
positions were measured rather than looked at. Measure the faces.

**Where this leaves the brief.** Steps 1–7 build as written. Step 8 does not, and the fix changes
the part's character (open back, not open bottom, and 83% hollow rather than half). The tilt
arithmetic in *"The neck is a tilt problem"* needs redoing: the boss is right, the 1 mm step is
right for the boss-to-boss gap, and the underside still binds at 17°.

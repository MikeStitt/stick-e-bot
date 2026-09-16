# Run 6p2 — reusing the joints

What the reuse route costs, what it takes, and what it changed. Written from 7a, the spike on
the gripper. The rule it follows is in [`plan.md`](plan.md) under **The joints are reused, not
rebuilt**; the numbers are in [`replan-measured.json`](replan-measured.json); the ids and named
versions are in [`run6p2-documents.json`](run6p2-documents.json).

## 7a — the gripper

Shots are `shots/p7a-copy-*` with [`shots/p7a-copy.log`](shots/p7a-copy.log), and
`shots/p7a-gripper-*` with [`shots/p7a-gripper.log`](shots/p7a-gripper.log).

The gripper went from ten features to four:

```
Clip profile / Clip / Socket from the joint / Union the clip and the socket
```

`Parts (1) Gripper`, no feature errors. The two clip features are the ones that survived the cut
at `Collar circle`; everything below them is the joint, arriving whole.

### What the route costs

Twenty-five clicks from the cut to the named union, counted off `p7a-gripper.log`: four to cut,
ten to derive, five to union, and six on the three renames. The three document copies took six
minutes of wall-clock for all three, about two minutes each, and the copy is once per run rather
than once per part.

The spike itself ran nineteen minutes, and most of that was finding `Derived` rather than using
it. What the route costs a student at the keyboard is not clocked and is not claimed here; 7b
puts it through five more parts, which is where a real per-part number comes from.

### Three things the route needs that were not known

**`Derived` is on no toolbar flyout in this window.** Every caret and every lone icon on the Part
Studio toolbar was opened and it is in none of them. The way in is the tool search: **Alt+c**,
type `derived`, click the result. It arms in about three seconds — the tree grows a `Derived 1`
row and the dialog opens. This contradicts [`build-notes.md`](build-notes.md), under *Deriving the
cavity from the ball-and-socket was tried, and dropped*, which has it the other way round: that
the search result does not arm the tool and a toolbar flyout row does, after about nine seconds.
The flyout row does not exist here. Take the search route.

**The union takes the first tool's name as well as its mate connectors.** Phase 0 settled that
the Boolean keeps the first tool's mate connectors, so the socket goes into the dialog first. It
also renames the merged part — the gripper came out of the union called `Socket body`. Rename the
part back after the union; it is one more right-click and it is easy to miss, because the feature
tree looks right and only the parts list is wrong.

Ordering the socket first turned out to buy nothing, because there was nothing to keep — see
*The joint documents carry no mate connectors* below. The rule still holds; it is the reason the
socket goes first, and it costs nothing to keep doing it.

**The gripper needed no Transform.** Placement `Base origin` put the socket exactly where it
belongs, because `ball-socket-run6p2` and `hand-run6p2` both put the wrist centre on the origin.
The route phase 0 settled is `Derived → Transform → Boolean Union` and the middle step was not
needed here. The head's socket is upside down and will need it; 7b is where that gets used.

Two smaller things worth having in hand: the picker's search box runs on **Enter**, not on typing,
and its tooltip says so; and the picker has no OK button — clicking a part row derives it, and the
picker is closed with its X, which leaves the `Derived` dialog standing.

### Measured against the from-scratch gripper

Both parts read off named versions: `hand-run6p2-2026-08-15` against `hand-run6-2026-08-15`. The
bounding box is identical to four decimals, x −4.6829…4.6829, y −5.0000…4.8280,
z −12.0000…1.3500. So are the slit planes at x and y ±0.4000,
the slit floors at z −4.1500, the collar top at z 1.3500, the 5.5000 slit depth, and the cavity's
r 3.2000 on the origin.

The volume is not identical: **544.6419 mm³ against 520.4792 mm³**, 4.6 percent, the derived one
heavier. Three differences, and they are one difference:

| | run 6, from scratch | run 6p2, derived |
| --- | --- | --- |
| cavity faces | four, 17.8924 mm² each | one, 60.8973 mm² |
| slit walls | eight, 13.2928 mm² each | eight, 8.9601 and 9.2599 mm² |
| clip side wall meets the collar at | z −3.5489 | z −2.0000 |

**The slits cross the axis in run 6 and stop short of it in the joint.** That is what the cavity
face count says: two slots that cross cut the spherical cavity into four separate patches, and
slots that die out before the middle leave it one. Slits that stop short remove less material,
which is the volume. The clip's own features were untouched by the cut, so the third row is the
collar's outer profile differing where the clip runs into it — same root cause.

**The derived gripper is the faithful one.** The joint's own `Socket body`, measured off
`ball-socket-run6p2-2026-08-15`, has eight slit walls of 10.3269 mm², four run-out slivers of
1.7327 mm², and a single cavity face of 80.1417 mm². The run6p2 gripper carries that topology
exactly, with the wall areas trimmed where the clip's union eats into them. Phase 4's from-scratch
socket is the one that differs from the joint it was meant to be a copy of.

This is the replan's own case, measured rather than asserted: five hand-built sockets did not stay
the same socket. Phase 5 measured every part against `target.json` and it passed, because
`target.json` does not pin the slit topology. The four cavity **areas** agreeing to the fourth
decimal, which [`evaluation.md`](evaluation.md) reads as evidence the brief is followable, is
still evidence about the brief — and it is now also visible that equal areas did not mean equal
parts.

Nothing here changes the joints. `ball-socket-run6p2` is a copy of `ball-socket-run61` and its
socket is the one every part now derives.

## 7b — the rest of the parts

Shots are `shots/p7b-copy2-*` with [`shots/p7b-copy.log`](shots/p7b-copy.log), and one set per
part.

### Cut the joint's features, not everything after them

[`plan.md`](plan.md)'s rule says to delete the first feature that re-creates a joint **and
everything after it**, and to rebuild whatever of the part's own work sat below the cut. On the
foot that meant `Groove profile`, `Sole groove` and `Sole ribs` — three features with nothing to
do with the socket, already built and already shot, thrown away and re-performed by hand. Half an
hour went into redrawing one 3 × 1 rectangle before it was clear this was the wrong trade.

**A joint's features are a contiguous block, and only that block has to go.** On the foot the
socket is `Collar circle` through `Four slits`; the sole groove sits on the plate and the ribs
pattern the groove, so neither depends on it. Selecting that range and deleting it left
`Foot outline`, `Foot plate`, `Top round`, `Groove profile`, `Sole groove` and `Sole ribs`
standing with no errors, and the derive, the pedestal and the union went on the end.

The one thing that must go with the block is the part's **mate connector on the joint** — the
foot's `Socket`, made in phase 6. It is placed on the socket's own geometry, and the derived
socket brings its connectors in with it, so it is deleted rather than repaired.

This is the rule 7b uses for the rest of the parts, and it is what makes plan step 5 — *the
prefix is already recorded, so it is not re-performed and not re-shot* — true of the middle of a
tree as well as the top of one. The foot was rebuilt twice to find it: the first `foot-run6p2`
was dropped and the document copied again.

### The foot needs a pedestal, and that settles the 7.35 collar

The plan left open whether the standard socket drops into the foot unchanged.
**It does not, and the first union proved it by leaving two parts.** The standard collar is 5.5
tall with its foot at z −4.15; the foot plate's top face is at z −6. The socket hangs 1.85 clear
of the plate and never touches it.

So the foot gets a `Pedestal circle` — the same Ø9.4 circle on the plate's own top face that run
6's `Collar circle` used — extruded **1.85** as `Pedestal under the socket`, merged into the
foot. The default direction off that face already points up, the same as run 6's collar extrude;
ticking **Direction** turns it into a query for a direction entity and the feature fails until
something is put in it. `Up to part` fails here too: the pedestal's footprint matches the collar
exactly, so under the four slits there is no socket above to stop against.

That resolves what [`audit.md`](audit.md) carried as a disagreement between `foot.md` and
`design-note.md`. **The foot's 7.35 is the standard 5.5 socket standing on 1.85 of the foot's own
pedestal.** Neither brief was wrong; the collar is standard and the pedestal belongs to the foot.

### Measured against the from-scratch foot

`foot-run6p2-2026-08-15` against `foot-run6-2026-08-15-2`. The bounding box is identical —
x ±12.0000, y −32.0000…16.0000, z −12.0000…1.3500 — and the volume is **4912.4451 mm³ against
4875.8691**, +36.5760, the derived one heavier. The same difference as the gripper's, in the same
direction:

| | run 6, from scratch | run 6p2, derived |
| --- | --- | --- |
| cavity faces | four, 17.8924 mm² each | one, 80.1417 mm² |
| slit walls | eight, 21.2162 mm² each | eight, 10.3269 mm² each |
| collar outside | four cylinders r 4.7000, 48.3760 mm² each | one, 199.4313 mm² |
| plate's top face | 410.0822 mm² | 395.7004 mm² |

The 10.3269 walls and the four 1.7327 slivers are the joint's own numbers, unchanged — the foot
carries `Socket body` exactly as `ball-socket-run6p2` publishes it. Run 6's slits crossed the
axis, which is why its cavity comes back as four patches and its collar as four separate
cylinders; the joint's stop short, so both are continuous. The plate's top face loses 14.3818 mm²
because run 6's four slits ran down to the plate and left four strips of it showing, and the
pedestal is a full disc. The extra four slivers at 1.7555 mm² are where the slits die out against
the pedestal.

Two parts measured, two parts where **the from-scratch socket is the one that differs from the
joint**, in the same way, for the same reason.

### The joint documents carry no mate connectors

Read off the feature lists of `ball-socket-run6p2-2026-08-15` and `hinge-run6p2-2026-08-15`:
seven features and twenty-six features, and **not one `mateConnector` among them**. The joints
were built as geometry, and phase 6 put the connectors on the parts, not on the joints — the
table of all twelve in [`build-notes.md`](build-notes.md) lists torso, head, hand, foot and the
two limbs, and neither joint document.

So a derive brings no connector with it, and the cut takes the part's own away. `hand-run6p2`,
`foot-run6p2` and `head-run6p2` were all published with **none**, which reads as fine in the
Part Studio and only shows up when an assembly asks for one.

**Every 6p2 part has to be given its phase-6 connectors again**, from the table in
`build-notes.md`. That is a step in the route, not an afterthought, and it is the thing 7c needs
before it can mate anything.

The three were given theirs in a pass of their own, `p2/e85.py`, one document at a time. Each is
a Mate connector started from `Origin` in the feature list — no viewport pick, so no hover to
settle — and the head's is dropped to its socket centre by typing −22.15 into the third Move box.
Phase 6 picked a point entity on the head instead; the station that comes out is the same.
Shots are `shots/p7b-hand-*`, `shots/p7b-foot-*` and `shots/p7b-head-*`, appended to each part's
own log.

| document | connector | origin | version |
| --- | --- | --- | --- |
| `hand-run6p2` | Socket | (0, 0, 0) | `hand-run6p2-mates-2026-08-15` |
| `foot-run6p2` | Socket | (0, 0, 0) | `foot-run6p2-mates-2026-08-15` |
| `head-run6p2` | Neck socket | (0, 0, −22.15) | `head-run6p2-mates-2026-08-15` |

All three read back z(0, 0, 1) x(1, 0, 0). The version ids are in
[`run6p2-documents.json`](run6p2-documents.json), and those are the versions 7c mates from. The
torso and the two limbs built their connectors during the build, so nothing is owed there.

### The head: a feature below the cut went with it, and the socket needed turning over

Shots are `shots/p7b-head-*` with [`shots/p7b-head.log`](shots/p7b-head.log).

The head's socket block is `Collar circle` through `Second slit pair`, and `Head shell` sits
below it. The shell takes a face of `Head body`, not of the socket, so on the reading above it
should have stood. **It was deleted with the block anyway.** Onshape stores a picked face as an
id that traces back through whatever last rebuilt the body, and `Cavity from ball` was set to
merge with all, so the shell's query ran through the socket. The `Neck socket` mate connector,
which really is placed on `Cavity profile`, survived the same delete and had to be removed by
hand — so the cascade is not simply "everything that depends on the block".

**Check the tree after the cut against the tree before it**, rather than assuming the block came
out cleanly. `Head shell` went back on the end, which is where run 6 had it too: after the
socket, so the 1.2 wall runs through the collar the same way.

The head is the part that needs the middle step of the route. Its socket is the standard one
turned end for end — the cavity centre sits 1.35 above the collar's open rim on both, but the
head's rim faces down. Two transforms do it:

| feature | what it is |
| --- | --- |
| `Turn the socket over` | Transform, **Rotate**, axis `Face of Head body`, 180° |
| `Drop the socket to the neck` | Transform, **Translate by XYZ**, z −22.15 |

**Rotate wants a line, an edge or a cylindrical face, and a plane will not do** — the `Front`
plane was offered and the field stayed empty. The head hands one over for free: `Head profile`
draws its top as a centre-point arc on the origin, so the dome is a cylinder of radius 18 whose
axis is the y axis through the origin. Clicking the dome is the axis. Half a turn about y is the
same body as half a turn about x here, because the socket's slits sit on the x = 0 and y = 0
planes and its collar is a revolve. The Transform list holds Translate by line, by distance, by
XYZ, by mate connectors, Rotate, Copy in place and Scale — there is no Mirror.

### Measured against the from-scratch head

`head-run6p2-2026-08-15` against `head-run6-2026-08-14`. The bounding box is identical —
x ±18.0000, y −16.5000…15.0000, z −23.5000…18.0000 — and the volume is **6021.6944 mm³ against
6019.0314**, +2.6630.

| | run 6, from scratch | run 6p2, derived |
| --- | --- | --- |
| cavity, sphere r 3.2000 | four, 17.8924 mm² each | one, 80.1417 mm² |
| slit walls | eight, 13.2928 mm² each | eight, 10.3269 mm² each, and four run-outs of 1.7327 |
| the shell's dome, sphere r 4.4000 | four, 1.9710 mm² each | those four, and one more of 6.9698 |

The third row is the shell doing to the derived socket what it did to the hand-built one. The
1.2 wall leaves the r 3.2 cup and offsets a second sphere at r 4.4 outside it, exactly as run 3
predicted and run 6 recorded; the difference is that run 6's crossing slits leave that dome in
four pieces and the joint's leave it whole with the run-outs beside it. **Deriving a joint does
not protect it from what comes after** — the head's socket is the standard socket with 1.2 of
wall left in it, and it is the head's own shell that decides that, not the joint document.

### The socket-clevis limb: the hinge reuses, and the joint brings limb with it

Shots are `shots/p7b-limb-socket-clevis-*` with
[`shots/p7b-limb-socket-clevis.log`](shots/p7b-limb-socket-clevis.log).

This is the part the plan pointed at, and the answer is **yes**. Twenty features became six:

```
Limb circle / Limb stock / Socket from the joint / Fork from the joint /
Drop the fork to the elbow / Union the limb and both joints
```

`Collar circle` through `Second ear` is one contiguous block covering both joints, because the
limb's own work is `Limb circle` and `Limb stock` and everything after them is joint. Both
`Hinge` and `Socket` mate connectors went with it. The fork needs one transform,
**Translate by XYZ z −24**: the hinge document draws the fork about a hinge axis on its own
origin, and the limb's elbow is 24 below its socket.

**The joint brings a length of limb with it.** `hinge-run61` starts with `Limb circle` and
`Fork limb`, z −6 to +16 about the hinge axis, so the derived fork already fills z −30 to −8.
Run 6's `Limb stock` ran the whole 25.85 to −30, and unioning the two **filled the fork's slot
back in**: 24 faces where run 6 has 127, the ears and all 48 detent teeth swallowed by a solid
Ø12 cylinder. The stock's Blind depth goes to **3.85**, from the socket's collar foot at −4.15
down to −8, and the joint supplies the rest.

That is a change to a feature above the cut, which the route otherwise leaves alone. It is the
right change: 3.85 is what is left of a 24-long limb once the joint contributes its own 16.

### The two mate connectors, and where Move measures from

`Socket` is the easy one: **Origin entity** the part's `Origin`, nothing else touched. Picking
the origin vertex fills **Owner entity** with the part and sets Attachment to `To owner` by
itself — clicking the owner field after that **clears both**, and the connector builds with an
error. Leave it alone.

`Hinge` needs to sit at (0, 0, −24) with its z along −y so the elbow closes as one revolute.
Realign takes a **Primary axis entity**, and the `Front` plane serves — z comes out (0, −1, 0)
and x (1, 0, 0), which is what run 6 measured. But picking that plane **also drops it into Owner
entity** and knocks Attachment back to None. Clear the owner chip with its × and pick the part
**in the viewport**; a click on the parts-list row does not fill that field.

**Move measures along the connector's own axes, not the part's.** Typing −24 into the z box put
the connector at (0, 24, 0) — realigned, its z is world −y. The drop belongs in the **y** box,
because the realigned connector's own y is world +z. Read back through `evMateConnector`, both
now match run 6's table exactly:

```
Socket  (0, 0,   0)  z(0,  0, 1)  x(1, 0, 0)
Hinge   (0, 0, -24)  z(0, -1, 0)  x(1, 0, 0)
```

### Measured against the from-scratch socket-clevis limb

`limb-socket-clevis-run6p2-2026-08-15-2` against `limb-socket-clevis-run6-2026-08-15`. Same
bounding box — x ±6.0000, y ±6.0000, z −30.0000…1.3500 — and **2051.8491 mm³ against
2041.9142**, +9.9349.

| | run 6, from scratch | run 6p2, derived |
| --- | --- | --- |
| cavity, sphere r 3.2000 | four, 17.8924 mm² each | one, 80.1417 mm² |
| slit walls | eight, 13.2928 mm² each | eight, 10.3269, four run-outs of 1.7327 |
| one more plane face | 58.0814 mm² | 50.7214 mm² |

That third row is a 7.3600 difference, and the head's big planes moved by the same 7.3600 — it
travels with the slits, like everything else here.

**Nothing of the clevis fork appears in the difference at all** — not the slot, not the two ears,
not one of the forty-eight detent teeth. The whole delta is the socket's, and it is the same
delta the gripper, the foot and the head showed. The hinge reuses as cleanly as the ball and
socket.

### The blade-ball limb: both ends derive, and the stock is the 4 between them

Shots are `shots/p7b-limb-blade-ball-*` with
[`shots/p7b-limb-blade-ball.log`](shots/p7b-limb-blade-ball.log). Version
**`limb-blade-ball-run6p2-2026-08-15`** (`3de8c815c62e72076c4c9c07`).

Both ends of this limb are joint, so the whole feature list is derive, place, union, connect:

```
Blade from the joint / Ball from the joint / Drop the ball to the wrist /
Limb section / Limb / Union the limb and both joints / Ball / Hinge
```

The derived blade fills z −15…+6 and the ball, translated z −24, fills −27…−19, so the limb's own
stock is the **4 between them** — a Ø12 circle on the Top plane, Blind, starting 15 below it. The
socket-clevis limb's stock is 3.85 for the same reason; on this one the two joints leave a
straight 4.

**Negative numbers turn a Blind extrude round; the button beside Depth does not.** Depth 4 with a
starting offset of 15 built the stock at z +15…+19, on the far side of the Top plane. The one
toggle on the Depth row, `parameter-state-toggle is-button`, was clicked three times — pressed,
unpressed, pressed — and the body measured +15…+19 every time. Typing **−4** for the depth and
**−15** for the starting offset put it at −19…−15 first go. (The `Direction` checkbox is not a
flip at all; it opens a query for a direction entity, the same trap the foot found.)

**A sphere clicked in the viewport did not reach Origin entity here.** For `Ball` the ball itself is
the natural pick — its centre is the wrist. Clicking it lights the face up and even draws the
connector triad at the sphere's centre, but the field stayed empty, Owner entity ticked itself on
with nothing in it, and the feature built red. Filling the owner by hand did not save it. The cause
is a missing hover, which the torso found later — *The torso*, below. `Ball`
is built the way the socket-clevis `Hinge` was: **Origin entity** the part's `Origin`, **Move**,
−24 in the z box. Nothing is realigned here, so the connector's own z is world z and the drop goes
in the z box — on a realigned connector it would not. `Hinge` is the Origin realigned on the
`Front` plane, no move. Read back through `evMateConnector`:

```
Ball   (0, 0, -24)  z(0,  0, 1)  x(1, 0, 0)
Hinge  (0, 0,   0)  z(0, -1, 0)  x(1, 0, 0)
```

### Measured against the from-scratch blade-ball limb

Same bounding box — x ±6.0000, y ±6.0000, z −27.0000…6.0000 — and the same width in x and in y in
every 5 mm band from −19 up to +6. Volume **1809.5507 mm³ against 1949.1024**, −139.5517, and 165
faces against 161. The difference is all inside, in two places:

| | run 6, from scratch | run 6p2, derived |
| --- | --- | --- |
| stock over the stud's shoulder | Ø12 down to z −20.0000 | stops at −19.0000, the stud's own top |
| Ø3 neck left showing | z −21.4000…−20.0000 | z −21.4000…−19.0000 |
| slit walls, z −10.0000…6.0000 | two, 176.2746 mm² | two, 163.7998 |
| slit root at z −10.0000 | 9.5929 mm² | 12.3990 |
| tab sides at x ±5.4540 | — | four, 26.2500 mm² |
| Ø12 wall | 476.9005, two 33.3986 | 339.2920, two 28.7537 |

Run 6 ran its stock a millimetre past the stud's top face and buried the shoulder; the derived
stud's top is at −19 and the reused stock sits on it. That millimetre of Ø12 less its Ø3 neck is
106 mm³, most of the difference. The rest is the seam: run 6 cut blade and stock from one solid, so
its Ø12 wall runs unbroken from −20 up past the slit, while here the derived blade's wall and the
new stock's meet at −15 and the blade's own slit walls and tab sides stay whole. Nothing of the
blade's pocket, its ring of valleys or its two detent tabs shows in the difference.

### The torso: one derived stud, copied four ways

Shots are `shots/p7b-torso-*` with [`shots/p7b-torso.log`](shots/p7b-torso.log). Version
**`torso-run6p2-2026-08-15`** (`9c8d9298e7fc0ef0f005b0c9`).

The torso carries five ball studs and no sockets, so the whole part reuses one derived body:

```
Torso outline / Torso block / Ball stud from the joint / Pivot lines /
Copy the stud for the neck / Copy the stud for the shoulder /
Move the hip stud to its station / Mirror the hip stud /
Turn the neck stud over / Move the neck stud to its station /
Lay the shoulder stud along x / Reach the shoulder stud out 13 /
Shoulder boss circle / Shoulder boss / Union the shoulder boss and stud /
Tip shoulder 53 deg / Swing shoulder 30 deg forward /
Move the shoulder to its station / Mirror the shoulder /
Union the studs into the torso / Trim ring / Trim the bosses flush /
Neck / Shoulder R / Hip R / Hip L / Shoulder L
```

**A Part Studio takes one Derived per source and configuration.** A second one is refused with
*"Creating multiple Derived features from the same source and configuration is not allowed.
Consider editing the previous Derived feature."* Four studs from one ball-socket document therefore
means one Derived plus **Transform ▸ Copy in place** for each extra, and the copies are named for
what they will become before they are moved.

The derived stud is a ball on a stalk and nothing else — SPHERE r3 on the origin, CYLINDER r1.5 up
to z 5, a flat end 7.0686 mm². The hips and the neck want exactly that, so they are only turned and
moved. The shoulder wants a **Ø8 boss** as well, and the boss is the torso's own work: a circle on
the `Right` plane extruded x −10…+8, which meets the stud's flat end at +8 and runs 10 into the
block. Boss and stud are unioned before the aiming turns, so the two travel together.

The aiming is two turns about the sketched pivot lines and one move, and every number is run 6's:
Rotate −90° about the +y line lays the stalk along −x; Translate 13 in x puts the ball where the
boss can reach it; +53° about +y tips it; −30° about +z swings it forward; Translate (18, 0, 20)
lands the ball at (24.7754, −3.9118, 9.6177). Mirroring across `Right` gives the other side.

Tipped that far, both bosses run out through the top face — their roots sit at z 27.986, nearly 4
above it. The cut that takes them off is a **ring**: two circles on the origin, Ø8 inside and Ø50
outside, extruded Remove from a 24 starting offset. The Ø8 hole is what keeps the neck, which is
the one thing meant to stand above the top face. The cut leaves the top face at 878.3647 mm² over
x ±20.1660 — the block's 864, less the neck stalk's 7.0686, plus the lobe each boss leaves where
it crosses z 24 outside x 18.

**A viewport pick needs a settled hover before the click.** This corrects what the blade-ball limb
recorded above. Ctrl+M, arm `Origin entity`, click a ball, and the field stays empty — but move the
cursor onto the ball, wait for it to light up, *then* click, and the pick lands as
`Face of …` with `Owner entity` filled and `Attachment` set to `To selection` on its own. All five
connectors here are built that way, which is also how run 6 built them: `ON_ENTITY` with
`entityInferenceType: CENTER`, no translations. The blade-ball limb's `Ball` connector is not
wrong — the Origin plus a Move reaches the same point — but it did not need the workaround.

Three more things the route wanted:

* **Transform's type list moves.** `Rotate` is not at a fixed height in the dropdown: a filled
  query chip pushes every row below it down, so a coordinate that picked `Rotate` once picked
  `Translate by line` the next time and the feature built red with an empty axis. The list items
  are read by their own text instead.
* **Rotate needs a line it can see.** The axis will not take a plane, and it will not take a line
  that is behind a part — the pivot sketch has to be shown (right-click ▸ `Show`), and for the
  swing the tipped stud is hidden first so the +z line is uncovered. The part is still picked from
  the parts list while it is hidden.
* **Boolean keeps only the tools whose clicks registered.** A union of four parts came back red
  with one tool in it. The dialog's text is checked after each pick now, and the pick is repeated
  until the part's name is in it. Two parts both called `Ball stud` cannot be told apart by a row
  lookup either, so they are named `Neck stud` and `Shoulder stud` first; `Rename` is missing from
  the context menu whenever more than one row is selected.

### Measured against the from-scratch torso

Identical, against `torso-run6-mates-2026-08-15` (`3a882a1ecb98644fa63a6e8e`): volume
**42890.0333 mm³** both ways, box x ±27.7754, y ±12.0000, z ±32.0000, **20 faces** each, and no
face in one that is not in the other — same surface, same radius, same area, right down to the two
43.1969 mm² boss ends and the 878.3647 top. The five connectors read the same stations:

```
Neck        (0, 0, 29)                            z(0, 0, 1)  x(1, 0, 0)
Shoulder R  (24.7754, -3.9118, 9.6177)            z(0, 0, 1)  x(1, 0, 0)
Shoulder L  (-24.7754, -3.9118, 9.6177)           z(0, 0, 1)  x(1, 0, 0)
Hip R       (12, 0, -29)                          z(0, 0, 1)  x(1, 0, 0)
Hip L       (-12, 0, -29)                         z(0, 0, 1)  x(1, 0, 0)
```

This is the first part of 7b where the derived route lands on the from-scratch part exactly, and
the reason is that the torso reuses only the stud: everything the two runs could have disagreed
about — block, boss, trim — is built the same way in both.

## 7c — the assembly

Shots are `shots/p7c-doc-*` and `shots/p7c-assembly-*`, with
[`shots/p7c-doc.log`](shots/p7c-doc.log) and
[`shots/p7c-assembly.log`](shots/p7c-assembly.log). The robot is
`robot-run6p2-2026-08-15` (`058dd63ee387e60a85040d70`) in `lesson-run6p2`,
[open](https://cad.onshape.com/documents/44e680c797993a1e48b675b6/v/058dd63ee387e60a85040d70/e/b01957cd5e2b54550d905ef1).

### A new document arrives with an assembly in it

`lesson-run6p2` was created empty in Coach Mike Experiments and came with `Part Studio 1`,
`Assembly 1` and a bill of materials already there, so the assembly needs no new tab. Its units are
set the same way every other document's were, from the hamburger menu beside the document name —
**a new document starts in inches**, and the green tick on Workspace units keeps whatever the two
dropdowns say, so the dropdowns are the step and the tick only closes it.

### Name the part before you insert it

`limb-blade-ball-run6p2` still called its part `limb-blade-ball`, because a part that is never
renamed takes the document's name — run 6 hit this too. Insert takes that name into the assembly,
so it is renamed to `Lower limb` and published as `limb-blade-ball-run6p2-named-2026-08-15`
(`cf8fa83d195bcc64303de3b0`). The geometry is untouched. The other five documents already named
their parts during the build.

### The assembly steps are phase 6's, unchanged

Insert reaches a version by searching for the document and pressing Enter; connectors are picked
from the tree by name rather than from the viewport, where fourteen parts stacked on the origin
overlap; the row names are snapshotted before a dialog opens, because the open dialog puts its own
row in the tree; and the mate row appears seconds after the tick, once the solve has run. Nothing
in the 6p2 route changed any of that — the only new thing is which version each instance comes
from.

One rename raced: `Revolute 1` was already renamed to `Right elbow` by the time the retry looked,
and the retry read the missing old name as a failure. The helper now checks for the new name first.

### Measured against the from-scratch robot

Against `robot-run6-2026-08-15` (`cab79923d9e94d9f908d359f`), **all fourteen instances land on
exactly the same transform** — every entry of every matrix, not just the origins:

```
Torso <1>       (0, 0, 0)                Head <1>        (0, 0, 51.2)
Upper limb <1>  (24.8, -3.9, 9.6)        Upper limb <3>  (12, 0, -29)
Lower limb <1>  (24.8, -3.9, -14.4)      Lower limb <3>  (12, 0, -53)
Gripper <1>     (24.8, -3.9, -38.4)      Foot <1>        (12, 0, -77)
```

with the left-hand instances mirrored in x. The thirteen mates match name for name and type for
type, five ball at the neck, shoulders and hips, four revolute at the elbows and knees, four ball
at the wrists and ankles. Every instance's `documentVersion` is a 6p2 named version and none is a
workspace.

**The reuse route reaches the same robot.** Six part documents, each derived from a joint rather
than drawn from scratch, assemble to the assembly phase 6 built by hand.

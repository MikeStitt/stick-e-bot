# Audit — the stickbot document

Audited 2026-08-20 against `stickbot-for-bot-review`
(`did=111f975041ddb104a6028d45`, `wid=38e73619152eec8be2c51f8b`), version **V1** *"First version
that has all internal components"*, plus the neck fix made during the audit.

The document is a second attempt at the whole robot, built to the same specification but with a
different modeling practice: **a joint's future mate point goes at the origin, and the part grows
outward from it by sketching on faces and extruding.** This audit records where that model and
[`robot-build-plan.md`](robot-build-plan.md) agree, where they differ, and what the differences
cost. Nothing in the model was changed by the audit except the one fix noted below, which the
author made.

## Containment

The document reaches no CAD outside itself. Three checks agree:

- `externalreferences` names one document, itself.
- `elementExternalReferences` is empty for every element.
- Every `importDerived` carries an element-only namespace (`e<eid>::m<micro>`), which is the form
  that means same document, same workspace.

**This was not true when the audit started.** `head` derived its socket from
**run6-ball-and-socket V2** (`d421233fbff9374b85bb6cc9`, version `548cc12f00c832f261da8954`), a
Ø9.3659 collar of 239.1478 mm³, where every other socketed part used the internal Ø9.4 collar of
249.6806 mm³. Onshape reported it in sync, because V2 had not moved — the drift was between two
different sockets, which nothing flags. The author repointed it at the internal
`ball and socket` studio. Comparing feature lists before and after, the fix reached one feature
in one studio and changed nothing else.

## What is in the document

Eight Part Studios — `ball and socket`, `hinge`, `body`, `head`, `u limb`, `l limb`, `foot`,
`gripper` — one assembly, one bill of materials. The assembly holds the robot's fourteen printed
instances and mates them with four revolute joints and nine ball joints. Every mate resolves
against a real coordinate system, and the torso is the grounded part. That is the plan's
one-part-per-unique-object rule and its instance list, built.

## Dimensions

### The ball and socket matches exactly

Measured off the faces, not read off the dimensions:

| Feature | Plan | Stickbot |
| ------- | ---- | -------- |
| Ball sphere | r 3.0 | r 3.0 |
| Stalk | r 1.5 | r 1.5 |
| Stud top face | z +5 | z +5 |
| Cavity sphere | r 3.2 | r 3.2 |
| Collar | r 4.7 | r 4.7 |
| Mating face | z +1.35 | z +1.35 |
| Bottom face | z −4.15 | z −4.15 |
| Mouth | r 2.9013 | r 2.9013 |
| Slit | 0.8 wide, floor z −2.65 | 0.8 wide, floor z −2.65 |
| Ball stud volume | 128.6210 mm³ | 128.6210 mm³ |
| Socket body volume | 249.6806 mm³ | 249.6806 mm³ |

Also matching the plan: torso 36 × 48 × 24, foot 48 × 24, head 36 across, limbs Ø12, hip
half-spacing ±12, hinge stub Ø2.0 × 0.8, pocket Ø2.2, detent valley Ø1.0, twenty-four detents
over 360° on a band at r 4.8, blade-to-ear gap 0.3 per side, detent interference 0.3 per side.

### The hinge is the pre-rebalance joint with wider ears

[`experiments/build-briefs/hinge.md`](experiments/build-briefs/hinge.md) records the
pre-rebalance joint as ear 1.2, slot 3.6, blade 3.0 solid, ends on r5.81. Stickbot is that joint
with the ear taken to 3.0. Measured off the planar faces, with the hinge axis on Y:

| Feature | Plan, post-rebalance | Stickbot |
| ------- | -------------------- | -------- |
| Blade thickness | 5.0 | 3.0, faces at y ±1.5 |
| Slot | 5.6 | 3.6, ear inner faces at ±1.8 |
| Ear thickness | 3.2 | 3.0, outer faces at ±4.8 |
| Fork span | 12.0, the ear's outer surface is the Ø12 cylinder | 9.6, flat, 1.2 inside the cylinder |
| Blade round end | r 6 | r 5.8 |
| Fork round end | r 6 | r 5.81 |
| Detent bump | Ø0.9 | Ø0.8 |
| Valley depth | 0.45 | 0.8 |

Two consequences. The blade has no relief slit, so the plan's 0.8 × 16 slit and the 2.1 mm tabs
either side of it do not exist here — the blade is solid. And the fork no longer reaches the limb
surface, so the plan's rule that every layer of the fork is a full slice of the Ø12 limb is not
what this model does.

**The snap is reversed, and the reversal is an improvement.** The plan puts stubs on the ears and
blind pockets in the blade. Stickbot puts the stub on the blade, standing 0.8 proud to y ±2.3,
and cuts the fork through with a Ø2.2 hole. A through hole prints without a ceiling. The
stiffness argument behind the rebalance does not depend on which side the stub is on, so this
change and the rebalance are independent.

### Other differences

| Measurement | Plan | Stickbot |
| ----------- | ---- | -------- |
| Gripper bar hole | Ø3.2 | Ø3.3 |
| Limb segment | `#limbSeg` 24 | 35.42 on `u limb`, 37.91 on `l limb` |
| Shoulder root | half-spacing 18, arm centerline 27 | ball at (±24.775, −3.912, +9.618) |
| Neck stud | — | ball center 2.402 above the torso's top face |
| Hip stud | — | ball center 5.0 below the torso's bottom face |

The limb difference is structural rather than a number. Stickbot's limb rod is a 4 mm connector,
and the segment's length comes from the joint pieces, each of which carries its own Ø12 rod.

The shoulder is a different design, not a moved number: a revolved profile at 53° on a plane
built at 60°, where the plan roots a stud on the torso's side face.

The neck and hip studs stand off their faces by different amounts. Whether that is deliberate is
an open question.

## Build order

The stated practice — mate point at the origin, part grown outward — is in the model and is
applied consistently.

**The ball and socket needs no scaffolding.** The plan revolves the stud, builds a Ø12 × 10 limb
stub, sketches the collar on the stub's top face and extrudes it 5.5 upward. Stickbot revolves
the stud and then makes the collar in **one** extrude from the Top plane through the ball center:
`#grip` up and `#collar - #grip` down, landing z −4.15 to +1.35. There is no stub and no base, so
the studio holds only the two mating pieces. The Boolean is the same as the plan's: subtract with
offset, offset all, distance `#fit`, keep tools.

This removes the thing the plan has to explain away — that the base is scaffolding rather than a
robot feature — so it is a better order to teach as well as a better model.

**Every consumer follows one shape.** Build the host, place named mate connectors,
`importDerived` the joint piece at the origin, `transform` it onto its connector, union, then
expose the connectors the assembly needs. Five of the six consumers move the joint with
`TRANSFORM_MATE_CONNECTORS`, so it lands by connector rather than by coordinate.

**The head is the exception.** After `get socket` it rotates 180° and then translates by a typed
`dz = -22.15 mm`. Every other part would survive a change to the torso or to the joint; the head
would land in the wrong place with no error.

**`foot` starts from its derived socket** before any of its own geometry, where every other
consumer builds the host shape first. It works; it is the odd one out.

## Variables

This is the widest gap between the model and the plan.

`ball and socket` carries the plan's ten variables, with the same names and the same values, and
every dimension in that studio is an expression: `#ball/2`, `#stalk/2`, `#stud_len`,
`#ball + 2*#fit + 2*#wall`, `#fit`, `#slit/2`, `#slit_in`, `#slit_out`, `#collar - #grip`,
`#collar - #wall`. Writing the collar as `#ball + 2*#fit + 2*#wall` rather than a typed 9.4 says
where the number comes from, which is what the plan asks a variable to do.

**The other seven studios declare no variables and reference none.** Every dimension is a typed
number. So `#torsoH`, `#torsoW`, `#torsoD` and `#limbSeg` — the four that drive the robot's size
— do not exist anywhere in the model. The torso is three typed numbers that happen to equal
36, 48 and 24. The proportions the plan records are all true of the built numbers and none of
them is expressed.

Onshape scopes variables to a Part Studio, so the joint's ten are unreachable from the six
studios that consume the joint. Sharing them across studios needs a mechanism, not discipline.

## Defects

- **Five mate connectors in `body` are in error**: `neck connector`, `left shoulder connector`,
  `r shoulder connector` twice, and `l hip connector`. Each reports *"Cannot resolve entities. 2
  missing selections"*, each is hidden, and all sit after `add neck to body`, so a Boolean took
  their references. The assembly mates against the four earlier, healthy connectors instead, so
  these are dead weight rather than a live fault. They were already broken before the neck fix.
- **Two features share the name `r shoulder connector`.** The sequence runs left shoulder, r
  shoulder, l hip, r shoulder, so the last is presumably meant to be `r hip connector`.
- **`Boolean 1` in `head` was never named.**
- **`59.99999999999998 deg`** in `body`'s *shoulder rotate about z* — dragged, not typed.
- **Stray asterisks** in two expressions: `5.81*mm` in the hinge's fork outline and `4.0*mm` in
  the head's mouth. Onshape accepts them; they read oddly in a dimension box a student is copying.
- **`l limb`'s second mate connector carries `translationZ = -2.3 mm`**, the only hand-nudged
  connector offset in the document.

## Decisions taken from this audit

**`#fit` becomes 0.02.** The 0.2 in the model was not the intended value. The joint is fully
parametric, so this is one field, and everything follows from it:

| Quantity | fit 0.2 | fit 0.02 |
| -------- | ------- | -------- |
| Cavity radius | 3.2 | 3.02 |
| Collar Ø | 9.4 | 9.04 |
| Mouth Ø | 5.803 | 5.403 |
| Retention, on diameter | 0.197 | 0.597 |
| Travel per tab, on radius | 0.099 | 0.299 |
| Slit reach inside the mouth | 0.401 | 0.202 |
| Slit past the rim | 1.30 | 1.48 |

`#wall` still comes out at exactly 1.5, so the collar stays three perimeters thick.

Two things follow that are worth measuring rather than assuming. Retention triples, so the mouth
must open three times as far on the same four slits and the same 1.5 mm floor — the brief already
records that nobody has measured whether those tabs flex, and this makes that the question.
And the collar drops to Ø9.04 on every socketed part, which is visible in every figure that shows
one.

`#slit_in` at 2.5 still breaks into the mouth, with 0.202 of overlap rather than 0.401. It works.
Holding the old proportion would want about 2.3.

**The rebalanced hinge is to be tried as an experiment.** The rebalance was missed when stickbot
was built.

> **Reversed later the same day.** The robot keeps the hinge as built in stickbot, and the
> rebalance is not adopted. The numbers below describe what a rebalanced hinge would cost from
> this tree; they are no longer a plan.
> [`experiments/build-briefs/hinge.md`](experiments/build-briefs/hinge.md) is the joint's
> specification. Reaching it from stickbot's tree changes four features and adds one pair:

- `blade blank` — 3.0 to 5.0 thick
- `fork blank` — ear 3.0 to 3.2, inner face 1.8 to 2.8, gap unchanged at 0.3
- `blade profile` and `fork outline` — round ends r 5.8 and r 5.81 to r 6
- new — the blade's relief slit, 0.8 wide and 16 deep down the centerline, leaving the 2.1 tabs

At ear 3.2 the outer face lands at exactly ±6.0, which is the Ø12 surface, so `trim fork to arm`
— the Ø12 intersect already in the tree — begins doing the job the brief describes instead of
trimming nothing. The build order already accommodates the change.

The detent stack moves with the blade: the brief records that widening it shifts every station
out by 1.0 and changes none of the clearances, so the band goes to r 4.40 → 5.20 and the 0.3 per
side interference survives.

## Open question — what this does to the capture

If stickbot's build order wins, the guide's
ball and socket page, `robot-guide4`'s, teaches a build
the model no longer performs: the page builds a limb stub and sketches the collar on its top
face, and stickbot has neither. Every frame under that page's `images/ball_and_socket/` shows the
old path. Three ways it could go:

1. Retake the page against stickbot. The new order is easier to teach, because there is no
   scaffolding to explain away. It costs a capture run.
2. Change stickbot to match the guide. Cheapest in frames, and it puts the stub back.
3. Retake only what moved. The stud sketch and revolve frames survive; the collar sketch, the
   collar extrude and anything showing the stub do not.

`#fit` at 0.02 makes the collar Ø9.04, so any frame showing a measured collar or a dimension box
holding 9.4 goes stale whichever option is chosen.

Stickbot's feature names — *stud profile*, *revolve stud*, *collar profile*, *collar blank*,
*cavity from ball*, *slit profile*, *relief slits* — map onto the identifier grammar in
[`build/steps.md`](build/steps.md) without translation, so adopting them would let the plan
headings and the frame stems take the model's own names.

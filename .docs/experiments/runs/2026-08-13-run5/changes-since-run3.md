# Run 5 — what changed since run 3 built the CAD

Phase 1 of [`../../design-into-cad.md`](../../design-into-cad.md). Derived from
`git diff 5ff5f3d..HEAD -- build-briefs sketches`, where `5ff5f3d` is where run 3's six part
waves landed. Everything below is design that was written after that and never reached a part
studio — run 4 copied run 3's geometry unchanged.

This is the *anticipated* list. The audit in phase 3 is what decides whether each item is really
a delta, and by what route it gets repaired. Nothing here is a measurement.

## Torso

| What | Written | In the CAD |
| ---- | ------- | ---------- |
| shoulder stud direction | 53° below horizontal, 30° toward the front | leaves the side face square |
| shoulder stud root | side face at x = ±18, 4 mm below the top face | side face, on the joint station |
| shoulder stud shape | first 8 mm Ø8 boss coaxial with the stalk, last 5 mm Ø3 stalk, then the Ø6 ball | plain Ø3 stalk |
| shoulder stud length | 13 mm from side face to ball center, ball 6.775 out and 10.382 below the root | ball center at (±23, 0, +24) |
| boss top | cut flush where it crosses the torso's top face | no boss |
| neck boss | Ø12 on the top face, on the axis | never built — plain stalk |
| hip stud | plain Ø3 stalk standing 5 off the bottom face | matches |

The shoulder is the largest single change in the robot and the reason the brief exists: with a
plain 5 mm stand-off the Ø12 upper arm fouls the torso through the first 12.19° of its swing, so
the ±37.09° the joint allows is not available. Acceptance check is the least clearance between arm
and torso across the swing.

## Hinge — both limb halves

| What | Written | In the CAD |
| ---- | ------- | ---------- |
| blade | 5.0 | 3.0 |
| slot | 5.6 | 3.6 |
| ear | 3.2 | 1.2 |
| blade width, the chord | 10.909 at ±2.5 | 11.62 at ±1.5 |
| ear inner chord | 10.613 at ±2.8 | 11.45 at ±1.8 |
| ear outer chord | **gone** — the ear's outer surface is the Ø12 cylinder, there is no outer plane | 10.39 |
| round ends | r6, which is `#limbD / 2` | r5.81 |
| blade stands out | 16, so the blade's own limb stops 10 from the pin axis | rod stops 6.11 from the axis |
| clevis slot | 17 deep from a tip standing 6 out, so the root sits 11 behind the axis | root 6.11 behind |
| slit | **new** — 0.8 wide, 16 deep, down the blade's middle, open at the round end, leaving two tabs of 2.1 | no slit, solid blade |
| detent crest | ±2.2 | ±1.2 |
| detent valley floor | ±2.05 | ±1.05 |
| detent land | ±2.5 | ±1.5 |
| ear face | ±2.8 | ±1.8 |

The detent band r4.40 → 5.20 does not move, and neither does any *difference* in the stack — the
rebalance shifted every station out by the same 1.0. Against an r6 end the rim outboard of the
valley ring becomes 0.70 rather than 0.26.

Why it changed: ear and blade are springs in series, so they carry the same force and split the
movement inversely with stiffness. The as-built 1.2 ear is 16.8× more flexible than the solid 3.0
blade, takes 0.472 of the 0.5 alone, and sits at 46.2 MPa against PETG's 50. The written joint
splits 0.20 / 0.30 at about 19 MPa and presses at 3.2 kgf.

## Foot

| What | Written | In the CAD |
| ---- | ------- | ---------- |
| ankle socket relief slits | four, as on every other socket | **none** — the collar is one unslit cylinder |
| collar length | 7.35 | 7.35 — **a record, not a target.** Do not repair toward 5.5; the plate sets it |
| symmetry about its own fore-and-aft centerline | required, so one part serves both sides | r4 features at (5.14, 5.94) and (7.10, −6.22) are not a mirror pair |
| which axis the length runs along | the brief says Y; the model builds X and the assembly turns it 90° | conflict, not a repair — see phase 4 |

The unslit collar is the one joint on the robot that cannot be assembled: the whole circumference
would have to stretch to pass a Ø6 ball through a Ø5.803 mouth.

## Head

| What | Written | In the CAD |
| ---- | ------- | ---------- |
| socket | bored into the boss face, not a collar | to be confirmed by the audit |
| recess step | 1.0, and it buys 11.4°, not the 42° an earlier draft claimed | 1.0 |
| head center / underside / top | +45.65 / +27.65 / +63.65 | measured at +45.65 in run 4 |

The head's tilt argument needs the torso's neck boss, which was never built. That is a cross-part
dependency, not a head repair.

## Gripper

| What | Written | In the CAD |
| ---- | ------- | ---------- |
| clip bore | 3.3 built; the radial `#fit` convention would give 3.6 | 3.3, measured r1.650 |

Marked `proposed` in the brief and unresolved: the row asks the builder to say which convention was
used and why. Not a repair until somebody decides.

## Limbs

Follows the hinge — the fork now spans the whole limb, and the ear is a slice of the Ø12 cylinder
that thins to nothing at |x| = 5.3066, below one nozzle width over the last 0.231 mm.

## The figure as a whole

The height is no longer a target. r1 set 150 and fitted the stations to it; r2 stacks the stations
and reports the sum, which is **152.65**. Nothing is to be adjusted to make 150 come out. The
run 4 assembly already measures 152.65, so this is a change in what the drawing claims, not in the
geometry.

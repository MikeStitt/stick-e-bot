# draft9p1p2 — the register

What was resolved, what was not, and what was never attempted, in those words. The
measurements are produced by [`check.py`](check.py), which reads the model back and compares
all 40 rows with `instructions/robot-guide/make_plans.py`; this file says where each thing
stands and, for the open ones, what it turns on.

## What was built

One document, `stickbot-draft9p1p2`, four Part Studios, six parts.

| Tab | Parts | Runs from | to |
| --- | ----- | --------- | -- |
| `hinge` | `fork`, `blade` | the fork's tip at −12 | the fork's rod end at +40.5 |
| `u limb` | `u limb` | the fork's tip at −12 | the socket's rim at +49.947 |
| `l limb` | `l limb` | the ball's far pole at −54 | the tongue's tip at +12 |
| `ball and socket` | `socket`, `ball stud` | the socket's stub at +28.5 | the stud's stub at +70 |

Every station is on the limb axis with the hinge pin at zero. The `u limb` is a thigh:
socket up, coaxial, its rod `ROD_FORK` long. The `l limb` is a shin: a ball stud on the far
end, its rod `ROD_BLADE` long. The two mate at the knee, so the pair is the joint this
draft exists to press.

| id | |
| -- | - |
| document | `2741f86a206bbf1af0dca541` |
| workspace | `1f88a856b82f57bbace9bd09` |
| `hinge` | `bf1c4ccf8e21be20bc22bc82` |
| `u limb` | `36f08721db339cb37ff4c4cf` |
| `l limb` | `bdce5bd8dd76aed29a46f749` |
| `ball and socket` | `060aa8d43f544377f3ecda6a` |

## Resolved

Each of these has a measurement behind it. `check.py` runs 40 rows and all 40 agree.

- **The settled hinge is built.** Forty-eight teeth and forty-eight valleys, each tooth a
  cone of half angle 45.000° whose flat top measures 0.1257 mm², which is Ø `TOOTH_FLAT`.
- **The seat is a land and the rest of the slot is relieved.** One planar face at
  x ±5.200 on each ear, and the relieved face at x ±5.600 on each side, in the two patches
  the land divides it into.
- **The land's ramps came out of one section.** The slot is a single cut from a profile that
  carries the relief, the land and both ramps; the outboard ramp runs off the ear's round
  end by itself, which is what the review said it would do.
- **The slit cuts the axle, and the axle is a stub on each leaf.** The Ø `STUB` cylinder reads
  as two patches, one standing off each leaf, with their end faces at x ±6.000, which is
  `STUB_PROUD` off the leaf. A third patch would be a shaft across the gap, and a shaft ties
  the two leaves together at the pin, where `hinge_spring.press` has them free to bend.
- **Each limb's rod stops at its own root.** The fork's rod ends at +39, which is
  `EAR_FREE + ROD_FORK`, and the blade's at −38, which is `TAB_FREE + ROD_BLADE`. The
  burial the review found in draft9p3 cannot happen here, because the rod is drawn from the
  root outward rather than from the joint inward.
- **The socket's mouth is not cut, and measures right anyway.** The cavity's center sits
  `GRIP` below the rim, so where the sphere breaks the rim face it leaves Ø `MOUTH`. One
  finger's top face measures 15.3301 mm², which is the annulus less the four slits, to four
  decimal places.
- **Each socket slit cuts into the hollow rather than stopping in the wall.** Where it does,
  the cavity's widest surviving point stops being its own equator and becomes the edge of a
  slit, at 6.0271 from the axis, which is what the sphere's face reports.
- **The socket springs back rather than yielding.** The collar wall is `COLLAR_WALL` 1.5 and
  the slits bottom out `BALL / 3` below the ball's center, so a finger is `SLIT_D` 5.9465
  long. The mouth has to open 0.240 mm on the radius to let the ball's equator through and
  can open 0.404 before a finger reaches PETG's yield, which is 59% of yield at the worst
  station. `check.py` reads the wall off the collar's own radius and the free length off the
  station the slit floors sit at. What the calculation says the pair should cost is 5.24 kgf
  to press together and the same to pull apart; [`tools/socket_spring.py`](../../../../tools/socket_spring.py)
  is the derivation, and nobody has pressed one.
- **Both parts are named.** `fork` and `blade`, not `Part 1` and `Part 2`, which closes for
  this document the finding the review raised against draft9p3.
- **The print files are watertight.** `u-limb.stl` is 22414 triangles and `l-limb.stl` is
  19646, both with zero open edges, and both bounding boxes match the model exactly. They
  are in [`print/`](print/) with the two coupon parts beside them, and
  [`print/README.md`](print/README.md) says which way up they go on the bed and why.

## The frame the build turned on

The slit is cut along the axis the joint opens, which is the pin. That makes the tongue a
tuning fork: two leaves `LEAF` thick, separated across the pin by `SLIT` and joined only at
the root. It follows that the pin is world X, the limb is world Y, the chord is world
Z, and each of the three default planes has exactly one job. `build.py` says which.

Every part is a profile prism cut back to the rod: the outline is sketched on Right,
extruded across the pin, then intersected with the Ø `LIMB` circle drawn on Front. No fillet
appears anywhere in the document, because the rounding is the rod.

## What the REST route taught, so it is not retested

These live in `build.py`'s helpers, which is where they are used.

- **An extrude's starting offset has its own direction flip.** `oppositeDirection` turns the
  extrude around and leaves the start plane where it was, so the second ring of teeth landed
  inside the leaf it was meant to stand on and Onshape reported the feature `INFO`, not
  failed. `startOffsetOppositeDirection` is the other half.
- **`draftPullDirection` true tapers inward.** False widens: a Ø `CONE_D` circle drafted 45°
  over `TOOTH_PROUD` came back Ø2.8 at the far end instead of Ø `TOOTH_FLAT`. Both were
  measured off the two planar faces, not eyeballed.
- **A drafted extrude makes every tooth at once.** Twenty-four circles in one sketch, one
  extrude, and no circular pattern — which matters, because the `Origin` feature exposes no
  edges at all, so there is no origin axis to pattern about without first making a mate
  connector.
- **`THROUGH_ALL` beats a big number.** Every cut in this document is through-all and
  symmetric, so no depth in the tree is a guess about how far is far enough.
- **A boolean needs its scope named once both members exist.** The fork's slot would eat the
  blade's tongue and its valleys would drill the blade's teeth; `defaultScope` false with the
  member's own body in `booleanScope` is what keeps each member's cuts to itself.
- **A cylindrical face is an axis.** The collar and the stalk are turned about the limb axis,
  so either one names that axis for the revolve that makes the cavity or the ball.

## Not resolved

- **Nobody has pressed one.** Every number in `.docs/reviews/hinge/` — 5.18 kgf to press,
  414.4 N·mm to hold, and the way that falls as the valley rims round — is a calculation.
  This draft exists to make the part that answers it, and the answer is not in yet.
- **The `hinge` tab's pair is drawn mated and has never been mated.** The two parts share the
  pin and the tooth ring by construction, not by an assembly, so nothing has checked that the
  joint can be brought together along any path a hand could take.

## Knowingly not met

The plan claims `req.model`. Three of its rows are not met, and the reason is the same one in
each case: the REST feature API writes sketch geometry as coordinates, and a constraint would
have to be authored entity by entity.

- **`req.model.design_intent`.** No sketch in this document is fully defined. Eight driving
  lengths are variables and every feature parameter that has a length in it reads one, but
  the profiles carry typed coordinates. The model does not survive a driving-dimension
  change; re-running `build.py` is what a change means here, and that file is the design
  source.
- **`req.model.derive`.** The `u limb` and `l limb` tabs rebuild the fork and the blade
  rather than deriving them from the `hinge` tab. One function builds each member and three
  tabs call it, so there is still one source, but it is in the repository rather than in the
  document.
- **`req.model.anchored`.** Sketches sit on the three default planes at typed stations rather
  than on geometry that already gives the position.

None of this carries. A tutorial that teaches this joint has to be built in the GUI, fully
defined and derived, the way every other tab in the guide is.

## Not attempted

- **The `robot sizes` tab.** The plan asked for five tabs and four were built. A Variable
  Studio that no part studio references would give the eight driving lengths a fourth home
  rather than removing the three they have, and wiring a part studio to a Variable Studio
  through the REST API was not tried. The eight sit in each tab instead, where the feature
  parameters can read them.
- **An assembly.** `Assembly 1` is empty. The hinge tab already shows the pair in position,
  and the plan's gates are the geometry gates only.

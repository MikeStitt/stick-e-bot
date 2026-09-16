# draft9p1p4 — the register

What this draft built, what it proved, and what it leaves open. The measurements come from
[`check.py`](check.py), which imports `instructions/robot-guide/make_plans.py` and reads the model
back through `bodydetails`, `parts` and `boundingboxes`; [`build-notes.md`](build-notes.md) says how
each tab was edited and where the build departed from [`plan.md`](plan.md).

This draft writes no page. It is a CAD reference for a later draft to inherit, edit and print from.

## What was built

One document holding a Variable Studio and six Part Studios, with eight parts among them.

| Tab | Parts | Runs from | to |
| --- | ----- | --------- | -- |
| `robot sizes` | | 20 rows | |
| `ball and socket` | `Ball stud`, `Socket body` | the socket's base at -10 | the stud's face at +10 |
| `hinge` | `fork`, `blade` | the blade's rod end at -38 | the fork's rod end at +38 |
| `u limb` | `u limb` | the fork's tip at -60 | the socket's rim at +2.2205 |
| `l limb` | `l limb` | the ball's far pole at -54 | the tongue's tip at +12 |
| `ball with cylinder` | `ball with cylinder` | the ball's far pole at -6 | the handle's far face at +22 |
| `socket with cylinder` | `socket with cylinder` | the handle's far face at -22 | the socket's rim at +2.2205 |

Every station is on the joint axis with the joint center at zero. The two limbs carry the same 48
between joint centers, and the two coupons carry the same 22 from joint center to the handle's far
face.

| id | |
| -- | - |
| document `stickbot-draft9p1p4` | `eca1f9c7feff156a3303d563` |
| workspace | `3a7d66574eb06d933f843fae` |
| version `C1 done - Phase C proved` | `be669c9b52ba1f351a4c0e79` |
| `robot sizes` | `988b1956623d991267021267` |
| `ball and socket` | `a4c789e918b85c50bd4e5ca8` |
| `hinge` | `ec6bde5ed2da077ce95ef48c` |
| `u limb` | `b7031730f11d5b9421f79441` |
| `l limb` | `659ecfa1f8cd7ad13d2af8e6` |
| `ball with cylinder` | `094af2e2bfbda8ded6a31fe2` |
| `socket with cylinder` | `0f9418dfe277dad03c5643ff` |

## Resolved

`check.py` runs 108 rows across the six Part Studios and all 108 agree.

- **The settled hinge is built, and the flats came with it.** Twenty-four teeth on each leaf and
  twenty-four valleys through each ear, each tooth a cone of half angle 45.000° whose flat top
  measures 0.5027 mm², each valley standing 8.8387 off the pin. The rod measures 21.6774 across the
  chord with a 10.3 face on each side, on the hinge and on both limbs, so a limb is a Ø24 cylinder
  with two flats rather than a round one.
- **The slot has no step in it.** One wall at y +5.15 and one at y -5.15, each running from the
  fork's tip at -12 to its root at 21 as a single face. The land the review argued about is gone,
  and what replaced it is one relieved wall a side.
- **The joint closes on the numbers it was designed to.** Ear to tongue is 0.1500 a side and the
  axle is engaged 1.1500 in the bore.
- **The socket is the settled socket.** A finger's top face measures 19.1906 mm², which is Ø11.32 at
  the mouth, and the four slits break into the cavity at 6.0271 from the axis rather than stopping
  in the wall.
- **Both limbs measure 48 between joint centers**, from the socket's ball center to the hinge pin on
  `u limb`, and from the pin to the ball's center on `l limb`.
- **Each coupon is half the joint on a limb-thick handle.** Ø24, 22 from joint center to the
  handle's far face, and neither tab draws a joint: both derive it from `ball and socket`.
- **Every part carries a name and every feature carries a name.** No `Sketch 1`, no `Part 1`, and no
  row rendering as `?`.
- **Every robot connector sits on its own end face, on the axis, pointing out.** The stud's at
  +10 and the socket's at -10 on `ball and socket`; the fork's at +38 and the blade's at -38 on
  `hinge`; and the derived copies land where they belong on the limbs and on both coupons.
- **One driving dimension moves the whole robot.** `#torsoH` driven 96 to 120 and `#limbD` driven to
  a literal 30 rebuilt all six studios with the same part names and the same face count per part,
  and both returned to their original bounding boxes exactly.
- **Nothing reaches outside the document.** `externalreferences` reports no external reference and
  no revision reference on any of the seven tabs.

## What is open

- **The two limbs start their rods by two different rules.** `u limb` draws `limb section` on the
  collar's end face and extrudes from it; `l limb` draws the same sketch on the Top plane and
  offsets the start by `#tab_free`, with the blade's root face sitting there unpicked. Both measure
  the same 48 and pass every row. [`construction.md`](construction.md) has the audit that found it,
  and re-cutting the sketch changes a construction every Phase C number was read from.
- **`Ball stud` and `Socket body` carry capitals where the other six parts do not.** Both are real
  names rather than defaults, so no gate fails; a draft that writes pages from these tabs picks one
  convention first.
- **Nobody has printed either coupon.** The socket's press force and the hinge's spring rate are
  calculations, and [`../../../../tools/hinge_spring.py`](../../../../tools/hinge_spring.py) still
  waits on the measured calibration factors.
- **No page teaches these six tabs, and no STL was exported.** Both are what
  [`plan.md`](plan.md) § *What this draft does not do* says, not omissions.
- **draft9p3 and draft9p1 keep their findings.** This draft repaired its own copy; it did not go
  back.

## Requirements

`req.carry.register` asks which requirements were met, missed and deferred.

| Requirement | Standing |
| ----------- | -------- |
| `req.model.one_document` | Met. Seven tabs in one document, no reference leaving it. |
| `req.model.derive` | Met. The joint is drawn once in `ball and socket` and derived into the limbs and both coupons; the hinge's two parts derive into the limbs. |
| `req.model.design_intent` | Met. All 17 sketches read fully defined, and 39 of 42 dimensions read a `robot sizes` row; the three that do not are a cut profile's clearances. |
| `req.model.named_features` | Met for the model. No frame in this draft teaches a rename, because this draft takes no teaching frames. |
| `req.model.same_structure` | Met, with one finding. [`construction.md`](construction.md). |
| `req.model.anchored` | Met but for the lower limb's rod, which offsets from a plane where a face was available. |
| `req.model.visible_geometry` | Met everywhere except that same offset. |
| `req.model.posed` | Not in play. This draft builds no assembly. |
| `req.carry.conventions` | Not in play. This draft writes no page. |

## What the next draft inherits

The version above, and three things that cost this draft time:

- **A mate connector set to `Attachment: To selection` needs its Attach to query filled**, not just
  its Origin entity. The tree reports the failure in a CSS class and nowhere else, and a
  measurement pass cannot see it, because a connector adds no material.
- **A bare click on the 3D canvas selects nothing.** Onshape picks what its own hover found, so the
  pointer moves first.
- **A feature's name is a template in which `#value` names one of its own parameters**, which is why
  a variable feature named `#nose` draws as `?`. [`build-notes.md`](build-notes.md) § *Phase C* has
  all three in full.

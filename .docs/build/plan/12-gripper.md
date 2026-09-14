# 12. The gripper

Starts from two limbs. Ends with a clip that grips a LEGO bar and mates to a wrist.

**The one part in the robot whose size is set by another part.** Everything else is driven by the
torso or by `#limbCenter`. The gripper's body is driven by the socket's collar, and that is worth
saying out loud rather than hiding.

**This part is being rebuilt, not transcribed.** What has to change and why is
[`gripper.md`](../../experiments/build-briefs/gripper.md).

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.gripper.socket.derive` | bring the socket in first | `copy socket` |
| `cad.parts.gripper.profile_sketch` | the clip's profile, width following the collar | `clip profile` |
| `cad.parts.gripper.body` | extrude it | `clip body` |
| `cad.parts.gripper.cut_plane` | the plane that flattens the clip's top | `plane to cut top of clip` |
| `cad.parts.gripper.cut_top` | split at it | `remove top of clip` |
| `cad.parts.gripper.combine` | union | `combine parts` |
| `cad.parts.gripper.connector` | the gripper's mate connector | `mate to robot` |

## What has to change from stickbot

**The body's width is typed, and it is wrong twice over.** Stickbot has 9.4, which was the
collar's diameter before `#fit` moved to 0.02. The collar became `#ball + 2 × #wall` = Ø9.0, and a
typed 9.4 left the gripper wider than the thing it was supposed to support. At the robot's size the
same expression gives **Ø15.6**, and the typed 9.4 is now well under it; the gripper would sit
under a socket twice its width. Two design changes, two failures, one typed number.

**The width has to be built from the collar, not typed and checked.** The sketch takes its width
from the collar's diameter so that a change to `#wall` moves the gripper with it. **The gripper
declares no `#wall` of its own**; it reads the Variable Studio's, which is `#torsoH * 3 / 160`,
1.8 mm at the robot's size. draft9p0 declared `#torsoH / 32` here against the joint's literal 3 mm,
and at `#torsoH` 120 mm the part changed shape rather than size: x followed its own collar while y
followed the derived socket. This is the
robot's only cross-part dimension, and building it as a real dependency is the difference between
a robot that survives a change and one that quietly stops fitting.

**The top of the clip should be flush with the edge of the socket.** Stickbot's is wider than
that, because it was widened by hand until the socket was fully supported. Flush is the intent;
wider was the way of reaching it. Flush means the top of the body is a **flat square of the
collar's own diameter, 18 × 18**, coaxial with the socket and tangent to it on all four sides —
not a slab wide enough to sit under it. A square rather than a disc, because a rectangular profile
extruded to its own width gives one, and the collar sits flush on it either way.

**Cut it flush; do not dimension it flush.** The reference robot puts a construction plane at
offset **zero** on the socket's root, splits the part on it and deletes the crown above. Nothing
is typed, and the face lands exactly at the root whatever the root does. Its own square is a
coincidence — its clip was Ø11 against a Ø9.4 collar, so the split's chord *was* the platform —
and that stopped being true when the robot doubled, which is why the width now comes from the
sketch and the cut only makes it flush.

**Below that top the body necks in fore-and-aft, and it has to.** The collar's radius reaches
7.8 mm forward and the clip's reaches 5 mm. A body that stayed `2 × #collarR` deep fore-and-aft
would close the mouth off, and the mouth opens forward. The neck is a **45° chamfer of leg
`#collarR − #clipR`** = 2.8 mm, landing on the mouth's **upper lip**: below the lip the part is the
clip circle and nothing else, so nothing 15.6 mm wide is ever beside the mouth, and 45° is an
overhang a printer bridges without support.

### Which way everything points

| what | settled | where it comes from |
| ---- | ------- | ------------------- |
| the profile's plane | `Right` (YZ) | the only plane holding both the mouth's direction and the part's length |
| the extrude | `Symmetric`, `2 × #collarR` = 15.6 mm | so the part cannot be built handed, and the top is flush with the collar |
| the bore's axis | along X, left-right | the robot grips a bar that runs left-right |
| the mouth | opens forward, −Y | the robot faces −Y, and forward is what makes one part serve both wrists |
| the mouth's angle, at the bore | `asin(#mouth / #bore)` = ±52.0° | where the two lips come 2.6 apart across the bore |
| the mouth's angle, outside | `asin(#mouth / (2 × #clipR))` = ±15.1° | the same 2.6 apart, on a wider circle. **The mouth is a parallel slot, not a radial V** — cut each circle where it crosses `#mouth / 2` from the axis and neither angle is chosen |

**Three sources described this part and no two agreed.** The plan sheet drew the C in the front
elevation with the mouth opening straight down — a part that grips a bar pointing away from itself,
which is the exact mistake the brief's acceptance list names — the brief wrote the mouth's sign as
+Y against a robot that faces −Y, and the sheet's body was a literal 6 that never followed the
collar. draft9p0 picked an answer for each and changed none of the sources.
[`../../experiments/runs/2026-08-25-draft9p1/a10-gripper.md`](../../experiments/runs/2026-08-25-draft9p1/a10-gripper.md)
has all four, and the fourth was found working the other three.

**The mirror check does not catch a mouth pointing the wrong way.** A clip built on `Front` with
its mouth opening down is symmetric about x = 0, so it mirrors onto itself and passes every other
check on the brief's list. The check that catches it is reading the bore's axis off the model.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.derive` — the joint is brought in from the studio that
owns it, never resketched here.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the gripper | `req.page.hero` |
| one more hero, holding a LEGO bar | the only frame that says what it is for | |
| the width dimension, showing where it comes from | the whole lesson of this part | |
| the cut plane, before and after the split | a split is a tool a student has not met yet | |
| the top of the clip and the edge of the socket, close-up | flush is only visible close up | |
| the transform's connectors, close-up with a ring | | `req.shot.two_frame` |
| the tree, the version dialog | | |

**The flush shot is an acceptance check as much as a figure.** If the two edges do not line up in
that frame, the part is wrong, and the frame says so before anything is printed.

## What we do not know yet

**How the width is expressed.** Options are a variable in the gripper's own tree computed from
the collar, a projected edge from the derived socket, or a dimension driven off the derived body.
The projected edge is the most honest — it cannot go stale — and it is also the one that might
not be available before the derive happens. This is a decision at the CAD.

**Whether the derive has to move earlier.** If the sketch takes its width from the derived
socket's edge, the derive comes first, and this part joins `foot` as an exception to the
build-the-host-first rule — for a reason, this time.

**Whether the bar hole is Ø3.2 or Ø3.3.** Stickbot has 3.3 and the plan says 3.2. **Neither
number moved at draft9p0**, and that is the point of the part: the bar is LEGO's and the robot
doubling around it changes nothing here. This is a
question for the print, not for the CAD, and it is part of
[task #29](../../robot-build-plan.md).

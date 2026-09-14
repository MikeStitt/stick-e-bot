# draft9p1p2 — build the settled hinge, so it can be printed and pressed

**This draft builds one document holding a hinge, a ball and socket, an upper limb and a lower
limb, and nothing else.** What it hands on is a pair of limbs a person can print, press together
by hand, and turn — which is the only way left to find out whether the numbers on
[`../../../reviews/hinge/`](../../../reviews/hinge/) are right.

## Why this draft exists

The hinge was swept end to end between 2026-08-27 and 2026-08-30, and every finding now ends in a
decision. The joint that came out of that is not the joint any document holds:

- the slot is relieved to 11.2 and the 0.20 fit is given back by a raised land on each ear
- the tongue has a 4.0 slit up it, so the leaf is a spring and the ear is not on its own
- the axle stands 1.0 proud, not 1.6, and 0.80 of it is engaged rather than 1.0
- a tooth is a truncated 45° cone into a straight hole, not a dome into a flat-bottomed pocket
- and each limb's rod stops at its own member's root instead of running on to the pin

The last one is the largest by force. Every printed elbow so far has had both members rooted 12 mm
from the pin, because the rod filled the slot back in; the settled roots are 20 and 21, and the
difference between those two joints is 25.72 kgf against 5.18.

**None of it has been built and none of it has been printed.** The solver in
`tools/hinge_spring.py` says 5.18 kgf to press and 414 N·mm to hold. Whether a printed PETG joint
agrees is the open question, and this draft exists to put a part in a hand.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p1p2` |
| `parent` | `stickbot-draft9p1p1` for the ball and socket, the limb pattern and the variable names |
| `from` | `empty` |
| `takes` | five tabs only: `robot sizes`, `ball and socket`, `hinge`, `u limb`, `l limb` |
| `gates` | the geometry gates only. **No pages, no frames, no tutorials, no capture.** |
| `requirements` | `req.model` and `req.log`. `req.page`, `req.shot`, `req.guide` and `req.audit` do not apply |

**This is a geometry draft, not an instructions draft.** It writes no `.rst`, takes no screenshots
and teaches nobody. The guide learns this joint in a later draft, from a document that is already
known to be right.

## Mike's permission for this run, and its limits

The standing rule is *"GUI only for geometry. REST is read-only, for verification."* On 2026-08-30
Mike lifted it for this run, in these words:

> You can CAD it by whatever methods you want that go as fast as possible for you (copying existing
> CAD, using the programmatic OnShape API).

So this draft may call `POST /api/partstudios/.../features`, `POST /api/documents`, and anything
else that writes. Three things do not change:

- **The permission is for this run and this document.** It does not carry to draft9p3, to any
  guide, or to any later draft. Where a tutorial has to teach a click path, the click path is still
  found in the GUI.
- **Every other Onshape rule stands.** Port 9223 only. `stickbot-draft9p1p1` stays read only.
  Nothing closes a page it did not open.
- **Reading back is still how anything is proven.** A feature that Onshape accepts is not a feature
  that built what was asked for; `featureStatus` says OK for features that produced nothing.

## What gets built

Five tabs, in this order, each one only what the next one needs.

- **`robot sizes`** — the Variable Studio. The eleven rows `stickbot-draft9p1p1` carries, unchanged:
  `#torsoH`, `#torsoW`, `#torsoD`, `#limbCenter`, `#ball`, `#limbD`, `#wall`, `#stand`, `#collar`,
  `#fit`, `#grip`. Nothing about the hinge lives here, because nothing outside the hinge uses it.

- **`ball and socket`** — 9p1p1's tab, reproduced. This joint is settled and is not under review;
  it is here because the limbs need a ball stud and a socket to be limbs.

- **`hinge`** — the settled joint, built from
  [`../../build-briefs/hinge.md`](../../build-briefs/hinge.md). Its own variables live in the tab,
  as 9p1p1's do, and the names change with the design: `#seat` and `#relief` are new, `#teeth_ri`,
  `#teeth_r`, `#bump_d` and `#valley_deep` are gone, `#slit_h`, `#land`, `#land_cham`,
  `#tooth_flat`, `#cone_d`, `#tab_free` and `#ear_free` arrive. Two parts come out, named **`fork`**
  and **`blade`**, and both robot connectors sit on their own end face pointing out.

- **`u limb`** — a Ø24 rod **18 mm long**, a socket at the top and the fork at the bottom. The rod
  stops at `#ear_free` from the pin. This is the thigh's arrangement; the upper arm's shoulder
  socket is in a side face and is a different rod, and it is not built here.

- **`l limb`** — a Ø24 rod **18 mm long**, the blade at the top and a ball stud at the bottom. The
  rod stops at `#tab_free` from the pin.

Both limbs are printed and pressed together as an elbow. Neither is a whole arm; they are the two
halves of one joint with enough limb on each to hold.

## Phase E — the build

- **E0.** Create `stickbot-draft9p1p2`, add the five tabs, record every element id in
  `build-notes.md` before anything is built. A document whose ids are not written down is a
  document that cannot be checked.
- **E1.** `robot sizes`, eleven rows.
- **E2.** `ball and socket`, reproduced from
  [`../2026-08-29-draft9p3/reference/ball-and-socket.features.json`](../2026-08-29-draft9p3/reference/ball-and-socket.features.json).
- **E3.** `hinge`. The long one. Build it in the brief's two stages and read back between them: the
  mechanical joint first, with no teeth, then the valleys and the cones.
- **E4.** `u limb`.
- **E5.** `l limb`.

Read the tab back after every tab, not at the end. A wrong number found at E3 costs one tab; the
same number found at F costs four.

## Phase F — prove it, then export

Against `instructions/robot-guide/make_plans.py` by import, never by transcription.

| What | Expected |
| ---- | -------- |
| parts in `hinge` | 2, named `fork` and `blade` |
| ear to tongue, at the land | 0.20 a side |
| ear to tongue, elsewhere | 0.60 a side |
| the land | 20.8 along the slot, the whole face across, 0.40 proud |
| axle engaged in the bore | 0.80 |
| valleys | 24, Ø1.2, through the ear, on r 9.109 |
| teeth | 24, 45° cones, base Ø1.6, flat top Ø0.4, standing 0.60 |
| tongue root, ear root | 20 and 21 from the pin |
| each limb's rod, by bounding box | 18 |
| both robot connectors | on their own end face, on the axis, pointing out |

Then export `u limb` and `l limb` as STL, one file each, and say in `build-notes.md` what units and
what resolution. **The export is the deliverable.** Everything above it is how we know the export is
worth printing.

## What this draft does not do

- It does not build the torso, the head, the foot, the gripper or the assembly.
- It does not touch `instructions/`. No page in this repository yet teaches this hinge, and none
  should until a printed one has been pressed.
- It does not fix draft9p3. draft9p3's hinge tab holds the old joint and its blade connector is on
  the tongue's root step; both are recorded and neither is repaired here.

## What we do not know yet

- **Whether 5.18 kgf is what a hand feels.** The solver treats PETG as linear at 2000 MPa and the
  contact as frictionless. Both are optimistic. If the printed joint is stiffer, the number to move
  is the slit, and the sweep for it is already in
  [`../../../reviews/hinge/source/tables/slit.rst`](../../../reviews/hinge/source/tables/slit.rst).
- **Whether the land prints.** A 0.40 step ramped 0.4 in 1.2 on a face that is already a cylinder's
  slice is the most delicate thing in the part, and it is unproven.
- **How fast the rim rounds.** The hold is 414 N·mm new and 268 at 0.10 of round. Nobody has cycled
  one of these.
- **Whether the tongue survives a child picking the robot up by its forearm.** 3377 N·mm about
  the tongue's weak axis is the smallest number in the joint, and that is the load it names.

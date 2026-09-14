# The taught path — 22 steps

The GUI build order. Every name in **bold** was read off the live Onshape UI during this session,
not recalled — toolbar tooltips (with shortcuts) and the actual dialog field labels.

**Caveat that matters:** the *dimensions* below are verified in the sense that they build this shape
cleanly via the API. The *click-path* has never been walked by a human in the GUI. Per the Quality
Gates this is a draft session plan, not a verified one.

**Second caveat:** these steps produce the shape but not the practice. They should be rewritten to
carry constraints and variables — see [`modeling-practice.md`](../../.parts/modeling-practice.md).

## Setup

Z is up. The figure faces **-Y** and stands on the **Top** plane, so z = 0 is the ground. All
sketches are on the **Front** plane unless stated. Units: inches.

## Session 1 — body, legs, arms

| #   | Feature        | What the student does                                                     |
| --- | -------------- | ------------------------------------------------------------------------- |
| 1   | **Sketch 1**   | **Corner rectangle** (`g`). **Dimension** (`d`): 8 wide × 10 tall, bottom edge 3 above the origin |
| 2   | **Extrude 1**  | **Solid**, **New**, tick **Symmetric**, **Depth** 3                       |
| 3   | **Sketch 2**   | Two leg rectangles, 0.9 wide, z = 1 → 3, centered at x = ±1.7              |
| 4   | **Extrude 2**  | **Solid**, **Add**, **Symmetric**, **Depth** 1.5                          |
| 5   | **Sketch 3**   | Two arm rectangles, z = 9 → 9.9, x = 4 → 7.5 and −7.5 → −4                |
| 6   | **Extrude 3**  | **Solid**, **Add**, **Symmetric**, **Depth** 0.9                          |

Steps 1–2 are the session floor: every student gets a sponge block. Legs and arms are the same two
moves again, which is the point — a tool used once is a tool forgotten.

## Session 2 — hands and shoes

| #     | Feature                 | What the student does                                                  |
| ----- | ----------------------- | ---------------------------------------------------------------------- |
| 7     | **Sketch 4**            | **3 point arc** (`a`), half-circle radius 1.1 centered at (8.2, 9.45), plus a **Line** (`l`) joining the arc ends |
| 8     | **Revolve 1**           | **Solid**, **Add**, **Revolve axis** = that line, tick **Full revolve** |
| 9–10  | **Sketch 5**/**Revolve 2** | Same again at x = −8.2                                              |
| 11    | **Sketch 6**            | Two shoe rectangles 2.0 wide × 1.2 tall sitting on z = 0, centered at x = ±1.7 |
| 12    | **Extrude 4**           | **Solid**, **New** (so shoes can be black), **Symmetric**, **Depth** 3 |
| 13    | **Fillet 1**            | **Entities to fillet** = the 8 top edges of both shoes, **Radius** 0.5 |

**The flat edge of the half-disc must be an ordinary Line, not construction geometry.** Construction
geometry does not bound a sketch region, so a construction diameter leaves the profile open and the
revolve has nothing to sweep. The same line is then selected as the **Revolve axis** — a profile
edge is allowed to be the axis.

## Session 3 — the face

| #   | Feature       | What the student does                                                       |
| --- | ------------- | ---------------------------------------------------------------------------- |
| 14  | **Sketch 7**  | Click the **front face of the body** as the sketch plane. Two **Center point circle** (`c`), radius 1.7, at (±1.9, 10.2) |
| 15  | **Extrude 5** | **Solid**, **New**, **Depth** 1.2, outward                                  |
| 16  | **Fillet 2**  | The outer circular edge of each eye, **Radius** 0.9 → domed bug eyes        |
| 17  | **Sketch 8**  | On the same body front face: two **Center point circle**, radius 0.62, at (±1.9, 10.2) |
| 18  | **Extrude 6** | **Solid**, **New**, **Depth** 1.35 → pupils poke through the eyes           |

Sketching on a *face* rather than a plane is the new idea, and it is the one that trips people up.

Pupils are sketched on the **body** front face, not on the eye front. Sketching on the filleted eye
front is fussier than it is worth, and from the body face a depth of 1.35 puts them proudly through.

## Session 4 — mouth, teeth, color

| #   | Feature        | What the student does                                                      |
| --- | -------------- | --------------------------------------------------------------------------- |
| 19  | **Sketch 9**   | On the body front face: five **Corner rectangle**s, 1.2 × 0.7, at x = −2.4, −1.2, 0, 1.2, 2.4 and z = 7.3, 6.7, 6.4, 6.7, 7.3 |
| 20  | **Extrude 7**  | **Solid**, **Remove**, **Depth** 0.35, **flipped inward**                  |
| 21  | **Sketch 10**  | Two tooth rectangles 0.8 × 0.7, x = 0.05 → 0.85 and −0.85 → −0.05, z = 6.05 → 6.75 |
| 22  | **Extrude 8**  | **Solid**, **New**, **Depth** 0.35, outward                                |
| —   | Appearance     | Color the parts from the **Parts** list                                    |

**Step 20 is the trap.** An extrude started from a face defaults to pointing *outward*, away from
the material. Left alone, the smile removes nothing — and Onshape reports this as `INFO`, not an
error, so the feature looks fine in the tree while the model is visibly wrong.

The flip is the **small arrow button to the right of the end-condition dropdown**, verified against
the live dialog. It is *not* the **Direction** checkbox lower down the panel, which does something
else — an earlier draft of these steps said Direction, and would have sent a room full of students
to the wrong control. Write the symptom down: "if you can't see the grin, your extrude went the
wrong way."

## Known gaps in these steps

- No constraints or variables anywhere (the big one).
- The **Mirror** dialog was never verified, which is why this build does everything twice by hand
  rather than mirroring. Mirror is currently the stretch task.
- The exact wording of the appearance menu in the **Parts** list was not verified.
- Fillet radii (13 and 16) are the most likely first failures if a dimension changes — a radius
  larger than the face allows is rejected outright.

# elephant cup — a 12 fl oz cup with 1 fl oz of headroom, built over REST

A scratch experiment on branch `elephant`, outside the stickbot course. The design was agreed with
Mike in conversation on 2026-09-30 before anything was built.

## Where the work is

| What | Value |
| ---- | ----- |
| Document | `elephant cup`, owned by Mike Stitt |
| Document id | `9a8f8614c04120c0a8f85448` |
| Part Studio `cup` | element `993e7039919edc785df99d49` |
| Named version | `cup, 12 fl oz with 1 fl oz headroom`, `1f0631a4e8285baf2d33f860` |
| Version link | https://cad.onshape.com/documents/9a8f8614c04120c0a8f85448/v/1f0631a4e8285baf2d33f860 |
| Live workspace | https://cad.onshape.com/documents/9a8f8614c04120c0a8f85448/w/2ba8fa28d04af5579c057984/e/993e7039919edc785df99d49 |

The links were assembled from ids the API returned; neither was opened in a browser as another
account would see it. The workspace was opened in the agent browser, signed in as the owner.

The new document came with `Assembly 1`, which the cup does not use. It was left in place.

## The agreed design

| Variable | Expression | Resolves to |
| -------- | ---------- | ----------- |
| `#fill` | `12 * 29.5735295625 cm^3` | 354.882 cm³, 12 US fl oz |
| `#overfill` | `1 * 29.5735295625 cm^3` | 29.574 cm³, 1 US fl oz |
| `#innerD` | `70 mm` | |
| `#wall` | `1.5 mm` | |
| `#floor` | `3 mm` | |
| `#lipR` | `1.5 mm` | |
| `#ridgeR` | `1 mm` | |
| `#fillH` | `#fill / (PI * (#innerD / 2) ^ 2)` | 92.2143 mm |
| `#brimH` | `(#fill + #overfill) / (PI * (#innerD / 2) ^ 2)` | 99.8989 mm |

Straight sides, no handle. A round lip of radius `#lipR`, flush with the inside wall, tops out at
`#brimH` above the inside floor. A half-round ridge of radius `#ridgeR` on the inside wall is
centered at `#fillH`, and marks the fill line.

An `ANY` variable takes a volume in `cm^3`. Onshape has no fluid-ounce unit, so the ounce is written
as its value in cm³.

## What was built

Eleven features: the nine variables, each immediately above the sketch that first reads it; the
sketch `cup profile` on Front; and `revolve cup` about the sketch's own axis line. One part, `Cup`.
The workspace length unit is millimeters, set through the GUI with draft9p5's `a0_units.py`.

`cup profile` is eight entities: six lines and two arcs, a closed half section. 18 point
coincidences, 2 point-on-line coincidences, 6 horizontal and vertical constraints and 1 tangency
fix the shape; 7 dimensions, each reading a variable, fix its size. The lip's height is dimensioned
to its center as `#brimH - #lipR`, because an arc's top is not a sketch point.

## What was checked

- **Ring 1, after every write.** Each feature read back from `/features`: every parameter sent
  matched what was stored, every `featureStates` entry was `OK`, and `rollbackIndex` equaled the
  feature count, eleven times.
- **The sketch solved where the design put it.** Read from `sketches?includeGeometry=true`: outer
  wall at x 36.5 mm, inner wall at x 35.0 mm, floor at y 3.0 mm, ridge center at y 95.2143 mm, lip
  center at (36.5 mm, 101.3989 mm).
- **The sketch is fully defined.** Opened for edit in the agent browser and taken square on: every
  entity is black, and the blue-pixel mask from `onshape_screen.is_sketch_blue` counts 0 px on the
  canvas. The shot stayed in the session scratchpad.
- **The faces.** Seven, from `bodydetails`: the base plane, the outside cylinder at r 36.5 mm, the
  lip torus of minor radius 1.5 mm centered at z 101.3989 mm, the inside cylinder at r 35.0 mm
  above and below the ridge, the ridge torus of minor radius 1.0 mm at z 95.2143 mm, and the inside
  floor at z 3.0 mm.
- **Capacity, from the measured faces.** 11.9942 fl oz to the ridge's center and 12.9921 fl oz to
  the lip's top. The misses are the ridge's 0.17 cm³ below the fill line, and the ridge's
  0.34 cm³ less the lip's 0.11 cm³ at the brim; both were named in the agreed design and left alone.
- **Part volume.** 47274.39 mm³ measured by `massproperties`, against 47274.5 mm³ integrated from
  the profile.
- **The drive test.** `#innerD` set to 80 mm: the model rebuilt with every state `OK`, the inside
  radius read 40.0 mm, the ridge center dropped to z 73.6016 mm and the lip top to z 79.4851 mm,
  and the cylinder to the ridge's center still held 12.0000 fl oz. Set back to 70 mm and read
  back as before.
- **Looked at.** Isometric, front and bottom from `shadedviews`: the lip bead stands proud of the
  outside wall, the ridge shows as a ring inside, and the bottom is flat. No section was rendered;
  the sketch shot square on stands in for one.

A pale blue horizontal line crosses the sketch shot at the ridge's height and runs to the canvas
edge. It is too pale for the mask and is not an entity; what draws it was not established.

## Scripts

`create.py` makes the document once and writes `ids.json`. `build.py` writes the eleven features
with the Ring 1 read after each. `verify.py`, `drive.py` and `look.py` are the checks above.
`units.py` and `version.py` set the unit and publish the version.

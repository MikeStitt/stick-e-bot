# C3 — the model opened and turned, and `Recovery point` published

*Model inspected* is a gate this draft claims, and reading a report about a model is not looking at
it. The assembly was opened in the browser, every instance made visible, fitted, and turned through
five orientations. The frames are in [`frames/`](frames).

| frame | what it shows |
| --- | --- |
| [`c-01-front.png`](frames/c-01-front.png) | the first look: fourteen instances, thirteen mates, standing |
| [`c-01-iso.png`](frames/c-01-iso.png) | the three-quarter view with nothing selected |
| [`c-02-front.png`](frames/c-02-front.png) | square on the front, off the view cube |
| [`c-03-right.png`](frames/c-03-right.png), [`c-04-back.png`](frames/c-04-back.png), [`c-05-left.png`](frames/c-05-left.png) | the same robot turned toward its left, a step at a time |
| [`c-06-top.png`](frames/c-06-top.png) | from above and to the side, where the soles show |

## What looking settled that measuring did not

- **The robot stands.** Head on the neck, both arms hanging, both feet flat on the floor plane.
  Nothing is floating, nothing is inside anything else, and no instance is at an angle. That is the
  rest pose B9 built, seen rather than read off fourteen transforms.
- **The eyes are ellipses and they stand off the face.** A3 and A8 are visible from the front and
  from the side: two ellipses wider than they are tall, above a rounded slot for the mouth, both
  clear of the head's upper rounds. There are no pupils, which is the decision A8 made.
- **The tread is on the sole and it stops short of both ends.** `c-06-top.png` looks down the leg
  onto the foot and the grooves read as a row of ribs with solid material at heel and toe. That is
  A5 in the picture, not just in the 16 groove walls the face dump counts.
- **The feet meet on the center plane.** The two soles touch along x = 0 with no gap between them.
  The measurement says ±24 and the picture says why that matters: the sheets draw a 16 mm gap, and
  there is none. The foot needs its 8 mm offset and its handedness before this looks right.
- **Every joint carries its mate connector at its station.** The triads are on in every frame, and
  they line up in two vertical columns down the arms and the legs, evenly spaced. A limb that
  reached the wrong distance would show as an uneven column.

## What the tab did that is worth writing down

- **The window was 1280 × 720, not the 1600 × 1000 the pixel masks are measured against.** None of
  `onshape_screen`'s masks were used here; the frames are plain screenshots. Any coordinate in this
  section is measured at 1280 × 720 and does not carry across.
- **`h` toggles *Show mates mode*, and it is a mode, not a visibility.** Turning it on highlights
  whatever the cursor is over and puts a connection message in the status bar. It is not what puts
  the triads on screen, and turning it off does not take them off.
- **`Hide mates` on all fourteen instances left the triads where they were.** The mate rows in the
  tree already read *(Hidden)*, so what is drawn is the mate connectors rather than the mates, and
  nothing in the instance context menu turns those off. The frames carry them.
- **The view cube's side arrows turn the model by a small step, not by 90°.** Four clicks walked the
  camera from *Front* to *Left* rather than all the way round. Clicking a named face of the cube is
  what lands on that face exactly.
- **The canvas ends where the window ends.** A click at y = 850 in a 720-high window does nothing,
  which is why the first attempt to clear the selection left everything orange.

## The version

| | |
| --- | --- |
| name | **`Recovery point`** |
| id | `8504f457723606c65c2ab48f` |
| cut | 2026-08-26T18:25:43Z |
| document | `stickbot-draft9p1` `a1a859f4bfdfe42d372aff90`, workspace Main `d3a590c94880f445e3c56902` |

Its description says what it is: the model read back against `make_plans.py` and agreeing,
`#limbCenter` driven 48 → 60 → 48 and `#fit` driven 0.08 → 1 → 0 → 0.08, both round trips exact.

**This is what draft9p2 starts from.** The document now carries four versions, and the other three
are steps on the way to it:

| version | id | what it holds |
| --- | --- | --- |
| `Start` | `8e4b28cc2cf504aef52a7a9a` | the copy of `stickbot-draft9p0` at `t14 legs`, before B1 |
| `parts built` | `6eae7c37deee3f58facbbf83` | every Part Studio at the end of B1 to B8 |
| `ankle centered` | `e6fd823965e71c15d9e267cb` | the foot's `mate to robot` connector moved onto the origin |
| `Recovery point` | `8504f457723606c65c2ab48f` | the measured, driven and inspected model |

The assembly's fourteen instances point at `parts built` and `ankle centered` rather than at Main.
That is deliberate and it is [C2](c2-driving.md)'s note about a version-linked assembly being deaf
to the variable table.

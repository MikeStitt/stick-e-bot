# The print files, and how to lay them on the bed

Four binary STLs, in millimeters, exported from `stickbot-draft9p1p2` at a chord tolerance
of 0.02 mm. Both limbs are watertight with zero open edges, and their bounding boxes match
the model; [`../check.py`](../check.py) is what proves the model.

| File | What it is | Bounding box |
| ---- | ---------- | ------------ |
| `u-limb.stl` | the thigh: a knee fork, a 19.5 mm rod, a hip socket | 24 × 62 × 24 |
| `l-limb.stl` | the shin: a knee blade, an 18 mm rod, an ankle ball stud | 24 × 66 × 24 |
| `socket.stl` | the socket alone, on a 12 mm stub | 24 × 21 × 24 |
| `ball-stud.stl` | the stud alone, on a 12 mm stub | 24 × 28 × 24 |

## Lay the limb axis flat, with the slit standing up

The hinge is a spring, and both halves of it bend the same way: the ear and the leaf are
cantilevers rooted 21 and 20 mm from the pin, and what they carry is tension running along
the limb's own axis. Layer adhesion is the weakest direction an FDM part has, so the limb
axis wants to lie in the layer plane rather than along the build direction. Print each limb
lying down.

Which way it lies then decides what happens to the 4 mm slit. Turn the part so the slit's
gap stands vertical — the pin axis across the bed, the chord axis up — and the slit is two
vertical walls with air between them, which needs nothing. Turn it the other way and the
slit becomes a 33 mm ceiling to bridge.

At that orientation the teeth are 45° cones growing sideways out of vertical walls, which is
the angle that supports itself, and the socket's four relief slits come out as two vertical
walls and two 1.6 mm bridges.

## What is not settled

- **The Ø24 rod lying down touches the bed on a line.** A brim holds it; whether the first
  layers need more than that has not been tried.
- **The socket's cavity is a Ø12.16 dome on its side.** It is small enough that the droop
  may not matter, and nobody has measured it.
- **The socket's finger is 1.42 mm at its thinnest**, at the cavity's equator, which is
  three and a half extrusion widths and the thinnest structural section in the robot.
- **Every force in the design assumes PETG**, E 2000 MPa and yield 50 MPa. Print it in
  something stiffer and the press force rises with E.

## What it should feel like

- **Pressing the knee together: about 5.2 kgf**, and the tongue goes in nose first, so the
  force builds toward the end rather than all at once.
- **Pressing the ball into its socket: about 5.2 kgf as well**, and it should snap over
  rather than crush in. The four fingers reach 59% of PETG's yield opening the mouth, so
  they are meant to spring back; if the mouth stays open afterward, the print came out
  narrower than drawn and that is worth measuring before printing another.
- **Turning it once together: 414 N·mm to break away**, which at a hand 150 mm from the pin
  is 0.28 kgf. That is 16 times what the limb needs to hold itself up.
- **It should click twenty-four times in a turn**, once every 15°.
- **Expect the hold to fall as the valley rims round off.** A 0.05 mm radius on the rim takes
  it to 82% of new, 0.10 mm to 65%, and 0.15 mm to 47%. The derivation is in
  [`.docs/reviews/hinge/`](../../../../reviews/hinge/source/index.rst).

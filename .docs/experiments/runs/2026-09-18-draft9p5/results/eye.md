# Phase A — why the eye in stickbot-draft9p4-check is 1.5 % oversize

**The two diameter dimensions carry the numbers the mouse landed on, not the expressions the page
tells the reader to type.** The cause is in neither the page nor the design source, so draft9p5
fixes it by building the ellipse with its diameters driven, and Ring 1 catches it if it ever
happens again.

Read on 2026-09-18 from `stickbot-draft9p4-check`, document `86f40935a709a0748cdbb199`, workspace
`075a86f5b8f922210c0a7317`, tab `head` `254cd749a0c6c642d288b8cc`. Every call was a GET; nothing in
that document was touched. The script is [`../scripts/a_eye_read.py`](../scripts/a_eye_read.py) and
its record is [`eye-read.json`](eye-read.json).

## What `eye profile` holds

One ellipse, `W7QpEuwBuld7`, and five constraints.

| Constraint | What it says | Driven? |
| ---------- | ------------ | ------- |
| `HORIZONTAL` | the ellipse lies on its side | — |
| `MAJOR_DIAMETER` | `15.983648598194122*mm` | no, a literal |
| `MINOR_DIAMETER` | `8.132031187415123*mm` | no, a literal |
| `DISTANCE` horizontal | `#eyeX` | yes |
| `DISTANCE` vertical | `#eyeUp` | yes |

The tab's four eye variables are right: `#eyeX` `#headW / 6`, `#eyeUp` `#headW / 9`, `#eyeRx`
`#headW / 9`, `#eyeRy` `#headW / 18`. So is the center the sketch reports, `(12.0, 8.0)` mm.

## The numbers close the chain

| | Major radius (mm) | Minor radius (mm) | End face (mm²) |
| --- | ---: | ---: | ---: |
| designed, `EYE_RX` and `EYE_RY` from `make_plans.py` | 8 | 4 | 100.531 |
| the sketch in the check document | 7.99182 | 4.06602 | 102.0857 |

Half of `15.983648598194122 mm` is 7.99182 mm and half of `8.132031187415123 mm` is 4.06602 mm, and
pi times those two is 102.0857 mm², which is the face area measured on that head. Sketch, face and
departure are one story, and the ratio is 1.0155.

**Neither candidate cause fits.** The plan offered both radii larger by a factor of 1.0077, which
predicts 8.0616 mm and 4.0308 mm, and both larger by 0.0411 mm, which predicts 8.0411 mm and
4.0411 mm. What the sketch holds is a major radius 0.00818 mm *under* 8 mm and a minor radius
0.06602 mm over 4 mm. An area on its own cannot tell a scale from an offset from a drag, which is
why the read was owed.

## The page is sound, and says so twice

[`head.rst:510`](../../../../instructions/stickbot-draft9p4/source/head.rst) tells the reader to
click **Dimension**, drop the label above the ellipse and type ``#eyeRx * 2``, then drop one out to
the side and type ``#eyeRy * 2``. The next paragraph says to read the number already in the box
before typing over it, *about 16 for the long way, about 8 for the short way*. The literals the
check document holds are 15.98 mm and 8.13 mm, which are those two numbers left as they were found.

**What draft9p5 does about it.** `eye profile` is built with `MAJOR_DIAMETER` `#eyeRx * 2` and
`MINOR_DIAMETER` `#eyeRy * 2`, and Ring 1 reads the sketch's constraints back before the extrude
runs. Ring 2's acceptance on `head` is each eye's end face at `math.pi * EYE_RX * EYE_RY`, imported
from `make_plans.py`.

**The symptom, for whoever writes the head's page next.** A sketch dimensioned to a dragged number
goes black and fully defined, and no feature reports anything. Nothing on the screen separates it
from a correct one, which is why the check is to read the dimension rather than to look at the
sketch.

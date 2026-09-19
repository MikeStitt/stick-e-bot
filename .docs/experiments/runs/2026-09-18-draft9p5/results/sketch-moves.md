# Phase A — which sketches should stand on a face

Written by [`../scripts/a_sketch_moves.py`](../scripts/a_sketch_moves.py).
A sketch on a stock plane is wrong when its extrude offsets its start by an
expression that names a dimension the geometry already fixes; it is right when the
extrude is symmetric about that plane, because then the plane is what places it.

**6 sketches offset their start**, and those are the ones to move.

## `ball and socket`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `stud profile` | Front plane | no extrude names it  |
| `collar profile` | Top plane | neither `collar blank` |

## `hinge`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `blade profile` | Front plane | symmetric about the plane `blade blank` |
| `stub axle outline` | Front plane | symmetric about the plane `stub axle` |
| `blade wedge outline` | Front plane | no extrude names it  |
| `blade rod outline` | Top plane | **offsets its start** `blade arm` by `#tab_free` |
| `relief slit outline` | Right plane | symmetric about the plane `relief slit` |
| `fork outline` | Top plane | no extrude names it  |
| `fork blade top cut outline` | Front plane | no extrude names it  |
| `pocket axle sketch` | Front plane | symmetric about the plane `pocket axle on fork` |
| `ear wedge outline` | Front plane | no extrude names it  |
| `fork arm outline` | Top plane | **offsets its start** `fork arm` by `#ear_free` |

## `body`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `torso outline` | Front plane | no extrude names it  |
| `pivot lines` | Front plane | no extrude names it  |
| `trim shoulder pattern` | Front plane | symmetric about the plane `trim shoulder cut` |

## `head`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `head profile` | Front plane | no extrude names it  |
| `eye profile` | Front plane | neither `eye` |
| `mouth profile` | Front plane | **offsets its start** `mouth` by `#headD / 2` |

## `foot`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `pedestal outline` | no query | **offsets its start** `foot pedestal` by `#collar_down` |
| `foot outline` | no query | **offsets its start** `foot` by `#plate` |
| `groove profile` | no query | **offsets its start** `sole groove` by `#ankle_h - #rib_d` |

## `gripper`

| Sketch | Stands on | What its extrude does |
| ------ | --------- | --------------------- |
| `clip profile` | no query | symmetric about the plane `clip body` |


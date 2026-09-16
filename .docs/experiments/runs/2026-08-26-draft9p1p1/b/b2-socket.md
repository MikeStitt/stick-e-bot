# B2 — the socket's root and the slit's floor

Two extrude distances in `ball and socket`, one from A2 and one from A1. No sketch was edited and no
feature was added, so the tab still holds the fourteen features B0 counted.

## `collar blank`'s second distance is `#collar` itself

The sketch is on the plane through the ball's center, so a second-direction depth measured from it
puts the socket's root at exactly minus that depth. It read `#collar - #grip`, which made the root
`#grip` shallower than the collar's own figure and moved it whenever the fit moved. It now reads
`#collar`.

| | before | after |
| --- | --- | --- |
| second direction depth | `#collar - #grip` | `#collar` |
| the root, z | −9.0535 | **−9.0000** |
| `Socket body`, mouth to root | 11.0000 | **10.9465** |

Both figures are A2's, to the digit.

## `relief slits` ends at `#grip + #ball / 4`

The slit sketch is on the mouth face, so the depth is measured down from z +`#grip`. It read
`#collar - #wall`, which is a wall's thickness up from the root and had no reason to be where the
tabs stop. It now reads `#grip + #ball / 4`, which puts the floor at `#ball / 4` below the ball's
center whatever the fit is.

| | before | after |
| --- | --- | --- |
| depth | `#collar - #wall` | `#grip + #ball / 4` |
| | 8.0000 | **4.9465** |
| the floor, z | −6.0535 | **−3.0000** |
| the ring under the tabs | 2.9465 | **6.0000** |

## The cut is a slot for its whole depth

`Socket body` reads three horizontal planes — z −9.0000, −3.0000 and +1.9465, the root, the slit
floor and the mouth — one cylinder at r 9.0, which is the Ø18 outside, and one sphere at r 6.0800,
which is `#ball / 2 + #fit`.

**No face at r 5.0.** That face is what C1 found in draft9p1: the slit profile's inner edge,
standing where the cut ran past the point at which the cavity had narrowed inside it. There is none
now, so the spherical cavity is what bounds every part of the cut on the inboard side and the slit
is a slot the whole way down. This is A1's claim, and it is measured rather than argued.

## The pattern is still four

`slit profile` holds sixteen curve segments, which is four rectangles, and one `CIRCULAR_PATTERN`
constraint over four instances. Opened to look at, its entities draw black and its three dimensions
read 5, 12 and 0.8. It was cancelled out of unchanged.

## The socket's consumers, so far

| part | before B1 | now | after B3 |
| --- | --- | --- | --- |
| `head` | 83.0000 | **82.9465** | 82.9465 |
| `Foot` | 25.9465 | 25.9465 | 25.9465 |
| `Gripper` | 25.9465 | 25.9465 | 25.9465 |
| `u limb` | 61.9465 | 63.8930 | 62.0000 |

The head is already where A2 says it lands, because it is built on the socket body rather than on a
dimension. `u limb` is long by `#grip` until B3 takes the `#grip` term out of its rod.

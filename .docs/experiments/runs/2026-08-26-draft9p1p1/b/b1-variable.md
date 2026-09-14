# B1 — `#collar` stops being typed

A2 re-based the socket on the ball's center. In the table that is one row: `collar` was the typed
`11 mm` and is now `#ball / 2 + #wall`, which evaluates to **9 mm** and is the collar's own radius.
The other ten rows were not touched.

## What reads it

Six expressions across four tabs, read before the edit:

| tab | feature | parameter | expression |
| --- | --- | --- | --- |
| `ball and socket` | `collar blank` | second direction depth | `#collar - #grip` |
| `ball and socket` | `relief slits` | depth | `#collar - #wall` |
| `foot` | `#collar_down` | value | `#collar - #grip` |
| `foot` | `#pedestal` | value | `#plate - #collar_down` |
| `foot` | `foot pedestal` | start offset | `#collar_down` |
| `u limb` | `limb` | depth | `#limbCenter - #collar + #grip - #limbD / 2` |

`head` and `l limb` name `#collar` nowhere. The head follows the socket because it is built on the
derived socket body rather than on a dimension, and `l limb` carries a ball rather than a socket. So
B3 has two expressions to edit and not four, and the head's move is something to measure rather
than something to make.

`gripper`'s `#collarR` and `#clipR` are its own variables and are read in B4.

## What the model did

Every tab regenerated with no feature out of OK and every Part Studio complete. Two parts moved,
and both moves are the ones B2 and B3 are for:

| part | before | after B1 | after B2 and B3 |
| --- | --- | --- | --- |
| `Socket body`, mouth to root | 11.0000 | 9.0000 | 10.9465 |
| `head`, overall | 83.0000 | 81.0000 | 82.9465 |

`Socket body` is short here because `collar blank` still extrudes `#collar - #grip` below the ball's
center; B2 is what makes that second distance `#collar` itself. `torso`, `Foot`, `blade`, `fork`,
`u limb`, `l limb` and `Gripper` all measure exactly what they measured before.

# B3 — the socket's consumers lose their `#grip` term

A2 fixed the socket's root, so the two expressions that added `#grip` back to reach it are now
adding it to a number that already includes it. Both are edited here. `head` and `l limb` name
neither `#collar` nor `#grip` anywhere, so B3 touches two tabs rather than four.

| tab | what it is | before | after |
| --- | --- | --- | --- |
| `u limb` | `limb`, its extrude depth | `#limbCenter - #collar + #grip - #limbD / 2` | `#limbCenter - #collar - #limbD / 2` |
| `foot` | `#collar_down` | `#collar - #grip` | `#collar` |

`#pedestal` is `#plate - #collar_down` and was not edited. It follows, and its value is what A2
said it would be.

| variable | before | after |
| --- | --- | --- |
| `#collar_down` | 7.0535 under B1, 9.0535 before it | **9.0000** |
| `#pedestal` | 4.9465 under B1, 2.9465 before it | **3.0000** |
| `u limb`'s rod | 28.9465 under B1, 26.9465 before it | **27.0000** |

## Nothing changed size except the head

Read part by part, against the same read taken before B1:

| part | before B1 | after B3 |
| --- | --- | --- |
| `torso` | 128.0000 | 128.0000 |
| `head` | 83.0000 | **82.9465** |
| `Ball stud` | 16.0000 | 16.0000 |
| `Socket body` | 11.0000 | **10.9465** |
| `Foot` | 25.9465 | 25.9465 |
| `blade` | 38.4000 | 38.4000 |
| `fork` | 39.4000 | 39.4000 |
| `u limb` | 61.9465 | 61.9465 |
| `l limb` | 66.0000 | 66.0000 |
| `Gripper` | 25.9465 | 25.9465 |

**`u limb` is the interesting row.** Its rod grew 0.0535 and the part did not, because the rod
starts at the socket's root and the root rose by the same 0.0535. The rod's far end is where it
always was, so the fork below it and the mouth above it are both untouched. The plan said this row
would grow; it does not, and the plan now says so.

## The standing height is 317.0000

The assembly follows the workspace, so it re-posed itself as each edit landed. Read after B3:

| | before B1 | after B3 |
| --- | --- | --- |
| standing height | 317.0535 | **317.0000** |
| the head's top | +139.0535 | **+139.0000** |
| the head's underside, the socket's root | +67.0535 | **+67.0000** |
| the socket's mouth under the head | +56.0535 | +56.0535 |
| the shoulders | ±49.5509, +19.2355 | unchanged |
| the elbows | ±49.5509, −28.7645 | unchanged |
| the wrists | ±49.5509, −76.7645 | unchanged |
| the hips | ±24, −58 | unchanged |
| the knees | ±24, −106 | unchanged |
| the ankles | ±24, −154 | unchanged |

Fourteen instances, none pinned to a version, thirteen mates. **Every joint station holds and only
the head moves**, which is what A2 said the whole re-basing was for. Phase C drives `#fit` and asks
whether it still holds when the fit is not 0.08.

## Read with the features endpoint spent

Onshape answered `retry-after: 67201` with `x-rate-limit-remaining: 0` on
`partstudios/.../features` partway through this row, so the expressions above were confirmed from
the feature tree in the GUI and from the dialogs, and the geometry from `parts`, `boundingboxes`
and `bodydetails`, which had hundreds to thousands of calls left each. The limit is per endpoint
family. [`../../../README.md`](../../../README.md) carries the todo this produced.

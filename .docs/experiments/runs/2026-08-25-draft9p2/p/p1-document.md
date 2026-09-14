# P1 — the empty document, and the numbers it will be built to

## Where the work is

**`stickbot-draft9p2`**, owned by Mike Stitt. Created empty on 2026-08-28.

| Thing | Id |
| ----- | -- |
| Document | `ff43b9ee37b87e04445bb573` |
| Workspace `Main` | `2625a774fd32dc519c24dce4` |
| `Part Studio 1` | `58e1fb096c6bb30ae8b5b407` |
| `Assembly 1` | `07f503bad249441d4bb50461` |
| `BOM : Assembly 1` | `97a1d12efa2ee4d28114f146` |

[The live workspace](https://cad.onshape.com/documents/ff43b9ee37b87e04445bb573/w/2625a774fd32dc519c24dce4/e/58e1fb096c6bb30ae8b5b407),
opened in the agent browser and confirmed by its title, `stickbot-draft9p2 | Part Studio 1`. **No
version is published yet** — the first one is tutorial 1's, and the *Recovery point* gate is claimed
per tutorial rather than here.

**A new document arrives with a Part Studio, an Assembly and that assembly's bill of materials.**
[`03-assembly-first-parts.md`](../../../build/plan/03-assembly-first-parts.md) renames and moves the
assembly, so no step creates one. The Variable Studio and the other twelve Part Studios do not
exist; their element ids are written down as each tutorial makes its tab.

## The numbers, read off `stickbot-draft9p1p1`

`robot sizes` in the reference model, over `/api/variables`, at the rest values. This is what Phase
T types, and it is the table `audit.part` measures against.

| Row | Expression | mm |
| --- | ---------- | -- |
| `#torsoH` | `96 mm` | 96 |
| `#torsoW` | `72 mm` | 72 |
| `#torsoD` | `48 mm` | 48 |
| `#limbCenter` | `48 mm` | 48 |
| `#wall` | `#torsoH / 32` | 3 |
| `#ball` | `#torsoH / 8` | 12 |
| `#collar` | `#ball / 2 + #wall` | 9 |
| `#fit` | `0.08 mm` | 0.08 |
| `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)` | 1.9465 |
| `#limbD` | `#torsoH / 4` | 24 |
| `#stand` | `#ball * 5 / 6` | 10 |

**Four of these are typed and the rest are derived**, which is what makes `#torsoH` the robot's one
driving dimension. `#fit` is typed because it is a property of the printer rather than of the robot,
and [`../2026-08-25-draft9p1/a2-fit.md`](../2026-08-25-draft9p1/a2-fit.md) settles its value.

## What Phase P found in the plan, and settled

**The plan put the joint's numbers in the wrong place.**
[`04-ball-and-socket.md`](../../../build/plan/04-ball-and-socket.md) called for ten variable
features declared inside the `ball and socket` tab, and
[`06-torso-joints.md`](../../../build/plan/06-torso-joints.md) listed `#limbD`, `#ball` and
`#stand` among eleven that `body` declares for itself. The reference model carries all eleven rows
in `robot sizes` and no tab declares any of them, because draft9p1's B1 promoted them after finding
five locals in `ball and socket` holding numbers the studio no longer carried.

Both files now add rows to the studio instead, on the page where each number first means something:
tutorial 1 types five, tutorial 4 adds `#ball`, `#collar`, `#fit` and `#grip`, tutorial 6 adds
`#limbD` and `#stand`. The end state is the eleven rows above, in one table, which is what the
reference holds.

**9p0's pages carry none of four conventions `robot-guide4` established.** Counted over the
eighteen inherited pages: no `image::` step shots, no `.. step:` tags, no toolbar close-ups, no clip
links. `robot-guide4`'s three pages carry thirty-five, sixty-seven and ninety-two step shots.
[`../../../experiments/runs/2026-08-25-draft9p2/plan.md`](plan.md) § *Phase W* names each against
the requirement that asks for it.

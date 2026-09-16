# Launch gate — run 3, wave 3: torso and head

Performed against [`../../../2026-08-12-launch-gate.md`](../../../2026-08-12-launch-gate.md).

**This gate is weaker than the others and the reason is structural: I wrote the briefs it
gates.** A gate catches what its author could not see, and the same reader cannot supply that
twice. What follows is the mechanical part — links opened, variables traced, arithmetic redone —
which is worth running regardless. The judgment part is missing and the briefs say so at the top
of each file.

## Links

Every relative link in [`torso.md`](../../build-briefs/torso.md) and
[`head.md`](../../build-briefs/head.md) resolves.

## Variables traced to the plan's table, not to memory

| Brief | Variable | Row in `robot-build-plan.md` |
| ----- | -------- | ---------------------------- |
| head | `#headD` | `#torsoH * 3/4` = 36 |
| torso | `#torsoH` | `48 mm` = 48 |
| torso | `#torsoW` | `#torsoH * 3/4` = 36 |
| torso | `#torsoD` | `#torsoH / 2` = 24 |
| torso | `#ballD` | `#torsoH / 8` = 6 |
| torso | `#stalkD` | `#ballD / 2` = 3 |
| torso | `#shoulderHalf` | `#torsoH * 3/8` = 18 |
| torso | `#hipHalf` | `#torsoH / 4` = 12 |
| torso | `#armX` | `#shoulderHalf + #limbD/2 + 3` = 27 |

Every cited variable has a row. That is the check `hand.md` failed on `#clipR`.

## Arithmetic redone rather than copied

Working from the plan's station table with the ground at z = −84:

| Brief says | Recomputed | |
| ---------- | ---------- | - |
| head center z = +48 | station 132 − 84 | |
| top of head z = +66 | station 150 − 84 | the figure's full height lands here |
| head 36 tall | 66 − 30 | |
| head underside z = +30 | 66 − 36 | |
| gap to the torso 6 | 30 − 24 | agrees with the plan's own tilt working |
| corner 23.4 from the neck axis | √(18² + 15²) = 23.43 | on a 36 × 30 underside |
| tilt without a boss 15° | asin(6 / 23.4) = 14.8° | |
| torso spans z −24 to +24 | 48 centered on the origin | hip and shoulder stations land on its faces |

## What is deliberately left open

Both briefs carry their open questions rather than resolving them, because resolving them is a
design decision and the person who makes those is asleep:

- the stand-off at the shoulder and hip, which the parts sheet flags in red
- boss diameter and protrusion away from the neck
- whether the shoulder stud lines up with `#armX` = 27 from a side face at 18
- the size of the eyes and the mouth

The briefs tell the agent to build at the stated number, measure, and report the gap — not to
pick a value that makes it close.

# B5 — the assembly takes this document's own parts

B0 found the copy's assembly still instancing `stickbot-draft9p1` at version `ankle centered`, so it
showed the previous draft's parts and would have ignored everything B1 through B4 edits. B5 moves
all fourteen instances onto this document's own workspace, which is what
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) *Insert from the workspace, and
keep every reference inside one document* now requires.

## B5 runs before B1, not after

The plan put B5 last because a version-linked assembly can only be updated once the parts it takes
have been published. Workspace instances invert that: the assembly follows a Part Studio edit as
soon as the edit is made, so the re-point has to happen first or B1 through B4 are done blind. The
rest pose and the stations are read here as the before picture, and Phase C reads them again.

## How each instance was moved

**Replace instances…**, one instance per operation, choosing the Part Studio and then the part from
the component browser that opens on this document. It is the only tool that reaches another
document's instances; *Update linked document…* offers newer versions on one branch and nothing
else, which B0 records.

*Replace all instances* is on the dialog and does not do what its name says. With all four `u limb`
instances riding on it, only `u limb <1>` moved. So the operation was run fourteen times.

## What the assembly reads now

Every instance names document `4b2e0d48efd37d3327a90afb` with no version, against the element ids
B0 recorded: `torso` `4e48e81a`, `head` `1562dee6`, `u limb` `65681629`, `l limb` `88de5da8`,
`Gripper` `32166c7b`, `Foot` `c01ac566`.

**All thirteen mates survived, none suppressed** — `head to neck`, both shoulders, both elbows, both
wrists, both knees, both ankles and both hips. Onshape reapplies the replaced component's mates, and
here it reapplied all of them, which B0 said would be measured rather than assumed.

## The rest pose, before Phase B edits anything

| instance | x | y | z |
| --- | --- | --- | --- |
| `head <1>` | 0.0000 | 0.0000 | 103.0535 |
| `u limb <1>` | 49.5509 | -7.8236 | 19.2355 |
| `u limb <2>` | -49.5509 | -7.8236 | 19.2355 |
| `torso <1>` | 0.0000 | 0.0000 | 0.0000 |
| `l limb <1>` | 49.5509 | -7.8236 | -28.7645 |
| `l limb <2>` | -49.5509 | -7.8236 | -28.7645 |
| `u limb <3>` | 24.0000 | 0.0000 | -58.0000 |
| `u limb <4>` | -24.0000 | 0.0000 | -58.0000 |
| `Gripper <1>` | 49.5509 | -7.8236 | -76.7645 |
| `Gripper <2>` | -49.5509 | -7.8236 | -76.7645 |
| `l limb <3>` | 24.0000 | 0.0000 | -106.0000 |
| `l limb <4>` | -24.0000 | 0.0000 | -106.0000 |
| `Foot <1>` | 24.0000 | 0.0000 | -154.0000 |
| `Foot <2>` | -24.0000 | 0.0000 | -154.0000 |

The hips, knees and ankles sit at x ±24 and the arms hang at x ±49.5509, so the pose is symmetric
and the legs are on the stations 9p1 built. The assembly's bounding box stands 317.0535 tall, which
is the height A2 says becomes 317.0000 once `#collar` is re-based.

The model was opened and turned: the robot stands, the arms hang, and the feet sit flat and apart.
`b5-after.png` is that view.

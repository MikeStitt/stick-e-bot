# The reference construction

**How `stickbot-draft9p1p1` is built, read off the model itself and off nothing else.** This is what
a take follows and what `audit.part` diffs against, so that a part which reaches the right shape by
the wrong construction is a finding rather than a pass.

The reference is `stickbot-draft9p1p1`, `4b2e0d48efd37d3327a90afb`, workspace
`a1af16872d25103815f1c32a`. It is read only.

## What each file holds

| File | What it is |
| ---- | ---------- |
| `body.json` | 33 features |
| `head.json` | 26 |
| `ball-and-socket.json` | 14 |
| `foot.json` | 24 |
| `hinge.json` | 49 |
| `u-limb.json` | 10 |
| `l-limb.json` | 10 |
| `gripper.json` | 15 |
| `assembly.json` | 14 instances and 13 mates, with each mate's type and the two instances it joins |
| `variables.json` | the 11 rows of `robot sizes`, with their expressions |
| `documents.json` | the element ids of `stickbot-draft9p3` and `stickbot-draft9p3-check` |

Each Part Studio file carries `order`, the feature tree top to bottom, and `features`, a map from a
feature's name to the `upstream` it was built on and the `downstream` built on it.
[`../../../../tools/read_construction.py`](../../../../tools/read_construction.py) wrote them and
[`../../../../tools/diff_construction.py`](../../../../tools/diff_construction.py) reads two of them
against each other.

## What is in these files, and what is not

**A feature's name, its place in the order, and what it stands on.** That is enough to catch a
boolean operating on the wrong body, a mirror mirroring a loose solid, and a sketch drawn on the
wrong plane, which is four of the four differences found between draft9p2's body tab and this one.

**Not a sketch's constraints, an extrude's end condition, or what a dimension measures from.** Those
live in `/api/partstudios/.../features`, which is rate limited to zero until about 12:30 on
Sat 29 Aug. These files are corrected against that route once it answers, and a take run before then
carries the gap rather than claiming it does not exist.

**Not the mate connectors' names in `assembly.json`.** A mate names its connectors by the Part Studio
feature id that made them, and the id-to-name map comes from the same refused route. The mate names,
the mate types and the instances each mate joins are all recorded.

## What the assembly's order says

Mates were made head, then the left arm shoulder-elbow-wrist, then the right arm elbow-wrist-shoulder,
then the left leg knee-ankle-hip, then the right leg knee-ankle-hip. The second arm and the second leg
each start at the joint furthest from the torso, which is what copying a mated limb and then
attaching it looks like from the outside.

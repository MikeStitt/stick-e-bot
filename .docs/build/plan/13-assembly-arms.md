# 13. One arm, then the other by copy

Starts from a robot with a head. Ends with two arms, only one of which was built a piece at a
time.

**The lesson is that a copied set of mated parts arrives already mated.** So the arm is built
the slow way once — place, mate, place, mate, place, mate — and then the whole thing is copied
and one mate attaches it to the other shoulder. A student does the work once and gets it twice.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.assembly.place_arm` | insert an upper limb and a lower limb from the workspace | two instances |
| `cad.assembly.mate_shoulder` | ball mate, upper limb's `shoulder end` to the torso's `left shoulder` | `left shoulder` |
| `cad.assembly.mate_elbow` | revolute mate, lower limb's `elbow end` to the upper limb's `elbow end` | `left elbow` |
| `cad.assembly.place_gripper` | insert a gripper from the workspace | one instance |
| `cad.assembly.mate_wrist` | ball mate, gripper to the lower limb's `wrist end` | `left wrist` |
| `cad.assembly.copy_arm` | select the upper limb, the lower limb and the gripper; copy; paste | three instances, and the elbow and the wrist carried with them |
| `cad.assembly.mate_shoulder_2` | ball mate, the new upper limb to the torso's `right shoulder` | `right shoulder` |

**A copied mate arrives with the original's name and gets renamed.** Paste brings `left elbow` and
`left wrist` across as copies, and the reference carries them as `right elbow` and `right wrist`.
Renaming them is part of the paste step, not a tidy-up afterwards: a tree holding two mates called
`left elbow` is a tree a student cannot read back.

**The elbow is the robot's first revolute mate.** Every mate before it has been a ball. A hinge
turns about one axis and a ball does not, and this is where that difference becomes something a
student can feel by dragging.

**Two mates arrive for free in `copy_arm`** — the elbow and the wrist — and one mate is placed
after it. That ratio is the argument.

**No hinge takes a width mate.** A revolute leaves one rotation and nothing else, so the blade
cannot slide in its fork and there is nothing for a width mate to remove; the 0.6 mm of clearance
each side is a fit in the printed solid.
[`../../experiments/build-briefs/assembly.md`](../../experiments/build-briefs/assembly.md) asked
for one until draft9p1 counted the assembly's degrees of freedom, and it is withdrawn there.

## The shots this tutorial needs by name

### The mates

Every pick is a medium view and a close-up with a ring, per [`shots.md`](../shots.md). Four picks
per mate, two mates picked per joint. Beyond that:

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the whole robot in the medium view, every time | *which* shoulder is not answerable from a picture of one shoulder | |
| the mate dialog after the first pick | | |
| the mate dialog after the second pick, with the preview | | |
| the mate type list, with ball and revolute both visible | the choice is the lesson at the elbow | |
| the elbow dragged, two or three positions | a revolute against a ball, shown rather than described | |

### The copy and paste

This is the operation nothing in guide 4 has ever done, so it is shot generously and cut down
afterwards.

| Shot | Why |
| ---- | --- |
| the instance list before the copy | the baseline half of every before-and-after here |
| the mate list before the copy | the frame that proves the claim, and the one nobody thinks to take |
| the three parts selected, in the graphics area | |
| the same three selected in the instance list | if both routes work, both are worth a frame |
| the instance list after the paste | what the copies are called |
| the mate list after the paste | the elbow and the wrist, arrived without being made |
| the graphics area after the paste | where the copies landed |

**The mate list before and after is the whole proof.** Everything else is bookkeeping.

## What we do not know yet

**Whether the selection has to be made in the graphics area or in the instance list.** Both are
plausible and the page should teach whichever is more reliable. Try both.

**Where the pasted instances land.** On top of the originals, offset, or at the origin. If they
land on top of the originals the frame is confusing and the page needs to say what to expect.

**What the pasted instances are called.** If they arrive as `<5>`-style suffixes, the page has to
say how to tell them apart before the next mate is picked — and picking the wrong upper limb for
`mate_shoulder_2` is exactly the kind of silent error the two-frame rule exists to prevent.

**Whether the shoulder mate is carried by the copy.** It should not be — the torso is not in the
selection — but if it is, the plan for both this tutorial and the next changes.

**Whether the copied arm arrives mirrored or parallel.** A parallel copy on the other shoulder
gives a robot with two right arms. If that happens it is worth one deliberate frame, because it is
the mistake a student will make and it looks almost right.

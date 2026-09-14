# 7. The head is mated to the torso

Starts from a torso with five studs and a head with a socket, both floating in the assembly. Ends
with the robot's first working joint.

**Short, and the first time anything in the assembly moves.**

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.assembly.fix_body` | fix the torso, so the robot has a ground | a fixed constraint |
| `cad.assembly.mate_head` | ball mate, head socket to neck stud | `head to neck` |

**Fixing the torso first is the habit, not a detail.** Everything after this hangs off it, and an
assembly with nothing fixed drifts when a mate is added.

## The shots this tutorial needs by name

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the torso before and after fixing | the icon that appears is the whole signal | |
| the head's connector, medium and close-up with a ring | first pick | `req.shot.two_frame` |
| the neck stud's connector, medium and close-up with a ring | second pick | `req.shot.two_frame` |
| the mate dialog after the first pick | what it shows with one of two picks made | |
| the mate dialog after the second pick, with the preview | the moment it snaps | |
| the head dragged, two or three positions | this is what a ball mate *is*, and a still of a finished mate shows none of it | |

**The dragged head is the payoff of the whole first half of the build.** Everything until now has
been geometry that did not move.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 7 - the head is mated to the torso** (`7f355cc3e40efbf26d248705`). The `stickbot`
assembly was standing where tutorial 3 left it, with `torso <1>` on the origin and `head <1>`
90 mm above it, and the written page was followed step for step.

**The assembly ends with two instances, one fixed part and one mate.** `torso <1>` carries the
ground mark; `head <1>` does not. **Mate features** reads 1 and holds `head to neck`, which reads
back over REST as a `BALL` mate. Its two connectors are `head mate of head <1>` and
`neck of torso <1>`, read off the dialog: the assembly route answers with the mate's type and name
but returns no id for either mated entity.

**The head lands at (0, 0, 104) mm and nothing typed that number.** `head mate` sits 46 mm below
the head's own middle and `neck` sits 58 mm above the torso's, so the mate puts the head's middle
at 58 plus 46. draft9p3 measured 103 mm with the head 0.8 mm off the middle line, because its
`head mate` inferred a centroid; draft9p4's infers the ball's center and the offset is gone.

**Dragged, the joint turns about that one point and comes back to it.** Three pulls left the head
at (−18.16, 1.19, 100.25) mm, (−3.88, −32.91, 89.9) mm and (−3.09, −10.71, 102.63) mm, and three
undos put it back at (0, 0, 104) mm exactly. The torso did not move on any of them.

**`stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) carries its own version
**tutorial 7 - the head is mated to the torso** (`79b42d425f9024fcc7cd99ea`), taken where the
page's frames were shot. Read back side by side, the two documents agree on the assembly tree, the
instance list, which instance is fixed, the mate count, the mate's name and type, and both
occurrence transforms. The three drag positions agree to two decimals as well.

## Captured

**`instructions/stickbot-draft9p4/source/mate-head.rst`**, written from the 19 frames in
`instructions/stickbot-draft9p4/source/images/mate-head/`, captured across four steps in
`stickbot-draft9p4-check`. `ninja check` comes back clean with no paragraph above grade 8, and
`tools/page_sweeps.py`'s four sweeps come back clean: every frame on disk is used, every frame the
page names is on disk, no picture stands above its sentence, and both view keys the take pressed
are named in the blocks that show them.

**`fix_body` gains a fourth frame, and it is the one that carries the point.** The mark that
arrives on `torso <1>` is about 12 px across in a 1600 px window, and the full-window frame after
**Fix** looks identical to the one before it. The close-up brackets both instance rows, so the
hatched ground mark on the torso and the three free arrows on the head are one picture.

**Each of the two connector picks gets a medium frame and a cropped close-up**, which is
`req.shot.two_frame` read for a tree row rather than a piece of geometry. The medium frame is the
whole window with the dialog open, and the close-up is the left panel around the row, ringed.

**The Ball mate button is found by its tooltip.** An assembly toolbar button carries no `title` and
no `aria-label`, so nothing in the DOM says which of the eleven mate buttons is which. The frame
keeps the pointer on the button, so the tooltip is in the picture and names it.

## What we do not know yet

Nothing on this page is open. The three questions it carried were driven in
`stickbot-draft9p4` and answered.

**The first pick is the part that moves, and fixing the torso makes that stop mattering.** Onshape
says so on the button: *the 1st selection serves as the rotational movement point, and the 2nd
selection serves as the stationary point*. Driven with nothing fixed and `neck` picked first, the
**torso** traveled 14 mm down to meet the head. Driven again with the torso fixed, the reversed
order put the head at (0, 0, 104) mm, the same place the right order does, because a fixed part
cannot move and Onshape has to move the other one.

**A wrong pick is a pick in the graphics area, and it reads
`Mate connector of torso <1>`.** Clicking the torso's front face with one connector already in the
dialog filled the second box with that generic name, where the tree row fills it with
`neck of torso <1>`. The neck ball itself cannot be clicked at all at this point, because the head
hangs over it until the mate lifts it.

**The drag is capturable as a sequence.** Three pulls from one grab point, each read back through
the occurrence transform to prove it moved somewhere new, then one undo per pull. The same answer
carries to the tab drag in [`03-assembly-first-parts.md`](03-assembly-first-parts.md).

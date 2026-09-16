# 8. The foot

Starts from a robot with a working neck. Ends with a foot that has a socket in it.

## The steps

### The numbers this tutorial adds

**Thirteen rows, all of them the tab's own, and none of them opens the tutorial.** Each goes in at
the step that first reads it, which is the step directly under it in the table below. `robot sizes`
gains nothing here: `#torsoH`, `#ball`, `#wall` and `#collar` are already there, and the foot reads
them.

| variable | expression | at the robot's size | typed at |
| -------- | ---------- | ------------------- | -------- |
| `#collar_r` | `#ball / 2 + #wall` | 7.8 mm | `collar_variable` |
| `#plate` | `12 mm` | 12 mm | `plate_variables` |
| `#collar_down` | `#collar` | 10 mm | `plate_variables` |
| `#pedestal` | `#plate - #collar_down` | 2 mm | `plate_variables` |
| `#foot_l` | `#torsoH` | 96 mm | `outline_variables` |
| `#foot_w` | `#torsoH / 2` | 48 mm | `outline_variables` |
| `#heel_r` | `#foot_w / 3` | 16 mm | `outline_variables` |
| `#toe_r` | `#foot_w / 2` | 24 mm | `outline_variables` |
| `#heel_y` | `#foot_l / 3` | 32 mm | `outline_variables` |
| `#ankle_h` | `#torsoH / 4` | 24 mm | `ankle_variable` |
| `#top_round` | `8 mm` | 8 mm | `round_variable` |
| `#rib_w` | `6 mm` | 6 mm | `groove_width_variable` |
| `#rib_d` | `2 mm` | 2 mm | `groove_depth_variable` |

**The plate's three rows are one chain and arrive together.** `#pedestal` is `#plate` less
`#collar_down`, so neither term can come after it, and the extrude that reads all three is the step
that forces them.

**The outline's five are one sketch's doing.** `foot outline` dimensions both circles and places
both of them, and `#heel_r`, `#toe_r` and `#heel_y` are each written from `#foot_l` or `#foot_w`.

**The groove's two numbers arrive one step apart.** The sketch draws a rectangle `#rib_w` along the
foot; the extrude cuts it `#rib_d` deep. Neither step reads the other's number.

**Four of the thirteen are typed.** `#plate`, `#top_round`, `#rib_w` and `#rib_d` are thicknesses
and radii the printer and the ground decide, not fractions of the robot. The other nine are
fractions of the torso or of the joint.

### The features

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.foot.tab` | a Part Studio called `foot` | |
| `cad.parts.foot.collar_variable` | `#collar_r`, the radius the pedestal matches | `#collar_r` |
| `cad.parts.foot.pedestal_sketch` | the pedestal the socket sits in | `pedestal outline` |
| `cad.parts.foot.plate_variables` | `#plate`, `#collar_down` and `#pedestal` | three variables |
| `cad.parts.foot.pedestal` | extrude it | `foot pedestal` |
| `cad.parts.foot.outline_variables` | the foot's length, width and two radii | five variables |
| `cad.parts.foot.outline_sketch` | the foot's plan shape | `foot outline` |
| `cad.parts.foot.ankle_variable` | `#ankle_h`, how high the ankle stands | `#ankle_h` |
| `cad.parts.foot.body` | extrude it | `foot` |
| `cad.parts.foot.round_variable` | `#top_round` | `#top_round` |
| `cad.parts.foot.top_round` | round the top | `top round` |
| `cad.parts.foot.groove_width_variable` | `#rib_w` | `#rib_w` |
| `cad.parts.foot.groove_sketch` | one sole groove | `groove profile` |
| `cad.parts.foot.groove_depth_variable` | `#rib_d` | `#rib_d` |
| `cad.parts.foot.groove` | cut it | `sole groove` |
| `cad.parts.foot.ribs` | pattern it along the sole — eight, at `2 × #rib_w` | `sole ribs` |
| `cad.parts.foot.socket.derive` | bring the socket in, onto the pedestal | `add socket` |
| `cad.parts.foot.combine` | union | `combine parts` |
| `cad.parts.foot.rename` | call the part `Foot` | |
| `cad.parts.foot.connector` | the foot's mate connector | `mate to robot` |

**The derive has moved.** Stickbot derives the socket as feature 1, before any of the foot's own
geometry, and every other consumer in the robot builds its host shape first. It works either way;
one of them is the shape the robot teaches, and this plan makes it the common one so that a
student meets the same sequence five times instead of four and an exception.

**Stickbot calls it `grove profile`.** It is a groove.

**The foot declares no `#wall` of its own.** It reads the Variable Studio's, which is the only
one and is `#torsoH * 3 / 160`, 1.8 mm at the robot's size. draft9p0 declared `#torsoH / 32` here
against the joint's literal 3 mm, and the two collars, the foot's own and the derived socket's,
coincided at the robot's size and parted at any other.

**The pedestal's two numbers are derived here, and stickbot types them.** `stickbot-draft9p1p1`
declares `#collar_r = 9 mm` and `#collar_down = 9 mm` with nothing upstream of either, and they are
`#ball / 2 + #wall` and `#collar` copied out as constants at the size the robot had then. At the
settled rows they are **7.8 mm** and **10 mm**, so `#pedestal`, which is `#plate - #collar_down`,
goes from 3 mm to **2 mm**. The pedestal is the seat the socket lands in, so a seat that does not
follow the collar is a seat the socket stops fitting, and nothing in the tree turns red when it
happens. `#collar_r` becomes `#ball / 2 + #wall` and `#collar_down` becomes `#collar`, which puts
this tab's pedestal on the same two rows the socket itself is built from.

**The first groove sits `#rib_w / 2` in from the end of the sole**, so it is centered in its own
repeat and the tread starts and ends with land. draft9p0 offset the pattern by `#foot_l −
`#heel_y`, which is 64 on a 96 sole and put five of the eight grooves off the end of the foot.
The arithmetic and the two candidate phases are
[`../../experiments/runs/2026-08-25-draft9p1/a5-foot-tread.md`](../../experiments/runs/2026-08-25-draft9p1/a5-foot-tread.md).

## The shots this tutorial needs by name

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the foot | `req.page.hero` |
| the pattern's direction and count, before and after | a pattern that goes the wrong way is the common failure | |
| the derived socket where it arrives | the arc that worked for the head, third time | |
| the sole from below, before and after the pattern | a pattern that goes the wrong way is the common failure | |
| the tree, the version dialog | | |

**There is nothing to place.** The head's socket arrives at the origin and is then moved down the
neck, so it needs a frame of "arrived" and a frame of "placed". The foot's pedestal is drawn around
the origin for exactly this reason, so Base origin puts the socket on the pedestal and the tutorial
has no transform in it at all. The arc is one frame.

**The part is renamed, and a step table built by reading a feature tree cannot see that.**
Renaming a part happens in the parts list and is never a feature. 9p1p1 calls this one `Foot`, and
tutorials 13 and 14 insert parts by name.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 8 - the foot** (`7d52c006c01d272fd24cd706`). The tab arrived carrying draft9p3's
construction, so it was emptied newest row first and rebuilt by following the written page.

**The tab ends with 31 rows and one part.** Thirteen variables, each directly above the feature
that reads it; eleven features; and `Foot`:

```
Default geometry, Origin, Top, Front, Right, #collar_r = 7.8 mm, pedestal outline,
#plate = 12 mm, #collar_down = 10 mm, #pedestal = 2 mm, foot pedestal, #foot_l = 96 mm,
#foot_w = 48 mm, #heel_r = 16 mm, #toe_r = 24 mm, #heel_y = 32 mm, foot outline,
#ankle_h = 24 mm, foot, #top_round = 8 mm, top round, #rib_w = 6 mm, groove profile,
#rib_d = 2 mm, sole groove, sole ribs, add socket, combine parts, mate to robot, Parts (1), Foot
```

**The foot measures what the page says it measures.** The part runs x ±24 mm, y −64 to +32 mm and
z −24 to +2.22 mm, which is 96 mm heel to toe, 48 mm across the toe and 24 mm from the ground to the
middle of the ball. The pedestal disc is 15.6 mm across and stands from 12 mm down to 10 mm down.
Sixty faces: 52 planes, 5 cylinders, 2 tori and the socket's sphere, carrying radii of 6.08, 7.8,
8.0, 16.0 and 24.0 mm. Eight groove roofs stand at z −22 mm.

**`mate to robot` is at the origin**, which is the middle of the socket's ball, and the derived
socket's own connector is 10 mm below it. Both were read through featurescript; `/features` was rate
limited for the rest of the run.

**`stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) carries its own version
**tutorial 8 - the foot** (`72b2929e96c17844bb44f7b9`), taken where the page's frames were shot.
Read back side by side, the two documents agree on all 31 tree rows, the part's name, the bounding
box, the face count, the count of each kind of face, the five radii, the eight groove roofs and both
connector origins.

## Captured

**`instructions/stickbot-draft9p4/source/foot.rst`**, written from the 115 frames in
`instructions/stickbot-draft9p4/source/images/foot/`, captured across 24 steps in
`stickbot-draft9p4-check`. `ninja check` comes back clean with no paragraph on the page above grade
8, Sphinx builds it without a warning, and `src/stickbot/page_sweeps.py`'s five sweeps come back
clean: 115 frames on disk and 115 used, no picture above its sentence, and all 19 recorded key
presses named in the blocks that show them.

**The page reproduces.** Driven back into `stickbot-draft9p4` from the written text, 20 of the 22
stages stood on their first attempt. The two that did not were a screenshot that would not settle
and a tree caret, and neither is a step the reader takes.

**The variables are seven steps, not one table.** Thirteen rows arriving in ones, threes and fives
means seven visits to the same dialog, which is seven pictures of a dialog the reader has already
met. Each visit carries one sentence about why those rows and not others, and the frames are the
dialog with the expression in it and the row standing in the tree.

**The pattern step is eleven frames, and it is the longest step on the page.** Four separate things
have to be right and three of them fail silently; see `## What the run answered` below.

## What the run answered

**The reorder does not break anything.** The derive stands ninth, after the whole foot exists, and
`Base origin` still puts the socket on the pedestal with no transform, because both were drawn
around the same origin. Nothing needed the socket to exist first. The reorder is not required,
then; what it buys is that the page's three extrudes read **New**, **Add** and **Remove** in that
order, and that the union at the end has both solids already standing.

**The sole ribs earn their frames.** The pattern can be got wrong four ways, and three of them
leave the sole with the one groove it started with and nothing red in the tree: **Reapply features**
arrives unticked, the **Direction** box has to be clicked before the plane is picked, and the copies
have to be sent toward the heel. The fourth is that **Feature pattern** is on a dropdown under
**Part pattern**, which at least announces itself. It is also the only linear pattern in the guide
before the hinge, and the hinge's patterns go about a mate connector's axis, which is a different
dialog path. Eleven frames is what it takes to show four things that each look like nothing
happening.

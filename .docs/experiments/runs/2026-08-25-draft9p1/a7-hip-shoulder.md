# A7 — the torso's width places the hips

The `body` tab writes the two limb stations side by side:

    #hip_half       =  #torsoH / 4      24
    #shoulder_half  =  #torsoW / 2      36

The second is right. The first names the wrong number, and gives the right answer anyway at every
size the robot has ever been driven to.

## The design source never had this defect

`make_plans.py` places both stations off the torso's width and neither off its height:

| station | the sheet | at the robot's size |
| --- | --- | --- |
| `LEG_X` | `TORSO_W / 2 - LIMB / 2`, commented *legs flush with the torso's sides* | 24 |
| `SH_X` | `TORSO_W / 2 + SH_DX` | 36 + 13.55 |

So A7 is not a decision about which number is correct — the sheet settled that when it was drawn.
It is one expression in one tab of the model, and a page that says what to type.

## Why driving `#torsoH` could never find it

The torso is 72 wide and 96 tall, so `#torsoW` is `0.75 × #torsoH`, and the limb is `#torsoH / 4`.
Put those into the expression the hip should have:

    #torsoW / 2 - #limbD / 2  =  0.375 × #torsoH - 0.125 × #torsoH  =  #torsoH / 4

The right expression and the wrong one are **the same function of `#torsoH`**. Driving `#torsoH` to
120 moves the hips correctly, because at 120 the torso is still 0.75 as wide as it is tall. The two
part company only when `#torsoW` moves on its own, which is why B3's first pass saw nothing and the
second pass — `#torsoW` 72 → 90 → 72 — put the body 21 mm over each hip.

**Two definitions that evaluate the same are indistinguishable from one**, and this pair stays
indistinguishable through a whole sweep of the number most likely to be swept. It is the strongest
case in the register for driving *every* number in the studio rather than the biggest one.

## What `body` builds instead

    #limbD          =  #torsoH / 4                 24
    #hip_half       =  #torsoW / 2 - #limbD / 2    24
    #shoulder_half  =  #torsoW / 2                 36

`#hip_half` is a half-width less a half-limb because that is what puts the leg's outer surface flush
with the torso's side — the thing the sheet's comment has always said and the thing a reader can
check by eye on the elevation.

`#shoulder_half` stays as it is. It is the side **face**, not the ball: the stud runs `#shoulder_len`
out along a tilted direction and the ball lands 13.55 mm clear of that face. The face is placed by
the width, so the expression is already the right one.

**`#limbD` has to be declared in `body` to write this.** Three tabs already declare their own
`#limbD = #torsoH / 4` — `hinge`, `u limb` and `l limb` — and `body` becomes the fourth. That is the
same shape of thing A6 found in `#wall`, without the harm: all four copies agree, and they agree
because they are the same expression rather than by arithmetic accident.

## What this hands to A13

The rule that moved `#wall` up into the Variable Studio reaches further than `#wall`. Reading every
tab's variables back off draft9p0, four names are declared in more than one Part Studio:

| name | tabs that declare it | expressions |
| --- | --- | --- |
| `#ball` | `body`, `ball and socket`, `foot`, `gripper` | all four `#torsoH / 8` |
| `#limbD` | `hinge`, `u limb`, `l limb`, and now `body` | all `#torsoH / 4` |
| `#collar` | `ball and socket`, `foot` | both `11 mm` |
| `#grip` | `ball and socket`, `foot` | both `3.6 mm`, and A2 makes both 1.9465 |

None of these is broken today; every copy of every one of them agrees. They are listed here because
A13 republishes the table and is the place to decide how many of them move up. `#ball` is the
strongest candidate — four tabs, and it is the joint's driving number — and `#grip` is the one where
leaving four copies to be edited by hand is a way to reintroduce exactly the defect A6 found.

## Found while reading, for other rows

**`#shoulder_len` is a typed `26 mm`.** The comment in `make_plans.py` says it is set by the torso
rather than by the joint, and at `#torsoH` 120 the stud would still run 26 out from a wider torso
while the ball it carries grew. This is the same failure as A9's `#boss_d` in the same feature, so
A9 is the row that should settle it.

**`LIMB` was a typed 24 in the design source** while three tabs of the model wrote
`#limbD = #torsoH / 4`. It now derives. Regenerating found five labels that printed it through a
bare `{LIMB}` rather than `{LIMB:g}`, so the sheets read `Ø24.0`; those are fixed and the parts
sheet came back byte-identical.

**`plan-assembly.svg` was stale in the commit before this one.** Regenerating with no source change
at all moves the figure 1.57 mm and rescales the type, which means it was last written before the
foot gained its tread in A5. It is regenerated here. A12 rebuilds both sheets from scratch anyway.

**`01-torso.md` cited a rule it did not contain.** A6 wrote *the rule this page already states — if
a dimension turns out to be read by two tabs, it moves up*, and [`a6-wall.md`](a6-wall.md) wrote
*the rule `01-torso.md` already wrote down*. Neither was true; the rule was reasoned out in A6 and
attributed backwards. `01-torso.md` now states it as its own rule, which is where a rule about what
the Variable Studio holds belongs, and `a6-wall.md` says where it came from.

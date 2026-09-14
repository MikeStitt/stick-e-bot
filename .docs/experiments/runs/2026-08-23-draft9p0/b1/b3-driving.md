# B3 — `#torsoH` driven 96 → 120 → 96

`robot sizes` holds four numbers and nothing else: `#torsoH` 96, `#torsoW` 72, `#torsoD` 48,
`#limbSeg` 48. B3 sets the first of them to 120, reads the whole model back, sets it to 96 again and
reads it back a second time. `req.model.design_intent` is the requirement, and the question it asks
is whether the figure follows or the model falls apart.

**It follows.** Every Part Studio regenerated, no feature failed, no mate dropped, and setting 96
back gave a model identical to the one B2 measured. What the drive found is not breakage — it is
four places where a number does not follow, and one of them cannot be seen at any other size.

## What followed, exactly

`120 / 96` is 1.25, and every cross-section is 1.25 of what it was:

| part | 96 | 120 | ratio |
| --- | --- | --- | --- |
| torso, z | 128.00 | 155.00 | the 96 box itself went 96 → 120, measured on its two cut planes |
| head, x | 72.00 | 90.00 | 1.2500 |
| `Ball stud`, x and y | 12.00 | 15.00 | 1.2500 |
| `Foot`, x and y | 48.00 · 96.00 | 60.00 · 120.00 | 1.2500 |
| `blade`, `fork`, `u limb`, `l limb`, x and y | 24.00 | 30.00 | 1.2500 |
| `Gripper`, x | 18.00 | 22.50 | 1.2500 |

The ball is `#torsoH / 8` and everything jointed hangs off it: ball r 6.000 → 7.500, stalk 3.000 →
3.750, cavity 6.800 → 8.300, collar 9.000 → 10.500, limb 12.000 → 15.000. The whole robot is one
chain of derivations from one typed number, and driving it is the proof.

## What deliberately did not follow, and should not

**The joint's print numbers are literals, and they hold their size.** `#fit` 0.8, `#wall` 3.0,
`#grip` 3.6 and `#collar` 11 are typed, so the socket's four cut planes stay at −7.4, −4.4, 3.6 and
10.0 at both sizes, and the collar keeps its 11 mm of length. The consequence is the good one: the
printed wall is 10.5 − 8.3 = **2.20 at 120 exactly as it is at 96**. A wall that scaled would get
thicker on a bigger robot and thinner on a smaller one, and 2.20 is the number the printer cares
about. This is the model doing the right thing and it is worth saying so.

**The hinge's snap features are literals too** — 96 faces at r0.8, 48 at r1.0, the r2.0 pocket and
the r2.2 stub are unchanged at both sizes, while the r12 nose goes to r15. The detent has to fit a
printer, not a robot.

**`#limbSeg` is its own number, so the limbs barely moved.** `u limb` went from 116.0 long to
122.0 — the 6 mm is two nose radii, not a segment. That is correct: the limbs are meant to be
driven by `#limbSeg`, and `#torsoH` has no business lengthening them.

## The expressions, read rather than inferred

Driving the table says which numbers move together. It does not say why, and the first draft of this
file guessed at three of the reasons and got them numerically right and causally wrong. The feature
list carries the actual expressions, so they were read: every Variable feature in all eight Part
Studios, in [`b3-variables.json`](b3-variables.json), fetched by
[`scripts/2201_b3_exprs.py`](scripts/2201_b3_exprs.py).

Two things about that fetch are worth writing down. The expression is in the parameter's
`expression` field and its `value` field is a hard `0`, so a reader that prefers `value` gets zero
for every variable in the document and no error. And `/features` is the endpoint that spent most of
this run rate limited account-wide; eight calls four seconds apart went through without complaint,
so the limit is not permanent and it is worth one careful try before giving up on it.

The four numbers in `robot sizes` reach exactly this far:

- **`#torsoH`** — the ball (`#torsoH / 8`), the limb (`#torsoH / 4`), the gripper's length, the
  foot's whole footprint and ankle height, the hip spacing, and the head. It is doing most of the
  work in this model.
- **`#torsoW`** — the torso's block and `#shoulder_half`. Nothing else in the document reads it.
- **`#torsoD`** — the torso's block.
- **`#limbSeg`** — the limb segments.

**The `head` tab holds no variables at all**, alone among the eight.

## What did not follow, and should have

### `#wall` is defined twice, and the two definitions agree only at 96

Every variable in every Part Studio was read back off the feature list and is kept in
[`b3-variables.json`](b3-variables.json). One name is declared in three tabs with two meanings:

| tab | `#wall` |
| --- | --- |
| `ball and socket` | `3 mm` |
| `foot` | `#torsoH / 32` |
| `gripper` | `#torsoH / 32` |

`#torsoH / 32` is 3 at 96 and 3.75 at 120. Both `foot` and `gripper` build their own collar as
`#ball / 2 + #wall`, and both wrap it around a socket **derived from `ball and socket`**, whose
collar used the literal 3. So at 96 the two collars are the same 9.000 and merge into one
cylindrical face with no seam; at 120 the part's own collar is 11.250 and the socket inside it is
10.500.

That is the whole of what the drive found in these two parts. The foot goes from five cylindrical
faces to six, gaining the derived socket's outside and a 0.75 mm ledge as two new annular faces at
z −7.4. The gripper's x extent follows its own collar to 22.500 while its y extent follows the
derived socket to 21.000, so the part changes shape rather than size. Task #28 already has the
gripper's overhang fore and aft; this is the same part failing in the other axis, from a cause
neither of them shares.

**Nothing is wrong at 96 and nothing can be seen at 96.** Two definitions of one name that happen to
evaluate the same are indistinguishable from one definition, and no measurement of the built robot
can tell them apart. Driving the variable is the only thing that can.

**The fix is one line, not three sketches.** `#wall` in `foot` and `#wall` in `gripper` should be
whatever `ball and socket` says, because the collar they are wrapping is the one `ball and socket`
built.

### The head keeps its depth at every size

The head measures 63 mm front to back at 96 and 63 mm at 120, while its width goes 72 → 90. Its
depth is a typed literal, so a driven robot gets a head that grows in two directions and not in the
third. The register already asks whether the head's depth should become a fifth variable; this is
the answer, measured.

### The head's width is driven by `#torsoH`, not `#torsoW`

The head is 72 across at 96 and 90 at 120, which is `0.75 × #torsoH` — and `#torsoW` is also 72.
Drive `#torsoW` alone and the head does not move at all. **The `head` tab holds no variables
whatsoever**, the only one of the eight that does not, so its sketches reach straight past the
part's own vocabulary to a global. There is nothing in the tab to read that would tell you which
number it depends on; the only way to find out is to change one and look.

### The torso's shoulder pads keep their radius

`#boss_d` is a typed `16 mm`, so the two angled pads the shoulder balls sit in are r8.0 at both
sizes while the ball they hold goes 6.000 → 7.500. The shoulder around the ball is therefore 2.0 at
96 and 0.5 at 120, and at `#torsoH` = 128 the ball would be r8.0 and the pad would vanish into
it. There is a size at which this model stops having shoulders, and it is only 8 mm away from the
plan sheet's next round number.

### The hips are spaced by `#torsoH` and the shoulders by `#torsoW`

The two are written side by side in the `body` tab:

    #hip_half       =  #torsoH / 4
    #shoulder_half  =  #torsoW / 2

Both are 24 and 36 at the built size and both look right. Drive `#torsoW` to 90 and the shoulders
move out to ±45 while the hips stay at ±24, so the body overhangs each hip by 21 mm. A hip is a
thing the torso's *width* places, and this is the one finding where the wrong variable is written
down in plain sight rather than hidden behind a coincidence.

## A second pass, on `#torsoW`

The plan asks for `#torsoH` only. Three of the findings above turn on whether a sketch names
`#torsoH` where it means `#torsoW`, and one more drive settles it, so `#torsoW` was taken 72 → 90 →
72 the same way.

**`#torsoW` reaches the torso and nothing else.** Every other part measured identical at 90 — the
head did not widen, the foot did not spread, no limb moved. Inside the torso it reaches the
shoulders and stops:

| | 72 | 90 |
| --- | --- | --- |
| torso, x | −55.55 … 55.55 | −64.55 … 64.55 |
| shoulder balls | x ±49.55 | x ±58.55 |
| hip balls | x ±24.00 | x ±24.00 |

So the head's width really is `#torsoH` and not `#torsoW`, and **the hips are not placed by the
torso's width at all**. Widen the torso and the legs stay where they were: at `#torsoW` 90 the body
overhangs each hip by 21 mm. Two of the four numbers in `robot sizes` point at the same hip, and the
one that ought to is not the one that does.

## Both round trips came back exact

After each drive the variable was set back and the whole model read a third time. The comparison is
every part bounding box, every cylinder and sphere radius with its count, every planar cut-face z
with its count, and every face area:

    #torsoH  96 → 120 → 96     identical
    #torsoW  72 →  90 → 72     identical

Not "within tolerance" — identical, to the six decimal places the API answers in. A variable studio
that drives a model this far and returns it unchanged is the whole claim of
`req.model.design_intent`, and it is now measured rather than asserted.

**The assembly survived both.** It still holds fourteen instances and thirteen mates, each with the
name it was given: `head to neck`, four Balls at the shoulders and hips, four more at the wrists and
ankles, and four Revolutes at the elbows and knees. Nothing dropped, nothing came back
under-defined, and no mate needed re-picking.

## How it was done

- `robot sizes` opened in its own tab, the value cell clicked, the number typed, Enter.
- The whole model read back over REST with the B2 fetch script after every change. The two driven
  reads are kept: [`b3-raw-120.json`](b3-raw-120.json) and [`b3-raw-w90.json`](b3-raw-w90.json).
  The two restored reads are not — they are identical to [`b2-raw.json`](b2-raw.json), which is the
  finding.
- Compared offline with `2104_b3_diff.py` (what moved), `2106_b3_ratio.py` (by how much) and
  `2107_b3_same.py` (did it come back).

**A screenshot of the 120 mm robot could not be taken.** `page.screenshot` timed out twice on the
assembly tab while the bigger model was live, at 30 s and again at 120 s, and the same call works
on every other tab. The drive is evidenced by measurement instead, which is the stronger evidence
anyway — but if a later run wants the picture, expect to fight for it.

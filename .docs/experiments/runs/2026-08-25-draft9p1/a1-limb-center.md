# A1 — `#limbCenter`, and what the parts sheet actually draws

The decision is the user's, taken on 2026-08-25 and recorded as U6 in
[`../2026-08-23-draft9p0/register.md`](../2026-08-23-draft9p0/register.md): **`#limbSeg` becomes
`#limbCenter` and means joint center to joint center.** This file is the arithmetic that decision
needs, measured off `make_plans.py` rather than read off its comments.

## What the sheet draws, measured

`limb(kind, length, top, bottom, ...)` draws the rod from y = 0 to y = length and then places a
joint at each end. Where each joint's center lands is not the same at the two ends, and is not the
same between limbs:

| Part | top joint, and where its center lands | bottom joint | center to center |
| ---- | ------------------------------------ | ------------ | ---------------- |
| upper arm | `socket(-r, 5, "right")` — ball center at y 5 | `clevis(0, L)` — pin at y 48 | **43.0** |
| thigh | `socket(0, 0, "up")` — cavity center at y `+#grip` | `clevis(0, L)` — pin at y 48 | **44.4** |
| forearm | `blade(0, 0)` — pin at y 0 | `stud(0, L, "down")` — ball center at y `L + #stand` | **58.0** |
| shin | `blade(0, 0)` — pin at y 0 | `stud(0, L, "down")` — ball center at y `L + #stand` | **58.0** |

**The station math spaces every joint by 48.** `EL_X, EL_Z = SH_X + ARM_SEG * sin, …` and
`KNEE_Z, ANKLE_Z = HIP_Z - LEG_SEG, HIP_Z - 2 * LEG_SEG` all step by `ARM_SEG`/`LEG_SEG`.

**So no limb on the sheet is 48 center to center, and no two of them agree.** The elevation places
the joints 48 apart; the parts sheet draws them 43, 44.4, 58 and 58 apart. The 48 is true of the
rod and of nothing else.

**This withdraws what U6 was recorded against.** U6's entry says the sheets already draw the joint
centers at the stations and only the name disagreed, on the strength of `clevis()` putting the pin
axis at `y = length` and of the comment at `make_plans.py:90`. The pin does sit at the station; the
socket and the ball stud do not, and the comment describes the fold at the clevis end and says
nothing about the other three ends. **The decision stands and the reasoning under it does not.**
`make_plans.py` is inconsistent with itself, which is a larger defect than the one U6 names.

## What changes

**`#limbCenter` is the input and the rod length is derived from it**, per limb, by subtracting what
each of that limb's two ends spends:

| Part | rod length | at `#limbCenter` 48 |
| ---- | ---------- | ------------------- |
| upper arm | `#limbCenter + inset` | 53.0 |
| thigh | `#limbCenter + #grip` | 51.6 |
| forearm | `#limbCenter − #stand` | 38.0 |
| shin | `#limbCenter − #stand` | 38.0 |

**A2 moved `#grip`, so the thigh now derives 49.95 rather than 51.6** — the expression is what is
settled here, not the number. See [`a2-fit.md`](a2-fit.md).

Every one is positive, so 48 is buildable at every limb — which is the claim U6's entry makes and
the reason the recorded minimum of 52.4 and 54 does not apply. That minimum was arithmetic about
the model's method of standing each joint clear of a full-length rod.

**The parts-sheet label stops reading `Ø24 × 48 mm`.** 48 is the center distance, not the stock, so
the label carries the derived rod length and the center distance is stated as what it is.

## Found while measuring, not fixed here

- **The shoulder socket's 5 is a typed number with nothing behind it.** Every other station on
  these four limbs derives from `#grip` or `#stand`. This one is the inset of the shoulder ball
  center from the rod's top end and no source says why it is 5.
- **The shoulder socket is drawn opening out of the part.** `socket(-r, 5, "right")` puts the mouth
  on the rod's left face and opens it rightward, which places the cavity center at `x = −r − #grip`
  — outside the rod. The other three sockets on the sheet open into material.
- **The sheet draws the shoulder socket as a bare bore and the model derives a collared one.** The
  upper limb's tab derives `ball and socket`'s `Socket body`, which carries the collar and the
  slits; the parts sheet draws a cavity in a face with neither.
- **[`../../../robot-build-plan.md`](../../../robot-build-plan.md) is still at 1×.** Its four
  driving variables read `#torsoH` 48, `#torsoW` 36, `#torsoD` 24, `#limbSeg` 24. The doubling
  reached `make_plans.py` and the briefs and never reached the table the Constitution calls the
  design source.

## Why 48 is buildable, when both limb pages say it is not

[`10-u-limb.md`](../../../build/plan/10-u-limb.md) and
[`11-l-limb.md`](../../../build/plan/11-l-limb.md) each record a minimum: the upper limb's two
joints admit no less than **52.4** between centers, the lower limb's no less than **54**. Both are
below 48, so on their arithmetic `#limbCenter` 48 cannot be built.

**Those minimums measure how draft9p0's model places a joint, not how the sheet draws one.** The
model derives each joint and sets it on an end face, so the whole of its reach is added to the
stock: the fork stands 45 off one end, the blade 44 off another. The sheet buries the same joints
in the rod. `clevis()` draws the fork's root at `y - (SLOT_DEEP - NOSE)`, which is 21 mm back from
the pin and inside the rod, and the comment at `make_plans.py:87` says so in words — *each takes
about 21 mm of a 48 mm segment, and the other end of that segment is a COLLAR_L socket*.

So the minimum is a consequence of stacking, and stacking is the defect. Bury each joint at its
station, the way the sheet has drawn it all along, and the four rod lengths above are what is left
over. Nothing about the hinge's reach has to change for 48 to fit.

**This is a Phase B correction to the limbs and it is A1 that creates it.** B7 places each derived
joint by its mate connector at the station and lets it overlap the rod, then combines. It does not
sit the joint on an end face. The stock lengths it extrudes are 53, 51.6, 38 and 38.

**It also settles the robot's height.** `11-l-limb.md` works it out both ways: stacked, the sole
lands at −284.4 and the robot stands about 422 tall; at 48 and 48 it stands **315.4**, against the
guide's plan page saying around 320.

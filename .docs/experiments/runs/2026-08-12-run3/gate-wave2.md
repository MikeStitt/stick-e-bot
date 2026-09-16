# Launch gate — run 3, wave 2: limbs, hand, foot

Performed against [`../../../2026-08-12-launch-gate.md`](../../../2026-08-12-launch-gate.md)
while wave 1 was still building, so nothing here touches a file a running agent reads.
**Every finding below is fixed, except the one held for the freeze.**

Scope: [`../../build-briefs/limbs.md`](../../build-briefs/limbs.md),
[`hand.md`](../../build-briefs/hand.md) and [`foot.md`](../../build-briefs/foot.md). These were
written after run 2 and have never been gated or built from.

## Blocking, and how each was resolved

**1. `limbs.md` links to a file that does not exist.** `../README.md` resolves to
`.docs/experiments/README.md`; there is no such file. The Stage 5 teaching routes it points at
are discussed in `build-briefs/README.md`, in the same directory. The label was wrong too — it
called them "recorded as open curriculum questions", where the README settles which gives way
(the route, not the diameter) and asks the agent to report hitting one.
*Fixed:* target corrected to `README.md`, label rewritten to say what is actually there.

**2. `hand.md` sources the Ø10 clip to a variable that does not exist.** It is marked `plan`,
citing `#clipR`. The build plan mentions `#clipR` once, in prose, saying it "still wants a look
when the hand is built" — its variables table has no row for it. A number marked `plan` is one
the agent can re-derive from the plan; this one cannot be.
*Fixed:* marked `proposed`, with what the plan actually says about it.

**3. Both briefs mark the socket collar `built` at "Ø9.4 × 5.5".** Neither part of that is
right. Ø9.4 is derived — `2 × (cavity 3.2 + wall 1.5)`, the same finding the wave 1 gate got
backwards. And nothing has been built on a limb or a plate: runs 1 and 2 built the socket on a
20 × 20 pad, which is the defect wave 1 exists to fix.
*Fixed:* split into a `derived` diameter and a length row, in both briefs.

**4. The 5.5 collar length is not a bare proposal.** Tracing it for finding 3 turned up the
plan's justification: the collar's height is what buys the ball joint its swing, and the plan
records **78° with the collar 5.5 proud against 56° bored straight into the face**. The wave 1
brief calls 5.5 a proposal "built at this size without being challenged", which is not what
happened — it was chosen for a reason and the reason is written down.
*Fixed in `hand.md` and `foot.md`; held for `ball-and-socket.md`* — that file is frozen while
its agent reads it. Applied after wave 1 reports.

## Numbers re-traced to `robot-build-plan.md` as it stands today

Every `plan` number traced to its row in the variables table, not to memory:

| Brief | Number | Row |
| ----- | ------ | --- |
| limbs | limb 12 | `#limbD` = `#torsoH / 4` |
| limbs | segment 24 | `#armSeg` = `#legSeg` = `#torsoH / 2` |
| hand | bar 3.2 | `#barD`, not scaled |
| hand | hand length 12 | `#handL` = `#torsoH / 4` |
| foot | length 48 | `#footL` = `#torsoH` |
| foot | width 24 | `#footW` = `#torsoH / 2` |
| foot | ankle height 12 | `#ankleH` = `#torsoH / 4` |
| hand | clip outer Ø10 | **no row** — finding 2 |

Derived numbers recomputed rather than taken from the brief: the clip wall `(10 − 3.3) / 2` =
3.35; the collar step in a Ø12 limb `(12 − 9.4) / 2` = 1.3; the foot's plate edge under an r4
fillet `6 − 4` = 2; the foot's stations `48 / 3` = 16 behind and 32 in front. All agree.

## Open questions checked before they go out as open

- **Four limbs, two parts.** Still open. The plan's part table says eight modeled parts, and
  nothing since has revised it. The brief asks the agent to report rather than act, which is
  right — collapsing it changes the bill of materials.
- **The hand's Ø10 clip against a Ø12 wrist.** The plan says "still open" in as many words.
- **The feet sit outboard of the shins**, `#footHalf` 16 against `#legX` 12. Nothing in the plan
  or the session logs settles it. The brief tells the agent not to pick a value, which is right.

## Note for the launch

`limbs.md` asks for **two documents**, `limb-socket-clevis-run3` and `limb-blade-ball-run3`,
because the four limbs collapse to two parts. That is two agents' worth of work in one brief and
the wave is sized accordingly.

# Launch gate — run 3, 2026-08-12

Performed against [`../../../2026-08-12-launch-gate.md`](../../../2026-08-12-launch-gate.md)
before any agent was launched. **Every finding below is fixed.**

Each finding says where it came from. What the reading pass found is only part of it: sourcing
the hinge's tooth numbers exposed one, **drawing** the joints exposed more after the gate had
otherwise passed, and the user looking at a rendered sheet exposed another. Reading the prose was
the weakest of the four.

Scope: the two briefs going out, `ball-and-socket.md` and `hinge.md`, plus the shared
`build-briefs/README.md` every agent reads. `limbs.md`, `hand.md` and `foot.md` are not launching
in run 3 and were not gated.

## Blocking, and how each was resolved

**1. Neither brief that is launching has a Source column.** `limbs.md`, `hand.md` and `foot.md`
have one; `ball-and-socket.md` and `hinge.md` do not, and those are the two being built.
[`../../run3-launch.md`](../../run3-launch.md) tells the agents "every numbers table carries a
Source column", which is false for both briefs they will read.
*Fixed:* see below.

**2. `build-briefs/README.md` links to two files that do not exist.** From
`.docs/experiments/build-briefs/`, `../onshape-gui-howto.md` resolves into `experiments/` and
`../../.parts/onshape.md` resolves into `.docs/`. Correct targets are `../../` and `../../../`
respectively — `../../robot-build-plan.md` in the same file is right, which is how the other two
went unnoticed. The how-to link is broken in both places it appears. Every agent reads this file,
and the how-to is the document the run depends on most.
*Fixed:* see below.

**3. `ball-and-socket.md` opens with "Nobody has built this joint."** Run 2 built it and measured
the mouth at Ø5.802586. The launch prompt's own tail tells the agent run 2 built it, so the agent
is handed a contradiction before it starts.
*Fixed:* see below.

**4. The same brief still asks a question that has been answered.** *"If the offset does not
apply uniformly over a sphere, this design is wrong and we need to know today"* — run 2 settled
it. Left as written, an agent spends the run deciding something already decided.
*Fixed:* see below.

**5. Relief slits are simultaneously required and optional.** Build order step 6 builds them, an
acceptance check requires them 5.5 mm deep and measures the z-extent, and then *Stretch, only if
the above works* introduces them again as stretch work. An agent has to guess.
*Fixed:* the stretch section now offers the Circular-pattern **method** as optional and says the
slits themselves are not.

**6. A Ø0.9 detent bump is specified into a band 0.80 mm wide.** Found while sourcing the tooth
numbers. Run 2 sized its bump to span the band exactly — a Ø0.9 circle at r 5.05 covers
r 4.60 → 5.50. The band then moved to r 4.40 → 5.20 so the rim outboard would stay 0.61, and the
bump did not follow. Both changes are in the same commit, `a7eb8a7`; the arithmetic between them
was never redone. This is run 2's stale-number failure again — a driver moved and its dependents
did not.

*Fixed as a recomputation, not a reopened question.* Applying run 2's own rule to the moved band
gives **Ø0.8 centered at r 4.80**. Pitch there is 2π × 4.80 / 24 = 1.257, so the flat between
neighbors becomes **0.46 mm**, better than the 0.42 that was accepted. The brief said 0.42, which
was computed at the old band's center and is also stale.

**Nothing about the detent design was reopened.** The tooth count, the 15° step, the wave
profile and the choice of bumps over wedges were settled in conversation on 2026-08-11 — the
count is a multiple of 4 so detents land on ±90°, 28 misses, 32 is too fine to form. Checking the
session log before calling this open is what kept it a recomputation.

**7. The rim was measured from the wrong circle.** Found while drawing the band, which is the
point of drawing it. The rim is the material between the round end and the **valley ring**, and
the valleys reach 0.5 mm beyond the bump centres — not to the band's outer radius. Run 2's notes
say this plainly: Ø1.0 valleys at r 5.05 reach r 5.55, and 5.81 − 5.55 = **0.26**. The brief was
computing 5.81 − 5.20 = 0.61 off the band instead, and calling that the thinnest wall.

*Fixed as a recomputation.* At r 4.80 the valleys reach r 5.30, so the rim is **0.51 mm**. The
band still moved for the right reason and by the right amount; only the number quoted for the
result was wrong.

**This also closes the discrepancy the first pass left open.** `a7eb8a7` said the 5.50 outer left
"a 0.26 mm rim" against 5.81 − 5.50 = 0.31. Both are right about different circles: 0.31 to the
band, 0.26 to the valley ring, and 0.26 is the one that matters. Not unresolved.

**8. The brief told the agent to finish work run 2 had already done.** *"Unfinished from the first
build, and the first thing to do: the blade valley exists as a single cut and was never patterned
or mirrored."* True of run 1. Run 2 patterned and mirrored both and counted them by volume — 48
bumps, 48 valleys — and its feature tree has `Detent valleys x24` and `Detent valleys on other
face`. Its rendered blade shows the full ring. An agent following this would have started by
redoing finished work and might have doubled it.
*Fixed:* replaced with what run 2 did, pointing at the render.

**9. The valley's break was drawn on the wrong edge, and reversed.** Found by the user looking at
`brief-detent.png` — not by any check in this gate. The sheet put the break on the valley's
**floor** and left the rim square, which is backwards: the rim is the edge the dome rides out
over, and it is what `hinge.md` says to break. Worse, the floor corners were drawn as arcs that
widened the pocket as it deepened — an undercut, a shape no cutter can make and no printer can
bridge.

*Fixed:* the break moved to the rim, the floor left flat with sharp corners, and the sheet
re-rendered and looked at.

**Drawing the fix found the constraint behind it.** The land between neighboring valleys is
`pitch 1.257 − valley 1.0` = **0.26 mm**, so a break over **0.13 mm** merges the valleys into a
continuous groove and there is no detent left. The brief said the break amount was open and gave
no ceiling; it now gives one, and tells the agent to look at the face rather than trust the
fillet dialog. The sheet draws the break deliberately smaller than the limit.

**This is the third arc drawn with the wrong sweep on these sheets** — the detent dome and the
socket cavity were the first two, both caught by rendering and looking. The geometry groups carry
`scale(S, -S)`, which mirrors what the SVG sweep flag means, and reasoning about it has been
wrong every time it has been tried. Render and look; do not reason it out.

## How findings 1 to 4 were fixed

1. Source columns added to both briefs, with the untraceable numbers marked `proposed` and said
   to be untraceable: slits 0.8, tooth band, tooth depth, and — wrongly, see below — collar Ø9.4.
   `derived` was in use in `hand.md` but missing from the README's Source table; added.
2. Link depths corrected in `build-briefs/README.md`, and every label made to match its target
   across all three files.
3. Replaced with "Runs 1 and 2 built this joint. This text has not been built from since run 2
   corrected it, so the brief is what is under test, not the design."
4. Replaced with run 2's result and an instruction to take the measurement anyway, as a check on
   the agent's own model rather than on the design.

## Second pass

Source column present in all six briefs. Every link in the two launched briefs and the shared
README resolves, and every label matches its target. No occurrence of "Nobody has built",
"never tested" or "need to know today" remains in any brief. `ninja check`'s wrap and spelling
gates are clean.

## Not blocking

**`hinge.md`'s closing section is titled "What the first build proved"** and contains run 2's
findings as well as run 1's. Left alone: nothing in it is wrong, only the heading.

A label/target mismatch on `ball-and-socket.md`'s how-to link was found on the first pass and
fixed with the rest.

## Numbers re-traced to `robot-build-plan.md` as it stands today

Every `plan` number in both briefs matches its variable: `#ballD` 6, `#stalkD` 3, `#fit` 0.2,
`#grip` 1.35, `#limbD` 12, `#blade` 3, `#ear` 1.2.

Every derived number recomputed rather than taken from the brief:

| Brief says | Recomputed | |
| ---------- | ---------- | - |
| mouth 5.803 | 2 √(3.2² − 1.35²) = 5.802586 | agrees, and agrees with run 2's measurement |
| retention 0.197 | 6.000 − 5.803 = 0.197 | |
| cavity 109.48 mm³ | 137.258 − 27.776 = 109.482 | |
| fork span 6.0 | 3.0 + 2(0.3) + 2(1.2) = 6.0 | |
| blade width 11.62 | chord at ±1.5 on Ø12 = 11.619 | |
| ear inner chord 11.45 | chord at ±1.8 = 11.4473 | |
| ear outer chord 10.39 | chord at ±3.0 = 10.3923 | |
| rim 0.61 | 5.81 − 5.30 = 0.51 | the brief's 0.61 measured the band, not the valley ring — finding 7 |
| teeth 24 at 15° | 24 × 15 = 360 | closes, and 24 is a multiple of 4 |

No stale numbers found. This is the check that caught six errors in run 2.

**These numbers have no variable in the build plan.** Tracing them is what produced finding 6.

- The hinge's **0.3 gap** and **Ø2.2 × 1.0 pocket** were measured by run 2 — 0.300 each side, and
  0.100 radial clearance to the stub. Marked `built`.
- The **set-back 6.11** and the **stub Ø2.0 × 0.8** are recorded as what the built joint uses, in
  run 2's notes and in `robot-build-plan.md` respectively. Marked `built`.
- The socket's **0.8 slits** come from nowhere. They were built at that size in runs 1 and 2
  without being challenged, and run 2 explicitly did not measure whether 0.8 mm slits let the
  tabs flex. Marked `proposed`, and the briefs now say so rather than leaving it to be inferred.
- The socket's **collar Ø9.4** is derived, and this gate first said it was not. The
  `socket-in-context` study's FeatureScript computes the collar as `cavityR + WALL`, so Ø9.4 =
  2 × (3.2 + 1.5); it moves if `fit` or `ball` moves. What is proposed is the **1.5 mm wall** —
  three perimeters at a 0.4 mm nozzle, never measured under load. Reading the model settled in a
  minute what reading the prose had got backwards.
- The **tooth band** and **tooth depth** are likewise proposals, and the band is finding 6.

## Open questions checked against the session logs and memories

The limb-section conflict that stopped the first attempt is gone from `build-briefs/README.md`
and from both briefs. `#limbD` = 12 is stated as settled, and `hinge.md` derives its blade width
from it rather than restating it. No other question in either brief is one the logs have already
answered, except finding 4 above.

## What drawing the sheets found

The briefs now carry dimensioned sheets, generated by
`instructions/robot-guide/make_brief_sheets.py`. Drawing them found defects prose review had
passed over twice — the findings above say which ones came this way. Two more turned up in the
student-facing plan sheets, which were not in this gate's scope and were corrected anyway:

- **The plan-sheet generator still had the pre-run-2 band**, `TEETH_RI, TEETH_R = 4.6, 5.5`, and
  drew the teeth as radial wedges rather than round bumps. That sheet is **student-facing**, so a
  driver moved and a dependent that students read did not follow. Corrected, along with a mouth
  figure hardcoded as "83% of the ball" when it is 97%.
- **The plan sheet drew the fork as a rectangle inside the limb**, which is the exact thing every
  brief tells an agent not to do. Now clipped to the circle, so the drawing agrees with the rule.

Every number on the new sheets is imported from the plan generator, so a sheet cannot go stale
without the plan going stale with it. That is the mechanism these defects lacked.

## Not yet performed

Watchdog grace, output paths and agent-id recording are launch-time items. The reading-list
descriptions in `run3-launch.md` were checked when it was rewritten.

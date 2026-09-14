# 9. The hinge

Starts from a robot with a head and a foot. Ends with a Part Studio holding a blade and a fork
that click together.

**The second joint, and the same shape of tutorial as the ball and socket**: one studio, two
parts that mate to each other, a connector on each.

**Rewritten on 2026-09-09 to the joint draft9p1p6 built and Mike printed.** Everything this page
said before described bumps domed onto the blade dropping into valleys bored through the ear. That
joint was built, printed and measured; it held 210 N·mm where it was drawn for 454, because the
printer put supports in the valley holes and they could not be picked out. There are no holes in the
joint now except the bore. The reference is `stickbot-draft9p1p6`, read into
[`../../experiments/runs/2026-09-08-draft9p4/reference/`](../../experiments/runs/2026-09-08-draft9p4/reference/README.md),
and the specification is [`hinge.md`](../../experiments/build-briefs/hinge.md).

## What the joint is

**Both mating faces carry a ring of wedges.** Twenty-four on each face of the tongue and twenty-four
on each ear's inner face, all four rings on the same radii and the same 15 deg pitch. A detent is
one member's wedge sitting between two of the other's, so the joint clicks between positions and
holds a pose. The step is 15 deg and the backlash is 2.29 deg.

**A wedge is one sketched annular sector, extruded 0.75 mm with a 45 deg inward draft.** Nothing
else. The 45 deg is what lets both flanks print without support, and drafting rather than lofting is
what makes the crest come out right on its own.

**A wedge is wider than half a step and that is not a mistake.** 11.5127 deg against 7.5 deg. Both
members are drafted and they lean away from each other, so the fit is set half way up the gap and
not at either base plane. A wedge fitted at its own base plane leaves 12.61 deg of play, which is
most of a step, and the joint barely detents at all. The tutorial types `#wedge_w` as a rule, never
as a number, so this cannot be got wrong at the CAD.

**The two faces do not touch.** They stand `#gap` 0.90 mm apart, which is one wedge plus 0.15 mm of
air over its tip, and nothing bears except wedge on wedge.

**The two rings are phased a half step apart**, 7.5 deg, so the parts as drawn sit at a detent
rather than crest on crest. Phased together, every measurement comes out 0.60 mm off and it reads as
a fit problem.

**Assembly is a pinch, not a press.** Squeeze the two leaves toward each other until the axle clears
the ear's face, slide the tongue in, and let go. That is 75.2 N, against 182.7 N to push the same
joint together the old way. The joint is sized on the pinch.

## What moved since draft9p0's page

- **The slit is back, and it is what the blade springs on.** Up the middle of the tongue the whole
  way, 1.60 mm at the root opening to 7.00 mm at the tip, leaving two leaves that taper from
  4.20 mm at the root to 1.50 mm at the tip. draft9p0 took the slit out on the evidence of a joint
  whose spring was all in the ears. This joint is pinched, so the spring is in the leaves.
- **The slit cuts the axle rather than the axle bridging the slit.** Settled at draft9p1p2.
- **The bore is Ø4.1 mm, not Ø4.4 mm**, around a Ø4.0 mm axle standing 3.00 mm proud of each tongue
  face. 0.05 mm a side is inside one `#t_print`, so whether it comes out a clearance or an
  interference is a question about the printer and not about the drawing.
- **The ear is 6.10 mm, not 6.4 mm.** It is whatever the slot leaves, `(#limbD - #seat) / 2`, and
  no row records it: the number falls out of the sketch rather than driving it.
- **Every protrusion is no longer on the blade.** That rule protected the axle from the fork, and it
  is gone because both members carry wedges now. What it protected is still true by a wide margin:
  the bore's radius is 2.05 mm and the ring starts at 6.00 mm, so the fork's wedges clear the axle
  by 3.95 mm.
- **Nothing is domed and nothing is rounded.** draft9p0 domed each bump and rounded each valley rim.
  A drafted sector needs neither.

**The axle is added before the ear is bored.** The parts genuinely interfere between those two
features, so feature order is load-bearing here and the tutorial cannot reorder them for narrative.

**Every face of both parts is a slice of the Ø24 mm limb.** No rectangular paddle drawn inside the
circle and cut off at some width. A rectangle in a circle has corners and the corners bind before
the faces do.

## The rows this tutorial adds to `robot sizes`

Twelve, and they are the last of the twenty-three.
[`00-manifest.md`](00-manifest.md) has which tutorial types which.

| Row | Expression | At the robot's size | typed at |
| --- | ---------- | ------------------- | -------- |
| `#blade` | `10 mm` | 10 mm | `blade.section_variables` |
| `#wedge_h` | `0.75 mm` | 0.75 mm | `blade.section_variables` |
| `#wedge_c` | `0.15 mm` | 0.15 mm | `blade.section_variables` |
| `#gap` | `#wedge_h + #wedge_c` | 0.90 mm | `blade.section_variables` |
| `#seat` | `#blade + 2 * #gap` | 11.80 mm | `blade.section_variables` |
| `#blade_out` | `32 mm` | 32 mm | `blade.section_variables` |
| `#tab_free` | `#blade_out - #limbD / 2` | 20 mm | `blade.section_variables` |
| `#flat` | `sqrt((#limbD / 2) ^ 2 - (#seat / 2) ^ 2)` | 10.4494 mm | `blade.section_variables` |
| `#t_print` | `0.10 mm` | 0.10 mm | `blade.wedge_variables` |
| `#limbCenter` | `#torsoH / 2` | 48 mm | `blade.arm_variables` |
| `#slot_deep` | `#blade_out + 1 mm` | 33 mm | `fork.blank_variables` |
| `#ear_free` | `#slot_deep - #limbD / 2` | 21 mm | `fork.arm_variables` |

**Eight of the twelve arrive at the first sketch, and the geometry is why.** `blade profile` is a
slice of the Ø24 mm limb, what the slice leaves is `#flat`, and `#flat` is written from `#seat`,
which is written from `#gap`, which is written from `#wedge_h` and `#wedge_c`. The chain cannot be
typed out of order and the first sketch is where it bottoms out, so the page introduces the eight as
one idea — *this is the limb's cross-section* — rather than as a table to copy.

**`#limbCenter` moves here from tutorial 1.** `#rod_blade` is the first thing in the robot to read
it, and it sat in the studio unread through eight tutorials before this one.

**The other four wait for the feature that asks for them.** `#t_print` is read only by
`#wedge_eps`, which is a wedge-ring number; `#slot_deep` is the depth `fork blank` cuts to; and
`#ear_free` is a term in `#rod_fork`, which the fork's arm reads.

**They are studio rows and not the tab's because both limbs read them.** `u limb` builds its rod to
`#limbCenter - #collar - #ear_free` and `l limb` to `#limbCenter - #stand - #tab_free`, and the
`hinge` tab's own rows are invisible to them.

**`#t_print` is a printing number, like `#fit`.** It is how far one printed surface lands off where
it was drawn, per surface, so a clearance is checked against twice it. `#wedge_eps` is the only row
that reads it.

**`#slot_deep` types a millimeter inside a rule.** The slot is cut one millimeter past where the
tongue reaches, so the tongue never bottoms in it. That millimeter is a choice and it stays visible
rather than being folded into `#blade_out`.

## The tab's variables

Sixteen rows. Five carry a number and eleven carry a rule, and each goes in at the feature that
first reads it rather than all of them ahead of the geometry.

| Row | What it is | typed at |
| --- | ---------- | -------- |
| `#nose` | `#limbD / 2`, the round end on both parts, about the pin | `blade.section_variables` |
| `#stub` | 4 mm, the axle | `blade.axle_variables` |
| `#stub_proud` | `2 * #wedge_h + 1.50 mm`, off each tongue face | `blade.axle_variables` |
| `#wedges` | 24 | `blade.wedge_variables` |
| `#ring_in` | 6.00 mm | `blade.wedge_variables` |
| `#ring_out` | `#flat`, so a wedge runs out to the limb's cut | `blade.wedge_variables` |
| `#wedge_bind` | `#ring_out - #gap / 2`, half way up the gap, where the fit is set | `blade.wedge_variables` |
| `#wedge_inset` | `2 * asin(#gap / 2 / #wedge_bind)`, the two drafts' lean together | `blade.wedge_variables` |
| `#wedge_eps` | `2 * #t_print / #wedge_bind * 1 rad`, the room a flank needs there | `blade.wedge_variables` |
| `#wedge_w` | `180 deg / #wedges + #wedge_inset - #wedge_eps` | `blade.wedge_variables` |
| `#rod_blade` | `#limbCenter - #stand - #tab_free` | `blade.arm_variables` |
| `#leaf_root` | 4.20 mm | `blade.slit_variables` |
| `#leaf_tip` | 1.50 mm | `blade.slit_variables` |
| `#slit_h` | `#blade - 2 * #leaf_root`, the slit at its root | `blade.slit_variables` |
| `#bore_d` | `#stub + 0.1 mm`, through each ear | `fork.pocket_variable` |
| `#rod_fork` | `#limbCenter - #collar - #ear_free` | `fork.arm_variables` |

`#wedge_eps` ends in `* 1 rad` because the term in front of it is a ratio and the row is an angle.

**Seven of the sixteen are the wedge ring and they go in together.** `#wedge_w` is written from
`#wedges`, `#wedge_inset` and `#wedge_eps`; those are written from `#wedge_bind`, which is written
from `#ring_out`. `blade wedge outline` is the sketch that reads the end of the chain, and one
sector drawn from eight numbers is a shorter explanation than eight numbers drawn from nothing.

**`#ear` and `#backlash` are dropped, because nothing read them.** draft9p1p6 carries both:
`#ear` recorded what the slot leaves and `#backlash` the play the ring ends up with. Walking every
expression in `hinge.features.json` finds no feature and no other row naming either one, so neither
drives anything and a reader typing them gets no geometry for the work. Both numbers are still in
the page as numbers — the ear comes out 6.10 mm and the ring's play is `2 * #wedge_eps` — and
neither is a row any more. Settled on 2026-09-11 by Mike.

## The steps

Forty-four features in tree order: the blade, then the fork, then the two connectors, with each
variable going in directly above the feature that reads it. draft9p1p6 built forty-six, all
eighteen of its rows first and ahead of any geometry; this draft types sixteen and does not, and
[`00-manifest.md`](00-manifest.md) § *A variable is typed at the step that first reads it* is why.

### The blade

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.hinge.tab` | a Part Studio called `hinge` | |
| `cad.parts.hinge.blade.section_variables` | the limb's cross-section: `#blade`, `#wedge_h`, `#wedge_c`, `#gap`, `#seat`, `#blade_out`, `#tab_free` and `#flat` in `robot sizes`, then `#nose` in the tab | nine variables |
| `cad.parts.hinge.blade.profile_sketch` | the blade's round end | `blade profile` |
| `cad.parts.hinge.blade.blank` | extrude it `#blade` | `blade blank` |
| `cad.parts.hinge.blade.axle_variables` | `#stub` and `#stub_proud` in the tab | two variables |
| `cad.parts.hinge.blade.axle_sketch` | the stub axle | `stub axle outline` |
| `cad.parts.hinge.blade.axle` | extrude it `#stub_proud` | `stub axle` |
| `cad.parts.hinge.blade.wedge_variables` | `#t_print` in `robot sizes`, then the ring's seven in the tab | eight variables |
| `cad.parts.hinge.blade.wedge_sketch` | one annular sector | `blade wedge outline` |
| `cad.parts.hinge.blade.wedge` | extrude it 0.75 mm with a 45 deg inward draft | `blade wedge` |
| `cad.parts.hinge.blade.pattern_axis` | the axis both patterns turn about | `axis for circular patterns` |
| `cad.parts.hinge.blade.wedges` | 24 of them | `blade wedges` |
| `cad.parts.hinge.blade.mirror` | the same ring on the other face | `mirror blade` |
| `cad.parts.hinge.blade.arm_variables` | `#limbCenter` in `robot sizes`, then `#rod_blade` in the tab | two variables |
| `cad.parts.hinge.blade.arm_sketch` | the arm back to the limb | `blade rod outline` |
| `cad.parts.hinge.blade.arm` | extrude it `#rod_blade` | `blade arm` |
| `cad.parts.hinge.blade.slit_variables` | `#leaf_root`, `#leaf_tip` and `#slit_h` in the tab | three variables |
| `cad.parts.hinge.blade.slit_sketch` | the slit up the middle | `relief slit outline` |
| `cad.parts.hinge.blade.slit` | cut it, through the axle | `relief slit` |

**The pattern axis is a mate connector, and it comes before the first pattern.** Both rings turn
about it, on both parts, and it is the one axis in the studio a pattern will take.

**The slit is cut last on the blade**, after the wedges and after the arm, so that it cuts the axle
and both leaves in one feature.

### The fork

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.hinge.fork.profile_sketch` | the fork's outline | `fork outline` |
| `cad.parts.hinge.fork.blank_variable` | `#slot_deep` in `robot sizes` | `#slot_deep` |
| `cad.parts.hinge.fork.blank` | extrude it `#slot_deep` | `fork blank` |
| `cad.parts.hinge.fork.trim_sketch` | where the fork clears the blade's arm | `fork blade top cut outline` |
| `cad.parts.hinge.fork.trim` | cut it | `trim fork to arm` |
| `cad.parts.hinge.fork.pocket_variable` | `#bore_d` in the tab | `#bore_d` |
| `cad.parts.hinge.fork.pocket_sketch` | the bore | `pocket axle sketch` |
| `cad.parts.hinge.fork.pocket` | cut it through the ear | `pocket axle on fork` |
| `cad.parts.hinge.fork.wedge_sketch` | one annular sector, phased a half step off the blade's | `ear wedge outline` |
| `cad.parts.hinge.fork.wedge` | extrude it 0.75 mm with a 45 deg inward draft | `ear wedge` |
| `cad.parts.hinge.fork.wedges` | 24 of them, about the blade's axis | `ear wedges` |
| `cad.parts.hinge.fork.mirror` | the second ear | `two forks` |
| `cad.parts.hinge.fork.arm_variables` | `#ear_free` in `robot sizes`, then `#rod_fork` in the tab | two variables |
| `cad.parts.hinge.fork.arm_sketch` | the arm back to the limb | `fork arm outline` |
| `cad.parts.hinge.fork.arm` | extrude it `#rod_fork` | `fork arm` |
| `cad.parts.hinge.fork.combine` | union the fork's pieces | `combine fork parts` |
| `cad.parts.hinge.rename` | call the two parts `blade` and `fork` | |

**The two parts are named `fork` and `blade` in the parts list.** draft9p3 left them `Part 1` and
`Part 2` and the page had to be fixed afterwards.

### The connectors

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.hinge.fork.connector` | the fork's mate connector | `fork to robot` |
| `cad.parts.hinge.blade.connector` | the blade's mate connector | `blade to robot` |

**Both connectors are placed by the same rule**, on the member's own rod end face, on its axis.
draft9p3 placed them two different ways and one of them came out off the axis and short.

## The shots this tutorial needs by name

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| two heroes | the blade and the fork, apart | `req.page.hero` |
| one more hero, clicked together | the only frame that says what the joint is for | |
| the part list, both named | | |
| one wedge, close-up before the pattern | at 24 it is a texture; at one it is a shape | |
| the draft field, and the wedge in preview | 45 deg is the whole reason the crest looks as it does | |
| the pattern's axis, picked, medium and close-up with a ring | a circular pattern about the wrong axis is a silent disaster | `req.shot.two_frame` |
| the count field, and the result | 24 is a number worth seeing chosen | |
| a section through the axle and the bore | the stub, the bore and the 2.10 mm of engagement are all inside the part | |
| the two rings meshed, close-up | the detent, which is the entire point of the joint | |
| the slit, before and after it cuts the axle | | |
| each connector's origin, medium and close-up with a ring | | `req.shot.two_frame` |
| the tree, the version dialog | | |

**The meshed-rings shot is the one to fight for.** Everything else in this tutorial is a shape; one
member's wedge sitting between two of the other's is the mechanism, and it is the reason the ear is
6.10 mm and the leaves taper.

## What we do not know yet

**Whether the two parts can be shown clicked together in the Part Studio at all**, or whether that
frame has to wait for the assembly. They are built in place at a detent, so they may already be in
the right relationship, in which case the hero is free.

**How many of the 24 wedges need to be visible for the ring to read.** A frame too close shows a
wedge and no ring; too far shows a texture and no wedge.

**Whether the crest photographs.** Inboard of r 7.478 mm the wedge is a ridge rather than a table,
and the two flanks meet before they reach 0.75 mm. That is drawn on purpose and it is the thing a
reader is most likely to think is a mistake, so it needs a frame that shows it as a shape.

**Whether the mirrors need their planes shown.** Two mirrors in this tutorial, and a mirror about
the wrong plane produces something that looks nearly right.

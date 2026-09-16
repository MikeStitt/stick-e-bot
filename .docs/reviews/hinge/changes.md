# Changes Mike wants to the hinge review

Running notes, taken while Mike reads `index.rst`. His words are the record; anything I add is
marked *(mine)*. Nothing here has been applied to `index.rst`, the figures, `make_plans.py` or
the CAD.

## Subtract

### One Part Studio holding two parts is not a problem

> "It is good that the hinge is a part studio that makes two parts. the two sides of the hinge
> work together and are designed from each other, putting them in one part studio defines that
> relationship and allows one to be easily made from the other. Being two parts in one studio is
> not a problem."

*(mine)* Where this lands in the review: the section *Both parts are still called Part 1 and Part 2*
(line 215) is about the two default names, not about the studio holding two parts, so the finding
itself survives. What has to change is anything that reads as if the arrangement were the
complaint, and the section should say plainly that one studio holding both halves is the right
arrangement and why — the two sides are designed from each other.


### A heading under this title reads as a charge, even when it reports good news

> "Reading your **bolded** text: 'What is wrong with the hinge' and 'Both documents hold the same
> joint' implies a claim that this is wrong."

*(mine)* The two documents agreeing is the good outcome, and the section's own body says so — it is
there to scope the review, not to accuse. The title makes every ``==`` heading beneath it read as an
item in the charge sheet, so a section that reports a fact or good news has to say that in the
heading itself, or the document needs a structure that separates what is wrong from what was
checked and found sound.

The same problem, not yet raised by Mike: *But the limb's rod buries the excess, so the printed
joint is right* (line 73) is also a not-wrong finding, and its heading opens with "But", which reads
as a continuation of the charge rather than a correction of it.

## Add

### The ear's valleys break out through the side of the fork

> "The ear valleys extend past the outside of the fork, we need to either have the valleys go all
> the way through the fork, or provide 1mm of thickness margin at outside of the fork so that the
> outside of the fork has a minimum thickness."

*(mine)* Checked against the numbers. The ear is a slice of the Ø``LIMB`` 24 cylinder, so it is
``EAR`` 6.4 thick only on the limb's axis and thins to nothing at the flank: at ``y`` from that axis
it is ``sqrt(12**2 - y**2) - SLOT/2``. The detent band sits at ``BUMP_R`` 9.60 with ``VALLEY_D`` 2.0
holes ``VALLEY_DEEP`` 0.90 deep, so a valley's outer edge reaches ``y`` 10.6, where the ear is
**0.025 mm** thick. It is not close: the hole is out through the flank.

| tooth | valley's outer edge | ear there | left under the valley |
| --- | --- | --- | --- |
| 0 deg | 10.600 | 0.025 | -0.875 |
| 15 deg | 10.273 | 0.602 | -0.298 |
| 30 deg | 9.314 | 1.967 | +1.067 |

``STEP`` is 15 deg, so 24 teeth, and six of them break out: 0, 15, 165, 180, 195 and 345 deg. The
two on the axis are the worst.

What each of Mike's two options costs, as far as arithmetic can say:

- **Through.** The valley becomes a hole, and at those six teeth it opens as a scallop in the limb's
  outside surface, not a round hole. The detent still works; the flank stops being smooth.
- **A 1 mm floor.** A valley may then reach out to ``y`` 9.367, so ``BUMP_R`` has to come in from
  9.60 to **8.367 or less**, and the band from 8.80 .. 10.40 to about 7.57 .. 9.17. The bore is
  R 2.2, so the band's inner edge cannot go below 3.20 without cutting into it; there is room. A
  smaller ``BUMP_R`` is a shorter lever arm, so the same bump gives less holding torque.

This also touches ``detail_hinge``'s right-hand view, which draws the band square on and would show
the break-out if it drew the ear's outline; it draws only the chord.

### The blade's bottom connector is not on the bottom of the blade

> "The mate connector for the bottom of the bade is not on the bottom of the blade."

*(mine)* Already on the page, as *draft9p3's blade connector landed on the tongue's root step*
(line 200), and open as task #142. Mike raising it independently is a confirmation, not a new
finding, so it needs no new section. The measurements it rests on: ``stickbot-draft9p1p1`` puts
``blade to robot connector`` at ``(0, 0, -26.4)``, on the blade's end face and on the limb axis;
``stickbot-draft9p3`` puts it at ``(0, -7.884, -20)``, the centroid of the step where the tongue
meets its own limb, 7.884 off the axis and 6.4 short of the end face.

What the review does not yet say, and Mike's wording points at: the connector is *named* for the
bottom of the blade, so the name and the place disagree, and that is what makes it a defect rather
than a choice. The section calls it a build defect belonging to draft9p3 alone; that still holds.

Sharpened by Mike:

> "The blade to robot connector is not in the center of the bottom of the blade."

*(mine)* So it is two independent errors, not one, and the fix has to name both: it is on the wrong
face, and it is not centered on the face it is on. Moving it to the end face without saying
*centered* would leave the second one. Its ``y`` of -7.884 is the centroid of the step face, whose
box is ``[-10.909, -12, -20] .. [10.909, -5, -20]`` — a segment of the Ø24 circle, not a full disc,
so its centroid is off the axis. That is the same failure as task #118, where ``socket connect to
robot`` inferred CENTROID where CENTER was wanted; picking a face and letting Onshape infer the
point is what produces it both times.

### The fork's connector is not on the top of the fork either

> "The fork to robot connector is not on the top of the fork, and not centered on the top of the
> fork."

*(mine)* The height half is measured and on the page already, as *The two robot connectors are
placed by two different rules* (line 176) and task #141: ``fork to robot connector`` reads back at
``(0, 0, 12)`` in both documents, which is ``NOSE`` from the pin and 15.4 mm short of the fork's own
end face at ``z`` +27.4, so it sits inside the material.

The centering half does not match what I measured, and I would rather say so than write it down
wrong. At ``(0, 0, 12)`` it is on the limb axis, so it is centered across the fork; what it is not
is at the center *of the top face*, which is ``(0, 0, 27.4)``. Read that way Mike's sentence is
exactly right and both halves are the same fault: the connector belongs at the top face's center
point and is 15.4 mm below it. If instead he is seeing it off the axis in the GUI, then the
read-back and the screen disagree and that is a third thing to chase.

Either way the two connector findings now pair up: the blade's is on the wrong face and off center,
the fork's is on no face at all. The review currently frames the fork's as a *consistency* problem
between two halves; Mike is framing it as each connector being in the wrong place on its own terms,
which is the stronger and simpler statement.

### New requirement: a bump's edge stands 1 mm clear of the blade's edge

> "The bumps are wrong per a new requirement. Let's require the edge of the bumps to be at least
> 1mm from the edge of the blade."

*(mine)* This is a requirement Mike is adding, not a mistake being found, and the hinge fails it as
built. The blade's toothed face is the Ø``LIMB`` circle cut at ``BLADE/2`` off the limb axis, so its
edge stands ``sqrt(12**2 - 5**2)`` = **10.909** from the pin, the same all the way round and down
the straight sides. A bump's outer edge is ``BUMP_R + BUMP_D/2`` = **10.400**, which leaves
**0.509 mm**. The requirement wants 1.0.

The band's outer radius is what the requirement names, and ``TEETH_R`` is exactly that number, so
the requirement reads ``TEETH_R <= 9.909``. Ways to reach it: bring the band in, make the bump
smaller, or both.

This one and the valley one are the same band seen from its two sides, so they have to be settled
together:

| requirement | what it allows |
| --- | --- |
| bump edge 1 mm inside the blade's edge | ``BUMP_R`` up to 9.109 |
| 1 mm of ear left under a valley | ``BUMP_R`` up to 8.367 |

The fork binds. At ``BUMP_R`` 8.367 the blade margin is 1.741 and the ear under a valley is 1.900,
so both hold with room, and the band becomes about 7.57 .. 9.17 against today's 8.80 .. 10.40. The
price is the lever arm: 87% of today's, so the same bump holds about 13% less angle for the same
force. If the valleys go through instead, the fork's limit disappears and only the blade's 9.109
binds.

*(mine)* Worth Mike knowing: the valley is ``VALLEY_D`` 2.0 where the bump is ``BUMP_D`` 1.6, so the
valley overhangs the bump by 0.2 a side. Every clearance above is figured on the valley where the
fork is concerned and on the bump where the blade is, which is why the two limits differ by more
than the ear's curvature alone explains.

### The round on the ear valley's rim comes out

> "Let's remove the round on the ear valley rim as too small to print."

*(mine)* The feature is ``round ear valley rim``, a Fillet whose radius is ``#rim_break`` = **0.1
mm**. That is under one layer and well under an extrusion width, so no nozzle forms it; the slicer
either drops it or renders it as the sharp edge it was meant to replace. Nothing is lost by deleting
a feature that never reached the plastic.

What the brief claims it was for, and whether that survives: it argued two sharp edges cannot cam,
so the bump's crown was filleted r0.8 — a full hemisphere on a Ø1.6 bump — **and** the valley's rim
broken. With the bump already a dome, only one of the two edges is sharp, and a dome riding a sharp
rim still ramps. The rim break was the smaller half of that pair and the half that cannot be
printed. It also had a hard ceiling of 0.25 mm before neighboring valleys merge into a groove, so
there was never room to make it printable by growing it.

What removing it touches, so nothing is left dangling:

- the hinge tab loses one feature, and ``24 ear valleys`` then patterns the cut alone
- ``#rim_break`` becomes an unused row in ``robot sizes``
- ``instructions/stickbot-draft9p3/source/hinge.rst`` loses the step *Break the dimple's rim* and
  its seven frames, and the pattern step stops saying to click the round as well
- the same step exists in the draft9p0 and draft9p2 pages, which are archival and stay as they are
- ``.docs/experiments/build-briefs/hinge.md`` loses the rim-break argument, the 0.25 ceiling
  arithmetic, and the open question *"how much rim break the valley actually needs"*

If the valleys go all the way through instead, this decides itself: a through hole has a rim on
each face and neither would be broken.

### New requirement: a valley's edge stands 1 mm inside the fork's edge

> "lets require the valley edge to at least 1mm from the fork edge so that there is material to
> build the edge of the fork at 0.4mm nozzle."

*(mine)* The ear's inner face is bounded two ways: by the ``NOSE`` round at r 12 about the pin, and
by the limb's own flanks, which cross that face at **10.613** off the limb axis. The valley ring
reaches r 10.600. So against the round there is 1.400 to spare, and against the flank there is
**0.013 mm**. The two teeth on the flank axis are the ones that fail, which is the same six teeth as
the break-out note above. At a 0.4 mm nozzle 1.0 mm is 2.5 extrusion widths, so the rule buys a
perimeter each side and something between them.

This reads as the in-plane version of the margin Mike asked for earlier, and the two are not the
same number:

| how the 1 mm is measured | allows |
| --- | --- |
| in plane, valley edge to the fork's edge | ``BUMP_R`` up to 8.613 |
| through the wall, valley floor to the outside | ``BUMP_R`` up to 8.367 |

At 8.613 the wall under the valley floor comes out 0.682, so the in-plane rule on its own does not
deliver a millimeter of material; at 8.367 both hold, the in-plane margin being 1.246. **Question
for Mike:** whether the earlier through-thickness margin still stands alongside this one. If it
does, 8.367 is the number and it also satisfies the blade's 9.109; if this in-plane rule replaces
it, the number is 8.613 and the wall under a valley is two-thirds of a millimeter.

Either way the band moves in and the lever arm goes to 87% or 90% of today's.

### Decided: the valleys go all the way through the fork

> "Lets decide to make the valleys go all the way through the fork so that they can be visually
> inspected from the outside and manually cleared out for small printing defects."

*(mine)* This settles the branch Mike opened at the top of these notes, and it retires the
through-thickness margin: there is no wall under a valley to keep, so the 8.367 figure is off the
table and the **in-plane 1 mm from the fork's edge, ``BUMP_R`` <= 8.613, is the rule that stands**.
The two decisions need each other. A through hole at today's 9.60 would not exit as a hole at the
six teeth near the flank; it would tear the flank open into a scallop. Moved in to 8.613, every one
of them is a clean round hole with a millimeter of face around it, which is what makes it
inspectable.

What else follows:

- ``VALLEY_DEEP`` stops being a dimension and joins ``#rim_break`` as a row with nothing left to do
- the bump can no longer bottom in its valley, so the 0.30 mm of clearance the brief works out
  between the crest tip at 6.20 and the valley floor at 6.50 stops being a number anyone has to
  keep. The bump is held by its side against the hole's bore, which is what was carrying it anyway
- the fork gains 48 holes through its flanks, two rows of 24, which is the inspection Mike wants and
  also the first thing anyone will notice about how the robot looks
- each hole breaks out obliquely, because the outer surface is the limb's curve and the hole's axis
  is the pin's; the exit is a slanted oval, not a circle
- the ear is the spring, and these holes are inside its bending span, so ``EAR_I`` and ``EAR_Z``
  computed by ``_seg`` over a solid slice are now optimistic. Given the ear is at 157 MPa on paper,
  losing stiffness here is help, not harm, but the calculation no longer describes the part

**And a collision that has to be settled with it.** Holding Ø2.0 valleys at ``STEP`` 15 deg, the
land between one valley and the next is ``2 r sin 7.5 - 2.0``. At today's 9.60 that is 0.506, thin
already. At 8.613 it is **0.248**, under one 0.4 mm extrusion, so the material between neighboring
holes cannot be printed either. The two rules cannot both hold at 24 teeth of Ø2.0:

| valley | teeth | radius the land needs | radius the edge rule allows |
| --- | --- | --- | --- |
| 2.0 at 15 deg | 24 | >= 9.194 | <= 8.613 |
| 2.0 at 20 deg | 18 | >= 6.911 | <= 8.613 |
| 1.6 at 15 deg | 24 | >= 7.661 | <= 8.813 |
| 1.2 at 15 deg | 24 | >= 6.129 | <= 9.013 |

So either the teeth get coarser or the bumps get smaller. **This one is Mike's**, and it is a feel
decision as much as an arithmetic one: 18 teeth at 20 deg keeps the bump's size and the detent's
strength and gives the joint 20 deg of angular resolution instead of 15; a Ø1.6 valley over a Ø1.2
bump keeps 24 teeth and 15 deg but makes every click smaller.

### If the valleys shrink instead of the teeth thinning out

> "I think per the initial list of problems we can make the valleys smaller. What happens then?"

*(mine)* It works, and it works better than coarsening the pitch, because everything downstream of
the valley is tied to it by a rule already: ``VALLEY_D`` is the bump plus 0.4 of radial clearance,
``BUMP_D`` is the band's width, and the crown fillet is ``BUMP_D/2``, a hemisphere. Shrink the
valley and all four follow. The band also moves back out a little, because the in-plane cap is
``9.613 - VALLEY_D/2``, so a narrower valley buys back some lever arm.

At 24 teeth and 15 deg, with each row at its largest allowed radius:

| valley | bump | ``BUMP_R`` | land | land in 0.4 nozzles | dome r | dome in 0.2 layers | lever |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.0 | 1.6 | 8.613 | 0.248 | 0.6 | 0.80 | 4.0 | 90% |
| 1.8 | 1.4 | 8.713 | 0.475 | 1.2 | 0.70 | 3.5 | 91% |
| 1.6 | 1.2 | 8.813 | 0.701 | 1.8 | 0.60 | 3.0 | 92% |
| 1.5 | 1.1 | 8.863 | 0.814 | 2.0 | 0.55 | 2.8 | 92% |
| 1.4 | 1.0 | 8.913 | 0.927 | 2.3 | 0.50 | 2.5 | 93% |
| 1.2 | 0.8 | 9.013 | 1.153 | 2.9 | 0.40 | 2.0 | 94% |

The largest valley that leaves one 0.4 mm land is **1.866**; the largest that leaves two perimeters,
0.8 mm, is **1.512**. So Ø1.5 is the round number that gives the land two passes to build with, and
Ø1.6 is the round number that gives it nearly two.

What does not improve, and is the reason to stop shrinking: the bump has to print as a dome, and its
dome is only ``BUMP_D/2`` tall. At Ø1.6 that is four layers at 0.2, which is a dome. At Ø1.2 it is
three, which is a coarse one. At Ø0.8 it is two, which is a cone with a flat on it, and the whole
argument for filleting the crown — that a dome cams where a square edge scrapes — is gone. **Ø1.2 is
the floor and Ø1.5 or Ø1.6 is the room.**

Three things a smaller valley does **not** fix, so they stay on the list:

- the interference is ``TOOTH_PROUD`` 1.2 against the ear's land at 5.60, which is **0.60 per side**
  whatever the bump's width. The ear gives that on every click, so the click force follows the ear's
  stiffness, not the bump's size. At ``EAR_FREE`` 12 that is around 117 kgf, on the same footing as
  the 195 kgf to press the axle home
- a narrower bump carries the same 0.60 on less contact, so the pressure on it goes up and it is
  likelier to flatten or shear over time
- the dome gets shallower relative to its height, which makes the ramp out of the valley steeper and
  the click sharper and harder rather than crisper

So shrinking the valley settles the printing of the fork's face, and settles it well. It leaves the
snap force exactly where the review left it.

### What narrowing the blade buys, and what it charges for it

> "Let's also look at what a reasonable narrowing of the blade would be to get us a little more
> external margin for a bigger BUMP_R."

*(mine)* It does buy room, and less than one might hope, and it charges for it in the one currency
the joint is already overdrawn in. ``BLADE`` sets ``SLOT`` = blade + 2 ``GAP`` and ``EAR`` =
whatever
the slot leaves of the Ø24. Narrow the blade and the ear's inner face moves outward, so the flank it
has to stay clear of moves outward with it. Rows below hold ``VALLEY_D`` at 1.6 and take the largest
radius the 1 mm rule allows:

| blade | ear | flank | ``BUMP_R`` cap | land | lever | ear I | press force |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10.0 | 6.40 | 10.613 | 8.813 | 0.701 | 92% | 275 | 195 kgf |
| 9.0 | 6.90 | 10.862 | 9.062 | 0.766 | 94% | 356 | 252 kgf |
| 8.0 | 7.40 | 11.083 | 9.283 | 0.823 | 97% | 451 | 319 kgf |
| 7.0 | 7.90 | 11.278 | 9.478 | 0.874 | 99% | 563 | 399 kgf |
| 6.0 | 8.40 | 11.447 | 9.647 | 0.918 | 100% | 693 | 490 kgf |

Reading it: taking the blade from 10 to 8 is a 2 mm cut that returns **0.47 mm** of band radius, and
the return falls off as it goes, because the flank is a circle and it flattens as it comes round.
Meanwhile the ear thickens by the same 2 mm, and the ear is the spring. Its second moment goes up
64%, and so does everything figured from it: the press force at ``EAR_FREE`` 12 goes from 195 kgf to
319. Narrowing the blade to help the band makes the joint's worst number worse, faster than it makes
the band's number better.

Two things that do not move, which is worth knowing before trading anything for them:

- the detent interference is ``TOOTH_PROUD`` 1.2 against the ear's land, which works out at
  **0.60 per side at every blade width in the table**. The blade's width cancels
- ``MOVE`` is ``STUB_PROUD`` - ``GAP`` = 1.0 at every width too

So the honest answer to "what is a reasonable narrowing": **none of it is reasonable for this
purpose.** ``BLADE`` 9 is the only row that could be called cheap, and it buys 0.25 mm of radius for
a 29% stiffer ear. Shrinking the valley gets the same room for nothing — Ø2.0 to Ø1.6 moved the cap
from 8.613 to 8.813 with the blade untouched, which is 0.2 of the 0.25 that costing 1 mm of blade
would have bought.

If the blade ever does narrow, let it be for its own reasons — the ear being too thin to print
beside a through hole, say — and not to feed the band.

### Blade 9 with a 1 mm slit, and the axle 0.8 proud

> "Let's look at 9mm blade with a 1mm slot in the middle (your old design) to remove stiffness of
> the joint. Let's also make the stub axle 0.8mm proud. How does the stiffness and insertion force
> look then?"

*(mine)* It is the first combination that gets the joint into a range a person could press. Both
halves earn their keep, and they earn it in different ways.

**The slit.** ``BLADE`` 9 with a 1.0 slit leaves two tabs 4.00 across, and an ear 6.90. The ear and
the tab are then springs in series: same force, movement splitting inverse to stiffness. Ear
1235 N/mm, tab 431 N/mm, series **319 N/mm**, against today's solid **955 N/mm**. The slit is worth
**3.0x**, and the softer member does most of the giving: of any move, the tab takes 74% and the ear
26%. Assumed and worth Mike confirming: the tab's free length is 12, the same as the ear's, which is
what a slit running the tongue's full length gives. That number is cubed, so it matters more than
anything else on this page.

**The axle.** ``STUB_PROUD`` 0.8 against ``GAP`` 0.6 leaves ``MOVE`` 0.2, a fifth of today's. Force
is linear in it, so the two changes multiply: **3.0 x 5 = 15x**.

Together, at ``EAR_FREE`` 12:

| | today | proposed |
| --- | --- | --- |
| spring | solid ear, 955 N/mm | ear + tab in series, 319 N/mm |
| ``MOVE`` | 1.00 | 0.20 |
| force to press, both sides | **194.78 kgf** | **13.02 kgf** |
| stress at that force | ear 157.1 MPa | ear 8.7, tab 12.5 MPa |
| against PETG's 50 | 3.1x over | comfortably under |

The stress answer is the one that changes character rather than degree. Today the estimate says the
ear yields on assembly. At 13 kgf nothing in the joint is near yield, so the cantilever arithmetic
stops being a warning and starts being a design.

**The catch, and it is a real one.** ``MOVE`` and the axle's engagement are the same number:
the axle crosses ``GAP`` and whatever is left over is both what the ear has to give and how far the
axle sits in the bore. So this is the whole ladder:

| ``STUB_PROUD`` | engagement | force to press | ear / tab |
| --- | --- | --- | --- |
| 1.6 | 1.00 | 65.1 kgf | 43.7 / 62.5 MPa |
| 1.2 | 0.60 | 39.1 kgf | 26.2 / 37.5 MPa |
| 1.0 | 0.40 | 26.0 kgf | 17.5 / 25.0 MPa |
| 0.8 | 0.20 | 13.0 kgf | 8.7 / 12.5 MPa |

The review already said the axle holds the arm on by one millimeter and called that thin. At 0.8
proud it holds it on by **0.2 mm**, which is half a layer. The slit is free money; the last four
rows of that ladder are all paid for in retention.

**One thing none of these numbers is.** Every force above is the *normal* force to spread the ear,
not the push a child feels. The two differ by the lead-in: the axle is a plain cylinder with a
square edge, so its ramp angle is 90 degrees and no axial push converts into spread at all. Give the
axle's outer edge a 30 degree chamfer and the axial force lands near 1.06x the normal force in
PETG, so 13 kgf normal is about 14 kgf to push. **Chamfering the axle may be worth more than any
number in this section**, because it is what turns the joint from one that cannot be pressed at any
force into one that presses at the force the spring says.

*(mine, and for Mike)* If retention at 0.2 mm is too little, the pair that keeps both ends is
``STUB_PROUD`` 1.2 with the slit and a chamfered axle: 0.60 of engagement, 39 kgf normal, both
members under 40 MPa. And the detent rides the same spring, so its click is
``(TOOTH_PROUD - GAP) x 319`` — at ``TOOTH_PROUD`` 1.2 that is 39 kgf a click, which wants looking
at in its own right.

### Sizing the joint for a 2 kgf press

> "Let's try to get the insertion press force to 2kg. What do you recommend for axle stub height,
> blade width, and blade slit width?"

*(mine)* **Recommended: ``BLADE`` 10 unchanged, slit 7.6, leaving two leaves 1.20 across, and
``STUB_PROUD`` 1.5.** That gives **2.02 kgf** to press, with **0.9 mm of engagement** — within a
tenth of the retention the joint has today, at a ninety-sixth of the force.

| | today | recommended |
| --- | --- | --- |
| ``BLADE`` / slit / leaf | 10 / none / solid | 10 / 7.6 / 1.20 |
| ``STUB_PROUD`` | 1.6 | 1.5 |
| ``MOVE``, which is also the engagement | 1.00 | 0.90 |
| spring | 955 N/mm | 11.0 N/mm |
| press force | 194.78 kgf | **2.02 kgf** |
| worst stress | ear 157.1 MPa | leaf 22.4, ear 1.6 MPa |
| detent, one click | 116.9 kgf | 1.35 kgf |

How the three numbers were picked, in the order they bind:

- **The leaf sets everything.** Once the blade is slit, the leaf is 99% of the spring and the ear
  stops mattering; the whole design problem becomes how thin a leaf may be. At a 0.4 nozzle **1.2 mm
  is three extrusion widths**, which is the floor for something that has to flex without splitting
  along its layers. That fixes the spring at about 11 N/mm.
- **The axle then follows from the target.** 2 kgf against 11 N/mm wants ``MOVE`` 0.89, so
  ``STUB_PROUD`` = 0.89 + ``GAP`` = 1.49, which rounds to **1.5**.
- **The blade width is the one that should not move.** Narrowing it was worth considering only while
  the ear was the spring; with the slit in, blade 9 and blade 10 come out at 11.2 and 11.0 N/mm,
  and blade 9 buys 0.25 mm of band radius for a change that cascades through ``SLOT``, ``EAR``, the
  flank, the valley caps and every drawing on the sheet. **Keep 10.** The slit is then 10 - 2 x 1.2.

Two alternatives, if 1.2 mm of leaf reads too thin to trust:

| leaf | slit | ``STUB_PROUD`` | press | engagement | leaf stress |
| --- | --- | --- | --- | --- | --- |
| 1.2 | 7.6 | 1.5 | 2.02 kgf | 0.90 | 22.4 MPa |
| 1.4 | 7.2 | 1.2 | 2.13 kgf | 0.60 | 17.3 MPa |
| 1.6 | 6.8 | 1.0 | 2.11 kgf | 0.40 | 13.1 MPa |

Every one of them hits 2 kgf; they differ only in how much retention is left. Thicker leaf, less
engagement.

Four things to know before committing:

- **Assumption, and it is the load-bearing one:** the leaf's free length is 12, the same as the
  ear's, which is what a slit running the tongue's whole length gives. It is cubed. If the slit
  stops at the axle instead, the leaf is half as long and eight times stiffer, and none of the
  numbers above survive.
- **Press force and pull-off force are the same force** while the axle is a plain cylinder, so a
  2 kgf joint also comes apart at about 2 kgf. The fix is the usual one for snaps: chamfer the
  axle's outer edge so it leads in, and leave its inner shoulder square so it does not lead out.
  Without that, this whole exercise trades a joint nobody can assemble for one nobody can keep
  together.
- **The tongue keeps its strength.** Two leaves at the outside of the slab hold 55% of the solid
  tongue's bending stiffness, because the material a slit takes out is the material nearest the
  neutral axis. The joint gets soft in the one direction it needs to be soft in.
- **The detent goes soft with it,** to 1.35 kgf a click. Holding torque works out somewhere around
  60 to 120 N-mm against a forearm and gripper that ask for under 10, so it holds, but the margin is
  no longer absurd and ``TOOTH_PROUD`` is now a number worth choosing rather than inheriting.

### Yes, and it changes the answer above

> "When inserting with with blade and fork parallel will the bumps press the leafs out before the
> stub hits?"

*(mine)* Yes, and asking it exposes an error in the section above, which sized the joint off the
axle alone. **The bumps are the insertion load. The axle is a rounding error on it.**

The sequence, with the pins s apart and closing:

- the leading bump enters the slot mouth at **s = 20.8**, because it sits ``BUMP_R`` 8.8 ahead
  of the
  blade's pin and the ear's tip is ``NOSE`` 12 ahead of the fork's
- the axle enters at **s = 12**, by which time **11 of the 24** are already riding the land
- from there every remaining bump joins, and all 24 are on the land for the last 3 mm
- at seating they drop into their valleys together and the whole thing relaxes to nothing

The force through that stroke, for the joint recommended above, counting every engaged contact:

| s | bumps in | from the bumps | from the axle | total |
| --- | --- | --- | --- | --- |
| 20 | 3 | 0.8 kgf | - | 0.8 kgf |
| 12 | 11 | 4.8 kgf | 1.9 kgf | 6.7 kgf |
| 8 | 15 | 11.9 kgf | 1.9 kgf | 13.9 kgf |
| 4 | 21 | 55.7 kgf | 2.0 kgf | 57.6 kgf |
| 2 | 24 | 102.0 kgf | 2.0 kgf | 104.0 kgf |
| ~1.4, where they start to drop in | 24 | ~110 kgf | 2.0 kgf | **~112 kgf** |

**Why it is so much worse than one tooth.** The leaf is rooted at the tongue's root and the ear is
rooted at the rod's end, at opposite ends of the joint, so every contact is soft on one side — but
which side, and how soft, depends on where round the ring the tooth is. A tooth by the blade's tip
runs on a long leaf and gives at 2.1 N/mm. A tooth by the blade's root runs on a leaf 3.2 mm long,
stiff as a wall, and has to lift the ear's tip instead, at 99 N/mm. Summed, the ring is
**962 N/mm — 87 times a single tooth at the leaf's tip**, and it is the teeth near the roots that
carry it. The slit does almost nothing for them.

**``TOOTH_PROUD`` is the lever nobody has chosen.** The interference on the land is
``TOOTH_PROUD - GAP``, exactly parallel to the axle's ``STUB_PROUD - GAP``, and at 1.2 it is 0.60 —
the same interference the axle used to have, times 24 teeth on a stiffer spring.

| ``TOOTH_PROUD`` | land interference | force to lift the ring | detent torque |
| --- | --- | --- | --- |
| 1.20 | 0.60 | 117.6 kgf | 5085 N-mm |
| 0.80 | 0.20 | 39.2 kgf | 1695 N-mm |
| 0.70 | 0.10 | 19.6 kgf | 848 N-mm |
| 0.65 | 0.05 | 9.8 kgf | 424 N-mm |
| 0.60 | 0.00 | none | none |

An arm and gripper ask for well under 10 N-mm to hold a pose. Reaching even 100 N-mm needs an
interference of **0.012 mm**, which no printer resolves. So the band cannot be tuned by its
interference at all: 24 teeth acting together on a ring rooted at both ends is too stiff a system
for the number to have a usable range. **This is structural, not dimensional.**

**One more, from the same geometry.** The dome's radius is ``BUMP_D``/2 = 0.6 and the engagement is
also 0.60, so the bump seats exactly to its equator. At the equator the dome's surface is parallel
to the direction it has to climb, so it does not cam out; it locks. Whatever else changes, the
engagement has to be a fraction of the dome's radius, not all of it.

**What this does to the 2 kgf recommendation.** The three numbers still stand for what they were
solving, the axle's own press. They do not deliver a 2 kgf joint, because the teeth are the load.
The band has to be settled first, and the honest order is: pick what holds a pose, work out what
that costs to insert, then size the axle in what is left.

### Correction: only one tooth carries, and the ~112 kgf was wrong

> "Did you give each tooth the same force or just the 3 or so teeth at the leading edge that press
> the joint apart?"

*(mine)* Each tooth got the same force, independently, and they were summed. That is wrong, and the
number it produced was **eight times too big**.

The leaf and the ear are beams, not a row of separate springs. Pushing the worst tooth out to 0.6
bends the whole leaf, and a cantilever loaded near its root deflects far more further out — at the
governing tooth's station, 3.2 from the leaf's root, the leaf's own tip moves **9.25 times** as far.
So every tooth outboard of the governing one is lifted clear and carries nothing.

Solved properly, as a contact problem with the contact forces free to go to zero:

| s | teeth inside | actually carrying | total | where the load is |
| --- | --- | --- | --- | --- |
| 12 | 6 | 1 | 0.78 kgf | eta +2.3 |
| 8 | 8 | 1 | 1.94 kgf | the axle |
| 4 | 11 | 1 | 9.93 kgf | eta -7.6 |
| 1.4 | 13 | 2 | **14.63 kgf** | eta -8.8, and 0.9 N at the axle |

So the peak is **14.6 kgf, not 112**.

Mike's instinct was right that it is a few teeth, and wrong about which: it is not the leading ones.
The leading teeth touch first, but as deeper teeth enter, they take over and lift the leading ones
off. **The governing tooth is always the last one in** — the one nearest the blade's root, entering
by the ear's tip, where the leaf's lever is 3.2 mm and stiff. It is the same tooth all the way to
seating.

**What this does to the recommendation.** The teeth stop governing as soon as ``TOOTH_PROUD`` comes
down enough for the axle to be the worst contact again:

| ``TOOTH_PROUD`` | peak press |
| --- | --- |
| 1.20 | 15.30 kgf |
| 1.00 | 9.86 kgf |
| 0.90 | 7.13 kgf |
| 0.80 | 4.41 kgf |
| 0.75 | 3.05 kgf |
| **0.70** | **2.02 kgf** |

At 0.70 and below the axle is back in charge and the earlier three numbers stand exactly as they
were. So the recommendation gains a fourth number and loses nothing:

**``BLADE`` 10, slit 7.6, leaves 1.20, ``STUB_PROUD`` 1.5, ``TOOTH_PROUD`` 0.70** — 2.02 kgf to
press, 0.90 mm of engagement, land interference 0.10.

And the detent survives that, because it is the same one-tooth-carries argument in rotation: the
innermost tooth climbing 0.10 takes about 12 N on an 8.8 mm arm, so roughly 200 N-mm over both
faces, against the under 10 N-mm an arm and gripper ask for. The tuning range that looked impossibly
narrow in the section above was an artifact of the same bad model.

*(mine)* Two things still soft in this: the beam model treats the leaf as prismatic when it is a
slice of a circle and its width varies, and it ignores that the two teeth at +/- the same angle sit
at one station and share. Neither moves the conclusion, which is that one contact governs and it is
the trailing one.

#### The same thing said plainly

The joint does not open parallel. It opens as a **wedge**, and the wedge is widest at the blade's
tip. A tooth is touching only where the wedge happens to be exactly as wide as that tooth needs;
everywhere the wedge is wider, the tooth is sitting in air.

Here is the gap at every tooth station at the tightest moment of insertion, 1.4 mm from seated:

| tooth, eta | needs | gap opened | from the leaf | from the ear | |
| --- | --- | --- | --- | --- | --- |
| -8.81, last one in | 0.60 | **0.600** | 0.127 | 0.473 | touching |
| -7.63 | 0.60 | 0.635 | 0.199 | 0.436 | clear |
| -4.41 | 0.60 | 0.739 | 0.404 | 0.334 | clear |
| -2.28 | 0.60 | 0.814 | 0.543 | 0.271 | clear |
| 0.00, the axle | 0.90 | **0.900** | 0.693 | 0.207 | touching |
| +4.41 | 0.60 | 1.086 | 0.985 | 0.101 | clear |
| +8.81, first one in | 0.60 | 1.304 | 1.276 | 0.028 | clear |

Two beams make that wedge, rooted at opposite ends and each widening toward its own free end. The
leaf is rooted at the blade's root, so its share grows toward the blade's tip: 0.127 at the deepest
tooth, 1.276 at the leading one. The ear is rooted at the other end and does the opposite: 0.473
down to 0.028. Their sum still widens toward the blade's tip, from 0.600 to 1.304.

So the leading tooth needs 0.60 and is sitting in 1.30 — seven tenths of a millimeter of air. It
touched earlier in the stroke, when it was the deepest thing in the slot and the wedge pivoted about
it. It stopped touching the moment something deeper came in and took the pivot over.

That is the handover, and one word in it matters: the tooth that carries is the **newest one in**,
which is the one nearest the slot's mouth, not the one deepest inside. It carries because it is the
tooth closest to the leaf's own root, where the leaf is short and stiff and can hardly bend.
Levering
the joint open there swings the leaf's far end wide, and everything deeper is left hanging. The load
never spreads across the teeth; it hands off from one to the next as each new one enters.

Two contacts appear in the table rather than one only because the axle asks for 0.90 where its
neighbors ask for 0.60, so it pokes through a wedge that has already opened to 0.900 there. It is
carrying 0.9 N against the tooth's 70.9.

#### The pictures

Open `.docs/reviews/hinge/changes-pictures.html`. Three drawings, generated by
`.docs/reviews/hinge/wedge_figures.py` from the same numbers as the table above, so a drawing
cannot disagree with it.

- **Each half bends about its own root.** The leaf rooted at the mouth, the ear rooted at the far
  end, each drawn as it actually bends. Left to right is true scale; up and down is four times
  bigger, or the bend would be invisible.
- **The joint opens as a wedge.** The two halves put together, with the air between them shaded.
  Each tooth is drawn at the height that tooth needs. The tooth at the mouth reaches the ear; the
  rest fall short, by 0.704 mm at the far end.
- **Through the stroke the load hands off.** The same joint at four points on the way in. Every
  tooth that is touching carries a number; there is only ever one worth reading, and it is always
  the tooth nearest the mouth, which is the one that just went in.

### Root the leaf and the ear farther out

> I think they mean we like root for the leaf and ear to be farther from center of the joint so
> they are springier without weakening the structure?

Yes, and it is a bigger lever than it looks. It is also the only lever found so far that lowers the
press force and the stress at the same time, and it costs no material.

*(mine)* Two things follow that were not obvious before the pictures.

**The length that governs is not 12. It is 3.2.** The teeth are a ring of radius `BUMP_R` = 8.813,
so the deepest tooth station sits 8.813 nearer the root than the pin does. With the ear rooted at
12 that tooth cantilevers on 12 − 8.813 = 3.19 mm, not 12. Rooting at 21 takes the same arm to
12.19, which is 3.8 times longer, so 55 times softer. The same is true of the leaf against the
blade's root. All the old arithmetic put the load at the pin and therefore flattered the joint.

**The numbers `make_plans.py` already types are the ones this asks for.** `BLADE_OUT` = 32 puts the
blade's root 20 mm from the pin; `SLOT_DEEP` = 33 measured from the fork's tip puts the fork's root
21 mm from the pin. What buries them is the limb, which unions a rod that stops at `NOSE` = 12 and
fills the rest of the slot back in. The rounding rule only says the rod must stop **at least**
`NOSE` from the pin so it clears the other member's swing; it does not say the rod must stop there.
Pulling each rod back to its own root is geometrically free: nothing on either member reaches past
radius 12 from the pin, and both roots are outside that.

So the correction is not to derive `BLADE_OUT` down to `2 * NOSE`. It is to leave 32 and 33 alone
and stop the limb from filling them in. That reverses the settled item in the review's last
section, and it reverses the `EAR_FREE` edit sitting uncommitted in `make_plans.py`.

#### What it buys

Peak press force through the stroke, from the same contact solve as the pictures. Roots are given
as blade / fork, in millimeters from the pin.

| blade | roots | tooth | press | ear root |
|---|---|---|---|---|
| solid | 12 / 12 (what prints today) | 1.2 | 2092 kgf | 644 MPa |
| solid | 20 / 21 | 1.2 | 80.5 kgf | 73.4 MPa |
| slit 7.6 | 12 / 12 | 1.2 | 14.63 kgf | 21.7 MPa |
| slit 7.6 | 12 / 12 | 0.70 | 2.01 kgf | 1.8 MPa |
| slit 7.6 | 20 / 21 | 1.2 | **1.34 kgf** | **2.8 MPa** |

The last two rows are the point. The earlier recommendation reached 2 kgf by shaving the tooth from
1.2 to 0.70, and a tooth is what holds the angle, so it paid for the press with the hold. Moving
the roots reaches 1.34 kgf with the tooth left at its full 1.2. Same press by hand, twice the
detent.

The two roots are not equally worth moving, because the leaf is the softer member:

| | fork 12 | fork 16 | fork 21 |
|---|---|---|---|
| **blade 12** | 14.63 | 9.64 | 6.11 |
| **blade 16** | 4.72 | 4.05 | 3.25 |
| **blade 20** | 1.54 | 1.46 | 1.34 |

Moving the blade's root alone takes 14.63 to 1.54. Moving the fork's root alone takes it to 6.11.

#### What it does not buy

It does not rescue a solid tongue. At 20 / 21 a solid tongue still wants 80 kgf, because with no
slit the ear is the only spring in the joint. The slit is doing work no root position can do, and
the two changes multiply rather than substitute. Any decision to move the roots is still also a
decision about the slit.

#### What it costs

The section over the newly exposed stretch, against the round rod it replaces:

| | mm⁴ | of the rod | stress |
|---|---|---|---|
| round rod | 16286 | 100 % | ×1.00 |
| the two ears, swinging | 4741 | 29 % | ×3.43 |
| the two ears, spreading apart | 550 | 3.4 % | ×29.6 |
| solid tongue, swinging | 10547 | 65 % | ×1.55 |
| the slit tongue's two leaves, swinging | 2224 | 14 % | ×7.32 |

So it does weaken the limb, and here is the honest size of it. In the swing plane, which is where a
limb is loaded, the fork's slotted stretch carries about three and a half times the stress the rod
would. That stretch already exists; the change makes it 21 mm instead of 12. Sideways, the ears
alone are thirty times worse, but the tongue is inside the slot with `GAP` each side, so the joint
rattles 0.6 mm and then bears rather than folding.

The bending moment at the ear's root under a service load barely changes, because moving the root
9 mm along a limb whose load is 150 mm away is nothing. What changes is which section carries that
moment.

The rod loses the length the joint gains. On a 48 mm segment with a 9 mm socket at the far end, the
rod goes from 27 mm to 18 mm, so a little under half the segment becomes fork. Two of these meet at
every elbow and knee, which is worth looking at on screen before it is worth arguing about.

**Mike decides:** whether the limb's rods pull back to 20 and 21, which is what the plan sheet
already draws.

### How strong the joint is, as a torque

> Please summarize in a way that I can quantify how strong the joints are in terms of breaking
> torque (foot pounds) in the various strong and weak axis for the blade and the fork.

*(mine)* Four points, then the two tables.

**Strength is a section property, so moving the roots does not change any of it.** Where a beam is
rooted sets how hard it is to bend, not how much it takes to break it. Every number in the breaking
table below is the same at roots 12 / 12 and at roots 20 / 21. What the roots change is the press
force and the holding torque, which are the second table.

**Nothing in this joint ever reaches its breaking torque.** The teeth let go first, by a factor
between thirty and seven hundred. So the honest answer to "how strong is the joint" is the torque
at which it slips, not the torque at which it snaps.

**The number to hold everything against is 26 N.mm.** One arm below an elbow is about 55 g of PETG
with its weight 48 mm out, so an elbow needs 26 N.mm, which is 0.019 ft.lb, just to stop the arm
drooping. Every useful torque in this joint is a small multiple of that.

**That number kills the 2 kgf recommendation.** Shaving the tooth to 0.70 leaves 0.10 mm of
interference and a slip torque of 7.5 N.mm. The arm falls under its own weight. The recommendation
was sized on the press force alone and never checked against the hold.

#### Breaking torque

Bulk PETG at 50 MPa, and 29 MPa in shear. Swing is bending in the plane the joint hinges in;
sideways is bending out of it, which is the direction that pries the ears apart; twist is about the
limb's own axis. The last two columns are the push at the next joint out, 48 mm away, that would
reach the break.

| section | swing | sideways | twist | swing | sideways |
|---|---|---|---|---|---|
| round rod, Ø24, the limb itself | 50.0 ft.lb | 50.0 ft.lb | 57.8 ft.lb | 144 kgf | 144 kgf |
| the fork: its two ears | 16.5 | 5.4 | 6.3 | 47 kgf | 15.5 kgf |
| the blade: a solid tongue, 10 wide | 35.7 | 14.0 | 5.8 | 103 kgf | 40 kgf |
| the blade: a tongue slit 7.6 | 7.5 | 0.4 | 0.4 | 22 kgf | 1.1 kgf |

The axle is not the weak link: shearing the Ø4.0 stub off takes 74 kgf, and crushing the 1.0 mm
that is engaged takes 41 kgf.

The slit tongue's 0.4 ft.lb sideways and in twist is the worst number in the robot, but it is
pessimistic, because a tongue on its own is not how the joint is loaded. The tongue sits in the
slot with `GAP` each side, so it bears on the ears after 0.6 mm and they carry it. Read the
assembled joint's weak axis as the fork's 5.4 ft.lb.

So the joint's weak axis is about a third of its strong axis, and its strong axis is about a third
of the limb it is set into. Nothing here is fragile.

#### Holding torque, which is what actually gives

The torque that walks the teeth one notch, from the same contact solve. `delta` is
`TOOTH_PROUD - GAP`, the height the joint has to open to let a tooth climb out.

| | press | hold | as a mass at the next joint |
|---|---|---|---|
| roots 12 / 12, tooth 1.2 (what prints today) | 14.63 kgf | 329 N.mm, 0.243 ft.lb | 699 g |
| roots 12 / 12, tooth 0.70 (the 2 kgf study) | 2.01 kgf | 7.5 N.mm, 0.006 ft.lb | 16 g |
| roots 20 / 21, tooth 1.2 | 1.34 kgf | 30 N.mm, 0.022 ft.lb | 64 g |
| roots 20 / 21, tooth 1.8 | 2.69 kgf | 121 N.mm, 0.089 ft.lb | 257 g |
| roots 20 / 21, tooth 2.4 | 4.03 kgf | 272 N.mm, 0.200 ft.lb | 577 g |

Read down the column: today's joint holds well and cannot be assembled. The 2 kgf study can be
assembled and cannot hold. Moving the roots and raising the tooth together gets both, because the
press force falls with the cube of the root length while the hold falls only with `delta`, so the
tooth can be bought back much more cheaply than it was sold.

Row four is the one to look at: **roots 20 / 21 with the tooth at 1.8**. It presses together at
2.69 kgf, which a middle-schooler can do, and it holds 4.7 times the arm's own weight, which is
about a third of what prints today.

A taller tooth is not free. It needs a valley that seats it, so `TOOTH_PROUD - VALLEY_DEEP` has to
stay inside `GAP`, and a taller dome on the same `BUMP_D` is a sharper cone. Both of those run into
the two 1 mm edge rules already settled above. That is the next thing to size, not another press
force.

**Mike decides:** whether the target is a press near 2.7 kgf with a 1.8 tooth, or some other point
on that table.

### Sized: the roots, then the valley

> Let's go with roots that are close to 4 kgf with tooth 1.8, size the roots, and then size the
> valley

*(mine)* Sizing the roots turned up a constraint that was not written down anywhere, and it moves
the axle, so it comes first.

#### The axle has to outlast the tooth

All the teeth ride onto their lands at the same moment, because they are one ring at one phase, so
turning the joint one notch lifts the whole ear by `TOOTH_PROUD - GAP`. The axle sits in the middle
of that ring and is lifted with it. If the axle is engaged by less than the tooth climbs, the arm
comes off instead of clicking.

So `STUB_PROUD` is not a free number. It is

    STUB_PROUD >= TOOTH_PROUD + margin

Today's joint passes by luck: a 1.2 tooth climbs 0.6 and a 1.6 axle is engaged 1.0, so there is
0.4 in hand. Keeping that same 0.4 of margin, **a 1.8 tooth needs a 2.2 axle**. Every earlier
sizing on this page held the axle at 1.5 or 1.6 and is wrong for a tooth taller than that.

#### The roots

With the tooth at 1.8, the axle at 2.2, a 10 mm tongue slit 7.6, and the two roots one millimeter
apart the way `SLOT_DEEP = BLADE_OUT + 1` already has them, a 4.00 kgf press wants the blade rooted
**18.2 mm** from the pin and the fork **19.2 mm**. The tooth count barely moves it, because the
axle and the two end stations set the answer.

Round them to 18 and 19 and the press lands between 4.06 and 4.47 kgf, depending on the count.

The two lengths that carry this should be named for what they are, which also settles the review's
complaint that `BLADE_OUT` is typed where a rule exists. The spring length is the design variable;
the slot depth follows from it:

    TAB_FREE  = 18                          # the leaf, blade root to the pin
    EAR_FREE  = 19                          # the ear, fork root to the pin
    BLADE_OUT = TAB_FREE + NOSE             # 30
    SLOT_DEEP = EAR_FREE + NOSE             # 31

Both are past `NOSE`, which is all the rounding rule asks. The rod on each limb loses what the
joint gains: 27 mm becomes 20 on the fork's limb and 26 becomes 20 on the blade's. That is the one
thing on this page worth looking at on screen before agreeing to it.

#### The valley

Two rules bind it, and only one of them ever wins. The fork's edge is at r 10.613 and the blade's
at r 10.909, so a valley may reach r 9.613 and a bump r 9.909. Since the valley is the bigger
circle, the valley rule always binds and the bump gets the slack. That gives

    BUMP_R = 9.613 - VALLEY_D / 2

The third rule is the land between one valley and the next, which is now a wall right through the
ear rather than a floor, because the valleys go all the way through. A wall wants two 0.4 beads, so
the land wants 0.8. Taking the largest valley that leaves 0.8:

| | valley | bump | BUMP_R | land | bump to the blade's edge | step |
|---|---|---|---|---|---|---|
| 24 teeth | 1.5 | 1.1 | 8.863 | 0.814 | 1.496 | 15° |
| **20 teeth** | **1.8** | **1.4** | **8.713** | **0.926** | **1.496** | **18°** |
| 16 teeth | 2.4 | 2.0 | 8.413 | 0.883 | 1.496 | 22.5° |
| 16 teeth, roomier | 2.0 | 1.6 | 8.613 | 1.361 | 1.496 | 22.5° |

24 teeth falls away: a Ø1.1 bump standing 1.8 proud is a spike, not a dome. The choice is really
20 or 16.

At roots 18 and 19, with the tooth at 1.8 and the axle at 2.2:

| | press | ear stress | hold | against the arm's own weight |
|---|---|---|---|---|
| 24 teeth | 4.47 kgf | 8.8 MPa | 201 N.mm | 7.7× |
| **20 teeth** | **4.33 kgf** | **8.5 MPa** | **162 N.mm** | **6.2×** |
| 16 teeth | 4.06 kgf | 7.9 MPa | 122 N.mm | 4.7× |
| 16 teeth, roomier | 4.24 kgf | 8.3 MPa | 127 N.mm | 4.9× |

**Recommended: 20 teeth at 18°, a Ø1.8 valley, a Ø1.4 bump on r 8.713.** It presses at 4.33 kgf,
holds 6.2 times the arm's own weight, works the ear to 8.5 MPa against PETG's 50, and leaves 0.926
of land, which is two beads and a bit.

The one thing 20 teeth gives up is 45°. A 24-tooth ring hits it and a 16-tooth ring hits it; an
18° ring goes 36°, 54°. If a robot posed at 45° matters more than the finer step, take the last row
instead: 16 teeth, a Ø2.0 valley, a Ø1.6 bump on r 8.613, and 1.361 of land, which is the most
comfortable set of numbers on the page.

#### What falls out of the design

- `VALLEY_DEEP` goes. The valley is a through hole, so there is no floor and no 0.30 clearance to
  quote. The tooth enters 1.20 mm into a wall that is 2.65 mm thick at its thinnest, so it never
  shows through the outside.
- The rim round is already gone by the decision above.
- The bump stops being a hemisphere. At 1.8 proud on Ø1.4 it is a 1.1 mm post capped with an r0.7
  dome. The brief's rule still reads the same way, fillet the crown at the bump's own radius, but
  the shape it produces is a domed post, not a ball.
- Nobody has printed this joint, and a 1.8 mm post hanging off a downward-facing tongue is a longer
  unsupported feature than a 1.2 mm one. That is a print-orientation question, not an arithmetic
  one.

#### The whole set

    GAP        0.6      unchanged
    BLADE      10       unchanged
    SLIT       7.6      two 1.2 leaves
    TAB_FREE   18       new; BLADE_OUT = TAB_FREE + NOSE = 30
    EAR_FREE   19       new; SLOT_DEEP = EAR_FREE + NOSE = 31
    TOOTH_PROUD 1.8
    STUB_PROUD  2.2     = TOOTH_PROUD + 0.4
    STEP       18       20 teeth
    VALLEY_D   1.8      through the ear
    BUMP_D     1.4
    BUMP_R     8.713    = 9.613 - VALLEY_D / 2

### Correction: the 0.4 is dead play, not clearance

> We're saying the valley is required to be 0.4 more diameter than the bump and the land is the
> space between valleys?

*(mine)* The land, yes. The 0.4, not really, and asking about it found a fault in the 20-tooth
recommendation above.

**The land** is the wall between one valley and the next, measured along the chord joining their
centers: `2 * BUMP_R * sin(180 / n) - VALLEY_D`. Since the valleys now go all the way through, that
wall is a wall in the full sense, standing the ear's whole thickness, which is why it wants two
beads rather than one. There is a second gap, the flat between one bump and the next on the blade,
which is `chord - BUMP_D`. It is always the easier of the two and it never governs.

**The 0.4** was carried over from today's Ø2.0 valley and Ø1.6 bump. It is not derived. What it has
to do is let the bump sink into the valley without its side jamming on the wall, so the requirement
is `VALLEY_D >= BUMP_D` plus enough for a printed hole and a printed post to fit. 0.2 a side is a
fair number for that.

**But it is not free, and at a 1.8 tooth it stops being clearance and becomes play.** A seated bump
sinks `TOOTH_PROUD - GAP` below the ear's face. The bump's widest point is `BUMP_D / 2` down from
its tip, where the dome meets the shank. So:

- if `TOOTH_PROUD - GAP <= BUMP_D / 2` the ear's face meets the bump on its **dome**, which is
  curved, so any sideways movement starts climbing at once and the spring pushes it back
- if `TOOTH_PROUD - GAP > BUMP_D / 2` the ear's face meets the bump on its **straight shank**, and
  a straight shank in a straight hole has no restoring force at all

Today's joint is the first case: a 1.2 tooth sinks 0.6 against a 0.8 dome, so there is no play. The
20-tooth recommendation above is the second case: a 1.8 tooth sinks 1.2 against a 0.7 dome, so the
0.4 becomes **0.2 a side of dead rotation, which is 1.3° at every notch**, about 2 mm at the end of
an arm. I did not catch that when I sized it.

#### The rule that was missing

    BUMP_D >= 2 * (TOOTH_PROUD - GAP)

A tall tooth needs a fat bump, and a fat bump needs a fatter valley, and a fatter valley needs more
pitch, so it costs teeth. That makes this a three-way trade where two of the three can be had:

| | teeth | step | bump | valley | BUMP_R | land | press | hold |
|---|---|---|---|---|---|---|---|---|
| tall tooth, fine step, **1.3° of play** | 20 | 18° | 1.4 | 1.8 | 8.713 | 0.926 | 4.33 kgf | 162 N.mm, 6.2× |
| tall tooth, no play, **coarse step** | 12 | 30° | 2.4 | 2.8 | 8.213 | 1.451 | 3.89 kgf | 88 N.mm, 3.4× |
| tall tooth, no play, middle step | 16 | 22.5° | 2.4 | 2.8 | 8.213 | 0.405 | 3.89 kgf | 117 N.mm, 4.5× |
| fine step, no play, **short tooth** | 24 | 15° | 1.6 | 2.0 | 8.613 | 0.248 | 2.12 kgf | 48 N.mm, 1.8× |

The last row is today's tooth on the new roots. It has no play and the finest step, and it holds
1.8 times the arm's own weight on a 0.248 land, which is under one bead.

**Revised recommendation: 12 teeth at 30°, a Ø2.4 bump, a Ø2.8 valley on r 8.213.** No dead play,
1.451 of land and 1.851 of flat, which are the roomiest numbers anywhere on this page, 3.89 kgf to
press, and 3.4 times the arm's weight held. The step lands on 0°, 30°, 60° and 90°, so it keeps
what the multiple-of-four rule was protecting and gives up 45°.

The 16-tooth row keeps 45° and a finer step for the same bump and valley, but its land is 0.405,
which is exactly one bead and no margin. It is the row to take if 22.5° matters; it is not the row
to take if the land is what worries you.

**Mike decides:** how much dead play a notch may have, which is what picks between rows one and
two.

### Correction: the section above is wrong twice over

> How are you getting rid of play without making the bottom of the bump wider than the valley?

*(mine)* I am not. There is no way to, and the rule I wrote to buy it is backwards.

**Play cannot be removed.** The tooth passes through the ear's face at height `GAP` above the
blade's face. Its radius there is some `R(GAP)`. The valley's radius is `VALLEY_D / 2`. The play is
the difference:

    play = VALLEY_D / 2 - R(GAP)

For the tooth to sink into the valley at all, the valley has to be wider than the tooth is at that
plane, by at least enough for a printed hole and a printed post to go together. So the play is
never less than the printing clearance, whatever the diameters are. Measured:

| | play | at its radius |
|---|---|---|
| today, tooth 1.2 on a Ø1.6 bump | 0.225 mm | 1.35° |
| the 20-tooth row, tooth 1.8 on a Ø1.4 bump | 0.200 mm | 1.32° |
| the 12-tooth row, tooth 1.8 on a Ø2.4 bump | 0.200 mm | 1.40° |

They are all the same number. The column headed "no play" was fiction, and so was the claim in the
paragraph above it that today's joint has none.

**What I was actually looking at is whether the tooth can climb out at all**, which is a different
property, and I stated its rule the wrong way round. A domed post's widest point, its equator, sits
at `TOOTH_PROUD - BUMP_D / 2` above the blade's face. The ear's face sits at `GAP`. What matters is
which is higher:

- equator **below** the face: the face meets the tooth on the narrowing dome, which is a slope, so
  the tooth rides up it and out
- equator **at** the face: the tooth's surface there is vertical, so the ramp is infinite
- equator **above** the face: the face meets the straight shank, and the tooth is undercut

Written out, riding out needs `BUMP_D > 2 * (TOOTH_PROUD - GAP)`, which is the inequality I wrote,
but I then chose numbers that make it an equality and called them the safe ones. Ø2.4 with a 1.8
tooth puts the equator at exactly 0.60, which is exactly the face. That row is a locked joint.

**And the row I recommended before it is worse.** 20 teeth, a Ø1.4 bump, a 1.8 tooth: the equator
is at 1.10 and the face at 0.60, so the face cuts the straight shank half a millimeter below the
widest point. That tooth is undercut. Once seated it does not click, it holds until something
breaks.

So of the four rows in that table, two are joints that cannot be turned, and the property the table
was sorted on does not exist.

**How I got it wrong.** I reasoned that a straight shank in a straight hole gives no restoring
force, which is true, and concluded that the bump should be made fatter until the shank was out of
the way. Making it fatter moves the equator *down*, toward the blade's face and away from the ear's
face. I never worked out which side of the face the equator landed on; I asserted the rule from the
shape of the argument instead of computing the contact. The arithmetic that would have caught it is
one line and is now written above.

Nothing in the sizing before this section is affected except through `BUMP_D` and `TOOTH_PROUD`:
the roots, the two 1 mm rules, the land definition, and the axle rule all still stand.

### The fork's face at 5.20, and a cone with a flat top

> Let's move the forks inner face to +/-5.20mm. Let's make the bumps be cones with a flat top.
> Let's design the valleys to be 1.2mm diameter. What is the bump size at a 45 degree slant with a
> 0.2mm flat top that nominally contacts the 1.2mm diameter valley. I think it is 2*(0.6+0.2)
> 1.6mm diameter base of the bump. I think we can fit 24 teeth.

*(mine)* The base is 1.6, 24 teeth fit with room to spare, and the cone does the one thing the
dome could not.

**The base.** The cone has to be Ø1.2 where it crosses the ear's face, which is `GAP` = 0.20 above
the blade's face, and at 45° the radius grows one for one with the rise. So the base radius is
0.60 + 0.20 and the base is **Ø1.60**, which is the arithmetic in the question.

**The height is a separate number, and the flat top sets it.** The base and the slant fix where the
cone seats; the flat top fixes how tall it is, and therefore how far the joint has to open to let it
out. Running from Ø1.60 at the base to the flat at 45°:

| flat top | height | climb, `TOOTH_PROUD - GAP` | axle, at `TOOTH_PROUD + 0.4` |
|---|---|---|---|
| 0.2 | 0.70 | 0.50 | 1.10 proud, 0.90 engaged |
| 0.4 | 0.60 | 0.40 | 1.00 proud, 0.80 engaged |

A 0.2 flat is half a nozzle, so it will come out as a rounded point rather than a flat. Size it at
0.4 and take the 0.60 tall cone; a rounded tip is better for camming anyway.

**The cone removes the play, and it does it by seating on a taper.** A cone landing on the valley's
rim centers itself: any difference between the printed hole and the printed cone is taken up by the
cone sitting a little deeper or a little shallower, not by sliding sideways. That is the thing a
domed post in a straight hole cannot do at any diameter.

**24 teeth.** With the fork's face at 5.20 the ear's edge moves out to r 10.8148, so a valley may
reach r 9.8148 and a bump r 9.9087. The bump is now the bigger circle, so for the first time the
**bump rule binds**: `BUMP_R = 9.9087 - 0.80 = 9.109`.

| teeth | step | land between valleys | flat between bumps | hits 45° |
|---|---|---|---|---|
| 32 | 11.25° | 0.586 | 0.186 | yes |
| 28 | 12.86° | 0.840 | 0.440 | no |
| **24** | **15°** | **1.178** | **0.778** | **yes** |
| 20 | 18° | 1.650 | 1.250 | no |

24 is comfortable: nearly three beads of land and nearly two of flat. 28 would build but misses 45°.
32 leaves 0.186 between bumps, which is under half a bead.

**What moving the face to 5.20 costs and pays.** The slot narrows to 10.4, so the ear thickens from
6.4 to 6.8 and its second moment rises from 275.2 to 338.3, a 23 % stiffer spring. Against that,
the climb falls from 0.60 to 0.40, and force goes as the climb. The climb wins.

#### The numbers, and a measure I had wrong

Press through the stroke and breakaway torque, 24 teeth on r 9.109, a 10 mm tongue slit 7.6.

| roots | flat | climb | press | breakaway | against the arm's weight | ear |
|---|---|---|---|---|---|---|
| 14 / 15 | 0.4 | 0.40 | 5.64 kgf | 504 N.mm | 19.4× | 8.3 MPa |
| **16 / 17** | **0.4** | **0.40** | **2.99 kgf** | **268 N.mm** | **10.3×** | **4.8 MPa** |
| 17 / 18 | 0.4 | 0.40 | 2.21 kgf | 197 N.mm | 7.6× | 3.7 MPa |
| 18 / 19 | 0.4 | 0.40 | 1.66 kgf | 148 N.mm | 5.7× | 2.8 MPa |
| 18 / 19 | 0.2 | 0.50 | 2.07 kgf | 185 N.mm | 7.1× | 3.6 MPa |
| 20 / 21 | 0.4 | 0.40 | 0.95 kgf | 85 N.mm | 3.3× | 1.7 MPa |

**The torque column is not the same measure as the one in the tables above it.** Those quoted the
work to cross a whole notch divided by the notch's angle, which is an average over a stroke that is
mostly flat sliding. What holds a joint is the peak, at the top of the ramp, and for a 45° cone
that is exactly `press force x BUMP_R` because the tangential and axial components are equal. The
earlier averages understate the hold and should not be compared against this column.

A solid tongue is still hopeless: 70 kgf even at roots 20 / 21. The slit is not optional.

**Roots 16 and 17 look like the pick**: `BLADE_OUT` 28, `SLOT_DEEP` 29, a 3 kgf press, ten times the
arm's own weight held, and the ear worked to 4.8 MPa against PETG's 50. The rods lose less than
they would have at 18 and 19.

#### Two things to watch

- `GAP` = 0.2 is now doing two jobs: it sets where the cone seats, and it is the clearance for a
  10 mm tongue in a 10.4 slot. On an X1C a slot prints narrow and a tongue prints wide, so 0.2 a
  side could close up to nothing and the tongue would bind before the teeth ever met. If that
  happens the way out is to relieve the slot to 11.2 everywhere except the toothed band, so the
  seat keeps 0.2 and the fit gets 0.6.
- The cone lands on a sharp hole rim, which is a line contact. That is a real cam, but the rim will
  wear or crush a little on the first few cycles, which will lower the hold from the numbers above.

**Mike decides:** the roots, and whether the slot is relieved outside the band.

### Drawn: the relieved slot, and the rim that does not stay sharp

Open `.docs/reviews/hinge/seat-pictures.html`. Two drawings, generated by
`.docs/reviews/hinge/seat_figures.py` from the same numbers as the section above.

**`seat.svg` — where a 0.20 seat and a 0.60 fit can both live.** Sectioned across the pin, drawn
260 times full size, so left to right is distance out from the pin and up the page is along it. Two
ways to get both numbers at once, and they are not quite equal:

- Relieve the slot to 11.2 and leave a raised band, 2.4 wide, on the inside of each ear. The cone
  goes on the tongue at 5.0, where the limb's round is still far away, so the bump may sit at
  r 9.109.
- Or leave the slot flat at 11.2 and raise the band on the tongue instead. That puts the cone's
  base at 5.4, where the round has already begun to close in, so the bump has to come in to
  r 8.915 and the joint gives up a little of its lever.

Either way the tongue keeps 0.60 a side over nearly all of its area and the cone still crosses the
ear's face 0.20 up, which is what fixes the Ø1.2 valley and the Ø1.6 base. The band is the only
place either part is held to a print tolerance.

**`rim.svg` — the cone lands on a corner, and the corner does not stay sharp.** The same cone and
valley at 150 times full size, in three states: seated new with the faces 0.200 apart and 0.400 of
climb left; at the top of the climb with the faces 0.600 apart, riding the land; and seated again
after the rim has worn 0.10, with the faces 0.341 apart and 0.259 of climb left.

A round on the rim, designed in or worn in, holds the cone up off its seat by 1.414 times the
radius, so the joint loses that much climb before it starts to turn:

| rim round | climb | holds |
| --- | --- | --- |
| 0.00 | 0.400 | 100% of new |
| 0.05 | 0.329 | 82% |
| 0.10 | 0.259 | 65% |
| 0.15 | 0.188 | 47% |

Two consequences. The 0.1 round that used to sit on the valley's rim was worth taking off, and it
must stay off. And the joint will feel looser after a few dozen presses than it does on the first
one, so the tooth is sized for the worn number, not the new one; the 3 kgf press at roots 16 and 17
is the new number, and two thirds of its hold is what to plan on.

### Settled: one raised land, chamfered coming and going

> make the band that is 0.20 at the seat, 1 rectangle that is as wide as the leaf and is
> chamfered rising up to it in both coming and going, but only covers the length a little past
> widest valley

Drawn in `seat.svg`, which now has three panels: the ear's inner face looked at along the pin,
a section down the slot on the middle line, and the true-scale section out across the width.
`seat_figures.py` generates all three.

The slot is relieved to 11.2 everywhere. One land, and only one, stays at 10.4:

| | |
| --- | --- |
| along the slot | 20.8, that is 10.4 each way from the pin |
| across the width | 21.2, which is the whole face; the rod's round ends it at 10.61 |
| how proud | 0.40 a side, which is what leaves the 0.20 fit at the seat |
| the two ends | chamfered 0.4 in 1.2, an 18° ramp |
| clear of the valleys | 0.69 past the widest part of the ring, which reaches 9.709 |

Why it is a rectangle and not a ring. A ring at the tooth radius would have an inner step and an
outer step as well as the two ends, and the tongue's face would have to cross all four. A rectangle
as wide as the leaf runs off both sides of the face, so there is no side step at all; only the two
ends are steps, and both of them are chamfered. Nothing on either part ever meets a square edge.

Why it stops at 10.4. The tongue enters over the ear's tip at 12. If the land ran to the tip the
tongue would meet a 0.4 step in the mouth of the slot. Stopping at 10.4 and ramping out to 11.6
leaves 0.4 of relieved face at the mouth, so the tongue is already guided before it starts to
climb. The far end is the same in reverse: the tongue's nose reaches 12 past the pin when it
seats, so it runs off the far end of the land and needs the ramp there too, coming and going.

Two things the drawing shows that the arithmetic did not:

- The face is 21.2 across, not 24. The ear is what is left of a Ø24 rod after an 11.2 slot is cut
  through it, so its inner face runs out where the rod's own round reaches that depth, at 10.61.
  The land, being 0.2 closer to the mid-plane, gets to 10.81. Either way the valley ring's outer
  edge at 9.709 has under a millimeter of face outside it.
- The leaf's face is 21.8 across by the same arithmetic at 5.0, so the leaf is a touch wider than
  the land. That is the right way round: the land is fully covered in every position.

The axle is drawn in the second panel. It stands 1.00 proud into a bore whose mouth is now the land
at 5.20, so 0.80 is engaged against a 0.40 climb, which still satisfies the rule that the axle must
out-engage the tooth.

### Decided: roots 16 and 17, a 0.4 flat top, and the slit rederived

> Let's go with roots 16 and 17 and a 0.4 flat top. Rederive the slit. Move the fork's robot
> connector. The part names become forks and blade.

Taken as: the parts are named `fork` and `blade`, one name each.

#### The slit is not optional, and 7.6 was too much

A solid tongue at roots 16 and 17 needs **206 kgf** to press together. The ear on its own cannot be
the spring; the joint has to open as a pair of springs in series, and the second one is the tongue.

The slit's width is the only thing left free, and it is a straight trade. A wider slit gives thinner
leaves, which press easier and hold less, and which snap sideways sooner. Everything below is at
roots 16 and 17, 24 teeth, a 1.6 cone with a 0.4 flat top, a 0.40 climb and the axle 1.00 proud:

| slit | each leaf | press, kgf | hold, N·mm | after 0.10 of wear | sideways, at the hand |
| --- | --- | --- | --- | --- | --- |
| 4.0 | 3.00 | 9.96 | 795 | 514 | 2.29 kgf |
| 5.0 | 2.50 | 7.30 | 691 | 447 | 1.59 kgf |
| **6.0** | **2.00** | **5.50** | **588** | **380** | **1.01 kgf** |
| 6.8 | 1.60 | 4.30 | 459 | 296 | 0.64 kgf |
| 7.6 | 1.20 | 2.99 | 283 | 183 | 0.36 kgf |

"Sideways, at the hand" is the push it takes to break the tongue in its weak axis, applied 150 mm
out, which is about where a hand is. Nothing in that column is protected by the detent, because the
detent only resists swing.

**The slit is 6.0, leaving two leaves 2.00 thick.** It is the widest slit whose tongue still takes a
kilogram at the hand. Below it the press gets easier but the arm starts to snap off when a child
picks the robot up by its forearm; above it the press climbs past what a middle-schooler will do
four times in a row.

The slit runs the whole tongue, all 28 mm of it, from the nose to where the limb's rod roots it. The
leaf's 16 mm of free length is the whole reason these numbers work; a slit that stops short of the
root stiffens the joint fast.

#### The press fit force

**5.50 kgf**, both sides together, which is 12 lb. Against the 194.78 kgf the review page found on
the printed elbow, that is a factor of 35.

What sets it is the **teeth**, not the axle. Broken apart at roots 16 and 17 with a 6.0 slit:

- the axle's 0.80 of engagement on its own: 3.37 kgf
- the teeth's 0.40 of climb on its own: 5.87 kgf
- both together: 5.50 kgf

The two do not add. Lifting the ear 0.80 at the pin lifts its neighborhood by more than the 0.40 the
teeth there need, so those teeth come off contact and stop carrying. That also means shortening the
axle buys nothing: at 0.70 of engagement the press is 5.61 kgf, and at 0.60 it is 5.72. The axle can
be sized for retention alone.

Stresses at the worst moment of the press: the ear at **7.6 MPa** and a leaf at **19.4 MPa**, both
against PETG's 50. The old design's ear was at 157.

#### The detent, click and hold

This is a **different load case from the press**, and an earlier section in this file got it
wrong by
treating them as one. Pressing the joint together opens it as a wedge, widest at the tongue's tip,
so only the last tooth in is touching. Turning a seated joint asks **every tooth to climb at once**,
with the axle home in its bore carrying nothing. The two give different forces.

Turning the joint at roots 16 and 17 with a 6.0 slit:

| | |
| --- | --- |
| teeth actually carrying | one, the one nearest the blade's root |
| force to lift it | 64.5 N over both faces |
| breakaway torque, new | **588 N·mm**, or 0.434 ft·lb |
| after the rim wears 0.10 | **380 N·mm**, or 0.280 ft·lb |
| what that is at the hand | 0.40 kgf new, 0.26 kgf worn |
| against the arm's own weight | 22.6 times new, 14.6 times worn |
| ear stress while turning | 10.0 MPa |
| leaf stress while turning | 14.9 MPa |

One tooth carrying is the same result as during insertion, and for the same reason: the members are
beams. Lifting the tooth on the short lever lifts every tooth further out by more than its own
climb, so they ride clear. In rotation the governing tooth is the one on the **leaf's** short lever,
6.89 from the leaf's root, where in insertion it was the last tooth in.

A worn hold of 380 N·mm is 0.26 kgf at the hand. That is a firm nudge, not a knock, which is what a
posable arm should feel like.

#### What breaks first, and at what

| | swing | sideways | twist |
| --- | --- | --- | --- |
| the limb rod, Ø24 | 50.0 | 50.0 | 57.8 |
| the fork, its two ears at 6.8 | 18.4 | 6.2 | 7.3 |
| the blade, a solid tongue | 35.7 | 14.0 | 11.7 |
| **the blade, slit 6.0, leaves 2.00** | **13.0** | **1.1** | **1.2** |

All in ft·lb. The ear is 6.8 thick now instead of 6.4, so the fork gained about a seventh over the
review page's figures.

The weakest thing in the joint is the slit tongue in its weak axis, at 1.1 ft·lb, which is 1.01 kgf
pushed at the hand. Everything else is between five and forty times that. In swing, which is the
axis the joint is for, the detent gives at 0.434 ft·lb and the tongue breaks at 13.0, so the joint
lets go 30 times before anything yields.

The axle shears at 73.9 kgf and crushes its 0.80 of engagement at 32.6 kgf, so with a 5.50 kgf press
it has six times the margin it needs.

#### The roots are worth one more look

Roots 16 and 17 were picked when the model still had a 7.6 slit in it, where they gave 2.99 kgf and
10.3 times the arm's weight held, and 18 and 19 gave only 5.7 times. With the slit rederived, hold
is no longer scarce anywhere, and the roots turn out to be the cheaper lever: they buy softness for
free, because **strength is a section property and does not care where a beam is rooted**, while
stiffness goes as one over the cube of the length.

| roots | slit 4.0 | slit 5.0 | slit 6.0 | slit 7.6 |
| --- | --- | --- | --- | --- |
| 14 / 15 | 14.87 | 11.36 | 8.82 | 5.64 |
| 16 / 17 | 9.96 | 7.30 | **5.50** | 2.99 |
| 18 / 19 | 7.06 | **4.80** | 3.47 | 1.66 |
| 20 / 21 | **5.18** | 3.22 | 2.22 | 0.95 |

Press, in kgf. Sideways strength reads straight off the slit and is the same in every row: 2.29 kgf
at slit 4.0, 1.59 at 5.0, 1.01 at 6.0, 0.36 at 7.6.

So roots 20 and 21 with a 4.0 slit press at 5.18 kgf, a shade easier than the settled pair, and the
tongue takes 2.29 kgf at the hand instead of 1.01. It still holds 268 N·mm worn, ten times the arm.
What it costs is rod: each root pulls the limb's rod back another millimeter, and at 20 and 21 a
little under half of every 48 mm segment is joint rather than rod. That is a look, not a number, and
it is why the shorter pair was chosen.

**Mike decides:** whether to leave the roots at 16 and 17 with a 6.0 slit, or move to 20 and 21 with
a 4.0 slit and buy back the tongue's weak axis. The rest of the design is the same either way.

#### The connector and the names

- The fork's robot connector moves to the fork's end face, where the blade's already is, pointing
  out. It takes Transform's flip out of tutorial 10 and gives both limbs one rule to state. It
  changes tutorials 9 and 10.
- The two parts are named `fork` and `blade`. The page for tutorial 10 stops having to say "Part 2,
  which is the fork" three times.

Both are recorded here only. The CAD is frozen and so is `index.rst`.

#### Where the stale numbers lived

The freeze lifted on 2026-08-30 and all four landed:

- `src/stickbot/make_plans.py`: `GAP`, `STUB_PROUD`, `BLADE_OUT`, `SLOT_DEEP`,
  `EAR_FREE`, `TOOTH_PROUD`, `VALLEY_D`, and the slit, which came out on 2026-08-24 and went back
  in. `VALLEY_DEEP` is gone; the valley is a through hole. `PRESS_F` and `EAR_STRESS` now come out
  of `src/stickbot/hinge_spring.py` rather than being typed
- the hinge plan sheet, which `detail_hinge` draws from those
- the build brief, rewritten whole, and the assembly brief, which both carried 36.3 kgf
- `.docs/reviews/hinge/source/index.rst`, rewritten so that every finding ends in a decision

### Decided: roots 20 and 21 with a 4.0 slit

> Let's go with roots 20 and 21 and a 4.0 slit, does that make the slit tongue stronger?

Yes. Half again in swing, and about two and a third times in the two weak axes:

| the tongue, at its root | 16 / 17, slit 6.0 | 20 / 21, slit 4.0 | |
| --- | --- | --- | --- |
| each leaf | 2.00 | 3.00 | |
| swing | 13.0 | 20.3 | ft·lb |
| sideways | 1.10 | 2.49 | ft·lb |
| twist | 1.24 | 2.79 | ft·lb |
| sideways, pushed at the hand | 1.01 | 2.29 | kgf |

**The slit is doing all of that, not the roots.** Strength is a section property; it does not care
where a beam is rooted. What the longer roots buy is softness, and softness is what pays for the
narrower slit. The two moves have to be made together, which is why the table above only has two
columns and not four.

#### The whole joint at 20 and 21

| | |
| --- | --- |
| `BLADE_OUT`, `SLOT_DEEP` | 32 and 33 |
| `TAB_FREE`, `EAR_FREE` | 20 and 21 |
| the limb's rods | 19 mm on the blade's side, 18 on the fork's |
| the slit | 4.0 wide, the whole 28 mm of the tongue, leaves 3.00 |
| press fit | **5.18 kgf**, both sides, which is 11 lb |
| breakaway, new | **414 N·mm**, 0.306 ft·lb, 0.28 kgf at the hand, 15.9 times the arm |
| breakaway, worn 0.10 | **268 N·mm**, 0.198 ft·lb, 0.18 kgf at the hand, 10.3 times the arm |
| ear and leaf, pressing | 6.7 and 15.0 MPa |
| ear and leaf, turning | 7.9 and 7.7 MPa |
| teeth carrying, turning | two |

Everything else is unchanged: the face at ±5.20, the 0.20 seat, the land and its two ramps, Ø1.2
valleys, a 1.6 cone with a 0.4 flat top, 24 teeth on r 9.109, the axle 1.00 proud.

#### What flips, in the review page's findings

`BLADE_OUT` 32 and `SLOT_DEEP` 33 are exactly the numbers typed in `make_plans.py` today. So the
finding that they were typed where the rule beside them derives them resolves the other way round:
**the typed pair stays and the limb's rods move.** Each rod ends at its root instead of at `NOSE`,
which is 19 mm on the blade's side and 18 on the fork's, out of a 48 mm segment carrying a 9 mm
socket at its far end. A little under half of every segment becomes joint.

`EAR_FREE = SLOT_DEEP - NOSE` is then right as it was originally written, 21 mm, and the
uncommitted edit that made it `NOSE` comes back out. The plan sheet's 21 mm ear was never the thing
that was wrong; the rod was.

#### The axle is back in charge of the press

At 16 and 17 with a 6.0 slit the teeth set the press and the axle's length bought nothing. At 20
and 21 with a 4.0 slit that reverses, because the leaves are thicker and the teeth are softer to
climb than the axle is to lift:

| axle proud | engaged | press | crushes at |
| --- | --- | --- | --- |
| 1.00 | 0.80 | 5.18 kgf | 32.6 kgf |
| 0.90 | 0.70 | 4.53 kgf | 28.5 kgf |
| 0.80 | 0.60 | 4.36 kgf | 24.5 kgf |

Below 0.90 the teeth take over again at 4.19 kgf and nothing more is on offer. The hold does not
move at all, because the axle is home in its bore when the joint turns.

Keep the axle at 1.00 proud. It out-engages the tooth's 0.40 climb by 0.40, which is the margin the
rule asks for, and it crushes at six times the press. Take the 0.90 only if 5.18 kgf turns out to be
too much in the hand, and know that it spends half the axle's margin to save 0.65 kgf.

#### Weakest link, restated

| | swing | sideways | twist |
| --- | --- | --- | --- |
| the limb rod, Ø24 | 50.0 | 50.0 | 57.8 |
| the fork, its two ears at 6.8 | 18.4 | 6.2 | 7.3 |
| **the blade, slit 4.0, leaves 3.00** | **20.3** | **2.49** | **2.79** |

All in ft·lb. The tongue is still the weakest thing in the joint sideways, but by two and a half
times against the fork rather than five and a half. At the hand that is 2.29 kgf against the fork's
5.75. In swing the detent lets go at 0.306 ft·lb and the tongue breaks at 20.3, so the joint gives
sixty-six times over before anything yields.

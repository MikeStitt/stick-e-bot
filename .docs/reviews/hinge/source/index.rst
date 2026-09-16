============================
What is wrong with the hinge
============================

.. note::

   **The joint on this page was printed, and then replaced.** Everything below is about a detent
   made of 45 degree cones dropping into holes bored through the ear. That joint was built as
   ``stickbot-draft9p1p2`` and ``stickbot-draft9p1p4``, printed, and measured at 210 N·mm against
   the 454 N·mm this page reports. The printer had put supports in the valley holes and they could
   not be cleaned out; 0.235 mm of residue in a valley, which is one extrusion width, accounts for
   the whole loss. The detent is now a ring of wedges standing proud of both members, with no hole
   anywhere in the joint. The last section says what changed and what it cost.

   This page is kept as the record of how the joint got here, so it is frozen. Its lengths are the
   lengths it reviewed, held in ``J`` in ``make_figures.py``, and no longer read out of the design
   source.

The elbow and the knee are the same joint. A **fork** carries two **ears** with a bore through
each; a **blade** carries a **tongue** with an **axle** across it; the tongue goes down the fork's
**slot** until the axle snaps into the bores, and a ring of teeth on each face holds whatever angle
the joint is left at. This is what a sweep of that joint found, and what was decided about it.

Where the numbers come from. A name in ``code`` is a length of the reviewed joint, frozen in ``J``
in ``.docs/reviews/hinge/make_figures.py``. It used to be read live out of
``src/stickbot/make_plans.py``, and that stopped being right the day the design source
stopped holding this joint. A position in millimeters is read off the model itself, through
Onshape's ``bodydetails``, with the pin on the origin. The drawings are generated from those same
frozen numbers, so a drawing here cannot disagree with the joint it draws. The press force and the
detent torque are still solved rather than typed, by ``src/stickbot/hinge_spring.py``, which is a contact
solver rather than a formula, for reasons the findings below give; run that file and it reproduces
both of this page's headline numbers, 7.16 kgf and 454 N·mm, on this geometry. The photographs are shaded views of
``stickbot-draft9p1p1``, which is the joint as it was when the sweep was made.

Every finding here now ends in a decision, and the decisions are in the design source. The joint
they add up to is in the last section.

.. contents::
   :local:
   :depth: 1

Both documents hold the same joint
==================================

.. figure:: images/frames.png
   :class: fig
   :alt: the fork, the blade, and the two of them together, seen square across the pin

   The hinge Part Studio, looked at square across the pin. Each part carries a stub of its own
   limb, and the pin is where the two overlap. The fork's limb runs up the page and the blade's
   down it, which is how every drawing on this page is laid out too.

``stickbot-draft9p1p1`` and ``stickbot-draft9p3`` answer identically: 153 faces on the fork and 111
on the blade in each, and the same bounding boxes to the last decimal. So nothing below is a
copying mistake in draft9p3. It is design, and it lands on 9p1p1 as hard as on 9p3.

The doubling took four lengths with it that should not have gone
================================================================

.. include:: tables/doubling.rst

Only ``LIMB`` is derived from anything. The rest were typed, and the pass that took the robot to
twice its size doubled them as one block.

Doubling is right for a length that sets the shape. It is wrong for two other kinds. The first is a
clearance the printer has to hold: ``GAP`` is the room each side of the tongue, and a printer does
not lay a wider bead because the part got bigger, so doubling it turns a fit into a rattle.
``STUB_PROUD`` is the same. The second kind is a length another number decides, and that is where
the interesting damage is.

``GAP`` is now 0.15, which is a fit rather than a rattle, and it is held over the 20.8 mm the teeth
need instead of the whole 33 mm of the slot. ``STUB_PROUD`` is 1.30. Both of those are decided
further down.

``BLADE_OUT`` is typed where the comment beside it gives a rule
===============================================================

The comment in ``make_plans.py`` says every end is rounded on ``NOSE`` about the pin, so the fork's
ear tips sweep ``NOSE`` from the axis, and the blade's own limb has to end ``NOSE`` clear of them or
the joint cannot close. That reads as a rule for ``BLADE_OUT``, and the rule gives ``2 * NOSE``,
which is 24. It is typed 32.

.. figure:: images/slot.png
   :class: fig
   :alt: the hinge tab with the slot's root, the blade's nose and the pin marked

   Nine millimeters of the slot sit above the highest point the blade's nose ever reaches, in every
   position the joint can be put in. The three lines are read off the model: the slot's walls run
   from the fork's tip to 21 mm past the pin, and the blade's nose stops at 12.

**Settled: the typed pair stays and the rule is what was wrong.** The comment gives the shortest
``BLADE_OUT`` the joint can close at, not the right one. What those nine millimeters buy is free
length, and free length is the only thing that makes this joint pressable by hand. ``BLADE_OUT`` 32
and ``SLOT_DEEP`` 33 root the tongue 20 mm from the pin and the ear 21, which is where the press
force comes out at something a middle-schooler can do. So the numbers are kept and the comment is
rewritten to say what they are for.

The limb's rod used to bury the free lengths, and now it stops short
====================================================================

Neither root survived into a part anyone printed, because each limb unioned a rod onto its half of
the joint and the rod ran all the way to ``NOSE`` from the pin, filling the slot back in.

.. figure:: images/burial.png
   :class: fig
   :alt: the joint with the rod run on to the pin, and the same joint with the rod stopped short

   Left, what draft9p1p1 prints: the rod fills in the last 9 mm of the slot and the first 8 mm of
   the tongue, and both members are rooted at 12 mm. Right, what the settled design asks for: each
   rod stops where its member's own cut stops.

Read off ``stickbot-draft9p1p1``, with the elbow's pin as the origin of each limb:

- the upper limb's slot walls run from 12 mm on the far side of the pin to 12 mm on the near side,
  so the slot is 24 mm deep and its root is ``NOSE`` from the pin
- the lower limb's tongue faces run the same way, so the tongue is 24 mm long and its root is
  ``NOSE`` from the pin as well
- the upper limb's rod is 27 mm long and the lower limb's 26 mm

**Settled: the rods move.** Each is ``LIMB_CENTER``, less how far its far joint's center stands
off the rod's own end face, less its hinge member's root. That gives three lengths across the four
limbs: 32 on the upper arm, whose shoulder socket is in a side face, and 18 on the thigh, the
forearm and the shin. The slot and the tongue then reach the roots the arithmetic uses, and a
printed elbow is a printed elbow rather than a different joint that happens to look the same.

What the roots do to the spring
===============================

A cantilever's stiffness goes as one over the cube of its free length. Its **strength** is a section
property and does not move at all. That asymmetry is the whole reason a long root is worth having:
it buys softness for nothing.

.. figure:: images/ear.png
   :class: fig
   :alt: one ear drawn three times, rooted at 33, 12 and 21 millimeters from the pin

   The same ear, the same 0.45 mm of climb, and the same solver. Only where the two members are
   rooted changes.

.. include:: tables/rooted.rst

The build brief and the assembly brief both used to carry 36.3 kgf and 51.3 MPa, which came from a
cantilever formula that treated the ear as the only spring and every tooth as an independent one.
Neither is true, and the section after next says why.

The plan sheet drew the ear longer still
========================================

``detail_hinge`` in ``make_plans.py`` drew the slot's root at ``SLOT_DEEP`` from the pin.
``SLOT_DEEP`` is measured from the fork's tip, not from the pin, so the ear on the published sheet
was 33 mm free where the Part Studio has 21 mm. That is the first row of the table above, and it was
the picture a student was handed.

**Settled and fixed.** The sheet draws the root at ``SLOT_DEEP - NOSE``, and it draws both members
cut off 15 mm from the pin with the two roots called out, because a detail drawn long enough to
reach them has nothing left to show at that scale.

The axle held the arm on by one millimeter
==========================================

.. figure:: images/axle.png
   :class: fig
   :alt: a section across the pin showing the two axle stubs, the gap each crosses and its bore

   The axle stands ``STUB_PROUD`` off each face of the tongue and has to cross the ``GAP`` to reach
   the bore. What is left is what holds the arm on. The slit runs through this section, so there
   is a stub on each leaf and nothing across the middle.

At 1.6 mm proud across a 0.6 mm gap, 1 mm of axle was engaged and 5.4 mm of bore was empty behind
it. That 1 mm was doing two jobs at once: it was everything holding an arm on, and it was the whole
distance the ear had to spread to let the tongue in.

**Settled: the axle is 1.30 mm proud and the gap at the seat is 0.15, so 1.15 is engaged.** The rule
that sets it is that the axle has to out-engage the tooth. A tooth needs the pair to open 0.45 mm to
leave its valley; if the axle were engaged by less than that, the joint would let go of the pin
before it let go of a detent and the tongue would walk out of the fork.

.. include:: tables/axle.rst

Keeping 1.30 mm buys 0.70 mm of margin over the climb. The gap cancels out of that difference, so
the margin is ``STUB_PROUD - TOOTH_PROUD`` exactly, and it is the same 0.70 mm that still holds the
axle when a hand turns the joint to a half step and twists it, which is how a joint that will not
come apart on a straight pull comes apart anyway. The bore is now a bore rather than a hole with an
axle resting in its mouth.

The axle cannot go much further than this. On the way in, the two leaves have to close by the whole
engagement before the axle clears its bore, and each millimeter at the pin closes the tongue's tips
by 3.28 mm into a 4 mm slit. At 1.374 mm proud the tips meet before the axle clears and the joint
will not go together at all; 1.30 leaves 0.24 mm of air, and that is the number the stand-off is
really limited by rather than by force or by stress.

No stand-off made the snap pressable, because the snap had to change kind
=========================================================================

Shortening the axle's stand-off is the obvious lever, because what the pair has to give is
``STUB_PROUD - GAP`` and the force goes straight through it. It was never enough on its own. With
the ear as the only spring, every stand-off worth having left a two-handed squeeze, four times over
on one robot.

The snap needed a change of kind, and it got two.

**The tongue is a spring as well.** A relief slit up its middle splits it into two leaves, and the
ear and the leaf are then springs in series: same force, sharing the movement in inverse proportion
to stiffness. A tongue with no slit in it is stiffer than the ear by two orders, so the ear gives
the whole climb on its own and the joint needs about 71 kgf.

.. include:: tables/slit.rst

The slit's width is a straight trade. A wider slit gives thinner leaves, which press easier and hold
less, and which snap sideways sooner. The last column is what it takes to break the tongue about its
weak axis with a hand 150 mm out from the elbow, which is a child picking the robot up by its
forearm.

**And the roots moved out.** Strength is a section property, so a longer root costs no strength at
all, while stiffness falls as its cube. That is what pays for a narrow slit: at roots 20 and 21 a
4.0 mm slit presses more easily than a 6.0 mm slit does at roots 16 and 17, and leaves the tongue
two and a half times stronger sideways.

Only two or three teeth carry, in either load case
==================================================

Pressing and turning are different questions and they do not share an answer.

.. figure:: images/wedge.png
   :class: fig
   :alt: the tongue part way in, holding the pair open as a wedge widest at its tip

   Pressing. The tongue goes in nose first and holds the pair open as a wedge, widest at its tip. A
   tooth back where the wedge is already wide is not touching anything, so the governing tooth is
   the last one in.

.. figure:: images/beams.png
   :class: fig
   :alt: the ear and the leaf as beams, with the tooth on the short lever lifting the rest clear

   Turning. The joint is seated, the axle is home in its bore carrying nothing, and every tooth is
   asked to climb at once. Three of them do, at two places along the beam, because the ring puts two
   teeth the same distance along it. The rest ride clear, because both members are beams: lifting
   the tooth on the short lever lifts everything outboard of it by more than that tooth's own
   climb.

.. figure:: images/stroke.png
   :class: fig
   :alt: the press force through the whole stroke, peaking where the axle reaches the bore

   The press force through the whole stroke. What a hand feels is the peak.

Adding the teeth up as independent springs overstates the press about eightfold, which is what the
old 36.3 kgf was. It also gave the detent hold as the press force times the tooth radius, which
mixes the two load cases together. Both are solved properly in ``src/stickbot/hinge_spring.py`` now.

The slot is one width, and the printer holds the fit down all of it
===================================================================

A 0.15 mm fit is what holds the joint square and stops the tongue rattling in the slot. The slot is
cut 10.3 mm from the fork's tip to its root, so the ear's whole inner face seats on the tongue and
the fit is 0.15 a side everywhere the two touch.

It was not always one width. The slot was cut 11.2 the whole way, which is an easy clearance to
print, with a raised land around the pin giving the 0.15 back just where the teeth need it: 20.8
long, the whole face across, 0.45 proud, ramped 0.45 in 1.2 at both ends. The argument for it was
that no printer holds 0.15 down 33 mm of slot wall, so only the 20.8 that matters should ask for it.
That argument was misleading, because it implied a benefit that turned out to be negligible when it
was analyzed, so the feature came out.

**Settled by Mike on 2026-09-02: the land comes out and the whole face comes forward to where it
was.** What that buys is a joint with no step in it anywhere; the tongue crosses nothing going in,
and one number describes the slot.

Nothing in ``src/stickbot/hinge_spring.py`` moves. It roots the ear at ``BLADE / 2 + GAP`` and has no term
for the relief, so it was already computing the joint that is now drawn; the relieved part was the
more compliant of the two, and the published press and hold figures were the land's.

The cone lands on a sharp rim, so the hold falls as the rim rounds
==================================================================

A tooth is a 45 degree cone with its point taken off 0.8 mm flat, and it drops into a straight
Ø1.7 mm hole through the ear. The flat is what sets how deep the detent is, and the hole is sized
with it so that the cone still stands 0.6 mm proud: a taller tooth would push the leaves further in
at a half step, and that is engagement taken straight back off the axle. What the cone bears on is the hole's rim, which is a sharp edge on a
part fresh off a printer and will not stay one.

.. figure:: images/rim.png
   :class: fig
   :alt: the cone seated on a new rim, on a rim rounded 0.05, and on a rim rounded 0.15

   A round of radius ρ on the rim lifts a 45 degree cone by √2·ρ, so the climb falls from 0.45 to
   ``0.45 - 1.414ρ``. At ρ 0.05 the joint holds 84% of new, at 0.10 it holds 69%, and at 0.15 it
   holds 53%.

Expect the first few cycles to crush the rim slightly and settle the hold lower than the new number.
Size the tooth for the worn figure. At 0.10 of round the joint still holds 311 N·mm, which is
twelve times what the arm's own weight asks of the elbow.

The two robot connectors were placed by two different rules
===========================================================

.. figure:: images/connectors.png
   :class: fig
   :alt: the fork's connector buried in its solid and the blade's flush on its end face

   Both connectors read back with ``evMateConnector``, in the hinge's own axes with the pin on the
   origin.

The blade's sits on its end face and points out of the part. The fork's sits ``NOSE`` from the pin,
15.4 mm short of its own end face and inside its own material, and points in. The two halves are
otherwise the same part turned around, and this was the one thing that stopped them being built the
same way: the fork needed Transform's flip in its limb where the blade did not, and the two
tutorials taught two different recipes for what is one idea.

**Settled: the fork's connector moves to its end face, pointing out, like the blade's.** That takes
the flip out of tutorial 10 and gives both limbs one rule to state.

draft9p3's blade connector landed on the tongue's root step
===========================================================

.. figure:: images/blade-connector.png
   :class: fig
   :alt: the reference connector on the blade's end face and draft9p3's on the tongue's root step

   The reference has it on the end face, on the axis. draft9p3 has it on the little step where the
   tongue meets its own limb, at that step's centroid, which is 7.884 mm off the axis and 6.4 mm
   short.

This one is a build defect rather than a design one, and it is the only finding on this page that
belongs to draft9p3 alone. ``stickbot-draft9p1p2`` builds the hinge again from the settled design,
so it is fixed by being rebuilt rather than repaired.

Both parts were still called Part 1 and Part 2
==============================================

In both documents. The page for tutorial 10 had to say "Part 2, which is the fork" three times, and
a student clicking a row in a list saw the same two words twice.

**Settled: the two parts are named** ``fork`` **and** ``blade``, one name each, and the tongue,
the ears and the leaves are named parts of them rather than parts in their own right.

The joint as it now stands
==========================

.. include:: tables/settled.rst

The weakest thing in the joint is still the tongue's weak axis, and it is now weaker than the fork's
two ears by two and a half times rather than by five and a half. Nothing in the joint is stressed
past 15 MPa against PETG's 50, at either load case.

What was left, and what the print answered
==========================================

``stickbot-draft9p1p2`` held the joint, and ``stickbot-draft9p1p4`` rebuilt it with the settled
axle. Four Part Studios and six parts: the fork and the blade in the mated position, an upper limb,
a lower limb, and a ball and socket coupon.
``.docs/experiments/runs/2026-08-30-draft9p1p2/check.py`` reads the model back and puts 29 rows
against the design; all 29 agree. Both limbs are exported as watertight STLs.

This section used to list three things the model could not answer. The first has been answered, and
it ended the joint:

- **the printed press force and the printed hold, measured against the 7.16 kgf and the 454 N·mm on
  this page, and whichever number is wrong is the model's, not the plastic's.** The printed joint
  held **210 N·mm**. The model is not wrong: the part is. A 45 degree cone dropping into a hole
  needs the hole empty, the slicer supports a hole bored through an ear, and the support cannot be
  reached to be picked out. Back the residue out of the measurement and 0.235 mm of it in each
  valley puts the hold where it landed, which is one extrusion width and exactly what a support
  interface leaves behind.
- how the hold really falls as the valley rims round off, against the 84, 69 and 53 percent above.
  Not answered, and now moot: there is no rim.
- whether the two can be brought together along a path a hand can take, which the ``hinge`` tab does
  not test. Not answered by the model, and answered by hand: they can, but not the way this page
  assumed. Pinching the two leaves together and sliding the tongue in is a different action from
  pressing the tongue down the slot, and it costs 39 N instead of 70.

What replaced it
================

A ring of wedges on each face, on the blade and on the ear alike, each a pie slice with 45 degree
sides standing 0.75 mm proud. A detent is one member's wedge sitting between two of the other's.
Nothing is bored, so nothing needs cleaning out, and the two faces no longer touch at all.

``stickbot-draft9p1p5`` put **12 wedges** on a face, 30 degrees apart, with the faces 1.00 mm apart.
It was printed on 8 Sep 2026 and it is good in the hand. ``draft9p1p6`` asks the same joint for a
15 degree step: **24 wedges**, the faces closed to 0.90 mm, the ring run right out to the limb's
flat, and the axle grown to 3.00 mm proud into a Ø4.1 mm bore. Everything below that names a number
is draft9p1p5's.

Three findings on this page survive the change unaltered, because they are about the members and
not the detent:

- only two or three teeth carry, in either load case, because both members are beams
- the free lengths are what make the joint assemblable, and a rod run on to the pin destroys them
- the tongue's weak axis is the weakest thing in the joint

Two are retired. **The cone lands on a sharp rim** has nothing left to land on. **The slot is one
width and the printer holds the fit down all of it** was true of a fit; there is no fit now, only a
space a wedge stands in.

One is turned over. This page treats the press force as the constraint that sizes the joint, and
argues that no stand-off makes it pressable. That is right about pressing and wrong about assembly:
the leaves can simply be pinched. The joint is now sized on a pinch, and the numbers are in the two
run plans. draft9p1p5, on a 40 N budget: 490 N·mm at a detent, 1018 N·mm with friction on the 45
degree flanks, 39.2 N to pinch together, 923 N·mm to wring apart. draft9p1p6, on a 100 N budget:
641 N·mm, 1332 N·mm, 75.2 N, 1889 N·mm. See
``.docs/experiments/runs/2026-09-04-draft9p1p5/plan.md`` and
``.docs/experiments/runs/2026-09-08-draft9p1p6/plan.md``.

The two arguments this page never had to make, and the new joint does, are printability of a
protrusion instead of a hole, and backlash. Two pie slices cannot mesh without room to miss each
other, so draft9p1p5 has 2.41 degrees of play at a detent and draft9p1p6 has 2.29. Backlash is set
by the printer's error and a radius, not by the pitch, so halving the step barely moved it and
doubled it as a share of one step, from 8 percent to 15. That is the price of a joint that goes
together at all, and it is paid.

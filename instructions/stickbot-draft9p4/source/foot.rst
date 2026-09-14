The foot, a shape with no corners
==================================

Every part so far has been a box, a cylinder or a ball. The foot is none of those. Its outline is
two circles of different sizes joined by two straight lines, and the lines run tangent to both
circles, so the shape turns from end to end without ever having a corner. Underneath it there is
tread: one groove cut across the sole and then repeated the length of the foot.

The page ends by bringing the socket across from the ``ball and socket`` tab, the same way the head
did, and joining it on.

.. step: cad.hero
.. req: req.page.hero

Here is what you are building. From a corner, with **shift+7**, the foot reads as a shape that
turns from heel to toe without a corner anywhere on it.

.. image:: images/foot/hero-01.png
   :alt: the finished foot from a corner: a rounded heel behind, a wider toe in front, the top edge
         rounded the whole way round, and the socket standing on its pedestal in the middle
   :class: shot

From underneath, with **shift+5**, the tread shows. The sole is the side of this part you will
spend the most time looking at, and the only way to see it is to ask for it.

.. image:: images/foot/hero-02.png
   :alt: the same foot from below, eight grooves across the sole with land left at the toe and at
         the heel
   :class: shot

This page adds thirteen numbers, and none of them is in ``robot sizes``. A foot is not measured
against the rest of the robot. It is measured against the ground. Each number goes in right before
the feature that reads it, so you will meet them a few at a time instead of all at once.

Make a Part Studio for the foot
--------------------------------

.. step: cad.parts.foot.tab
.. req: req.model.one_document

Open the ``ball and socket`` tab first. A new tab goes in beside the one you are on, so starting
here puts the foot at the end of the strip.

Click the **+** at the bottom left of the tab strip and choose **Create Part Studio**.

.. image:: images/foot/parts.foot.tab-01.png
   :alt: the tab strip's plus menu open, with Create Part Studio above Create Assembly
   :class: shot

The new studio opens empty, with ``Default geometry`` and nothing else.

.. image:: images/foot/parts.foot.tab-02.png
   :alt: the new empty Part Studio, its tab called Part Studio 1 and its feature list holding only
         Default geometry
   :class: shot

Right-click the new tab, choose **Rename**, and type ``foot``.

.. image:: images/foot/parts.foot.tab-03.png
   :alt: the tab strip with foot at the end of it
   :class: shot

The radius the pedestal has to match
-------------------------------------

.. step: cad.parts.foot.collar_variable
.. req: req.model.derive

The socket will stand on a small disc called the pedestal, and the disc has to be exactly as wide as
the socket's collar. Open **Variable** and add one row.

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``collar_r``
     - ``#ball / 2 + #wall``
     - the socket's outside radius, 7.8 mm

The dialog arrives on **Length**. Leave the type alone; every row on this page is a length. The
title at the top of the dialog does the arithmetic for you as you type, so you can read the answer
before you accept it.

.. image:: images/foot/parts.foot.collar_variable-01.png
   :alt: the Variable dialog in the foot tab, its title reading #collar_r = 7.8 mm, collar_r in the
         Name box and #ball / 2 + #wall in the Value box
   :class: shot

One row stands in the feature list, under ``Default geometry``.

.. image:: images/foot/parts.foot.collar_variable-02.png
   :alt: the foot's feature list with one row under Default geometry, reading #collar_r = 7.8 mm
   :class: shot

.. admonition:: Write the rule, not the answer
   :class: advice

   ``#ball / 2 + #wall`` reads 7.8 mm today. Typing ``7.8 mm`` would read the same today and be
   wrong the moment the robot changes size, because the pedestal would stay 15.6 mm across while the
   socket around it grew. The socket is built from those same two rows, so the disc under it should
   be too.

Draw the pedestal's circle
---------------------------

.. step: cad.parts.foot.pedestal_sketch
.. req: req.model.design_intent
.. req: req.model.anchored

The foot is built from the ankle down, so the first thing drawn is the small disc the socket will
stand on. Pick the ``Top`` plane in the feature list and open **Sketch**.

.. image:: images/foot/parts.foot.pedestal_sketch-01.png
   :alt: the Top plane picked in the feature list, the floor everything on this page is drawn on
   :class: shot

Name the sketch ``pedestal outline`` in the dialog before you draw anything.

.. image:: images/foot/parts.foot.pedestal_sketch-02.png
   :alt: the sketch dialog titled pedestal outline, its plane field reading Top
   :class: shot

Press **n** to look **n**ormal to the plane. Open **Circle** and put the pointer on the origin.
Start the circle on the origin point itself. Onshape adds a coincident constraint as you draw, and
that is what holds the circle there.

.. image:: images/foot/parts.foot.pedestal_sketch-03.png
   :alt: the circle tool armed, the pointer on the origin
   :class: shot

Draw it about the right size. The dimension is what makes it exact.

.. image:: images/foot/parts.foot.pedestal_sketch-04.png
   :alt: a circle centered on the origin, drawn about the right size and not yet dimensioned
   :class: shot

Open **Dimension**, click the circle, and type ``2 * #collar_r``. It reads 15.6 mm, and the circle
turns black. Black means fully defined: the dimension gives it its size and the origin gives it its
place, so nothing about it can move.

.. image:: images/foot/parts.foot.pedestal_sketch-05.png
   :alt: the circle black and fully defined, 15.6 mm across
   :class: shot

Accept the sketch. It goes into the feature list under ``#collar_r``, which is the row it reads.

.. image:: images/foot/parts.foot.pedestal_sketch-06.png
   :alt: the feature list with pedestal outline under #collar_r, and one small circle round the
         origin
   :class: shot

Three numbers for the plate
----------------------------

.. step: cad.parts.foot.plate_variables
.. req: req.model.derive
.. req: req.page.typed_values

The extrude that turns that circle into a disc needs three numbers, and they are one chain: the last
is the first two subtracted. Add them in this order.

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``plate``
     - ``12 mm``
     - how deep the plate around the ankle is
   * - ``collar_down``
     - ``#collar``
     - how far the socket hangs below the middle of its ball, 10 mm
   * - ``pedestal``
     - ``#plate - #collar_down``
     - what is left of the plate underneath, 2 mm

``#plate`` is the one thickness on this page that is typed. It is a printing decision, not a
fraction of the robot.

.. image:: images/foot/parts.foot.plate_variables-01.png
   :alt: the Variable dialog with plate in the Name box and 12 mm in the Value box, the one
         thickness on this page that is typed
   :class: shot

``#pedestal`` is worked out from the two rows above it. Write the subtraction rather than the
answer, and the disc follows both numbers if either one changes.

.. image:: images/foot/parts.foot.plate_variables-02.png
   :alt: pedestal in the Name box and #plate - #collar_down in the Value box, its title reading
         #pedestal = 2 mm, a number worked out from two rows above it
   :class: shot

The three new rows go in under ``pedestal outline``, which is where you were standing when you typed
them.

.. image:: images/foot/parts.foot.plate_variables-03.png
   :alt: the feature list with plate, collar_down and pedestal added under pedestal outline
   :class: shot

Extrude the pedestal
---------------------

.. step: cad.parts.foot.pedestal
.. req: req.model.named_features

Press **shift+7** to look from a corner, where a disc reads as a disc rather than a circle. Then
open **Extrude**. It arrives on **Solid** and **New**, with its region field empty. **New** is right
here: this is the foot's first part, so there is nothing yet for it to join.

.. image:: images/foot/parts.foot.pedestal-01.png
   :alt: the Extrude dialog open on Solid and New, its region field empty and waiting
   :class: shot

Click ``pedestal outline`` in the feature list. Picking the sketch by name takes the whole sketch,
which is what you want when the sketch holds one region.

.. image:: images/foot/parts.foot.pedestal-02.png
   :alt: pedestal outline picked in the feature list, its name now in the Extrude dialog's region
         field
   :class: shot

Type ``#pedestal`` into **Depth**.

.. image:: images/foot/parts.foot.pedestal-03.png
   :alt: #pedestal typed into the Depth box, reading 2 mm, which is what is left of the plate under
         the collar
   :class: shot

Tick **Starting offset** and type ``#collar_down`` into it. That is what moves the disc down to
where the socket's collar stops.

.. image:: images/foot/parts.foot.pedestal-04.png
   :alt: Starting offset ticked and #collar_down typed into it, reading 10 mm, so the disc begins
         where the socket's collar ends
   :class: shot

Both distances go the wrong way to start with. An extrude grows up from its sketch, and this disc
belongs underneath. Click the **Opposite direction** arrow beside the depth.

.. image:: images/foot/parts.foot.pedestal-05.png
   :alt: the Opposite direction arrow beside the depth clicked, so the disc grows down away from the
         floor instead of up into it
   :class: shot

Click the **Opposite direction** arrow on the starting offset's own row too. Each distance carries
its own arrow, and each one has to be turned.

.. image:: images/foot/parts.foot.pedestal-06.png
   :alt: the Opposite direction arrow on the starting offset's own row clicked, so the disc starts
         below the floor as well
   :class: shot

Click the pencil beside the dialog's title and type ``foot pedestal`` there before you accept it.

.. image:: images/foot/parts.foot.pedestal-07.png
   :alt: foot pedestal typed into the Extrude dialog's name box
   :class: shot

A disc 15.6 mm across stands under the ``Top`` plane, from 12 mm down to 10 mm down. It is the
foot's first part.

.. image:: images/foot/parts.foot.pedestal-08.png
   :alt: a disc 15.6 mm across standing under the Top plane, the foot's first part
   :class: shot

Five numbers for the outline
-----------------------------

.. step: cad.parts.foot.outline_variables
.. req: req.model.derive

The outline is two circles, so it needs a size for each and a place to put them. One sketch reads
all five of these, so all five go in together.

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``foot_l``
     - ``#torsoH``
     - heel to toe, 96 mm
   * - ``foot_w``
     - ``#torsoH / 2``
     - across the widest part, 48 mm
   * - ``heel_r``
     - ``#foot_w / 3``
     - the heel circle's radius, 16 mm
   * - ``toe_r``
     - ``#foot_w / 2``
     - the toe circle's radius, 24 mm
   * - ``heel_y``
     - ``#foot_l / 3``
     - how far the heel reaches behind the ankle, 32 mm

A foot as long as the torso is tall sounds like a lot. It is what keeps the robot standing up
instead of tipping over.

.. image:: images/foot/parts.foot.outline_variables-01.png
   :alt: foot_l in the Name box and #torsoH in the Value box, so the foot is as long as the torso is
         tall
   :class: shot

The heel is a third of the foot's width across its radius and the toe is half. That difference is
the whole shape.

.. image:: images/foot/parts.foot.outline_variables-02.png
   :alt: heel_r in the Name box and #foot_w / 3 in the Value box, which makes the heel noticeably
         smaller than the toe
   :class: shot

``#heel_y`` puts the back of the heel a third of the foot's length behind the ankle, which leaves
the other two thirds in front for the toe.

.. image:: images/foot/parts.foot.outline_variables-03.png
   :alt: heel_y in the Name box and #foot_l / 3 in the Value box, which puts the back of the heel a
         third of the foot's length behind the ankle
   :class: shot

The five new rows sit under ``foot pedestal``, not with the three before them. Variables are read in
tree order, so a row has to stand above the feature that reads it.

.. image:: images/foot/parts.foot.outline_variables-04.png
   :alt: the feature list with foot_l, foot_w, heel_r, toe_r and heel_y added under foot pedestal
   :class: shot

Draw the foot's outline
------------------------

.. step: cad.parts.foot.outline_sketch
.. req: req.model.design_intent
.. req: req.page.view_keys

Pick ``Top`` again and open a second sketch on it. The pedestal is already there, under the plane.

.. image:: images/foot/parts.foot.outline_sketch-01.png
   :alt: the Top plane picked in the feature list again, the same floor the pedestal was drawn on
   :class: shot

Name it ``foot outline``, then press **n** to look **n**ormal to the plane. You are looking straight
down at the sketch with the disc below it.

.. image:: images/foot/parts.foot.outline_sketch-02.png
   :alt: the sketch dialog titled foot outline, its plane field reading Top
   :class: shot

Draw two circles on the vertical axis. A small one above the origin is the heel. A bigger one below
it is the toe. Start each circle on the axis itself, so neither can drift sideways later.

.. image:: images/foot/parts.foot.outline_sketch-03.png
   :alt: two circles on the vertical axis, a small one above the origin for the heel and a bigger
         one below it for the toe, both loose
   :class: shot

Dimension the heel circle across at ``2 * #heel_r``.

.. image:: images/foot/parts.foot.outline_sketch-04.png
   :alt: the heel circle dimensioned across at 2 * #heel_r, reading 32 mm
   :class: shot

Dimension the toe circle across at ``#foot_w``. This is the one place the foot's width is set, and
it says the widest part of the foot is the toe.

.. image:: images/foot/parts.foot.outline_sketch-05.png
   :alt: the toe circle dimensioned across at #foot_w, reading 48 mm, so the widest part of the foot
         is the toe
   :class: shot

Now place them. Dimension the heel circle's center up from the origin at ``#heel_y - #heel_r``. The
subtraction is what makes ``#heel_y`` mean the back of the heel rather than its middle.

.. image:: images/foot/parts.foot.outline_sketch-06.png
   :alt: the heel circle's center dimensioned up from the origin at #heel_y - #heel_r, reading 16 mm
   :class: shot

Dimension the toe circle's center down from the origin at ``#foot_l - #heel_y - #toe_r``. Both
circles are now sized and placed.

.. image:: images/foot/parts.foot.outline_sketch-07.png
   :alt: the toe circle's center dimensioned down from the origin at #foot_l - #heel_y - #toe_r,
         reading 40 mm
   :class: shot

Open **Line** and lay one line from the heel circle down to the toe circle on each side. Draw them
roughly; the constraints come next.

.. image:: images/foot/parts.foot.outline_sketch-08.png
   :alt: two lines laid from the heel circle down to the toe circle, one each side, drawn roughly
         and leaning
   :class: shot

Hold each line tangent to both circles: pick the line and one circle, apply **Tangent**, then the
same line and the other circle. A line that touches two circles and leans on neither is what makes
the side of the foot run smooth.

.. image:: images/foot/parts.foot.outline_sketch-09.png
   :alt: both lines now held tangent to the heel circle as well as the toe, so neither can swing
   :class: shot

Open **Trim** and click the inside half of each circle. What is left is a closed outline: a heel
arc, two straight sides and a toe arc.

.. image:: images/foot/parts.foot.outline_sketch-10.png
   :alt: the finished outline: a heel arc, a toe arc and two straight sides, with the inside arcs
         trimmed away
   :class: shot

Accept it. ``foot outline`` goes into the list under the five numbers it reads.

.. image:: images/foot/parts.foot.outline_sketch-11.png
   :alt: foot outline in the feature list, and the closed outline drawn over the pedestal's disc
   :class: shot

.. admonition:: A dimension moves what it has not pinned yet
   :class: advice

   Set the heel's diameter and the toe circle jumps down the axis, because nothing is holding it
   where you drew it. That is the sketch solver doing its job, not a mistake.

   It means you should look for a circle where it is now rather than where you drew it. By the
   fourth dimension both circles have stopped moving, because by then both are sized and both are
   placed.

How high the ankle stands
--------------------------

.. step: cad.parts.foot.ankle_variable
.. req: req.model.derive

One more number before the foot itself: how far the middle of the ankle's ball sits above the
ground.

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``ankle_h``
     - ``#torsoH / 4``
     - ground to the middle of the ball, 24 mm

.. image:: images/foot/parts.foot.ankle_variable-01.png
   :alt: ankle_h in the Name box and #torsoH / 4 in the Value box, its title reading #ankle_h = 24
         mm, which is how high off the ground the ankle's ball sits
   :class: shot

It goes in under ``foot outline``, and the extrude that reads it comes next.

.. image:: images/foot/parts.foot.ankle_variable-02.png
   :alt: the feature list with ankle_h added under foot outline
   :class: shot

Extrude the foot
-----------------

.. step: cad.parts.foot.body
.. req: req.model.named_features

Press **shift+7** for the corner view again and open **Extrude**. It arrives on **New**, the same
way it did last time.

.. image:: images/foot/parts.foot.body-01.png
   :alt: the Extrude dialog open on New again, with the region field empty
   :class: shot

Click **Add**. That is the change that matters here: the foot joins the pedestal, so the tab still
holds one part instead of two.

.. image:: images/foot/parts.foot.body-02.png
   :alt: Add picked instead of New, so the foot joins the pedestal rather than standing beside it as
         a second part
   :class: shot

Click ``foot outline`` in the feature list.

.. image:: images/foot/parts.foot.body-03.png
   :alt: foot outline picked in the feature list, its name now in the Extrude dialog's region field
   :class: shot

Type ``#ankle_h - #plate`` into **Depth**. It is the ankle's height less the plate above it.

.. image:: images/foot/parts.foot.body-04.png
   :alt: #ankle_h - #plate typed into the Depth box, reading 12 mm, the ankle's height less the
         plate above it
   :class: shot

Tick **Starting offset** and type ``#plate``, which starts the foot at the bottom of the plate.

.. image:: images/foot/parts.foot.body-05.png
   :alt: Starting offset ticked and #plate typed into it, reading 12 mm, so the foot starts at the
         bottom of the plate
   :class: shot

Turn both directions, the same pair of arrows as before. The depth first.

.. image:: images/foot/parts.foot.body-06.png
   :alt: the Opposite direction arrow beside the depth clicked, so the foot grows down toward the
         ground
   :class: shot

Then the starting offset.

.. image:: images/foot/parts.foot.body-07.png
   :alt: the Opposite direction arrow on the starting offset's row clicked as well, so the foot
         starts under the floor rather than above it
   :class: shot

Name it ``foot``.

.. image:: images/foot/parts.foot.body-08.png
   :alt: foot typed into the Extrude dialog's name box
   :class: shot

The foot stands under the pedestal, one part, reaching from 12 mm below the plane down to 24 mm
below it. That bottom face is the ground the robot stands on.

.. image:: images/foot/parts.foot.body-09.png
   :alt: the foot standing under the pedestal, one part, with a rounded heel behind and a wider toe
         in front
   :class: shot

The radius that rounds the top
-------------------------------

.. step: cad.parts.foot.round_variable
.. req: req.model.derive

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``top_round``
     - ``8 mm``
     - the radius on the foot's top edge

This one is typed. How round the top of a foot looks is a choice, not a fraction of anything.

.. image:: images/foot/parts.foot.round_variable-01.png
   :alt: top_round in the Name box and 8 mm in the Value box, the radius that rounds the foot's top
         edge
   :class: shot

It goes in under ``foot``.

.. image:: images/foot/parts.foot.round_variable-02.png
   :alt: the feature list with top_round added under foot
   :class: shot

Round the top edge
-------------------

.. step: cad.parts.foot.top_round
.. req: req.model.named_features

Press **shift+7** and open **Fillet**. It waits for an edge.

.. image:: images/foot/parts.foot.top_round-01.png
   :alt: the Fillet dialog open with its edge field empty and waiting
   :class: shot

Click one edge of the foot's top. The whole way round lights up with it, because the arcs and the
straight sides meet tangent and Onshape follows a tangent chain as one edge. The work you did in the
sketch is paying off here.

.. image:: images/foot/parts.foot.top_round-02.png
   :alt: one edge of the foot's top picked, and the whole way round lit up with it, because the arcs
         and the straight sides meet tangent
   :class: shot

Type ``#top_round`` into **Radius**.

.. image:: images/foot/parts.foot.top_round-03.png
   :alt: #top_round typed into the Radius box, reading 8 mm
   :class: shot

Name it ``top round``.

.. image:: images/foot/parts.foot.top_round-04.png
   :alt: top round typed into the Fillet dialog's name box
   :class: shot

The top edge is rounded the whole way round, in one feature.

.. image:: images/foot/parts.foot.top_round-05.png
   :alt: the top edge rounded the whole way round the foot, in one feature
   :class: shot

How wide one groove is
-----------------------

.. step: cad.parts.foot.groove_width_variable
.. req: req.model.derive

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``rib_w``
     - ``6 mm``
     - how wide one groove in the sole is

.. image:: images/foot/parts.foot.groove_width_variable-01.png
   :alt: rib_w in the Name box and 6 mm in the Value box, how wide one groove in the sole is
   :class: shot

It goes in under ``top round``, and the sketch that reads it comes next.

.. image:: images/foot/parts.foot.groove_width_variable-02.png
   :alt: the feature list with rib_w added under top round
   :class: shot

Draw one groove
----------------

.. step: cad.parts.foot.groove_sketch
.. req: req.model.design_intent
.. req: req.page.view_keys

The tread is one cut, repeated. Draw the cut once, at the toe end, and the pattern later does the
rest. Pick ``Top`` and open a third sketch on it.

.. image:: images/foot/parts.foot.groove_sketch-01.png
   :alt: the Top plane picked in the feature list a third time
   :class: shot

Name it ``groove profile``, then press **n** to look **n**ormal to the plane again.

.. image:: images/foot/parts.foot.groove_sketch-02.png
   :alt: the sketch dialog titled groove profile, its plane field reading Top
   :class: shot

Open the arrow beside the rectangle button and choose **Center point rectangle**, the one the torso
used.

.. image:: images/foot/parts.foot.groove_sketch-03.png
   :alt: the arrow beside the rectangle button open, with Center point rectangle on the menu
   :class: shot

Draw one rectangle across the toe end of the sole, starting on the vertical axis. Let it run off
both sides of the foot. A cut that starts and ends outside the part leaves a clean slot, with no
thin sliver of material at either end.

.. image:: images/foot/parts.foot.groove_sketch-04.png
   :alt: one rectangle drawn across the toe end of the sole, starting on the vertical axis and
         running off the foot on both sides
   :class: shot

Dimension it across at ``2 * #foot_w``. That is twice the width of the foot, which is what runs it
clean off both sides however wide the foot becomes.

.. image:: images/foot/parts.foot.groove_sketch-05.png
   :alt: the rectangle dimensioned across at 2 * #foot_w, reading 96 mm, twice the width of the foot
   :class: shot

Dimension it along the foot at ``#rib_w``.

.. image:: images/foot/parts.foot.groove_sketch-06.png
   :alt: the rectangle dimensioned along the foot at #rib_w, reading 6 mm, which is how wide one
         groove is
   :class: shot

Dimension the far edge from the origin at ``#foot_l - #heel_y - #rib_w / 2``. The toe reaches 64 mm
past the origin, so this leaves half a groove's width of land right at the tip.

.. image:: images/foot/parts.foot.groove_sketch-07.png
   :alt: the far edge dimensioned from the origin at #foot_l - #heel_y - #rib_w / 2, reading 61 mm,
         which leaves half a groove's width of land at the tip of the toe
   :class: shot

Accept it.

.. image:: images/foot/parts.foot.groove_sketch-08.png
   :alt: the feature list with groove profile in it, and one rectangle lying across the toe end of
         the sole
   :class: shot

How deep the groove is cut
---------------------------

.. step: cad.parts.foot.groove_depth_variable
.. req: req.model.derive

.. list-table::
   :header-rows: 1
   :widths: 26 40 34

   * - Name
     - Value
     - What it is
   * - ``rib_d``
     - ``2 mm``
     - how deep the groove is cut into the sole

.. image:: images/foot/parts.foot.groove_depth_variable-01.png
   :alt: rib_d in the Name box and 2 mm in the Value box, how deep the groove is cut
   :class: shot

It goes in under ``groove profile``. The sketch drew the groove's width; this is the only number the
cut adds.

.. image:: images/foot/parts.foot.groove_depth_variable-02.png
   :alt: the feature list with rib_d added under groove profile
   :class: shot

Cut the groove
---------------

.. step: cad.parts.foot.groove
.. req: req.model.named_features
.. req: req.page.view_keys

Press **shift+7** and open **Extrude** once more.

.. image:: images/foot/parts.foot.groove-01.png
   :alt: the Extrude dialog open on New, with the region field empty
   :class: shot

Set it to **Remove**. That is the third of the three buttons you have used on this page: **New**
made a part, **Add** joined one, and **Remove** takes material out.

.. image:: images/foot/parts.foot.groove-02.png
   :alt: Remove picked, the third of the three buttons this page uses: New made a part, Add joined
         one, and Remove takes material out
   :class: shot

Click ``groove profile`` in the feature list.

.. image:: images/foot/parts.foot.groove-03.png
   :alt: groove profile picked in the feature list, its name now in the Extrude dialog's region
         field
   :class: shot

Type ``#rib_d`` into **Depth**.

.. image:: images/foot/parts.foot.groove-04.png
   :alt: #rib_d typed into the Depth box, reading 2 mm, which is how deep the groove is cut
   :class: shot

Tick **Starting offset** and type ``#ankle_h - #rib_d``. Together the two say: begin 22 mm under the
sketch and take the last 2 mm off the sole.

.. image:: images/foot/parts.foot.groove-05.png
   :alt: Starting offset ticked and #ankle_h - #rib_d typed into it, reading 22 mm, so the cut
         begins 22 mm under the sketch and takes the last 2 mm off the sole
   :class: shot

Turn both arrows, so the cut runs down toward the sole rather than up into the foot.

.. image:: images/foot/parts.foot.groove-06.png
   :alt: both Opposite direction arrows clicked, so the cut runs down toward the sole rather than up
         into the foot
   :class: shot

Name it ``sole groove``.

.. image:: images/foot/parts.foot.groove-07.png
   :alt: sole groove typed into the Extrude dialog's name box
   :class: shot

One slot is cut across the toe end.

.. image:: images/foot/parts.foot.groove-08.png
   :alt: the foot with one slot cut right across the toe end of the sole
   :class: shot

Press **shift+5** to look from underneath. The sole is where the rest of this page happens, and it
is the side you cannot see from any of the other views.

.. image:: images/foot/parts.foot.groove-09.png
   :alt: the sole seen from below, with one slot cut clean across it from side to side
   :class: shot

Repeat the groove down the sole
--------------------------------

.. step: cad.parts.foot.ribs
.. req: req.model.named_features
.. req: req.page.view_keys

Stay looking at the sole, with **shift+5**, so you can watch the copies arrive.

.. image:: images/foot/parts.foot.ribs-01.png
   :alt: the sole from below with one slot in it, before the pattern
   :class: shot

Open **Linear pattern**. It arrives on **Part pattern**.

.. image:: images/foot/parts.foot.ribs-02.png
   :alt: the Linear pattern dialog open on Part pattern, its boxes empty
   :class: shot

**Part pattern** is a dropdown. Open it and choose **Feature pattern**.

.. image:: images/foot/parts.foot.ribs-03.png
   :alt: the pattern dropdown open, with Feature pattern under Part pattern
   :class: shot

That is the choice that matters here. A feature pattern repeats the cut itself, so every copy is a
real cut into whatever is under it, and the pattern still works if the foot's shape changes.

.. image:: images/foot/parts.foot.ribs-04.png
   :alt: Feature pattern picked instead of Part pattern, so the cut itself is what repeats
   :class: shot

Click ``sole groove`` in the feature list as the feature to repeat.

.. image:: images/foot/parts.foot.ribs-05.png
   :alt: sole groove picked in the feature list as the feature to repeat
   :class: shot

Click into the **Direction** box, then click the ``Front`` plane in the feature list. A plane gives
a direction by its normal, and ``Front`` points along the length of the foot, which is the way the
copies have to march.

.. image:: images/foot/parts.foot.ribs-06.png
   :alt: the Front plane picked for the direction; a plane gives a direction by its normal, and
         Front points along the length of the foot
   :class: shot

Type ``2 * #rib_w`` into **Distance**: two groove widths, so a rib as wide as a slot is left between
one slot and the next. Type ``#foot_l / (2 * #rib_w)`` into **Instance count**, which is how many of
those fit in the foot's length.

.. image:: images/foot/parts.foot.ribs-07.png
   :alt: 2 * #rib_w typed into Distance, reading 12 mm, and #foot_l / (2 * #rib_w) typed into
         Instance count, reading 8
   :class: shot

Tick **Reapply features**. It arrives unticked, and unticked every copy after the first one fails,
because a copy has to cut into what the copies before it left.

.. image:: images/foot/parts.foot.ribs-08.png
   :alt: Reapply features ticked, which is what lets each copy cut into what the copies before it
         left
   :class: shot

Click the **Opposite direction** arrow beside **Instance count**.

.. image:: images/foot/parts.foot.ribs-09.png
   :alt: the Opposite direction arrow clicked, so the copies march from the toe back toward the heel
         and stay on the foot
   :class: shot

Name it ``sole ribs``.

.. image:: images/foot/parts.foot.ribs-10.png
   :alt: sole ribs typed into the Linear pattern dialog's name box
   :class: shot

The sole is ribbed the whole length of the foot, and there is land left at both ends. That is the
half groove width the toe dimension left over, arriving at the heel as well.

.. image:: images/foot/parts.foot.ribs-11.png
   :alt: the sole ribbed the whole length of the foot, with land left at both ends
   :class: shot

.. admonition:: A pattern that goes the wrong way looks like a pattern that did nothing
   :class: advice

   Point the copies at the toe instead of the heel and they all land past the end of the foot, where
   there is nothing to cut. The sole comes back with the one groove it started with, and no feature
   turns red to tell you.

   Count the slots. Eight is the answer here, and eight is what ``#foot_l / (2 * #rib_w)`` works
   out to.

Bring the socket across
------------------------

.. step: cad.parts.foot.socket.derive
.. req: req.model.derive

Press **shift+7** to see the pedestal again. The foot needs the socket half of the joint, and the
socket already exists in the ``ball and socket`` tab. Nobody draws it twice. **Derived** brings a
linked copy of it into this tab, the same way the head got its socket. It has no button on the
toolbar, so open it from the **Search tools** box at the right-hand end of the toolbar.

.. image:: images/foot/parts.foot.socket.derive-01.png
   :alt: the Derived dialog open, its Select Part Studio button red and empty, Placement reading
         Base origin and both tick boxes ticked
   :class: shot

Click the Part Studio button. A panel opens listing this document's studios.

.. image:: images/foot/parts.foot.socket.derive-02.png
   :alt: the Select Part Studio panel open on Current document, listing the other Part Studios in it
   :class: shot

Open ``ball and socket`` by the caret at the left of its row. Clicking the name itself picks the
whole studio, which brings both of its parts across.

.. image:: images/foot/parts.foot.socket.derive-03.png
   :alt: the ball and socket studio opened by its caret, listing its parts, with the Derived dialog
         still red and empty
   :class: shot

Pick ``Socket body``, and only that.

.. image:: images/foot/parts.foot.socket.derive-04.png
   :alt: Socket body picked in the panel, the Derived dialog now reading ball and socket, and the
         parts list behind it gaining a second part
   :class: shot

Close the panel. Leave **Placement** on **Base origin** and leave **Include mate connectors**
ticked. Base origin is what saves you a move: the socket was drawn around its own origin, and so was
the pedestal, so the socket arrives sitting where it belongs.

.. image:: images/foot/parts.foot.socket.derive-05.png
   :alt: the Derived dialog with ball and socket in its Part Studio box, Placement on Base origin
         and Include mate connectors ticked
   :class: shot

Name it ``add socket``.

.. image:: images/foot/parts.foot.socket.derive-06.png
   :alt: add socket typed into the dialog's name box
   :class: shot

The socket is standing on the foot's pedestal, and nothing was moved to put it there.

.. image:: images/foot/parts.foot.socket.derive-07.png
   :alt: the socket standing on the foot's pedestal, where Base origin put it, with nothing moved to
         get it there
   :class: shot

Make them one part
-------------------

.. step: cad.parts.foot.combine
.. req: req.model.named_features

Two solids that touch are still two parts, and a printer would print two. Press **shift+7** and open
**Boolean**. It arrives on **Union**.

.. image:: images/foot/parts.foot.combine-01.png
   :alt: the Boolean dialog open on Union with its Parts box empty, and the two solids still
         separate
   :class: shot

Click both parts in the parts list.

.. image:: images/foot/parts.foot.combine-02.png
   :alt: both parts picked into the Boolean's box
   :class: shot

Name it ``combine parts``.

.. image:: images/foot/parts.foot.combine-03.png
   :alt: combine parts typed into the Boolean dialog's name box
   :class: shot

The parts list holds one part where it held two.

.. image:: images/foot/parts.foot.combine-04.png
   :alt: one part in the parts list where there were two, with the socket now part of the foot
   :class: shot

.. admonition:: Check that Keep tools is unticked
   :class: advice

   Boolean remembers what you left it at last time. Ticked, it leaves the two solids standing and
   adds a third made out of them, which is three parts where you wanted one.

   It arrived unticked here, because the last Boolean before this one left it that way. Look at the
   box rather than trusting it.

Name the part
--------------

.. step: cad.parts.foot.rename
.. req: req.model.named_features

The part is still called ``Part 1``. Renaming a part is not a feature and never appears in the
feature list, which is why it is easy to forget.

.. image:: images/foot/parts.foot.rename-01.png
   :alt: the parts list holding one part, still called Part 1
   :class: shot

Double-click the name and type ``Foot``. The assembly pages insert parts by name, and ``Foot`` with
a capital F is the name they look for.

.. image:: images/foot/parts.foot.rename-02.png
   :alt: the parts list holding one part called Foot, with a capital F, which is the name the
         assembly pages look for
   :class: shot

Put a mate connector on it
---------------------------

.. step: cad.parts.foot.connector
.. req: req.model.named_features

The foot needs one connector for the assembly to mate the leg to. Press **shift+7** and open **Mate
connector**. It waits with **Origin entity** empty.

.. image:: images/foot/parts.foot.connector-01.png
   :alt: the Mate connector dialog open with Origin entity empty and waiting
   :class: shot

Click ``Origin`` in the feature list, at the top under ``Default geometry``. The socket was built
around that point, and so was the pedestal, so the origin is already the middle of the joint.
Picking it says *put the connector where the joint is*, with nothing to measure.

.. image:: images/foot/parts.foot.connector-02.png
   :alt: Origin picked at the top of the feature list, under Default geometry; the socket and the
         pedestal were both built around that point, so it is already the middle of the joint
   :class: shot

One pick fills three things. **Origin entity** reads ``Vertex of Origin``, **Owner entity** fills
itself with ``Foot``, and **Attachment** goes to **To owner**. Owner is the one that matters most. A
connector with an owner belongs to the part and goes with it into the assembly. One without an owner
exists only in this tab.

.. image:: images/foot/parts.foot.connector-03.png
   :alt: one pick filling three boxes: Origin entity reading Vertex of Origin, Owner entity filled
         with Foot, and Attachment on To owner
   :class: shot

Open the **Attachment** dropdown and choose **To selection**, which opens an **Attach to** box.

.. image:: images/foot/parts.foot.connector-04.png
   :alt: the Attachment dropdown open, with To selection under To owner
   :class: shot

Click ``Foot`` in the parts list to fill it. Naming the part in both boxes says plainly what the
connector is attached to.

.. image:: images/foot/parts.foot.connector-05.png
   :alt: Foot picked in the parts list to fill the Attach to box, so both boxes name the part the
         connector belongs to
   :class: shot

Name it ``mate to robot``.

.. image:: images/foot/parts.foot.connector-06.png
   :alt: mate to robot typed into the dialog's name box
   :class: shot

Three small arrows stand in the middle of the socket's ball, at the origin, and ``mate to robot`` is
the last row in the feature list. The assembly page will pick this row by name.

.. image:: images/foot/parts.foot.connector-07.png
   :alt: mate to robot the last row in the tree, its three arrows standing at the middle of the
         socket's ball
   :class: shot

.. admonition:: The parts list and the feature list fill different boxes
   :class: advice

   Clicking a part in the parts list fills **Owner entity** and **Attach to**. It does not fill
   **Origin entity**, which takes geometry: a vertex, an edge, a face, or the ``Origin`` row in the
   feature list.

   If **Origin entity** stays empty, the connector has nowhere to stand and the row goes red. Click
   ``Origin`` under ``Default geometry`` and the rest of the dialog fills itself.

.. step: cad.part_list

One part is in the list, and clicking it lights the whole shape, socket and all.

.. image:: images/foot/part_list-01.png
   :alt: the parts list holding one part, Foot, lit against the whole shape: the socket is inside it
         now rather than beside it
   :class: shot

.. step: cad.tree
.. req: req.page.view_keys

Press **shift+7** and read the feature list top to bottom. It is an account of the page: every
number stands directly above the feature that reads it, so you can see what each one is for without
being told.

.. image:: images/foot/tree-01.png
   :alt: the top of the feature list: the thirteen numbers the foot keeps to itself, each one
         standing above the feature that reads it
   :class: shot

Below the numbers come the eleven features, in the order you made them. Under them all is one part,
called ``Foot``.

.. image:: images/foot/tree-02.png
   :alt: the foot of the feature list, ending in add socket, combine parts and mate to robot, with
         one part called Foot under it
   :class: shot

Publish a version
------------------

.. step: cad.version
.. req: req.page.document

Click **Create version…** in the strip of icons down the far left. The dialog offers a name of its
own, already selected.

.. image:: images/toolbar/tb-create-version.png
   :alt: Close-up of the Create version button in the left icon strip, its tooltip reading Create
         version…
   :class: button

.. image:: images/foot/version-01.png
   :alt: the Create version from Main dialog with the name Onshape offers already in the Name box
         and selected
   :class: shot

Type ``tutorial 8 - the foot``, then click **Create**.

.. image:: images/foot/version-02.png
   :alt: the same dialog with tutorial 8 - the foot typed into the Name box
   :class: shot

The new version is at the top of the ``Versions and history`` panel.

.. image:: images/foot/version-03.png
   :alt: the Versions and history panel listing Main with tutorial 8 - the foot at the top
   :class: shot

What you should be able to read off the foot
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Check
     - Expected
     - Where to look
   * - parts in the tab
     - one, called ``Foot``
     - the parts list
   * - heel to toe
     - 96 mm
     - **Measure** across the outline
   * - across the toe
     - 48 mm
     - **Measure** across the widest part
   * - ground to the ball's middle
     - 24 mm
     - **Measure** from the sole up to the origin
   * - slots in the sole
     - eight, with land at both ends
     - the view from below, **shift+5**
   * - ``mate to robot``
     - the last row, in black
     - the end of the feature list

The foot is done, and it is the first part on the robot that was not a box or a ball. The pages
after this one build the joint that carries it.

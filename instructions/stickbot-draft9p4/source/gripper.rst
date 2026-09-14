The gripper — a clip that holds a LEGO bar
===========================================

Every other part in this robot is sized by the torso. This one is sized by **another part**: its
body is as wide as the socket's collar, and its mouth is as wide as a LEGO bar. It is the only
place in the build where two designs have to agree, so it is the page where the numbers get built
instead of typed.

.. figure:: images/gripper/hero.png
   :alt: The finished gripper seen from above and to the side: a round socket cup with four fingers
         at the top, a wider collar under it, and a flat clip hanging below with a round hole and a
         slot cut into it
   :width: 1130px
   :class: shot

   **The gripper.** The cup at the top clicks onto a limb's ball; the C-shaped clip at the bottom
   grips a Ø3.2 LEGO bar.

Eight variables, in this tab
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 30 48

   * - Name
     - Value
     - What it is
   * - ``#gripperL``
     - ``#torsoH / 4``
     - 24 mm — origin to the bore's center, so the gripper scales with the robot
   * - ``#clipR``
     - ``5 mm``
     - the clip head's radius
   * - ``#barD``
     - ``3.2 mm``
     - the LEGO bar
   * - ``#bore``
     - ``#barD + 0.1 mm``
     - 3.3 — the hole that holds it
   * - ``#mouth``
     - ``2.6 mm``
     - the gap the bar snaps through
   * - ``#ball``
     - ``#torsoH / 8``
     - 12 — the joint's ball, same as everywhere else
   * - ``#wall``
     - ``#torsoH / 32``
     - 3 — the socket's wall
   * - ``#collarR``
     - ``#ball / 2 + #wall``
     - 9 — and therefore the collar

.. admonition:: Three of these do not scale, and that is the point
   :class: advice

   ``#barD``, ``#bore`` and ``#mouth`` are the LEGO bar's numbers. Doubling the robot does not
   double LEGO, so these three stay put while everything around them grows. ``#clipR`` stays with
   them, because the clip head is built around the bar.

   ``#bore`` is ``#barD + 0.1``, not ``#barD + #fit``. The general print allowance is for parts
   this build prints itself; a bought bar gets its own number, chosen by trying it.

Copy the socket in — first, not last
-------------------------------------

**Derive** from the ``ball and socket`` Part Studio, pick the **Socket body** part, leave
**Placement** on **Base origin**, and rename the feature ``copy socket``.

This is the only tab where the derive comes **before** the part it joins, and there are two
reasons. The socket lands with its ball center on the studio origin and the underside of its
collar at z −7.4, so the wrist center is in the right place without a single move. And the plane
that flattens the top of the clip needs a real face to sit on — so the socket has to exist before
the clip does.

Sketch the profile on Right
----------------------------

Start a sketch on the **Right** (YZ) plane and name it ``clip profile``. Draw it in this order:

- a rectangle from (−5, 0) to (5, −17.7), with its **top edge on the horizontal axis**
- two circles, both centered on the vertical axis below the rectangle
- one short line across the lower circle, to make the mouth's lower lip
- then trim away everything inside the shape

Six dimensions define it:

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Dimension
     - Where it goes
   * - ``2 * #clipR``
     - the outer circle's diameter
   * - ``#bore``
     - the inner circle's diameter
   * - ``#gripperL - #clipR``
     - the vertical axis down to the circles' center
   * - ``#clipR``
     - the vertical axis across to the rectangle's **left** line
   * - ``#mouth / 2``
     - the circles' center up to the rectangle's bottom edge
   * - ``#mouth``
     - between the two lips

.. admonition:: One ``#clipR`` is enough, and the second one will not solve
   :class: advice

   The outer circle is tangent to both sides of the rectangle, so dimensioning the left line fixes
   the right one too. Dimension the right line as well and Onshape says **"Sketch could not be
   solved"** — which sounds like a geometry problem and is really a redundancy.

   Undo takes back one step, not the pair. Click the dimension you did not want, press
   :kbd:`Delete`, and the sketch solves.

**The mouth opens forward, toward −Y.** The robot faces −Y, so a hand that grips behind itself is
no use. In the **Right** view (:kbd:`Shift+4`) forward is to the **left** of your screen, which is
the check to make before you leave the sketch.

.. figure:: images/gripper/mouth.closeup.png
   :alt: Close up of the clip head from the right, a C-shaped ring of material with a round bore in
         the middle and a narrow slot opening toward the left of the screen
   :width: 1130px
   :class: shot

   **The mouth, opening to screen-left.** That is −Y, which is the way the robot faces.

Extrude it as wide as the collar
---------------------------------

Extrude the region. Click **New** first, tick **Symmetric**, and type ``2 * #collarR`` into the
depth. Rename the feature ``clip body``.

.. figure:: images/gripper/width.png
   :alt: The extrude dialog with New and Symmetric selected and the depth box showing the
         expression 2 star hash collarR, with a tooltip repeating it
   :width: 1130px
   :class: shot

   **The lesson of this page, in one box.** The depth is an expression, not 18. Change ``#wall``
   or ``#torsoH`` and the clip follows the collar it has to support.

.. admonition:: A shared expression, not a shared face
   :class: advice

   The honest way to build a cross-part dimension is to reference the other part's geometry, so it
   can never go stale. Onshape will not do it here: the width runs along the **extrude axis**, and
   a depth field cannot measure another body's diameter.

   So the dependency is ``#collarR = #ball / 2 + #wall`` — the same expression the ``ball and
   socket`` tab uses — and a depth of ``2 * #collarR``. It is the next best thing, and it is worth
   knowing which one you have.

   The version this replaces had **9.4** typed into that box, and the number went stale twice: once
   when the collar's formula changed, and again when the robot doubled.

Cut the top of the clip flat
-----------------------------

The clip runs straight up past the collar's underside, so the two have to be trimmed to meet.

- **Plane**, with the collar's **bottom face** in **Entities**, type **Offset**, distance **0 mm**.
  Rename it ``plane to cut top of clip``.
- **Split**, on the **Part** tab. The clip body goes in the top field and the plane in **Entity to
  split with**. Tick **Keep tools**; leave **Trim to face boundaries** and **Keep both sides**
  clear. Rename it ``remove top of clip``.

.. figure:: images/gripper/cut_plane.medium.png
   :alt: The split dialog with Part 2 in the parts field and plane to cut top of clip in the entity
         field, Keep tools ticked, and the model showing the clip still running up past the socket's
         collar
   :width: 1130px
   :class: shot

   **Before.** The clip's top is still buried in the socket, and the plane sits on the line where
   the collar ends.

.. figure:: images/gripper/cut_top.medium.png
   :alt: The same view after the split, the clip now stopping exactly at the collar's underside and
         the Parts list showing one part named Gripper
   :width: 1130px
   :class: shot

   **After.** One clean face where the two meet.

.. admonition:: A plane at offset zero is still worth building
   :class: advice

   Typing −7.4 into an offset would work today and break the moment ``#ball`` or ``#wall`` moves.
   An offset of **0 mm** on the collar's own face is a dependency: it goes where the face goes.

Weld it and name the part
--------------------------

**Boolean → Union**, both bodies, rename ``combine parts``. Then rename the part in the **Parts**
list ``Gripper``.

.. admonition:: Editing the sketch afterwards breaks the two features below it
   :class: advice

   Change ``clip profile`` and the extrude re-solves into a body with a **new identity**, so the
   split and the union both go red — *"Missing Part of clip body"*, *"Missing Part of remove top of
   clip"*. Nothing about them is wrong; their picks point at a body that no longer exists.

   Open each one, click the **×** on the missing reference, and click the body again in the
   graphics area. Read the split's three checkboxes once more afterwards.

Put the mate connector on the origin
-------------------------------------

**Mate connector**, mode **On entity**, and pick the **Origin** itself — the vertex, in the tree.
Tick **Owner entity** and set it to ``Gripper``. Name it ``mate to robot``.

This is the shortest connector in the whole guide, and it is short because of the derive. Bringing
the socket in at **Base origin** already put the wrist center on the origin, so the connector the
assembly needs is the origin.

Publish the version
-------------------

Version icon, ``t12 gripper``, create.

.. figure:: images/gripper/version.png
   :alt: The Create version dialog named t12 gripper, its description recording the bore, the clip
         diameter, the mouth gap, the length, the thinnest wall and the volume
   :width: 1130px
   :class: shot

   **The measurements go in the description**, so they travel with the version.

.. figure:: images/gripper/tree.png
   :alt: The gripper's feature tree: eight variables, copy socket, clip profile, clip body, plane
         to cut top of clip, remove top of clip, combine parts and mate to robot, with one part
         named Gripper
   :width: 380px
   :class: shot

   **Seven features after the variables, one part.**

Where the clip meets the socket
--------------------------------

The acceptance check is that the top of the clip is flush with the edge of the socket. It is —
**in Z**, which is what the plane gives. The outline is a different question, and the two frames
below are the honest answer.

.. figure:: images/gripper/flush.end.closeup.png
   :alt: The junction seen from the front, the socket above and the clip below, their left and
         right edges continuing in a straight line with no step
   :width: 1130px
   :class: shot

   **From the front, flush.** Both are 18 across, so the sides run straight through the joint.

.. figure:: images/gripper/flush.side.closeup.png
   :alt: The same junction seen from the right, the socket clearly wider than the clip below it,
         with a step on each side
   :width: 1130px
   :class: shot

   **From the side, not flush.** The collar is round and Ø18; the clip is a flat slab 10 deep. The
   collar overhangs by 4 at the middle and the overhang tapers to nothing at the ends.

.. admonition:: No width makes this joint flush
   :class: advice

   A round collar and a straight-sided slab cannot share an outline whatever number you type. Make
   the slab 18 deep and it stops overhanging at the ends but sticks out at the corners instead.

   Following the collar's profile takes a different feature — a loft or a revolve — and that is a
   change to the design, not a number to fix. It is on the list.

What you should be able to read off the model
----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 46 20 34

   * - Check
     - Expected
     - Where to look
   * - parts in the tab
     - 1
     - the **Parts** list
   * - the bore
     - Ø3.300
     - Measure, on the round face
   * - the clip head
     - Ø10.000
     - the same
   * - the mouth's actual gap
     - 2.600
     - Measure, between the two lips
   * - the bore's axis
     - parallel to **X**
     - the bore is a full circle in the **Right** view
   * - origin to the bore's center
     - 24.000
     - the bounding box reaches z −24
   * - the thinnest wall
     - 2.20
     - the socket's collar, ``#collarR − #ball / 2 − 0.8``
   * - the whole part
     - 4006.738 mm³
     - Measure → volume

.. admonition:: The little ledge on the back is meant to be there
   :class: advice

   The slab's flat side is tangent to the clip head's circle at its widest point, but the slab
   stops ``#mouth / 2`` **above** that point — so its bottom corner ends up 5 − 4.828 = **0.172**
   outside the arc.

   It is a tenth of a print layer and nothing to chase. Building the mouth toward −Y puts it on the
   back of the gripper, which is the better of the two places for it.

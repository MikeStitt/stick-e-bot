The lower limb — a blade at the top, a ball at the bottom
==========================================================

This is the other half of the arm, and it is the page before it with the joints swapped: where the
upper limb had a socket on top and a fork underneath, this one has the hinge's **blade** on top and
a **ball stud** underneath.

.. figure:: images/l-limb/hero.png
   :alt: The finished lower limb: a tall gray rod with a flat dimpled blade at the top and a small
         ball on a stalk at the bottom, with the feature tree beside it
   :width: 1130px
   :class: shot

   **The lower limb.** The blade at the top drops into the upper limb's fork to make an elbow; the
   ball at the bottom clicks into a gripper or a foot.

If you have just built the upper limb, this page will take you a fraction of the time. The moves
are the same and there is one fewer of them.

Make the tab and the one variable
----------------------------------

New Part Studio, renamed ``l limb``. One variable, the same as before:

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - Name
     - Value
     - What it is
   * - ``#limbD``
     - ``#torsoH / 4``
     - 24 mm — the limb's diameter

Copy the blade in
-----------------

**Derive** from the ``hinge`` Part Studio and click the indented **blade** row — not the studio
row, which would bring the fork along with it. Leave **Placement** on **Base origin** and accept.
Rename it ``add blade``.

The blade arrives with the **hinge axis on the origin**, because that is where the hinge tab built
it. That is the whole reason this page is shorter than the last one: the joint that will become the
elbow is already in exactly the right place, so there is nothing to sketch a connector onto and
nothing to move.

Draw the limb on the blade's own end face
------------------------------------------

The blade has an arm on it — a flat-ended stub of limb sticking out of the joint. Start a sketch
**on the flat disc at the end of that arm**, draw one circle centered on the sketch origin, and
dimension it ``#limbD``. One dimension takes the sketch fully defined.

Name the sketch ``limb section``.

Extrude it away from the blade
-------------------------------

Extrude the region. Click **New** first — the dialog opens on **Add**, with the blade already in
its merge scope.

.. figure:: images/l-limb/limbseg.png
   :alt: The extrude dialog with New selected, the limb section face in the region field, Blind,
         and 48 mm in the depth box
   :width: 560px
   :class: shot

   **Blind, ``#limbSeg``, pointing away from the blade.** Check the direction arrow before you
   accept; it is much easier than undoing a limb that grew back into the joint.

Set **Blind**, type ``#limbSeg``, and check the arrow points away from the blade. Accept, and
rename the feature ``limb``.

.. admonition:: Read the number back before you accept
   :class: advice

   Two things go wrong in this one box, and neither shows on screen. A view key pressed while the
   box has focus gets typed into it, so ``#limbSeg`` becomes ``#limbSeg1f``. And **⌘A** in a box
   you have just clicked does not always select what is in it, so the new text lands in front of
   the old.

   Both are cured the same way: clear the box, look at it, type, then click the dialog title and
   read the value back.

Put a mate connector on the far end
------------------------------------

Add a **mate connector** on the limb's far end face, with **Owner part** unticked. Name it
``mate for ball stud``. It exists to be a target for the move that comes next.

.. figure:: images/l-limb/move_stud.target.closeup.png
   :alt: Close up of the limb's lower end face, with a red ring around the mate connector triad
         standing on it
   :width: 1130px
   :class: shot

   **mate for ball stud**, on the end of the rod.

Copy the ball stud in, and move it there
-----------------------------------------

**Derive** from ``ball and socket`` and pick the **Ball stud** part. Rename the feature
``add ball stud``.

Then **Transform**, set to **By mate connectors**:

1. the ball stud in the **Entities** field
2. **From** is the stud's own ``stud connect to robot``
3. **To** is ``mate for ball stud``
4. tick **Flip primary axis**

Accept, and rename it ``move ball stud``.

.. figure:: images/l-limb/move_stud.source.closeup.png
   :alt: The ball stud in the ball and socket tab, a red ring around the connector triad on the end
         of its stalk
   :width: 1130px
   :class: shot

   **stud connect to robot**, the connector the **From** field wants, at z +10 on the end of the
   stalk. It is shown here in the ``ball and socket`` tab, where it was made, because the derive
   drops the stud on *this* tab's origin — inside the blade — where none of it can be seen. The
   triad is all you get to click.

.. admonition:: Why it needs the flip
   :class: advice

   The two connectors both point outward from their own parts, so landing one on the other without
   the flip turns the stud round and buries the ball 10 mm **inside** the limb. Nothing errors —
   the model just quietly grows the wrong way.

.. figure:: images/l-limb/move_stud.medium.png
   :alt: The end of the rod with the ball stud now attached, stalk and ball standing clear of the
         end face, and three connector triads on screen
   :width: 1130px
   :class: shot

   **After the move, with the flip on.** The ball is outside the limb and the stalk stands clear.
   Three marks are visible here — ``blade to robot`` at the top of the crop, the rod's end
   face where ``mate for ball stud`` and the stud's own ``stud connect to robot`` now sit on top of
   each other, and the ball's center.

   The check is the bounding box. With the flip, the bottom of the part reads **−108**. Without it,
   it reads −92 and the ball is nowhere to be seen.

Weld it into one part
----------------------

**Boolean → Union**, all three bodies, accept, rename ``combine parts``. Then rename the part in
the **Parts** list ``l limb``.

The volumes add up exactly here, and it is worth checking why: the blade's arm ends where the rod
starts, and the stud's stalk sits flat on the rod's far end. Nothing overlaps anything, so the
finished part weighs exactly what its three pieces weighed.

The two connectors the assembly will use
-----------------------------------------

**The elbow end is two picks, and here they are easy.** The blade carries a Ø4 stub axle standing
proud on each of its faces. Add a mate connector, set it to **Between entities**, and pick the flat
end disc of each stub.

The trick is to use two views. Press **shift+1** for the front and click the disc facing you; press
**shift+2** for the back and click the other one. Two equal discs, one on each side, average to the
axis exactly between them.

.. figure:: images/l-limb/ends.medium.png
   :alt: The whole lower limb seen front on, the blade with its ring of twenty-four dimples at the
         top, the rod below it, and the ball stud on its short stalk at the bottom
   :width: 1130px
   :class: shot

   **The whole part.** Blade at the top, ball at the bottom. This frame was taken at the end of the
   build, so all four connectors are already on it: the two that came in with the derives, and the
   two you are about to add.

.. figure:: images/l-limb/elbow_end.medium.png
   :alt: The same view with a red ring around the connector at the center of the blade's dimple
         ring, and the rod highlighted orange
   :width: 1130px
   :class: shot

   **Where elbow end lands**, in the middle of the ring of dimples — which is the hinge axis, and
   the studio origin.

.. figure:: images/l-limb/elbow_end.closeup.png
   :alt: Close up of the blade end from the front, a red ring around the mate connector on the
         hinge axis, the near stub axle in front of it and the far one hidden directly behind
   :width: 1130px
   :class: shot

   **elbow end.** Both picks are the same kind of thing — two flat circular faces — which is what
   keeps the connector on the axis.

Set **Owner part** to ``l limb`` and name it ``elbow end``.

**The wrist end is one pick.** Click the **ball's outer surface** and Onshape offers you its
center. Set **Owner part** to ``l limb`` and name it ``wrist end``.

.. figure:: images/l-limb/wrist_end.medium.png
   :alt: The whole limb again with a red ring around the ball at the far end
   :width: 1130px
   :class: shot

   **And where wrist end lands**, 102 below the elbow. The two rings in these two pictures are the
   segment this page builds.

.. figure:: images/l-limb/wrist_end.closeup.png
   :alt: Close up of the ball at the bottom of the limb with a red ring around the mate connector
         sitting at the center of the ball
   :width: 1130px
   :class: shot

   **wrist end**, at the center of the ball.

.. admonition:: Outside of a ball, yes. Inside of a cup, no
   :class: advice

   A **convex** sphere offers its center when you click it. A **hollow** one does not — it gives
   you the surface point, or the center of the mouth circle. That is why the upper limb's shoulder
   connector went on the origin instead of into the cup, and why this one is a single click.

Publish the version
-------------------

Version icon, ``t11 l limb``, create.

.. figure:: images/l-limb/version.png
   :alt: The Create version dialog named t11 l limb, its description recording the frame the limb
         was built in and the measured segment and volume
   :width: 1130px
   :class: shot

   **Put the measurements in the description.** This one records the frame, the segment of 102 and
   the volume of 40056.825 mm³ — so the numbers travel with the version instead of living only in
   your notes.

.. figure:: images/l-limb/tree.png
   :alt: The lower limb's feature tree from the default geometry down to wrist end, with one part
         named l limb
   :width: 380px
   :class: shot

   **Fourteen features, one part** — the same count as the upper limb, because it is the same
   recipe with the two ends swapped.

The elbow, both halves together
--------------------------------

.. figure:: images/l-limb/side-by-side.png
   :alt: The whole upper limb and the whole lower limb side by side from the right, the fork's slot
         and bumps facing the blade's stub axle, the blade itself edge on
   :width: 1130px
   :class: shot

   **The elbow, in two tabs.** The fork's slot, its detent bumps and its axle pockets, facing the
   blade's stub axle. The view is from the right, so the blade is edge on and its ring of dimples is
   on the two faces you cannot see. They do not meet until page 13.

   This picture is **composed** — two separate screenshots, scaled to match and placed side by
   side. Onshape cannot draw it, because the two halves live in different Part Studios and only
   meet in the assembly.

What you should be able to read off the model
----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 45 20 35

   * - Check
     - Expected
     - Where to look
   * - parts in the tab
     - 1
     - the **Parts** list
   * - the blade, unchanged from its source
     - 17313.169 mm³
     - Measure → volume, before the Boolean
   * - the rod alone
     - 21714.688 mm³
     - the same
   * - the ball stud, unchanged from its source
     - 1028.968 mm³
     - the same
   * - the whole part
     - 40056.825 mm³
     - Measure → volume, after the Boolean
   * - the bottom of the part
     - −108
     - the bounding box, which is how you check the flip

.. admonition:: The finished part is longer than the rod
   :class: advice

   The same arithmetic as the upper limb, with this limb's numbers: the rod is 48, the blade
   reaches 44 above it and the ball stands 10 below, so the part is **120** long and its two joint
   centers are **102** apart.

   ``#limbSeg`` is 48 on both limbs and nothing in the build wanted them different. If you want the
   joint centers closer together, that one variable moves both.

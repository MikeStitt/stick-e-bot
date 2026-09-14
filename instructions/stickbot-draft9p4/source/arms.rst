Both arms — build one, copy the other
======================================

This page is where the robot stops being a torso with a head on it. It is also the page where you
stop building things one at a time: the left arm is three parts and three mates, and the right arm
is a copy that arrives with two of its three mates already made.

Everything here happens in the ``stickbot`` Assembly tab. No Part Studio is opened and no geometry
is drawn.

.. figure:: images/arms/hero.png
   :alt: The robot in the assembly with a head, a torso and two arms, each an upper limb, a lower
         limb and a gripper; the right arm hangs straight down past the bottom of the torso and the
         left is folded across the front of it
   :width: 1130px
   :class: shot

   **Both arms on**, and already posed — the right one hanging, the left folded across. There are
   no legs yet, so the hanging arm reaches well past the bottom of the torso and the robot looks
   longer than it will end up.

Insert the upper limb and the lower limb
-----------------------------------------

**Insert**, and stay on the **Current document** tab. The **Part Studios** list holds every tab in
this document. Each row expands to the parts inside it, and every one of these tabs has exactly
one part.

Click ``u limb``. Click ``l limb``. The counter at the foot of the panel reads ``Inserted: 2``.
Close the panel with the green tick.

.. figure:: images/arms/insert.dialog.png
   :alt: The Insert parts and assemblies panel on the Current document tab, listing gripper, head,
         hinge, l limb and u limb as Part Studios, with l limb and u limb expanded to show one part
         each
   :width: 1130px
   :class: shot

   **The insert panel.** One click per row inserts it; the panel stays open so you can put several
   in without reopening it.

.. admonition:: The parts land where they were drawn
   :class: advice

   Each limb arrives at the assembly's origin, because that is where it sits in its own Part
   Studio. Both limbs are drawn around the same origin, so they arrive inside one another.

   That is normal and it sorts itself out on the first mate. Do not try to drag them apart first.

Mate the shoulder with a Ball
------------------------------

Pick the **Ball** mate from the toolbar. If you would rather see the whole list, open the type
dropdown at the top of the mate panel — it holds all eight, and the two this page uses are three
rows apart.

.. figure:: images/arms/mate.types.png
   :alt: The mate type dropdown open in the mate panel, listing Slider, Cylindrical, Revolute, Pin
         slot, Planar, Ball, Fastened and Parallel
   :width: 1130px
   :class: shot

   **The eight mate types.** Ball for the shoulder and the wrist, Revolute for the elbow.

A mate takes two picks, and this page always picks the moving part first.

**First pick:** expand ``u limb <1>`` in the instance list and click ``shoulder end``.

.. figure:: images/arms/mate.shoulder.pick1.png
   :alt: The mate panel with one row in its Mate connectors list, shoulder end of u limb, and
         nothing moved in the graphics area yet
   :width: 1130px
   :class: shot

   **After the first pick.** One row in the list and no preview — a mate needs both halves before
   it can show you anything.

**Second pick:** expand ``torso <1>`` and click ``left shoulder``.

The arm swings into place as soon as the second pick lands. Rename the mate ``left shoulder``.

.. figure:: images/arms/mate.shoulder.pick2.png
   :alt: The mate panel with two rows in its Mate connectors list, shoulder end of u limb and
         left shoulder of torso, the type set to Ball, and the arm now hanging from the
         torso's left shoulder
   :width: 1130px
   :class: shot

   **Two picks, one mate.** Both rows appear in the **Mate connectors** list, and the preview shows
   where the part will end up.

.. admonition:: The connector you want has neighbors that will also solve
   :class: advice

   Every part in this tutorial carries mate connectors left over from how it was built, and they
   sit right beside the one you want. ``u limb`` has ``socket connect to robot`` and
   ``fork to robot`` next to ``shoulder end``. ``l limb`` has ``blade to robot``
   and ``axis for circular patterns`` next to ``elbow end``. The torso has five.

   Pick the wrong one and the mate still solves — it just puts the arm somewhere strange. That is
   harder to spot than a mate that fails, so read the name before you click.

Mate the elbow with a Revolute
--------------------------------

**First pick:** ``elbow end`` under ``l limb <1>``.

**Second pick:** ``elbow end`` under ``u limb <1>``.

Both connectors are called ``elbow end``, because each limb names its own. The list in the panel
tells them apart by the instance: ``elbow end of l limb <1>`` and ``elbow end of u limb <1>``.

Rename the mate ``left elbow``.

.. figure:: images/arms/mate.elbow.picks.png
   :alt: The mate panel set to Revolute with elbow end of l limb and elbow end of u limb in its
         list, the instance tree showing u limb expanded to shoulder end, elbow end and socket
         connect to robot
   :width: 1130px
   :class: shot

   **The elbow.** A Revolute, not a Ball — the printed hinge only folds one way, and the mate
   should say so.

Insert the gripper and mate the wrist
---------------------------------------

**Insert** again and click ``gripper``. Then a **Ball** mate:

**First pick:** ``mate to robot`` under ``Gripper <1>``.

**Second pick:** ``wrist end`` under ``l limb <1>``.

Rename it ``left wrist``. One arm is done: three instances and three mates.

Drag it before you copy it
---------------------------

Grab the arm in the graphics area and pull it around. This is the fastest way to see that a Ball
and a Revolute are not the same thing, and it costs nothing — dragging a mated assembly moves it
within its mates and changes no geometry.

.. figure:: images/arms/pose.raised.png
   :alt: The robot with one arm raised up and out to the side, the elbow bent, the other arm
         hanging straight down
   :width: 1130px
   :class: shot

   **Raised.** The shoulder swings in any direction, because a Ball leaves all three rotations
   free.

.. figure:: images/arms/pose.across.png
   :alt: The robot with one arm folded across the front of the torso, the upper limb horizontal and
         the lower limb angled down and away
   :width: 1130px
   :class: shot

   **Folded across**, which is the pose the picture at the top of this page is in. The elbow only
   opens and closes, in one plane, because a Revolute leaves one rotation free.

Copy the arm
-------------

Before you copy anything, look at the two counts at the top of each list: **Instances (5)** and
**Mate features (4)**. Write them down. They are the proof that the next two clicks did what this
page says they did.

Click ``u limb <1>`` in the instance list, then ``Meta``-click ``l limb <1>`` and ``Gripper <1>``.
All three rows highlight, and the whole arm lights up in the graphics area.

.. figure:: images/arms/copy.selected.png
   :alt: The instance list with u limb, l limb and Gripper highlighted, the whole arm highlighted
         orange in the graphics area, Instances reading 5 and Mate features reading 4
   :width: 1130px
   :class: shot

   **Three parts selected, and the counts before.** Instances (5), Mate features (4).

.. figure:: images/arms/copy.tree.before.png
   :alt: The instance list before the copy reading Instances 5 and Mate features 4, listing head to
         neck, left shoulder, left elbow and left wrist
   :width: 220px
   :class: shot

   **The lists before.** Five instances, four mates.

Copy, then paste. The counts change.

.. figure:: images/arms/copy.tree.after.png
   :alt: The instance list after the paste reading Instances 8 with Gripper 2, l limb 2 and u limb
         2 added, and Mate features 6 with left elbow (1) and left wrist (1) added
   :width: 220px
   :class: shot

   **And after.** Instances (8), Mate features (6). Three parts in, two mates in, from one paste.

.. admonition:: A mate comes along when both of its ends do
   :class: advice

   ``left elbow`` joins the lower limb to the upper limb. ``left wrist`` joins the gripper to the
   lower limb. Both ends of both mates were in what you selected, so both were duplicated.

   ``left shoulder`` joins the upper limb to the **torso**, and the torso was not selected. That
   mate had nowhere to land, so it was dropped. It is the only one you build again by hand.

The copy lands offset from the original. How far, and in which direction, depends on where your
camera was — it may overlap the robot, and it may be off the edge of the screen. Hover the graphics
area and press ``f`` to bring everything back into view.

.. figure:: images/arms/paste.graphics.png
   :alt: The graphics area after the paste, the original arm still hanging from the torso and the
         pasted arm floating above and to the right, partly off the top of the view
   :width: 1130px
   :class: shot

   **Where the copy lands.** Offset and unmated — not exactly on top of the original, and not at
   the origin.

Rename the two mates that came along
--------------------------------------

Onshape names a duplicated mate after the one it came from, with a number in brackets. So the right
arm arrives carrying ``left elbow (1)`` and ``left wrist (1)``, which are on the right.

Rename them ``right elbow`` and ``right wrist`` now, while you still know which is which.

Mate the second shoulder
--------------------------

One **Ball** mate finishes the robot's arms.

**First pick:** ``shoulder end`` under ``u limb <2>``.

**Second pick:** ``right shoulder`` under ``torso <1>``.

Rename it ``right shoulder``.

.. figure:: images/arms/mate.shoulder2.picks.png
   :alt: The mate panel with shoulder end of u limb 2 and right shoulder of torso in its
         list, the torso expanded to show its five connectors, and the pasted arm still floating to
         the right waiting to be pulled in
   :width: 1130px
   :class: shot

   **The seventh mate.** The torso's five connectors are all in one place, so read the name — the
   right shoulder is one row below the left.

.. admonition:: The copy is not mirrored, and it does not need to be
   :class: advice

   A copy is a copy: the right arm starts out pointing the same way as the left one. It still lands
   correctly, because a Ball mate puts two points together and says nothing about which way the
   part faces.

   Where handedness would matter is the elbow, and that Revolute came in from a copy of a joint
   that already worked. Building the second elbow by hand is the way to get it backwards.

Publish the version
--------------------

Put both counts in the description, so they travel with the version.

.. figure:: images/arms/version.png
   :alt: The Create version dialog named t13 arms, its description recording how one arm was built
         and the other copied, and the counts 8 instances and 7 mates
   :width: 1130px
   :class: shot

   **t13 arms.** The next page starts from here.

What you should be able to read off the assembly
--------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 42 18 40

   * - Check
     - Expected
     - Where to look
   * - instances
     - 8
     - the **Instances** heading
   * - mate features
     - 7
     - the **Mate features** heading
   * - Ball mates
     - 5
     - neck, two shoulders, two wrists
   * - Revolute mates
     - 2
     - the two elbows
   * - mates you built by hand
     - 6
     - the seventh, ``right wrist``, came from the paste
   * - top of the head
     - 137.40 mm
     - the bounding box's high **Z**

.. figure:: images/arms/tree.png
   :alt: The finished instance list, eight instances and seven mate features named head to neck,
         left shoulder, left elbow, left wrist, right elbow, right wrist and right shoulder
   :width: 380px
   :class: shot

   **Seven mates, seven real names.** Nothing left in brackets.

.. admonition:: The elbow can still slide sideways
   :class: advice

   A Revolute holds the hinge's axis and lets it turn. It does not stop the blade sliding along
   that axis, so you can push the lower limb a little way across inside the fork.

   The fix is a **Width** mate on each elbow, holding the blade centered between the fork's two
   inner faces. It is not built here, and the arm works without it — but it is the difference
   between a joint that is held and a joint that only looks held.

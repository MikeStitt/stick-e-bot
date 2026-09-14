Both legs — copy an arm, then copy the leg
============================================

A leg is an upper limb, a lower limb and a foot. You have already built two upper limbs and two
lower limbs, and they are the same parts — so this page starts by copying half an arm, and the
first thing that arrives is a working knee.

Everything here happens in the ``stickbot`` Assembly tab. No Part Studio is opened and no geometry
is drawn. When you finish, the robot is complete and it stands up.

.. figure:: images/legs/hero.png
   :alt: The finished robot standing on two feet, seen from an isometric view, with a head, a
         torso, two arms ending in grippers and two legs ending in feet
   :width: 1130px
   :class: shot

   **The whole robot.** Fourteen instances and thirteen mates, and every joint still free to move.

Copy the arm's two limbs
--------------------------

Read the two counts at the top of the lists first: **Instances (8)** and **Mate features (7)**.
They are how you will know what the paste did.

Select ``u limb <1>`` and ``Meta``-click ``l limb <1>``. Two rows, not three — leave the gripper
behind, because a leg does not have one.

.. figure:: images/legs/copy1.selected.png
   :alt: The instance list with u limb and l limb highlighted and Gripper not highlighted, and the
         arm's two limbs lit orange in the graphics area with the gripper left plain
   :width: 1130px
   :class: shot

   **Two limbs, no gripper.** The orange in the graphics area is the check — the gripper at the end
   of the arm stays its normal color.

Copy, then paste.

.. figure:: images/legs/copy1.tree.before.png
   :alt: The instance list before the paste reading Instances 8 and Mate features 7, ending at
         right shoulder
   :width: 220px
   :class: shot

   **Before.** Eight instances, seven mates.

.. figure:: images/legs/copy1.tree.after.png
   :alt: The instance list after the paste reading Instances 10 and Mate features 8, with l limb 3
         and u limb 3 added and left elbow (1) at the end of the mate list
   :width: 220px
   :class: shot

   **After.** Ten instances, eight mates. Two parts in and one mate in, from one paste.

.. admonition:: The paste lands near the original, not away from it
   :class: advice

   The copy is offset by a small amount in screen space, so where it ends up depends on where your
   camera was pointing. It may sit almost on top of the parts it came from.

   Hover the graphics area and press ``f`` to fit everything in view, then look for the pair that
   is not attached to anything.

.. figure:: images/legs/copy1.paste.graphics.png
   :alt: The graphics area just after the paste, the original arm lit orange and the pasted pair in
         plain gray almost overlapping it
   :width: 1130px
   :class: shot

   **Where it landed this time.** The orange pair is the original; the gray pair behind it is the
   copy.

The pair arrives already jointed
----------------------------------

Drag the new pair away from the robot and look at it on its own. It is bent, and the bend is a real
joint: ``left elbow (1)`` came along in the paste, because both of the parts it joins were in what
you selected.

.. figure:: images/legs/pair.floating.png
   :alt: The Front view with the copied limb pair moved out to the right of the robot, floating
         free and bent at the joint between its two limbs, the mate list reading eight with left
         elbow (1) last
   :width: 1130px
   :class: shot

   **A jointed pair, attached to nothing.** This is the whole idea of the page — you did not build
   that joint, you copied it.

.. figure:: images/legs/pair.floating.closeup.png
   :alt: A close view of the floating limb pair, the upper limb's fork wrapped around the lower
         limb's blade at the bend
   :width: 300px
   :class: shot

   **The joint, close up.** Fork around blade, exactly as it is at the elbow.

.. admonition:: You cannot bend it yet, and that is not a fault
   :class: advice

   Try to drag one limb and the whole pair slides instead. Nothing in the pair is attached to the
   robot, so the solver is free to move both parts together — and moving both is a cheaper answer
   than turning one about the joint. The joint is there; it has no reason to be used.

   Mate the hip first. Then the upper limb is held, and the knee is the only way left to move.

.. figure:: images/legs/pair.bent.png
   :alt: The same view after dragging the floating pair, which has moved bodily to the right with
         the angle between its two limbs unchanged
   :width: 1130px
   :class: shot

   **Dragged, and unchanged.** The pair has moved across the screen; the angle at the joint is the
   one it arrived with.

Rename the elbow that is now a knee
-------------------------------------

The mate is called ``left elbow (1)``. It is not an elbow any more. Rename it ``left knee``.

That rename is the whole conversion from arm to leg. Nothing about an upper limb or a lower limb is
arm-specific — the difference between an arm and a leg is what you attach it to.

Insert the foot
-----------------

**Insert**, stay on the **Current document** tab, and type ``foot`` in the search box to shorten the
list. Click the row, and the counter reads ``Inserted: 1``. Close the panel with the green tick.

.. figure:: images/legs/insert.foot.png
   :alt: The Insert panel filtered to foot with one matching Part Studio row, the counter reading
         Inserted 1, and Foot 1 added at the bottom of the instance list
   :width: 1130px
   :class: shot

   **One part, one click.** The foot arrives at the origin, inside the torso, the way every
   inserted part has.

Mate the ankle with a Ball
----------------------------

**First pick:** ``mate to robot`` under ``Foot <1>``.

**Second pick:** ``wrist end`` under ``l limb <3>``.

Rename it ``left ankle``.

.. figure:: images/legs/mate.ankle.picks.png
   :alt: The mate panel set to Ball with mate to robot of Foot 1 and wrist end of l limb 3 in its
         Mate connectors list, and the foot now on the end of the floating limb pair
   :width: 1130px
   :class: shot

   **The ankle.** The lower limb's connector is called ``wrist end`` because that is what it was on
   an arm. The name does not change what it does.

Mate the hip with a Ball
--------------------------

**First pick:** ``shoulder end`` under ``u limb <3>``.

**Second pick:** ``left hip`` under ``torso <1>``.

Rename it ``left hip``. The leg swings up under the torso and hangs.

.. figure:: images/legs/mate.hip.picks.png
   :alt: The mate panel with shoulder end of u limb 3 and left hip of torso 1 in its list,
         the torso expanded to show neck, left shoulder, right shoulder,
         left hip and right hip
   :width: 1130px
   :class: shot

   **The torso's five connectors, all in one place.** Read the name — the two hips are one row
   apart, and picking the wrong one puts the leg on the wrong side.

.. admonition:: The copy is not mirrored, and it does not need turning
   :class: advice

   The pair you pasted points whatever way it happened to point, and it came off an arm. Neither
   matters. A Ball mate puts one point on another point and leaves all three rotations free, so it
   says nothing about which way the leg faces.

   The first drag puts the leg where you want it. There is no Mirror on this page and there does
   not need to be one.

Bend the knee, now that the hip holds it
------------------------------------------

Grab the foot and pull it forward. The hip turns, and so does the knee — and this time the knee is
the only thing that can give, because the top of the leg is held to the torso.

.. figure:: images/legs/knee.straight.png
   :alt: The robot with one leg mated at the hip, hanging straight down with its foot at the bottom
   :width: 1130px
   :class: shot

   **Hanging.** One leg on, eleven instances and ten mates.

.. figure:: images/legs/knee.bent.png
   :alt: The same robot seen from the front with the mated leg swung out to the side and folded at
         the knee, the foot well clear of the body
   :width: 1130px
   :class: shot

   **Bent.** Same leg, same mates. Only the joint angles changed.

Copy the whole leg
--------------------

The counts before this paste are **Instances (11)** and **Mate features (10)**.

Select ``u limb <3>``, ``l limb <3>`` and ``Foot <1>``. Three rows this time — the foot comes too.

.. figure:: images/legs/copy2.selected.png
   :alt: The instance list with l limb 3, u limb and Foot 1 highlighted, and the whole leg
         including its foot lit orange in the graphics area
   :width: 1130px
   :class: shot

   **A whole leg selected.** Upper limb, lower limb and foot, orange from hip to sole.

Copy, then paste.

.. figure:: images/legs/copy2.paste.graphics.png
   :alt: The graphics area after the second paste with the original leg still lit orange and the
         copy in plain gray behind it, and the mate list reading Mate features 12 ending in left
         knee (1) and left ankle (1)
   :width: 1130px
   :class: shot

   **Fourteen instances, twelve mates.** Three parts in and two mates in — the knee and the ankle,
   both arriving with brackets on their names.

The hip did not come along. Its other end is the torso, and the torso was not in the selection —
the same rule that dropped the shoulder when you copied the arm.

Rename the two mates that came along
--------------------------------------

``left knee (1)`` and ``left ankle (1)`` are on the right leg. Rename them ``right knee`` and
``right ankle`` before you forget which is which.

Mate the second hip
---------------------

One **Ball** mate finishes the robot.

**First pick:** ``shoulder end`` under ``u limb <4>``.

**Second pick:** ``right hip`` under ``torso <1>``.

Rename it ``right hip``.

.. figure:: images/legs/mate.hip2.picks.png
   :alt: The mate panel with shoulder end of u limb 4 and right hip of torso 1 in its list,
         the torso expanded with right hip highlighted, and the instance count reading 14
   :width: 1130px
   :class: shot

   **The thirteenth mate.** The last one you build by hand — five of the thirteen arrived by
   paste.

Stand it up, then pose it
---------------------------

Drag the feet until both soles are level and the robot stands. The Front view is the one to check
it in — the two soles should sit on the same line.

.. figure:: images/legs/hero.front.png
   :alt: The finished robot seen straight on from the front, standing square on two feet with both
         soles level and its arms hanging at its sides
   :width: 1130px
   :class: shot

   **Standing.** Both soles level and both legs straight. Measured from the parts, the head sits
   421.8 mm above the floor.

Then pull it around and watch which joints do what: the hips and ankles swing every way, the knees
only fold.

.. figure:: images/legs/pose.stride.png
   :alt: The robot in an isometric view with one leg forward and bent at the knee and the other
         back, as though mid-step
   :width: 1130px
   :class: shot

   **Mid-step.** One knee folded, both ankles turned to keep the soles down.

.. figure:: images/legs/pose.wave.png
   :alt: The same striding robot with one arm raised straight out to the side
   :width: 1130px
   :class: shot

   **And waving.** Every joint on the robot is free at the same time.

Publish the version
---------------------

Put the counts and the measured height in the description, so they travel with the version.

.. figure:: images/legs/version.png
   :alt: The Create version dialog named t14 legs, its description recording that one leg came from
         copying an arm's limb pair and the other from copying the leg, with the counts and the
         measured standing height
   :width: 1130px
   :class: shot

   **t14 legs.** The robot is complete at this version. Read the description and you get
   **431.97 mm** for the standing height, which is the assembly's bounding box rather than the
   robot: it stands **421.8 mm**. A version description cannot be edited once it is published, so
   the wrong number is stuck in there.

What you should be able to read off the assembly
--------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 42 18 40

   * - Check
     - Expected
     - Where to look
   * - instances
     - 14
     - the **Instances** heading
   * - mate features
     - 13
     - the **Mate features** heading
   * - Ball mates
     - 9
     - neck, two shoulders, two wrists, two hips, two ankles
   * - Revolute mates
     - 4
     - two elbows and two knees
   * - mates you built by hand
     - 7
     - the other six arrived in three pastes
   * - top of the head
     - 137.40 mm
     - the bounding box's high **Z**

.. figure:: images/legs/tree.png
   :alt: The finished instance list, fourteen instances and thirteen mate features named head to
         neck, left shoulder, left elbow, left wrist, right elbow, right wrist, right shoulder,
         left knee, left ankle, left hip, right knee, right ankle and right hip
   :width: 380px
   :class: shot

   **Thirteen mates, thirteen real names.** Nothing left in brackets.

.. admonition:: Measure the parts, not the pose
   :class: advice

   Do not read the robot's height off the bounding box. Every joint below the neck is free, so the
   box changes every time you drag something — and a foot tilted a few degrees puts a corner of its
   sole lower than the ankle it hangs from, which makes the robot look taller than it is.

   The height that means something is added up from the parts: the top of the head at 137.40, the
   hip at −58, a limb segment at each of the knee and the ankle, and the foot's own 24 below that.
   The one number on the list above that a bounding box *can* give you is the top of the head,
   because nothing above the neck moves much.

.. admonition:: The knees slide sideways, the same as the elbows
   :class: advice

   A Revolute holds the hinge's axis and lets it turn, and it does not stop the blade sliding along
   that axis. You can push each lower limb a little way across inside its fork.

   The fix is a **Width** mate on each of the four hinges, holding the blade centered between the
   fork's two inner faces. None of the four is built here. The robot walks and poses without them —
   but a printed joint is held by its parts, and a mated one should be held the same way.

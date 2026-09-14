The plan — the whole robot before the first part
================================================

You are going to build a robot out of about twenty printed pieces, in Onshape. It has a head that
turns, arms and legs that bend at the shoulder, elbow, hip and knee, feet it stands on, and a pair
of grippers that hold a LEGO bar.

The sheet below dimensions it at **315.4 mm** from the floor to the top of its head. The robot
these pages actually build stands **421.8 mm**, because each limb segment came out longer than the
sheet draws it — 106.4 mm of the difference is in the four segments and nothing else. Which of the
two is right has not been decided, so both numbers are here rather than one of them being quietly
picked. Everything else on the sheet was measured on the built model and agrees.

.. figure:: images/plan/assembly.png
   :alt: The assembly sheet: the whole robot drawn from the front and from the side, with the
         joints marked and the overall height dimensioned
   :width: 1130px
   :class: shot

   **The robot, drawn before it is built.** Front and side, with every joint on it. This sheet and
   the parts sheet below are drawn from the four numbers, so if a number ever changes, both sheets
   change with it. The height carries the one disagreement between the sheets and the model, and
   it is the paragraph above.

Nothing on this page is a step. It is what the robot is, so that when a page tells you to make a
box 72 mm wide you already know which box it is and what gets bolted to it later.

Two kinds of joint, and that is all
-----------------------------------

Every joint on the robot is one of two things, and both of them snap together without a screw, a
pin or any glue.

A **ball and socket** is a ball on a stalk that clicks into a cup. It turns every way at once, and
it is what the neck, the shoulders, the hips and the wrists are. The cup is split by four relief
slits so that its mouth — which is narrower than the ball — can spring open once to let the ball
in, and then close behind it.

A **hinge** is a flat blade that slides between two ears, so it swings one way only. It is what the
elbows and the knees are. The ears carry a ring of small bumps and the blade carries a ring of
matching dimples, so the joint clicks from angle to angle and stays where you leave it.

.. figure:: images/plan/parts.png
   :alt: The parts sheet: every printed piece of the robot drawn to scale with its dimensions,
         and detail views of the ball and socket and of the hinge
   :width: 1130px
   :class: shot

   **Every piece, to scale, with the two joints drawn large.** The details along the bottom are
   the ones worth reading twice: the socket in section, the hinge along the limb, and one of the
   hinge's toothed faces seen square on.

Four numbers drive the whole thing
----------------------------------

The robot is not a list of dimensions. It is four numbers, and everything else is arithmetic on
them.

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Name
     - Value
     - What it is
   * - ``#torsoH``
     - 96 mm
     - the torso's height, and the number most of the robot is measured against
   * - ``#torsoW``
     - 72 mm
     - the torso's width
   * - ``#torsoD``
     - 48 mm
     - the torso's depth
   * - ``#limbSeg``
     - 48 mm
     - how long one piece of an arm or a leg is

They live in a **Variable Studio**, which is a tab that holds a table of numbers every other tab in
the document can read. A limb is ``#torsoH / 4`` across, so it is Ø24. A ball is ``#torsoH / 8``,
so it is Ø12. Change ``#torsoH`` and the limbs and the balls change with it, and so does everything
that was built to fit them.

That is the habit the whole guide is teaching, and it is the reason the first page is a table of
four numbers rather than a box.

The order it gets built in
--------------------------

Parts are built in the order the assembly needs them, so building and assembling interleave rather
than happening in two blocks. A part is also built twice: the head arrives as a plain shell, goes
into the assembly, and comes back later to be given its socket once the socket exists.

.. list-table::
   :header-rows: 1
   :widths: 8 30 62

   * -
     - Page
     - What you end up with
   * - 1
     - The torso
     - the four numbers, and a box
   * - 2
     - The head
     - a second box, with a face on it
   * - 3
     - The assembly
     - both boxes in one assembly, named ``stickbot``
   * - 4
     - The ball and socket
     - the joint itself, in its own tab: a ball on a stalk, and a cup to take it
   * - 5
     - The head's socket
     - the head gains the cup the neck stud clicks into
   * - 6
     - The shoulders and the studs
     - the torso gains five ball studs — neck, two shoulders, two hips
   * - 7
     - The head on the torso
     - the first real joint, mated in the assembly
   * - 8
     - The foot
     - a foot with a socket in its top and a tread on its sole
   * - 9
     - The hinge
     - the second joint: a blade, a fork, and the teeth that make it click
   * - 10
     - The upper limb
     - a rod with a socket at one end and a hinge fork at the other
   * - 11
     - The lower limb
     - a rod with a hinge blade at one end and a ball stud at the other
   * - 12
     - The gripper
     - a C-clip that holds a LEGO bar, on a socket
   * - 13
     - One arm, then the other
     - an arm assembled and mated, then copied to the far side
   * - 14
     - One leg, then the other
     - the same for the legs, and the robot stands up

.. admonition:: You can stop at the end of any page
   :class: advice

   Each page ends with a named version of the document, which is a bookmark you can always come
   back to. Nothing later reaches back and changes what an earlier page built.

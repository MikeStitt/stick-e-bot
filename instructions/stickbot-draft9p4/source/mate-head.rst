The head goes on, and the robot's first joint works
====================================================

Everything so far has been parts. This page is the assembly. The torso gets pinned down, the head
gets mated to the neck ball, and for the first time something on the robot moves the way it is meant
to.

Open the ``stickbot`` assembly tab. It holds ``torso`` and ``head`` from page 3, where you put the
head above the torso by hand. Both of them have grown since: the torso has its balls and the head
has its socket, and the assembly shows what the tabs hold now. In the graphics area the head hangs
over the top of the torso, because the socket page 5 gave it reaches further down than the head did
when you parked it. Neither part has moved. The mate is what puts the head where it belongs.

Fix the torso
--------------

.. step: cad.assembly.fix_body
.. req: req.model.anchored

Something in every assembly has to be held still, or the whole thing floats. The torso is the one:
everything else on the robot hangs off it. Open both instances in the tree first, so you can see
what each one brought with it.

.. image:: images/mate-head/assembly.fix_body-01.png
   :alt: the assembly tree with torso <1> and head <1> both opened and neither marked fixed, because
         nothing is fixed yet
   :class: shot

Right-click ``torso <1>`` and choose **Fix**, about a third of the way down the menu.

.. image:: images/mate-head/assembly.fix_body-02.png
   :alt: the menu on torso <1> with Fix about a third of the way down
   :class: shot

Nothing in the graphics area moves. The only thing that changes is one small mark on one row.

.. image:: images/mate-head/assembly.fix_body-03.png
   :alt: the whole window after Fix, with the torso unmoved and the mark on its row the only thing
         that changed
   :class: shot

Look closely at the two instance rows. ``torso <1>`` now carries a hatched ground mark, and
``head <1>`` still carries the three arrows that mean free to move. That mark is the difference
between a robot that swings its head and a robot that drifts off the screen when you drag it.

.. image:: images/mate-head/assembly.fix_body-04.png
   :alt: the mark on torso <1> close up, and no mark on head <1>, which is the whole signal that the
         torso is the ground
   :class: shot

.. admonition:: If the torso lists no connectors
   :class: advice

   An instance with nothing under it means its connectors have no owner part. A connector made with
   **Owner entity** unticked works inside the Part Studio and does not exist outside it, which is
   why page 6 leaves two of them that way on purpose and gives the other five an owner.

   The repair is in the ``body`` tab, one connector at a time: double-click it, tick **Owner
   entity**, click into the field it reveals, and click ``torso`` in the parts list. Ticking the box
   is not enough on its own; something has to go in the field.

Mate the head to the neck
--------------------------

.. step: cad.assembly.mate_head
.. req: req.model.named_features
.. req: req.page.view_keys
.. req: req.shot.two_frame

The tree is where the picking happens. Under ``torso <1>`` are the five connectors page 6 named, and
under ``head <1>`` are the two page 5 named. Two of those seven are what this mate joins.

.. image:: images/mate-head/assembly.mate_head-01.png
   :alt: both parts opened in the tree, so head mate sits under head <1> and neck under torso <1>
   :class: shot

The neck is a ball in a socket, so the mate is a **Ball** mate. It is on the assembly toolbar, the
seventh of the mate buttons. Hover it and the tooltip says what it does.

.. image:: images/mate-head/assembly.mate_head-02.png
   :alt: the Ball mate button on the assembly toolbar
   :class: shot

Click the pencil beside the dialog's title and type ``head to neck`` over the name Onshape offered.
Do it before you pick anything. The dialog waits with two connector boxes empty.

.. image:: images/mate-head/assembly.mate_head-03.png
   :alt: the mate dialog renamed head to neck with both connector boxes empty, and head mate waiting
         in the tree beside it
   :class: shot

Pick ``head mate`` under ``head <1>`` first. The part that moves is picked first.

.. image:: images/mate-head/assembly.mate_head-04.png
   :alt: the head mate row under head <1> close up; the part that moves is picked first
   :class: shot

The box fills with ``head mate of head <1>`` and nothing has moved yet. One connector is a place,
not a joint.

.. image:: images/mate-head/assembly.mate_head-05.png
   :alt: the dialog holding head mate of head <1> and nothing moved yet, with neck waiting under
         torso <1> in the tree
   :class: shot

Pick ``neck`` under ``torso <1>`` second. That is where the head goes.

.. image:: images/mate-head/assembly.mate_head-06.png
   :alt: the neck row under torso <1> close up; this is where the head goes
   :class: shot

The head lifts out of where you left it and lands on the neck stud, the moment the second connector
is picked.

.. image:: images/mate-head/assembly.mate_head-07.png
   :alt: the head lifted out of where tutorial 3 left it and sitting on the neck stud, the moment
         the second connector is picked
   :class: shot

Accept it and press **f** to fit the robot in the window. **Mate features** reads 1.

.. image:: images/mate-head/assembly.mate_head-08.png
   :alt: the torso with the head on top of it, the robot's first joint, and Mate features reading 1
   :class: shot

.. admonition:: Pick the connector by name, in the tree
   :class: advice

   Clicking a face in the graphics area also fills the box, and what it fills it with is
   **Mate connector of torso <1>**. That generic name means Onshape made a connector of its own
   where you clicked, instead of using one of yours.

   It is anonymous, it is not the one in your Part Studio, and you cannot go back and repair it from
   there. Clicking the tree row fills the box with ``neck of torso <1>``, and that is the one you
   want.

.. admonition:: What the order of the two picks buys you
   :class: advice

   Onshape's own tooltip on the button says it: the first selection is the point that moves, and the
   second is the point that stays. Pick ``neck`` first in an assembly with nothing fixed and the
   *torso* travels 14 mm down to meet the head, which is backwards and looks alarming.

   With the torso fixed, the reversed order lands the head in exactly the same place, because a
   fixed part cannot move and Onshape has to move the other one. That is a second reason to fix the
   torso before anything else: it makes the picking order stop mattering.

.. admonition:: The × is what cancels a mate
   :class: advice

   While the dialog is open and unfinished, a half-made mate already sits under **Mate features** in
   red. Clicking a row in the tree selects that row and leaves the dialog open. The **×** at the top
   of the dialog is what cancels it.

Turn the head, and let it go
-----------------------------

.. step: cad.assembly.drag_head
.. req: req.model.posed

This is the part worth doing slowly, because it is the first thing the robot does. Press
**shift+1** to look from the front, where a turned head reads as turned. The head sits square on
the stud, which is where the joint rests when nothing is pushing it.

.. image:: images/mate-head/assembly.drag_head-01.png
   :alt: the head sitting square on the neck stud, the rest the joint returns to when it is let go
   :class: shot

Drag the head by its cheek. It turns on the ball, and it turns in every direction, because that is
what a ball mate allows.

.. image:: images/mate-head/assembly.drag_head-02.png
   :alt: the head turned on its ball, position 1 of three; the torso has not moved, because it is
         fixed
   :class: shot

Drag it somewhere else. The torso has not moved once.

.. image:: images/mate-head/assembly.drag_head-03.png
   :alt: the head turned on its ball, position 2 of three; the torso has not moved, because it is
         fixed
   :class: shot

And again. Only the head is free, and it is free about one point.

.. image:: images/mate-head/assembly.drag_head-04.png
   :alt: the head turned on its ball, position 3 of three; the torso has not moved, because it is
         fixed
   :class: shot

Press **Ctrl+Z** once for each drag, until the head is square on the stud again. It comes back to
the first picture in this section, at the same place to three decimals; a ball mate holds a point,
and the point never moved.

.. image:: images/mate-head/assembly.drag_head-05.png
   :alt: the head back where it started, square on the stud again, so the version is published on
         the rest pose
   :class: shot

.. admonition:: Fixed is why the torso stays put
   :class: advice

   Drag the head in an assembly where nothing is fixed and both parts move, because Onshape has no
   reason to prefer one over the other. The ground mark on ``torso <1>`` is the whole reason this
   reads as a robot turning its head rather than two shapes sliding about.

Publish a version
------------------

.. step: cad.version
.. req: req.page.document

A version is a snapshot of the whole document, so this one is the recovery point for everything
pages 1 to 7 built. Click **Create version…** in the strip of icons down the far left. The dialog
offers a name of its own, already selected.

.. image:: images/toolbar/tb-create-version.png
   :alt: Close-up of the Create version button in the left icon strip, its tooltip reading Create
         version…
   :class: button

Type ``tutorial 7 - the head is mated to the torso`` over it, then click **Create**.

.. image:: images/mate-head/version-01.png
   :alt: the Create version dialog with tutorial 7 - the head is mated to the torso typed into the
         Name box
   :class: shot

The new version arrives at the top of the ``Versions and history`` panel.

.. image:: images/mate-head/version-02.png
   :alt: the Versions and history panel listing Main with tutorial 7 - the head is mated to the
         torso at the top
   :class: shot

What you should be able to read off the assembly
--------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 42 28 30

   * - Check
     - Expected
     - Where to look
   * - instances
     - two, ``torso <1>`` and ``head <1>``
     - the assembly tree
   * - mates
     - one, named ``head to neck``
     - **Mate features**
   * - the torso
     - fixed
     - the hatched ground mark on its row
   * - the torso's connectors
     - five, listed by name
     - open ``torso <1>``
   * - the head's socket
     - on the middle line, 58 mm up
     - Measure, on the hollow ball
   * - the head at rest
     - square on the stud
     - the graphics area

.. admonition:: 104 is a number nobody typed
   :class: advice

   The head's hollow sits 46 mm below the head's middle, in its tab. The neck ball sits 58 mm above
   the torso's middle, in its tab. The Ball mate makes those two points one point, so the head's
   middle lands 104 mm above the torso's.

   Nothing in that chain was typed twice. That is what building each part around its own joint
   center buys you, and it is why the guide keeps saying to build around the joint.

The head turns and the arms do not exist yet. The pages after this one build a limb, and the limb is
built out of the same joint you have already made twice.

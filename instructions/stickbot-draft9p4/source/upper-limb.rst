The upper limb, built out of two joints you already have
=========================================================

This is the arm above the elbow and the leg above the knee. You build it once and the assembly
uses it four times.

Almost none of it is new. The socket comes from page 4 and the fork comes from page 9, and both
are copied in whole. The only shape drawn on this page is one circle, and the only thing grown
from it is a plain round rod between the two joints.

Open ``stickbot``. You will make a new tab called ``u limb``.

.. step: cad.hero
.. req: req.page.hero

.. figure:: images/u-limb/hero-01.png
   :alt: the finished upper limb from a corner: a socket cup at the top, a plain round rod, and
         the hinge's two-eared fork at the bottom
   :width: 1130px
   :class: shot

   **The upper limb at the end of this page.** One part, 24 mm across from end to end. The socket
   is at the top, the fork is at the bottom, and the rod between them is the only thing you draw.

.. figure:: images/u-limb/hero-02.png
   :alt: the same limb from the front, where the socket, the rod and the fork read as one straight
         line of three parts
   :width: 1130px
   :class: shot

   **The same limb from the front.** The fork's ears are the same 24 mm across as the rod, so they
   do not stick out. The joint is buried in the limb rather than bolted onto it.

Make a Part Studio for the limb
--------------------------------

.. step: cad.parts.u_limb.tab
.. req: req.model.one_document

Click the **+** at the bottom left of the tab strip and choose **Create Part Studio**.

.. image:: images/toolbar/tb-new-tab.png
   :alt: Close-up of the plus button at the bottom left of the tab strip, its tooltip reading
         Insert new tab
   :class: button

.. image:: images/u-limb/parts.u_limb.tab-01.png
   :alt: the plus menu open at the bottom left, Create Part Studio above Create Assembly
   :class: shot

Right-click the new tab and choose **Rename**.

.. image:: images/u-limb/parts.u_limb.tab-02.png
   :alt: the right-click menu on the new Part Studio tab, with Rename on it
   :class: shot

Type ``u limb``.

.. image:: images/u-limb/parts.u_limb.tab-03.png
   :alt: the tab strip alone, with u limb at the end of it
   :class: shot

One number before any drawing
------------------------------

.. step: cad.parts.u_limb.variables
.. req: req.model.derive
.. req: req.page.typed_values

The hinge page needed twenty rows. This page needs one. Everything else it uses is a number the
document already knows: the sizes in ``robot sizes``, and the two joints, which arrive at whatever
size they were built at.

Open **Variable**. Leave the type on **Length**.

.. image:: images/u-limb/parts.u_limb.variables-01.png
   :alt: the Variable dialog open, its type on Length and its Name and Value boxes empty
   :class: shot

.. list-table::
   :header-rows: 1
   :widths: 22 34 44

   * - Name
     - Value
     - What it is
   * - ``#limbD``
     - ``#torsoH / 4``
     - 24 mm, the round bar every limb is made at

.. image:: images/u-limb/parts.u_limb.variables-02.png
   :alt: limbD typed into the Name box and #torsoH / 4 into the Value box, so the rod is a quarter
         of the torso's height across
   :class: shot

The row goes in above **Default geometry**, at the head of the feature list.

.. image:: images/u-limb/parts.u_limb.variables-03.png
   :alt: the feature tree with limbD standing above Default geometry
   :class: shot

Copy the socket in
-------------------

.. step: cad.parts.u_limb.socket.derive
.. req: req.model.derive

**Derive** copies a part out of one Part Studio into another. The copy keeps its link to the
source, so a change to the socket on page 4 reaches every limb that uses it.

Open **Derived**. The **Part Studio** button is red and empty until you say which one.

.. image:: images/toolbar/tb-derived.png
   :alt: Close-up of the Derived button in the toolbar, its tooltip reading Derived
   :class: button

.. image:: images/u-limb/parts.u_limb.socket.derive-01.png
   :alt: the Derived dialog open, its Part Studio button red and empty and Placement reading Base
         origin
   :class: shot

Click it. A panel opens on this document, with a row for every Part Studio in it.

.. image:: images/u-limb/parts.u_limb.socket.derive-02.png
   :alt: the Select Part Studio panel open on this document, with a row for every Part Studio in it
   :class: shot

Click the arrow beside ``ball and socket``. Its parts appear indented underneath.

.. image:: images/u-limb/parts.u_limb.socket.derive-03.png
   :alt: the ball and socket studio opened in the panel, its two parts listed under it
   :class: shot

Click ``Socket body``, and only that. The parts list behind the panel goes to one part.

.. image:: images/u-limb/parts.u_limb.socket.derive-04.png
   :alt: Socket body picked in the panel, and the parts list behind it now holding one part
   :class: shot

.. admonition:: Click the part, not the studio
   :class: advice

   Clicking the studio's own row brings in every part it holds. If the parts list jumps to four
   where you expected one, that is what happened. Click the single indented part row instead.

Leave **Placement** on **Base origin** and **Include mate connectors** ticked.

.. image:: images/u-limb/parts.u_limb.socket.derive-05.png
   :alt: the Derived dialog with ball and socket in its Part Studio box, Placement on Base origin
         and Include mate connectors ticked
   :class: shot

Name it ``add socket``.

.. image:: images/u-limb/parts.u_limb.socket.derive-06.png
   :alt: add socket typed into the dialog's name box
   :class: shot

The socket lands at this tab's origin with its cup opening upward and its collar below.

.. image:: images/u-limb/parts.u_limb.socket.derive-07.png
   :alt: the socket alone at the origin, its cup opening upward and its collar below, with add
         socket the last row in the tree
   :class: shot

.. admonition:: Base origin means "put it where it was built"
   :class: advice

   Page 4 built the socket with its ball center on its own origin. A derive at base origin lands
   that ball center on this tab's origin. The joint arrives in the right place, and there is
   nothing to move it with. The connector that came in with it, ``socket connect to robot``, is
   nested under ``add socket`` in the feature list.

Draw the limb's circle on the collar's underside
-------------------------------------------------

.. step: cad.parts.u_limb.section_sketch
.. req: req.model.sketch_defined

The rod grows out of the socket's own face, not off a plane. That way the rod hangs on a real face
of a real part: if the socket ever changes size, the face moves and the rod follows it.

Turn the model over and click the round underside of the socket's collar.

.. image:: images/u-limb/parts.u_limb.section_sketch-01.png
   :alt: the model seen from below, the round underside of the socket's collar picked and
         highlighted
   :class: shot

Open **Sketch**. The view looks straight at the face you picked.

.. image:: images/toolbar/tb-sketch.png
   :alt: Close-up of the Sketch button in the toolbar, its tooltip reading Sketch
   :class: button

.. image:: images/u-limb/parts.u_limb.section_sketch-02.png
   :alt: an empty sketch open on the collar's underside, looking straight at it
   :class: shot

Draw a **circle**. Put it anywhere for now; the next two steps say where it goes and how big it is.

.. image:: images/toolbar/tb-circle.png
   :alt: Close-up of the Circle button in the sketch toolbar, its tooltip reading Circle
   :class: button

.. image:: images/u-limb/parts.u_limb.section_sketch-03.png
   :alt: a circle drawn out to one side of the origin, the wrong size and in the wrong place
   :class: shot

Drag the circle's center onto the sketch origin until the two snap together. The rod then grows
straight down the middle of the socket.

.. image:: images/u-limb/parts.u_limb.section_sketch-04.png
   :alt: the circle pulled onto the origin, so the rod grows straight down the middle of the socket
   :class: shot

**Dimension** the circle across and type ``#limbD``. The box reads 24 mm.

.. image:: images/toolbar/tb-dimension.png
   :alt: Close-up of the Dimension button in the sketch toolbar, its tooltip reading Dimension
   :class: button

.. image:: images/u-limb/parts.u_limb.section_sketch-05.png
   :alt: the circle dimensioned across at #limbD, reading 24 mm, which is a quarter of the torso's
         height
   :class: shot

The circle turns black. Its place is held by the origin and its size is held by the dimension, so
there is nothing left to drag. Name the sketch ``limb section``.

.. image:: images/u-limb/parts.u_limb.section_sketch-06.png
   :alt: the finished circle, drawn in black because its place and its size are both held
   :class: shot

Grow the rod down from the socket
----------------------------------

.. step: cad.parts.u_limb.body
.. req: req.model.derive

Open **Extrude** with the sketch showing.

.. image:: images/toolbar/tb-extrude.png
   :alt: Close-up of the Extrude button in the toolbar, its tooltip reading Extrude
   :class: button

.. image:: images/u-limb/parts.u_limb.body-01.png
   :alt: the Extrude dialog open on New with nothing picked yet
   :class: shot

Click the circle. Onshape sees a solid touching the sketch and switches the dialog to **Add**,
with the socket already in its merge scope.

.. image:: images/u-limb/parts.u_limb.body-02.png
   :alt: the sketch picked, and the dialog switched itself to Add with the socket in its merge
         scope
   :class: shot

Press **New**. The rod comes out as a part of its own and the merge scope goes away. The three
bodies get welded later, in one step you can see and check.

.. image:: images/u-limb/parts.u_limb.body-03.png
   :alt: New pressed again, so the rod comes out as a part of its own and the merge scope goes away
   :class: shot

Set **Blind** and type ``#limbCenter - #collar - #limbD / 2`` in the depth box. It comes to 27 mm.
Check the arrow points **away** from the socket before you accept.

.. image:: images/u-limb/parts.u_limb.body-04.png
   :alt: the depth typed as #limbCenter - #collar - #limbD / 2, which the box works out to 27 mm,
         and the preview growing down away from the socket rather than up through its cup
   :class: shot

Name it ``limb``.

.. image:: images/u-limb/parts.u_limb.body-05.png
   :alt: the socket standing on top of a plain round rod, with limb the last row in the tree
   :class: shot

.. admonition:: Where the 27 comes from
   :class: advice

   ``#limbCenter`` is 48 mm, and it is the distance the assembly wants between the two joint
   centers. The rod does not carry all of it. The collar already reaches ``#collar``, 9 mm, below
   the ball center, and the fork's ears put their pin ``#limbD / 2``, 12 mm, past the end of the
   rod. What is left for the rod is 48 less 9 less 12, which is 27.

   Typing the rule rather than the 27 is what makes the limb hold together. Change the ball size
   in ``robot sizes`` and the collar changes, the rod changes with it, and the two joint centers
   stay 48 mm apart.

A connector for the fork to land on
------------------------------------

.. step: cad.parts.u_limb.fork_connector
.. req: req.model.anchored

The fork arrives at the origin, which is not where it belongs. Onshape's neatest way to move a
body is to say "put *this* point on *that* point", so the rod needs a point at the end where the
fork goes.

Open **Mate connector**.

.. image:: images/toolbar/tb-mate-connector.png
   :alt: Close-up of the Mate connector button in the toolbar, its tooltip reading Mate connector
   :class: button

.. image:: images/u-limb/parts.u_limb.fork_connector-01.png
   :alt: the Mate connector dialog open, waiting for the entity it is to sit on
   :class: shot

Click the flat face at the far end of the rod, the one furthest from the socket. The connector's
three axes stand at the middle of it.

.. image:: images/u-limb/parts.u_limb.fork_connector-02.png
   :alt: the rod's far end face picked, and the connector's three axes drawn at the middle of it
   :class: shot

Untick **Owner entity**, and name it ``mate for fork``. This connector is a target for the move
that comes next and nothing else, so it belongs to the tab rather than to any one part.

.. image:: images/u-limb/parts.u_limb.fork_connector-03.png
   :alt: Owner entity unticked, so the connector belongs to the tab rather than to any one part
   :class: shot

.. image:: images/u-limb/parts.u_limb.fork_connector-04.png
   :alt: the whole limb from the corner, the socket at the top and the new connector on the flat
         end at the bottom
   :class: shot

.. image:: images/u-limb/parts.u_limb.fork_connector-05.png
   :alt: the same connector close up, its three axes standing on the middle of the rod's flat end
   :class: shot

Copy the fork in
-----------------

.. step: cad.parts.u_limb.fork.derive
.. req: req.model.derive

Open **Derived** again.

.. image:: images/u-limb/parts.u_limb.fork.derive-01.png
   :alt: the Derived dialog open again, its Part Studio button red and empty
   :class: shot

Open the ``hinge`` studio in the panel. Its two parts appear underneath.

.. image:: images/u-limb/parts.u_limb.fork.derive-02.png
   :alt: the hinge studio opened in the panel, its two parts listed under it
   :class: shot

Click the fork. The blade is the other one, and it belongs on the limb below this one.

.. image:: images/u-limb/parts.u_limb.fork.derive-03.png
   :alt: Part 2 picked in the panel, which is the fork; Part 1 is the blade and belongs on the limb
         below this one
   :class: shot

Leave **Placement** on **Base origin** and **Include mate connectors** ticked, and name it
``add fork``.

.. image:: images/u-limb/parts.u_limb.fork.derive-04.png
   :alt: the Derived dialog with hinge in its Part Studio box, Placement on Base origin and Include
         mate connectors ticked
   :class: shot

It lands across the limb at the origin, with its ears through the socket. Base origin put it where
the hinge tab built it, which is right for the socket and wrong for the fork.

.. image:: images/u-limb/parts.u_limb.fork.derive-05.png
   :alt: the fork sitting across the limb at the origin, its ears through the socket, which is
         where the hinge tab built it and not where it belongs
   :class: shot

Move the fork onto the connector
---------------------------------

.. step: cad.parts.u_limb.fork.place
.. req: req.model.anchored

Open **Transform**.

.. image:: images/toolbar/tb-transform.png
   :alt: Close-up of the Transform button in the toolbar, its tooltip reading Transform
   :class: button

.. image:: images/u-limb/parts.u_limb.fork.place-01.png
   :alt: the Transform dialog open, its entity box empty and its type on the first thing in the
         list
   :class: shot

Click the fork, taking it by its arm. That is the part of it nothing else is near, so a click
there cannot land on the socket by mistake.

.. image:: images/u-limb/parts.u_limb.fork.place-02.png
   :alt: the fork picked as the thing to move, taken by its arm because that is the part of it
         nothing else is near
   :class: shot

Set the type to **By mate connectors**. Two boxes open: a point to move from, and a point to move
to.

.. image:: images/u-limb/parts.u_limb.fork.place-03.png
   :alt: the type set to by mate connectors, which asks for a point to move from and a point to
         move to
   :class: shot

Pick ``fork to robot`` in the feature list for the first box. It is nested under
``add fork``, because it came in with the fork rather than being built here.

.. image:: images/u-limb/parts.u_limb.fork.place-04.png
   :alt: fork to robot picked in the feature list, into the first of the two boxes
   :class: shot

Pick ``mate for fork`` for the second box.

.. image:: images/u-limb/parts.u_limb.fork.place-05.png
   :alt: mate for fork picked in the feature list, into the second of the two boxes
   :class: shot

The preview shows the fork turned to face back up the rod, with its ears inside the limb.

.. image:: images/u-limb/parts.u_limb.fork.place-06.png
   :alt: the preview with no flip on it: the fork has turned to face back up the rod, so its ears
         sit inside the limb
   :class: shot

Tick **Flip primary axis**. The fork turns around and stands off the end of the rod with its ears
clear. Name it ``move fork``.

.. image:: images/u-limb/parts.u_limb.fork.place-07.png
   :alt: the flip pressed, and the fork now standing off the end of the rod with its ears clear
   :class: shot

.. image:: images/u-limb/parts.u_limb.fork.place-08.png
   :alt: the limb with a socket at one end and a fork at the other, still three parts
   :class: shot

.. admonition:: The flip is not a fudge
   :class: advice

   Both connectors point their blue Z arrow out of their own part. Land one on the other as they
   are and the two parts grow back through each other. The flip turns one of them around so they
   grow apart instead. If you are ever unsure which way it goes, look at the preview without the
   flip, then tick it and look again.

Weld the three into one part
-----------------------------

.. step: cad.parts.u_limb.combine
.. req: req.model.one_part

Open **Boolean** and set it to **Union**.

.. image:: images/toolbar/tb-boolean.png
   :alt: Close-up of the Boolean button in the toolbar, its tooltip reading Boolean
   :class: button

.. image:: images/u-limb/parts.u_limb.combine-01.png
   :alt: the Boolean dialog open on Union, its Tools box empty
   :class: shot

Click the socket, the rod and the fork in the graphics area, one at a time.

.. image:: images/u-limb/parts.u_limb.combine-02.png
   :alt: the socket clicked in the graphics area, into the Tools box
   :class: shot

.. image:: images/u-limb/parts.u_limb.combine-03.png
   :alt: the rod clicked in the graphics area, into the Tools box
   :class: shot

.. image:: images/u-limb/parts.u_limb.combine-04.png
   :alt: the fork clicked in the graphics area, into the Tools box
   :class: shot

Name it ``combine parts``.

.. image:: images/u-limb/parts.u_limb.combine-05.png
   :alt: the Boolean dialog with combine parts typed into its name box
   :class: shot

The parts list reads **Parts (1)**.

.. image:: images/u-limb/parts.u_limb.combine-06.png
   :alt: the finished limb, one part, with Parts (1) under the feature list
   :class: shot

.. admonition:: The count is the check
   :class: advice

   A union that did not take leaves two or three parts and a model that looks exactly right from
   outside. **Parts (1)** is the cheapest thing to look at in Onshape, and it costs one glance.

Give the part its name
-----------------------

.. step: cad.parts.u_limb.rename
.. req: req.model.named

The one part the union left is still carrying the socket's name.

.. image:: images/u-limb/parts.u_limb.rename-01.png
   :alt: the one part the Boolean left, still carrying the socket's name Socket body
   :class: shot

Double-click it in the parts list and type ``u limb``. The assembly will show this name four times
over, once for each arm and each leg.

.. image:: images/u-limb/parts.u_limb.rename-02.png
   :alt: the part now called u limb, which is the name the assembly will show four times over
   :class: shot

The shoulder end
-----------------

.. step: cad.parts.u_limb.shoulder_connector
.. req: req.model.anchored

The limb is finished as a shape. What it still needs is a named point at each joint for the
assembly to mate to.

Open **Mate connector**.

.. image:: images/u-limb/parts.u_limb.shoulder_connector-01.png
   :alt: the Mate connector dialog open, waiting for the thing the connector is to sit on
   :class: shot

Click **Origin** at the head of the feature list. The socket's ball center is already there, so
the origin is the point you want.

.. image:: images/u-limb/parts.u_limb.shoulder_connector-02.png
   :alt: Origin picked at the head of the feature list, which is where the socket's ball center
         already is
   :class: shot

Name it ``shoulder end``.

.. image:: images/u-limb/parts.u_limb.shoulder_connector-03.png
   :alt: the dialog with shoulder end typed into its name box
   :class: shot

.. image:: images/u-limb/parts.u_limb.shoulder_connector-04.png
   :alt: the limb with a small set of axes at the ball, marking the shoulder end
   :class: shot

.. admonition:: Why the origin, and not the cup
   :class: advice

   You might expect to click inside the cup and get its center. A hollow sphere does not offer
   one. It offers the point you clicked, or the center of the mouth circle if you click near the
   axis. Building the part around the origin is what turns this step into a single click.

The elbow end
--------------

.. step: cad.parts.u_limb.elbow_connector
.. req: req.model.anchored

The elbow turns about the pin that runs through both of the fork's ears. Nothing on the part sits
on that pin: there is a hole through each ear, and the axis runs down the middle of the air
between them. So this connector takes two picks rather than one, and Onshape puts it half way
between them.

Turn the limb until the fork's two ears fill the window. Each has a hole through it, and the two
holes face opposite ways.

.. image:: images/u-limb/parts.u_limb.elbow_connector-01.png
   :alt: the fork's two ears filling the window, each with a hole through it, before the dialog is
         opened
   :class: shot

Open **Mate connector** and change the type from **On entity** to **Between entities**. A second
box opens under the first, so there is one box for each hole.

.. image:: images/u-limb/parts.u_limb.elbow_connector-02.png
   :alt: the dialog with its type set to Between entities, so there are two boxes to pick a hole
         into
   :class: shot

Look straight at the near ear from outside the fork, then turn a little off the pin, so the round
wall inside the hole comes into view. Click that wall.

.. image:: images/u-limb/parts.u_limb.elbow_connector-03.png
   :alt: a close view into the hole through the near ear, with the round wall inside it clicked
   :class: shot

Turn the model right around, so the ear that was hidden behind the first one now faces you.

.. image:: images/u-limb/parts.u_limb.elbow_connector-04.png
   :alt: the same fork seen from the other side, so the ear that was hidden behind the first one
         now faces you
   :class: shot

Turn off the pin by the same amount again, and click that hole's wall the same way.

.. image:: images/u-limb/parts.u_limb.elbow_connector-05.png
   :alt: a close view into the hole through the far ear, with the round wall inside it clicked
   :class: shot

The connector jumps to the middle of the two, on the pin.

.. image:: images/u-limb/parts.u_limb.elbow_connector-06.png
   :alt: the dialog now reading Between entities, with the connector drawn halfway between the two
         holes on their shared axis
   :class: shot

Name it ``elbow end``.

.. image:: images/u-limb/parts.u_limb.elbow_connector-07.png
   :alt: the dialog with elbow end typed into its name box
   :class: shot

The limb now has a connector at each end: one at the ball, and one on the hinge axis.

.. image:: images/u-limb/parts.u_limb.elbow_connector-08.png
   :alt: the finished limb with a connector at each end: one at the ball and one on the hinge axis
   :class: shot

.. admonition:: Both clicks have to mean the same end
   :class: advice

   A hole is a round wall, and a click on that wall tells Onshape "one end of this hole" rather
   than "this hole". The end it takes is the one nearest your eye. Look into each hole from
   outside its own ear and both clicks mean the outer end. The two outer ends are the same
   distance either side of the middle, so half way between them is the pin.

   Click one hole from outside and the other through the gap between the ears, and the two ends
   disagree. The connector then lands about 3 mm off the pin, and nothing on screen says so: it
   is drawn as a triad on the axis either way. **Measure** from the connector to each ear's
   outside face. The two numbers should match.
.. step: cad.tree

The whole page reads down the feature list. The one variable comes first. Then the socket, derived
in. Then the sketch and the extrude that make the rod, and the connector the fork lands on. Then
the fork, derived in and moved. Then the weld, and the two ends.

.. image:: images/u-limb/tree-01.png
   :alt: the whole feature list: the one variable, then the socket derived in, the sketch and the
         extrude that make the rod, the connector, the fork derived in and moved, the union, and
         the two ends
   :class: shot

Each derive brought the source's own mate connector in with it. ``socket connect to robot`` is
nested under ``add socket`` and ``fork to robot`` under ``add fork``, and neither was
built here.

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

.. image:: images/u-limb/version-01.png
   :alt: the Create version from Main dialog with the name Onshape offers already in the Name box
         and selected
   :class: shot

Type ``tutorial 10 - the upper limb``, then click **Create**.

.. image:: images/u-limb/version-02.png
   :alt: the same dialog with tutorial 10 - the upper limb typed into the Name box
   :class: shot

The new version is at the top of the ``Versions and history`` panel.

.. image:: images/u-limb/version-03.png
   :alt: the Versions and history panel listing Main with tutorial 10 - the upper limb at the top,
         above the nine tutorials before it
   :class: shot

What you should be able to read off the limb
---------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Check
     - Expected
     - Where to look
   * - parts in the tab
     - one
     - the parts list
   * - the widest the limb gets
     - 24 mm
     - **Measure** across the rod
   * - the rod's own length
     - 27 mm
     - open ``limb``; the box holds the rule, not the number
   * - shoulder end to elbow end
     - 48 mm
     - **Measure** between the two connectors
   * - the limb end to end
     - 61.95 mm
     - **Measure** from the cup's rim to the fork's round end
   * - both new connectors
     - black, not red
     - the end of the feature list

.. admonition:: The limb is longer than the two joints are apart
   :class: advice

   48 mm is the distance between the joint centers, and it is the number the assembly cares
   about. The part itself is longer, because the socket stands proud at one end and the fork's
   ears reach past the pin at the other. Both numbers are real and they measure different things.

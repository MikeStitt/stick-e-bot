The ball and socket, one studio and two parts
==============================================

This page builds the joint the whole robot is made of. One Part Studio makes two parts: a ball on
a short stalk, and a socket with a ball-shaped hole in it. The head, both arms, both legs and the
grippers all end in a copy of one or the other.

.. step: cad.hero
.. req: req.page.hero

.. figure:: images/ball-and-socket/hero-03.png
   :alt: both halves of the joint together, the stalk standing out of the socket's mouth
   :width: 1130px
   :class: shot

   **The joint at the end of this page.** Press **shift+7** for the corner view. The ball is inside
   the socket and only the stalk shows. The two parts are drawn in one studio because the hole is
   cut with the ball itself, so the two shapes can never disagree.

Hide one part and then the other to look at each half on its own. The stud is a sphere on a stalk
with a flat top, and that flat top is where a limb will attach.

.. figure:: images/ball-and-socket/hero-01.png
   :alt: the ball stud on its own, a sphere on a short round stalk with a flat top
   :width: 1130px
   :class: shot

   **The ball stud.** 12 mm across the ball, and 10 mm from the middle of the ball to the top of
   the stalk.

The socket is a round collar with the hole in it and four slits down its rim. The slits are what
let the mouth spread open as the ball goes in.

.. figure:: images/ball-and-socket/hero-02.png
   :alt: the socket on its own, a round collar with a hollow ball-shaped hole and four slits cut
         down its rim
   :width: 1130px
   :class: shot

   **The socket.** 15.6 mm across and 12.2205 mm tall, with a mouth narrower than the ball behind
   it.

Seven of this joint's numbers go in ``robot sizes`` and five stay in this tab. Nobody types all
twelve at once. Each one goes in just before the feature that reads it, so a number never arrives
with nothing on screen to say what it is for.

.. admonition:: The name in the title bar is not the one you typed
   :class: advice

   The pictures come from the documents this guide was built and checked in, and those have
   longer names than yours. Yours reads ``stickbot``. Everything else in the pictures is what
   you will see.

Make a Part Studio for the joint
---------------------------------

.. step: cad.parts.ball_and_socket.tab
.. req: req.model.one_document

Click the **+** at the bottom left of the tab strip and choose **Create Part Studio**.

.. image:: images/toolbar/tb-new-tab.png
   :alt: Close-up of the plus button at the bottom left of the tab strip, its tooltip reading
         Insert new tab
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.tab-01.png
   :alt: the tab strip's plus menu open, with Create Part Studio ringed
   :class: shot

You land in a new, empty Part Studio called ``Part Studio 1``. Its feature list holds
``Default geometry`` and no parts.

.. image:: images/ball-and-socket/parts.ball_and_socket.tab-02.png
   :alt: the new empty Part Studio, its tab called Part Studio 1 and its feature list holding only
         Default geometry
   :class: shot

Right-click the tab, choose **Rename**, and type ``ball and socket``. The new tab goes in beside
the one you were on, so the strip reads ``stickbot``, ``body``, ``head``, ``ball and socket`` and
``robot sizes``.

.. image:: images/ball-and-socket/parts.ball_and_socket.tab-03.png
   :alt: the tab strip with ball and socket on it, between head and robot sizes
   :class: shot

Name the ball, the stand and the stalk
---------------------------------------

.. step: cad.parts.ball_and_socket.stud.variables
.. req: req.model.derive, req.page.typed_values

The head kept its numbers in its own tab, because no other part reads them. This joint is the
other case. The torso, both limbs, the foot and the gripper all build a stud or a collar, so the
numbers they share go in ``robot sizes`` and only the ones this tab alone reads stay here.

Open the ``robot sizes`` tab. It holds the three rows page 1 put there, with an empty row under
them.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.variables-01.png
   :alt: the robot sizes table holding the three rows tutorial 1 typed, with an empty row under
         them
   :class: shot

Type these two into that empty row, one at a time. A new empty row appears under each one you
finish.

.. list-table::
   :header-rows: 1
   :widths: 16 32 52

   * - Name
     - Value
     - What it is
   * - ``ball``
     - ``#torsoH / 8``
     - how wide the ball is
   * - ``stand``
     - ``#ball * 5 / 6``
     - how far the stud stands off the face it is built on

The table fills in the answers as you go: ``ball`` 12 mm and ``stand`` 10 mm.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.variables-02.png
   :alt: the table with ball reading 12 mm and stand reading 10 mm under the three from tutorial 1
   :class: shot

Go back to the ``ball and socket`` tab. The stalk's width is this tab's own business, because
nothing outside it reads that number. Click **Search tools** at the right of the toolbar, or press
**alt/⌥+c**, type ``variable``, and pick **Variable**. Type ``stalk`` into **Name** and
``#ball / 2`` into **Value**, then press **Tab**. The title at the top of the dialog reads
``#stalk = 6 mm``. Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.variables-03.png
   :alt: the Variable dialog in the ball and socket tab, its title reading #stalk = 6 mm, stalk in
         the Name box and #ball / 2 in the Value box
   :class: shot

The row lands in the feature list under ``Default geometry``, reading its own name and its own
value.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.variables-04.png
   :alt: the ball and socket feature list with one row under Default geometry, reading
         #stalk = 6 mm
   :class: shot

.. admonition:: Keep one name in one place
   :class: advice

   A tab may declare a name that ``robot sizes`` already uses, and then the tab quietly keeps its
   own value while the table moves without it. Nothing turns red when that happens. So a number
   two tabs read is a row in ``robot sizes``, and a number one tab reads is that tab's own.

Draw the stud's profile
------------------------

.. step: cad.parts.ball_and_socket.stud.profile_sketch
.. req: req.model.design_intent, req.page.view_keys

A revolve spins a flat shape about a line. Half a ball with a stalk on it, spun about the stalk's
middle, gives you the whole stud. Click the **Front** plane in the feature list.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-01.png
   :alt: the empty ball and socket studio with the Front plane ringed in the feature list and lit
         up in the graphics area
   :class: shot

Click **Sketch**.

.. image:: images/toolbar/tb-sketch.png
   :alt: Close-up of the Sketch button at the left of the Part Studio toolbar, its tooltip reading
         Create new sketch shift+s
   :class: button

Press **n** to look square on at the plane, so what you draw is what you see. A plane has two
square-on views and **n** goes from one to the other, so press it again if the plane's name reads
backwards. Then name the sketch ``stud profile`` from the pencil beside the dialog's title.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-02.png
   :alt: the sketch dialog titled stud profile, its plane field reading Front
   :class: shot

Open the dropdown beside the arc button, choose **Center point arc**, and put the pointer on the
origin.

.. image:: images/toolbar/tb-arc.png
   :alt: Close-up of the arc button in the sketch toolbar, its tooltip reading 3 point arc a
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-03.png
   :alt: the center point arc tool armed, the pointer on the origin
   :class: shot

Click the origin for the arc's center. Start the arc on the vertical axis below it, then sweep it
round to the right and up.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-04.png
   :alt: an arc centered on the origin, starting on the vertical axis below it and sweeping round
         to the right and up
   :class: shot

Now close the shape with three lines. One runs up the side of the stalk. One runs across the top.
The last runs back down the vertical axis, to where the arc began.

.. image:: images/toolbar/tb-line.png
   :alt: Close-up of the line button in the sketch toolbar, its tooltip reading Line l
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-05.png
   :alt: the profile closed: the arc at the bottom, a short line up the side of the stalk, one
         across the top and one down the axis
   :class: shot

Three dimensions hold it. Put the first on the arc and type ``#ball / 2``, so the ball is a radius
of half its own width. It reads 6.

.. image:: images/toolbar/tb-dimension.png
   :alt: Close-up of the dimension button in the sketch toolbar, its tooltip reading Dimension d
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-06.png
   :alt: the arc dimensioned and reading 6, so the ball is half its own width across
   :class: shot

Put the second on the line across the top and type ``#stalk / 2``. That line is a radius too, so
the stalk finishes ``#stalk`` across. It reads 3.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-07.png
   :alt: the line across the top dimensioned and reading 3, half the stalk's width
   :class: shot

Put the third between the origin and the line across the top, and type ``#stand``. That is how far
the stud stands off whatever it is built on, measured from the middle of the ball. It reads 10, and
every line goes black.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-08.png
   :alt: the third dimension in, from the middle of the ball up to the line across the top, reading
         10, and every line black
   :class: shot

Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.profile_sketch-09.png
   :alt: the feature list reading #stalk and stud profile, with the closed sketch behind it
   :class: shot

Spin it into a ball
--------------------

.. step: cad.parts.ball_and_socket.stud.revolve
.. req: req.model.named_features, req.page.view_keys

Press **shift+1** to look straight at the profile, so the axis is a line you can click. Then open
**Revolve** and name it ``revolve stud``.

.. image:: images/toolbar/tb-revolve.png
   :alt: Close-up of the Revolve button in the Part Studio toolbar, its tooltip reading Revolve
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-01.png
   :alt: the Revolve dialog open, its region field empty and waiting
   :class: shot

Pick ``stud profile`` in the feature list as the region to spin.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-02.png
   :alt: stud profile picked in the feature list, its name now in the Revolve dialog's region field
   :class: shot

The dialog asks for an axis next. Click its second field, **Revolve axis**, so the next thing you
pick lands there rather than in the region field.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-03.png
   :alt: the Revolve dialog's second field, named Revolve axis, about to be clicked so the next
         pick lands in it
   :class: shot

Pick the line that runs up the vertical axis. That is the side the shape spins around, and a
preview of the ball and its stalk appears behind the dialog.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-04.png
   :alt: the line up the axis picked as the axis to spin about, with a preview of the ball and its
         stalk behind the dialog
   :class: shot

Leave the dialog on **New** and **Full**. Full means all the way round, and New means this becomes
a part of its own rather than joining something.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-05.png
   :alt: the Revolve dialog reading New and Full revolve, so the profile goes all the way round and
         becomes a part of its own
   :class: shot

Click the **green ✓**, then press **p** to hide the planes, **shift+7** for the corner view and
**f** to zoom to fit. A round thing reads as round from a corner and reads as a circle from
anywhere else.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-06.png
   :alt: the finished stud seen from the corner: a ball with a short stalk standing out of the top
         of it
   :class: shot

Rename the part underneath the feature: in the parts list, double-click ``Part 1`` and type
``Ball stud``.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.revolve-07.png
   :alt: the parts list reading Ball stud instead of Part 1
   :class: shot

Name the wall the collar is made of
------------------------------------

.. step: cad.parts.ball_and_socket.collar.wall_variable
.. req: req.model.derive

The circle you are about to draw asks how thick the material round the ball is, so that number goes
in first. It is a ``robot sizes`` row: the foot and the gripper build collars of their own and read
the same wall.

Open ``robot sizes`` and type ``wall`` into the empty Name cell.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.wall_variable-01.png
   :alt: the table with wall typed into the Name cell and its Value cell empty, waiting
   :class: shot

Type ``#torsoH * 3 / 160`` into its Value cell. It comes to 1.8 mm.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.wall_variable-02.png
   :alt: the table with wall reading 1.8 mm under ball and stand
   :class: shot

Draw the collar's circle
-------------------------

.. step: cad.parts.ball_and_socket.collar.profile_sketch
.. req: req.model.derive, req.page.view_keys

The socket starts as a plain cylinder round the ball. Go back to ``ball and socket``, click the
**Top** plane in the feature list and start a sketch on it. The Top plane cuts through the middle
of the ball, which is exactly where the widest part of the hole has to be.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-01.png
   :alt: the ball stud seen from the corner with Top picked in the feature list, the plane it names
         still hidden
   :class: shot

Press **n** to look straight down at it, again pressing it a second time if you land on the far
side, and name the sketch ``collar profile``.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-02.png
   :alt: the sketch dialog titled collar profile, its plane field reading Top
   :class: shot

Choose the circle tool and put the pointer on the origin.

.. image:: images/toolbar/tb-circle.png
   :alt: Close-up of the circle button in the sketch toolbar, its tooltip reading Center point
         circle c
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-03.png
   :alt: the circle tool armed, the pointer on the origin
   :class: shot

Click the origin for the center and drag out past the edge of the ball.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-04.png
   :alt: a circle centered on the origin and drawn out past the edge of the ball
   :class: shot

Dimension it ``(#ball / 2 + #wall) * 2``. The dimension is a diameter and the bracket is a radius:
half the ball, plus one wall of material round it. So the circle comes out as the ball plus a wall
each side, and reads 15.6.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-05.png
   :alt: the circle black and fully defined, reading 15.6 across
   :class: shot

Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.profile_sketch-06.png
   :alt: the feature list with collar profile under revolve stud, and the circle drawn round the
         ball
   :class: shot

Name the four numbers that hold the ball in
--------------------------------------------

.. step: cad.parts.ball_and_socket.collar.grip_variables
.. req: req.model.derive, req.page.typed_values

The extrude you are about to make asks how far the collar goes up and how far it goes down, and
the answer to the first one is worked out from two printing numbers. All four rows go in
``robot sizes``.

Open ``robot sizes`` and type ``fit`` and ``ballLoss``. Both are typed as lengths, and they are the
only two numbers on this page that are about the printer rather than about the robot: ``#fit`` is
the clearance the printer can hold, and ``#ballLoss`` is what a printed ball loses off its radius.

.. list-table::
   :header-rows: 1
   :widths: 16 44 40

   * - Name
     - Value
     - What it is
   * - ``fit``
     - ``0.08 mm``
     - how much bigger the hole is than the ball, all the way round
   * - ``ballLoss``
     - ``0.10 mm``
     - how much of its radius a printed ball comes out short

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.grip_variables-01.png
   :alt: the table with fit reading 0.08 mm and ballLoss reading 0.1 mm, the two numbers on this
         page that are about the printer
   :class: shot

Now type ``grip``, and give it
``sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball - #ballLoss) ^ 2)``. It comes to 2.2205 mm, worked
out from the two rows above it.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.grip_variables-02.png
   :alt: the table with grip added, its value worked out as 2.2205 mm from the two rows above it
   :class: shot

Last, type ``collar`` and give it ``#stand``. The socket reaches as far below the middle of the
ball as the stud stands above it, which is 10 mm.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.grip_variables-03.png
   :alt: the table with collar reading 10 mm, the last of the seven rows this page adds
   :class: shot

.. admonition:: What the square root is for
   :class: advice

   ``#grip`` is the one row on this page you would not guess. The socket's top face is its mouth,
   and the mouth has to be narrower than the ball or the ball falls out. Onshape has no field for
   *how narrow*, so you set it by choosing where to stop the collar.

   Cut a sphere of radius ``#ball / 2 + #fit`` at a height ``h`` above its middle and the circle
   you get has a radius you can work out with a right triangle. Turn that around and you get the
   line in the table: it is the height that leaves a mouth ``0.96 × #ball - 2 × #ballLoss`` across,
   which is 11.32 mm here. The drawn ball is 12 mm, so 0.34 mm of material lies over it on each
   side; the printed ball comes out 0.10 mm short on its radius, so the pair you hold grips by
   0.24 mm a side. That is 2 % of the ball, so it grows with the robot rather than staying put.

Give the collar its height
---------------------------

.. step: cad.parts.ball_and_socket.collar.extrude
.. req: req.model.design_intent

This extrude goes both ways from the sketch, and the two distances are different. Go back to
``ball and socket``, open **Extrude** and name it ``collar blank``.

.. image:: images/toolbar/tb-extrude.png
   :alt: Close-up of the Extrude button in the Part Studio toolbar, its tooltip reading Extrude
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.extrude-01.png
   :alt: the Extrude dialog open with its region field empty and waiting
   :class: shot

Pick ``collar profile`` in the feature list.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.extrude-02.png
   :alt: collar profile picked in the feature list, its name now in the Extrude dialog's region
         field
   :class: shot

Leave it on **New** and type ``#grip`` into the depth box. That is the short way, up, and it is the
number the square root worked out: stop there and the mouth comes out the right size.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.extrude-03.png
   :alt: New chosen and #grip typed into the depth box, the little the collar stands above the
         middle of the ball
   :class: shot

Tick **Second end position** and type ``#collar`` into the box it opens. That is the long way,
down, and it puts a floor of solid material under the ball.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.extrude-04.png
   :alt: Second end position ticked and #collar typed into the box it opened, so the same circle
         goes down as well as up
   :class: shot

Click the **green ✓**. The collar swallows most of the ball, with the stalk standing out of the
top.

.. image:: images/ball-and-socket/parts.ball_and_socket.collar.extrude-05.png
   :alt: the collar standing round the ball, its top a little above the middle of the ball and its
         body reaching well below
   :class: shot

Take the hole out with the ball itself
---------------------------------------

.. step: cad.parts.ball_and_socket.cavity
.. req: req.model.named_features

A **Boolean** takes one solid out of another. Here the ball is the tool and the collar is the
target, so the hole comes out as a copy of the ball and cannot be any other shape. Open **Boolean**
and name it ``cavity from ball``. It opens on **Union**, with one field asking for tools.

.. image:: images/toolbar/tb-boolean.png
   :alt: Close-up of the Boolean button in the Part Studio toolbar, its tooltip reading Boolean
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-01.png
   :alt: the Boolean dialog open on Union, with one field called Tools
   :class: shot

Choose **Subtract**, the middle of the three words across the top of the dialog. A second field
appears, for what the tools come out of.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-02.png
   :alt: Subtract about to be chosen, the middle of the three words across the top of the Boolean
         dialog
   :class: shot

Pick ``Ball stud`` in the parts list as the tool.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-03.png
   :alt: Ball stud picked in the parts list as the tool, the thing whose shape the hole takes
   :class: shot

Click the **Targets** field, then pick ``Part 2`` in the parts list. That is the collar you just
made.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-04.png
   :alt: Part 2 picked in the parts list as the target, the thing the hole is taken out of
   :class: shot

Tick **Offset** and type ``#fit`` into its box, then tick **Offset all** under it. The hole comes
out 0.08 mm bigger than the ball, everywhere at once. Without it the two parts would be exactly the
same size and the joint would seize. **Keep tools** is already ticked at the foot of the dialog;
leave it that way, because you want the ball to still be there when the hole it made is finished.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-05.png
   :alt: Offset ticked with #fit in its box and Offset all under it, and Keep tools already ticked
         at the bottom of the dialog
   :class: shot

Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-06.png
   :alt: the collar with the ball sunk into it, the stalk standing out of the top and the two parts
         still both in the list
   :class: shot

Rename the second part ``Socket body``. The parts list now holds both halves of the joint, made by
one Part Studio.

.. image:: images/ball-and-socket/parts.ball_and_socket.cavity-07.png
   :alt: the parts list reading Ball stud and Socket body, the two halves of the joint made by one
         studio
   :class: shot

.. admonition:: One shape, used twice
   :class: advice

   This is the reason both parts live in one studio. The hole is the ball, moved out by ``#fit``.
   Change ``#ball`` and both move together, because there is only one sphere in the file and the
   second one is a copy of it made at build time.

   Two studios could hold the same two parts, and then somebody would have to remember to change
   both. Nobody remembers.

Name where the slits start, stop and how wide they are
-------------------------------------------------------

.. step: cad.parts.ball_and_socket.slit.variables
.. req: req.model.derive, req.page.typed_values

The mouth is narrower than the ball, so the ball cannot go in unless the mouth spreads. Four slits
down the rim turn it into four fingers that bend out of the way and spring back. Three numbers
describe one slit, and all three stay in this tab.

Open **Variable** three times in the ``ball and socket`` tab, once for each row below.

.. list-table::
   :header-rows: 1
   :widths: 18 46 36

   * - Name
     - Value
     - What it is
   * - ``slit``
     - ``1.6 mm``
     - how wide the slit is
   * - ``slit_in``
     - ``sqrt((#ball / 2 + #fit) ^ 2 - (#ball / 3) ^ 2) - #wall / 2``
     - how far from the middle the slit starts
   * - ``slit_out``
     - ``#ball``
     - how far from the middle it stops

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.variables-01.png
   :alt: the Variable dialog with slit in the Name box and 1.6 mm in the Value box, its title
         reading #slit = 1.6 mm
   :class: shot

They come to 1.6 mm, 3.67891 mm and 12 mm, and they land in a run under ``cavity from ball``.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.variables-02.png
   :alt: the feature list with #slit, #slit_in and #slit_out in a run under cavity from ball
   :class: shot

``#slit`` is typed, like ``#fit`` and ``#ballLoss``. A slit has to print open and still spring
back, so its width is about the printer too. The other two are worked out: the slit has to start
inside the hole where the cut bottoms out, and finish outside a collar 7.8 mm in radius, and
``#ball`` clears that by 4.2 mm.

Draw four slits
----------------

.. step: cad.parts.ball_and_socket.slit.profile_sketch
.. req: req.model.anchored, req.page.view_keys

Pick the socket's flat top: the ring of metal round the ball's shoulder.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-01.png
   :alt: the socket seen from above with the pointer on its flat top, the ring of metal round the
         ball's shoulder
   :class: shot

Start a sketch on it, press **n** to look straight down at the ring, and name the sketch
``slit profile``. The origin is in the middle of the ring, because the ring is centered on it.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-02.png
   :alt: a new sketch open on the socket's top face, looking straight down at the ring with the
         origin in the middle
   :class: shot

Choose the rectangle tool. You are going to draw one slit, and let Onshape make the other three.

.. image:: images/toolbar/tb-rectangle.png
   :alt: Close-up of the rectangle button in the sketch toolbar, its tooltip reading Corner
         rectangle g
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-03.png
   :alt: the rectangle tool armed, the pointer inside the ring just above the horizontal axis
   :class: shot

Draw a thin rectangle lying along the horizontal axis. Start it inside the ring and finish it out
past the edge of the collar. The exact corners do not matter; four dimensions are about to pin
them.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-04.png
   :alt: one thin rectangle lying along the horizontal axis, starting inside the ring and running
         out past its edge
   :class: shot

Dimension the near end from the origin and type ``#slit_in``. It reads 3.679, which is inside the
mouth.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-05.png
   :alt: the near end dimensioned from the origin and reading 3.679, inside the mouth
   :class: shot

Dimension the far end from the origin and type ``#slit_out``. It reads 12, well past the outside of
the collar.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-06.png
   :alt: the far end dimensioned from the origin and reading 12, past the outside of the collar
   :class: shot

Dimension the upper long side from the origin and type ``#slit / 2``. It reads 0.8.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-07.png
   :alt: the upper long side dimensioned from the origin and reading 0.8
   :class: shot

Do the lower long side the same way, with ``#slit / 2`` again. The rectangle goes black: it is
3.679 to its near end, 12 to its far end and 0.8 above and below the axis, so the slit is 1.6 mm
wide and the axis runs down the middle of it.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-08.png
   :alt: the rectangle black and fully defined, 3.679 to its near end, 12 to its far end and 0.8
         above and below the axis
   :class: shot

.. admonition:: Watch what a dimension moves
   :class: advice

   A rectangle nobody has pinned yet is free to grow and shrink as a whole, so the first dimension
   you put on it moves the ends you have not dimensioned. This is normal and it is worth seeing:
   put the near end in and watch the far end walk away. Pick the lines where they are drawn now,
   not where they were.

Pick all four sides of the rectangle, and nothing else.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-09.png
   :alt: all four sides of the rectangle picked and orange, and nothing else
   :class: shot

Open the pattern menu in the sketch toolbar and choose **Circular pattern**. Three copies appear at
once, spread evenly round the origin. Beside the rectangle you drew, Onshape writes ``3x``.

.. image:: images/toolbar/tb-circular-pattern.png
   :alt: Close-up of the sketch pattern menu open, reading Linear pattern, Circular pattern and
         Transform
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-10.png
   :alt: three copies of the rectangle spread evenly round the origin, with 3x written beside the
         one you drew
   :class: shot

Double-click the ``3x`` and type ``4``. The count is written on the drawing rather than in a panel,
and one click only lights it up; the second click is what turns it into a box you can type in.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-11.png
   :alt: the count beside the rectangle open for editing with 4 typed in
   :class: shot

Press **Enter**. Four rectangles reach out across the ring, a quarter turn apart.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-12.png
   :alt: four rectangles a quarter turn apart, reaching out across the ring in four directions
   :class: shot

.. admonition:: Click empty space, not Escape
   :class: advice

   While the pattern is still live, **Escape** throws it away instead of letting go of it. There is
   no banner and no complaint; the sketch simply goes back to the one rectangle you started from.
   To drop a selection at this point, click an empty part of the sketch. The green ✓ on the sketch
   is what accepts the pattern for good.

The pattern turns round a center point. That point arrives on the origin, but nothing holds it
there. Drag it away and you can see for yourself. The four copies swing off the middle and turn
blue again, and blue means they are still free to move.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-13.png
   :alt: the pattern dragged away from the middle, its center point now sitting off the origin and
         the four copies blue again
   :class: shot

Pick the pattern's center point, then hold **shift** and pick the origin, so both are selected.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-14.png
   :alt: the pattern's center point and the origin both picked
   :class: shot

Apply **Coincident**. The pattern jumps back to the middle and every line goes black. The sketch is
fully defined now: the slits sit where they sit because the origin does.

.. image:: images/toolbar/tb-coincident.png
   :alt: Close-up of the Coincident button in the sketch toolbar, its tooltip reading Coincident i
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-15.png
   :alt: the pattern back in the middle and every line black, so the sketch is fully defined
   :class: shot

Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.profile_sketch-16.png
   :alt: the feature list reading slit profile under #slit_out, with four thin rectangles drawn
         across the socket's top
   :class: shot

Name how deep the slits go
---------------------------

.. step: cad.parts.ball_and_socket.slit.depth_variable
.. req: req.model.derive

The cut you are about to make asks for a depth. Open **Variable**, type ``slit_d`` into **Name**
and ``#grip + #ball / 3`` into **Value**.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.depth_variable-01.png
   :alt: the Variable dialog with slit_d in the Name box and #grip + #ball / 3 in the Value box
   :class: shot

It comes to 6.22054 mm. The cut starts at the top face, which is ``#grip`` above the middle of the
ball, so its floor lands ``#ball / 3`` below the middle: 4 mm here. That leaves a solid ring under
the slits, and the ring is what springs the four fingers shut again.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.depth_variable-02.png
   :alt: the feature list with #slit_d under slit profile, reading 6.2205 mm
   :class: shot

Cut them
---------

.. step: cad.parts.ball_and_socket.slit.extrude
.. req: req.model.design_intent

Pick ``slit profile`` in the feature list and open **Extrude**. It arrives on **New**, which is
what the last extrude left it on, so the four rectangles stand up as four new solids.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.extrude-01.png
   :alt: the Extrude dialog open with slit profile already in its region field, four rectangles
         standing up as four new solids
   :class: shot

Choose **Remove**. The same four rectangles are now drawn as the material they will take out.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.extrude-02.png
   :alt: Remove chosen, so the four rectangles are drawn as the material they will take out
   :class: shot

Type ``#slit_d`` into the depth box. The cut already points down into the collar, because the
sketch is on the collar's top face and down is into the material.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.extrude-03.png
   :alt: #slit_d typed into the depth box, the cut already pointing down into the collar
   :class: shot

Click the **Merge scope** box and pick ``Socket body``. That is what the cut is allowed to take
material from, and naming it leaves the ball alone. Name the feature ``relief slits``.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.extrude-04.png
   :alt: Socket body named in the Merge scope box, so the cut takes material from the socket and
         leaves the ball alone
   :class: shot

Click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.slit.extrude-05.png
   :alt: four slots cut down through the socket's rim, a quarter turn apart, splitting it into four
         fingers that can spread
   :class: shot

.. admonition:: Look at the rim before you carry on
   :class: advice

   A **Remove** with nothing in its merge scope takes material from nothing. It goes green, it says
   nothing, and the feature list looks right. The picture is what catches it: four slots through
   the rim, a quarter turn apart. If the rim is still a plain ring, open ``relief slits`` again and
   put ``Socket body`` in the box.

Put a mate connector on the stud
---------------------------------

.. step: cad.parts.ball_and_socket.stud.connector
.. req: req.shot.two_frame

Every part that uses this joint moves it by a mate connector, so the connectors belong to the
joint. The stud's goes on the flat top of the stalk, which is the face a limb attaches to. Press
**shift+7** for the corner view, then open the Custom features menu in the toolbar and choose
**Mate connector**, near the bottom of a long list.

.. image:: images/toolbar/tb-mate-connector.png
   :alt: Close-up of the Custom features menu open, Mate connector near the bottom with its
         shortcut ctrl m beside it
   :class: button

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.connector-01.png
   :alt: the Mate connector dialog open and waiting, its origin entity box empty
   :class: shot

Click the small flat circle on top of the stud. The connector's three arrows stand up at the middle
of it.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.connector-02.png
   :alt: the small flat circle on top of the stud picked, and the connector's three arrows standing
         at the middle of it
   :class: shot

Name it ``stud connect to robot`` and click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.connector-03.png
   :alt: the connector's three arrows standing on the stud's top face, the whole joint in view
   :class: shot

Zoom in on it. The origin sits on the center of the top face and the blue arrow points up the
stalk, away from the ball.

.. image:: images/ball-and-socket/parts.ball_and_socket.stud.connector-04.png
   :alt: the same connector close up, its origin on the center of the stud's top face and its blue
         arrow pointing up the stalk
   :class: shot

.. admonition:: Onshape says centroid where you said center
   :class: advice

   Click the middle of a flat disc and Onshape writes down *centroid*, which is the balance point
   of the face. On a full circle the balance point and the center are the same place, so the
   connector lands where you meant. Both connectors on this page read centroid, and both are on a
   full disc.

Put one under the socket
-------------------------

.. step: cad.parts.ball_and_socket.socket.connector
.. req: req.shot.two_frame

The socket's connector goes on its flat underside, which is the face the socket sits on. Press
**shift+6** to turn the joint over and look at it from below, then open **Mate connector** again.

.. image:: images/ball-and-socket/parts.ball_and_socket.socket.connector-01.png
   :alt: the Mate connector dialog open and waiting, its origin entity box empty
   :class: shot

Click the flat underside, off to one side rather than dead center. The origin sits at the middle of
that face, and a click there picks the origin, not the face.

.. image:: images/ball-and-socket/parts.ball_and_socket.socket.connector-02.png
   :alt: the socket turned over, its flat underside picked, and the connector standing at the
         middle of that disc
   :class: shot

Name it ``socket connect to robot`` and click the **green ✓**.

.. image:: images/ball-and-socket/parts.ball_and_socket.socket.connector-03.png
   :alt: the connector standing under the socket, the whole joint in view
   :class: shot

Zoom in on it, the same as you did for the stud. Its origin is on the center of the socket's
underside, 10 mm below the middle of the ball.

.. image:: images/ball-and-socket/parts.ball_and_socket.socket.connector-04.png
   :alt: the same connector close up, its origin on the center of the socket's underside
   :class: shot

What the studio holds now
--------------------------

.. step: cad.part_list
.. req: req.model.named_features

The parts list holds both halves of the joint, under the names you gave them. Click ``Ball stud``,
then hold **shift** and click ``Socket body``, and both light up in the graphics area so you can see
which name goes with which shape.

.. image:: images/ball-and-socket/part_list-01.png
   :alt: both parts picked in the parts list, Ball stud and Socket body, so each name is lit
         against the shape it belongs to
   :class: shot

.. step: cad.tree

Above it, the feature list reads back as a story about the joint. Name the stalk, draw the stud,
spin it. Name the wall, draw the collar, give it height. Take the hole out with the ball. Name the
slit, draw it four times, say how deep it cuts, cut it. Name a place on each half.

.. image:: images/ball-and-socket/tree-01.png
   :alt: the whole feature list: the tab's own variables, then stud profile, revolve stud, collar
         profile, collar blank, cavity from ball, slit profile, relief slits and the two mate
         connectors
   :class: shot

Cut it in half and look at the gap
-----------------------------------

.. step: cad.section
.. req: req.shot.true_state, req.page.view_keys

The gap between the ball and the socket is the whole design, and it is inside the part where you
cannot see it. **Section view** cuts the model open on a plane so you can look. Press **shift+7**
for the corner view, then open the view menu beside the view cube; **Section view…** is at the foot
of the list.

.. image:: images/toolbar/tb-section-view.png
   :alt: Close-up of the view menu open, Section view at the bottom of the list
   :class: button

.. image:: images/ball-and-socket/section-01.png
   :alt: the Section view panel open and asking for a plane to cut on
   :class: shot

Pick ``Right`` in the feature list as the plane to cut on. The cut runs through the middle of the
ball.

.. image:: images/ball-and-socket/section-02.png
   :alt: Right taken as the section plane, so the cut runs through the middle of the ball
   :class: shot

Click the **green ✓** to accept the cut, then press **shift+4** to look straight at it. The ball
fills the socket, the stalk stands out of the mouth, and there is a floor of solid material under
the ball.

.. image:: images/ball-and-socket/section-03.png
   :alt: the joint cut in half and seen face-on at a fit of 0.08 mm: the ball fills the socket, the
         stalk stands out of the mouth, and there is a floor of solid material under the ball
   :class: shot

Zoom in on the mouth, where the socket's rim comes over the widest part of the ball.

.. image:: images/ball-and-socket/section-04.png
   :alt: the mouth of the socket up close at 0.08 mm, ringed where the rim comes over the widest
         part of the ball
   :class: shot

There is a gap in that picture. It is 0.08 mm, and at this zoom it is about as thin as the line
Onshape draws an edge with, so it reads as one dark line rather than two edges with a space between
them. That is the right answer. A gap you can see without zooming is a joint that rattles.

.. admonition:: The cut goes through two of the four slits
   :class: advice

   The slits sit at a quarter turn to each other and two of them lie on the ``Right`` plane, so the
   cut passes straight down the middle of those two. That is why the rim looks missing on both
   sides of the mouth: you are looking through a slit at the metal behind it, which is drawn plain
   instead of hatched. Hatching is what Onshape puts on a face the cut actually made.

Prove the gap is real
----------------------

.. step: cad.section.wide
.. req: req.model.design_intent

You cannot see 0.08 mm, so make it ten times bigger for a moment, look, and put it back. This is
worth doing once. It is how you find out whether a number you cannot see is really driving
anything.

Open ``robot sizes`` and change ``fit`` to ``0.8 mm``. ``grip`` moves too, from 2.2205 mm to
3.7689 mm, because it is worked out from ``fit``, and the socket gets taller with it.

.. image:: images/ball-and-socket/section.wide-01.png
   :alt: the fit row in robot sizes typed up to 0.8 mm, ten times the number the joint is really
         built with
   :class: shot

Go back to ``ball and socket``. The cut is gone: a section view belongs to the tab you are looking
at and leaving the tab turns it off. Open the view menu and make the same cut on ``Right`` again,
then press **shift+4**. The gap now runs all the way round the ball, and you can see it.

.. image:: images/ball-and-socket/section.wide-02.png
   :alt: the same cut with the fit at 0.8 mm: the gap between the ball and the socket is now wide
         enough to see all the way round
   :class: shot

Zoom back in on the mouth, the same close-up as before.

.. image:: images/ball-and-socket/section.wide-03.png
   :alt: the mouth at 0.8 mm, at the same scale as the honest close-up and ringed at the same place
         on the part, so the two can be read one after the other
   :class: shot

Those two close-ups are the same size on the same part, so read them one after the other: a dark
line at 0.08 mm, a dark band at 0.8 mm. The gap was always there.

Now put ``fit`` back to ``0.08 mm``. The table reads exactly as it did before you touched it, with
``grip`` back at 2.2205 mm, and so is everything the joint is built from.

.. image:: images/ball-and-socket/section.wide-04.png
   :alt: the fit row back at 0.08 mm, ringed, which is the value everything after this page is
         built with
   :class: shot

.. admonition:: Turn the section off before you carry on
   :class: advice

   A section view stays on until you turn it off. Open the same menu; where it said
   **Section view…** it now says **Turn off section view**.

Publish a version
------------------

.. step: cad.version
.. req: req.page.document

Save the tab as a version, so the pages after this one can point at a joint that will not move
under them. Click **Create version…** in the strip of icons down the far left. The dialog opens
with a name of Onshape's own in the box, selected, so what you type replaces it.

.. image:: images/toolbar/tb-create-version.png
   :alt: Close-up of the Create version button in the left icon strip, its tooltip reading Create
         version…
   :class: button

.. image:: images/ball-and-socket/version-01.png
   :alt: the Create version from Main dialog with the name Onshape offers already in the Name box
         and selected
   :class: shot

Type ``tutorial 4 - the ball and socket``, then click **Create**.

.. image:: images/ball-and-socket/version-02.png
   :alt: the same dialog with tutorial 4 - the ball and socket typed into the Name box
   :class: shot

Open **Versions and history**. The new version is at the top of the list, above the three the
earlier pages left.

.. image:: images/ball-and-socket/version-03.png
   :alt: the Versions and history panel listing Main with tutorial 4 - the ball and socket at the
         top, above tutorial 3, tutorial 2, tutorial 1 and Start
   :class: shot

What you should be able to read off the joint
----------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Check
     - Expected
     - Where to look
   * - parts in the studio
     - ``Ball stud`` and ``Socket body``
     - the parts list
   * - the ball
     - 12 mm across
     - ``ball`` in ``robot sizes``
   * - the stud, middle to top
     - 10 mm
     - ``stand`` in ``robot sizes``
   * - the socket
     - 15.6 mm across
     - the collar's circle
   * - the socket, top to bottom
     - 12.2205 mm
     - ``grip`` above and ``collar`` below
   * - the hole
     - 6.08 mm radius
     - ``#ball / 2 + #fit``, and no dialog
   * - the slit floors
     - 4 mm below the ball's middle
     - the cut through the rim
   * - slits
     - four, a quarter turn apart
     - the socket's rim
   * - mate connectors
     - ``stud connect to robot`` and ``socket connect to robot``
     - the feature list
   * - every sketch
     - black
     - the graphics area

Three numbers on this page were typed as lengths: ``#fit``, ``#ballLoss`` and ``#slit``. All three
are about the printer rather than about the robot. Everything else came out of ``#ball``, and
``#ball`` came out of ``#torsoH``. Change the torso's height on page 1 and this joint changes with
it, hole and all.

Working habits
==============

Eight things to do every time. They are what separates a model that survives a change from one that
has to be rebuilt when a number moves, and they cost nothing once they are habits.

Type a name into a dimension box, not a number
----------------------------------------------

When a dialog asks for a length, type ``#torsoH / 4`` rather than ``24``. Onshape works it out and
shows you the answer, and the box keeps the expression.

The point is what happens next time. Change ``#torsoH`` in the Variable Studio and every box that
holds an expression follows; every box that holds a typed number stays where it was and quietly
becomes wrong. A robot with four numbers driving it is a robot you can rescale in one edit.

Name every feature as you make it
---------------------------------

``Sketch 1`` and ``Extrude 4`` are not names. ``limb section`` and ``add ball stud`` are.

Name the feature in its own dialog, before you fill it in, while you still know what it is for.
Hover the dialog's title and a small pencil appears to the right of it; click the pencil and the
title turns into a box. Letters typed at the title itself go to the sketch as tool shortcuts
instead. A feature already in the tree is renamed from its row's menu. Ten features in, a tree
that reads
``collar blank / cavity from ball / slit profile / relief slits`` tells you where to click; a tree
of ``Extrude 1`` through ``Extrude 6`` makes you open all six.

Name the parts too. A Part Studio's **Parts** list is where the assembly reads its names from, so
``Ball stud`` in the list is ``Ball stud`` in the assembly.

Finish every sketch fully defined
---------------------------------

A sketch is **fully defined** when all of its lines have gone black. Until then, Onshape is free to
move it, and a change somewhere else can move it in a way you did not ask for.

Getting there is dimensions and constraints: a diameter, a distance to the origin, a *concentric*
or a *symmetric*. If a sketch will not go black, something in it has a freedom you have not decided
on yet, which is worth a moment of thought rather than a rough drag into place.

Reframe before you look
-----------------------

The view keys are worth learning on the first page, because you use them on every page after.

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - Key
     - What it does
   * - **f**
     - zoom to fit — the whole model fills the window
   * - **shift+1**
     - look at the front
   * - **shift+2**
     - look at the back
   * - **shift+4**
     - look at the right side
   * - **shift+5**
     - look down from the top
   * - **shift+6**
     - look up from the bottom
   * - **shift+7**
     - back to the corner view
   * - **p**
     - hide and show the three default planes

Press **f** far more often than feels necessary. Most of the picking mistakes in a model are made
zoomed out, on a face two pixels wide that turned out to be the wrong one.

.. admonition:: One key with a trap in it
   :class: advice

   A view key pressed while a number box still has the cursor in it gets **typed into the box**.
   The view does not change and the number quietly becomes something like ``#limbSeg1f``. Click
   the dialog's title first to put the cursor down, then press the key.

Hold shift, and turn the view, before you pick
---------------------------------------------

When you place a mate connector, Onshape offers you the points it can snap to on whatever the
pointer is over: the middle of a face, the center of a circle, the end of an edge. They are the
small white squares. Move the pointer a little and it offers a different thing's points instead,
and that is what makes a point in the middle of a hollow hard to land on. On the way there you
cross an edge, and the edge takes over.

**Hover the face you want first, then hold shift, then travel to the point and click.** Shift
locks the offer to the face you were on when you pressed it, and the squares stay on screen the
whole way across, even after the pointer has left the face. Let go of shift once you have clicked.
Pressing shift before you hover locks nothing; the face has to be under the pointer first.

Shift does the opposite favor inside a sketch. Held while you draw, it turns snapping off, so a
line stops jumping onto whatever happens to be near it.

Shift holds the offer still, and it cannot separate two things drawn at the same pixel; a click
there takes whichever is in front. That is what a view straight down a part's axis gives you,
because everything built on that axis lines up. Press **shift+7** and then the arrow keys, which
turn the view 15 degrees a press, and things at different depths slide apart. Pick from the turned
view. The model does not care which way you were looking when you clicked.

Build the part around the joint, not the joint onto the part
------------------------------------------------------------

Every part with a joint on it gets built with that joint's center **on the origin**, and the part
grown outward from there.

It sounds backwards and it saves a step every time: the joint arrives at the origin already in the
right place, so there is nothing to move it with. It also means a limb and the joint on its end are
measured from the same point, which is what makes the two ends of a chain line up.

Read the number back off the model
----------------------------------

After a feature, check it. Onshape's **Measure** tool gives you a diameter, a distance, a volume;
the **Parts** list gives you a count.

A count is the cheapest check there is. If a part studio should hold one part and holds two, a
Boolean did not take, and finding that now is much easier than finding it in the assembly.

Publish a version at the end of every page
------------------------------------------

Click the document name's **version** icon at the top left, give it a name like ``t9 hinge``, and
create it.

A version is a permanent bookmark of the whole document. Nothing you do afterwards can disturb it,
you can open it, compare against it, or branch off it, and every page in this guide ends with one
so you always have somewhere clean to come back to.

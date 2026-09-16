# What you are building, and how Onshape holds it

Background for the course. Nothing here is a step to follow — the steps are in
[`instructions/`](../instructions/). Read this if you want to know what the thing is before you
start making it, or if a word in the steps was new.

## The robot

A robot figure, 150 mm tall, that you can pose.

It has thirteen joints. Nine of them are **ball and socket** — a ball on one part, a cup on the
next — and those turn every way. The neck is one. So are both shoulders, both wrists, both hips
and both ankles.

The other four are **hinges**. Elbows and knees only bend one way, like your own do. There is no
pin in them. One part ends in a fork, the other ends in a flat tongue, and the tongue pushes in
between the two ears of the fork and stays there. The tongue carries a short axle across it, each
ear has a hole for it, and the two snap together. A ring of little cones on the tongue drops into a
ring of little holes in the ears, so the joint clicks as it turns and holds the pose you leave it
in. The idea is borrowed from a LEGO click joint.

Every size in the robot comes from one number: **the torso is 48 mm tall.** The head, the neck,
the arms and the legs are all fractions of that. Change the 48 and the whole robot changes size
with it. That is not a trick — it is the point of the course, and you will do it in the first
session.

There are only **eight parts you have to draw**. The robot has more parts than that, but the
left arm is the same shape as the right arm, so you draw it once and use it twice.

## Four sessions

Eight hours in total, two hours at a time.

The first session builds the body: torso, neck, head, and a face. Later sessions add the joints,
the arms and the legs, and then put them together so the robot can move.

Every session ends with something you can show someone, and something you can come back to. If
you miss a week, you do not start again from nothing.

## The words Onshape uses

Onshape has its own names for things, and the steps use them exactly. Here are the ones that
come up first.

**A document** is the whole project. It holds everything else, and it lives on Onshape's servers
rather than on your computer. There is nothing to save.

**A Part Studio** is where parts are made. Confusingly, one Part Studio can hold several parts —
that is normal, and it is how the robot is built.

**An Assembly** is where finished parts are put together and made to move. Parts are made in a
Part Studio; they are joined in an Assembly.

**A sketch** is a flat drawing — lines, rectangles, circles — on a flat surface. Sketches are not
solid. They are the outline that a solid gets made from.

**A feature** is one thing you did to make a shape. Pulling a rectangle out into a block is a
feature. So is spinning a shape around a line, or rounding an edge.

Features stack up in a list down the left of the screen, in the order you did them. You can go
back and change any one of them later.

## Constraints, and why the course cares

A sketch can be drawn by eye. It will look right and be wrong.

Instead you tell Onshape what must stay true: this line is horizontal, this corner sits on the
origin, these two circles are the same size. Those rules are called **constraints**, and Onshape
holds the drawing to them.

A sketch that is completely pinned down is **fully defined**, and Onshape turns it black to say
so. A sketch that is not fully defined can still be dragged around — which means it can drift
later, after you have built things on top of it.

This is the difference between a drawing that happens to look right and a model you can change.
It is why the first session spends its time on it.

## Versions

Onshape keeps its own history of your document. You do not save files, and there is nothing to
name until you want to.

When you finish something, you **publish a version** and give it a name. That version is frozen.
It stays exactly as it was, no matter what you do to the document afterwards.

Two reasons that matters here:

- If a later session goes wrong, you can open the version from the end of the last one and carry
  on from there.
- If you miss a session, there is a named version to start from, so you are not behind.

A link to a version always shows the same thing. A link to the live document shows whatever it
looks like right now, which may not be what the person who sent it saw.

## Where things are

- [`instructions/`](../instructions/) — the steps to follow, session by session.
- `docs/` — this page, and other background.
- [`README.md`](../README.md) — the short version of all of it.

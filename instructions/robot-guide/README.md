# The robot lesson

A Sphinx page for the robot build, starting from a design plan rather than from a click.

```sh
ninja plan          # re-render the plan drawing from source/images/design-plan.svg
ninja guide         # build
ninja open-guide
```

`ninja plan` renders the SVG by loading it in the headless browser from
[`tools/agent_browser.py`](../../tools/agent_browser.py) and screenshotting it, so there is no
extra image dependency to install.

## Why it opens with a drawing

People do not start CAD by clicking. They start with a picture of the thing and a rough
idea of how it comes apart. The first figure in this page is that picture — front and side
views with the key dimensions — and it is explicitly **not** a CAD sketch: nothing in
Onshape is built from it. It exists so a student knows where they are going before the
first rectangle.

The CAD sketch that follows is deliberately the *minimum* front view that the features can
be made from: three rectangles, one of them a half-profile for a revolve. It does not look
like the robot, and it is not supposed to. A sketch is a pool of shapes that features reach
into, not a drawing.

## Status

Written, not yet tested against a student or an agent. The first draft of the
markdown version was tested and the report is in
[`test-report.md`](../../.docs/experiments/session-1-layout-and-torso/test-report.md);
every finding from it that survives the redesign has been folded into this page.

No screenshots yet. They come from capturing a run once the steps are known to work.

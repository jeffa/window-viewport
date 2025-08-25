+++++++++
window-viewport
+++++++++

Just another window to viewport coordinates translator.

Installing
==========

Use pip:

    $ pip install window-viewport

Using window-viewport
===============

The world bounds are typically bounded by 0 and 1 or -1 and 1. Your view bounds are whatever your target's maximum values are. The order of arguments is: bottom, top, left, right. If your target is an image file with dimension 640x480 then you might construction your object like so:

   tform = viewport( world_bounds=(0, 1, 0, 1), view_bounds=(0, 480, 0, 640))

Then you can make your calculations within the world bounds and draw the results using the transformed values:

   x, y = ( calculate_x(x), calculate_y(y) )

   window.draw( tform.Dx(x), tform.Dy(y) )

development
===========

* Source hosted at `GitHub <http://github.com/jeffa/window-viewport>`

Pull requests welcomed. Make sure your patches are well tested.

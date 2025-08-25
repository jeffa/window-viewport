window-viewport
=====================
Just another window to viewport coordinates translator.  [![pypi package](https://badge.fury.io/py/window-viewport.svg)](https://pypi.python.org/pypi/window-viewport)

Description
-----------
Transform any window coordinates to any viewport coordinates.

Synopsis
--------
```python
from window.viewport import viewport

tform = viewport( world_bounds=(0, 1, 0, 1), view_bounds=(9, 0, 0, 9))

x, y = ( 1, 2 )

x2, y2 = ( tform.Dx(x), tform.Dx(y) )
```
See [readme](readme.rst) for more documentation.

Installation
------------
```
pip install window-viewport
```

License and Copyright
---------------------
See [License](License.md).

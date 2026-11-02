Set a prim's translation, rotation, and scale with `UsdGeom.XformCommonAPI`. Pass a time code to animate them.
``` {literalinclude} py_usd.py
:language: py
```

If you already have the transform as a matrix, for example from another application, replace the prim's operations with a single matrix operation using `UsdGeom.Xformable.MakeMatrixXform()`.
``` {literalinclude} py_usd_var1.py
:language: py
```

To place a prim at a world space transform, convert it into the prim's parent space first, using the inverse of the parent's world transform.
``` {literalinclude} py_usd_var2.py
:language: py
```

Wrap a valid imageable prim, such as a mesh or an Xform, in `UsdGeom.Imageable` and call `ComputeVisibility()`. Compare its result with `UsdGeom.Tokens.invisible` or `UsdGeom.Tokens.inherited`; the result is a token string, not a Boolean.

The example checks both a prim's own visibility and visibility inherited from an ancestor. For animated visibility, pass a `Usd.TimeCode` for the time you want to inspect. `Usd.TimeCode.Default()` reads default values, not the application's current frame.

``` {literalinclude} py_usd.py
:language: py
```

`ComputeVisibility()` is convenient for checking individual prims. When checking every prim during a large traversal, carrying the inherited visibility down the traversal avoids repeatedly inspecting the same ancestors.

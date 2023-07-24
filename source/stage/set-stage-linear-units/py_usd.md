You can set the `metersPerUnit` metadata on the stage using `UsdGeom.SetStageMetersPerUnit` to define the linear units of the stage. Convenience shortcuts for units are scoped in `UsdGeom.LinearUnits` (e.g. `UsdGeom.LinearUnits.meters` is `1.0 metersPerUnit`)
``` {literalinclude} py_usd.py
:language: py
```
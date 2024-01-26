``` {literalinclude} py_usd.py
:language: py
```

Alternatively, if you need to compute the world transform for multiple prims on a stage, [UsdGeom.XformCache](https://openusd.org/release/api/class_usd_geom_xform_cache.html) is more efficient.

``` {literalinclude} py_usd_var1.py
:language: py
```
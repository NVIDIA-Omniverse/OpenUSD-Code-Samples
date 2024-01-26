``` {literalinclude} py_usd.py
:language: py
```

Alternatively, if you need to compute the bounding box for multiple prims on a stage, [UsdGeom.BBoxCache](https://openusd.org/release/api/class_usd_geom_b_box_cache.html) is more efficient.

``` {literalinclude} py_usd_var1.py
:language: py
```
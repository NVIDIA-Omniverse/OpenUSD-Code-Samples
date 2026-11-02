``` {literalinclude} py_usd.py
:language: py
```

If you need the world positions of many prims on a stage, [UsdGeom.XformCache](https://openusd.org/release/api/class_usd_geom_xform_cache.html) is more efficient, because it reuses the transforms of shared ancestors.

``` {literalinclude} py_usd_var1.py
:language: py
```

To get the world-space center of a prim's geometry rather than its origin, compute its world bounds with [UsdGeom.BBoxCache](https://openusd.org/release/api/class_usd_geom_b_box_cache.html) and take the centroid.

``` {literalinclude} py_usd_var2.py
:language: py
```

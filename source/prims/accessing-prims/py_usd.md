**Get a Reference by using the prim’s stage path**

``` {literalinclude} py_usd.py
:language: py
```

**Getting cached prims**

For performance reasons some API’s use cached versions of prims and the stage. prim_id is an ID to the cached prim with the path in the string var ``my_prim_path`` and ``stage_id`` is an ID for the cached stage.


``` {literalinclude} py_usd_var1.py
:language: py
```
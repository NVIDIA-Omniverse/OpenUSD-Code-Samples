Traverse a stage to find prims with a given attribute.

``` {literalinclude} py_usd.py
:language: py
```

```{warning}
This will be slow for stages with many prims, as stage traversal is currently single-threaded. Learn more about [scene complexity](https://openusd.org/release/maxperf.html#what-makes-a-usd-scene-heavy-expensive).
```

Traverse a parent-child hierarchy to find prims with a given attribute.

``` {literalinclude} py_usd_var1.py
:language: py
``` 
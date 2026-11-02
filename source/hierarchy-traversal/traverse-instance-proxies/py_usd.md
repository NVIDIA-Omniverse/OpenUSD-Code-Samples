Traverse the whole Stage, including the children of instanced prims, with `Usd.Stage.Traverse(Usd.TraverseInstanceProxies())`.
``` {literalinclude} py_usd.py
:language: py
```

Traverse everything below a specific prim, including instance proxies, with `Usd.PrimRange`. A range starts at the prim you give it, so skip the first prim to get only its descendants.
``` {literalinclude} py_usd_var1.py
:language: py
```

By default, traversal also skips prims that are inactive, unloaded, undefined (only `over` opinions), or abstract (`class` prims). Wrap `Usd.PrimAllPrimsPredicate` in `Usd.TraverseInstanceProxies()` to visit every prim on the Stage.
``` {literalinclude} py_usd_var2.py
:language: py
```

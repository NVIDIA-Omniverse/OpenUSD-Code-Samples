With the USD API, you can use `Usd.Prim.GetReferences()` to receive the references and add a new one with `Usd.References.AddReference()`. The target prim path is optional: pass it to reference a specific prim, or leave it out to reference the layer's default prim.
``` {literalinclude} py_usd.py
:language: py
```
With the USD API, you can use `Usd.Prim.GetPayloads()` to receive the payloads and add a new one with `Usd.Payloads.AddPayload()`. The target prim path is optional: pass it to payload a specific prim, or leave it out to payload the layer's default prim.
``` {literalinclude} py_usd.py
:language: py
```
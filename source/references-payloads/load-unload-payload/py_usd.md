Unload a prim's Payload with `Usd.Prim.Unload()` and load it again with `Usd.Prim.Load()`.
``` {literalinclude} py_usd.py
:language: py
```

Open a Stage with nothing loaded, find the prims that can be loaded with `Usd.Stage.FindLoadable()`, and load only the ones you need with `Usd.Stage.LoadAndUnload()`. This is the usual way to work with large scenes, since nothing heavy is composed until you ask for it.
``` {literalinclude} py_usd_var1.py
:language: py
```

Payloads can contain other Payloads. Loading with `Usd.LoadWithoutDescendants` loads only the given prim's Payload and leaves the Payloads nested inside it unloaded.
``` {literalinclude} py_usd_var2.py
:language: py
```

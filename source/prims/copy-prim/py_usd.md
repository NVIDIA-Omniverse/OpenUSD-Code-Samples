Copy a prim's specs within a layer with `Sdf.CopySpec()`. Composition arcs on the prim, such as references, are copied as arcs.
``` {literalinclude} py_usd.py
:language: py
```

To copy what the prim looks like after composition, including opinions from other layers and the contents of its references and payloads, flatten the stage first and copy from the flattened layer. The copy has no composition arcs of its own. Flattening a large stage is expensive, so prefer the first example when the prim's opinions are all in one layer.
``` {literalinclude} py_usd_var1.py
:language: py
```

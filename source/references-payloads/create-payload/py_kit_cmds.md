The `CreatePayload` command is a convenient wrapper that creates an Xform prim and adds a Payload to it all at once. If you don't need the two steps batched together, you may want to [add a Payload](add-payload) to an existing prim via Kit Commands or USD Python API.

``` {literalinclude} py_kit_cmds.py
:language: py
```
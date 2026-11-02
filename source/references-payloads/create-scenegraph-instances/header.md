[Scenegraph instancing](https://openusd.org/release/api/_usd__page__scenegraph_instancing.html) is a lightweight way to repeat the same content many times. Mark prims that bring in the same content through a composition arc, such as a [Reference](add-reference), as instanceable with `Usd.Prim.SetInstanceable(True)`. USD composes the shared content once, as a prototype, and every instance shares it.

Each instance prim can still have its own opinions, such as a transform. The children of an instance are read-only instance proxies: to change them, edit the asset that the instances reference. To make an independent, editable duplicate instead, see [Copy a Prim](../prims/copy-prim).

```{note}
Prototypes are created and named by USD (for example, `/__Prototype_1`), and are shared only by instances whose composition arcs match. Don't author on prototypes or rely on their paths; use `Usd.Prim.GetPrototype()` to find an instance's prototype.
```

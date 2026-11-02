`Usd.Stage.Traverse()` and `Usd.Prim.GetChildren()` include the contents of [References](https://openusd.org/release/glossary.html#usdglossary-references) and [Payloads](https://openusd.org/release/glossary.html#usdglossary-payload), but they stop at [instanced](https://openusd.org/release/glossary.html#usdglossary-instancing) prims. Assets brought in by reference are often marked instanceable, so their children appear to be missing. Those children are [instance proxies](https://openusd.org/release/api/_usd__page__scenegraph_instancing.html#Usd_ScenegraphInstancing_InstanceProxies). To include them, pass the `Usd.TraverseInstanceProxies()` predicate when you traverse.

```{warning}
Instance proxies are read-only: authoring an opinion on one is an error. To change what every instance shows, edit the asset the instances reference. To change one instance, make it non-instanceable with `Usd.Prim.SetInstanceable(False)`, or author on the instanced prim itself.
```

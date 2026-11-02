To duplicate a prim and everything below it, copy its specs with [Sdf.CopySpec()](https://openusd.org/release/api/copy_utils_8h.html). The copy is independent: changing it does not change the original, and changing the original does not change the copy. Relationship targets and attribute connections that point inside the copied prim are updated to point inside the copy.

There are three common ways to repeat a prim. Choose based on whether the repeats should stay linked to the original:

| Approach | Result |
| --- | --- |
| Copy (this sample) | An independent duplicate that you can edit freely. |
| [Reference](../references-payloads/add-reference) | A live link: later changes to the original show up in every referencing prim, and each one can still override it. |
| [Instance](../references-payloads/create-scenegraph-instances) | A reference that shares one read-only prototype with other instances. Lightest for many identical repeats. |

```{warning}
`Sdf.CopySpec()` replaces anything already authored at the destination path in that layer, and it copies only the opinions in the source layer. If the prim gets opinions from other layers or from composition arcs such as references, copy from a flattened layer instead, as shown in the second example.
```

A prim's world position is where its local origin ends up after the transformations of the prim and all of its ancestors are applied. Compute the prim's local-to-world matrix with [UsdGeom.Xformable.ComputeLocalToWorldTransform()](https://openusd.org/release/api/class_usd_geom_imageable.html#a8e3fb09253ba63d63921f665d63cd270) and take its translation with `Gf.Matrix4d.ExtractTranslation()`. If you also need the world rotation and scale, see [Get the World Space Transforms for a Prim](get-world-transforms).

```{note}
The world position is the prim's origin (its pivot), which is not necessarily the center of its geometry. If the geometry is offset from the origin, use the center of the prim's world-space bounds instead, as shown in the last example.
```

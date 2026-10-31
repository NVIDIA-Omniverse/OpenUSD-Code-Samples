These snippets show how to create a Material prim and a `UsdPreviewSurface` Shader prim. Optionally, you can also create a `UsdUVTexture` to read from a texture file and connect it to the `UsdPreviewSurface`. A texture needs texture coordinates (UVs) to sample with, so pair it with a `UsdPrimvarReader_float2` that reads them from the geometry's `st` primvar. Learn more in the [UsdPreviewSurface specification](https://openusd.org/release/spec_usdpreviewsurface.html) and the [Simple Shading in USD](https://openusd.org/release/tut_simple_shading.html) tutorial.

```{note}
`UsdTransform2d` transforms the texture coordinates, not the texture itself, so the image moves the opposite way: a `scale` of `(2, 2)` repeats the texture twice in each direction, making it look smaller. The UVs are scaled, then rotated counterclockwise in degrees, then translated, all around the UV origin `(0, 0)` rather than the center of the texture.
```

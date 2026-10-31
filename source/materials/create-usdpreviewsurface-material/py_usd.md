This version creates just the Material prim and UsdPreviewSurface Shader.

``` {literalinclude} py_usd.py
:language: py
```

This version builds a textured material from all four core nodes of the [UsdPreviewSurface specification](https://openusd.org/release/spec_usdpreviewsurface.html): a `UsdPrimvarReader_float2` reads the UVs from the mesh's `st` primvar, a `UsdTransform2d` scales, rotates and translates them, and `UsdUVTexture` shaders sample the diffuse, roughness, occlusion, displacement and normal textures at those UVs and feed the `UsdPreviewSurface`. One `UsdTransform2d` is shared by every texture so they stay aligned. It is adapted from the [How to Create a USD Material Using Python and UsdPreviewSurface](https://www.youtube.com/watch?v=fwI4P5MFIbU) livestream.

``` {literalinclude} py_usd_var1.py
:language: py
```
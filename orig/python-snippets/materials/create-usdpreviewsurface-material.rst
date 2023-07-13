.. meta::
    :description: Universal Scene Description (USD) Python code snippets for creating a UsdPreviewSurface material including UsdUVTexture Shader for loading data from textures.
    :keywords: USD, Python, snippet, UsdPreviewSurface, UsdUVTexture, material, CreatePreviewSurfaceMaterialPrim, Omniverse Kit, Kit Commands, shader

===================================
Create a UsdPreviewSurface Material
===================================

These snippets show how to create a Material prim and a :code:`UsdPreviewSurface` Shader prim. Optionally, you can also create a :code:`UsdUVTexture` to read from a texture file and connect it to the :code:`UsdPreviewSurface`.

Omniverse Kit Commands
----------------------
This version creates just the material prim and UsdPreviewSurface Shader.

.. code-block:: python
    
    import omni.kit.commands

    omni.kit.commands.execute("CreatePreviewSurfaceMaterialPrim",
        mtl_path="/World/Looks/PreviewSurface",
        select_new_prim=True)


This version also creates UsdUVTexture Shader prims for the diffuse, roughness, metallic, and normal properties and connects them to the UsdPreviewSurface.

.. code-block:: python

    import omni.kit.commands

    omni.kit.commands.execute("CreatePreviewSurfaceTextureMaterialPrim",
        mtl_path="/World/Looks/PreviewSurfaceWithTextures",
        select_new_prim=True)


USD API
-----------
This version creates just the Material prim and UsdPreviewSurface Shader.

.. code-block:: python

    from pxr import Sdf, UsdShade

    mtl_path = Sdf.Path("/World/Looks/PreviewSurface")
    mtl = UsdShade.Material.Define(stage, mtl_path)
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
    shader.CreateIdAttr("UsdPreviewSurface")
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set([1.0, 0.0, 0.0])
    shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.5)
    shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)
    mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")

This version also creates UsdUVTexture Shader prim and connects it to the diffuse property of the UsdPreviewSurface.

.. code-block:: python

    from pxr import Sdf, UsdShade

    mtl_path = Sdf.Path("/World/Looks/PreviewSurface")
    mtl = UsdShade.Material.Define(stage, mtl_path)
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
    shader.CreateIdAttr("UsdPreviewSurface")
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((1.0, 0.0, 0.0))
    shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.5)
    shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)

    diffuse_tx = UsdShade.Shader.Define(stage,mtl_path.AppendPath("DiffuseColorTx"))
    diffuse_tx.CreateIdAttr('UsdUVTexture')
    diffuse_tx.CreateInput('file', Sdf.ValueTypeNames.Asset).Set("C:/path/to/texture.png")
    diffuse_tx.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(diffuse_tx.ConnectableAPI(), 'rgb')
    mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
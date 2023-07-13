.. meta::
    :description: Universal Scene Description (USD) Python code snippets for creating an MDL material with a Shader prim with an MDL source asset.
    :keywords: USD, Python, snippet, MDL, material, CreateMdlMaterialPrimCommand, Omniverse Kit, Kit Commands, shader

======================
Create an MDL Material
======================

If you want to create an MDL material, you can use the :code:`CreateMdlMaterialPrimCommand` or the USD API to do the same. These snippets show how to create a Material prim and a Shader prim that reads from an MDL file. They also utilizes the `sourceAsset:subIdentifier` attribute to choose a specific material description from within the MDL file.

Omniverse Kit Commands
----------------------
.. code-block:: python
    
    import omni.kit.commands

    success, result = omni.kit.commands.execute('CreateMdlMaterialPrimCommand',
        mtl_url='OmniPBR.mdl', # This can be path to local or remote MDL
        mtl_name='OmniPBR', # sourceAsset:subIdentifier (i.e. the name of the material within the MDL)
        mtl_path="/World/Looks/OmniPBR" # Prim path for the Material to create.
    )


USD API
-----------
.. code-block:: python

    from pxr import Sdf, UsdShade

    mtl_path = Sdf.Path("/World/Looks/OmniPBR")
    mtl = UsdShade.Material.Define(stage, mtl_path)
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
    shader.CreateImplementationSourceAttr(UsdShade.Tokens.sourceAsset)
    # MDL shaders should use "mdl" sourceType
    shader.SetSourceAsset("OmniPBR.mdl", "mdl")
    shader.SetSourceAssetSubIdentifier("OmniPBR", "mdl")
    # MDL materials should use "mdl" renderContext
    mtl.CreateSurfaceOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
    mtl.CreateDisplacementOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
    mtl.CreateVolumeOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
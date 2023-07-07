#!/usr/bin/env python3
# 
# See https://graphics.pixar.com/usd/release/tut_simple_shading.html

from pxr import Gf, Usd, UsdGeom, UsdShade, Sdf


def run(stage: Usd.Stage, root: Sdf.Path):
    # Mesh creation
    mesh_path = root.AppendPath("Mesh")
    mesh: UsdGeom.Mesh = UsdGeom.Mesh.Define(stage, mesh_path)
    mesh.CreatePointsAttr([(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)])
    mesh.CreateFaceVertexCountsAttr([4])
    mesh.CreateFaceVertexIndicesAttr([0, 1, 2, 3])
    mesh.CreateExtentAttr([(-1, -1, 0), (1, 1, 0)])
    texCoords = UsdGeom.PrimvarsAPI(mesh).CreatePrimvar(
        "st", Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.varying
    )
    texCoords.Set([(0, 0), (1, 0), (1, 1), (0, 1)])

    # Material + Shader creation and binding
    material_path = root.AppendPath("Material")
    material = UsdShade.Material.Define(stage, material_path)
    shader_path = material_path.AppendPath("Shader")
    shader: UsdShade.Shader = UsdShade.Shader.Define(
        stage, shader_path
    )
    shader.SetSourceAsset("UsdPreviewSurface.mdl", "mdl")
    shader.SetSourceAssetSubIdentifier("UsdPreviewSurface", "mdl")
    shader.CreateIdAttr("UsdPreviewSurface")
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(1.0, 0.0, 1.0))
    material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
    mesh.GetPrim().ApplyAPI(UsdShade.MaterialBindingAPI)
    UsdShade.MaterialBindingAPI(mesh).Bind(material)


def run_usda():
    stage: Usd.Stage = Usd.Stage.CreateInMemory()
    root_path = Sdf.Path("/World")
    root_prim = UsdGeom.Xform.Define(stage, root_path)
    stage.SetDefaultPrim(root_prim.GetPrim())
    run(stage=stage, root=root_path)
    usda = stage.GetRootLayer().ExportToString()
    print(usda)


def run_omni_usd():
    import omni
    usd_context = omni.usd.get_context()
    stage: Usd.Stage = usd_context.get_stage()
    run(stage=stage, root=Sdf.Path("/World"))


if __name__ == "__main__":
    import os
    running_in_ov = os.environ.get("OMNI_USD_RESOLVER_MDL_BUILTIN_PATHS") is not None
    if running_in_ov:
        run_omni_usd()
    else:
        run_usda()

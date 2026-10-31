# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, Usd, UsdShade

def create_preview_surface_material(stage: Usd.Stage, mtl_path: Sdf.Path) -> UsdShade.Material:
    mtl = UsdShade.Material.Define(stage, mtl_path)
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
    shader.CreateIdAttr("UsdPreviewSurface")
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0.0, 0.0, 1.0))
    shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.5)
    shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)
    mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
    return mtl


#############
# Full Usage
#############

from pxr import Gf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

mtl_path = Sdf.Path("/World/Looks/PreviewSurface")
mtl = create_preview_surface_material(stage, mtl_path)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the material's surface is driven by a blue UsdPreviewSurface shader
shader = UsdShade.Shader(mtl.ComputeSurfaceSource()[0].GetPrim())
assert shader.GetShaderId() == "UsdPreviewSurface"
assert shader.GetInput("diffuseColor").Get() == Gf.Vec3f(0.0, 0.0, 1.0)

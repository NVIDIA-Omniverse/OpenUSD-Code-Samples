# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, Usd

def copy_prim(stage: Usd.Stage, src_path: Sdf.Path, dst_path: Sdf.Path) -> Usd.Prim:
    # Copy the prim's specs within the current edit target layer
    layer: Sdf.Layer = stage.GetEditTarget().GetLayer()
    # The destination's parent must exist in the layer; an "over" is enough
    if not layer.GetPrimAtPath(dst_path.GetParentPath()):
        Sdf.CreatePrimInLayer(layer, dst_path.GetParentPath())
    if not Sdf.CopySpec(layer, src_path, layer, dst_path):
        raise RuntimeError(f"Could not copy {src_path} to {dst_path}")
    return stage.GetPrimAtPath(dst_path)


#############
# Full Usage
#############
from pxr import Gf, UsdGeom, UsdShade

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())

# A car with a body and a material bound to it
car: UsdGeom.Xform = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Car"))
body: UsdGeom.Cube = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Car/Body"))
body.CreateDisplayColorAttr([Gf.Vec3f(1, 0, 0)])
paint: UsdShade.Material = UsdShade.Material.Define(stage, Sdf.Path("/World/Car/Paint"))
UsdShade.MaterialBindingAPI.Apply(body.GetPrim()).Bind(paint)

# Duplicate the car and move the copy
car_copy: Usd.Prim = copy_prim(stage, Sdf.Path("/World/Car"), Sdf.Path("/World/Garage/CarCopy"))
UsdGeom.Xformable(car_copy).AddTranslateOp().Set((5, 0, 0))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# The copy has the same children...
body_copy = UsdGeom.Cube(stage.GetPrimAtPath("/World/Garage/CarCopy/Body"))
assert body_copy and body_copy.GetDisplayColorAttr().Get()[0] == Gf.Vec3f(1, 0, 0)
# ...and its material binding points at the copy's own material, not the original's
bound_material = UsdShade.MaterialBindingAPI(body_copy.GetPrim()).ComputeBoundMaterial()[0]
assert bound_material.GetPath() == Sdf.Path("/World/Garage/CarCopy/Paint")

# Editing the copy does not change the original
body_copy.GetDisplayColorAttr().Set([Gf.Vec3f(0, 0, 1)])
assert body.GetDisplayColorAttr().Get()[0] == Gf.Vec3f(1, 0, 0)
assert not UsdGeom.Xformable(car).GetOrderedXformOps()

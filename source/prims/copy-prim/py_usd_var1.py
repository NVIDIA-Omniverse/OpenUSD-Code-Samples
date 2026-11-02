# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, Usd

def copy_composed_prim(stage: Usd.Stage, src_path: Sdf.Path, dst_path: Sdf.Path) -> Usd.Prim:
    # Flatten the stage so the source prim's spec holds its fully composed result
    flattened: Sdf.Layer = stage.Flatten()
    layer: Sdf.Layer = stage.GetEditTarget().GetLayer()
    if not layer.GetPrimAtPath(dst_path.GetParentPath()):
        Sdf.CreatePrimInLayer(layer, dst_path.GetParentPath())
    if not Sdf.CopySpec(flattened, src_path, layer, dst_path):
        raise RuntimeError(f"Could not copy {src_path} to {dst_path}")
    return stage.GetPrimAtPath(dst_path)


#############
# Full Usage
#############
from pxr import UsdGeom

# Create a wheel asset. In practice this would be a file such as "./assets/wheel.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
asset_stage.SetDefaultPrim(UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Wheel")).GetPrim())
UsdGeom.Cylinder.Define(asset_stage, Sdf.Path("/Wheel/Tire"))

# Create an in-memory Stage with a car whose wheel is a reference
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())
UsdGeom.Xform.Define(stage, Sdf.Path("/World/Car"))
body: UsdGeom.Cube = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Car/Body"))
wheel: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Car/Wheel")).GetPrim()
wheel.GetReferences().AddReference(asset_stage.GetRootLayer().identifier)

# An opinion in the session layer, which a copy of the root layer alone would miss
with Usd.EditContext(stage, stage.GetSessionLayer()):
    body.GetSizeAttr().Set(4.0)

car_copy: Usd.Prim = copy_composed_prim(stage, Sdf.Path("/World/Car"), Sdf.Path("/World/CarCopy"))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# The copy includes the session layer opinion and the referenced wheel's contents...
assert stage.GetPrimAtPath("/World/CarCopy/Body").GetAttribute("size").Get() == 4.0
assert stage.GetPrimAtPath("/World/CarCopy/Wheel/Tire").IsA(UsdGeom.Cylinder)
# ...baked in, so the copy no longer references the wheel asset
assert not stage.GetPrimAtPath("/World/CarCopy/Wheel").HasAuthoredReferences()
assert stage.GetRootLayer().GetPrimAtPath("/World/CarCopy/Wheel/Tire") is not None

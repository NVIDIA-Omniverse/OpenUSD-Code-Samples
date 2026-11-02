# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Sdf, Usd, UsdGeom

def create_instances(stage: Usd.Stage, asset_path: str, instance_paths: List[Sdf.Path]) -> List[Usd.Prim]:
    instances: List[Usd.Prim] = []
    for path in instance_paths:
        prim: Usd.Prim = UsdGeom.Xform.Define(stage, path).GetPrim()
        prim.GetReferences().AddReference(asset_path)
        # Instances whose composition arcs match share one prototype
        prim.SetInstanceable(True)
        instances.append(prim)
    return instances


#############
# Full Usage
#############

# Create a chair asset. In practice this would be a file such as "./assets/chair.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
asset_stage.SetDefaultPrim(UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Chair")).GetPrim())
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Seat"))
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Back"))
asset_path: str = asset_stage.GetRootLayer().identifier

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())

chairs: List[Usd.Prim] = create_instances(stage, asset_path, [Sdf.Path("/World/Chair_01"), Sdf.Path("/World/Chair_02")])

# Each instance can have its own transform
UsdGeom.Xformable(chairs[0]).AddTranslateOp().Set((-1, 0, 0))
UsdGeom.Xformable(chairs[1]).AddTranslateOp().Set((1, 0, 0))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Both chairs are instances of the same prototype, which holds the asset's contents once
assert all(chair.IsInstance() for chair in chairs)
prototype: Usd.Prim = chairs[0].GetPrototype()
assert chairs[1].GetPrototype() == prototype
assert [child.GetName() for child in prototype.GetChildren()] == ["Seat", "Back"]
assert len(stage.GetPrototypes()) == 1

# The instances' children are read-only instance proxies
seat: Usd.Prim = stage.GetPrimAtPath("/World/Chair_01/Seat")
assert seat.IsInstanceProxy()

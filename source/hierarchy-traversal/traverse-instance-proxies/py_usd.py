# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Usd, UsdGeom

def find_meshes_including_instances(stage: Usd.Stage) -> List[Usd.Prim]:
    # The default Traverse() stops at instanced prims; TraverseInstanceProxies() also visits their children
    return [prim for prim in stage.Traverse(Usd.TraverseInstanceProxies()) if prim.IsA(UsdGeom.Mesh)]


#############
# Full Usage
#############
from pxr import Sdf

# Create a chair asset. In practice this would be a file such as "./assets/chair.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
asset_stage.SetDefaultPrim(UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Chair")).GetPrim())
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Seat"))
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Back"))
asset_path: str = asset_stage.GetRootLayer().identifier

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())

# Reference the chair once as a regular prim and twice as instances
UsdGeom.Xform.Define(stage, Sdf.Path("/World/Chair")).GetPrim().GetReferences().AddReference(asset_path)
for name in ("InstancedChair1", "InstancedChair2"):
    prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World").AppendChild(name)).GetPrim()
    prim.GetReferences().AddReference(asset_path)
    prim.SetInstanceable(True)

meshes: List[Usd.Prim] = find_meshes_including_instances(stage)
print([str(mesh.GetPath()) for mesh in meshes])

# The default traversal finds the referenced chair's meshes, but not the instanced chairs' meshes
assert [str(p.GetPath()) for p in stage.Traverse() if p.IsA(UsdGeom.Mesh)] == ["/World/Chair/Seat", "/World/Chair/Back"]
# With instance proxies, every chair's meshes are found
assert len(meshes) == 6
assert stage.GetPrimAtPath("/World/InstancedChair1/Seat") in meshes
assert all(mesh.IsInstanceProxy() for mesh in meshes if "Instanced" in str(mesh.GetPath()))

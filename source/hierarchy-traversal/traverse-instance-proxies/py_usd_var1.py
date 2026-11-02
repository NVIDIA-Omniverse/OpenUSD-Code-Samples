# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Usd

def get_descendants_including_instances(prim: Usd.Prim) -> List[Usd.Prim]:
    prim_range = Usd.PrimRange(prim, Usd.TraverseInstanceProxies())
    # A PrimRange starts at the given prim; skip it to get only the descendants
    return list(prim_range)[1:]


#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create a chair asset. In practice this would be a file such as "./assets/chair.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
asset_stage.SetDefaultPrim(UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Chair")).GetPrim())
UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Chair/Frame"))
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Frame/Legs"))
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Seat"))

# Create an in-memory Stage with an instanced chair under /World/Room
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())
UsdGeom.Xform.Define(stage, Sdf.Path("/World/Room"))
chair: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Room/Chair")).GetPrim()
chair.GetReferences().AddReference(asset_stage.GetRootLayer().identifier)
chair.SetInstanceable(True)

room: Usd.Prim = stage.GetPrimAtPath("/World/Room")
descendants: List[Usd.Prim] = get_descendants_including_instances(room)
print([str(prim.GetPath()) for prim in descendants])

# GetChildren() stops at the instanced chair...
assert chair.GetChildren() == []
# ...but the range includes its instance proxies, depth-first, without the starting prim
assert [str(prim.GetPath()) for prim in descendants] == [
    "/World/Room/Chair",
    "/World/Room/Chair/Frame",
    "/World/Room/Chair/Frame/Legs",
    "/World/Room/Chair/Seat",
]

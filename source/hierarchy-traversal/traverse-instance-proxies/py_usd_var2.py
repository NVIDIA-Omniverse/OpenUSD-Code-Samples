# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Usd

def get_all_prims(stage: Usd.Stage) -> List[Usd.Prim]:
    # PrimAllPrimsPredicate also visits inactive, unloaded, undefined, and abstract prims
    return list(stage.Traverse(Usd.TraverseInstanceProxies(Usd.PrimAllPrimsPredicate)))


#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create a chair asset. In practice this would be a file such as "./assets/chair.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
asset_stage.SetDefaultPrim(UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Chair")).GetPrim())
UsdGeom.Mesh.Define(asset_stage, Sdf.Path("/Chair/Seat"))

# Create an in-memory Stage with prims that the default traversal skips
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())
instanced: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/InstancedChair")).GetPrim()
instanced.GetReferences().AddReference(asset_stage.GetRootLayer().identifier)
instanced.SetInstanceable(True)
UsdGeom.Xform.Define(stage, Sdf.Path("/World/Hidden")).GetPrim().SetActive(False)  # inactive
stage.OverridePrim(Sdf.Path("/World/OverOnly"))  # undefined: only an "over"
stage.CreateClassPrim(Sdf.Path("/_class_Chair"))  # abstract

all_prims: List[str] = [str(prim.GetPath()) for prim in get_all_prims(stage)]
print(all_prims)

# The default traversal sees only the defined, active, non-abstract prims and stops at the instance
assert [str(prim.GetPath()) for prim in stage.Traverse()] == ["/World", "/World/InstancedChair"]
# The full traversal sees every prim, including the instance proxy
assert all_prims == [
    "/World",
    "/World/InstancedChair",
    "/World/InstancedChair/Seat",
    "/World/Hidden",
    "/World/OverOnly",
    "/_class_Chair",
]

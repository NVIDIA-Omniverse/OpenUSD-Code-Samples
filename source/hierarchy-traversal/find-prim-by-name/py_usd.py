# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Usd


def find_prims_by_name(stage: Usd.Stage, prim_name: str) -> List[Usd.Prim]:
    found_prims = [x for x in stage.Traverse() if x.GetName() == prim_name]
    return found_prims


##############
# Full Usage
##############

from pxr import UsdGeom, Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create some shape prims
UsdGeom.Xform.Define(stage, "/World/Group")
UsdGeom.Cone.Define(stage, "/World/Foo")
UsdGeom.Cube.Define(stage, "/World/Group/Foo")
UsdGeom.Sphere.Define(stage, "/World/Group/Bar")

# find the prims with the name "Foo"
prims: List[Usd.Prim] = find_prims_by_name(stage, "Foo")

# Print the prims to check the found prims by name.
print(prims)

# Check the number of prims found and whether the found data is correct.
assert len(prims) == 2
assert isinstance(prims[0], Usd.Prim)
assert prims[0].GetName() == "Foo"
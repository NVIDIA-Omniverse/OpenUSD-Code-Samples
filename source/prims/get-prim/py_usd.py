# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Union
from pxr import Usd, Sdf

def get_prim_by_path(stage: Usd.Stage, prim_path: Union[str, Sdf.Path]) -> Usd.Prim:
    return stage.GetPrimAtPath(prim_path)

##############
# Full Usage
##############

from pxr import UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create some prims
UsdGeom.Xform.Define(stage, "/World/Group")
UsdGeom.Cube.Define(stage, "/World/Group/Foo")

# Get a prim using a str object
group_prim_path = "/World/Group"
group_prim = get_prim_by_path(stage, group_prim_path)
# Get a prim using an Sdf.Path object
foo_prim_path = Sdf.Path("/World/Group/Foo")
foo_prim = get_prim_by_path(stage, foo_prim_path)

# Print the prim objects that were retrieved 
print(group_prim)
print(foo_prim)

# Check that the prims retrieve match the paths provided
assert group_prim.GetPath() == Sdf.Path(group_prim_path)
assert foo_prim.GetPath() == foo_prim_path
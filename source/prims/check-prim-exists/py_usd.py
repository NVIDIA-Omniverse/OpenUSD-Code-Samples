# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd


def check_prim_exists(prim: Usd.Prim) -> bool:
    if prim.IsValid():
        return True
    return False

#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# Create one prim and 
cube: Usd.Prim = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Cube")).GetPrim()
empty_prim = Usd.Prim()

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check if prims exist
assert check_prim_exists(default_prim)
assert check_prim_exists(cube)
assert not check_prim_exists(empty_prim)
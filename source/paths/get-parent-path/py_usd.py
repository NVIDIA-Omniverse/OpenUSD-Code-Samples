# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf

def get_parent_path(prim_path: Sdf.Path) -> Sdf.Path:
    parent_path = prim_path.GetParentPath()
    return parent_path

#############
# Full Usage
#############
from pxr import Usd, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)
cone_prim = UsdGeom.Cone.Define(stage, Sdf.Path("/World/Cone")).GetPrim()

# Given Sdf.Path('/World/Cone') for my_prim_path, parent_path will contain Sdf.Path('/World')
parent_path = get_parent_path(cone_prim.GetPrimPath())

usda = stage.GetRootLayer().ExportToString()
print(usda)

assert parent_path == default_prim.GetPrimPath()
# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def get_child_prim(parent_prim, child_name) -> Usd.Prim:
    child_prim: Usd.Prim = parent_prim.GetChild(child_name)  
    return child_prim

#############
# Full Usage
#############

from pxr import Sdf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

cube: Usd.Prim = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("Cube"))

child_prim = get_child_prim(default_prim, "Cube")

usda = stage.GetRootLayer().ExportToString()
print(usda)

assert child_prim.GetParent() == default_prim
assert child_prim.GetPath() == cube.GetPath()
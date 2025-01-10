# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf

def concat_property_with_prim_path(prim_path: Sdf.Path, prop) -> Sdf.Path:
    prop_path = prim_path.AppendProperty(prop)
    return prop_path

#############
# Full Usage
#############

# e.g., get path to "points" attribute on a mesh prim
from pxr import UsdGeom, Usd

stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)
mesh_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Mesh")).GetPrim()

prop_path: Sdf.Path = concat_property_with_prim_path(mesh_prim.GetPrimPath(), UsdGeom.Tokens.points) #nothing happend so did it get added?

usda = stage.GetRootLayer().ExportToString()
print(usda)

assert Sdf.Path.IsValidPathString(prop_path.pathString)
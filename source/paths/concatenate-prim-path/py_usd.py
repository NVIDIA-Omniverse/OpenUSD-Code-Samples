# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf

def concat_prim_path(prim_path: Sdf.Path, path_to_add: str) -> Sdf.Path:
    concat_path = prim_path.AppendPath(path_to_add)
    return concat_path

#############
# Full Usage
#############

from pxr import Usd, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# Concatenate the Paths
concatenated_prim_path: Sdf.Path = concat_prim_path(default_prim.GetPrimPath(), "Kitchen_set/Props_grp/North_grp/NorthWall_grp/MeasuringSpoon_1")

usda = stage.GetRootLayer().ExportToString()
print(usda)

assert concatenated_prim_path.pathString == "/World/Kitchen_set/Props_grp/North_grp/NorthWall_grp/MeasuringSpoon_1"
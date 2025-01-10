# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def add_specialize_to(base_prim: Usd.Prim, specializes: Usd.Specializes) -> bool:
    return specializes.AddSpecialize(base_prim.GetPath())

#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

prim: Usd.Prim = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("prim")).GetPrim()
base: Usd.Prim = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("base")).GetPrim()
specializes: Usd.Specializes = prim.GetSpecializes()

added_successfully = add_specialize_to(base, specializes)

usda = stage.GetRootLayer().ExportToString()
print(usda)

assert added_successfully
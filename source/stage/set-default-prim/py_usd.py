# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd 

def set_default_prim(stage: Usd.Stage, prim: Usd.Prim):
    stage.SetDefaultPrim(prim)


#############
# Full Usage
#############

from pxr import UsdGeom, Sdf

# Create new USD stage for this sample
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Create an xform which should be set as the default prim
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()

# Make the xform the default prim
set_default_prim(stage, default_prim)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected default prim was set
assert stage.GetDefaultPrim() == default_prim

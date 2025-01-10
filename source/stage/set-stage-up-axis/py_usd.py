# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom

def set_up_axis(stage: Usd.Stage, axis: UsdGeom.Tokens):
    UsdGeom.SetStageUpAxis(stage, axis)


#############
# Full Usage
#############
axis: UsdGeom.Tokens = UsdGeom.Tokens.z
stage: Usd.Stage = Usd.Stage.CreateInMemory()
set_up_axis(stage, axis)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected upAxis was set
assert UsdGeom.GetStageUpAxis(stage) == axis

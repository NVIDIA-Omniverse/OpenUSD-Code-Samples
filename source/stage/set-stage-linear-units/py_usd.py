# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom


def set_meters_per_unit(stage: Usd.Stage, unit: UsdGeom.LinearUnits = UsdGeom.LinearUnits.centimeters):
    UsdGeom.SetStageMetersPerUnit(stage, unit) # Any double-precision float can be used for metersPerUnit.


#############
# Full Usage
#############
unit: UsdGeom.LinearUnits = UsdGeom.LinearUnits.centimeters
stage: Usd.Stage = Usd.Stage.CreateInMemory()
set_meters_per_unit(stage, unit)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected meterPerUnit were set
assert UsdGeom.GetStageMetersPerUnit(stage) == unit

# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def create_new_stage(path : str, stage_name : str = "my_new_stage.usd") -> Usd.Stage:
    layer_path : str = path + stage_name
    stage: Usd.Stage = Usd.Stage.CreateNew(layer_path)
    return stage

##############
# Full Usage
##############

from pxr import UsdGeom, Sdf

# Create a stage
stage = create_new_stage("my_path/")

# Create and set /World Xform prim as the default prim
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Print the stage
print(stage)

# Save the stage
stage.Save()

# Export the stage to a new file. Serialization format can be changed based on provided file extenson (.usd, .usda, .usdc)
stage.Export("my_path/my_new_stage.usda")

assert stage.GetRootLayer().ExportToString() # .usda for the stage exists
assert Usd.Stage.Open("my_path/my_new_stage.usd") # Stage can be opened
assert stage.GetDefaultPrim().GetPath() == Sdf.Path("/World") # Default prim is set at corect path
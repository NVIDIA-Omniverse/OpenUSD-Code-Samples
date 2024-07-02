# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, Tf

def create_stage_in_memory(identifier : str = "MyStage") -> Usd.Stage:
    stage: Usd.Stage = Usd.Stage.CreateInMemory(identifier)
    return stage

##############
# Full Usage
##############

from pxr import UsdGeom, Sdf

# Create an in-memory Stage 
stage = create_stage_in_memory()

# Create and set /World Xform prim as the default prim
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Print the stage
print(stage)

# Export the stage to a new file. Serialization format can be changed based on provided file extenson (.usd, .usda, .usdc)
stage.Export("my_path/my_new_stage.usda")

assert stage.GetRootLayer().ExportToString() # .usda for the stage exists
assert stage.GetDefaultPrim().GetPath() == Sdf.Path("/World") # Default prim is set at corect path
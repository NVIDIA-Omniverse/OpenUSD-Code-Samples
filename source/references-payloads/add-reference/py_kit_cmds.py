# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import Usd, Sdf

def add_int_reference(prim: Usd.Prim, ref_target_path: Sdf.Path) -> None:
    omni.kit.commands.execute("AddReference",
        stage=prim.GetStage(),
        prim_path = prim.GetPath(), # an existing prim to add the reference to.
        reference=Sdf.Reference(
            primPath = ref_target_path
        )
    )

def add_ext_reference(prim: Usd.Prim, ref_asset_path: str, ref_target_path: Sdf.Path) -> None:
    omni.kit.commands.execute("AddReference",
        stage=prim.GetStage(),
        prim_path = prim.GetPath(), # an existing prim to add the reference to.
        reference=Sdf.Reference(
            assetPath = ref_asset_path,
            primPath = ref_target_path
        )
    )


#############
# Full Usage
#############
import omni.usd
from pxr import UsdGeom

# Create new USD stage for this sample in OV
context: omni.usd.UsdContext = omni.usd.get_context()
success: bool = context.new_stage()
stage: Usd.Stage = context.get_stage()

# Create and define default prim, so this file can be easily referenced again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create a xform which should hold all references in this sample
ref_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/ref_prim")).GetPrim()

# Add an internal reference
intern_target_path: Sdf.Path = Sdf.Path("/World/intern_target")
target_prim: Usd.Prim = UsdGeom.Xform.Define(stage, intern_target_path).GetPrim()
add_int_reference(ref_prim, intern_target_path)

# Add an external reference to specific prim
add_ext_reference(ref_prim, "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Add other external reference to default prim
add_ext_reference(ref_prim, "C:/path/to/other/file.usd", Sdf.Path.emptyPath)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Get a list of all prepended references
references = []
for prim_spec in ref_prim.GetPrimStack():
    references.extend(prim_spec.referenceList.prependedItems)

# Check that the reference prim was created and that the references are correct
assert ref_prim.IsValid()
assert references[0] == Sdf.Reference(primPath=intern_target_path)
assert references[1] == Sdf.Reference(assetPath="C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
assert references[2] == Sdf.Reference(assetPath="C:/path/to/other/file.usd")
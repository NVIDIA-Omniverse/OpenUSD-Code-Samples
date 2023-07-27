# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
import omni.usd
from pxr import Usd, Sdf, UsdGeom

def create_int_reference(context: omni.usd.UsdContext, prim_path: Sdf.Path, ref_target_path: Sdf.Path) -> Usd.Prim:
    omni.kit.commands.execute("CreateReference",
        path_to=prim_path, # Prim path for where to create the reference
        prim_path=ref_target_path,
        usd_context=context
    )
    return stage.GetPrimAtPath(prim_path)

def create_ext_reference(context: omni.usd.UsdContext, prim_path: Sdf.Path, ref_asset_path: str, ref_target_path: Sdf.Path) -> Usd.Prim:
    omni.kit.commands.execute("CreateReference",
        path_to=prim_path, # Prim path for where to create the reference
        asset_path=ref_asset_path, # The file path to reference. Relative paths are accepted too.
        prim_path=ref_target_path,
        usd_context=context
    )
    return stage.GetPrimAtPath(prim_path)


#############
# Full Usage
#############

# Create new USD stage for this sample in OV
context: omni.usd.UsdContext = omni.usd.get_context()
success: bool = context.new_stage()
stage: Usd.Stage = context.get_stage()

# Create and define default prim, so this file can be easily referenced again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create and add internal reference to specific prim
intern_target_path: Sdf.Path = Sdf.Path("/World/intern_target")
target_prim: Usd.Prim = UsdGeom.Xform.Define(stage, intern_target_path).GetPrim()
int_ref_prim: Usd.Prim = create_int_reference(context, Sdf.Path("/World/int"), intern_target_path)

# Create and add external reference to specific prim
ext_ref_prim: Usd.Prim = create_ext_reference(context, Sdf.Path("/World/ref_ext"), "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Create and add external reference to default prim
def_ext_ref_prim: Usd.Prim = create_ext_reference(context, Sdf.Path("/World/ref_ext_default"), "C:/path/to/other/file.usd", Sdf.Path.emptyPath)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the reference prims were created
assert success
assert target_prim.IsValid()
assert int_ref_prim.IsValid()
assert ext_ref_prim.IsValid()
assert def_ext_ref_prim.IsValid()

assert int_ref_prim.GetPrimStack()[0].referenceList.prependedItems[0] == Sdf.Reference(primPath=intern_target_path)
assert ext_ref_prim.GetPrimStack()[0].referenceList.prependedItems[0] == Sdf.Reference(assetPath="file:/C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
assert def_ext_ref_prim.GetPrimStack()[0].referenceList.prependedItems[0] == Sdf.Reference(assetPath="file:/C:/path/to/other/file.usd")
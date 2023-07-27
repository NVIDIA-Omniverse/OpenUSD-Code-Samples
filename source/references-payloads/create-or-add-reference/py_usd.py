# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, Sdf, UsdGeom

def add_int_reference(prim: Usd.Prim, ref_target_path: Sdf.Path) -> None:
    references: Usd.References = prim.GetReferences()
    references.AddInternalReference(ref_target_path)

def add_ext_reference(prim: Usd.Prim, ref_asset_path: str, ref_target_path: Sdf.Path) -> None:
    references: Usd.References = prim.GetReferences()
    references.AddReference(
        assetPath=ref_asset_path,
        primPath=ref_target_path # OPTIONAL: Reference a specific target prim. Otherwise, uses the referenced layer's defaultPrim.
    )


#############
# Full Usage
#############

# Create new USD stage for this sample
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Create and define default prim, so this file can be easily referenced again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create an xform which should hold all references in this sample
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

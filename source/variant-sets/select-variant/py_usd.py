# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def select_variant_from_varaint_set(prim: Usd.Prim, variant_set_name: str, variant_name: str) -> None:
    variant_set = prim.GetVariantSets().GetVariantSet(variant_set_name)
    variant_set.SetVariantSelection(variant_name)

#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# Create the Variant Set
shading_varset: Usd.VariantSet = default_prim.GetVariantSets().AddVariantSet("shading")

# Add Variants to the Variant Set
shading_varset.AddVariant("cell_shading")
shading_varset.AddVariant("realistic")

select_variant_from_varaint_set(default_prim, "shading", "realistic")

usda = stage.GetRootLayer().ExportToString()
print(usda)


assert default_prim.GetVariantSets().GetVariantSet("shading").GetVariantSelection() == "realistic"
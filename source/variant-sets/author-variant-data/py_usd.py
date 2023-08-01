# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

shading_varset = prim.GetVariantSets().GetVariantSet("shading")
selected_variant = shading_varset.GetVariantSelection()

shading_varset.SetVariantSelection(variant_name)
with shading_varset.GetVariantEditContext():
    # Specs authored within this context are authored just for the variant.
    ...

# Set the variant selection back to the previously selected variant.
# Alternatively, you can use Usd.VariantSet.ClearVariantSelection()
# if you know that there isn't a variant selection in the current EditTarget.
if selected_variant:
    shading_varset.SetVariantSelection(selected_variant)

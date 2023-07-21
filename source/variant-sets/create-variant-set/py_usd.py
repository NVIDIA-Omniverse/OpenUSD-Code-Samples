# Create the variant set and add your variants to it.
variants = ["red", "blue", "green"]
shading_varset = prim.GetVariantSets().AddVariantSet("shading")
for variant_name in variants:
    shading_varset.AddVariant(variant_name)
    
# Author opinions in for each variant. You could do this in the previous for loop too.
for variant_name in variants:
    # You must select a variant to author opinion for it.
    shading_varset.SetVariantSelection(variant_name)
    with shading_varset.GetVariantEditContext():
        # Specs authored within this context are authored just for the variant.
        ...

# Remember to set the variant you want selected once you're done authoring.
shading_varset.SetVariantSelection(variants[0])
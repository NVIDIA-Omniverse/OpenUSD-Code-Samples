.. meta::
    :description: Universal Scene Description (USD) Python code snippet for authoring data for a particular snippet.
    :keywords: USD, Python, snippet, variant set, composition, variant

====================================
Author Data for a Particular Variant
====================================

Opinions (i.e. data) for a particular variant can be authored on different layers. This shows how you can author opinions for an existing variant that
might have been authored on a different layer.

USD API
-------
.. code-block:: python

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
.. meta::
    :description: Universal Scene Description (USD) Python code snippet showing how to create a variant set.
    :keywords: USD, Python, snippet, variant set, composition, variant

===================================
Create a Variant Set
===================================

.. note::
    If this is your first time authoring a variant set, we recommend that you follow `Authoring Variants USD tutorial <https://graphics.pixar.com/usd/docs/Authoring-Variants.html>`_ first.

A `Variant Set <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-variantset>`_ is a composition arc that serves as a sort of "switchable Reference" allowing you to provide alternate property opinions or entire prim hierarchies. In this snippet, you'll find how to create a Variant Set, add variants to the new Variant Set and author opinions for each variant.

USD API
-------
.. code-block:: python

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
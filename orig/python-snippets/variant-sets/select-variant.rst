.. meta::
    :description: Universal Scene Description (USD) Python code snippet for selecting a variant for a variant set.
    :keywords: USD, Python, snippet, variant set, composition, variant

====================================
Select a Variant for a Variant Set
====================================

Apart from selecting a default Variant when you create a Variant Set, you may want to change the selection in other USD layers. For example, a model could have a shading Variant Set defined, but when you Reference that model a few times in a Stage, you may want to select a different shading Variant for each Reference.

USD API
-------
.. code-block:: python

    shading_varset = prim.GetVariantSets().GetVariantSet("shading")
    shading_varset.SetVariantSelection(variant_name)
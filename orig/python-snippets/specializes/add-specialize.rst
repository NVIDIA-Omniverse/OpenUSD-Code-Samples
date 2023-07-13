.. meta::
    :description: Universal Scene Description (USD) Python code snippet for adding a Specialize composition arc to a prim.
    :keywords: USD, Python, snippet, specialize, AddSpecialize, composition, composition arc

======================
Add a Specialize
======================

A `Specialize <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-specializes>`_ is a composition arc that enables a prim to contain all of the scene description contained in the base prim it specializes. The difference between Specialize and Inherit is that opinions authored on the prim with the specialize arc will always be stronger than the base prim. This snippet shows how to add a Specialize arc to a prim. A single prim can have multiple Specializes.


USD API
-------
.. code-block:: python

    from pxr import Usd

    prim: Usd.Prim = stage.GetPrimAtPath("/World/my/prim")
    base: Usd.Prim = stage.GetPrimAtPath("/World/my/base")
    specializes: Usd.Specializes = prim.GetSpecializes()
    specializes.AddSpecialize(base.GetPath())
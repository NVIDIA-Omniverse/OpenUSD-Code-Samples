.. meta::
    :description: Universal Scene Description (USD) Python code snippet for adding an Inherit composition arc to a prim.
    :keywords: USD, Python, snippet, inherit, AddInherit, composition, composition arc

======================
Add an Inherit
======================

An `Inherit <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-inherits>`_ is a composition arc that enables a prim to contain all of the scene description contained in the base prim it inherits. This enables users to author opinions on the base prim that are broadcast to all the prims that inherit it. The `Inherit USD Glossary entry <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-inherits>`_ explains the nuances of the composition arc in more detail. This snippet shows how to add an Inherit arc to a prim. A single prim can have multiple Inherits.


USD API
-------
.. code-block:: python

    from pxr import Usd

    # The base prim typically uses the "class" Specifier to designate that it
    # is meant to be inherited and skipped in standard stage traversals
    quadruped_class: Usd.Prim = stage.CreateClassPrim("/_class_Quadruped")
    dog_prim: Usd.Prim = stage.GetPrimAtPath("/World/Dog")
    inherits: Usd.Inherits = dog_prim.GetInherits()
    inherits.AddInherit(quadruped_class.GetPath())
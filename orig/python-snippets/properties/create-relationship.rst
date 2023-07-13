.. meta::
    :description: Universal Scene Description (USD) Python code snippet for creating a Relationship.
    :keywords: USD, Python, snippet, property, relationship, create

==========================
Create a Relationship
==========================

A `Relationship <https://graphics.pixar.com/usd/release/api/class_usd_relationship.html>`_ is a type of :code:`Usd.Property` that points to other Prims, Attributes or Relationships. The Relationship targets are represented by a list of Paths. This snippet shows how to create a Relationship and set some initial targets.

USD API
-------
.. code-block:: python

    from pxr import Usd

    prim: Usd.Prim = stage.GetPrimAtPath("/World/MyPrim")
    custom_relationship: Usd.Relationship = prim.CreateRelationship("myCustomRelationship")
    # You can also use Usd.Relationship.AddTarget() to add targets to an existing Relationship.
    custom_relationship.SetTargets(["/World/TargetA", "/World/TargetB"])
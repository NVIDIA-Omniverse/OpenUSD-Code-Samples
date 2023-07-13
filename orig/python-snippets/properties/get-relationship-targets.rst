.. meta::
    :description: Universal Scene Description (USD) Python code snippet for getting the targets of a Relationship taking into account relationship forwarding.
    :keywords: USD, Python, snippet, relationship, targets, relationship forwarding

=================================
Get the Targets of a Relationship
=================================

If you need to get the targets of a Relationship, you can use `Usd.Relationship.GetForwardedTargets() <https://graphics.pixar.com/usd/release/api/class_usd_relationship.html#a66140abeac945df3998b3297e52ca99b>`_. This method will give you the final composed targets for the Relationship and also take into account the relationship forwarding. That is, if the Relationship itself targets another Relationship, we want to get the final targets in a potential chain of Relationships. Learn more about `relationship forwarding <https://graphics.pixar.com/usd/release/api/class_usd_relationship.html#usd_relationship_forwarding>`_.

USD API
-------
.. code-block:: python

    from pxr import Usd, UsdGeom

    # For example, getting the proxy prim on an Imageable
    proxy_prim_rel: Usd.Relationship = UsdGeom.Imageable(myprim).GetProxyPrimRel()
    proxyPrimTargets = proxy_prim_rel.GetForwardedTargets()
    

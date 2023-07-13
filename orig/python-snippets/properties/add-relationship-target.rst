.. meta::
    :description: Universal Scene Description (USD) Python code snippet for adding a target to a Relationship.
    :keywords: USD, Python, snippet, relationship, targets, property

=================================
Add a Relationship Target
=================================

If you just want to add a target to an existing Relationship, you can use `Usd.Relationship.AddTarget() <https://graphics.pixar.com/usd/release/api/class_usd_relationship.html#a0db3d68820f130f08152592b0fe10b00>`_ to add a Path to the Relationship's targets list.

USD API
-------
.. code-block:: python

    from pxr import Usd, UsdGeom

    # For example, adding a proxy prim target on an Imageable
    proxy_prim_rel: Usd.Relationship = UsdGeom.Imageable(myprim).GetProxyPrimRel()
    proxy_prim_rel.AddTarget("/World/MyProxy")
    

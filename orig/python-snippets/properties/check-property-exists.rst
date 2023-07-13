.. meta::
    :description: Universal Scene Description (USD) Python code snippets for checking if a Property exists.
    :keywords: USD, Python, snippet, property, relationship, attribute, IsValid, exists, valid

==========================
Check if a Property Exists
==========================

Certain functions may return a :code:`Usd.Property` object, but the Property may not exist due to an incorrect path or because of changes on the Stage. You can use `Usd.Object.IsValid() <https://graphics.pixar.com/usd/dev/api/class_usd_object.html#ac532c4b500b1a85ea22217f2c65a70ed>`_ to check if the Property is valid or exists.

.. note::
    Remember, that Properties consist of :code:`Usd.Attribute` and :code:`Usd.Relationship`. You can perform this check on both types of objects.

USD API
-------
.. code-block:: python

    from pxr import Usd

    pts_attr: Usd.Attribute = mesh_prim.GetAttribute("points")
    if pts_attr.IsValid():
        print("Attribute exists!")

Alternatively, :code:`Usd.Object` overrides the boolean operator so you can check with a simple boolean expression.

.. code-block:: python

    from pxr import Usd

    pts_attr: Usd.Attribute = mesh_prim.GetAttribute("points")
    if pts_attr:
        print("Attribute exists!")
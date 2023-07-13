.. meta::
    :description: Universal Scene Description (USD) Python code snippets for checking if a Prim exists on a Stage.
    :keywords: USD, Python, snippet, prim, exists, IsValid, valid

======================
Check if a Prim Exists
======================

Certain functions may return a :code:`Usd.Prim` object, but the Prim may not exist due to an incorrect path or because of changes on the Stage. You can use `Usd.Object.IsValid() <https://graphics.pixar.com/usd/dev/api/class_usd_object.html#ac532c4b500b1a85ea22217f2c65a70ed>`_ to check if the Prim is valid or exists.


USD API
-------
.. code-block:: python

    from pxr import Sdf, Usd

    prim_path = Sdf.Path("/World/Hello")
    prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
    if prim.IsValid():
        print("Prim exists!")

Alternatively, :code:`Usd.Object` overrides the boolean operator so you can check with a simple boolean expression.

.. code-block:: python

    from pxr import Sdf, Usd

    prim_path = Sdf.Path("/World/Hello")
    prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
    if prim:
        print("Prim exists!")
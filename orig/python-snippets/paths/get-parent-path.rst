
.. meta::
    :description: Universal Scene Description (USD) Python code snippet for getting the parent path from a prim path.
    :keywords: USD, Python, snippet, prim, path, GetParentPath

===================================
Get the Parent Path for a Prim Path
===================================

If you want have a Prim path and you want to get the Prim path of its parent, you can use `Sdf.Path.GetParentPath() <https://graphics.pixar.com/usd/release/api/class_sdf_path.html#a0da79e196526d8f2e9bfd075e36e505f>`_.

USD API
--------------
.. code-block:: python

    from pxr import Sdf

    parent_path = my_prim_path.GetParentPath()

    # Given Sdf.Path('/World/Cone') for my_prim_path, parent_path will contain Sdf.Path('/World')




.. meta::
    :description: Universal Scene Description (USD) Python code snippet showing how to concatenate a property name with a prim path.
    :keywords: USD, Python, snippet, prim, property, path, AppendProperty

============================================
Concatenate a Property Name with a Prim Path
============================================

If you want to concatenate a property name with a Prim path, you can use `Sdf.Path.AppendProperty <https://graphics.pixar.com/usd/release/api/class_sdf_path.html#a94b67bfea8a8295271a32014b563d913>`. In this example, given :code:`Sdf.Path("/World/MyMesh")` in :code:`mesh_prim_path`, :code:`points_attr_path` will contain :code:`Sdf.Path("/World/MyMesh.points")`.

USD API
--------------
.. code-block:: python

    # e.g., get path to "points" attribute on a mesh prim
    from pxr import UsdGeom, Sdf

    points_attr_path = mesh_prim_path.AppendProperty(UsdGeom.Tokens.points)

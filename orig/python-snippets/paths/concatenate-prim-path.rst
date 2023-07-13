.. meta::
    :description: Universal Scene Description (USD) Python code snippet for concatenating prim paths.
    :keywords: USD, Python, snippet, prim, property, path, AppendPath

==================================
Concatenate a Prim Path
==================================

If you want to concatenate two strings to extend a prim path, you can use `Sdf.Path` to store and manipulate prim and property paths. This is useful for extending a prim path with the name of a new child prim that you plan to create. In this snippet we use :code:`Sdf.Path.AppendPath()`, but you can `learn more about other append methods <https://graphics.pixar.com/usd/release/api/class_sdf_path.html>`_.

USD API
--------------
.. code-block:: python

    from pxr import Sdf

    prim_path = Sdf.Path("/Kitchen_set/Props_grp")
    concat_prim_path = prim_path.AppendPath("North_grp/NorthWall_grp/MeasuringSpoon_1")
    # concat_prim_path now contains Sdf.Path("/Kitchen_set/Props_grp/North_grp/NorthWall_grp/MeasuringSpoon_1")


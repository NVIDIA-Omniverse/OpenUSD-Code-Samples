.. meta::
    :description: Universal Scene Description (USD) Python code snippet for finding all the Prims on a Stage of a certain type.
    :keywords: USD, Python, snippet, prim, type, Traverse, IsA

==================================
Find All the Prims of a Given Type
==================================

If you want to find all of the prims of a certain type, you can `Traverse <https://graphics.pixar.com/usd/release/api/class_usd_stage.html#adba675b55f41cc1b305bed414fc4f178>`_ the stage and use `Usd.Prim.IsA() <https://graphics.pixar.com/usd/release/api/class_usd_prim.html#a0a50d49f93140253633fa2e256a0e43f>`_ to compare the type of every prim on the stage with the type you are looking for.

USD API
--------------
.. code-block:: python

    from pxr import UsdGeom

    # e.g., find all prims of type UsdGeom.Mesh
    mesh_prims = [x for x in stage.Traverse() if x.IsA(UsdGeom.Mesh)]

.. warning::
    This will be slow for stages with many prims, as stage traversal is currently single-threaded. Learn more about `scene complexity <https://graphics.pixar.com/usd/release/maxperf.html#what-makes-a-usd-scene-heavy-expensive>`_.

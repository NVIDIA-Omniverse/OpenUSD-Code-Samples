.. meta::
    :description: Universal Scene Description (USD) Python code snippets showing how to compute the bounding box for a prim.
    :keywords: USD, Python, snippet, bounding box, prim, omni.usd, bbox, ComputeWorldBound, ComputeAlignedBox

===================================
Compute the Bounding Box for a Prim
===================================

USD includes functions for computing the bounding box for a prim and all of its descendants. Bounding boxes are represented by the minimum point and maximum point of the bounding box. The two points form a diagonal across the interior of the box. These snippets show how to compute and retrieve a prim's bounding box in world space.

`omni.usd` API
------------------
.. code-block:: python

    import typing

    import carb
    import omni.usd

    def compute_path_bbox(prim_path: str) -> typing.Tuple[carb.Double3, carb.Double3]:
        """
        Compute Bounding Box using omni.usd.UsdContext.compute_path_world_bounding_box
        See https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.UsdContext.html#omni.usd.UsdContext.compute_path_world_bounding_box

        Args:
            prim_path: A prim path to compute the bounding box.
        Returns: 
            A range (i.e. bounding box) as a minimum point and maximum point.
        """
        return omni.usd.get_context().compute_path_world_bounding_box(prim_path)

USD API
-------
.. code-block:: python

    from pxr import Usd, UsdGeom, Gf

    def compute_bbox(prim: Usd.Prim) -> Gf.Range3d:
        """
        Compute Bounding Box using ComputeWorldBound at UsdGeom.Imageable
        See https://graphics.pixar.com/usd/release/api/class_usd_geom_imageable.html

        Args:
            prim: A prim to compute the bounding box.
        Returns: 
            A range (i.e. bounding box), see more at: https://graphics.pixar.com/usd/release/api/class_gf_range3d.html
        """
        imageable = UsdGeom.Imageable(prim)
        time = Usd.TimeCode.Default() # The time at which we compute the bounding box
        bound = imageable.ComputeWorldBound(time, UsdGeom.Tokens.default_)
        bound_range = bound.ComputeAlignedBox()
        return bound_range

Alternatively, if you need to compute the bounding box for multiple prims on a stage, `UsdGeom.BBoxCache <https://graphics.pixar.com/usd/dev/api/class_usd_geom_b_box_cache.html>`_ is more efficient.

.. code-block:: python

    from pxr import Usd, UsdGeom, Gf

    def compute_bbox_with_cache(cache: UsdGeom.BBoxCache, prim: Usd.Prim) -> Gf.Range3d:
        """
        Compute Bounding Box using ComputeWorldBound at UsdGeom.BBoxCache. More efficient if used multiple times.
        See https://graphics.pixar.com/usd/dev/api/class_usd_geom_b_box_cache.html
        
        Args:
            cache: A cached, i.e. `UsdGeom.BBoxCache(Usd.TimeCode.Default(), ['default', 'render'])`
            prim: A prim to compute the bounding box.
        Returns: 
            A range (i.e. bounding box), see more at: https://graphics.pixar.com/usd/release/api/class_gf_range3d.html

        """
        bound = cache.ComputeWorldBound(prim)
        bound_range = bound.ComputeAlignedBox()
        return bound_range


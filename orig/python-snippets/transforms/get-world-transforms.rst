.. meta::
    :description: Universal Scene Description (USD) Python code snippets showing how to get the world space transforms for a prim.
    :keywords: USD, Python, snippet, local space, local, transforms, omni.usd, get_local_transform_SRT, GetLocalTransformation

=========================================
Get the World Space Transforms for a Prim
=========================================

If you need to get the transformation of a prim in world space (i.e. taking into account the transformations of any ancestor prims), you can use a convenience function in Kit, `omni.usd.get_world_transform_matrix() <https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.get_world_transform_matrix.html>`_. Alternatively, you can use `UsdGeom.Xformable.ComputeLocalToWorldTransform() <https://graphics.pixar.com/usd/release/api/class_usd_geom_imageable.html#a8e3fb09253ba63d63921f665d63cd270>`_ or `UsdGeom.XformCache.GetLocalToWorldTransform() <https://graphics.pixar.com/usd/release/api/class_usd_geom_xform_cache.html#aaba1e27b19713a49c1b5b77805184113>`_ to get the world transformation matrix. Once you have the matrix, decompose it into individual xform components.

`omni.usd` API
------------------
.. code-block:: python

    def get_world_transform_xform(prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]
        """
        Get the local transformation of a prim using omni.usd.get_world_transform_matrix().
        See https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.get_world_transform_matrix.html
        Args:
            prim: The prim to calculate the world transformation.
        Returns:
            A tuple of:
            - Translation vector.
            - Rotation quaternion, i.e. 3d vector plus angle.
            - Scale vector.
        """
        world_transform: Gf.Matrix4d = omni.usd.get_world_transform_matrix(prim)
        translation: Gf.Vec3d = world_transform.ExtractTranslation()
        rotation: Gf.Rotation = world_transform.ExtractRotation()
        scale: Gf.Vec3d = Gf.Vec3d(*(v.GetLength() for v in world_transform.ExtractRotationMatrix()))
        return translation, rotation, scale
        

USD API
-------
.. code-block:: python

    import typing
    from pxr import Usd, UsdGeom, Gf

    def get_world_transform_xform(prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]:
        """
        Get the local transformation of a prim using Xformable.
        See https://graphics.pixar.com/usd/release/api/class_usd_geom_xformable.html
        Args:
            prim: The prim to calculate the world transformation.
        Returns:
            A tuple of:
            - Translation vector.
            - Rotation quaternion, i.e. 3d vector plus angle.
            - Scale vector.
        """
        xform = UsdGeom.Xformable(prim)
        time = Usd.TimeCode.Default() # The time at which we compute the bounding box
        world_transform: Gf.Matrix4d = xform.ComputeLocalToWorldTransform(time)
        translation: Gf.Vec3d = world_transform.ExtractTranslation()
        rotation: Gf.Rotation = world_transform.ExtractRotation()
        scale: Gf.Vec3d = Gf.Vec3d(*(v.GetLength() for v in world_transform.ExtractRotationMatrix()))
        return translation, rotation, scale

Alternatively, if you need to compute the world transform for multiple prims on a stage, `UsdGeom.XformCache <https://graphics.pixar.com/usd/release/api/class_usd_geom_xform_cache.html>`_ is more efficient.

.. code-block:: python

    import typing
    from pxr import Usd, UsdGeom, Gf

    def get_world_transform_cache(cache: UsdGeom.XformCache, prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]:
        """
        Get the local transformation of a prim using UsdGeom.XformCache.
        See: https://graphics.pixar.com/usd/release/api/class_usd_geom_xform_cache.html
        Args:
            cache: A cache, created for example as `UsdGeom.XformCache()`
            prim: The prim to calculate the world transformation.
        Returns:
            A tuple of:
            - Translation vector.
            - Rotation quaternion, i.e. 3d vector plus angle.
            - Scale vector.
        """
        time = Usd.TimeCode.Default() # The time at which we compute the bounding box
        world_transform: Gf.Matrix4d = cache.GetLocalToWorldTransform(time)
        translation: Gf.Vec3d = world_transform.ExtractTranslation()
        rotation: Gf.Rotation = world_transform.ExtractRotation()
        scale: Gf.Vec3d = Gf.Vec3d(*(v.GetLength() for v in world_transform.ExtractRotationMatrix()))
        return translation, rotation, scale


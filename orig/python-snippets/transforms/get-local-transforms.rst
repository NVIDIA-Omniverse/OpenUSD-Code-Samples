.. meta::
    :description: Universal Scene Description (USD) Python code snippets showing how to get the local transform for a prim.
    :keywords: USD, Python, snippet, local space, local, transforms, omni.usd, get_local_transform_SRT, GetLocalTransformation

=========================================
Get the Local Space Transforms for a Prim
=========================================

If you need to get the local transformation of a prim (i.e. not taking into account the transformations of any ancestor prims), you can use a convenience function in Kit, `omni.usd.get_local_transform_SRT() <https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.get_local_transform_SRT.html>`_. Alternatively, you can use `UsdGeom.Xformable.GetLocalTransformation() <https://graphics.pixar.com/usd/release/api/class_usd_geom_xformable.html#a9a04ccb1ba8aa16e8cc1e878c2c92969>`_ to get the local transformation matrix and decompose it into individual components.

`omni.usd` API
------------------
.. code-block:: python

    import typing
    import omni.usd
    from pxr import Gf

    def get_local_transform_omni(prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]:
        """
        Get the local transformation of a prim using omni.usd.get_local_transform_SRT.
        See https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.get_local_transform_SRT.html
        Args:
            prim: The prim to calculate the local transformation.
        Returns:
            A tuple of:
            - Translation vector.
            - Rotation quaternion, i.e. 3d vector plus angle.
            - Scale vector.
        """
        local_transform = omni.usd.get_local_transform_SRT(cube_prim)
        scale: Gf.Vec3d = local_transform[0]
        rotation: Gf.Vec3d = local_transform[1]
        rotation_order: float = local_transform[2]
        translation: Gf.Vec3d = local_transform[3]
        return translation, Gf.Rotation(rotation, rotation_order), scale


USD API
-------
.. code-block:: python

    import typing
    from pxr import UsdGeom, Gf

    def get_local_transform_xform(prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]:
        """
        Get the local transformation of a prim using Xformable.
        See https://graphics.pixar.com/usd/release/api/class_usd_geom_xformable.html
        Args:
            prim: The prim to calculate the local transformation.
        Returns:
            A tuple of:
            - Translation vector.
            - Rotation quaternion, i.e. 3d vector plus angle.
            - Scale vector.
        """
        xform = UsdGeom.Xformable(prim)
        local_transformation: Gf.Matrix4d = xform.GetLocalTransformation()
        translation: Gf.Vec3d = local_transformation.ExtractTranslation()
        rotation: Gf.Rotation = local_transformation.ExtractRotation()
        scale: Gf.Vec3d = Gf.Vec3d(*(v.GetLength() for v in local_transformation.ExtractRotationMatrix()))
        return translation, rotation, scale

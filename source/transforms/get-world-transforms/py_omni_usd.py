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
    

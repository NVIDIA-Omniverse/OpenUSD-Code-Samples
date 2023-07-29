# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

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


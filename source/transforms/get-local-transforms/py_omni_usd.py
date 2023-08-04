# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import typing
import omni.usd
from pxr import Usd, Gf

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
    local_transform = omni.usd.get_local_transform_SRT(prim)
    scale: Gf.Vec3d = local_transform[0]
    rotation: Gf.Vec3d = local_transform[1]
    rotation_order: float = local_transform[2]
    translation: Gf.Vec3d = local_transform[3]
    return translation, Gf.Rotation(rotation, rotation_order), scale

#############
# Full Usage
#############

import omni.kit.commands

# Create an Xform with a Cube Prim as it's Child
omni.kit.commands.execute('CreatePrimWithDefaultXform',
	prim_type='Xform',
	attributes={},
	select_new_prim=True)

omni.kit.commands.execute('TransformMultiPrimsSRTCpp',
	count=1,
	paths=['/World/Xform'],
	new_translations=[100, 0, 0],
	new_rotation_eulers=[0, 50 ,0],
	new_rotation_orders=[0, 1, 2],
	new_scales=[5, 5, 5],
	old_translations=[0.0, 0.0, 0.0],
	old_rotation_eulers=[0.0, 0.0, 0.0],
	old_rotation_orders=[0, 1, 2],
	old_scales=[1.0, 1.0, 1.0],
	usd_context_name='',
	time_code=0.0)

omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
	prim_type='Cube',
	prim_path='/World/Xform/Cube',
	select_new_prim=True,
	prepend_default_prim=False)

omni.kit.commands.execute('TransformMultiPrimsSRTCpp',
	count=1,
	paths=['/World/Xform/Cube'],
	new_translations=[4, 0, 0],
	new_rotation_eulers=[100, 0 ,0],
	new_rotation_orders=[0, 1, 2],
	new_scales=[2, 2, 2],
	old_translations=[0.0, 0.0, 0.0],
	old_rotation_eulers=[0.0, 0.0, 0.0],
	old_rotation_orders=[0, 1, 2],
	old_scales=[1.0, 1.0, 1.0],
	usd_context_name='',
	time_code=0.0)

stage = omni.usd.get_context().get_stage()
cube_prim = stage.GetPrimAtPath("/World/Xform/Cube")
transform = get_local_transform_omni(cube_prim)

assert transform[0] == cube_prim.GetAttribute('xformOp:translate').Get()
assert (100,0,0) == cube_prim.GetAttribute('xformOp:rotateXYZ').Get()
assert transform[2] == cube_prim.GetAttribute('xformOp:scale').Get()
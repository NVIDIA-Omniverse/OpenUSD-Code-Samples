# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.usd
from pxr import Usd, Gf
import typing

def get_world_transform_xform(prim: Usd.Prim) -> typing.Tuple[Gf.Vec3d, Gf.Rotation, Gf.Vec3d]:
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
transform = get_world_transform_xform(cube_prim)
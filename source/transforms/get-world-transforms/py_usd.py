# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.transform
# SPDX-License-Identifier: Apache-2.0

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

#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

xform: Usd.Prim = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("Xform"))
xform.AddTranslateOp().Set(value=(100,10,0))
xform.AddRotateXYZOp().Set(value=(0,50,0))
xform.AddScaleOp().Set(value=(5,5,5))

cube = UsdGeom.Cube.Define(stage, xform.GetPath().AppendPath("Cube"))
cube.AddTranslateOp().Set(value=(4,0,0))
cube.AddRotateXYZOp().Set(value=(100,0,0))
cube.AddScaleOp().Set(value=(2,2,2))

transform = get_world_transform_xform(cube)

usda = stage.GetRootLayer().ExportToString()
print(usda)

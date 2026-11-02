# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, Usd, UsdGeom

def get_world_position(prim: Usd.Prim, time: Usd.TimeCode = Usd.TimeCode.Default()) -> Gf.Vec3d:
    """
    Get the world space position of a prim's origin.
    See https://openusd.org/release/api/class_usd_geom_xformable.html
    Args:
        prim: The prim to get the world position of.
        time: The time at which to compute the position, for animated transforms.
    Returns:
        The position of the prim's origin in world space.
    """
    world_transform: Gf.Matrix4d = UsdGeom.Xformable(prim).ComputeLocalToWorldTransform(time)
    return world_transform.ExtractTranslation()


#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A parent Xform that is translated, rotated, and scaled
xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("Xform"))
xform.AddTranslateOp().Set(value=(100, 10, 0))
xform.AddRotateXYZOp().Set(value=(0, 50, 0))
xform.AddScaleOp().Set(value=(5, 5, 5))

# A child Cube that is offset from its parent
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, xform.GetPath().AppendPath("Cube"))
cube.AddTranslateOp().Set(value=(4, 0, 0))
cube.AddRotateXYZOp().Set(value=(100, 0, 0))
cube.AddScaleOp().Set(value=(2, 2, 2))

position: Gf.Vec3d = get_world_position(cube.GetPrim())
print(position)

# The Cube's local offset of 4 is scaled by 5 and rotated 50 degrees around Y, then moved by the parent's translation
expected = Gf.Vec3d(100, 10, 0) + Gf.Rotation(Gf.Vec3d(0, 1, 0), 50).TransformDir(Gf.Vec3d(20, 0, 0))
assert Gf.IsClose(position, expected, 1e-6)
# The world position is not the same as the local translation
assert not Gf.IsClose(position, Gf.Vec3d(4, 0, 0), 1e-6)

# For animated prims, pass the time to get the position at that time
xform.GetPrim().GetAttribute("xformOp:translate").Set(Gf.Vec3d(0, 10, 0), 1.0)
xform.GetPrim().GetAttribute("xformOp:translate").Set(Gf.Vec3d(200, 10, 0), 24.0)
assert Gf.IsClose(get_world_position(cube.GetPrim(), Usd.TimeCode(24.0)), expected + Gf.Vec3d(100, 0, 0), 1e-6)

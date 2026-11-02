# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, Usd, UsdGeom

def set_world_transform(prim: Usd.Prim, world_matrix: Gf.Matrix4d, time: Usd.TimeCode = Usd.TimeCode.Default()) -> None:
    """
    Set a prim's local transform so that its world space transform becomes world_matrix.
    See https://openusd.org/release/api/class_usd_geom_xformable.html
    """
    xformable = UsdGeom.Xformable(prim)
    # A prim's transform is relative to its parent, so remove the parent's world transform
    parent_to_world: Gf.Matrix4d = xformable.ComputeParentToWorldTransform(time)
    local_matrix: Gf.Matrix4d = world_matrix * parent_to_world.GetInverse()
    xformable.MakeMatrixXform().Set(local_matrix, time)


#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A parent that is moved and scaled, with a child Cube
table: UsdGeom.Xform = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Table"))
UsdGeom.XformCommonAPI(table).SetTranslate((100, 0, 0))
UsdGeom.XformCommonAPI(table).SetScale((2, 2, 2))
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Table/Cube"))

# Place the Cube at (110, 5, 0) in world space
set_world_transform(cube.GetPrim(), Gf.Matrix4d().SetTranslate(Gf.Vec3d(110, 5, 0)))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# The Cube ends up at the requested world position...
world: Gf.Matrix4d = cube.ComputeLocalToWorldTransform(Usd.TimeCode.Default())
assert Gf.IsClose(world.ExtractTranslation(), Gf.Vec3d(110, 5, 0), 1e-6)
# ...because its local translation accounts for the parent's translation and scale
assert Gf.IsClose(cube.GetLocalTransformation().ExtractTranslation(), Gf.Vec3d(5, 2.5, 0), 1e-6)

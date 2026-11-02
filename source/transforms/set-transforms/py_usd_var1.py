# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, Usd, UsdGeom

def set_transform_matrix(prim: Usd.Prim, matrix: Gf.Matrix4d, time: Usd.TimeCode = Usd.TimeCode.Default()) -> None:
    """
    Replace a prim's transform operations with a single matrix operation and set it.
    See https://openusd.org/release/api/class_usd_geom_xformable.html
    """
    # MakeMatrixXform() clears the existing operation order and adds one xformOp:transform
    transform_op: UsdGeom.XformOp = UsdGeom.Xformable(prim).MakeMatrixXform()
    transform_op.Set(matrix, time)


#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A Cube that already has separate translate and scale operations
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Cube"))
cube.AddTranslateOp().Set((1, 2, 3))
cube.AddScaleOp().Set((4, 4, 4))

# A matrix that scales by 2, rotates 90 degrees around Z, then translates by (10, 0, 0)
matrix: Gf.Matrix4d = (Gf.Matrix4d().SetScale(2)
                       * Gf.Matrix4d().SetRotate(Gf.Rotation(Gf.Vec3d(0, 0, 1), 90))
                       * Gf.Matrix4d().SetTranslate(Gf.Vec3d(10, 0, 0)))
set_transform_matrix(cube.GetPrim(), matrix)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# The old operations are no longer in the operation order, and the local transform is the matrix
assert [op.GetOpName() for op in cube.GetOrderedXformOps()] == ["xformOp:transform"]
assert Gf.IsClose(cube.GetLocalTransformation(), matrix, 1e-9)
# XformCommonAPI cannot edit a matrix operation; its setters return False
assert not UsdGeom.XformCommonAPI(cube).SetTranslate((0, 0, 0))

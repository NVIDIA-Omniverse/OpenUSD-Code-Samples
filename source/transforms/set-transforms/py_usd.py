# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Tuple
from pxr import Usd, UsdGeom

def set_transforms(prim: Usd.Prim, translation: Tuple[float, float, float], rotation: Tuple[float, float, float],
                   scale: Tuple[float, float, float], time: Usd.TimeCode = Usd.TimeCode.Default()) -> None:
    """
    Set the local translation, rotation (XYZ Euler angles in degrees), and scale of a prim.
    See https://openusd.org/release/api/class_usd_geom_xform_common_a_p_i.html
    """
    xform_api = UsdGeom.XformCommonAPI(prim)
    # The setters return False if the prim's existing transform operations are incompatible
    if not (xform_api.SetTranslate(translation, time)
            and xform_api.SetRotate(rotation, UsdGeom.XformCommonAPI.RotationOrderXYZ, time)
            and xform_api.SetScale(scale, time)):
        raise ValueError(f"Cannot set the transforms of {prim.GetPath()} with UsdGeom.XformCommonAPI")


#############
# Full Usage
#############

from pxr import Gf, Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, Sdf.Path("/World/Cube"))
set_transforms(cube.GetPrim(), translation=(10, 0, 0), rotation=(0, 45, 0), scale=(2, 2, 2))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check the authored values and the resulting local transform
translation, rotation, scale, _, _ = UsdGeom.XformCommonAPI(cube).GetXformVectors(Usd.TimeCode.Default())
assert translation == Gf.Vec3d(10, 0, 0)
assert rotation == Gf.Vec3f(0, 45, 0)
assert scale == Gf.Vec3f(2, 2, 2)
assert Gf.IsClose(cube.GetLocalTransformation().ExtractTranslation(), Gf.Vec3d(10, 0, 0), 1e-6)

# Setting the transforms again updates the same operations instead of adding new ones
set_transforms(cube.GetPrim(), translation=(20, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))
assert [op.GetOpName() for op in cube.GetOrderedXformOps()] == ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
assert UsdGeom.XformCommonAPI(cube).GetXformVectors(Usd.TimeCode.Default())[0] == Gf.Vec3d(20, 0, 0)

# Pass time codes to animate the transforms; values between time samples are interpolated
set_transforms(cube.GetPrim(), translation=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), time=Usd.TimeCode(0))
set_transforms(cube.GetPrim(), translation=(0, 10, 0), rotation=(0, 90, 0), scale=(1, 1, 1), time=Usd.TimeCode(10))
assert Gf.IsClose(cube.GetLocalTransformation(Usd.TimeCode(5)).ExtractTranslation(), Gf.Vec3d(0, 5, 0), 1e-6)

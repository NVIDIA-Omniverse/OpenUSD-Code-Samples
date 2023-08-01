# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, Usd, UsdGeom

def create_orthographic_camera(stage: Usd.Stage, prim_path: str="/World/MyOrthoCam"):
    """Create an orthographic camera

    Args:
        stage (Usd.Stage): A USD Stage to create the camera on.
        prim_path (str, optional): The prim path for where to create the camera. Defaults to "/World/MyOrthoCam".
    """
    camera_path = Sdf.Path(prim_path)
    usd_camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.orthographic)



#############
# Full Usage
#############
cam_path = "/World/MyOrthoCam"
stage: Usd.Stage = Usd.Stage.CreateInMemory()
root_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(root_prim.GetPrim())

create_orthographic_camera(stage, cam_path)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the camera was created
prim = stage.GetPrimAtPath(cam_path)
assert prim.IsValid()
assert prim.GetPath() == Sdf.Path(cam_path)
assert prim.GetTypeName() == "Camera"
projection = prim.GetProjectionAttr().Get()
assert projection == UsdGeom.Tokens.orthographic

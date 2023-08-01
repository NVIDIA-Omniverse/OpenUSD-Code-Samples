# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import UsdGeom


def create_perspective_camera(prim_path: str="/World/MyPerspCam"):
    """Create a perspective camera

    Args:
        prim_path (str, optional): The prim path where the camera should be created. Defaults to "/World/MyPerspCam".
    """

    omni.kit.commands.execute("CreatePrimWithDefaultXform",
       prim_type="Camera",
       prim_path=prim_path,
       attributes={
           "projection": UsdGeom.Tokens.perspective,
           "focalLength": 35,
           "horizontalAperture": 20.955,
           "verticalAperture": 15.2908,
           "clippingRange": (0.1, 100000)
       }
    )


#############    
# Full Usage
#############
import omni.usd


# Create a perspective camera at /World/MyPerspCam
path = "/World/MyPerspCam"
create_perspective_camera(path)

# Check that the camera was created
stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath(path)
assert prim.IsValid() == True
assert prim.GetTypeName() == "Camera"
projection = prim.GetAttribute("projection").Get()
assert projection == UsdGeom.Tokens.perspective
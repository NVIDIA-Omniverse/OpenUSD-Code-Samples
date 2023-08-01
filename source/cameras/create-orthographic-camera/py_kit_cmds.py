# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import UsdGeom


def create_orthographic_camera(prim_path: str="/World/MyOrthoCam"):
    """Create an orthographic camera

    Args:
        prim_path (str, optional): The prim path where the camera should be created. Defaults to "/World/MyOrthoCam".
    """

    omni.kit.commands.execute("CreatePrimWithDefaultXform",
       prim_type="Camera",
       prim_path="/World/MyOrthoCam",
       attributes={"projection": UsdGeom.Tokens.orthographic}
    )


#############    
# Full Usage
#############
import omni.usd

# Create an orthographic camera at /World/MyOrthoCam
path = "/World/MyOrthoCam"
create_orthographic_camera(path)

# Check that the camera was created
stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath(path)
assert prim.IsValid() == True
assert prim.GetTypeName() == "Camera"
projection = prim.GetAttribute("projection").Get()
assert projection == UsdGeom.Tokens.orthographic
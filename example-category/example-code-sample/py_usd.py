# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Add all the imports that you need for you snippets
from pxr import Usd, Sdf, UsdGeom


def descriptive_code_sample_name(stage: Usd.Stage, prim_path: str="/World/MyPerspCam") -> UsdGeom.Camera:
    """Docstring is optional. Use Google style docstrings if you choose to add them.

    The code sample should be defined as a function. As a descriptive name for the function.
    Use function arguments to:
        - Pass in any objects that your code sample expects to exist (e.g. a Stage)
        - Pass in Paths rather than hard-coding them.

    Use type-hinting to help learners understand what type every variable is. Don't assume they'll know.

    Args:
        stage (Usd.Stage): _description_
        prim_path (str, optional): _description_. Defaults to "/World/MyPerspCam".

    Returns:
        UsdGeom.Camera: _description_
    """
    camera_path = Sdf.Path(prim_path)
    usd_camera: UsdGeom.Camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)
    return usd_camera


#############
# Full Usage
#############
# Here you will show your code sample in context. Add any additional imports
# that you may need for your "Full Usage" code

# You can create an in-memory stage and do any stage setup before calling
# you code sample.
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())
cam_path = default_prim.GetPath().AppendPath("MyPerspCam")

# Call your code sample function
camera = descriptive_code_sample_name(stage, cam_path)

# print out the result
usda = stage.GetRootLayer().ExportToString()
print(usda)

# Do some basic asserts to show learners how to interact with the results.
prim = camera.GetPrim()
assert prim.IsValid()
assert camera.GetPath() == Sdf.Path(cam_path)
assert prim.GetTypeName() == "Camera"
projection = camera.GetProjectionAttr().Get()
assert projection == UsdGeom.Tokens.perspective

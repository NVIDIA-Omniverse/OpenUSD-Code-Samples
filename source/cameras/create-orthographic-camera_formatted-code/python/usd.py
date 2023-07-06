"""
This is the module docstring that you can use for more info about this sample flavor.
"""

"""
Hi thisdfasdf
adsfkadsflksfd 
"""

import pxr
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

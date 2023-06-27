"""
The `CreatePrimWithDefaultXform` command in Kit can create a Camera prim and you can optionally set camera attributes values during creation. You must use the attribute token names as the keys for the `attributes` dictionary. In Omniverse applications, you can explore the names by hovering over a property label in the Property Window and reading it from the tooltip.
"""

import omni.kit.commands
from pxr import UsdGeom


def create_ortho_camera(prim_path: str="/World/MyOrthoCam"):
    """Create an orthographic camera

    Args:
        prim_path (str, optional): The prim path where the camera should be created. Defaults to "/World/MyOrthoCam".
    """
    omni.kit.commands.execute("CreatePrimWithDefaultXform",
        prim_type="Camera",
        prim_path=prim_path,
        attributes={"projection": UsdGeom.Tokens.orthographic}
    )

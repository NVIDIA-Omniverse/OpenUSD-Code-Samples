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

# Full Usage
import omni.usd

path = "/World/MyOrthoCam"
create_ortho_camera(path)

# Check that the camera was created
stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath(path)
assert(prim.IsValid())
# TODO: Assert Type
# TODO: Assert Projection Attr value
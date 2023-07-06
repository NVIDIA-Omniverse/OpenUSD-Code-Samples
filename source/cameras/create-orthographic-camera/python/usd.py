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

# Full Usage
path = "/World/MyOrthoCam"
stage = Usd.Stage.CreateNew('HelloWorld.usda')
create_orthographic_camera(stage, path)
# TODO: should we save the stage?
stage.GetRootLayer().Save()

# Check that the camera was created
prim = stage.GetPrimAtPath(path)
assert(prim.IsValid())
# TODO: Assert Type
# TODO: Assert Projection Attr value

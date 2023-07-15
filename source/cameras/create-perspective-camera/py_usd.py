from pxr import Usd, Sdf, UsdGeom

def create_perspective_camera(stage: Usd.Stage) -> UsdGeom.Camera:
    camera_path = Sdf.Path("/World/MyPerspCam")
    usd_camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)
    return usd_camera
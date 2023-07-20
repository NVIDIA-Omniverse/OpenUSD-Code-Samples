from pxr import Usd, Sdf, UsdGeom

def create_perspective_35mm_camera(stage: Usd.Stage, prim_path: str="/World/MyPerspCam") -> UsdGeom.Camera:
    camera_path = Sdf.Path(prim_path)
    usd_camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)
    usd_camera.CreateFocalLengthAttr().Set(35)
    # Set a few other common attributes too.
    usd_camera.CreateHorizontalApertureAttr().Set(20.955)
    usd_camera.CreateVerticalApertureAttr().Set(15.2908)
    usd_camera.CreateClippingRangeAttr().Set((0.1,100000))
    return usd_camera


#############
# Full Usage
#############
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

cam_path = default_prim.GetPath().AppendPath("MyPerspCam")
camera = create_perspective_35mm_camera(stage, cam_path)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check the camera attributes
focal_len = camera.GetFocalLengthAttr().Get()
assert focal_len == 35.0
clip_range = camera.GetClippingRangeAttr().Get()
assert clip_range == (0.1,100000)



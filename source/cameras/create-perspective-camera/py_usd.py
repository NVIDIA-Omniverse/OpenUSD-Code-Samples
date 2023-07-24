from pxr import Usd, Sdf, UsdGeom

def create_perspective_camera(stage: Usd.Stage, prim_path: str="/World/MyPerspCam") -> UsdGeom.Camera:
    camera_path = Sdf.Path(prim_path)
    usd_camera: UsdGeom.Camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)
    return usd_camera


#############
# Full Usage
#############

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create the perspective camera at /World/MyPerspCam
cam_path = default_prim.GetPath().AppendPath("MyPerspCam")
camera = create_perspective_camera(stage, cam_path)

# Export the complete Stage as a string and print it.
usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the camera was created
prim = camera.GetPrim()
assert prim.IsValid()
assert camera.GetPath() == Sdf.Path(cam_path)
assert prim.GetTypeName() == "Camera"
projection = camera.GetProjectionAttr().Get()
assert projection == UsdGeom.Tokens.perspective

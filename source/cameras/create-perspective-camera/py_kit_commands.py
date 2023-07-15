import omni.kit.commands
from pxr import UsdGeom

omni.kit.commands.execute("CreatePrimWithDefaultXform",
   prim_type="Camera",
   prim_path="/World/MyPerspCam",
   attributes={
      "projection": UsdGeom.Tokens.perspective,
      "focalLength": 35,
      "horizontalAperture": 20.955,
      "verticalAperture": 15.2908,
      "clippingRange": (0.1, 100000)
   }
)
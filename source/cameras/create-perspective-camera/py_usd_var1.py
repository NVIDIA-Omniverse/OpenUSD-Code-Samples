from pxr import Sdf, UsdGeom

usd_camera.CreateFocalLengthAttr().Set(35)
usd_camera.CreateHorizontalApertureAttr().Set(20.955)
usd_camera.CreateVerticalApertureAttr().Set(15.2908)
usd_camera.CreateClippingRangeAttr().Set((0.1,100000))
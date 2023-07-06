```python
from pxr import Sdf, UsdGeom

camera_path = Sdf.Path("/World/MyOrthoCam")
usd_camera = UsdGeom.Camera.Define(stage, camera_path)
usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.orthographic)
```
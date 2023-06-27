# USD API
```python
from pxr import Sdf, UsdGeom

camera_path = Sdf.Path("/World/MyOrthoCam")
usd_camera = UsdGeom.Camera.Define(stage, camera_path)
usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.orthographic)
```

# Omniverse Kit Commands
The `CreatePrimWithDefaultXform` command in Kit can create a Camera prim and you can optionally set camera attributes values during creation. You must use the attribute token names as the keys for the `attributes` dictionary. In Omniverse applications, you can explore the names by hovering over a property label in the Property Window and reading it from the tooltip.

```python
import omni.kit.commands
from pxr import UsdGeom

omni.kit.commands.execute("CreatePrimWithDefaultXform",
    prim_type="Camera",
    prim_path="/World/MyOrthoCam",
    attributes={"projection": UsdGeom.Tokens.orthographic}
)
```
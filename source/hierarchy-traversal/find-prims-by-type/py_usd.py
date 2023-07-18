from pxr import UsdGeom

# e.g., find all prims of type UsdGeom.Mesh
mesh_prims = [x for x in stage.Traverse() if x.IsA(UsdGeom.Mesh)]
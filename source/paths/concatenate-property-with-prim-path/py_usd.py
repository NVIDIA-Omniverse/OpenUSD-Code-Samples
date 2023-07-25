# e.g., get path to "points" attribute on a mesh prim
from pxr import UsdGeom, Sdf

points_attr_path = mesh_prim_path.AppendProperty(UsdGeom.Tokens.points)

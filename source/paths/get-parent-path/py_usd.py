from pxr import Sdf

parent_path = my_prim_path.GetParentPath()

# Given Sdf.Path('/World/Cone') for my_prim_path, parent_path will contain Sdf.Path('/World')


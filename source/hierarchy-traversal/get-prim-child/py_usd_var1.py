from pxr import Usd, UsdGeom

def get_first_child_mesh(parent_prim: Usd.Prim) -> Usd.Prim:
    # Iterates only active, loaded, defined, non-abstract children
    for child_prim in parent_prim.GetChildren():
        if child_prim.IsA(UsdGeom.Mesh):
            return child_prim

def print_all_children_names(parent_prim: Usd.Prim):
    # Iterates over all children
    for child_prim in parent_prim.GetAllChildren():
        print(child_prim.GetName())
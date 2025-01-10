# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Usd

def find_prims_by_attribute(parent_prim: Usd.Prim, attr_name: str) -> List[Usd.Prim]:
    found_prims = [x for x in parent_prim.GetAllChildren() if x.GetAttribute(attr_name).IsValid()]
    return found_prims


##############
# Full Usage
##############

from pxr import UsdGeom, Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create some shape prims
xform_parent = stage.DefinePrim('/xform', 'Xform')
cone_child = stage.DefinePrim('/xform/cone', 'Cone') # Has a radius attribute
cube_child = stage.DefinePrim('/xform/cube', 'Cube')
sphere_child = stage.DefinePrim('/xform/sphere', 'Sphere') # Has a radius attribute

# Find all the prims under the given parent prim with the attribute "radius"
prims: List[Usd.Prim] = find_prims_by_attribute(xform_parent, "radius")

# Print the prims to check that only the prims with radius attribute are printed
print(prims)

# Check the number of prims found and whether the found data is correct
assert len(prims) == 2
assert isinstance(prims[0], Usd.Prim)
assert prims[0].GetAttribute("radius").IsValid()
assert prims[0].GetTypeName() == "Cone"
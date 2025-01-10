# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def add_inherit(stage: Usd.Stage, prim: Usd.Prim, class_prim: Usd.Prim):
    inherits: Usd.Inherits = prim.GetInherits()
    inherits.AddInherit(class_prim.GetPath())

#############
# Full Usage
#############

from pxr import Sdf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# The base prim typically uses the "class" Specifier to designate that it
# is meant to be inherited and skipped in standard stage traversals
tree_class: Usd.Prim = stage.CreateClassPrim("/_class_Tree")
tree_prim: Usd.Prim = UsdGeom.Mesh.Define(stage, default_prim.GetPath().AppendPath("TreeA")).GetPrim()

add_inherit(stage, tree_prim, tree_class)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check to see if the inherit was added
inherits_list = tree_prim.GetInherits().GetAllDirectInherits()
assert tree_class.GetPath() in inherits_list
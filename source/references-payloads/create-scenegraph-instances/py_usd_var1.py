# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List
from pxr import Sdf, Usd, UsdGeom

def create_internal_instances(stage: Usd.Stage, source_path: Sdf.Path, instance_paths: List[Sdf.Path]) -> List[Usd.Prim]:
    instances: List[Usd.Prim] = []
    for path in instance_paths:
        prim: Usd.Prim = UsdGeom.Xform.Define(stage, path).GetPrim()
        prim.GetReferences().AddInternalReference(source_path)
        prim.SetInstanceable(True)
        instances.append(prim)
    return instances


#############
# Full Usage
#############

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
stage.SetDefaultPrim(UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim())

# A tree that is already in the scene
UsdGeom.Xform.Define(stage, Sdf.Path("/World/Tree"))
UsdGeom.Cylinder.Define(stage, Sdf.Path("/World/Tree/Trunk"))
UsdGeom.Cone.Define(stage, Sdf.Path("/World/Tree/Leaves"))

# Repeat it as a row of instances
paths: List[Sdf.Path] = [Sdf.Path(f"/World/Forest/Tree_{i:02d}") for i in range(3)]
trees: List[Usd.Prim] = create_internal_instances(stage, Sdf.Path("/World/Tree"), paths)
for i, tree in enumerate(trees):
    UsdGeom.Xformable(tree).AddTranslateOp().Set((i * 5, 0, 0))

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Every repeat shares one prototype; the original tree is not an instance
assert all(tree.GetPrototype() == trees[0].GetPrototype() for tree in trees)
assert not stage.GetPrimAtPath("/World/Tree").IsInstance()
assert stage.GetPrimAtPath("/World/Forest/Tree_02/Leaves").IsInstanceProxy()

# Changes to the source tree show up in every instance
UsdGeom.Cone(stage.GetPrimAtPath("/World/Tree/Leaves")).GetHeightAttr().Set(3.0)
assert stage.GetPrimAtPath("/World/Forest/Tree_01/Leaves").GetAttribute("height").Get() == 3.0

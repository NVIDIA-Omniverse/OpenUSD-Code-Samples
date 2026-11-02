# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, Usd, UsdGeom

def get_world_position_cached(cache: UsdGeom.XformCache, prim: Usd.Prim) -> Gf.Vec3d:
    """
    Get the world space position of a prim's origin using a UsdGeom.XformCache.
    See https://openusd.org/release/api/class_usd_geom_xform_cache.html
    Args:
        cache: A cache, created for example as `UsdGeom.XformCache(Usd.TimeCode.Default())`.
        prim: The prim to get the world position of.
    Returns:
        The position of the prim's origin in world space.
    """
    world_transform: Gf.Matrix4d = cache.GetLocalToWorldTransform(prim)
    return world_transform.ExtractTranslation()


#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A row of Cubes under one translated parent
row: UsdGeom.Xform = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("Row"))
row.AddTranslateOp().Set(value=(0, 0, 50))
for i in range(5):
    cube = UsdGeom.Cube.Define(stage, row.GetPath().AppendPath(f"Cube_{i}"))
    cube.AddTranslateOp().Set(value=(i * 10, 0, 0))

# One cache answers every query, reusing the parent's transform
cache = UsdGeom.XformCache(Usd.TimeCode.Default())
positions = {prim.GetName(): get_world_position_cached(cache, prim) for prim in row.GetPrim().GetChildren()}
print(positions)

for i in range(5):
    assert Gf.IsClose(positions[f"Cube_{i}"], Gf.Vec3d(i * 10, 0, 50), 1e-6)

# The cache does not track edits; clear it (or create a new one) after changing transforms
row.GetPrim().GetAttribute("xformOp:translate").Set(Gf.Vec3d(0, 0, 100))
cache.Clear()
assert Gf.IsClose(get_world_position_cached(cache, stage.GetPrimAtPath("/World/Row/Cube_0")), Gf.Vec3d(0, 0, 100), 1e-6)

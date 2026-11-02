# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Gf, Usd, UsdGeom

def get_world_bounds_center(prim: Usd.Prim, time: Usd.TimeCode = Usd.TimeCode.Default()) -> Gf.Vec3d:
    """
    Get the world space center of a prim's geometry, rather than the position of its origin.
    See https://openusd.org/release/api/class_usd_geom_b_box_cache.html
    Args:
        prim: The prim to get the world space center of.
        time: The time at which to compute the bounds, for animated prims.
    Returns:
        The centroid of the prim's world space bounds.
    """
    cache = UsdGeom.BBoxCache(time, [UsdGeom.Tokens.default_])
    world_bound: Gf.BBox3d = cache.ComputeWorldBound(prim)
    return world_bound.ComputeCentroid()


#############
# Full Usage
#############

from pxr import Sdf

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A house that is moved away from the world origin
house: UsdGeom.Xform = UsdGeom.Xform.Define(stage, default_prim.GetPath().AppendPath("House"))
house.AddTranslateOp().Set(value=(0, 0, 5))

# A 2x2 quad whose origin is at one corner instead of its center, like a door hinged at its edge
door: UsdGeom.Mesh = UsdGeom.Mesh.Define(stage, house.GetPath().AppendPath("Door"))
door.CreatePointsAttr([(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)])
door.CreateFaceVertexCountsAttr([4])
door.CreateFaceVertexIndicesAttr([0, 1, 2, 3])
door.CreateExtentAttr(UsdGeom.PointBased.ComputeExtent(door.GetPointsAttr().Get()))
door.AddTranslateOp().Set(value=(10, 0, 0))

origin: Gf.Vec3d = UsdGeom.Xformable(door).ComputeLocalToWorldTransform(Usd.TimeCode.Default()).ExtractTranslation()
center: Gf.Vec3d = get_world_bounds_center(door.GetPrim())
print(origin, center)

# The origin is the hinge corner, while the center is in the middle of the geometry
assert Gf.IsClose(origin, Gf.Vec3d(10, 0, 5), 1e-6)
assert Gf.IsClose(center, Gf.Vec3d(11, 1, 5), 1e-6)

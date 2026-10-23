# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom


def get_prim_visibility(
    prim: Usd.Prim, time: Usd.TimeCode = Usd.TimeCode.Default()
) -> str:
    """Compute general visibility, including opinions on imageable ancestors.

    Args:
        prim: A valid prim that supports UsdGeom.Imageable.
        time: The time at which to compute visibility.

    Returns:
        UsdGeom.Tokens.invisible if the prim or an ancestor is invisible;
        otherwise, UsdGeom.Tokens.inherited.

    Raises:
        ValueError: If the prim is invalid or does not support Imageable.
    """
    imageable = UsdGeom.Imageable(prim)
    if not imageable:
        raise ValueError("The prim must be a valid UsdGeom.Imageable.")
    return imageable.ComputeVisibility(time)


#############
# Full Usage
#############

stage = Usd.Stage.CreateInMemory()
world = UsdGeom.Xform.Define(stage, "/World")
stage.SetDefaultPrim(world.GetPrim())
UsdGeom.Xform.Define(stage, "/World/Group")
cube = UsdGeom.Cube.Define(stage, "/World/Group/Cube")
cube_prim = cube.GetPrim()

# With no invisible opinions, the computed visibility is inherited.
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.inherited

# Hide an ancestor. The cube's own attribute is still inherited, but its
# computed visibility is invisible, even through the intermediate Group.
world.CreateVisibilityAttr().Set(UsdGeom.Tokens.invisible)
assert cube.GetVisibilityAttr().Get() == UsdGeom.Tokens.inherited
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.invisible

# Setting inherited on the cube does not override its invisible ancestor.
cube.CreateVisibilityAttr().Set(UsdGeom.Tokens.inherited)
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.invisible

# Restoring inherited visibility on the ancestor allows the cube to be visible.
world.GetVisibilityAttr().Set(UsdGeom.Tokens.inherited)
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.inherited

# A prim's own invisible opinion also hides it.
cube.GetVisibilityAttr().Set(UsdGeom.Tokens.invisible)
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.invisible
cube.GetVisibilityAttr().Set(UsdGeom.Tokens.inherited)

# Animated ancestor visibility must be evaluated at the requested time.
world.GetVisibilityAttr().Set(UsdGeom.Tokens.invisible, Usd.TimeCode(1))
world.GetVisibilityAttr().Set(UsdGeom.Tokens.inherited, Usd.TimeCode(2))
assert get_prim_visibility(cube_prim, Usd.TimeCode(1)) == UsdGeom.Tokens.invisible
assert get_prim_visibility(cube_prim, Usd.TimeCode(2)) == UsdGeom.Tokens.inherited
assert get_prim_visibility(cube_prim) == UsdGeom.Tokens.inherited

print(stage.GetRootLayer().ExportToString())

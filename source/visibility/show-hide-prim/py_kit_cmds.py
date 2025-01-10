# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
import omni.usd
from pxr import Sdf


def hide_prim(prim_path: str):
    """Hide a prim

    Args:
        prim_path (str, required): The prim path of the prim to hide
    """
    set_prim_visibility_attribute(prim_path, "invisible")


def show_prim(prim_path: str):
    """Show a prim

    Args:
        prim_path (str, required): The prim path of the prim to show
    """
    set_prim_visibility_attribute(prim_path, "inherited")


def set_prim_visibility_attribute(prim_path: str, value: str):
    """Set the prim visibility attribute at prim_path to value

    Args:
        prim_path (str, required): The path of the prim to modify
        value (str, required): The value of the visibility attribute
    """
    # You can reference attributes using the path syntax by appending the
    # attribute name with a leading `.`
    prop_path = f"{prim_path}.visibility"
    omni.kit.commands.execute(
        "ChangeProperty", prop_path=Sdf.Path(prop_path), value=value, prev=None
    )


"""
Full Usage
"""

# Path to a prim in the open stage
prim_path = "/World/Cube"
stage = omni.usd.get_context().get_stage()
prim = stage.GetPrimAtPath(prim_path)
assert prim.IsValid()

# Manually confirm that the prim is not visible in the viewport after calling
# hide_prim. You should comment out the below show_prim call and assert.
hide_prim(prim_path)
assert prim.GetAttribute("visibility").Get() == "invisible"

# Manually confirm that the prim is visible in the viewport after calling 
# show_prim
show_prim(prim_path)
assert prim.GetAttribute("visibility").Get() == "inherited"

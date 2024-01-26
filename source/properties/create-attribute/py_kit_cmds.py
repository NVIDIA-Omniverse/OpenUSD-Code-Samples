# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
import omni.usd

from pxr import Gf, Sdf, Usd, UsdGeom


def create_float_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
    """Creates attribute for a prim that holds a float.
    See: https://openusd.org/release/api/class_usd_prim.html
    See: https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd.commands/omni.usd.commands.CreateUsdAttributeCommand.html
    Args:
        prim (Usd.Prim): A Prim for holding the attribute.
        attribute_name (str): The name of the attribute to create.
    Returns:
        Usd.Attribute: An attribute created at specific prim.
    """
    omni.kit.commands.execute(
        "CreateUsdAttributeCommand",
        prim=prim,
        attr_name=attribute_name,
        attr_type=Sdf.ValueTypeNames.Float,
    )

    attr: Usd.Attribute = prim.GetAttribute(attribute_name)
    return attr


def create_vector_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
    """Creates attribute for a prim that holds a vector.
    See: https://openusd.org/release/api/class_usd_prim.html
    See: https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd.commands/omni.usd.commands.CreateUsdAttributeCommand.html
    Args:
        prim (Usd.Prim): A Prim for holding the attribute.
        attribute_name (str): The name of the attribute to create.
    Returns:
        Usd.Attribute: An attribute created at specific prim.
    """
    omni.kit.commands.execute(
        "CreateUsdAttributeCommand",
        prim=prim,
        attr_name=attribute_name,
        attr_type=Sdf.ValueTypeNames.Float3,
    )
    attr: Usd.Attribute = prim.GetAttribute(attribute_name)
    return attr


#############
# Full Usage
#############

# Get the current stage
stage: Usd.Stage = omni.usd.get_context().get_stage()

# Get the default prim
prim: Usd.Prim = stage.GetDefaultPrim()

# Create a float attribute on /World
float_attr: Usd.Attribute = create_float_attribute(prim, "my_float_attr")

# Create a vector attribute on /World
vector_attr: Usd.Attribute = create_vector_attribute(prim, "my_vector_attr")

# Set and query values
print(float_attr.Get())
float_attr.Set(0.1)
print(float_attr.Get())

vector_value: Gf.Vec3f = Gf.Vec3f(0.1, 0.2, 0.3)
print(vector_attr.Get())
vector_attr.Set(vector_value)
print(vector_attr.Get())

# Optionally preview the usd
# print(stage.GetRootLayer().ExportToString())

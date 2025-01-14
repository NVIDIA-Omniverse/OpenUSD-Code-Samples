# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, Sdf

def get_attribute_value_at_time(prim: Usd.Prim, attribute_name: str, time_value: float):
    """
    See: https://openusd.org/release/api/class_usd_attribute.html
    Args:
        prim: The prim owner of the attribute.
        attribute_name: The name of the attribute to retrieve.
        time_value: Get the value authored or interpolated at a particular time.
    Return:
        The value of the attribute, see https://openusd.org/release/api/_usd__page__datatypes.html
        for the return types.
        For example, for `float3`, the return type will be `Gf.Vec3f`.
    """
    attr = prim.GetAttribute(attribute_name)
    return attr.Get(time_value)
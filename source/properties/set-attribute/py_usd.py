# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, Sdf, Gf

def set_float_attribute(attr: Usd.Attribute, value: float) -> None:
    """
    See: https://graphics.pixar.com/usd/release/api/class_usd_attribute.html
    Args:
        attr: The attribute to set.
        value: A floating point value, i.e. `3.141516`.
    """
    attr.Set(value)

def set_vector_attribute(attr: Usd.Attribute, value: Gf.Vec3f) -> None:
    """
    Args:
        attr: The attribute to set.
        value: A floating point vector, i.e. `(1., 2., 3.)`.
    """
    attr.Set(value)
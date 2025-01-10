# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

pts_attr: Usd.Attribute = mesh_prim.GetAttribute("points")
if pts_attr:
    print("Attribute exists!")
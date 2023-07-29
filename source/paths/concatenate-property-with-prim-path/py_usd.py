# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# e.g., get path to "points" attribute on a mesh prim
from pxr import UsdGeom, Sdf

points_attr_path = mesh_prim_path.AppendProperty(UsdGeom.Tokens.points)

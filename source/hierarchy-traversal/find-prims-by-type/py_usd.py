# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import UsdGeom

# e.g., find all prims of type UsdGeom.Mesh
mesh_prims = [x for x in stage.Traverse() if x.IsA(UsdGeom.Mesh)]
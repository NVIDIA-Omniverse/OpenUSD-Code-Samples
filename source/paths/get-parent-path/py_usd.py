# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf

parent_path = my_prim_path.GetParentPath()

# Given Sdf.Path('/World/Cone') for my_prim_path, parent_path will contain Sdf.Path('/World')


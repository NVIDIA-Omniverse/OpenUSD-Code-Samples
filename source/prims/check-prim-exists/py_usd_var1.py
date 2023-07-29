# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, Usd

prim_path = Sdf.Path("/World/Hello")
prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
if prim:
    print("Prim exists!")
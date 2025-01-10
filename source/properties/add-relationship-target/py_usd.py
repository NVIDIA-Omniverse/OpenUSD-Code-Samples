# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom

# For example, adding a proxy prim target on an Imageable
proxy_prim_rel: Usd.Relationship = UsdGeom.Imageable(myprim).GetProxyPrimRel()
proxy_prim_rel.AddTarget("/World/MyProxy")

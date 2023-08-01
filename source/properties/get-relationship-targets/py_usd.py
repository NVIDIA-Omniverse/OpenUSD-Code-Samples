# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd, UsdGeom

# For example, getting the proxy prim on an Imageable
proxy_prim_rel: Usd.Relationship = UsdGeom.Imageable(myprim).GetProxyPrimRel()
proxyPrimTargets = proxy_prim_rel.GetForwardedTargets()
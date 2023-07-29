# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

prim: Usd.Prim = stage.GetPrimAtPath("/World/my/prim")
base: Usd.Prim = stage.GetPrimAtPath("/World/my/base")
specializes: Usd.Specializes = prim.GetSpecializes()
specializes.AddSpecialize(base.GetPath())
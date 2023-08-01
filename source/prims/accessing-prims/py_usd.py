# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

usd_context = omni.usd.get_context()
stage = usd_context.get_stage()
my_prim_path = "/World/building/window/"
my_prim = stage.GetPrimAtPath(my_prim_path)
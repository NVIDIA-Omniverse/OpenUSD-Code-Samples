# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.usd

prim_path = "/World/My/Prim"
ctx = omni.usd.get_context()
# The second arg is unused. Any boolean can be used.
ctx.get_selection().set_selected_prim_paths([prim_path], True)
# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.usd

prim_path = "/World/My/Prim"
ctx = omni.usd.get_context()
# returns a list of prim path strings
selection = ctx.get_selection().get_selected_prim_paths()
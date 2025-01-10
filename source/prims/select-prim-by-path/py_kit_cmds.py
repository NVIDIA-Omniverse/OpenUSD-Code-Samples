# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
import omni.usd

prim_path = "/World/My/Prim"
ctx = omni.usd.get_context()
old_selection = ctx.get_selection().get_selected_prim_paths()

omni.kit.commands.execute('SelectPrimsCommand',
    old_selected_paths=old_selection,
    new_selected_paths=[prim_path],
    expand_in_stage=True) #DEPRECATED: Used only for backwards compatibility.
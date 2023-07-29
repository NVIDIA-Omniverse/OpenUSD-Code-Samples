# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands

omni.kit.commands.execute("CreatePreviewSurfaceMaterialPrim",
    mtl_path="/World/Looks/PreviewSurface",
    select_new_prim=True)


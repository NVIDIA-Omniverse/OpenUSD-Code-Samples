# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands

success, result = omni.kit.commands.execute('CreateMdlMaterialPrimCommand',
    mtl_url='OmniPBR.mdl', # This can be path to local or remote MDL
    mtl_name='OmniPBR', # sourceAsset:subIdentifier (i.e. the name of the material within the MDL)
    mtl_path="/World/Looks/OmniPBR" # Prim path for the Material to create.
)

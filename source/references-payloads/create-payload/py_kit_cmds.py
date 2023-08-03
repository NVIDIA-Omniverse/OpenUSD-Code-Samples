# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
import omni.usd
from pxr import Usd, Sdf

def create_payload(usd_context: omni.usd.UsdContext, path_to: Sdf.Path, asset_path: str, prim_path: Sdf.Path) -> Usd.Prim:
    omni.kit.commands.execute("CreatePayload",
        usd_context=usd_context,
        path_to=path_to, # Prim path for where to create the prim with the payload
        asset_path=asset_path, # The file path to the payload USD. Relative paths are accepted too.
        prim_path=prim_path # OPTIONAL: Prim path to a prim in the payloaded USD, if not provided the default prim is used
    )
    return usd_context.get_stage().GetPrimAtPath(path_to)


#############
# Full Usage
#############

# Get the USD context from kit
context: omni.usd.UsdContext = omni.usd.get_context()

# Create and add external payload to specific prim
payload_prim: Usd.Prim = create_payload(context, Sdf.Path("/World/payload_prim"), "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Get the existing USD stage from kit
stage: Usd.Stage = context.get_stage()
usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the payload prims were created
assert payload_prim.IsValid()

assert payload_prim.GetPrimStack()[0].payloadList.prependedItems[0] == Sdf.Payload(assetPath="file:/C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from pxr import Usd, Sdf

def add_payload(prim: Usd.Prim, payload_asset_path: str, payload_target_path: Optional[Sdf.Path] = None) -> None:
    payloads: Usd.Payloads = prim.GetPayloads()
    if payload_target_path is None:
        # Payload the payloaded layer's defaultPrim
        payloads.AddPayload(assetPath=payload_asset_path)
    else:
        # Payload a specific target prim
        payloads.AddPayload(assetPath=payload_asset_path, primPath=payload_target_path)


#############
# Full Usage
#############
from pxr import UsdGeom

# Create new USD stage for this sample
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Create and define default prim
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create an xform which should hold all payloads in this sample
payload_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/payload_prim")).GetPrim()

# Add an external payload
add_payload(payload_prim, "C:/path/to/file.usd", payload_target_path=Sdf.Path("/World/some/target"))

# Add other external payload to default prim
add_payload(payload_prim, "C:/path/to/other/file.usd")

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Get a list of all prepended payloads
payloads = []
for prim_spec in payload_prim.GetPrimStack():
    payloads.extend(prim_spec.payloadList.prependedItems)

# Check that the payload prim was created and that the payloads are correct
assert payload_prim.IsValid()
assert payloads[0] == Sdf.Payload(assetPath="C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
assert payloads[1] == Sdf.Payload(assetPath="C:/path/to/other/file.usd")

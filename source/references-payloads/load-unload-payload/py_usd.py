# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def load_payload(prim: Usd.Prim) -> None:
    # Loads the prim's Payload and any Payloads nested inside it
    prim.Load()

def unload_payload(prim: Usd.Prim) -> None:
    # Unloads the prim's Payload and any Payloads nested inside it
    prim.Unload()


#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create an asset to use as a Payload. In practice this would be a file such as "./assets/building.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
building: Usd.Prim = UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Building")).GetPrim()
asset_stage.SetDefaultPrim(building)
UsdGeom.Cube.Define(asset_stage, Sdf.Path("/Building/Walls"))

# Create a Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# Add the asset as a Payload. Stages load Payloads by default.
payload_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Building")).GetPrim()
payload_prim.GetPayloads().AddPayload(asset_stage.GetRootLayer().identifier)
assert payload_prim.IsLoaded()
assert stage.GetPrimAtPath("/World/Building/Walls").IsValid()

authored_before = stage.GetRootLayer().ExportToString()
unload_payload(payload_prim)
print(stage.ExportToString())

# Unloading is Stage state; nothing was authored in the layer
assert stage.GetRootLayer().ExportToString() == authored_before

# The prim and its Payload arc remain, but nothing from the Payload is composed
assert payload_prim.IsValid() and payload_prim.HasAuthoredPayloads()
assert not payload_prim.IsLoaded()
assert not stage.GetPrimAtPath("/World/Building/Walls").IsValid()

load_payload(payload_prim)

# The Payload's contents are back on the Stage
assert payload_prim.IsLoaded()
assert stage.GetPrimAtPath("/World/Building/Walls").IsValid()

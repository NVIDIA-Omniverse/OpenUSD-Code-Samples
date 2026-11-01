# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def load_payload_only(prim: Usd.Prim) -> None:
    # Loads the prim's Payload, but leaves any Payloads nested inside it unloaded
    prim.Load(Usd.LoadWithoutDescendants)


#############
# Full Usage
#############
from pxr import Sdf, UsdGeom

# Create a furniture asset. In practice this would be a file such as "./assets/furniture.usd".
furniture_stage: Usd.Stage = Usd.Stage.CreateInMemory()
furniture: Usd.Prim = UsdGeom.Xform.Define(furniture_stage, Sdf.Path("/Furniture")).GetPrim()
furniture_stage.SetDefaultPrim(furniture)
UsdGeom.Cube.Define(furniture_stage, Sdf.Path("/Furniture/Chair"))

# Create a building asset whose furniture is a nested Payload. In practice: "./assets/building.usd".
building_stage: Usd.Stage = Usd.Stage.CreateInMemory()
building: Usd.Prim = UsdGeom.Xform.Define(building_stage, Sdf.Path("/Building")).GetPrim()
building_stage.SetDefaultPrim(building)
UsdGeom.Cube.Define(building_stage, Sdf.Path("/Building/Walls"))
nested: Usd.Prim = UsdGeom.Xform.Define(building_stage, Sdf.Path("/Building/Furniture")).GetPrim()
nested.GetPayloads().AddPayload(furniture_stage.GetRootLayer().identifier)

# Author a scene with the building as a Payload and open it with nothing loaded
scene_layer: Sdf.Layer = Sdf.Layer.CreateAnonymous(".usda")
scene_stage: Usd.Stage = Usd.Stage.Open(scene_layer)
scene_stage.SetDefaultPrim(UsdGeom.Xform.Define(scene_stage, Sdf.Path("/World")).GetPrim())
payload_prim: Usd.Prim = UsdGeom.Xform.Define(scene_stage, Sdf.Path("/World/Building")).GetPrim()
payload_prim.GetPayloads().AddPayload(building_stage.GetRootLayer().identifier)
stage: Usd.Stage = Usd.Stage.Open(scene_layer, Usd.Stage.LoadNone)

load_payload_only(stage.GetPrimAtPath("/World/Building"))
print(stage.ExportToString())

# The building's own contents are loaded, including the prim that holds the nested Payload...
assert stage.GetPrimAtPath("/World/Building").IsLoaded()
assert stage.GetPrimAtPath("/World/Building/Walls").IsValid()
# ...but the nested furniture Payload is not
assert not stage.GetPrimAtPath("/World/Building/Furniture").IsLoaded()
assert not stage.GetPrimAtPath("/World/Building/Furniture/Chair").IsValid()

# Loading with the default policy also loads the nested Payloads
stage.GetPrimAtPath("/World/Building").Load()
assert stage.GetPrimAtPath("/World/Building/Furniture/Chair").IsValid()

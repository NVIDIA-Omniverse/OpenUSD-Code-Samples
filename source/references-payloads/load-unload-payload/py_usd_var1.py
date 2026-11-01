# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import List, Sequence
from pxr import Sdf, Usd

def load_payloads(stage: Usd.Stage, paths_to_load: Sequence[Sdf.Path], paths_to_unload: Sequence[Sdf.Path] = ()) -> None:
    # Load and unload several Payloads in one call, which recomposes the Stage only once
    stage.LoadAndUnload(paths_to_load, paths_to_unload)


#############
# Full Usage
#############
from pxr import UsdGeom

# Create an asset to use as a Payload. In practice this would be a file such as "./assets/building.usd".
asset_stage: Usd.Stage = Usd.Stage.CreateInMemory()
building: Usd.Prim = UsdGeom.Xform.Define(asset_stage, Sdf.Path("/Building")).GetPrim()
asset_stage.SetDefaultPrim(building)
UsdGeom.Cube.Define(asset_stage, Sdf.Path("/Building/Walls"))

# Author a scene with three Payloads to the same asset
scene_layer: Sdf.Layer = Sdf.Layer.CreateAnonymous(".usda")
scene_stage: Usd.Stage = Usd.Stage.Open(scene_layer)
scene_stage.SetDefaultPrim(UsdGeom.Xform.Define(scene_stage, Sdf.Path("/World")).GetPrim())
for name in ("BuildingA", "BuildingB", "BuildingC"):
    prim = UsdGeom.Xform.Define(scene_stage, Sdf.Path("/World").AppendChild(name)).GetPrim()
    prim.GetPayloads().AddPayload(asset_stage.GetRootLayer().identifier)

# Open the scene with no Payloads loaded. In practice: Usd.Stage.Open("./scene.usd", Usd.Stage.LoadNone)
stage: Usd.Stage = Usd.Stage.Open(scene_layer, Usd.Stage.LoadNone)
assert stage.GetLoadSet() == []

# Find every prim that has a Payload, loaded or not
loadable: List[Sdf.Path] = stage.FindLoadable()
print(loadable)

# Load only the first two buildings
load_payloads(stage, loadable[:2])
print(stage.ExportToString())

assert stage.GetLoadSet() == [Sdf.Path("/World/BuildingA"), Sdf.Path("/World/BuildingB")]
assert stage.GetPrimAtPath("/World/BuildingA/Walls").IsValid()
assert not stage.GetPrimAtPath("/World/BuildingC/Walls").IsValid()

# Swap BuildingA for BuildingC in a single recomposition
load_payloads(stage, [Sdf.Path("/World/BuildingC")], [Sdf.Path("/World/BuildingA")])
assert stage.GetLoadSet() == [Sdf.Path("/World/BuildingB"), Sdf.Path("/World/BuildingC")]

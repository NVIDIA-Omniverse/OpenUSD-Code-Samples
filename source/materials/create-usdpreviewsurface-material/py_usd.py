# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, UsdShade

mtl_path = Sdf.Path("/World/Looks/PreviewSurface")
mtl = UsdShade.Material.Define(stage, mtl_path)
shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
shader.CreateIdAttr("UsdPreviewSurface")
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set([1.0, 0.0, 0.0])
shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.5)
shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)
mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
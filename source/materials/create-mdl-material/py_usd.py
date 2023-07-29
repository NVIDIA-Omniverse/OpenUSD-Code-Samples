# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf, UsdShade

mtl_path = Sdf.Path("/World/Looks/OmniPBR")
mtl = UsdShade.Material.Define(stage, mtl_path)
shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
shader.CreateImplementationSourceAttr(UsdShade.Tokens.sourceAsset)
# MDL shaders should use "mdl" sourceType
shader.SetSourceAsset("OmniPBR.mdl", "mdl")
shader.SetSourceAssetSubIdentifier("OmniPBR", "mdl")
# MDL materials should use "mdl" renderContext
mtl.CreateSurfaceOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
mtl.CreateDisplacementOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
mtl.CreateVolumeOutput("mdl").ConnectToSource(shader.ConnectableAPI(), "out")
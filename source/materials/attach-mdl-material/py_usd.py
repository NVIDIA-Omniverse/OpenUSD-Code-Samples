# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni
from pxr import Sdf, UsdShade

stage = omni.usd.get_context().get_stage()

# Create a mesh plane from points and indices
points = [(0, 0, 0), (1, 0, 0),  (1, 1, 0),  (0, 1, 0) ]
indices = [ 0, 1, 2, 0, 2, 3 ]

mesh = UsdGeom.Mesh.Define(stage, '/World/plane')
mesh.GetPointsAttr().Set(points)
mesh.GetFaceVertexIndicesAttr().Set(indices)
mesh.GetFaceVertexCountsAttr().Set([3] * len(indices))

# Set the materials path
mtl_path = Sdf.Path(f"/World/Looks/PreviewSurface")
#Define the shader
shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
shader.CreateIdAttr("UsdPreviewSurface")
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).Set((0,0,1)) 
shader.CreateInput("opacity", Sdf.ValueTypeNames.Float).Set(0.5)
shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0.0)
shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)
shader.CreateInput("ior", Sdf.ValueTypeNames.Float).Set(1.0)

# Bind the material to the mesh
mtl = UsdShade.Material.Define(stage, mtl_path)
mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
UsdShade.MaterialBindingAPI(mesh).Bind(mtl)
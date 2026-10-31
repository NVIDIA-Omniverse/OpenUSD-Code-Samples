# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Tuple
from pxr import Sdf, Usd, UsdShade

def create_texture_sampler(stage: Usd.Stage, path: Sdf.Path, file_path: str, st_source: UsdShade.Shader,
                           output_name: str, output_type: Sdf.ValueTypeName, color_space: str) -> UsdShade.Shader:
    texture = UsdShade.Shader.Define(stage, path)
    texture.CreateIdAttr("UsdUVTexture")
    texture.CreateInput("file", Sdf.ValueTypeNames.Asset).Set(file_path)
    # Sample the texture at the (transformed) UVs
    texture.CreateInput("st", Sdf.ValueTypeNames.Float2).ConnectToSource(st_source.ConnectableAPI(), "result")
    texture.CreateInput("wrapS", Sdf.ValueTypeNames.Token).Set("repeat")
    texture.CreateInput("wrapT", Sdf.ValueTypeNames.Token).Set("repeat")
    # "sRGB" for color textures, "raw" for data textures such as roughness or normals
    texture.CreateInput("sourceColorSpace", Sdf.ValueTypeNames.Token).Set(color_space)
    texture.CreateOutput(output_name, output_type)
    return texture


def create_textured_preview_surface_material(stage: Usd.Stage, mtl_path: Sdf.Path, texture_dir: str,
                                             uv_scale: Tuple[float, float] = (1.0, 1.0),
                                             uv_rotation: float = 0.0,
                                             uv_translation: Tuple[float, float] = (0.0, 0.0)) -> UsdShade.Material:
    mtl = UsdShade.Material.Define(stage, mtl_path)
    shader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Shader"))
    shader.CreateIdAttr("UsdPreviewSurface")
    shader.CreateInput("metallic", Sdf.ValueTypeNames.Float).Set(0.0)
    mtl.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")
    mtl.CreateDisplacementOutput().ConnectToSource(shader.ConnectableAPI(), "displacement")

    # Read the UVs from the "st" primvar of the bound mesh. The primvar name is exposed as a
    # material input, so the material can be pointed at a different UV set without editing the shaders.
    st_reader = UsdShade.Shader.Define(stage, mtl_path.AppendPath("STReader"))
    st_reader.CreateIdAttr("UsdPrimvarReader_float2")
    st_name_input = mtl.CreateInput("frame:stPrimvarName", Sdf.ValueTypeNames.Token)
    st_name_input.Set("st")
    st_reader.CreateInput("varname", Sdf.ValueTypeNames.Token).ConnectToSource(st_name_input)
    st_reader.CreateOutput("result", Sdf.ValueTypeNames.Float2)

    # Scale, rotate (counterclockwise, in degrees) and then translate the UVs around the UV origin.
    # One Transform2d is shared by every texture so they all stay aligned.
    transform2d = UsdShade.Shader.Define(stage, mtl_path.AppendPath("Transform2d"))
    transform2d.CreateIdAttr("UsdTransform2d")
    transform2d.CreateInput("in", Sdf.ValueTypeNames.Float2).ConnectToSource(st_reader.ConnectableAPI(), "result")
    transform2d.CreateInput("scale", Sdf.ValueTypeNames.Float2).Set(uv_scale)
    transform2d.CreateInput("rotation", Sdf.ValueTypeNames.Float).Set(uv_rotation)
    transform2d.CreateInput("translation", Sdf.ValueTypeNames.Float2).Set(uv_translation)
    transform2d.CreateOutput("result", Sdf.ValueTypeNames.Float2)

    # Connect one texture to each UsdPreviewSurface input
    diffuse = create_texture_sampler(stage, mtl_path.AppendPath("DiffuseTexture"), f"{texture_dir}/diffuse.png",
                                     transform2d, "rgb", Sdf.ValueTypeNames.Float3, "sRGB")
    shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(diffuse.ConnectableAPI(), "rgb")

    roughness = create_texture_sampler(stage, mtl_path.AppendPath("RoughnessTexture"), f"{texture_dir}/roughness.png",
                                       transform2d, "r", Sdf.ValueTypeNames.Float, "raw")
    shader.CreateInput("roughness", Sdf.ValueTypeNames.Float).ConnectToSource(roughness.ConnectableAPI(), "r")

    occlusion = create_texture_sampler(stage, mtl_path.AppendPath("OcclusionTexture"), f"{texture_dir}/occlusion.png",
                                       transform2d, "r", Sdf.ValueTypeNames.Float, "raw")
    shader.CreateInput("occlusion", Sdf.ValueTypeNames.Float).ConnectToSource(occlusion.ConnectableAPI(), "r")

    displacement = create_texture_sampler(stage, mtl_path.AppendPath("DisplacementTexture"), f"{texture_dir}/displacement.png",
                                          transform2d, "r", Sdf.ValueTypeNames.Float, "raw")
    shader.CreateInput("displacement", Sdf.ValueTypeNames.Float).ConnectToSource(displacement.ConnectableAPI(), "r")

    # Normal maps store [-1, 1] vectors as [0, 1] colors, so remap them with scale and bias
    normal = create_texture_sampler(stage, mtl_path.AppendPath("NormalTexture"), f"{texture_dir}/normal.png",
                                    transform2d, "rgb", Sdf.ValueTypeNames.Float3, "raw")
    normal.CreateInput("scale", Sdf.ValueTypeNames.Float4).Set((2.0, 2.0, 2.0, 1.0))
    normal.CreateInput("bias", Sdf.ValueTypeNames.Float4).Set((-1.0, -1.0, -1.0, 0.0))
    shader.CreateInput("normal", Sdf.ValueTypeNames.Normal3f).ConnectToSource(normal.ConnectableAPI(), "rgb")
    return mtl


#############
# Full Usage
#############

from pxr import Gf, UsdGeom

# Create an in-memory Stage with /World Xform prim as the default prim
stage: Usd.Stage = Usd.Stage.CreateInMemory()
default_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World")).GetPrim()
stage.SetDefaultPrim(default_prim)

# A plane with UVs authored in the "st" primvar, which the material reads
mesh = UsdGeom.Mesh.Define(stage, Sdf.Path("/World/Plane"))
mesh.CreatePointsAttr([(-100, -100, 0), (100, -100, 0), (100, 100, 0), (-100, 100, 0)])
mesh.CreateFaceVertexCountsAttr([4])
mesh.CreateFaceVertexIndicesAttr([0, 1, 2, 3])
mesh.CreateExtentAttr([(-100, -100, 0), (100, 100, 0)])
st = UsdGeom.PrimvarsAPI(mesh).CreatePrimvar("st", Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.varying)
st.Set([(0, 0), (1, 0), (1, 1), (0, 1)])

# Transform2d transforms the texture coordinates, not the texture, so the image moves the opposite way:
# scaling the UVs by 2 repeats the texture twice in each direction, making it look smaller.
mtl_path = Sdf.Path("/World/Looks/TexturedPreviewSurface")
mtl = create_textured_preview_surface_material(stage, mtl_path, "./textures", uv_scale=(2.0, 2.0))
UsdShade.MaterialBindingAPI.Apply(mesh.GetPrim()).Bind(mtl)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check the UV chain: mesh "st" primvar -> STReader -> Transform2d -> every texture
st_reader = UsdShade.Shader(stage.GetPrimAtPath(mtl_path.AppendPath("STReader")))
assert UsdShade.Utils.GetValueProducingAttributes(st_reader.GetInput("varname"))[0].Get() == "st"
transform2d = UsdShade.Shader(stage.GetPrimAtPath(mtl_path.AppendPath("Transform2d")))
assert transform2d.GetInput("in").GetConnectedSource()[0].GetPath() == st_reader.GetPath()
assert transform2d.GetInput("scale").Get() == Gf.Vec2f(2.0, 2.0)
for name in ("DiffuseTexture", "RoughnessTexture", "OcclusionTexture", "DisplacementTexture", "NormalTexture"):
    texture = UsdShade.Shader(stage.GetPrimAtPath(mtl_path.AppendPath(name)))
    assert texture.GetInput("st").GetConnectedSource()[0].GetPath() == transform2d.GetPath()

# Check that each texture drives the right UsdPreviewSurface input
shader = UsdShade.Shader(mtl.ComputeSurfaceSource()[0].GetPrim())
for input_name, texture_name in (("diffuseColor", "DiffuseTexture"), ("roughness", "RoughnessTexture"),
                                 ("occlusion", "OcclusionTexture"), ("displacement", "DisplacementTexture"),
                                 ("normal", "NormalTexture")):
    assert shader.GetInput(input_name).GetConnectedSource()[0].GetPath() == mtl_path.AppendPath(texture_name)
assert shader.GetInput("normal").GetTypeName() == Sdf.ValueTypeNames.Normal3f
assert mtl.ComputeDisplacementSource()[0].GetPath() == shader.GetPath()

# Check that the mesh resolves to the material and has the UVs it reads
assert UsdShade.MaterialBindingAPI(mesh.GetPrim()).ComputeBoundMaterial()[0].GetPath() == mtl_path
assert UsdGeom.PrimvarsAPI(mesh).HasPrimvar("st")

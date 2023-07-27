import omni.kit.commands
import omni.usd
from pxr import Usd, Sdf, UsdGeom

def create_payload(context: omni.usd.UsdContext, prim_path: Sdf.Path, payload_asset_path: str, payload_target_path: Sdf.Path) -> Usd.Prim:
    omni.kit.commands.execute("CreatePayload",
        path_to=prim_path, # Prim path for where to create the payload
        asset_path=payload_asset_path, # The file path to payload. Relative paths are accepted too.
        prim_path=payload_target_path,
        usd_context=context
    )
    return stage.GetPrimAtPath(prim_path)


#############
# Full Usage
#############

# Create new USD stage for this sample in OV
context: omni.usd.UsdContext = omni.usd.get_context()
success: bool = context.new_stage()
stage: Usd.Stage = context.get_stage()

# Create and define default prim, so this file can be easily payloadd again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create and add external payload to specific prim
payload_prim: Usd.Prim = create_payload(context, Sdf.Path("/World/payload_prim"), "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Create and add external payload to default prim
def_payload_prim: Usd.Prim = create_payload(context, Sdf.Path("/World/payload_default"), "C:/path/to/other/file.usd", Sdf.Path.emptyPath)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the payload prims were created
assert success
assert payload_prim.IsValid()
assert def_payload_prim.IsValid()

assert payload_prim.GetPrimStack()[0].payloadList.prependedItems[0] == Sdf.Payload(assetPath="file:/C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
assert def_payload_prim.GetPrimStack()[0].payloadList.prependedItems[0] == Sdf.Payload(assetPath="file:/C:/path/to/other/file.usd")
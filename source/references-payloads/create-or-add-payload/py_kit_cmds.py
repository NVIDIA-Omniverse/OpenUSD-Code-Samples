import omni.kit.commands
import omni.usd
from pxr import Usd, Sdf, UsdGeom

def add_payload(prim: Usd.Prim, payload_asset_path: str, payload_target_path: Sdf.Path) -> None:
    omni.kit.commands.execute("AddPayload",
        stage=prim.GetStage(),
        prim_path = prim.GetPath(), # an existing prim to add the payload to.
        payload=Sdf.Payload(
            assetPath = payload_asset_path,
            primPath = payload_target_path
        )
    )


#############
# Full Usage
#############

# Create new USD stage for this sample in OV
context: omni.usd.UsdContext = omni.usd.get_context()
success: bool = context.new_stage()
stage: Usd.Stage = context.get_stage()

# Create and define default prim, so this file can be easily payloaderenced again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create a xform which should hold all payloads in this sample
payload_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/payload_prim")).GetPrim()

# Add an payload specific prim
add_payload(payload_prim, "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Add other payload to default prim
add_payload(payload_prim, "C:/path/to/other/file.usd", Sdf.Path.emptyPath)

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
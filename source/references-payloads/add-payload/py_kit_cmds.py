import omni.kit.commands
import omni.usd
from pxr import Usd, Sdf, UsdGeom

def add_payload(prim: Usd.Prim, ref_asset_path: str, ref_target_path: Sdf.Path) -> None:
    omni.kit.commands.execute("AddPayload",
        stage=prim.GetStage(),
        prim_path = prim.GetPath(), # an existing prim to add the payload to.
        payload=Sdf.Payload(
            assetPath = ref_asset_path,
            primPath = ref_target_path
        )
    )


#############
# Full Usage
#############

# Create new USD stage for this sample
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Create and define default prim, so this file can be easily referenced again
default_prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World"))
stage.SetDefaultPrim(default_prim.GetPrim())

# Create a xform which should hold all payloads in this sample
ref_prim: Usd.Prim = UsdGeom.Xform.Define(stage, Sdf.Path("/World/ref_prim")).GetPrim()

# Add an payload specific prim
add_payload(ref_prim, "C:/path/to/file.usd", Sdf.Path("/World/some/target"))

# Add other payload to default prim
add_payload(ref_prim, "C:/path/to/other/file.usd", Sdf.Path.emptyPath)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Get a list of all prepended payloads
payloads = []
for prim_spec in ref_prim.GetPrimStack():
    payloads.extend(prim_spec.payloadList.prependedItems)

# Check that the payload prim was created and that the payloads are correct
assert ref_prim.IsValid()
assert payloads[0] == Sdf.Payload(assetPath="C:/path/to/file.usd", primPath=Sdf.Path("/World/some/target"))
assert payloads[1] == Sdf.Payload(assetPath="C:/path/to/other/file.usd")
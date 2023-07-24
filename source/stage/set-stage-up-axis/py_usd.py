from pxr import Usd, UsdGeom

def set_up_axis(stage: Usd.Stage, axis: UsdGeom.Tokens):
    """Sets stage up axis

    Args:
        stage (Usd.Stage): The stage where the up axis should be set.
        axis (Tf.Token): The token to define the up axis.
    """
    UsdGeom.SetStageUpAxis(stage, axis)


#############
# Full Usage
#############
axis: UsdGeom.Tokens = UsdGeom.Tokens.z
stage: Usd.Stage = Usd.Stage.CreateInMemory()
set_up_axis(stage, axis)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected upAxis was set
assert UsdGeom.GetStageUpAxis(stage) == axis

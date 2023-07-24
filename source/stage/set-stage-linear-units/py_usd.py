from pxr import Usd, UsdGeom


def set_meters_per_unit(stage: Usd.Stage, unit: UsdGeom.LinearUnits = UsdGeom.LinearUnits.centimeters):
    """Sets stage linear units 

    Args:
        stage (Usd.Stage): The stage where the linear units should be set.
        unit (UsdGeom.LinearUnits, Optional): The linear units to set the stage to.
    """
    UsdGeom.SetStageMetersPerUnit(stage, unit) # Any double-precision float can be used for metersPerUnit.


#############
# Full Usage
#############
unit: UsdGeom.LinearUnits = UsdGeom.LinearUnits.centimeters
stage: Usd.Stage = Usd.Stage.CreateInMemory()
set_meters_per_unit(stage, unit)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected meterPerUnit were set
assert UsdGeom.GetStageMetersPerUnit(stage) == unit

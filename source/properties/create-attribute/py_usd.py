# Add all the imports that you need for you snippets
from pxr import Gf, Sdf, Usd, UsdGeom

"""
Find all relevant data types at: https://graphics.pixar.com/usd/release/api/_usd__page__datatypes.html
"""


def create_float_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
    """Creates attribute for a prim that holds a float.
    See: https://graphics.pixar.com/usd/release/api/class_usd_prim.html
    Args:
        prim (Usd.Prim): A Prim for holding the attribute.
        attribute_name (str): The name of the attribute to create.
    Returns:
        Usd.Attribute: An attribute created at specific prim.
    """
    attr = prim.CreateAttribute(attribute_name, Sdf.ValueTypeNames.Float)
    return attr


def create_vector_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
    """Creates attribute for a prim that holds a vector.
    See: https://graphics.pixar.com/usd/release/api/class_usd_prim.html
    Args:
        prim (Usd.Prim): A Prim for holding the attribute.
        attribute_name (str): The name of the attribute to create.
    Returns:
        Usd.Attribute: An attribute created at specific prim.
    """
    attr = prim.CreateAttribute(attribute_name, Sdf.ValueTypeNames.Float3)
    return attr


#############
# Full Usage
#############

# Create an in-memory Stage
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Create a default prim named /World
default_prim_path = "/World"
default_prim = UsdGeom.Xform.Define(stage, default_prim_path)
stage.SetDefaultPrim(default_prim.GetPrim())

# Create a child prim on which to test attribute creation
test_prim_path = f"{default_prim_path}/test_prim"
test_prim = UsdGeom.Scope.Define(stage, test_prim_path)

# create a float attribute
float_attr = create_float_attribute(test_prim.GetPrim(), "test_float_attr")

# create a vector attribute
vector_attr = create_vector_attribute(test_prim.GetPrim(), "test_vector_attr")

# Set and query values
print(float_attr.Get())
float_attr.Set(0.1)
print(float_attr.Get())

vector_value = Gf.Vec3f(0.1, 0.2, 0.3)
print(vector_attr.Get())
vector_attr.Set(vector_value)
print(vector_attr.Get())

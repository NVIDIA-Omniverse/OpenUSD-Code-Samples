# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict
from pxr import Usd

def set_metadata_on_attribute(attr: Usd.Attribute, data: dict):
    attr.SetMetadata("customData", data)


##############
# Full Usage
##############

from pxr import UsdGeom, Sdf

# Create an in-memory Stage
stage : Usd.Stage = Usd.Stage.CreateInMemory()

# Create a prim
xform : Usd.Prim = UsdGeom.Xform.Define(stage, "/World/Xform")
xform_prim = xform.GetPrim()

# Create an attribute on the prim
attr : Usd.Attribute = xform_prim.CreateAttribute("custom_attribute", Sdf.ValueTypeNames.String)

# Create a customData dictionary
my_dict = dict()
my_dict["my_int"] = 3
my_dict["my_string"] = "I love OpenUSD!"

# Set customData to the previously defined dict
set_metadata_on_attribute(attr, my_dict)

# Get the custom metadata defined previously
cust_data = attr.GetMetadata("customData")

# Print the custom metadata dict
print(cust_data)

# Print the value of the keys "my_int" and "my_string" in the custom metadata dict
my_int_value = cust_data["my_int"]
my_string_value = cust_data["my_string"]
print(my_int_value)
print(my_string_value)

# Check whether found data is correct
assert cust_data == my_dict
assert len(cust_data.keys()) == 2
assert cust_data["my_int"] == 3
assert cust_data["my_string"] == "I love OpenUSD!"
assert cust_data == attr.GetCustomData() # Alternative way to get custom data
assert attr.GetCustomDataByKey("my_int") == 3
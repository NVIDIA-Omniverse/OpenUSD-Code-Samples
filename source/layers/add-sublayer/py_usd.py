# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf


def add_sub_layer(sub_layer_path: str, root_layer) -> Sdf.Layer:
    sub_layer: Sdf.Layer = Sdf.Layer.CreateNew(sub_layer_path)
    # You can use standard python list.insert to add the subLayer to any position in the list
    root_layer.subLayerPaths.append(sub_layer.identifier)
    return sub_layer

#############
# Full Usage
#############

from pxr import Usd

# Get the root layer
stage: Usd.Stage = Usd.Stage.CreateInMemory()
root_layer: Sdf.Layer = stage.GetRootLayer()

# Add the sub layer to the root layer
sub_layer = add_sub_layer(r"C:/path/to/sublayer.usd", root_layer)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check to see if the sublayer is loaded 
loaded_layers = root_layer.GetLoadedLayers()
assert sub_layer in loaded_layers
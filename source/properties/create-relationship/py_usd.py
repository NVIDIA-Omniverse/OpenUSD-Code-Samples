# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

prim: Usd.Prim = stage.GetPrimAtPath("/World/MyPrim")
custom_relationship: Usd.Relationship = prim.CreateRelationship("myCustomRelationship")
# You can also use Usd.Relationship.AddTarget() to add targets to an existing Relationship.
custom_relationship.SetTargets(["/World/TargetA", "/World/TargetB"])
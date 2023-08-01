# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import omni.kit.commands
from pxr import Gf, Sdf, Usd

prim_path = Sdf.Path("/World/defaultLight")
prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
prop_name = "xformOp:rotateXYZ"
rotation = prim.GetAttribute(prop_name)
omni.kit.commands.execute("ChangeProperty",
    prop_path=Sdf.Path(prim_path.AppendProperty(prop_name)),
    value=Gf.Vec3d(180.0, 0.0, 0.0),
    prev=rotation.Get(10.0),
    timecode=Usd.TimeCode(10.0)
)
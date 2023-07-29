# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Sdf

prim_path = Sdf.Path("/Kitchen_set/Props_grp")
concat_prim_path = prim_path.AppendPath("North_grp/NorthWall_grp/MeasuringSpoon_1")
# concat_prim_path now contains Sdf.Path("/Kitchen_set/Props_grp/North_grp/NorthWall_grp/MeasuringSpoon_1")


# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy
from pxr import Vt

my_vec3_array = Vt.Vec3fArray([(1,2,3),(4,5,6),(7,8,9)])
from_vt = numpy.array(my_vec3_array)
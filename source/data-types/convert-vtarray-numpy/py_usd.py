# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy
from pxr import Vt


def convert_vt_to_np(my_array: Vt.Vec3fArray) -> numpy.ndarray:
    return numpy.array(my_vec3_array)


#############
# Full Usage
#############
my_vec3_array = Vt.Vec3fArray([(1,2,3),(4,5,6),(7,8,9)])
np_array: numpy.ndarray = convert_vt_to_np(my_vec3_array)

assert np_array.size == 9
assert len(np_array) == 3

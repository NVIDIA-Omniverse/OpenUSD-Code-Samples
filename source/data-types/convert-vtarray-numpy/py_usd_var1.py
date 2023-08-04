# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy
from pxr import Vt


def convert_np_to_vt(my_array: numpy.ndarray) -> Vt.Vec3fArray:
    return Vt.Vec3fArray.FromNumpy(my_array)


#############
# Full Usage
#############

# Create a numpy array and convert it into a Vt.Vec3fArray
np_array = numpy.array([(1,2,3),(4,5,6),(7,8,9)])
from_numpy: Vt.Vec3fArray = convert_np_to_vt(np_array)

# Print the Vt.Vec3fArray to check the values
print(from_numpy)

# Check the length of the numpy array
assert len(np_array) == 3
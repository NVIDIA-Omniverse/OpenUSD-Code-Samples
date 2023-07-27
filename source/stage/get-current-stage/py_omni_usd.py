# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd
import omni.usd

def get_current_stage() -> Usd.Stage:
    return omni.usd.get_context().get_stage()


#############
# Full Usage
#############
# Create a new USD stage throught the UsdContext
success: bool = omni.usd.get_context().new_stage()

# Get the the current stage from the UsdContext
current_stage: Usd.Stage = get_current_stage()

# Check if the a new stage was created and a valid stage was returned
assert success
assert current_stage

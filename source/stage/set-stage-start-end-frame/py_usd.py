# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pxr import Usd

def set_start_end_frame(stage: Usd.Stage, start: float, end: float):
    stage.SetStartTimeCode(start)
    stage.SetEndTimeCode(end)


#############
# Full Usage
#############
start: float = 1.0
end: float = 240.0
stage: Usd.Stage = Usd.Stage.CreateInMemory()
set_start_end_frame(stage, start, end)

usda = stage.GetRootLayer().ExportToString()
print(usda)

# Check that the expected start and end frames were set
assert stage.GetStartTimeCode() == start
assert stage.GetEndTimeCode() == end
assert stage.HasAuthoredTimeCodeRange()

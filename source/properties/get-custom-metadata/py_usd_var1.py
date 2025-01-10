# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Any
from pxr import Usd

def get_customdata(usd: Usd.Object, key: Any = None) -> Any:
    """
    Args:
        usd : Any USD scene description that has customData metadata.
            For example, Usd.Prim, Usd.Property

        key : Key to retrieve the value from the customData dictionary. 
            If not provided, will return the entire metadata dictionary.
    Return:
        metadata : Python dictionary containing the metadata for the USD object, 
            or the value associated with the key if provided.
    """
    if key:
        return usd.GetCustomDataByKey(key)
    else:
        metadata : Dict = usd.GetCustomData()
        return metadata

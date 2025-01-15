# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Any
from pxr import Usd

def get_metadata(usd: Usd.Object, data_type: str = "customData", key: Any = None) -> Any:
    """
    Args:
        usd : Any USD scene description that can be authored with metadata. 
            For example, Usd.Prim, Usd.Property

        data_type : Name of the metadata to be retrieved. 
            customData is provided by USD as a dictionary-valued metadatum. No user config needed to use this.
        
        key : Key to retrieve the value from the metadata dictionary. If not provided, will return the entire metadata dictionary.
    Return:
        metadata : Python dictionary containing the metadata for the USD object, or the value associated with the key if provided.
    """
    if key:
        return usd.GetMetadata(data_type)[key]
    else:
        metadata : Dict = usd.GetMetadata(data_type)
        return metadata

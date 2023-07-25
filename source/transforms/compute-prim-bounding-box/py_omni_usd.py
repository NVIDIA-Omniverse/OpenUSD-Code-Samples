import typing

import carb
import omni.usd

def compute_path_bbox(prim_path: str) -> typing.Tuple[carb.Double3, carb.Double3]:
    """
    Compute Bounding Box using omni.usd.UsdContext.compute_path_world_bounding_box
    See https://docs.omniverse.nvidia.com/kit/docs/omni.usd/latest/omni.usd/omni.usd.UsdContext.html#omni.usd.UsdContext.compute_path_world_bounding_box

    Args:
        prim_path: A prim path to compute the bounding box.
    Returns: 
        A range (i.e. bounding box) as a minimum point and maximum point.
    """
    return omni.usd.get_context().compute_path_world_bounding_box(prim_path)
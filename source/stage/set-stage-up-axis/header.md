You can set the `upAxis` metadata on the stage using `UsdGeom.SetStageUpAxis` to define which world axis points up. The tokens for the different axes are scoped in `UsdGeom.Tokens`.

.. note::
    Fallback stage upAxis is Y.

.. warning::
    Existing objects will not be automatically rotated to adapt to the stage `upAxis`. Learn more about `stage up axis <https://graphics.pixar.com/usd/release/api/group___usd_geom_up_axis__group.html>`_.


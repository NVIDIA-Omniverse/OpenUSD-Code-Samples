You can set the :code:`metersPerUnit` metadata on the stage using :code:`UsdGeom.SetStageMetersPerUnit`. Convenience shortcuts for units are scoped in :code:`UsdGeom.LinearUnits` (e.g. :code:`UsdGeom.LinearUnits.meters` is :code:`1.0 metersPerUnit`)

.. note::
    Fallback stage linear units are centimeters (0.01).

.. warning::
    Existing objects will not be automatically scaled to adapt to the stage linear units. Learn more about `stage linear units <https://graphics.pixar.com/usd/release/api/group___usd_geom_linear_units__group.html>`_.


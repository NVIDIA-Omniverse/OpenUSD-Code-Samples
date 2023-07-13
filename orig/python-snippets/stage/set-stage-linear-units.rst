.. meta::
    :description: Universal Scene Description (USD) Python code snippet for defining the linear units of a Stage (i.e. metersPerUnit metadata).
    :keywords: USD, Python, snippet, stage, metadata, metersPerUnit, units, linear units

=================================
Set the Stage Linear Units
=================================

You can set the :code:`metersPerUnit` metadata on the stage using :code:`UsdGeom.SetStageMetersPerUnit` to define the linear units of the stage. Convenience shortcuts for units are scoped in :code:`UsdGeom.LinearUnits` (e.g. :code:`UsdGeom.LinearUnits.meters` is :code:`1.0 metersPerUnit`)

.. note::
    Fallback stage linear units are centimeters (0.01).

.. warning::
    Existing objects will not be automatically scaled to adapt to the stage linear units. Learn more about `stage linear units <https://graphics.pixar.com/usd/release/api/group___usd_geom_linear_units__group.html>`_.

USD API
-------
.. code-block:: python

    from pxr import UsdGeom

    
    # Set stage linear units to meters.
    # Any double-precision float can be used for metersPerUnit.
    UsdGeom.SetStageMetersPerUnit(stage, UsdGeom.LinearUnits.meters)
    


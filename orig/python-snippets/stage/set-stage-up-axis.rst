.. meta::
    :description: Universal Scene Description (USD) Python code snippet for defining the up axis of a Stage.
    :keywords: USD, Python, snippet, stage, metadata, upAxis, axis, coordinate system

=================================
Set the Stage Up Axis
=================================

You can set the :code:`upAxis` metadata on the stage using :code:`UsdGeom.SetStageUpAxis` to define which world axis points up. The tokens for the different axes are scoped in :code:`UsdGeom.Tokens`.

.. note::
    Fallback stage upAxis is Y.

.. warning::
    Existing objects will not be automatically rotated to adapt to the stage :code:`upAxis`. Learn more about `stage up axis <https://graphics.pixar.com/usd/release/api/group___usd_geom_up_axis__group.html>`_.

USD API
-------
.. code-block:: python

    from pxr import UsdGeom

    # Set stage upAxis to Z.
    UsdGeom.UsdGeomSetStageUpAxis(stage, UsdGeom.Tokens.z)

    

    

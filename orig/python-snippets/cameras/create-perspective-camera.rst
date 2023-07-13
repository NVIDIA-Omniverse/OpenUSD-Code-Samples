.. meta::
    :description: Universal Scene Description (USD) Python code snippet for creating a perspective camera prim and setting some common camera attributes.
    :keywords: USD, Python, snippet, prim, camera, UsdGeom, Perspective

=============================
Create a Perspective Camera
=============================

You can define a new camera on a stage using :code:`UsdGeom.Camera`. The Camera prim has a :code:`projection` attribute that can be set to :code:`perspective`.

Omniverse Kit Commands
----------------------
The :code:`CreatePrimWithDefaultXform` command in Kit can create a Camera prim and you can optionally set camera attributes values during creation. You must use the attribute token names as the keys for the :code:`attributes` dictionary. In Omniverse applications, you can explore the names by hovering over a property label in the Property Window and reading it from the tooltip.

.. code-block:: python
    
    import omni.kit.commands
    from pxr import UsdGeom

    omni.kit.commands.execute("CreatePrimWithDefaultXform",
       prim_type="Camera",
       prim_path="/World/MyPerspCam",
       attributes={
          "projection": UsdGeom.Tokens.perspective,
          "focalLength": 35,
          "horizontalAperture": 20.955,
          "verticalAperture": 15.2908,
          "clippingRange": (0.1, 100000)
       }
    )


USD API
-----------
.. code-block:: python

    from pxr import Sdf, UsdGeom

    camera_path = Sdf.Path("/World/MyPerspCam")
    usd_camera = UsdGeom.Camera.Define(stage, camera_path)
    usd_camera.CreateProjectionAttr().Set(UsdGeom.Tokens.perspective)

Here is how to you can set some other common attributes on the camera:

.. code-block:: python

    from pxr import Sdf, UsdGeom

    usd_camera.CreateFocalLengthAttr().Set(35)
    usd_camera.CreateHorizontalApertureAttr().Set(20.955)
    usd_camera.CreateVerticalApertureAttr().Set(15.2908)
    usd_camera.CreateClippingRangeAttr().Set((0.1,100000))

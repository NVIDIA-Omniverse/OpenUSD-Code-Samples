.. meta::
    :description: Universal Scene Description (USD) Python code snippets for setting the value of an Attribute.
    :keywords: USD, Python, snippet, attribute, set, value, ChangeProperty, Omniverse Kit, Kit Commands

=============================
Set the Value of an Attribute
=============================

In Omniverse, you can use the :code:`ChangeProperty` command to set the default value or timesample value of an Attribute. With the USD API, you can call :code:`Usd.Attribute.Set()` to set a default value or timesample value.

.. note::
    You will need to provide the value in the correct data type for the attribute you want to set. See our reference listing all of the :doc:`USD Data Types <../../quick-start/usd-types>` and how to work with them in Python.

Omniverse Kit Commands
----------------------
The :code:`ChangeProperty` command allows users to undo the operation, but you must provide the value to use during the undo operation as the :code:`prev` parameter.

.. code-block:: python

    import omni.kit.commands
    from pxr import Gf, Sdf, Usd

    prim_path = Sdf.Path("/World/defaultLight")
    prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
    prop_name = "xformOp:rotateXYZ"
    rotation = prim.GetAttribute(prop_name)
    omni.kit.commands.execute("ChangeProperty",
        prop_path=Sdf.Path(prim_path.AppendProperty(prop_name)),
        value=Gf.Vec3d(180.0, 0.0, 0.0),
        prev=rotation.Get()
    )

You can also set a timesample value at a particular time:

.. code-block:: python

    import omni.kit.commands
    from pxr import Gf, Sdf, Usd

    prim_path = Sdf.Path("/World/defaultLight")
    prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
    prop_name = "xformOp:rotateXYZ"
    rotation = prim.GetAttribute(prop_name)
    omni.kit.commands.execute("ChangeProperty",
        prop_path=Sdf.Path(prim_path.AppendProperty(prop_name)),
        value=Gf.Vec3d(180.0, 0.0, 0.0),
        prev=rotation.Get(10.0),
        timecode=Usd.TimeCode(10.0)
    )

USD API
-------
.. code-block:: python

    from pxr import Usd, Sdf, Gf

    def set_float_attribute(attr: Usd.Attribute, value: float) -> None:
        """
        See: https://graphics.pixar.com/usd/release/api/class_usd_attribute.html
        Args:
            attr: The attribute to set.
            value: A floating point value, i.e. `3.141516`.
        """
        attr.Set(value)

    def set_vector_attribute(attr: Usd.Attribute, value: Gf.Vec3f) -> None:
        """
        Args:
            attr: The attribute to set.
            value: A floating point vector, i.e. `(1., 2., 3.)`.
        """
        attr.Set(value)


You can also set a timesample value at a particular time:

.. code-block:: python

    from pxr import Usd, Sdf, Gf

    def set_float_attribute(attr: Usd.Attribute, value: float, time_value: float) -> None:
        """
        See: https://graphics.pixar.com/usd/release/api/class_usd_attribute.html
        Args:
            attr: The attribute to set.
            value: A floating point value, i.e. `3.141516`.
            time_value: Set a timesample at a particular time.
        """
        attr.Set(value, time_value)

    def set_vector_attribute(attr: Usd.Attribute, value: Gf.Vec3f, time_value: float) -> None:
        """
        Args:
            attr: The attribute to set.
            value: A floating point vector, i.e. `(1., 2., 3.)`.
            time_value: Set a timesample at a particular time.
        """
        attr.Set(value, time_value)


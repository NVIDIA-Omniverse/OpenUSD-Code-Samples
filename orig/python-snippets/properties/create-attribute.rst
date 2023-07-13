.. meta::
    :description: Universal Scene Description (USD) Python code snippets for creating an Attribute on a prim.
    :keywords: USD, Python, snippet, attribute, create, CreateUsdAttributeCommand, Omniverse Kit, Kit Commands

==========================
Create an Attribute
==========================

You should create a schema or custom Attribute on a Prim in order to set its value. To create an Attribute, you must provide the Attribute name and the data type for the Attribute value. This snippet shows how you can create an Attribute using :code:`CreateUsdAttributeCommand` in Kit or `Usd.Prim.CreateAttribute() <https://graphics.pixar.com/usd/release/api/class_usd_prim.html#a935381d7c7100b583fdcdb0e10dae9e6>`_.

.. note::
    You will need to define the data type of the Attribute you want to create. See our reference listing all of the :doc:`USD Data Types <../../quick-start/usd-types>` and how to work with them in Python.

Omniverse Kit Commands
----------------------
:code:`CreateUsdAttributeCommand` allows users to undo the operation.

.. code-block:: python
    
    import omni.kit.commands
    from pxr import Sdf, Usd

    # Create a float attribute
    prim: Usd.Prim = stage.GetPrimAtPath("/World/MyMesh")
    attr_name = "myFloat"
    omni.kit.commands.execute("CreateUsdAttributeCommand",
        prim=prim,
        attr_name=attr_name,
        attr_type=Sdf.ValueTypeNames.Float
    )

    # Create a vector attribute
    prim: Usd.Prim = stage.GetPrimAtPath("/World/MyMesh")
    attr_name = "myFloat3"
    omni.kit.commands.execute("CreateUsdAttributeCommand",
        prim=prim,
        attr_name=attr_name,
        attr_type=Sdf.ValueTypeNames.Float3
    )

USD API
-------
.. code-block:: python

    from pxr import Usd, Sdf

    def create_float_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
        """
        Creates attribute for a prim that holds a float.
        See: https://graphics.pixar.com/usd/release/api/class_usd_prim.html
        Args:
            prim: A prim holding the attribute.
            attribute_name: The name of the attribute to create.
        Returns:
            An attribute created at specific prim.
        """
        attr = prim.CreateAttribute(attribute_name, Sdf.ValueTypeNames.Float)
        return attr

    def create_vector_attribute(prim: Usd.Prim, attribute_name: str) -> Usd.Attribute:
        """
        Creates attribute for a prim that holds a 3D vector.
        See: https://graphics.pixar.com/usd/release/api/class_usd_prim.html
        Args:
            prim: A prim holding the attribute.
            attribute_name: The name of the attribute to create.
        Returns:
            An attribute created at specific prim.
        """
        attr = prim.CreateAttribute(attribute_name, Sdf.ValueTypeNames.Float3)
        return attr

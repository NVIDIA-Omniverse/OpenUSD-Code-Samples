.. meta::
    :description: Universal Scene Description (USD) Python code snippets for getting the value of an Attribute.
    :keywords: USD, Python, snippet, attribute, get, value, value resolution

=============================
Get the Value of an Attribute
=============================

:code:`Usd.Prim.GetAttribute()` returns a :code:`Usd.Attribute`, but this is not the value for the Attribute. You must call :code:`Usd.Attribute.Get()` to perform the `attribute value resolution <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-valueresolution>`_ resulting in a default value, timesample value or interpolated value for the Attribute.

USD API
-------
.. code-block:: python

    from pxr import Usd, Sdf

    def get_attribute_value(prim: Usd.Prim, attribute_name: str):
        """
        See: https://graphics.pixar.com/usd/release/api/class_usd_attribute.html
        Args:
            prim: The prim owner of the attribute.
            attribute_name: The name of the attribute to retrieve.
        Return:
            The value of the attribute, see https://graphics.pixar.com/usd/release/api/_usd__page__datatypes.html
            for the return types.
            For example, for `float3`, the return type will be `Gf.Vec3f`.
        """
        attr = prim.GetAttribute(attribute_name)
        return attr.Get()

You can also get the value at a particular time:

.. code-block:: python

    from pxr import Usd, Sdf

    def get_attribute_value(prim: Usd.Prim, attribute_name: str, time_value: float):
        """
        See: https://graphics.pixar.com/usd/release/api/class_usd_attribute.html
        Args:
            prim: The prim owner of the attribute.
            attribute_name: The name of the attribute to retrieve.
            time_value: Get the value authored or interpolated at a particular time.
        Return:
            The value of the attribute, see https://graphics.pixar.com/usd/release/api/_usd__page__datatypes.html
            for the return types.
            For example, for `float3`, the return type will be `Gf.Vec3f`.
        """
        attr = prim.GetAttribute(attribute_name)
        return attr.Get(time_value)

.. note::
    See our reference listing all of the :doc:`USD Data Types <../../quick-start/usd-types>` and how to work with them in Python.
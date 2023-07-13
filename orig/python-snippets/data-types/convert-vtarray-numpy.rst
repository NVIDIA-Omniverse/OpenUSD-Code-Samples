.. meta::
    :description: Universal Scene Description (USD) Python code snippets for converting between VtArray classes and Numpy.
    :keywords: USD, Python, snippet, data types, array, numpy, VtArray

===============================================
Convert Between VtArray and Numpy Array
===============================================

Some Attributes store array type data which are accessed using the VtArray classes. You can find a list of the VtArray classes in our :doc:`USD Data Types documentation <../../quick-start/usd-types>`. 

If you need to manipulate the arrays using Python, it is advantageous to use Numpy to benefit from it's speed and efficiency. These snippets show how you can convert between the VtArray objects and Numpy Array objects.


USD API
--------------

Convert to Numpy Array
######################

To convert a VtArray to a Numpy Array, simply pass the VtArray object to :code:`numpy.array` constructor.

.. code-block:: python
    
    import numpy
    from pxr import Vt

    my_vec3_array = Vt.Vec3fArray([(1,2,3),(4,5,6),(7,8,9)])
    from_vt = numpy.array(my_vec3_array)

Convert from Numpy Array
########################

To convert a Numpy Array to a VtArray, you can use :code:`FromNumpy()` from the VtArray class you want to convert to.

.. code-block:: python
    
    import numpy
    from pxr import Vt

    my_array = numpy.array([(1,2,3),(4,5,6),(7,8,9)])
    from_numpy = Vt.Vec3fArray.FromNumpy(my_array)

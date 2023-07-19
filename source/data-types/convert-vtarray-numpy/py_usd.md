**Convert to Numpy Array**

To convert a VtArray to a Numpy Array, simply pass the VtArray object to `numpy.array` constructor.

``` {literalinclude} py_usd.py
:language: py
```

**Convert from Numpy Array** 

To convert a Numpy Array to a VtArray, you can use `FromNumpy()` from the VtArray class you want to convert to.

``` {literalinclude} py_usd_var1.py
:language: py
``` 
Some Attributes store array type data which are accessed using the VtArray classes. You can find a list of the VtArray classes in the [Vt (Value Types) library module documentation](https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/Vt.html). 


If you need to manipulate the arrays using Python, it is advantageous to use Numpy to benefit from its speed and efficiency. These code samples show how you can convert between the VtArray objects and Numpy Array objects.

```{note}
These examples show how to convert using only the Vt.Vec3fArray class, but the same can be applied to any VtArray class. See what other VtArray classes exist in the [USD Data Types documentation](https://docs.omniverse.nvidia.com/usd/latest/technical_reference/usd-types.html).
```


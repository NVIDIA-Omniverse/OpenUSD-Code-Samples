You can use the USD API [`Usd.Prim.GetAttribute`](https://openusd.org/dev/api/class_usd_prim.html#a31225ac7165f58726f000ab1d67e9e61) to get an attribute of a prim and then use [`Usd.Attribute.Set`](https://openusd.org/dev/api/class_usd_attribute.html#a151e6fde58bbd911da8322911a3c0079) to change the value. The attribute name for visibility is `visibility` and you can set it to the value of `inherited` or `invisible`.

``` {literalinclude} py_usd.py
:language: py
```
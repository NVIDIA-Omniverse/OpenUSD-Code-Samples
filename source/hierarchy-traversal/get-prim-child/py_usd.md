If you know the name of the child prim, you can use `Usd.Prim.GetChild()`. This returns an invalid prim if the child doesn't exist. You can 

FIXME
check if the returned prim exists <../prims/check-prim-exists>`.

``` {literalinclude} py_usd.py
:language: py
```

Another option is to iterate through all of the prim's children to operate on all the children or query them to find the child you are looking for.
``` {literalinclude} py_usd_var1.py
:language: py
```
Create a new Stage.

``` {literalinclude} py_usd.py
:language: py
```

Create a new Stage only in memory. These stages are anonymous layers and hence cannot be saved or opened.
To create a stage without a session layer, pass `sessionLayer = None` as an argument to `Usd.Stage.CreateInMemory()`

``` {literalinclude} py_usd_var1.py
:language: py
``` 
``` {literalinclude} py_usd.py
:language: py
```

FIXME:
.. warning::    This will be slow for stages with many prims, as stage traversal is currently single-threaded. Learn more about `scene complexity <https://graphics.pixar.com/usd/release/maxperf.html#what-makes-a-usd-scene-heavy-expensive>`_.
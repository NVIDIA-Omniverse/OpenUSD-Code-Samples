.. meta::
    :description: Universal Scene Description (USD) Python code snippet for finding a Prim by its name on a Stage.
    :keywords: USD, Python, snippet, prim, name, Traverse

==================================
Find a Prim by Name
==================================

If you want to find all of the prims of a certain type, you can `Traverse <https://graphics.pixar.com/usd/release/api/class_usd_stage.html#adba675b55f41cc1b305bed414fc4f178>`_ the stage and use `Usd.Prim.GetName() <https://graphics.pixar.com/usd/release/api/class_usd_object.html#ae57e12beedf10c423e11c5b889343f6d>`_ to compare the name of every prim on the stage with the name you are looking for.

.. note::
    There could be more than one prim with the same name on a stage.

USD API
--------------
.. code-block:: python

    foundPrims = [x for x in stage.Traverse() if x.GetName() == myname]

.. warning::
    This will be slow for stages with many prims, as stage traversal is currently single-threaded. Learn more about `scene complexity <https://graphics.pixar.com/usd/release/maxperf.html#what-makes-a-usd-scene-heavy-expensive>`_.


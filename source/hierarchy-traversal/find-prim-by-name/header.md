FIXME:
If you want to find all of the prims of a certain type, you can `Traverse <https://graphics.pixar.com/usd/release/api/class_usd_stage.html#adba675b55f41cc1b305bed414fc4f178>`_ the stage and use `Usd.Prim.GetName() <https://graphics.pixar.com/usd/release/api/class_usd_object.html#ae57e12beedf10c423e11c5b889343f6d>`_ to compare the name of every prim on the stage with the name you are looking for.

.. note::
    There could be more than one prim with the same name on a stage.

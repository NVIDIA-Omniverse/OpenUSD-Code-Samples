
.. meta::
    :description: Universal Scene Description (USD) Python code snippet for setting the default prim on a Stage.
    :keywords: USD, Python, snippet, stage, default prim, metadata

=================================
Set the Default Prim on a Stage
=================================

It's best practice to set the :code:`defaultPrim` metadata on a Stage if the Stage's root layer may be used as a Reference or Payload. Otherwise, consumers of your Stage are forced to provide a target prim when they create a Reference or Payload arc. Even though the :code:`Usd.Stage.SetDefaultPrim()` accepts any :code:`Usd.Prim`, the default prim must be a top-level prim on the Stage.

USD API
--------------
.. code-block:: python

    # my_prim should be a top-level Usd.Prim object.
    stage.SetDefaultPrim(my_prim)


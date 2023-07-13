.. meta::
    :description: Universal Scene Description (USD) Python code snippets for adding a Payload to a prim.
    :keywords: USD, Python, snippet, payload, AddPayload

======================
Add a Payload
======================

A `Payload <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-payload>`_ is a composition arc that functions similar to a Reference to enable users to aggregate layers or assets onto a Stage. The difference is that a users can choose to not load a Payload. This can help users see the full hierarchy of a Stage, but only load the heavy parts ( i.e. Payloads) that they need. A Payload targets a prim from a layer and loads it and all of its descendants into a new namespace within the referencing layer. This snippet shows how to add a Payload to a prim. A single prim can have multiple Payloads.

Omniverse Kit Commands
----------------------
.. code-block:: python
    
    import omni.kit.commands
    import omni.usd
    from pxr import Sdf

    omni.kit.commands.execute("AddPayload",
        stage=omni.usd.get_context().get_stage(),
        prim_path=Sdf.Path("/World/Add/Payload/Here"), # an existing prim to add the payload to.
        payload=Sdf.Payload(r"C:/path/to/file.usd")
    )

USD API
-------
.. code-block:: python

    from pxr import Usd

    prim: Usd.Prim = stage.GetPrimAtPath("/World/my/prim")
    payloads: Usd.Payloads = prim.GetPayloads()
    payloads.AddPayload(
        assetPath=r"C:/path/to/file.usd", 
        primPath="/World/some/target" # OPTIONAL: Uses a specific target prim. Otherwise, uses the payload layer's defaultPrim.
    )
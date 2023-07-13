.. meta::
    :description: Universal Scene Description (USD) Python code snippet for creating an Xform prim and adding a Payload in Omniverse Kit in one step.
    :keywords: USD, Python, snippet, payload, CreatePayload, Kit Commands, Omniverse Kit

======================
Create a Payload
======================

The :code:`CreatePayload` command is a convenient wrapper that creates an Xform prim and adds a Payload to it all at once. If you don't need the two steps batched together, you may want to :doc:`add-payload` to an existing prim via Kit Commands or USD API.

Omniverse Kit Commands
----------------------
.. code-block:: python
    
    import omni.kit.commands
    import omni.usd
    from pxr import Sdf

    omni.kit.commands.execute("CreatePayload",
        usd_context=omni.usd.get_context(),
        path_to=Sdf.Path("/World/New/Prim/Path"), # Prim path for where to create the payload
        asset_path="C:/path/to/file.usd", # The file path to payload asset. Relative paths are accepted too.
        instanceable=False # The instanceable metadata value for the `path_to` prim
    )

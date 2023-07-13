.. meta::
    :description: Universal Scene Description (USD) Python code snippet for creating an Xform prim and adding a Reference in Omniverse Kit in one step.
    :keywords: USD, Python, snippet, reference, CreateReference, Kit Commands, Omniverse Kit

======================
Create a Reference
======================

The :code:`CreateReference` command is a convenient wrapper that creates an Xform prim and adds a Reference to it all at once. If you don't need the two steps batched together, you may want to :doc:`add-reference` to an existing prim via Kit Commands or USD API.

Omniverse Kit Commands
----------------------
.. code-block:: python
    
    import omni.kit.commands
    import omni.usd
    from pxr import Sdf

    omni.kit.commands.execute("CreateReference",
        path_to=Sdf.Path("/World/New/Prim/Path"), # Prim path for where to create the reference
        asset_path=r"C:/path/to/file.usd", # The file path to reference. Relative paths are accepted too.
        usd_context=omni.usd.get_context()
    )


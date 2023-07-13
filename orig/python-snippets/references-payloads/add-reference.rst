.. meta::
    :description: Universal Scene Description (USD) Python code snippets for adding a Reference to a prim.
    :keywords: USD, Python, snippet, reference, AddReference

======================
Add a Reference
======================

A `Reference <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-references>`_ is a composition arc that enables users to aggregate layers or assets onto a Stage. A Reference targets a prim from a layer and loads it and all of its descendants into a new namespace within the referencing layer. This snippet shows how to add a Reference to a prim. A single prim can have multiple References.

Omniverse Kit Commands
----------------------
.. code-block:: python
    
    import omni.kit.commands
    import omni.usd
    from pxr import Sdf

    omni.kit.commands.execute("AddReference",
        stage=omni.usd.get_context().get_stage(),
        prim_path=Sdf.Path("/World/Add/Reference/Here"), # an existing prim to add the reference to.
        reference=Sdf.Reference(r"C:/path/to/file.usd")
    )

USD API
-------
.. code-block:: python

    from pxr import Usd

    prim: Usd.Prim = stage.GetPrimAtPath("/World/my/prim")
    references: Usd.References = prim.GetReferences()
    references.AddReference(
        assetPath=r"C:/path/to/file.usd", 
        primPath="/World/some/target" # OPTIONAL: Reference a specific target prim. Otherwise, uses the referenced layer's defaultPrim.
    )
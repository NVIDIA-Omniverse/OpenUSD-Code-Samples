.. meta::
    :description: Universal Scene Description (USD) Python code snippets for adding a SubLayer composition arc.
    :keywords: USD, Python, snippet, SubLayer, composition, composition arc

======================
Add a SubLayer
======================

A `SubLayer <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-sublayers>`_ is a composition arc used to build `LayerStacks <https://graphics.pixar.com/usd/release/glossary.html#usdglossary-layerstack>`_. In a LayerStack, the Layer that includes SubLayers has the strongest opinion. From there, the SubLayers are ordered from strongest to weakest starting from top to bottom (or first to last) in the :code:`subLayers` list. This snippet shows how to create a new Layer and add it as a SubLayer.

Omniverse Kit Commands
----------------------
.. code-block:: python

    import omni.kit.commands


    omni.kit.commands.execute("CreateSublayer",
        layer_identifier=stage.GetRootLayer().identifier,
        # This example prepends to the subLayers list
        sublayer_position=0,
        new_layer_path=r"C:/path/to/sublayer.usd",
        transfer_root_content=False,
        # When True, it will create the layer file for you too.
        create_or_insert=True
    )

USD API
-------
.. code-block:: python

    from pxr import Sdf

    
    root_layer: Sdf.Layer = stage.GetRootLayer()
    sub_layer: Sdf.Layer = Sdf.Layer.CreateNew(r"C:/path/to/sublayer.usd")
    # You can use standard python list.insert to add the subLayer to any position in the list
    root_layer.subLayerPaths.append(sub_layer.identifier)
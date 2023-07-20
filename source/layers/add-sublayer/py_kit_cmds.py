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

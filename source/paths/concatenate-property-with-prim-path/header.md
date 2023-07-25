FIXME:

If you want to concatenate a property name with a Prim path, you can use `Sdf.Path.AppendProperty <https://graphics.pixar.com/usd/release/api/class_sdf_path.html#a94b67bfea8a8295271a32014b563d913>`. In this example, given `Sdf.Path("/World/MyMesh")` in `mesh_prim_path`, `points_attr_path` will contain `Sdf.Path("/World/MyMesh.points")`.
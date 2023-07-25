from pxr import Sdf, Usd

prim_path = Sdf.Path("/World/Hello")
prim: Usd.Prim = stage.GetPrimAtPath(prim_path)
if prim.IsValid():
    print("Prim exists!")
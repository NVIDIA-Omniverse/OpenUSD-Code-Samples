from pxr import Usd

prim: Usd.Prim = stage.GetPrimAtPath("/World/my/prim")
base: Usd.Prim = stage.GetPrimAtPath("/World/my/base")
specializes: Usd.Specializes = prim.GetSpecializes()
specializes.AddSpecialize(base.GetPath())
from pxr import Usd

# The base prim typically uses the "class" Specifier to designate that it
# is meant to be inherited and skipped in standard stage traversals
quadruped_class: Usd.Prim = stage.CreateClassPrim("/_class_Quadruped")
dog_prim: Usd.Prim = stage.GetPrimAtPath("/World/Dog")
inherits: Usd.Inherits = dog_prim.GetInherits()
inherits.AddInherit(quadruped_class.GetPath())
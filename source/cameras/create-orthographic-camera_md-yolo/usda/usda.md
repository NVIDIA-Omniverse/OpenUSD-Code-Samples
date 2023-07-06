# USDA 
```usda
def Xform "World"{
    def Camera "MyOrthoCam"{
        token projection = "orthographic"
        double3 xformOp:rotateYXZ = (0, -0, -0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateYXZ", "xformOp:scale"]
    }
}
```
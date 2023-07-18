import numpy
from pxr import Vt

my_array = numpy.array([(1,2,3),(4,5,6),(7,8,9)])
from_numpy = Vt.Vec3fArray.FromNumpy(my_array)
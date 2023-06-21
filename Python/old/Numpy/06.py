import numpy

a = numpy.array([1,2,3,4])
print("a:\n",a)
print("a.dtype:", a.dtype)

b = numpy.array([1.1,2.2,3.0])
print("b:\n", b)
print("b.dtype:", b.dtype)

c = numpy.array([1,1.2])
print("c:\n", c)
print("c.dtype:", c.dtype)

# 可以改变数据类型

a2 = numpy.array(a, dtype = numpy.float64)
print("a2:\n",a2)
print("a2.dtype:", a2.dtype)

b2 = numpy.array(b, dtype = numpy.int64)
print("b2:\n", b2)

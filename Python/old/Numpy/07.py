
import numpy

a = numpy.array([[1,2],[3,4]])
b = numpy.array([[5,6],[7,8]])

c1 = a+b
c2 = numpy.add(a,b)
d1 = a-b
d2 = numpy.subtract(a,b)
e1 = a*b
e2 = numpy.multiply(a,b)
f1 = a/b
f2 = numpy.divide(a,b)

sqrt_a = numpy.sqrt(a)

print("c1:\n",c1)
print("c2:\n",c2)
print("d1:\n",d1)
print("d2:\n",d2)
print("e1:\n",e1)
print("e2:\n",e2)
print("f1:\n",f1)
print("f2:\n",f2)
print("sqrt_a:\n",sqrt_a)
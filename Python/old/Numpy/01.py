import numpy

a = numpy.array([1,2,3])

print("a:",a)
print("type(a):", type(a))
print("a.shape:", a.shape)
# help(a.shape)
a = a.reshape((1,-1))
print(a.shape)

a = numpy.array([1,2,3,4,5,6])

a = a.reshape((3,-1))
print(a.shape)
print(a)

a = a.reshape((2,-1))
print(a.shape)
print("a:", a)
print("a[1][2]:", a[1][2])
a[1][2] = 66
print("a:",a)
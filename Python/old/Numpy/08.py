import numpy

# (3*3)
a = numpy.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
# (3*4)
b = numpy.array([[10,20,30,40],
                 [50,60,70,80],
                 [90,100,110,120]])
c1 = numpy.dot(a,b)
c2 = a.dot(b)

print("c1:\n",c1)
print("c2:\n",c2)
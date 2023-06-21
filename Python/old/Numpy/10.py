import numpy

a = numpy.array([[1,2,3,4],
                 [5,6,7,8]])

number = numpy.random.uniform(10,100)
print("number:", number)

new_a = numpy.tile(a,(2,3))
print("new_a:\n", new_a)

b = numpy.array([[5,10,1,3],
                 [6,8,1,0]])
sort_b = numpy.argsort(b)
sort_b_y = numpy.argsort(b, axis = 0)
print("sort_b:\n", sort_b)
print("sprt_b_y:\n", sort_b_y)
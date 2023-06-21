import numpy

a = numpy.array([[1,2,3,4],
                 [5,6,7,8]])

sum_a = numpy.sum(a)
sum_a_x = numpy.sum(a, axis=1)
sum_a_y = numpy.sum(a, axis=0)
print("sum_a:", sum_a)
print("sum_a_x:", sum_a_x)
print("sum_a_y:", sum_a_y)

mean_a = numpy.mean(a)
mean_a_x = numpy.mean(a, axis=1)
mean_a_y = numpy.mean(a, axis=0)
print("mean_a:", mean_a)
print("mean_a_x:", mean_a_x)
print("mean_a_y:", mean_a_y)

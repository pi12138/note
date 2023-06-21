import numpy

a = numpy.arange(3)
print("a:",a)
print("a.shape:",a.shape)

b = numpy.arange(1,7)
print("b:",b)
print("b.shape:", b.shape)

# 让数组c中第二列元素均加上10
c = numpy.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]])

# 下面4种写法效果类似
c[numpy.arange(3), 1] += 10
print("c:\n", c)

c[range(3), 1] += 10
print("c:\n",c)

c[[0,1,2], [1,1,1]] += 10
print("c:\n",c)

c[numpy.arange(3), [1,1,1]] += 10
print("c:\n", c)


# 获得所有大于10的数
result_index = c>10
print("result_index:\n", result_index)
print("c[result_index]:\n", c[result_index])
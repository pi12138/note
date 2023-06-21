import numpy

a = numpy.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12]])

b = numpy.array([1,2,3,4])

# 将b中的数据加到a上
# 1.使用for循环
for i in range(3):
    a[i,0:4] += b

print("a:\n", a)

# 2.使用tile()函数
a = a + numpy.tile(b,(3,1))
print("a:\n", a)

# 3.直接相加
a = a+b
print("a:\n", a)
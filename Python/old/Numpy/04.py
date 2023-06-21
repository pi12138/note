# indexing

import numpy

# 创建一个3*4的数组

a = numpy.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11]])

print(a.shape)
print("a:\n", a)

# 提取数组中成组的元素
b = a[-2:, 1:3]
print("b:\n", b)

# c和b一样
c = a[1:3, 1:3]
print("c:\n", c)

# 提取单个元素
print("a[1][1]:", a[1][1])
print("a[1,1]:", a[1,1])


# 注意下面两种写法,返回的shape有所不同
x = a[2,1:3]
print("x:\n",x)
print("x.shape:",x.shape)   # (2,)

y = a[2:3,1:3]
print("y:\n", y)
print("y.shape:",y.shape)   # (1,2)


"""
问题
  你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使
用复数空间。再或者是你仅仅需要使用复数来执行一些计算操作。
解决方案
  复数可以用使用函数 complex(real, imag) 或者是带有后缀 j 的浮点数来指定。
比如：
"""

a = complex(3, -4)
b = 3-5j

print(a)                    # > (3-4j)
print(b)                    # > (3-5j)


"""  对应的实部、虚部和共轭复数可以很容易的获取。就像下面这样："""

print(a.real)               # > 3.0
print(a.imag)               # > -4.0
print(a.conjugate())        # (3+4j)


"""  另外，所有常见的数学运算都可以工作："""

print(a+b)                  # >  (6-9j)
print(a-b)                  # > 1j
print(a*b)                  # > (-11-27j)
print(a/b)                  # > (0.8529411764705882+0.08823529411764708j)


"""  如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块："""

import cmath

print(cmath.sin(a))         # > (3.853738037919377+27.016813258003936j)
print(cmath.cos(a))         # > (-27.034945603074224+3.8511533348117775j)
print(cmath.exp(a))         # > (-13.128783081462158+15.200784463067954j)


"""
讨论
  Python 中大部分与数学相关的模块都能处理复数。比如如果你使用 numpy ，可以
很容易的构造一个复数数组并在这个数组上执行各种操作：
"""

import numpy

a = numpy.array([2+3j, 4+5j, 6-7j, 8+9j])

print(a)                    # > [2.+3.j 4.+5.j 6.-7.j 8.+9.j]
print(a+2)                  # > [ 4.+3.j  6.+5.j  8.-7.j 10.+9.j]
print(numpy.sin(a))         
# > [   9.15449915  -4.16890696j  -56.16227422 -48.50245524j
#  -153.20827755-526.47684926j 4008.42651446-589.49948373j]


"""
  Python 的标准数学函数确实情况下并不能产生复数值，因此你的代码中不可能会
出现复数返回值。比如：

    >>> import math
    >>> math.sqrt(-1)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: math domain error
    >>>
"""

"""
  如果你想生成一个复数返回结果，你必须显示的使用 cmath 模块，或者在某个支
持复数的库中声明复数类型的使用。比如：
"""

import cmath

print(cmath.sqrt(-1))           # > 1j
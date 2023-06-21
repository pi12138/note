"""
问题
  你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
解决方案
  Python 并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们。比如：
  float('inf'),float('-inf')代表正负无穷,float('nan')代表非数字
"""

a = float('inf')
b = float('-inf')
c = float('nan')

print(a)                  # > inf
print(b)                  # > -inf
print(c)                  # > nan
print(type(a))            # > <class 'float'>
print(type(1.0))          # > <class 'float'>


"""   为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数。比如："""

import math

print(math.isinf(a))      # > True
print(math.isinf(b))      # > True
print(math.isnan(c))      # > True


"""
讨论
  想了解更多这些特殊浮点值的信息，可以参考 IEEE 754 规范。然而，也有一些地
方需要你特别注意，特别是跟比较和操作符相关的时候。
  无穷大数在执行数学计算的时候会传播，比如：
"""

a = float('inf')

print(a+45)               # > inf
print(a*10)               # > inf
print(10/a)               # > 0.0


"""  但是有些操作时未定义的并会返回一个 NaN 结果。比如："""

a = float('inf')
b = float('-inf')

print(a/a)                # > nan
print(a+b)                # > nan


"""  NaN 值会在所有操作中传播，而不会产生异常。比如："""

c = float('nan')

print(c+23)               # > nan
print(c*10)               # > nan
print(c/2)                # > nan
print(math.sqrt(c))       # > nan


"""  NaN 值的一个特别的地方时它们之间的比较操作总是返回 False。比如："""

c = float('nan')
d = float('nan')

print(c == d)             # > False
print(c is d)             # > False


"""
  由于这个原因，测试一个 NaN 值得唯一安全的方法就是使用 math.isnan() ，也
就是上面演示的那样。 
  有时候程序员想改变 Python 默认行为，在返回无穷大或 NaN 结果的操作中抛出
异常。fpectl 模块可以用来改变这种行为，但是它在标准的 Python 构建中并没有被
启用，它是平台相关的，并且针对的是专家级程序员。可以参考在线的 Python 文档获
取更多的细节
"""


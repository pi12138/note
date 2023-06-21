"""
问题
  你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。或者
你可能需要写代码去计算在你的木工工厂中的测量值。
解决方案
  fractions 模块可以被用来执行包含分数的数学运算。比如：
"""

from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)

print(a)                        # > 5/4
print(b)                        # > 7/16

print(a+b)                      # > 27/16
print(a*b)                      # > 35/64

# 获取分子(numerator)/分母(denominator)
c = a*b

print(c)                        # > 35/64
print(c.numerator)              # > 35
print(c.denominator)            # > 64 

# 转化为浮点数
print(float(c))                 # > 0.546875

# 限制值的分母
print(c.limit_denominator(8))   # > 4/7

# 将浮点数转换为分数
x = 3.75
y = Fraction(*x.as_integer_ratio())

print(y)                        # > 15/4


"""
讨论
  在大多数程序中一般不会出现分数的计算问题，但是有时候还是需要用到的。比
如，在一个允许接受分数形式的测试单位并以分数形式执行运算的程序中，直接使用分
数可以减少手动转换为小数或浮点数的工作。
"""
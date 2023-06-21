# match()函数使用案例

import re

# help(re.match)
# Help on function match in module re:

# match(pattern, string, flags=0)
#     Try to apply the pattern at the start of the string, returning
#     a match object, or None if no match was found.

p = re.compile(r'\d+')

# help(p.match)
# Help on built-in function match:

# match(string=None, pos=0, endpos=9223372036854775807, *, pattern=None) method of _sre.SRE_Pattern instance
#     Matches zero or more characters at the beginning of the string.

# 上述两个match()函数的作用有所不同，函数参数也不同

str1 = "adsad1232a5asdas"

p1 = p.match(str1)
print(p1) 	# 此处返回None，因为match是从字符串开头开始查找，如果开头不匹配，则不会继续向下查找

p2 = p.match(str1, pos = 5, endpos = 10)
# 此处返回<_sre.SRE_Match object; span=(5, 9), match='1232'>
# 因为pos参数和endpos参数可以指定函数match()的查找的起始范围和结束范围，起始范围满足要求就
# 继续查找(如p2)；如果起始开头不匹配，则不会继续向下查找(如p3)
print(p2)
# print(str1[5])
# print(str1[10])
p3 = p.match(str1, pos = 4, endpos = 10)
print(p3)	# 此处打印None，因为"str1[4] = d"
# print(str1[4])
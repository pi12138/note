import re

str1 = '111222 a   asdada'
str2 = 'dhjasgd a   hsajgdj2223'
# help(re.match)
# match(pattern, string, flags=0)	注意此处match和下面match有所不同
p1 = re.compile(r"\d*")
p2 = re.compile(r"\D+")
p3 = re.compile(r"\s?")
# match(string=None, pos=0, endpos=9223372036854775807, *, pattern=None)
# help(p.match)
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# match可以制定查找的起始位置pos和结束位置endpos
m1 = p1.match(str1)
n1 = p1.match(str2)

m2 = p2.match(str1)
n2 = p2.match(str2)

m3 = p3.match(str1)
n3 = p3.match(str2)

print(m1)
print(n1)

print(m2)
print(n2)

print(m3)
print(n3)
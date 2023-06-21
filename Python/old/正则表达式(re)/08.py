import re

str1 = 'this is a string'

p = re.compile(r'([a-z]+) ([a-z]+)')

# help(p.findall)
# Help on built-in function findall:

# findall(string=None, pos=0, endpos=9223372036854775807, *, source=None) method of _sre.SRE_Pattern instance
#     Return a list of all non-overlapping matches of pattern in string.

p1 = p.findall(str1)
print(p1)
# print(p1.group(0))	没有group方法

for i in p1:
	print(i)
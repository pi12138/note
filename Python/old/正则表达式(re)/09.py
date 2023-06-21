import re

str1 = "this is a string"

p = re.compile(r'([a-z]+) ([a-z]+)')

# help(p.finditer)
# Help on built-in function finditer:

# finditer(string, pos=0, endpos=9223372036854775807) method of _sre.SRE_Pattern instance
#     Return an iterator over all non-overlapping matches for the RE pattern in string.

#     For each match, the iterator returns a match object.

p1 = p.finditer(str1)
# print(p1)	# <callable_iterator object at 0x0000021DE40FF780>
for i in p1:
	print(i)

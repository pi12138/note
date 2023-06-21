import re

# help(re.search)
# Help on function search in module re:

# search(pattern, string, flags=0)
#     Scan through string looking for a match to the pattern, returning
#     a match object, or None if no match was found.

p = re.compile(r'([a-z]+) ([a-z]+)')

# help(p.search)
# Help on built-in function search:

# search(string=None, pos=0, endpos=9223372036854775807, *, pattern=None) method of _sre.SRE_Pattern instance
#     Scan through string looking for a match, and return a corresponding match object instance.

#     Return None if no position in the string matches.
str1 = "this is a string"

p1 = p.search(str1)
print(p1)

p2 = p.search(str1, pos = 5, endpos = 10)
print(p2)
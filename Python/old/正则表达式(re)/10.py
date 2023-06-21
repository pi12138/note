import re

str1 = "hello 123 hello 456 hello 789"

p = re.compile(r'([a-zA-Z]+) ([0-9]+)')

# help(p.sub)
# Help on built-in function sub:

# sub(repl, string, count=0) method of _sre.SRE_Pattern instance
#     Return the string obtained by replacing the leftmost non-overlapping 
#     occurrences of pattern in string by the replacement repl.
repl = 'hello world'

p1 = p.sub(repl, str1)
print("str1:{0}".format(str1)) 
print("p1  :{0}".format(p1))   
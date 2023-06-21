import re


# help(re.compile)
str1 = "This is a string"

# re.I表示查找是不区分大小写
p = re.compile(r"([a-z]+) ([a-z]+)", re.I)

p1 = p.match(str1)

print(p1) 
print("p1.group(0):", p1.group(0))
print("p1.start(0):{0}, p1.end(0):{1}".format(p1.start(0), p1.end(0)))
print("p1.group(1):", p1.group(1))
print("p1.start(1):{0}, p1.end(1):{1}".format(p1.start(1), p1.end(1)))
print("p1.group(2):", p1.group(2))
print("p1.start(2):{0}, p1.end(2):{1}".format(p1.start(2), p1.end(2)))
print("p1.groups():", p1.groups())



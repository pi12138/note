# 正则函数比较

import re

# help(re.search) 扫描字符串寻找匹配的模式，返回匹配对象，如果没有找到匹配，则为None。
# help(re.findall)	返回字符串中所有不重叠匹配的列表。如果模式中存在一个或多个捕获组，返回
# 组列表;如果模式是这样，这将是一个元组列表有多个基团。结果中包含了空匹配。
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
# help(re.match)	尝试在字符串开头应用模式，返回匹配对象，如果没有找到匹配，则为None。
# help(re.sub)
# sub(pattern, repl, string, count=0, flags=0)
# 

str1 = 'hello hello hello'

re1 = re.search(r'l', str1)

re2 = re.findall(r'l', str1)

re3 = re.match(r'l', str1)

re4 = re.sub(r'l', 'm', str1)

print(re1)
print(re2)
print(re3)
print(re4)

# help(re1.group)
print(re1.group())

print(re1.start(), re1.end())


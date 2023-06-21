'''
match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置，使用 findall()方法去代替。比如：
'''

import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

pattern = re.compile(r'\d+\/\d+\/\d+')

result1 = pattern.match(text)
result2 = pattern.findall(text)

print(result1)
print(result2)
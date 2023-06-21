'''
在定义正则式的时候，通常会利用括号去捕获分组。比如：
'''

import re

pattern = re.compile(r'(\d+)+/(\d+)+/(\d+)')

text1 = '11/22/2018'
text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

result1 = pattern.match(text1)
# result2 = pattern.findall(text)

print(result1)
print(result1.group(0))
print(result1.group(1))
print(result1.group(2))
print(result1.group(3))
print(result1.groups())
month, day, year = result1.groups()
print("{0}-{1}-{2}".format(year, month, day))

print("---" * 20)
result2 = pattern.findall(text2)

# print(result2)
for i in result2:
    # print(i)
    month,day,year = i
    print("{0}-{1}-{2}".format(year,month,day))

'''
findall() 方法会搜索文本并以列表形式返回所有的匹配。如果你想以迭代方式返
回匹配，可以使用 finditer() 方法来代替，比如：
'''
print("---" * 20)
result3 = pattern.finditer(text2)

for i in result3:
    print(i.groups())

'''
讨论
关于正则表达式理论的教程已经超出了本书的范围。不过，这一节阐述了使用 re
模块进行匹配和搜索文本的最基本方法。核心步骤就是先使用 re.compile() 编译正则
表达式字符串，然后使用 match() , findall() 或者 finditer() 等方法。
当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 r'(\d+)/
(\d+)/(\d+)' 。这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。如果
不这样做的话，你必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)' 。
需要注意的是 match() 方法仅仅检查字符串的开始部分。它的匹配结果有可能并
不是你期望的那样。比如：
'''
result4 = pattern.match('11/27/2012abcdef')
print(result4)
print(result4.group())
'''
如果你想精确匹配，确保你的正则表达式以 $ 结尾，就像这么这样：
'''

new_pat = re.compile(r'(\d+)/(\d+)/(\d+)$')
result5 = new_pat.match('11/27/2012abcdef')
result6 = new_pat.match('11/27/2012')

print(result5)
# print(result5.group())
print(result6.group())

'''
最后，如果你仅仅是做一次简单的文本匹配/搜索操作的话，可以略过编译部分，
直接使用 re 模块级别的函数。比如：
>>> re.findall(r'(\d+)/(\d+)/(\d+)', text)
[('11', '27', '2012'), ('3', '13', '2013')]
>>>
但是需要注意的是，如果你打算做大量的匹配和搜索操作的话，最好先编译正则表
达式，然后再重复使用它。模块级别的函数会将最近编译过的模式缓存起来，因此并不
会消耗太多的性能，但是如果使用预编译模式的话，你将会减少查找和一些额外的处理
损耗。
'''
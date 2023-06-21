'''
对于复杂的匹配需要使用正则表达式和 re 模块。为了解释正则表达式的基本原理，
假设你想匹配数字格式的日期字符串比如 11/27/2012 ，你可以这样做：
'''
import re

date1 = '2018.11.22'
date2 = '11/22/2018'

result1 = re.match(r'\d+\.\d+\.\d+', date1)
result2 = re.match(r'\d+\/\d+\/\d+', date2)

print(result1)
print(result2)

'''
如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。比如：
'''
pattern = re.compile(r'\d+\.\d+\.\d+')
result3 = pattern.match(date1)
result4 = pattern.match(date2)

print(result3)
print(result4)
'''
问题
你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。

解决方案
string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，最好使用 re.split() 方法：
'''
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

# 使用空格符分割，分割结果不满意
l1 = line.split(' ')
print(l1)

# 使用正则表达式定制分割字符
l2 = re.split(r'[;,\s]\s*', line)
print(l2)

# 保留分割符号
l3 = re.split(r'([;,\s]\s*)', line)
print(l3)
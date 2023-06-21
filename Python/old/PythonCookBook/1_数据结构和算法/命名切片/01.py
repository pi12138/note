'''
问题
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。

解决方案
假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段
（比如文件或类似格式）：
'''


record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# print(len(record))
# print(record[20:23])
# print(record[31:37])
# help(slice)
#  slice(start, stop[, step])
#  |
#  |  Create a slice object.  This is used for extended slicing (e.g. a[0:10:2]).

first = slice(20,23)
second = slice(31,37)
cost = int(record[first]) * float(record[second])
print(cost)

# 第二种版本中，你避免了大量无法理解的硬编码下标，使得你的代码更加清晰可读
# 了。
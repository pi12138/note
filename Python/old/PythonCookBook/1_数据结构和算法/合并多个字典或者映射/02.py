'''
ChainMap 对于编程语言中的作用范围变量（比如 globals , locals 等）是非常有
用的。事实上，有一些方法可以使它变得简单：
'''
from collections import ChainMap

values = ChainMap()

values['x'] = 1
values['y'] = 2
print(values)

# add a new mapping
values2 = values.new_child()
values2['x'] = 10
values2['y'] = 20
print(values2)

# add a new mapping
values3 = values2.new_child()
values3['x'] = 100
values3['y'] = 200
print(values3)
print(values3['x'])


# discard last mapping
values4 = values3.parents
print(values4)
print(values4['x'])

# dicard last mapping
values5 = values4.parents
print(values5)
print(values5['x'])
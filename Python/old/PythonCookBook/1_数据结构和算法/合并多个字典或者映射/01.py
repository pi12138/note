'''
问题
现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某
些操作，比如查找值或者检查某些键是否存在。

解决方案
假如你有如下两个字典:
'''

a = {'x':1, 'z':2}
b = {'y':2, 'z':4}

from collections import ChainMap

c = ChainMap(a,b)
print(c['x'])   # from a
print(c['y'])   # from b
print(c['z'])   # from a

'''
讨论
一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并
不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重
新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的，
比如：
'''
print(len(c))
print(c.keys())
print(list(c.keys()))
print(c.values())
print(list(c.values()))

'''
如果出现重复键，那么第一次出现的映射值会被返回。因此，例子程序中的 c['z']
总是会返回字典 a 中对应的值，而不是 b 中对应的值。

对于字典的更新或删除操作总是影响的是列表中第一个字典。比如：
'''

c['z'] = 100
c['w'] = 'new_key'
del c['x']
# del c['y']    # 操作第二个字典数据，会报错
print("a:",a)
print("b:",b)

print("c:", c)
c = c.parents   # 会先丢弃在前面字典
print("c:", c)